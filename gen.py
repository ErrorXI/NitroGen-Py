import random, string
import webbrowser
import time
import requests
from colorama import Fore, init
init()

print(Fore.RED + """\n\n     ███╗   ██╗██╗████████╗██████╗  ██████╗ 
     ████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗
     ██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║
     ██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║
     ██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝
     ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝\n\n""")

amount = int(input('Amount of nitro codes to generate: '))
value = 1
while value <= amount:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('Codes.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'[GENERATED] {code}')
    value += 1

print(Fore.GREEN + """Now i will check nitro codes!""")    

with open("Codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitelemnts/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(" Valid | {} ".format(line.strip("\n")))
            break
        else:
            print(" Invalid | {}".format(line.strip("\n")))
input("The end! Press Enter 5 times to close the program.")
input("4")
input("3")
input("2")
input("1")    