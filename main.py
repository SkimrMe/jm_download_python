# 主函数
# 引入 jmcomic
import jmcomic as jm

# 下载功能
print(f'请输入 jmcomic 车号')

car_id = input()

jm.download_album(car_id)

