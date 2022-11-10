#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    test_russe.py
# @Author:      Oghenemarho ORUKELE
from unittest import TestCase
import russe


# @Time:        10/11/2022 12:58
class Test(TestCase):
    def test_pass(self):
        self.assertEqual(russe.russe(981, 1234), 1210554)

    def test_fail(self):
        self.assertIsNot(russe.russe(100, 100), 1210554)
