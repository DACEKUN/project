import subprocess
import time
import os
import sys

#TODO:以后重构
__version__ = "1.0.1" # 主 副 修
print(f"版本号：{__version__}")

running = True
print("\n\n\n这个程序能够让你不输入命令来运行Windows的CMD命令行.")
time.sleep(1.5)
print("这个程序只能运行一些简单的命令, 在运行之前会打印出即将运行的命令.")

def admin():
    import ctypes
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        return 0
    else:
        return 1
result = admin()
if result == 0:
    print("\n未获取管理员权限, 请以管理员身份运行此程序. 程序将在3秒后退出")
    time.sleep(3)
    sys.exit()
elif result == 1:
    print("\n已获取管理员权限.")

if os.name != 'nt':
    print(f"此程序只能在Windows系统使用, 当前操作系统为{os.name}. 将在3秒后退出程序")
    time.sleep(3)
    sys.exit()

# def help_():
#     while True:
#         print("可选项:")
#         print("1.DISM --帮助")
#         print("2.SFC --帮助")
#         print("3.CHKDSK --帮助")
#         print("4.返回")
#         input_ = input("选择类型.")
#         if input_ in ('1','1.'):
#             print("")

#         elif input_ in ('2','2.'):
#             print("")

#         elif input_ in ("3",'3.'):
#             print("")

#         elif input_ in ('4','4.'):
#             print("回到选择页.")
#             time.sleep(1.3)
#             break
#         else:
#             print("无效的输入.")
#             time.sleep(1.3)

def input_():
    while True:
        order_type = input("输入选择的类型代号:")
        if order_type in ("1",'1.'):
            return "chkdsk"
        elif order_type in ("2",'2.'):
            return "dism"
        elif order_type in ("3",'3.'):
            return "sfc"
        elif order_type in ("4",'4.'):
            print("退出程序…")
            time.sleep(1)
            global running
            running = False
            return None
        # elif order_type in ('5','5.'):
        #     return 'help'
        else:
            print("无效的选择")
            time.sleep(1)

def chkdsk():
    global running
    print("默认参数为'/f'.")
    time.sleep(0.5)
    print("\n此命令将卸载所检查硬盘的逻辑分区, 如C盘,D盘.")
    time.sleep(1)
    print("\n\n务必确保在运行此命令时'没有'重要程序在所检查磁盘运行, 或提前保存工作项目文件.")
    time.sleep(2)
    print("\n\n此命令的成功运行, 根据不同参数需要不同的时间.'/f'参数的用时通常比'/r'快很多.")
    print("\n此命令为'chkdsk 盘符: /f'.")
    time.sleep(2)
    continue_ = input("确认继续吗?(Y/N)\n")
    if continue_.upper() == "Y":
        drive_letter = input("\n输入要检查的盘符的'字母'(如C、D、E), 不需要添加如':'的任何内容.\n")
        if not drive_letter:
            print("盘符不能为空")

        elif drive_letter in ('退出程序','4','退出','返回'):
            print("已退出.\n")
            time.sleep(1.5)
            return input_()
        
        elif drive_letter not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            print("盘符必须是字母.")
            time.sleep(1)

        elif len(drive_letter) != 1:
            print("盘符只能是一个字符.")
            time.sleep(1)
        
        else:
            try:
                drive_letter = drive_letter.upper()
            except TypeError as e:
                print(f'类型错误: {e}.')
                time.sleep(10)
                return None
            
            except ValueError as e:
                print(f"值错误: {e}.")
                time.sleep(10)
                return None

            except Exception as e:
                print(f"\n\n错误: {e}\n---延时10秒---.")
                time.sleep(10)
                return None

            try:
                #没有设置超时，为了防止被中断
                result = subprocess.run(["chkdsk",f"{drive_letter}:","/f"],text=True)
                print("\n命令结束.")
                time.sleep(1.5)

            except Exception as e:
                print(f"\n\n错误: {e}\n---延时10秒---")
                time.sleep(10)

    elif continue_.upper() == "N":
        while True:
            trace_back = input("是否回到选择页?(Y/N)\n")
            if trace_back.upper() == "Y":
                time.sleep(0.7)
                return input_()
            elif trace_back.upper() == "N":
                print("退出程序…")
                time.sleep(1)
                running = False
                return None
            else:
                print("无效的输入.")
                time.sleep(1)

    else:
        print("无效的输入, 默认取消.")
        time.sleep(1.5)

def dism():
    global running
    print("警告: 默认参数为'/online /cleanup-image /restorehealth'.")
    time.sleep(1)
    print("\n命令为'dism /online /cleanup-image /restorehealth'.")
    continue_ = input("确认继续吗?(Y/N)")
    if continue_.upper() == 'Y':
        try:
            result = subprocess.run(['dism','/online','/cleanup-image','/restorehealth'],text=True)
            print("\n命令结束.")
            time.sleep(1.5)

        except Exception as e:
            print(f"\n\n错误: {e}\n---延时10秒---.")
            time.sleep(10)

    elif continue_.upper() == 'N':
        while True:
            trace_back = input("是否回到选择页?(Y/N)\n")
            if trace_back.upper() == "Y":
                time.sleep(0.7)
                return input_()
            elif trace_back.upper() == "N":
                print("退出程序…")
                time.sleep(1)
                running = False
                return None
            else:
                print("无效的输入.")
                time.sleep(1)
    else:
        print(" 无效的输入, 默认取消.")
        time.sleep(1.5)

def sfc():
    global running
    print("警告: 默认参数为'/scannow'.")
    time.sleep(1)
    print("\n命令为'sfc /scannow'.")
    continue_ = input("确认继续吗?(Y/N)\n")
    if continue_.upper() == 'Y':
        try:
            result = subprocess.run(['sfc','/scannow'],text=True)
            print("\n命令结束.")
            time.sleep(1)

        except Exception as e:
            print(f"\n\n错误: {e}\n---延时10秒---.")
            time.sleep(10)

    elif continue_.upper() == 'N':
        while True:
            trace_back = input("是否回到选择页?(Y/N)\n")
            if trace_back.upper() == "Y":
                time.sleep(0.7)
                return input_()
            elif trace_back.upper() == "N":
                print("退出程序…")
                time.sleep(1)
                running = False
                return None
            else:
                print("无效的输入.")
                time.sleep(1.3)
    else:
        print("无效的输入, 默认取消.")
        time.sleep(1.5)

def run():
    time.sleep(1)
    print("\n可选项:")
    time.sleep(0.5)
    print("1.chkdsk/磁盘检查")
    print("2.dism/部署映像")
    print("3.sfc/资源保护")
    print("4.退出程序")
    # print("5.帮助")
    type_ = input_()
    if type_ == "chkdsk":
        return chkdsk()
    elif type_ == "dism":
        return dism()
    elif type_ == "sfc":
        return sfc()
    # elif type_ == 'help':
    #     return help_()

while running:
    run()
