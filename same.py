# -*- encoding: utf-8 -*-
"""
返回对词汇的查看情况
    查看六级词汇的频率
2021年11月14日
by littlefean
"""
from docx import Document
import os


def main():
    path = r"dataBaseOrigin\大学英语CET6历年真题试卷+听力音频+答案（2017年-2019年）"
    for item in os.walk(path):
        for file in item[2]:
            filePath = item[0] + os.sep + file
            if filePath.endswith(".docx"):
                print("正在打开这个docx", filePath)
                print("【【【" + getWordStr(filePath) + "】】】")
    return None


def getWordStr(path: str) -> str:
    """输入一个word文档的路径，返回这个word文档里的字符串内容"""
    document = Document(path)
    res = ""
    for paragraph in document.paragraphs:
        res += paragraph.text + "\n"
    return res


if __name__ == '__main__':
    main()
