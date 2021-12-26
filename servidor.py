import socket
import threading

HEADER = 1024 # Padrão do tamanho da mensagem
HOST = socket.gethostbyname(socket.gethostname()) #Host (coletado automaticamente)
PORTA = 5000 # Porta
ENDEREÇO = (HOST, PORTA) # Endereço do servidor
FORMATO = "utf-8" # Padrão do fomato das mensagens
MENSAGEM_DESCONEXÃO = "0" # Mensagem que desconecta o usuario

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Criação do soquete do servidor
servidor.bind(ENDEREÇO) # faz o bind para começar a escutar

CLIENTES = [] # Lista de usuarios que conectam no servidor

def addCliente(con, ender, username): # Função para adicionar usuarios a lista CLIENTES
    cliente = {
        "conexão": con,
        "endereço": ender,
        "username": username 
        }
    CLIENTES.append(cliente)

def removeCliente(con, ender): # Função para remover usuarios da lista CLIENTES
    for i in range(len(CLIENTES) + 1):
        if CLIENTES[i]["conexão"] == con and CLIENTES[i]["endereço"] == ender:
            print("Cliente", CLIENTES[i]["username"], " removido")
            CLIENTES.pop(i)
            break

def broadcast(mensagem, endereço, username): # Função para enviar uma mensagem a todos os usuarios
    if len(CLIENTES) <= 1:
        pass
    else:
        msg = f"[{username}]: {mensagem}"
        for cliente in CLIENTES:
            if endereço == cliente["endereço"]:
                pass
            else:
                cliente["conexão"].send(msg.encode(FORMATO))

def broadcast_con(endereço, username): # Função para enviar que um usuario entrou
    if len(CLIENTES) <= 1:
        pass
    else:
        msg = f"[NOVA CONEXÂO] {username} conectado"
        for cliente in CLIENTES:
            if endereço == cliente["endereço"]:
                pass
            else:
                cliente["conexão"].send(msg.encode(FORMATO))
                

def client_handle(con, ender): # Função para receber as mensagens do cliente
    username = con.recv(HEADER).decode()

    addCliente(con, ender, username)

    print(f"[NOVA CONEXÃO] {username} conectado")
    broadcast_con(ender, username)

    conectado = True
    while conectado:
        mensagem = con.recv(HEADER).decode(FORMATO)

        if mensagem == MENSAGEM_DESCONEXÃO:
            print(f"[{username}] !!SAIU!!")
            broadcast("!!SAIU!!", ender, username)
            removeCliente(con, ender)
            conectado = False
        else:
            print(f"[{username}] {mensagem}")
            broadcast(mensagem, ender, username)
            

            
    con.close()

def start(): # Função para iniciar o servidor e receber clientes
    print(f"[ESCUTANDO] O servidor está escutando em {HOST}")
    servidor.listen() # O servidor está escutando
    while True:
        con, ender = servidor.accept() # O servidor se conecta com o cliente
        thread = threading.Thread(target=client_handle, args=(con, ender))
        thread.start()
        print(f"[CONEXÕES ATIVAS] {threading.active_count() - 1}")

print("[INICIANDO] Iniciando conexão...")
start()