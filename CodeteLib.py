# -*- coding: utf-8 -*-
# @Time    : 2024/5/5 18:43:27
# @Author  : ZMF
# @FileName: CodeteLib.py
# @IDE: PyCharm
# @E-Mail: ZZMF20110806@163.com
import os
import jwt
import socket
import datetime

gameTitle = """██████╗ ██████╗ ███████╗███████╗███████╗                                                         
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝                                                         
██████╔╝██████╔╝█████╗  ███████╗███████╗                                                         
██╔═══╝ ██╔══██╗██╔══╝  ╚════██║╚════██║                                                         
██║     ██║  ██║███████╗███████║███████║                                                         
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝                                                         

███████╗███╗   ██╗████████╗███████╗██████╗                                                       
██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔══██╗                                                      
█████╗  ██╔██╗ ██║   ██║   █████╗  ██████╔╝                                                      
██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗                                                      
███████╗██║ ╚████║   ██║   ███████╗██║  ██║                                                      
╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝                                                      

████████╗ ██████╗      ██████╗ ██████╗ ███╗   ██╗████████╗██╗███╗   ██╗██╗   ██╗███████╗         
╚══██╔══╝██╔═══██╗    ██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██║████╗  ██║██║   ██║██╔════╝         
   ██║   ██║   ██║    ██║     ██║   ██║██╔██╗ ██║   ██║   ██║██╔██╗ ██║██║   ██║█████╗           
   ██║   ██║   ██║    ██║     ██║   ██║██║╚██╗██║   ██║   ██║██║╚██╗██║██║   ██║██╔══╝           
   ██║   ╚██████╔╝    ╚██████╗╚██████╔╝██║ ╚████║   ██║   ██║██║ ╚████║╚██████╔╝███████╗██╗██╗██╗
   ╚═╝    ╚═════╝      ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝╚═╝╚═╝"""
CodeteLogo = """███████████
█ █████ █ █
█ █ █   █ █   ╔═╗╔═╗╔╦╗╔═╗╔╦╗╔═╗       ╔═╗╔╦╗╔═╗
█ █  █  █ █   ║  ║ ║ ║║║╣  ║ ║╣   ───  ╔═╝║║║╠╣ 
█ █████ █ █   ╚═╝╚═╝═╩╝╚═╝ ╩ ╚═╝       ╚═╝╩ ╩╚ 
█   █     █
███████████"""
languages = """Please choose your language 请选择您的语言：
1. English
2. Español
3. Français
4. Русский язык
5. 简体中文
6. 繁體中文
"""


def cls():
    os.system("cls")

def getLanguage() -> str:
    while True:
        print(languages)
        user = input()
        cls()
        if user not in [str(i) for i in range(1, 7)]:
            print("Invalid input, English will be used as your language", end='')
            s = input("Are you sure? (yes / no)")
            if s == "yes":
                return "en"
        else:
            if user == "1":
                print("We will use English as your language.")
                s = input("Are you sure? (yes / no)")
                if s == "yes":
                    return "en"
            elif user == "2":
                print("Usaremos el español como tu idioma.")
                s = input("¿¿ estás seguro? (sí / no)")
                if s == "sí":
                    return "es"
            elif user == "3":
                print("Nous utiliserons le français comme votre langue.")
                s = input("T'en es sûr? (Oui / non)")
                if s == "Oui":
                    return "fr"
            elif user == "4":
                print("Мы будем использовать русский язык как ваш язык.")
                s = input("Ты уверен? (Да / Нет)")
                if s == "Да":
                    return "ru"
            elif user == "5":
                print("我们将使用简体中文作为您的语言。")
                s = input("您确定吗？(是 / 否)")
                if s == "是":
                    return "zh_CN"
            elif user == "6":
                print("我們將使用繁體中文作為您的語言。")
                s = input("您確定嗎？(是 / 否)")
                if s == "是":
                    return "zh_TW"

# This function will remove a line from a file.
# From https://zhuanlan.zhihu.com/p/678680796
def remove_line(fileName,lineToSkip):
    with open(fileName,'r', encoding='utf-8') as read_file:
        lines = read_file.readlines()
    currentLine = 1
    with open(fileName,'w', encoding='utf-8') as write_file:
        for line in lines:
            if currentLine == lineToSkip:
                pass
            else:
                write_file.write(line)
            currentLine += 1

# This function will change the level.
def changeLevel(levelTo, dataFileName='data.petc', levelLine='2'):
    remove_line(dataFileName, levelLine)
    with open(dataFileName, 'a', encoding='utf-8') as data:
        data.write('level={}'.format(levelTo))

def getIP():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
def getToken():
    return jwt.encode(
    {"exp": datetime.datetime.now() + datetime.timedelta(days=1),
     "iss": "CODETE",
     "data": getIP()},
    "PETCTokenKey",
    algorithm = "HS256",
    )

def decodeToken(token):
    try:
        decoded_token = jwt.decode(token, issuer="CODETE", key="PETCTokenKey", algorithms=["HS256"])
        return decoded_token
    except:
        return False

def checkToken(token):
    if decodeToken(token):
        if decodeToken(token)["data"] == getIP():
            return True
        else:
            return False
    else:
        return False