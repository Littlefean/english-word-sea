# -*- encoding: utf-8 -*-
"""
词海程序的单词训练入口
2021年12月01日
by littlefean
"""
from Practice import *
from word import Word


def main():
    w = WordList.initialize()
    addWords(w, "dataBaseOrigin/相对于岳同学的六级高频词")
    print(w)
    fastPractice(w, "yxt")
    easyPractice(w)
    return None


def addWords(wordList: WordList, path):
    """从自己写的txt文本文件里生成一个词库
    格式：
    英文 + 若干空格 + 中文"""
    with open(path, "r", encoding='utf-8') as f:
        for line in f.readlines():
            if len(line.strip()) > 0:
                eng, chinese = line.split()
                w = Word(eng, chinese)
                wordList.addWord(w)
    return


if __name__ == "__main__":
    main()
