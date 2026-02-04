import sys, os, subprocess
from pathlib import Path

# 设定使用的python环境
venv_python = Path(r"./venv/Scripts/python.exe")


# 设定
if len(sys.argv) == 1:
    # 如果什么都没输入就输出
    subprocess.run([str(venv_python),".\\command\\help.py"], check=True)

if len(sys.argv) > 1:
    command = sys.argv[1]

    if command == "help":
        subprocess.run([str(venv_python),".\\command\\help.py"], check=True)
    elif command == "jm":
        subprocess.run([str(venv_python),".\\command\\Download.py"], check=True)
    elif command == "version":
        subprocess.run([str(venv_python),".\\command\\version.py"], check=True)
    else:
        print(f"未知的命令: {command}")