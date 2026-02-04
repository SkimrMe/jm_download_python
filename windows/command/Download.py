import jmcomic as jm
import os, sys

print(f'请输入 jmcomic 车号')

car_id = input()

jm.download_album(car_id)
