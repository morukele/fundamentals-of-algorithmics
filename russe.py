#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    russe.py
# @Author:      Oghenemarho ORUKELE
# @Time:        10/11/2022 12:30

def russe(m, n):
    result = 0
    while m > 0:
        if m % 2 != 0:
            result = result + n
        m = int(m / 2)
        n = n + n
    return result


if __name__ == "__main__":
    print(russe(981, 1234))
