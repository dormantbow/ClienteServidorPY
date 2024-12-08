import socket

HOST = "0.0.0.0"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Servidor escutando na porta {PORT}...")

conn, addr = server_socket.accept()
print(f"Conexão estabelecida com {addr}")

while True:
    data = conn.recv(1024).decode()
    if data.strip().lower() == "exit":
        print("Conexão encerrada pelo cliente.")
        break
    print(f"Mensagem recebida: {data.strip()}")
    conn.send(data.encode())

conn.close()
server_socket.close()
