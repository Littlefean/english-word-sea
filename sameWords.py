#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
单词相似度展现程序
2021年06月23日
by littlefean
"""
from typing import *
from word import Word
from words import WordList
import json


class Sames:
    """此类代表一个单词与多个与之有关系的单词相连组成的一种关系"""

    def __init__(self, word: Word, connectWords: WordList):
        self.word = word
        self.sameWords = connectWords

    @classmethod
    def initialize(cls, word: Word):
        """初始化工厂方法"""
        return cls(word, WordList.initialize())

    @classmethod
    def crateSames(cls, word: Word, wordArr: WordList, func, funcN=3):
        """根据一个目标单词，一个目标词表，一个匹配方法，创建出目标单词与词表里一些单词的关系
        这是一个静态工厂方法"""
        newArr = WordList.initialize()
        for w in wordArr:
            if w.name != word.name:
                try:
                    # todo 暂时这样做是否有可选参数的处理
                    if func(word, w, n=funcN):
                        newArr.addWord(w)
                except TypeError:
                    if func(word, w):
                        newArr.addWord(w)
        return cls(word, newArr)

    def __len__(self):
        return len(self.sameWords)

    def __str__(self):
        res = ""
        if len(self.sameWords) != 0:
            res += self.word.toTxtLineString()
            for ow in self.sameWords:
                res += "\t" + ow.toTxtLineString()
        return res

    def toDic(self):
        res = {
            "word": self.word.toDic(),
            "sameWords": self.sameWords.toDic()
        }
        return res


class SamesList:
    """多种相同关系组成的列表"""

    # todo 应该出一个图一样的关系，一种新的类 SameSea,里面的每一个节点都是Sames类实例
    # todo 想一想怎么用html的前端方法，把这个图或者关系网络来表示出来
    def __init__(self, array: List[Sames]):
        """类外部不要用此方法实例化对象"""
        self.array = array

    @classmethod
    def initialize(cls):
        """初始化方法"""
        return cls([])

    def append(self, item: Sames):
        """往单词表中增加一种关系"""
        self.array.append(item)

    @classmethod
    def wordListToSamesArr(cls, wordList: WordList, sameFunc, funcN=3):
        """根据一个词表，返回这个词表里每一个单词与其他所有单词所组成的关系的表
        此过程可能较长，可以打印进度"""
        res = cls.initialize()
        i = 0
        barLen = 100
        for w in wordList:
            res.append(Sames.crateSames(w, wordList, sameFunc, funcN=funcN))
            i += 1
            iCount = int((i / len(wordList)) * 100)
            print("=" * iCount + " " * (barLen - iCount) + "|" + f"{i} / {len(wordList)}")
        return res

    def __str__(self):
        res = ""
        for sames in self.array:
            if len(sames) != 0:
                res += str(sames)
                res += "-" * 10 + "\n"
        return res

    def saveTxt(self, fileName: str):
        """把这个关系列表保存成txt文件"""
        with open(f"samesListOut/{fileName}.txt", "w", encoding="utf-8") as f:
            f.write(str(self))

    def toDic(self):
        array = []
        for item in self.array:
            if len(item.sameWords) != 0:
                array.append(item.toDic())
        res = {
            "array": array
        }
        return res

    def saveJson(self, fileName: str):
        dicStr = self.toDic()
        jsonStr = json.dumps(dicStr, ensure_ascii=False)
        with open(f"wordSeaHtml/json/{fileName}.json", "w", encoding="utf-8") as f:
            f.write(jsonStr)


def wordInWord(word1: Word, word2: Word) -> bool:
    """一个单词，一个词表，看看词表里那些单词和这个目标单词相似
    返回相似单词组成的新词表
    此相似度匹配算法是名称是否在内"""
    if word1.name in word2.name:
        return True
    elif word2.name in word1.name:
        return True
    else:
        return False


def lenSame(word1: Word, word2: Word, n=3) -> bool:
    """两个单词长度相同，只差了n个字母不一样"""
    # todo bug
    if len(word1.name) == len(word2.name):
        count = 0
        for i in range(len(word1.name)):
            if word1.name[i] == word2.name[i]:
                count += 1
        return count == len(word1.name) - n
    else:
        return False


def partInPart(word1: Word, word2: Word, n=3) -> bool:
    """含有长度为n的公共子串"""
    maxN = _maxLineLen(_twoWordArray(word1.name, word2.name))
    return maxN >= n


def sameStart(word1: Word, word2: Word, n=3) -> bool:
    """都以一定长度的子串开头"""
    maxN = _maxFirstLineLen(_twoWordArray(word1.name, word2.name))
    return maxN >= n


def sameEnd(word1: Word, word2: Word, n=3) -> bool:
    """都以一定长度的子串结尾"""
    maxN = _maxLastLineLen(_twoWordArray(word1.name, word2.name))
    return maxN >= n


def sameChineseWord(word1: Word, word2: Word, n=3) -> bool:
    """含有相同的汉语意思，相同汉字的字数至少为n"""
    maxN = _sameChCharCount(word1, word2)
    return maxN >= n


def sameChinese(word1: Word, word2: Word) -> bool:
    """含有相同的汉语词"""
    # print(word1.chineseList, word2.chineseList)
    if word1.chineseList == [''] or word2.chineseList == ['']:
        return False
    w1cArr = word1.chineseList
    w2cArr = word2.chineseList
    if "" in w1cArr:
        w1cArr.remove("")
    if "" in w2cArr:
        w2cArr.remove("")
    set1 = set(w1cArr)
    set2 = set(w2cArr)
    if len(set1 & set2) == 0:
        for w1 in w1cArr:
            if len(w1) == 1:
                continue
            for w2 in w2cArr:
                if w1 in w2 or w2 in w1:
                    return True
    else:
        return True


def chineseInWord(word: Word, chineseChar: str) -> bool:
    """判断一个汉字是不是在英语单词的汉语解释里"""
    return chineseChar in word.chinese


def _sameChCharCount(word1: Word, word2: Word):
    """返回两个单词中汉语解释相同汉字的数量"""
    ignoreWords = "的 地".split()
    set1 = set()
    set2 = set()
    for char1 in set(word1.chinese):
        if _isChineseChar(char1):
            set1.add(char1)
    for char2 in set(word2.chinese):
        if _isChineseChar(char2):
            set2.add(char2)
    # print(set1, set2)
    for igWord in ignoreWords:
        if igWord in set1:
            set1.remove(igWord)
        if igWord in set2:
            set2.remove(igWord)
    return len(set1 & set2)


def _isChineseChar(char: str):
    """判断一个字符是不是汉语字符"""
    return u'\u4e00' <= char <= u'\u9fa5'


def _twoWordArray(word1: str, word2: str) -> List[List[int]]:
    """
    返回两个单词的01二维数组
    :param word1:
    :param word2:
    :return:
    """
    res = []
    for c1 in word1:
        line = []
        for c2 in word2:
            if c2 == c1:
                line.append(1)
            else:
                line.append(0)
        res.append(line)
    return res


def _maxLineLen(arr: List[List[int]]):
    """返回二维矩阵中最长斜线长度"""
    maxCount = 0
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            count = 0
            offsetX, offsetY = x, y
            while arr[offsetY][offsetX] == 1:
                count += 1
                offsetX += 1
                offsetY += 1
                if offsetX not in range(len(arr[0])) or offsetY not in range(len(arr)):
                    break
            if count > maxCount:
                maxCount = count
    return maxCount


def _maxFirstLineLen(arr: List[List[int]]):
    """返回二维矩阵中最长斜线长度"""
    count = 0
    offsetX, offsetY = 0, 0
    while arr[offsetY][offsetX] == 1:
        count += 1
        offsetX += 1
        offsetY += 1
        if offsetX not in range(len(arr[0])) or offsetY not in range(len(arr)):
            break
    return count


def _maxLastLineLen(arr: List[List[int]]):
    """返回二维矩阵中最长斜线长度"""
    count = 0
    offsetX, offsetY = len(arr[0]) - 1, len(arr) - 1
    while arr[offsetY][offsetX] == 1:
        count += 1
        offsetX -= 1
        offsetY -= 1
        if offsetX not in range(len(arr[0])) or offsetY not in range(len(arr)):
            break
    return count


def _printArray(arr: List[List[int]]):
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            print(arr[y][x], end=" ")
        print()


if __name__ == '__main__':
    array_ = _twoWordArray("earthquake", "earth")
    _printArray(array_)
    print(_maxLineLen(array_))
    ...
