'''

~~~ Coded by sidi @ Oxyde Development (https://oxyde.dev) ~~~

MIT License

Copyright (c) 2021 sidi69

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


~~~ Coded by sidi @ Oxyde Development (https://oxyde.dev) ~~~

'''
import requests, tkinter as tk, concurrent.futures, os, time, json, uuid
from tkinter import filedialog
from colorama import Fore, Back, Style, init
import threading
import datetime

resultsFolder = 'Results'
folders = ['HTTP', 'SSL', 'Socks4', 'Socks5']
checkerFolder = os.path.join(resultsFolder, 'Checker')
scraperFolder = os.path.join(resultsFolder, 'Scraper')

if not os.path.exists(resultsFolder):
    os.mkdir(resultsFolder)
    os.mkdir(os.path.join(resultsFolder, 'Checker'))
    os.mkdir(os.path.join(resultsFolder, 'Scraper'))

    for folder in folders:
        os.mkdir(os.path.join(checkerFolder, folder))
        os.mkdir(os.path.join(scraperFolder, folder))


def menu():
    clear()
    os.system(f'title ProxyAIO ~ Coded by sidi for Oxyde Development')

    print(Fore.RED + "                                                                                          ")
    print("                            ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗ █████╗ ██╗ ██████╗ ")
    print("                            ██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝██╔══██╗██║██╔═══██╗")
    print("                            ██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝ ███████║██║██║   ██║")
    print("                            ██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝  ██╔══██║██║██║   ██║")
    print("                            ██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║   ██║  ██║██║╚██████╔╝")
    print("                            ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝ ")
    print("                            ")
    print(Fore.YELLOW + "                                                          Coded by sidi | Oxyde Development")

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def scrape():
    clear()
    os.system(f'title [Scraper Module] ProxyAIO ~ Coded by sidi for Oxyde Development')
    print(f"{Fore.RED + Style.BRIGHT}[!]{Fore.YELLOW + Style.BRIGHT} Proxy Type:")
    print("\n")
    print(f"{Fore.RED + Style.BRIGHT}[1]{Fore.YELLOW + Style.BRIGHT} HTTP")
    print(f"{Fore.RED + Style.BRIGHT}[2]{Fore.YELLOW + Style.BRIGHT} SSL")
    print(f"{Fore.RED + Style.BRIGHT}[3]{Fore.YELLOW + Style.BRIGHT} Socks4")
    print(f"{Fore.RED + Style.BRIGHT}[4]{Fore.YELLOW + Style.BRIGHT} Socks5")
    print(f"{Fore.RED + Style.BRIGHT}[Other]{Fore.YELLOW + Style.BRIGHT} Exit")
    print("\n")
    proxyType = input(f"{Fore.RED + Style.BRIGHT}[Console]{Fore.YELLOW + Style.BRIGHT} Input: ")
    
    if proxyType == '1' or proxyType == '2':
        proxyType = 'http'
    elif proxyType == '3':
        proxyType = 'socks4'
    elif proxyType == '4':
        proxyType = 'socks5'
    else:
        menu()

    now = datetime.datetime.now()
    timeFormatted = now.strftime("%Y-%m-%d %H;%M")

    scrapedList = requests.get(f"https://api.proxyscrape.com/?request=getproxies&proxytype={proxyType}&timeout=10000&country=all")

    outputFile = open(f"{os.getcwd()}\\Results\\Scraper\\{proxyType.upper()}\\{timeFormatted}.txt", "wb").write(scrapedList.content)

    print(f"{Fore.RED + Style.BRIGHT}[Console]{Fore.YELLOW + Style.BRIGHT} Scraping done, redirecting to checker module...")

    time.sleep(5)
    menu()

def check(proxy, proxyType):
    proxies = {'http' : proxyType + '://' + proxy}
    try:
        r = requests.get("http://icanhazip.com/", proxies = proxies)
        outputFileChecker = open(f"{os.getcwd()}\\Results\\Checker\\{proxyType.upper()}\\{timeFormatted}.txt", "a+")
        outputFileChecker.write(f"{proxy[ : -1]}\n")
        return Fore.GREEN + "ALIVE~: " + proxy[ : -1]
    except Exception as e:
        return Fore.RED + "DEAD~: " + proxy[ : -1]

