from collections import *
from add_device import *
q = 1
network = defaultdict(lambda:[])

def execute_command(command:str):
    command = command.split()
    if len(command) < 3:
        print("Error : Invalid command syntax")
        return

    if command[0] == "ADD":
        if command[1] == "COMPUTER":
            print(add_device(network, command[1], command[2]))
        elif command[1] == "REPEATER":
            print(add_device(network, command[1], command[2]))
        else:
            print("Error: Invalid command syntax")
    
    if command[0] == "SET_DEVICE_STRENGTH":
        print(set_device_strength(network, command[1], command[2]))

    if command[0] == "CONNECT":
        print(connect_device(network, command[1], command[2]))

    if command[0] == "INFO_ROUTE":
        print(info_route(network, command[1], command[2]))

    print(network)




print("Welcome to Ajira Network Console!")


while(q!=0):
    q= int(input("\nPress 1 Enter your command \nPress 0 to exit\n\n>"))
    if q == 0:
        break
    command = input(">")
    
    

