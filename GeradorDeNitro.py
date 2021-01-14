
import requests
import random
import string
from time import sleep
prox = list()
o9 = 0
prox.append(None)
print('\n \033[1;31mcriador por: \033[1;36mJS\n')
optsproxy = input('\033[1;33m você deseja adicionar uma proxy?\n não é obrigatório mas é recomendado S / N: \033[1;0m').upper()
if optsproxy == 'S':
    f2 = int(input(' \033[1;31mATENÇÃO! AS PROXYS DEVEM SER HTTPS!\033[1;33m\n quantas proxies você deseja adicionar? \033[1;0m'))
    for _ in range(f2):
        o9 += 1
        p1 = input(f'\033[1;36m proxy número {o9} : \033[1;0m')
        p2 = input(f'\033[1;36m qual e a porta da proxy {p1} : \033[1;0m')
        prox.append(p1 + f':{p2}')
        print(' \033[1;35mlista de proxy:', prox)
elif optsproxy == 'N':
    sleep(0.2)
else:
    print('\033[1;31m essa opção não existe!\033[m')
    exit()

users = ['Mozilla / 5.0 (Windows NT 10.0; WOW64) AppleWebKit / 537.36 (KHTML, como Gecko) Chrome / 72.0.3626.121 Safari / 537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36', 'Mozilla / 5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36 (KHTML, como Gecko) Chrome / 64.0.3282.140 Safari / 537.36 Edge / 18.17763', 'Mozilla / 5.0 (Windows NT 6.1; WOW64; rv: 54.0) Gecko / 20100101 Firefox / 54.0', 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1', 'Mozilla / 5.0 (Linux; Android 6.0.1; RedMi Note 5 Build / RB3N5C; wv) AppleWebKit / 537.36 (KHTML, como Gecko) Versão / 4.0 Chrome / 68.0.3440.91 Mobile Safari / 537.36']
proxe = random.choice(prox)
users1 = random.choice(users)
while True:
    gift = ''.join(random.choice(string.digits + string.ascii_letters)for _ in range(24))
    print(f'\033[1;34m ip proxy ( \033[1;36m{proxe} \033[1;34m)\033[m')
    print(f' \033[1;32mUser-Agent - \033[1m\n \033[7m{users1}\n\033[m')
    url2 = f'https://discordapp.com/api/v6/entitlements/gift-codes/{gift}'
    heads = {'User-Agent':users1}
    sleep(0.7)
    
    try:
        res = requests.get(url2, proxies={'https':proxe}, headers=heads)
        if res.status_code == 200:
            print(f' \033[1;m{gift} \033[1;32mvalido!\033[m\n')
        elif res.status_code == 404:
            print(f' \033[1;m{gift} \033[1;31minvalido\033[m\n')
        else:
            print(f'\033[1;33m status code | {res.status_code} | \033[m\n')
            sleep(5)
            proxe = random.choice(prox)
            users1 = random.choice(users)
            sleep(1)
    except:
        print(f' \033[7merro de proxy ({proxe})\033[m')
        sleep(0.3)
        proxe = random.choice(prox)
        
    
