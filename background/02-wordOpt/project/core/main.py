from docx import Document
import os
from core.Paragraph import *
from core.File import FileInfo
from data.model import *
from mongoengine import *

targetfilename=r"5622.docx"
# aw
# targetpath=r"D:\01proj\typhoon\TyphoonSearchSys\demo_data"
# P52S
# targetpath=r"D:\04git仓库\TyphoonSearchSys\demo_data"
# mac15
# targetpath=r"/Users/liusihan/Documents/01project/TyphoonSearchSys/demo_data"
# mac16
targetpath=r"/Users/drno/Documents/01proj/TyphoonSearchSys_new/TyphoonSearchSys/background/05-docx/result"


fullname=os.path.join(targetpath,targetfilename)


def readtxt(filename):
    '''
        读取word文档
    :param filename:
    :return:
    '''
    doc = Document(filename)
    fullText = []
    # ((lambda x: fullText.append(x) )(para))
    for para in doc.paragraphs:
        if len(para.text)>0:
            fullText.append(para.text)
    return '\n'.join(fullText)

def main():
    file=FileInfo(targetpath)
    # 获取所有的word对象
    words= file.getWordFiles()
    # 遍历将每一个符合条件的word对象写入mongo中
    # [word for word in words if word.standard==True]
    for word in words:
        if word.standard==True:
            code=word.typhoonNum
            # code = '5622'
            par = Paragraph(word.dir, word.filename)
            # 写入mongo
            connect('typhoon')
            dis = DisasterWordInfo(code=code, wordDocument=par.wordText)
            dis.save()
            print(par.wordText)

    # code='5622'
    # par= Paragraph(targetpath,targetfilename)
    # # 写入mongo
    # connect('typhoon')
    # dis=DisasterWordInfo(code=code,wordDocument=par.wordText)
    # dis.save()
    # print(par.wordText)

if __name__=='__main__':
    main()
# print (readtxt(fullname))