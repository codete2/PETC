# -*- coding: utf-8 -*-
# @Time    : 2024/5/5 15:23:14
# @Author  : Codete
# @FileName: main.py
# @IDE: PyCharm
# @E-Mail: CodeteMail@163.com
import sys
import CodeteLib as cl
import time as t
import gettext
import os
import http.server
import socketserver

cl.cls()

# Settings
if os.path.exists("data.petc") == False:
    with open("data.petc", "w", encoding="utf-8") as dataTemp:
        userLang = [cl.getLanguage()]
        dataTemp.write("language={}\nlevel=0".format(userLang))
with open("data.petc", "r", encoding="utf-8") as data1:
    d1 = data1.readlines()
    data = {}
    for d2 in d1:
        data[d2.split("=")[0]] = d2.split("=")[1].replace("\n", "")
    userLang = data['language']

lang = gettext.translation('PETCTrans', localedir='locales', languages=userLang)
lang.install('PETCTrans')
_ = lang.gettext

if data['level'] == '0':
    # Print Logo
    cl.cls()
    print(cl.CodeteLogo)
    t.sleep(5)
    cl.cls()
    print(cl.gameTitle)
    t.sleep(5)
    cl.cls()

    # Tips
    cl.cls()
    print(_("提示:"))
    print(_("1. 本游戏有20关, 请确保您已经阅读了游戏规则"))
    print(_("2. 本游戏将会开启您的电脑的45678端口, 请确保您的电脑的45678端口未被占用"))
    print(_("3. 本游戏将会在您的电脑上开启一个HTTP服务器"))
    print(_("4. 本游戏将会在您的电脑中创建一些文件夹和文件"))
    print(_("5. 您可以在游玩本游戏的同时查看Github上的源代码, 但可能会影响游玩的体验"))
    print(_("6. 本游戏已在Github上开源, 如遇到bug, 请随时在Github上提交issue"))
    print(_("7. 如果您想查看本游戏的源代码, 请访问Github: https://github.com/Codete/PETC"))
    print(_("8. 如果您在游戏中遇到了困难, 可以查看Github上的教程"))
    print(_("9. 在一关结束后, 窗口会关闭, 请重新打开本游戏"))
    print(_("10. 祝您游戏愉快!"))
    print(_("11. 本提示将不会再次显示!!!!"))
    print()
    input("Press ENTER to continue...")
    cl.changeLevel(1)
    sys.exit(0)
elif data['level'] == '1':
    cl.cls()
    print(_("在读取提示词时遇到了错误: 无法识别的字符"))
    t.sleep(0.1)
    print(_("正在尝试恢复......"))
    t.sleep(3)
    print(_("错误: 未能完全修复提示词"))
    print("p-es- enTre two CotINeu...", end='')
    user = input("\b" * 26)
    if user == "Press ENTER to continue...":
        cl.changeLevel(2)
    else:
        cl.cls()
        print(_("错误"))
        print(_("无法识别的字符"))
        t.sleep(3)
elif data['level'] == '2':
    cl.cls()
    with open('TOKEN', 'r', encoding='utf-8') as tok:
        if cl.checkToken(tok.read()) == True:
            cl.changeLevel(3)
            input("Token Check OK!\nPress ENTER to continue...")
            sys.exit(0)
    with open('TOKEN', 'w+', encoding='utf-8') as toke:
        toke.write(_("在此处写下你的Token"))
    class MyHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'{}: {}'.format(_("你的Token"), cl.getToken()))

    with socketserver.TCPServer(("", 45678), MyHandler) as httpd:
        print("Server started at http://localhost:{}/".format(45678))
        httpd.serve_forever()
else:
    cl.cls()
    print(_("---------- 开发中, 敬请期待 ----------"))
    input("Press ENTER to continue...")
    sys.exit(0)