CPM1 = 0
CPM = 0

def cpm_():
    global CPM1, CPM
    CPM = CPM1
    CPM1 = 0
    time.sleep(1)
    threading.Thread(target=cpm_, args=()).start()


menu()

init()
root = tk.Tk()
root.withdraw()

print("\n")
print(f"{Fore.RED + Style.BRIGHT}[!]{Fore.YELLOW + Style.BRIGHT} Logged in as root!")
print("\n")
print(f"{Fore.RED + Style.BRIGHT}[!]{Fore.YELLOW + Style.BRIGHT} Modules:")
print(f"{Fore.RED + Style.BRIGHT}[1]{Fore.YELLOW + Style.BRIGHT} Proxy Scraper")
print(f"{Fore.RED + Style.BRIGHT}[2]{Fore.YELLOW + Style.BRIGHT} Proxy Checker")
print("\n")
choice = input(f"{Fore.RED + Style.BRIGHT}[Console]{Fore.YELLOW + Style.BRIGHT} Input: ")
if choice == '1':
    scrape()

lines = []
checked = []
hits = []
bad = []

clear()
os.system(f'title [Checker Module] ProxyAIO ~ Coded by sidi for Oxyde Development')
print(f"{Fore.RED + Style.BRIGHT}[!]{Fore.YELLOW + Style.BRIGHT} Proxy Type:")
print("\n")
print(f"{Fore.RED + Style.BRIGHT}[1]{Fore.YELLOW + Style.BRIGHT} HTTP")
print(f"{Fore.RED + Style.BRIGHT}[2]{Fore.YELLOW + Style.BRIGHT} SSL")
print(f"{Fore.RED + Style.BRIGHT}[3]{Fore.YELLOW + Style.BRIGHT} Socks4")
print(f"{Fore.RED + Style.BRIGHT}[4]{Fore.YELLOW + Style.BRIGHT} Socks5")
print(f"{Fore.RED + Style.BRIGHT}[Other]{Fore.YELLOW + Style.BRIGHT} Exit")
print("\n")

proxyType = input(f"{Fore.RED + Style.BRIGHT}[Console]{Fore.YELLOW + Style.BRIGHT} Input: ")

if proxyType == '1' or proxyType == '2':
    proxyType = 'http'
elif proxyType == '3':
    proxyType = 'socks4'
elif proxyType == '4':
    proxyType = 'socks5'
else:
    menu()

file_path = filedialog.askopenfilename(title = "Open Proxy File.")

with open(file_path, 'r') as f:
    for proxy in f:
        lines.append(proxy)

print(f"{Fore.RED + Style.BRIGHT}[Console]{Fore.YELLOW + Style.BRIGHT} Loaded", len(lines), "lines.")
threads = int(input(f"{Fore.RED + Style.BRIGHT}[Console]{Fore.YELLOW + Style.BRIGHT} Number of Threads(max. 500): "))

cpm_()

now = datetime.datetime.now()
timeFormatted = now.strftime("%Y-%m-%d %H;%M")

with open(file_path, 'r') as proxies:
    with concurrent.futures.ThreadPoolExecutor(max_workers = threads) as executor:
        results = [executor.submit(check, proxy, proxyType) for proxy in proxies]
            
        for f in concurrent.futures.as_completed(results):
            checked.append(proxy)
            if "ALIVE~:" in f.result():
                CPM1+=1
                hits.append(proxy)

            elif "DEAD~:" in f.result():
                CPM1+=1
                bad.append(proxy)

            os.system(f'title [Checker Module] Threads: {threads} - Checked: {len(checked)}/{len(lines)} - Hits: {len(hits)} - Bad: {len(bad)} - CPM: {CPM1*60}')
            print(f.result())
        
        print(f"{Fore.RED + Style.BRIGHT}[Console]{Fore.YELLOW + Style.BRIGHT} Done Checking.")
