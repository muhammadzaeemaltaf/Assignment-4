import socket
from _thread import *
import pickle
from game import Game

server = "192.168.0.114"
# server = "192.168.100.164"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0

def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games:
                game = games[gameId]
                if not data:
                    break
                else:
                    if data == "reset":
                        game.reset()
                    elif data != "get":
                        game.play(p, data)

                    reply = game
                    conn.sendall(pickle.dumps(reply))
            else:
                break    
        except Exception as e:
            print(f"Error: {e}")
            break

    print("Lost connection")
    print("Closing game", gameId)
    try:
        del games[gameId]
        print("Closing game", gameId)
    except:
        pass

    idCount -= 1
    conn.close()    


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1) // 2

    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating new game...")
    else:
        games[gameId].ready = True
        p = 1


    start_new_thread(threaded_client, (conn, p, gameId))
