# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 15:41:55 2023

@author: User
"""
h = float(input("請輸入你的身高(公尺):"))
w = float(input("請輸入你的體重(公斤):"))
bmi = w/(h**2)
print(f"你的BMI值為{bmi:.2f}")