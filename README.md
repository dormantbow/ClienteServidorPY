# Comunicação entre Processos com Sockets em C e Python

## 📌 Objetivo
Este projeto tem como finalidade demonstrar a comunicação entre processos via sockets, utilizando o protocolo TCP/IP, em dois exemplos: um totalmente em C e outro em Python.

## 🌐 Contexto
- O **servidor** é executado em uma máquina virtual (VM) configurada no **Google Cloud**.
- O **cliente** é executado localmente na máquina do aluno.
- A comunicação entre cliente e servidor ocorre via **internet**, utilizando **sockets TCP**.

## 🧪 Cenários Implementados

### 🟦 Exemplo 1: Cliente-Servidor em C
- O servidor em C escuta na porta `80`, aceita conexões de múltiplos clientes e responde a cada mensagem recebida.
- O cliente em C se conecta ao servidor, permite entrada contínua de mensagens e encerra a conexão ao digitar `exit`.

### 🟨 Exemplo 2: Cliente-Servidor em Python
- O servidor em Python escuta na porta `5000`, recebe e ecoa mensagens.
- O cliente em Python envia mensagens digitadas pelo usuário e exibe as respostas. Conexão encerrada ao digitar `exit`.

## 🔄 Alterações Realizadas

### C
- **Servidor (server.c):** Adicionado loop para processar múltiplas mensagens de um mesmo cliente até o envio de `exit`.
- **Cliente (cliente.c):** Adicionado loop para entrada de mensagens do usuário. Envio de `exit` encerra a comunicação.

### Python
- **Servidor (server.py):** Verifica se a mensagem recebida é `exit` para encerrar a conexão.
- **Cliente (cliente.py):** Loop contínuo de envio/recebimento de mensagens. Digitar `exit` finaliza a execução.

## ☁️ Configuração do Google Cloud
1. Criar uma VM Linux (ex: Ubuntu) no Google Cloud.
2. Instalar dependências:
   - Para C: `sudo apt install gcc`
   - Para Python: `sudo apt install python3`
3. Configurar o **firewall** da VM para permitir tráfego na(s) porta(s) usada(s): `80` (C) e `5000` (Python).
4. Subir os códigos do servidor e executar via terminal:
   - C: `gcc server.c -o server && ./server`
   - Python: `python3 server.py`

## 🖥️ Execução

### Cliente (C ou Python)
Execute localmente:
```bash
# Cliente em C
gcc cliente.c -o cliente && ./cliente

# Cliente em Python
python3 cliente.py
