import socket
import threading

HEADER = 1024 # Padrão do tamanho da mensagem
HOST = socket.gethostbyname(socket.gethostname()) #Host (coletado automaticamente)
PORTA = 5000 # Porta
FORMATO = "utf-8" # Padrão do fomato das mensagens
MENSAGEM_DESCONEXÃO = "0" # Mensagem que desconecta o usuario
ENDEREÇO = (HOST, PORTA) # Endereço do cliente

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Criação do soquete do servidor
cliente.connect(ENDEREÇO) # O cliente se conecta com o servidor

username = input("Digite seu nome: ") # O usuario digita seu nome
cliente.send(username.encode(FORMATO)) # Envia o nome do usuario

def enviar(mensagem): # Função para enviar mensagem
    cliente.send(mensagem.encode(FORMATO))

def receber(): # Função para receber mensagem
    while conectado:
        print(cliente.recv(HEADER).decode(FORMATO))

conectado = True
while conectado: # Loop para enviar e receber mensagens e verificar se o usuario saiu
    receive = threading.Thread(target=receber)
    receive.start()

    mensagem = input()
    send = threading.Thread(target=enviar, args=(mensagem,))
    send.start()
    
    if mensagem == MENSAGEM_DESCONEXÃO:
        conectado = False

