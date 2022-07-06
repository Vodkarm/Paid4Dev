import os, requests, time
from threading import Thread

os.system("")

def open(url, devid, campid, func):
    def _():
        n = 0
        time.sleep(0.5)
        while True:
            time.sleep(0.1)
            n += 0.1
            print(f"Link will be opened in 3seconds: {round(n, 1)}s/3s", end = "\r")
            if n >= 3:
                os.system("start " + url)
                requests.get("https://api.adskit.cf/earn/?id=" + str(devid) + "&ip=" + requests.get("https://api.ipify.org").text + "&campid=" + str(campid))
                func()
                break
    Thread(target = _).start()

class init():
    def start(func, devid):
        os.system('cls && title Hey !' if os.name == "nt" else 'clear')
        print("Hi! This developer decided to get paid thanks to AdsKit.\nNobody likes the ads even this developer, however this program took time to be developed, thanks for your understanding.")
        print()
        input("Press enter if you understand...")
        os.system('cls && title Powered by AdsKit 🚀' if os.name == "nt" else 'clear')
        print("Ad Title: " + doNotUse.title(devid) + "\nAd Description: " + doNotUse.description(devid))
        print()
        doNotUse.link(devid, func)

class doNotUse():
    global r
    r = requests.get("https://api.adskit.cf/ad/")
    def title(devid):
        if requests.get("https://api.adskit.cf/check/?devid=" + str(devid)).text == "True":
            return r.json()["title"]
        else:
            return 'invalid devid'
    def description(devid):
        if requests.get("https://api.adskit.cf/check/?devid=" + str(devid)).text == "True":
            return r.json()["desc"] + u" - \u001b[1m\u001b[31m Powered by AdsKit \u001b[0m"
        else:
            return 'invalid devid'
    def link(devid, func):
        if requests.get("https://api.adskit.cf/check/?devid=" + str(devid)).text == "True":
            open(r.json()["link"], devid, r.json()["campid"], func)
            return r.json()["link"]
        else:
            return 'invalid devid'
