#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
英语单词类
2021年06月21日
by littlefean
"""
from copy import deepcopy
from random import choice


class Word:
    chineseObjType = {
        "a.": [],
        "v.": [],
        "n.": [],
        "vi.": [],
        "ad.": [],
        "conj.": [],
        'vt.': [],
        "pron.": []
    }

    def __init__(self, name: str, chinese: str, chineseList=None, speaker=""):
        """
        单词类的构造方法
        :param name: 英文单词
        :param chinese: 汉语解释
        :param chineseList: 汉语解释列表
        """
        if chineseList is None:
            chineseList = []
        self.name = name
        self.chinese = chinese.strip()
        self.chineseList = chineseList
        self.speaker = speaker  # 音标
        self.chineseObj = deepcopy(self.chineseObjType)

    def toLineStr(self):
        """返回该单词的一行字符串形式
        主要用于打印单词库"""
        return f"{self.name}\t\t{self.chinese}"

    def __str__(self):
        """打印单词的详细形式，主要用于程序测试"""
        res = ""
        res += f"\t{self.name}\t{self.speaker}\n"
        res += f"\t【所有翻译内容】{self.chinese}\t【翻译列表】{self.chineseList}\n"
        res += f"\t【分词性的翻译】\n"
        for k, v in self.chineseObj.items():
            if len(v) != 0:
                res += f"\t\t{k}\t{v}\n"
        res += "\n"
        return res

    def __or__(self, other):
        """用于合并两个单词，返回合并后的单词"""
        res = deepcopy(self)
        for k, v in other.chineseObj.items():
            if res.chineseObj.get(k) is None:
                print(f"-{k}-{type(k)}-", self.chineseObj)
                print(other.chineseObj)
                ...
            elif v and res.chineseObj.get(k) == []:
                # 如果对方有但是自己没有，那就把对方的加进来
                res.chineseObj[k] = v
            elif v and res.chineseObj.get(k) != []:
                # 如果对方有并且自己也有，那就看谁的更长，就要谁的
                if len(self.chineseObj.get(k)) > len(v):
                    res.chineseObj[k] = res.chineseObj.get(k)
                else:
                    res.chineseObj[k] = v
        return res

    def shortStr(self):
        """返回该单词的简单表示形式"""
        return f"[{self.name} {choice(self.chineseList)}]"

    def toString(self):
        """单行的单词打印形式，主要用于大量的程序测试"""
        return "{:<15}\t{:<20}\t{:<20}\t{:<40}\t{:<30}".format(
            self.name, self.speaker, self.chinese, self.dicToStr(), str(self.chineseList)
        )

    def toTxtLineString(self):
        """返回在txt文本里一行的形式"""
        return "{:<15}\t{:<20}\t{:<20}\n".format(
            self.name, self.speaker, self.chinese
        )

    def toHtmlString(self):
        """返回此单词的html盒子表示形式"""
        """
            <div class="word">
                <span class="name">due</span>
                <span class="chinese">由于</span>
            </div>
        """

        # return f"""<div class="word">
        #         <div class="name">{self.name}</div>
        #         <div class="chinese">{self.chinese}</div>
        #     </div>"""
        return f"""<div class="word">
                {self.name}
                <div class="chinese">{self.chinese}</div>
            </div>"""

    def dicToStr(self):
        """返回汉语翻译字典的字符串形式"""
        res = "{"
        for k, v in self.chineseObj.items():
            if len(v) != 0:
                res += f"{k}:{v}\t"
        res = res.rstrip()
        res += "}"
        return res

    def toEasyJs(self):
        return "{" + f"name: '{self.name}', chinese: '{self.chinese}'" + "}"

    def toDic(self):
        """把自己转化成字典对象的形式"""
        res = {
            "name": self.name,
            "chinese": self.chinese,
            "chineseList": self.chineseList,
            # "speaker": self.speaker,
            # "chineseObj": self.chineseObj
        }
        return res

    def getFirstKind(self):
        """获取这个单词的第一词性"""
        arr = self.chinese.split(".")
        return arr[0]

    def toExclStr(self):
        """返回excl的行形式"""
        return f"{self.name}\t{self.speaker}\t{self.chinese}\t{self.getFirstKind()}\t{len(self.name)}"


if __name__ == '__main__':
    te = {"a": 1}
    print(te.get("a"))
