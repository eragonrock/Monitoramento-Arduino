import socket #Biblioteca para conexao por sockets
import os     #Biblioteca que permitem que você interferencia com o SO subjacente em que o Python está sendo executado para o uso de funções corelacionadas ao SO
 
HOST = raw_input("Digite o IP do servidor:") #Campo de IP do servidor
PORTA = 7000                                 #Porta destinada para a comunicação
 
tcpSOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Criação do socket
destinoCONEXAO = (HOST, PORTA)
tcpSOCKET.connect(destinoCONEXAO) #Solicitacao de conexao ao servidor
 
os.system("clear")
print "|====================================================|"
print "|       Monitoramento de ambiente via arduino        |"
print "|====================================================|"
print "| Digite 1 para leitura de luminosidade              |"
print "| Digite 2 para leitura de temperatura               |"
print "| Digite SAIR para teminar a conexao                 |"
print "|====================================================|" 

dados = raw_input("Opcao: ") #Recebmento da opcao desejada

while dados!='SAIR':
         
    if dados=='1':
        tcpSOCKET.send (dados)                                     #Envio ao servidor da opcao desejada, no caso a 1
        print "Insidencia de luminosidade: ", tcpSOCKET.recv(1024) #Recebmento, proviniente do servidor, da leitura respectiva a opcao desejada, no caso a luminosidade
        
    if dados=='2':
        tcpSOCKET.send (dados)                                     #Envio ao servidor da opcao desejada, no caso a 2
        print "Temperatura: ", tcpSOCKET.recv(1024)                #Recebmento, proviniente do servidor, da leitura respectiva a opcao desejada, no caso a temperatura
        
    if dados!='1' and dados!='2': 
        print "Opcao invalida, por favor digite somente as opcoes exposta no menu"
    
    dados = raw_input("Opcao: ")

tcpSOCKET.close()