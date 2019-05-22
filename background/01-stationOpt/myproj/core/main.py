import sys
import os
import mongoengine
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from core.stationtide import *
from core.typhoon import TyphoonRealData
from conf import setting



def main():
    dir_path=setting.DIR_PATH
    file_name=setting.FILE_TARGET
    mongoengine.connect(setting._MONGODB_NAME)
    # 测试
    # 写入测站数据
    # station=StationTideRealData(dir_path,file_name)
    station=StationRealData(dir_path)
    # station.open()
    station.run()
    # typhoon=TyphoonRealData(dir_path)
    # typhoon.run()
    print('录入完成')
    pass

if __name__=='__main__':
    main()