import socket

HEADER = 1024 # Padrão do tamanho da mensagem
HOST = socket.gethostbyname(socket.gethostname()) #Host (coletado automaticamente)
PORTA = 5000 # Porta
ENDEREÇO = (HOST, PORTA) # Endereço do servidor
FORMATO = "utf-8" # Padrão do fomato das mensagens
MENSAGEM_DESCONEXÃO = "0" # Mensagem que desconecta o usuario

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Criação do soquete do servidor
servidor.bind(ENDEREÇO) # faz o bind e começa a "escutar" conexões

def start(): # Função para iniciar o servidor e receber mensagens
    print(f"[ESCUTANDO] O servidor está escutando em {HOST}")
    while True:
        msg, ender = servidor.recvfrom(HEADER)
        if msg == MENSAGEM_DESCONEXÃO:
            break
        print(f"[{ender}]: {msg.decode(FORMATO)}")


print("[INICIANDO] Iniciando conexão...")
start()