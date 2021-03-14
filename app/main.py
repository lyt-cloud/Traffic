# app程序的入口

# 包文件的管理 项目的跟根路径引入
from app.uis.trafficapp import TrafficApp
import sys


app=TrafficApp()
status=app.exec_()
sys.exit(status)

