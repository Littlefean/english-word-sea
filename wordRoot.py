# -*- encoding: utf-8 -*-
"""
PyCharm wordRoot 词根词缀字典
这个设计的初心就是：输入一个英文，我能立刻知道这个英文有哪些匹配了的词根词缀
2021年12月31日
by littlefean
"""

prefix = {}  # 前缀
suffix = {}  # 后缀
rootWord = {}  # 词根


def removeNum(string: str) -> str:
    """去除字符串里的数字"""
    res = ""
    for char in string:
        if char.isdigit():
            continue
        else:
            res += char
    return res


def removeSubStr(string: str, removeStr: str) -> str:
    res = string
    i = res.find(removeStr)
    if 0 <= i < len(res):
        res = res[:i] + res[i + len(removeStr):]
    return res


def transPar(string: str) -> tuple:
    """将一个t（o）返回成 (to, t)"""
    leftI = string.find("（")
    rightI = string.rfind("）")
    small = string[:leftI] + string[rightI + 1:]  # 不含括号的单词
    big = string[:leftI] + string[leftI + 1:rightI] + string[rightI + 1:]
    return small, big


def init():
    """初始化读取的操作"""
    # 加入从四级词汇闪过中的词根词缀
    with open(r"dataBaseOrigin/词根词缀.txt", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip()
            if len(line.split()) == 2:
                eng, chi = line.split()
                if "，" in eng:
                    engArr = eng.split("，")
                    for e in engArr:
                        if e.startswith("-"):
                            prefix[e[1:]] = chi
                        elif e.endswith("-"):
                            suffix[e[:-1]] = chi
                        else:
                            rootWord[e] = chi
                else:
                    rootWord[eng] = chi
            ...
    # 加入从百度文库中找到的词根词缀
    with open(r"dataBaseOrigin/词根词缀大全.txt", encoding="utf-8") as f:
        arr = f.readlines()
    for i, line in enumerate(arr):
        if i in range(3, 79):
            prefixName = line.split("-")[0]
            prefix[prefixName] = "".join(line.split("-")[1:]).strip()
        if i in range(87, 216):
            # print(line)
            if line.strip() == "":
                continue
            line = line[1:]
            prefixName = ""
            index = 0
            for char in line:
                if char.isalpha():
                    prefixName += char
                    index += 1
                else:
                    break
            suffix[prefixName] = line[index:].strip()

        if i in range(218, 381):
            index = 0  # 中文汉字开始的下标
            for j, char in enumerate(line):
                if u'\u4e00' <= char <= u'\u9fff':
                    index = j
                    break

            mean = line[index:].strip()  # 这个词根的意思解释
            before = line[:index].strip()  # 中文前面的部分
            arr = before.split("，")

            def addToDic(wordName: str, wordInfo: str):
                """把一个单词添加到字典的做法"""
                if wordName in rootWord:
                    if wordInfo in rootWord[wordName]:
                        return
                    else:
                        rootWord[wordName] += f" {wordInfo}"
                else:
                    rootWord[wordName] = wordInfo

            for word in arr:
                # 遍历每一个单词
                word = removeNum(word)
                if "（" in word and "）" in word:
                    word1, word2 = transPar(word)
                    addToDic(word1, mean)
                    addToDic(word2, mean)
                else:
                    addToDic(word, mean)
                ...
            ...
    ...


def main():
    print("初始化中……")
    init()
    while True:
        word = input("请输入你要解析词根词缀的单词：")
        print("词根匹配")
        for k, v in rootWord.items():
            if k in word:
                print(f"\t{k}\t{v}")
        print("前缀匹配：")
        for k, v in prefix.items():
            if k in word:
                print(f"\t{k}-\t{v}")
        wordCopy = word
        print("后缀匹配")
        for k, v in suffix.items():
            if k in word:
                print(f"\t-{k}\t{v}")


if __name__ == "__main__":
    main()