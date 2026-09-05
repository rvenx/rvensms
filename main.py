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
        self.country_codes = ["90", "1", "44", "49", "33", "7"]
        self.selected_code_index = 0
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
        print(Fore.GREEN + "[1]" + Style.RESET_ALL + f" Alan Kodu Seçimi: " + Fore.YELLOW + f"+{self.country_codes[self.selected_code_index]}")
        print(Fore.GREEN + "[2]" + Style.RESET_ALL + f" Hedef Numara   : " + Fore.YELLOW + (self.phone_number if self.phone_number else "Girilmedi"))
        print(Fore.GREEN + "[3]" + Style.RESET_ALL + f" Gönderilecek Adet: " + Fore.YELLOW + (str(self.target_count) if self.target_count > 0 else "Sınırsız"))
        print(Fore.GREEN + "[4]" + Style.RESET_ALL + f" SALDIRIYI BAŞLAT")
        print(Fore.GREEN + "[5]" + Style.RESET_ALL + f" Çıkış\n")
        print(Fore.MAGENTA + "--------------------------------------------------")

    def run(self):
        self.show_intro()
        while True:
            self.render_menu()
            choice = input(Fore.CYAN + "Seçiminiz (1-5): " + Style.RESET_ALL).strip()
            
            if choice == "1":
                print(Fore.YELLOW + "\n1) +90 (TR)  2) +1 (US)  3) +44 (UK)  4) +49 (DE)  5) +33 (FR)  6) +7 (RU)")
                try:
                    sec = int(input(Fore.CYAN + "Seçim (1-6): " + Style.RESET_ALL).strip())
                    if 1 <= sec <= len(self.country_codes):
                        self.selected_code_index = sec - 1
                except:
                    pass
            elif choice == "2":
                num = input(Fore.CYAN + "\nTelefon Numarası (Başında 0 yok): " + Style.RESET_ALL).strip()
                if num.isdigit() and len(num) >= 7:
                    self.phone_number = num
            elif choice == "3":
                try:
                    adet = int(input(Fore.CYAN + "\nKaç adet atılsın? (0 = Sınırsız): " + Style.RESET_ALL).strip())
                    self.target_count = adet if adet >= 0 else 0
                except:
                    pass
            elif choice == "4":
                if not self.phone_number:
                    input(Fore.RED + "\nÖnce numara girmelisin! ENTER'a bas.")
                    continue
                self.start_attack_screen()
            elif choice == "5":
                sys.exit()

    def start_attack_screen(self):
        self.running = True
        self.clear_screen()
        self.draw_banner()
        print(Fore.RED + Style.BRIGHT + ">>> SALDIRI BAŞLATILDI! DURDURMAK İÇİN [Ctrl + C] YAPABILIRSIN <<<\n")
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
        sms = SendSms(self.phone_number, country_code=self.country_codes[self.selected_code_index])
        methods = [
            sms.KahveDunyasi, sms.Wmf, sms.Bim, sms.Englishhome, sms.Icq,
            sms.Suiste, sms.KimGb, sms.Tazi, sms.Evidea, sms.Hey,
            sms.Bisu, sms.Ucdortbes, sms.Macro, sms.TiklaGelsin, sms.Ayyildiz,
            sms.Naosstars, sms.Istegelsin, sms.Koton, sms.Hayatsu, sms.Hizliecza,
            sms.Ipragaz, sms.Metro, sms.Qumpara, sms.Paybol, sms.Migros,
            sms.File, sms.Joker, sms.Akasya, sms.Akbati, sms.Clickme,
            sms.Happy, sms.Komagene, sms.KuryemGelsin, sms.Porty, sms.Taksim,
            sms.Tasdelen, sms.Tasimacim, sms.ToptanTeslim, sms.Uysal, sms.Yapp,
            sms.YilmazTicaret, sms.Yuffi, sms.Beefull, sms.Starbucks, sms.Dominos,
            sms.Baydoner, sms.Pidem, sms.Frink, sms.Bodrum, sms.LcWaikiki
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
