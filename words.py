#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
单词库类
2021年06月21日
by littlefean
"""
import json
import random
from copy import deepcopy
from typing import List

from word import Word


class WordList:
    def __init__(self, array: List[Word]):
        """不要使用此方法创建实例"""
        self.array = array
        self._nameHash = set()

    @classmethod
    def initialize(cls):
        """创建一个空的，初始的实例对象"""
        return cls([])

    def __str__(self):
        result = ""
        for word in self.array:
            result += str(word)
        return result

    def __contains__(self, item):
        """判断某个单词对象是否在这个词列表里"""
        if type(item) == str:
            return item in self._nameHash
        elif type(item) == Word:
            return item.name in self._nameHash
        else:
            return False

    def __iter__(self):
        return iter(self.array)

    def __getitem__(self, index: int):
        return self.array[index]

    def __len__(self):
        return len(self.array)

    def __add__(self, other):
        """实现+操作，词表+词表 词表+单词"""
        res = self.initialize()
        for w in self:
            res.addWord(w)
        if type(other) is WordList:
            for ow in other:
                if ow not in self:
                    res.addWord(ow)
            return res
        elif type(other) is Word:
            res.addWord(other)
            return res

    def __and__(self, other):
        """单词表与单词表的与运算，即求交集"""
        res = self.initialize()
        for w in self:
            if w in other:
                res.addWord(w)
        return res

    def __or__(self, other):
        """表与表的或运算，即合并"""
        return self + other

    def __xor__(self, other):
        """表与表的异或运算，即获取两者都只有对方的部分"""
        res = self.initialize()
        for w in other:
            if w not in self:
                # 对方有的，自己没有的，加进来
                res.addWord(w)
        for w in self:
            if w not in other:
                res.addWord(w)
        return res

    def shuffle(self):
        """打乱自己的顺序"""
        random.shuffle(self.array)

    def addWord(self, word: Word):
        """往词库里增加一个单词"""
        # 此类用O(1)的时间复杂度保证了词不重复
        if word.name in self._nameHash:
            # print(word)
            self.array[self.index(word.name)] = self.array[self.index(word.name)] | word
        else:
            self.array.append(word)
            self._nameHash.add(word.name)

    def remove(self, word: str):
        """删除一个制定的单词"""
        if len(self) == 0:
            return None
        for w in self.array:
            if w.name == word.strip():
                self.array.remove(w)
                self._nameHash.remove(w.name)
                break

    def removeRight(self, n: int):
        """在词表中找到下标为n的单词，这个单词前面的单词以及包括这个单词将被保留，后面的单词全部剔除"""
        if n in range(len(self)):
            for i in range(n, len(self)):
                self._nameHash.remove(self[i].name)
            self.array = self.array[:n + 1]

    def cut(self, w1: str, w2: str):
        """选取该单词列表的一段区间[w1, w2]"""
        i = self.index(w1)
        j = self.index(w2)
        self.array = self.array[i: j + 1]
        self._nameHash = set()
        for w in self.array:
            self._nameHash.add(w.name)

    def saveTxtFile(self, fileName: str):
        """将此词序列保存到一个文件里"""
        with open(f"wordListOut/{fileName}.txt", "w", encoding="utf-8") as f:
            lineArray = []
            for word in self.array:
                lineArray.append(word.toTxtLineString())
            f.writelines(lineArray)

    def saveHtmlFile(self, fileName: str):
        """将此词序列保存到一个文件里"""
        with open(f"wordListOut/{fileName}.html", "w", encoding="utf-8") as f:
            content = ""
            for word in self:
                content += f"{word.toHtmlString()}\n"
            f.write(f"""<!DOCTYPE html>
                    <html>
                        <head>
                            <meta charset="utf-8">
                            <title></title>
                            <link rel="stylesheet" type="text/css" href="wordList.css"/>
                        </head>
                        <body>
                            {content}
                        </body>
                    </html>
                    <script type="text/javascript" src="wordList.js"></script>
            """)

    def index(self, word: str) -> int:
        """查询某个单词在列表里的下标位置"""
        res = 0
        for w in self.array:
            if w.name == word:
                return res
            res += 1
        else:
            raise Exception(f"未找到单词{word}")

    @staticmethod
    def stringToChineseList(string: str) -> list:
        """把字符串解析成一个汉语列表"""
        for key in Word.chineseObjType:
            string = string.replace(key, "")
        res = _mySplit(string, ',', '，', '/', ";", '；')
        newRes = []
        for r in res:
            newRes.append(r.strip())
        return newRes

    @staticmethod
    def stringToChineseObj(string) -> dict:
        """把一段汉语字符串解析成一个汉语字典对象并返回
        例如字符串是 :
            n.柏油，焦油 vt.涂或浇柏油/焦油于
            v.(on,with)喂养,饲养;(with)向…供给
            n.快乐,高兴 v.(使)高兴,(使)欣喜
            n.(tumor)(肿)瘤，肿块
            a.八十 pron.八十(个，只...)
        """
        res = deepcopy(Word.chineseObjType)
        keyIDic = {
            "a.": -1,
            "v.": -1,
            "n.": -1,
            "vi.": -1,
            "ad.": -1,
            "conj.": -1,
            'vt.': -1,
            "pron.": -1
        }
        seps = tuple(",/，；;")
        indexCountArr = []
        for key in res:
            if key in string:
                index = string.find(key)
                keyIDic[key] = index
                indexCountArr.append(index)
        indexCountArr = sorted(indexCountArr)
        for i in range(len(indexCountArr) - 1):
            leftIndex = indexCountArr[i]
            rightIndex = indexCountArr[i + 1]

            for key, value in keyIDic.items():
                if value == leftIndex:
                    typeContent = string[leftIndex + len(key):rightIndex]
                    res[key] += _mySplit(typeContent, *seps)
        else:
            # bug
            leftIndex = indexCountArr[-1]
            for key, value in keyIDic.items():
                if value == leftIndex:
                    typeContent = string[leftIndex + len(key):len(string)]
                    res[key] += _mySplit(typeContent, *seps)
        for k, v in res.items():
            a = []
            for string in v:
                a.append(string.strip())
            res[k] = a
        return res

    def toDic(self):
        res = []
        for item in self.array:
            res.append(item.toDic())
        return res

    def toJsonStr(self):
        """将自己单词列表转化为Json字符串"""
        dicStr = self.toDic()
        return json.dumps(dicStr, ensure_ascii=False)

    def saveJson(self, fileName: str):
        with open(f"wordSeaHtml/json/{fileName}.json", "w", encoding="utf-8") as f:
            f.write(self.toJsonStr())


def _mySplit(string, *seps):
    """将字符串string以多种分隔符分割形成一个列表
    'a b/c,d，e' --> ['a', 'b', 'c', 'd', 'e']
    但是如果是在小括号里面，会把它看成一个整体，不会分割。
    """
    result = []
    addStr = ""
    inTuple = False  # 表示是否进了括号
    for char in string:
        if char == "(":
            inTuple = True
        if char == ")":
            inTuple = False
        if char in seps:
            if addStr != "" and not inTuple:
                result.append(addStr)
                addStr = ""
            elif addStr != "" and inTuple:
                addStr += char
        else:
            addStr += char
    if addStr != "":
        result.append(addStr)
    return result


if __name__ == '__main__':
    # print(WordList.stringToChineseObj("n.柏油，焦油 vt.涂或浇柏油/焦油于"))
    # print(WordList.mySplit('n.快乐,高兴 v.(使，a)高兴,(使)欣喜', ' ', '/', ',', '，'))
    print(WordList.stringToChineseObj("n.柏油，焦油 vt.涂或浇柏油/焦油于"))
    print(WordList.stringToChineseObj("n.快乐,高兴 v.(使，a)高兴,(使)欣喜"))
    print(WordList.stringToChineseObj(" ad./a.向旁边(的),侧身,横着(的),斜着(的)"))
    # print(WordList.mySplit("n.快乐,高兴 v.(使，a)高兴,(使)欣喜", '/', ',', '，'))
    ...
