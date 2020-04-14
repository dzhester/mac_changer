import subprocess
import optparse
import re


def out_int():
    ifc = subprocess.check_output(["ifconfig"])
    check_ifc = re.search(r'\w\w\w\w', ifc.decode('utf-8'))
    print(check_ifc.group(0))

def out_mac():
    macc = subprocess.check_output(["ifconfig"])
    check_macc = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', macc.decode('utf-8'))
    print ((check_macc.group(0)))

def change_mac(interface, new_mac):
    subprocess.call(['ifconfig', interface,  'down'])
    subprocess.call(['ifconfig', interface, 'hw',  'ether', new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def start():
    print("Доступный интерфейс: ")
    out_int()
    print("Нынешний MAC-адрес: ")
    out_mac()

start()

def change():

    interface = input("Ебани интерфейс, который хочешь: ")
    new_mac = input("ебани MAC, который хочешь: ")
    return change_mac(interface,new_mac)

change()

print ("\n[+]MAC adress SUCKseful changed to: "), out_mac()




