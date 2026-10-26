
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <pthread.h>
#include <stdint.h>

int clients[10], count = 0;
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;

void *handle(void *arg) {
    int s = (int)(intptr_t)arg;
    char msg[1024];
    int n, i;

    while ((n = recv(s, msg, sizeof(msg), 0)) > 0) {
        pthread_mutex_lock(&lock);

        for (i = 0; i < count; i++) {
            if (clients[i] != s)
                send(clients[i], msg, n, 0);
        }

        pthread_mutex_unlock(&lock);
    }

    pthread_mutex_lock(&lock);
    for (i = 0; i < count; i++) {
        if (clients[i] == s) {
            clients[i] = clients[count - 1];
            count--;
            break;
        }
    }
    pthread_mutex_unlock(&lock);

    close(s);
    return NULL;
}

int main() {
    int server, c;
    struct sockaddr_in addr, client;
    socklen_t len = sizeof(client);
    pthread_t t;

    server = socket(AF_INET, SOCK_STREAM, 0);

    addr.sin_family = AF_INET;
    addr.sin_port = htons(8080);
    addr.sin_addr.s_addr = INADDR_ANY;

    bind(server, (struct sockaddr *)&addr, sizeof(addr));
    listen(server, 10);

    printf("Chat server started...\n");

    while (1) {
        c = accept(server, (struct sockaddr *)&client, &len);

        pthread_mutex_lock(&lock);
        if (count < 10)
            clients[count++] = c;
        else {
            close(c);
            pthread_mutex_unlock(&lock);
            continue;
        }
        pthread_mutex_unlock(&lock);

        pthread_create(&t, NULL, handle, (void *)(intptr_t)c);
        pthread_detach(t);
    }

    close(server);
    return 0;
}
