"""
词海计划的一部分：单词相似
2021年06月21日
by littlefean
"""
from sameWords import *
from Practice import *


def matchStr():
    """词根词缀匹配"""
    wordArr = WordList.initialize()
    addWords1(wordArr, "dataBaseOrigin/考研单词乱序版.txt")

    a = WordList.initialize()
    addWordsRoot(a, "dataBaseOrigin/词根词缀.txt")

    def printWord(w, r):
        print("\t", w.name, w.chinese, "\t\t\t")
        ...

    wordSet = set()
    for root in a:
        # print(root.toExclStr())
        print(f"【{root.name}】=======", root.chinese)
        if root.name.startswith("-"):
            for word in wordArr:
                if word.name.endswith(root.name[1:]):
                    printWord(word, root)
                    wordSet.add(word.name)
                    # print(root.name, root.name[1:])
                    ...
        elif root.name.endswith("-"):
            for word in wordArr:
                if word.name.startswith(root.name[:-1]):
                    printWord(word, root)
                    wordSet.add(word.name)
                    ...
        else:
            for word in wordArr:
                if root.name in word.name:
                    printWord(word, root)
                    wordSet.add(word.name)
                    ...
    print(len(wordSet))
    return None


def getExcl():
    a = WordList.initialize()
    addWords1(a, "dataBaseOrigin/正序.txt")
    string = """abuse aggreeable analyse ankle apparatus arithmetic arrogant ascertain attribute auditorium avert aviation awkward axis beard blossom bosom bulletin camel worship whip whirl whisky whistle weary wedding versus vessel veteran turbine trivial tribe trial tremble tray tragedy transfer transcend tilt tile thermometer theoretical terminate territory"""
    arr = string.split()
    print(arr)
    for eng in arr:
        for item in a:
            if item.name == eng:
                print(item.toExclStr())
                break
    # for item in a:
    #     print(item.toExclStr())


def main():
    a = WordList.initialize()
    addWords1(a, "dataBaseOrigin/正序.txt")
    day = 1
    startWord = input("startWord: ")
    endWord = input("endWord: ")
    a.cut(startWord, endWord)
    # addWords1(a, "dataBaseOrigin/陌生单词.study")
    # a.cut("shape", "famous")
    # a.cut("capitalism", "slit")
    # a.cut("remove", "vegetarian")

    # a.cut("transfer",  "retain")

    # practiceCE(a)
    easyPractice(a)

    # practiceE(a)

    # fName = "myJson"
    # with open(f"practiceHtml/json/{fName}.json", "w", encoding="utf-8") as f:
    #     f.write(a.toJsonStr())

    def upDate():
        untilWord = "improve"
        # a.removeRight(a.index(untilWord))
        # print(a.index(untilWord))
        # print(a.index(untilWord) / len(a))
        # print((a.index(untilWord) + 30 * 49))
        # print((a.index(untilWord) + 30 * 49) / len(a))
        a.removeRight(a.index(untilWord))
        # a.saveHtmlFile("out")
        title = f"考研单词到{untilWord}"

        s1 = SamesList.wordListToSamesArr(a, wordInWord)
        s1.saveTxt(f"{title}，是字串的")
        # s1.saveJson(f"to-{title}")
        s3 = SamesList.wordListToSamesArr(a, sameChinese)
        s3.saveTxt(f"{title}，含有相同汉语词的单词")
        # s3.saveJson("ChineseWordIn")
        for i in range(4, 10):
            SamesList.wordListToSamesArr(a, sameChineseWord, funcN=i).saveTxt(
                f"{title}，汉语相同文字{i}个的单词们")
            SamesList.wordListToSamesArr(a, lenSame, funcN=i).saveTxt(
                f"{title}，长度相同但是有{i}个字母不同的单词们")
            SamesList.wordListToSamesArr(a, partInPart, funcN=i).saveTxt(
                f"{title}，含有长度为{i}个字母的公共字串的单词们")
            SamesList.wordListToSamesArr(a, sameStart, funcN=i).saveTxt(
                f"{title}，都以{i}个相同字母开头的单词们")
            SamesList.wordListToSamesArr(a, sameEnd, funcN=i).saveTxt(
                f"{title}，都以{i}个相同字母结尾的单词们")

        # for charIndex in range(ord("\u4e00"), ord("\u9fa5")):
        #     wArr = WordList.initialize()
        #     for w in a:
        #         if chineseInWord(w, chr(charIndex)):
        #             wArr.addWord(w)
        #     if len(wArr) != 0:
        #         wArr.saveTxtFile(f"汉字的/{len(wArr)} {chr(charIndex)}字")

    return None


