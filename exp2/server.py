
import socket
import re

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(("0.0.0.0", 8080))

msg, client = s.recvfrom(1024)
msg = msg.decode()

words = {
    "tbh": "to be honest",
    "ig": "I guess",
    "tbf": "to be fair",
    "atm": "at the moment",
    "irl": "in real life",
    "lol": "laughing out loud",
    "asap": "as soon as possible",
    "omg": "oh my God",
    "ttyl": "talk to you later",
    "idk": "I don't know",
    "nvm": "never mind"
}

result = re.sub(
    r'\b(tbh|ig|tbf|atm|irl|lol|asap|omg|ttyl|idk|nvm)\b',
    lambda m: words[m.group().lower()],
    msg,
    flags=re.IGNORECASE
)

s.sendto(result.encode(), client)

s.close()
