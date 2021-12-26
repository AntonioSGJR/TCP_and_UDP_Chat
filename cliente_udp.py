import socket

HEADER = 1024 # Padrão do tamanho da mensagem
HOST = socket.gethostbyname(socket.gethostname()) #Host (coletado automaticamente)
PORTA = 5000 # Porta
FORMATO = "utf-8" # Padrão do fomato das mensagens
MENSAGEM_DESCONEXÃO = "0" # Mensagem que desconecta o usuario
ENDEREÇO = (HOST, PORTA) # Endereço do cliente

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Criação do soquete do servidor 

def enviar(mensagem): # Função para enviar mensagem
    cliente.sendto(mensagem.encode(FORMATO), ENDEREÇO)

conectado = True
while conectado: # Loop para enviar mensagens e verificar se o usuario saiu
    mensagem = input()
    enviar(mensagem)
    
    if mensagem == MENSAGEM_DESCONEXÃO:
        conectado = False

