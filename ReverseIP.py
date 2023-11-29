import importlib, time
def check_and_install_module(module_name):
    try:
        importlib.import_module(module_name)
        print(f"{module_name} is already installed.")
        time.sleep(0.5)
    except ImportError:
        print(f"{module_name} is not installed. Installing...")
        time.sleep(0.5)
        install_module(module_name)

def install_module(module_name):
    try:
        import subprocess
        subprocess.check_call(["pip", "install", module_name])
        print(f"{module_name} has been successfully installed.")
        time.sleep(0.5)
    except Exception as e:
        print(f"Error installing {module_name}: {e}")
        time.sleep(0.5)

modules  = ['requests', 'pytz', 'colorama']
for module in modules:
    check_and_install_module(module)

import requests, urllib3, re, subprocess, platform
from concurrent.futures import ThreadPoolExecutor as Pool2
from colorama import Fore, Style
from datetime import datetime
import pytz

now = datetime.now(pytz.timezone('Asia/Jakarta'))
filenow = now.strftime("%H'%M")
def clear():
    if platform.system() == "Windows":
        subprocess.call('cls', shell=True)
    else:
        subprocess.call('clear', shell=True)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
errors = (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout,
          requests.exceptions.BaseHTTPError, requests.exceptions.HTTPError,
          requests.exceptions.InvalidHeader, requests.exceptions.ConnectTimeout,
          requests.exceptions.TooManyRedirects, requests.exceptions.RequestException,
          requests.exceptions.RequestsWarning, requests.exceptions.Timeout,
          requests.exceptions.InvalidURL, requests.exceptions.RequestsDependencyWarning)

bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.GREEN
red = Fore.RED
cyan = Fore.CYAN
res = Style.RESET_ALL
yl = Fore.YELLOW
gr2 = Fore.LIGHTGREEN_EX
red2 = Fore.LIGHTRED_EX
yl2 = Fore.LIGHTYELLOW_EX

s = requests.Session()
class NANCY_REV:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }
        self.working = 0
        self.totaling = len(stars)
    def rsec(self, star):
        star = star.replace("\n", "").replace("\r", "").replace(" ", "")
        try:

            payload = {
                'email':'nancy@nax1.cc', 'password':'NANCY-0dFJA-3YW2L-4UXXT-LLzxY'
            }
            log = s.post(f"https://75.101.214.154/api/auth/login", data=payload, verify=False, headers=self.headers)
            if "success" in log.text:
                try:
                    pages = 1
                    total_revers = []
                    while True:
                        rev = s.get(f"https://75.101.214.154/list/ip/{star}?page={pages}", verify=False, headers=self.headers)
                        if rev.status_code == 200:
                            page = rev.text
                            pattern = r'<a class="link" href="/domain/(.*?)/dns">'
                            result = re.findall(pattern, page)
                            if not result:
                                break
                            if result:
                                for revers in result:
                                    revers = revers.strip()
                                    if revers.startswith("www."):
                                        revers = "" + revers[4:]
                                    else:
                                        pass
                                    open(f"REV-IP({filenow}).txt", "a").write(f"{revers}\n")
                            total_revers.extend(result)
                            pages += 1
                        elif rev.status_code == 404:
                            break
                        else:
                            break
                    if len(total_revers) == 0:
                        print(f"{wh}[ {cyan}{self.working}{wh}/{cyan}{self.totaling}{wh} ] {yl2}0xb511{wh}({yl}REV.IP{wh}) » {cyan}{star} {wh}» {red2}NO~DATA{res}")
                    else:
                        print(f"{wh}[ {cyan}{self.working}{wh}/{cyan}{self.totaling}{wh} ] {yl2}0xb511{wh}({yl}REV.IP{wh}) » {cyan}{star} {wh}» {wh}[ {gr2}{len(total_revers)} {wh}]{res}")
                except:
                    pass
            else:
                print(f"AKUN ERROR")
        except Exception as e:
            print(e)
    def filters(self, star):
        try:
            r = self.rsec(star)
            if r:
                return True
        except Exception as e:
            print(e)
        self.working += 1

if __name__ == "__main__":
    try:
        clear()
        lists = input(f"{gr}List {wh}=> {res}")
        stars = open(lists, 'r').readlines()
        threads = int(input(f"{gr}Threads {wh}=> {res}"))
        clear()
        nan = NANCY_REV()
        try:
            with Pool2(threads) as start:
                start.map(nan.filters, stars)
        except:
            pass
        s.close()
    except KeyboardInterrupt:
        print(f"\n{red}KeyboardInterrupt{res}")
    except FileNotFoundError:
        print(f"\n{red}FileNotFoundError{res}")
    except FileExistsError:
        print(f"\n{red}FileExistsError{res}")