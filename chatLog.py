server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'rennahweng' #username
token = 'oauth:3yunmu22zkam0nexhl7moh89uyvmk4' #https://twitchapps.com/tmi/ to request an auth token 
channel = '#gernaderjake'

import socket
sock = socket.socket()
sock.connect((server, port))

sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

resp = sock.recv(2048).decode('utf-8')

#---------------------------------------------------------------------------------------------
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s — %(message)s',
                    datefmt='%Y-%m-%d_%H:%M:%S',
                    handlers=[logging.FileHandler('chat.log', encoding='utf-8')])
logging.info(resp)

#continous extracting data into chat.log
while True:
    resp = sock.recv(2048).decode('utf-8')
    if resp.startswith('PING'):
        sock.send("PONG\n".encode('utf-8'))
    elif len(resp) > 0:
        logging.info(resp)

# tail -f chat.log 
