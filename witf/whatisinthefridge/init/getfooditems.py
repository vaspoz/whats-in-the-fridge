# -*- coding: utf-8 -*-
import requests


def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


arr = []


def func():
    global arr
    file = open('food.txt')
    with file as f:
        [arr.append(a) for a in f.read().split(',') if isEnglish(a)]


if __name__ == '__main__':
    func()
    print(arr)
