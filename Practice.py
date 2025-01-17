# -*- encoding: utf-8 -*-
"""
PyCharm Practice
此模块中定义了一些单词训练函数
大多数是基于控制台交互式操作的方式进行单词训练的
2021年08月08日
by littlefean
"""

from words import WordList


class Proficiency:
    """ 单词列表对应的单词熟练度 """

    def __init__(self, words: WordList):
        self.proValueDic = {}
        self.practiced = []  # 正在练习中的单词，若空了表示练习完了
        self.words = words
        for w in words:
            self.proValueDic[w.name] = 0
            self.practiced.append(w.name)

    def addValue(self, wordName: str, n: float):
        """熟练度增加"""
        if wordName in self.proValueDic:
            self.proValueDic[wordName] += n

    def __str__(self):
        d_order = sorted(self.proValueDic.items(), key=lambda x: x[1], reverse=True)
        return "".join(str(item) + "\n" for item in d_order)


def practiceE(wordList: WordList):
    """
    在控制台上开始交互式练习，
    单词练习 随机展示英语想汉语
    """
    while True:
        wordList.shuffle()
        for w in wordList:
            print(w.name)
            input()
            print(w)
            input()


def easyPractice(wordList: WordList):
    """
    在控制台上开始交互式练习，
    只进行辨识度的练习  看英文能知道是什么意思
    """
    count = len(wordList)
    wv = Proficiency(wordList)

    while True:
        wordList.shuffle()
        print("洗牌了一遍")
        if len(wordList) == 0:
            print("训练完毕")
            break
        for w in wordList:
            print(w.name)
            inputN = input("2熟练 3不熟练")
            print(w)
            if inputN == "2":
                wordList.remove(w.name)
            elif inputN == "3":
                wv.addValue(w.name, 1)
            print(f"总共：{count}，剩余：{len(wordList)}")  # 展示进度
    print(wv)


def practiceCE(wordList: WordList):
    """
    在控制台上开始交互式练习
    根据汉语意思输入英文单词的练习
    """
    count = len(wordList)
    wv = Proficiency(wordList)

    while True:
        wordList.shuffle()
        print("洗牌了一遍")
        if len(wordList) == 0:
            print("训练完毕")
            break
        for w in wordList:
            print(w.chinese)
            inputData = inputEnglishOut(input(":"))
            # 输入1也可以通过，这个是为了测试
            # todo 可以请求发送读音
            # todo 也可以直接删除这个单词
            if inputData in [w.name, "1"]:
                print("拼写正确")
                wordList.remove(w.name)
            else:
                print(f"错误：{w.name}", w.speaker)
                wv.addValue(w.name, 1)
            print(f"总共：{count}，剩余：{len(wordList)}")  # 展示进度
            input("回车继续...")
    print(wv)


def fastPractice(wordList: WordList, listName: str):
    """
    生成含有js的静态网页，对其进行高速练习
    此方法仅仅是根据一个单词列表，生成（更新）一个js文件
    注意：生成的网页不能直接运行，需要在webstorm里或者pycharm里用小三角运行
    或者vscode的LiveServer运行
    :param wordList: 单词列表
    :param listName: 生成js文件得名字
    :return:
    """
    listStr = ''.join(f"{word.toEasyJs()}," for word in wordList)
    jsStr = f"""
    WORD_LIST = [{listStr}]
    """
    with open(f"fastPractice\\js\\{listName}.js", "w", encoding="utf-8") as f:
        f.write(jsStr)


def inputEnglishOut(string: str) -> str:
    """对输入的单词进行预处理"""
    arr = [char for char in string if char.isalpha()]
    return "".join(arr)


def test():
    """用于方便提问对方的的模块"""
    ...
