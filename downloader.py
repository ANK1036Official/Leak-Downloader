import sys, os, platform, pathlib, colorama
from colorama import Fore, Back, Style
from csv import DictReader
count = 1
origin = []
url = []
ascii_banner = open('ascii_banner.txt', 'r')
if platform.system() == "Windows":
    banner = ascii_banner.read()
elif platform.system() == "Linux":
    os.system("echo -e $(cat ansi_banner.ans)")
else:
    pass

print(banner)
with open('list.csv', 'r') as list_obj:
    csv_dict_reader = DictReader(list_obj)
    for row in csv_dict_reader:
        menu_format = f"{Fore.LIGHTCYAN_EX} {row['number']}{Fore.RESET} -- {Fore.MAGENTA}{row['origin']} {Fore.LIGHTGREEN_EX}({row['url']}){Fore.RESET}\n"
        sys.stdout.write(menu_format)

choice = input(f"Choose what to download: {Fore.YELLOW}")
with open('list.csv', 'r') as list_obj2:
    csv_dict_reader2 = DictReader(list_obj2)
    for row2 in csv_dict_reader2:
        if str(row2['number']) == str(choice):
            if platform.system() == "Windows":
                drive = pathlib.Path.home().drive
                curdrive = drive + "\\"
                if os.path.isfile(curdrive + "Users\\" + os.getlogin() + "\\AppData\\Local\\MEGAcmd\\MEGAclient.exe"):
                    DOWN_CODE = f"os.system(r\'{curdrive}Users\\{os.getlogin()}\\AppData\\Local\\MEGAcmd\\MEGAclient.exe get \"{str(row2['url'])}\"\')"
                    print(f"Windows detected...\nDown code: {DOWN_CODE}")
                else:
                    print("MEGAcmd not detected...\nInstall MEGAcmd to continue! ( https://mega.io/cmd )")
                    exit()
            elif platform.system() == "Linux":
                if os.path.isfile("/usr/bin/mega-get"):
                    DOWN_CODE = f"os.system(r\'/usr/bin/mega-get \"{str(row2['url'])}\"\')"
                    print(f"Linux detected...\nDown code: {DOWN_CODE}")
                else:
                    print("MEGAcmd not detected...\nInstall MEGAcmd to continue! ( https://mega.io/cmd )")
                    exit()
            else:
                print("Unable to detect operating system, or not supported...\nExiting...")
                exit()
            # m = mega.login()
            # m.download_url(str(row2['url']), './')
            exec(DOWN_CODE)
            print(f"{Fore.LIGHTCYAN_EX}Done!\nPassword: ANK_Stash5!{Fore.RESET}")
