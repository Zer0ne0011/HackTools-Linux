import os

os.system("clear")

def capa():
    print("""
 /$$$$$$                       /$$               /$$ /$$
|_  $$_/                      | $$              | $$| $$
  | $$   /$$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$ | $$| $$
  | $$  | $$__  $$ /$$_____/|_  $$_/   |____  $$| $$| $$
  | $$  | $$  \ $$|  $$$$$$   | $$      /$$$$$$$| $$| $$
  | $$  | $$  | $$ \____  $$  | $$ /$$ /$$__  $$| $$| $$
 /$$$$$$| $$  | $$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$| $$
|______/|__/  |__/|_______/    \___/   \_______/|__/|__/

by Zer0ne""")

def instalar():
    print("[*] Baixando nmap")
    print()
    os.system("apt install nmap -y")
    os.system("clear")
    print("[*] Baixando sqlmap")
    print()
    os.system("apt install sqlmap -y")
    os.system("clear")
    print("[*] Baixando gobuster")
    print()
    os.system("apt install gobuster -y")
    os.system("clear")
    print("[*] Baixando subfinder")
    print()
    os.system("apt install subfinder -y")
    os.system("clear")
    print("[*] Baixando unzip")
    print()
    os.system("apt install unzip -y")
    os.system("clear")
    print("[*] Baixando clang")
    print()
    os.system("apt install clang -y")
    os.system("clear")
    print("[*] Baixando o nslookup")
    print()
    os.system("apt install dnsutils -y")
    os.system("clear")
    print("[*] Baixando o golang")
    print()
    os.system("apt install golang -y")
    os.system("clear")
    
    print("[*] Baixando cariddi")
    print()
    os.system("go install -v github.com/edoardottt/cariddi/cmd/cariddi@latest")
    os.system("clear")
    print("[*] Baixando subzy")
    print()
    os.system("go install -v github.com/PentestPad/subzy@latest")
    os.system("clear")
    print("[*] Baixando httpx")
    print()
    os.system("go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest")
    os.system("clear")
   
    print("[*] Setando ferramentas...")
    os.system("clang ddos.c -o ddos")
    os.chdir(os.path.expanduser("~/go/bin"))
    os.system("mv * /usr/local/bin")
    
capa()
print()
instalar()
