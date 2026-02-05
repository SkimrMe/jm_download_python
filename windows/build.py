#打包脚本
import subprocess, os, sys

# 建立venv虚拟环境
print("建立venv虚拟环境")
subprocess.run("python -m venv venv", shell=True)

# 安装requirements.txt中的库
print("安装requirements.txt中的库")
subprocess.run("venv\\Scripts\\pip.exe install -r ..\\requirements.txt", shell=True)

# 列出pip安装的库
print("列出pip安装的库")
subprocess.run("venv\\Scripts\\pip.exe list", shell=True)

# pyinstaller打包程序
print("pyinstaller打包中")
print("打包main.py")
subprocess.run("venv\\Scripts\\pyinstaller.exe --onefile command\\main.py", shell=True)
print("打包help.py")
subprocess.run("venv\\Scripts\\pyinstaller.exe --onefile command\\help.py", shell=True)
print("打包Download.py")
subprocess.run("venv\\Scripts\\pyinstaller.exe --onefile command\\Download.py", shell=True)
print("打包version.py")
subprocess.run("venv\\Scripts\\pyinstaller.exe --onefile command\\version.py", shell=True)

# 清理build和*.spec文件
print("清理build和*.spec文件")
subprocess.run("RMDIR build /s /q", shell=True)
print("正在清理*.spec文件")
subprocess.run("DEL main.spec version.spec Download.spec help.spec", shell=True)


# 重命名dist为jm_
print("重命名dist为jm_")
dir_path = os.path.dirname(os.path.abspath(__file__))
print("当前路径: " , f"{dir_path}")
pass
os.rename(f"{dir_path}\\dist", "jm_")

# 进入打包后产物文件夹
print("进入打包后产物文件夹")
os.chdir("jm_")

# 测试程序
print("测试程序")
subprocess.run("main.exe", shell=True)
subprocess.run("version.exe", shell=True)
subprocess.run("help.exe", shell=True)

print("大功告成~感谢您的使用")