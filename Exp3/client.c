
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <pthread.h>

int s;

void *receive_msg(void *arg) {
    char msg[1024];
    int n;

    while ((n = recv(s, msg, sizeof(msg) - 1, 0)) > 0) {
        msg[n] = '\0';
        printf("\nReceived: %s\n", msg);
        printf("Enter message: ");
        fflush(stdout);
    }

    return NULL;
}

int main() {
    struct sockaddr_in server;
    pthread_t t;
    char msg[1024];

    s = socket(AF_INET, SOCK_STREAM, 0);

    server.sin_family = AF_INET;
    server.sin_port = htons(8080);
    inet_pton(AF_INET, "127.0.0.1", &server.sin_addr);

    connect(s, (struct sockaddr *)&server, sizeof(server));

    printf("Connected to chat server!\n");

    pthread_create(&t, NULL, receive_msg, NULL);

    while (fgets(msg, sizeof(msg), stdin) != NULL) {
        send(s, msg, strlen(msg), 0);
    }

    close(s);
    return 0;
}