def addWordsRoot(wordList: WordList, path):
    """
    从词根词缀中添加单词
    :param wordList:
    :param path:
    :return:
    """
    with open(path, "r", encoding='utf-8') as f:
        lineList = f.readlines()
        for line in lineList:
            if len(line.strip()) > 0:
                lineArr = line.split()
                try:
                    roots, chinese = lineArr[0], lineArr[1]
                    rootArr = roots.split("，")
                    for root in rootArr:
                        w = Word(root, chinese)
                        wordList.addWord(w)
                except IndexError:
                    print(lineArr, f"line:<<<{line}>>>")
        ...
    return None


def addWords1(wordList: WordList, path):
    """
    从文件中添加单词到词库，
    当前是考研单词格式
    :param wordList: 制定添加的词表
    :param path: 文件路径，一般是txt文件
    :return: 没有返回值
    """
    # a. v. n. vi. ad. conj. vt. pron.
    with open(path, "r", encoding='utf-8') as f:
        lineList = f.readlines()
        for line in lineList:
            if "视频网课资料请" in line:
                continue
            if len(line) > 0:
                if line[0].isalpha():  # 如果第一个字符是字母，则认为这一行是有效的单词行
                    try:
                        splitArr = line.split("/")
                        word = splitArr[0].strip()
                        speak = line.split("/")[1]
                        speak = f"/{speak}/"
                        chinese = "".join(line.split("/")[2:]).strip()  # 音标后面的部分都是汉语意思
                        w = Word(word, chinese, speaker=speak)
                        w.chineseObj = WordList.stringToChineseObj(chinese)
                        w.chineseList = WordList.stringToChineseList(chinese)
                        wordList.addWord(w)
                    except IndexError:
                        # todo 解决解析错误
                        # print(f"【出现了解析错误】：{line}")
                        pass


def addWords2(wordList: WordList, path):
    """添加张麟的词库"""
    with open(path, "r", encoding='utf-8') as f:
        fileString = f.read()
        i = 1
        while True:
            a = fileString.find(f"{i}.")
            b = fileString.find(f"{i + 1}.")
            if a != -1 and b == -1:
                # 这是最后一个了
                wordStr = fileString[a:]
            elif a == -1 and b == -1:
                # 没了
                break
            else:
                wordStr = fileString[a:b]
            wordStr = wordStr.replace("\n", "").replace(f"{i}.", "").strip()

            # print(wordStr)

            # ==开始解析这个单词字符串==
            arr = wordStr.split(" ")
            wordArr = []  # 如果这个单词是短语，那么准备一个列表
            for part in arr:
                count = 0
                for char in part:
                    if char.isalpha():
                        count += 1
                    else:
                        break
                else:
                    if count == len(part) and count > 0:
                        wordArr.append(part)

            word = " ".join(wordArr)

            cL = []
            for part in arr:
                for char in part:
                    if u'\u4e00' <= char <= u'\u9fa5':
                        cL.append(part)
                        break
            # ========================
            w = Word(word, " ".join(cL))
            w.chineseList = cL
            wordList.addWord(w)
            i += 1


if __name__ == '__main__':
    # main()
    # matchStr()
    getExcl()
    input("end...")
