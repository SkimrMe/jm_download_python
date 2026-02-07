import sys, subprocess

# 设定
if len(sys.argv) == 1:
    # 如果什么都没输入就输出
    subprocess.run("./help", check=True)

if len(sys.argv) > 1:
    command = sys.argv[1]

    if command == "help":
        subprocess.run("./help", check=True)
    elif command == "jm":
        subprocess.run("./Download", check=True)
    elif command == "version":
        subprocess.run("./version", check=True)
    else:
        print(f"未知的命令: {command}")