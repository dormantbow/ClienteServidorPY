import socket

HOST = "35.239.100.64"
PORT = 80

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    message = input("Digite uma mensagem (ou 'exit' para sair): ")
    client_socket.send(message.encode())
    if message.strip().lower() == "exit":
        print("Encerrando conexão.")
        break
    response = client_socket.recv(1024).decode()
    print(f"Resposta do servidor: {response.strip()}")

client_socket.close()
