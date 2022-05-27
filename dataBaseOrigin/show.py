# -*- encoding: utf-8 -*-
"""
PyCharm show 展示词根词缀表字典序
2021年12月21日
by littlefean
"""


def main():
    with open("词根词缀.txt", encoding="utf-8") as f:
        lineArr = f.readlines()
    dic = {}
    for line in lineArr:
        if line.strip() == "":
            continue
        key, end = line.split()
        dic[key] = end
    print(dic)
    for i in sorted(dic):
        print(i, "\t\t", dic[i])
    return None


if __name__ == "__main__":
    main()
