#!/usr/bin/env python
# coding: utf-8

# # 외장함수

# In[1]:


# argv_test.py
import sys
print(sys.argv)


# In[1]:


import os


# In[2]:


os.environ


# In[3]:


os.environ['PATH']


# In[4]:


os.getcwd()    # 현재 디렉터리 위치


# In[6]:


os.chdir("c:\\WINDOWS")    # 디렉터리 위치 변경


# In[7]:


os.getcwd()


# In[10]:


os.system("dir")    # 시스템 명령어 호출하기


# In[11]:


os.getcwd()


# In[73]:


os.listdir("C:/Users/82108/Documents/")


# In[15]:


import shutil
# shutil.copy('src.txt', 'dst.txt')    # 앞의 인수 내용을 뒤에 복사


# In[18]:


import glob


# In[26]:


glob.glob("C:/Users/82108/Documents/pythonbasic*")


# In[28]:


import tempfile


# In[29]:


filename = tempfile.mkstemp()


# In[30]:


filename


# In[31]:


import time


# In[32]:


time.time()


# In[34]:


time.localtime()


# In[39]:


time.ctime()


# In[40]:


time.asctime()


# In[43]:


time.strftime('%x', time.localtime(time.time()))


# In[45]:


time.strftime('%c',time.localtime(time.time()))


# In[46]:


for i in range(10):
    print(i)
    time.sleep(1)


# In[49]:


# Calendar

import calendar
print(calendar.calendar(2021))


# In[51]:


calendar.prmonth(2021,2)


# In[52]:


calendar.weekday(2021, 2, 22)    # 요일을 숫자로 알려줌


# In[54]:


calendar.monthrange(2021,2)    # 해당 달의 시작 요일과 며칠까지 있는지 알려줌


# In[57]:


# random

import random


# In[60]:


random.random()    # 실수 중 임의의 수 발생


# In[65]:


random.randint(1, 100)    # 정수 중 임의의 수 발생


# In[66]:


# 입력받은 함수에서 무작위로 돌려줌

def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number


# In[67]:


data = [1, 2, 3, 4, 5]
print(random_pop(data))


# In[70]:


random.shuffle(data)
data


# In[71]:


# webbrowser

import webbrowser


# In[72]:


webbrowser.open('http//google.com')


# # Application

# In[76]:


def GuGu(n):
    result = []
    result.append(n*1)
    result.append(n*2)
    result.append(n*3)
    result.append(n*4)
    result.append(n*5)
    result.append(n*6)
    result.append(n*7)
    result.append(n*8)
    result.append(n*9)
    return result
print(GuGu(2))
    


# In[79]:


i = 1
while i < 10:
    print(i)
    i += 1
    


# In[84]:


def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n*i)
        i = i + 1
    return result
    
print(GuGu(2))


# In[87]:


# Quiz 1 : 구구단을 for문으로 작성하세요.

def GuGu(n):
    result = []
    for i in range(1, 10):
        result.append(n*i)
    return result

print(GuGu(2))


# In[89]:


# def GuGu(n):
#     ans[a*n for a in range(1, 10)]    # List Comprehension 사용
#     return ans

# print(GuGu(2))


# In[90]:


n = 1
while n < 1000:    # 1~1000 출력
    print(n)
    n += 1


# In[91]:


# 1~1000 출력
for n in range(1, 1000):
    print(n)


# In[92]:


# 1~1000 중 3의 배수 출력
for n in range(1, 1000):
    if n % 3 == 0:
        print(n)


# In[93]:


# 1~1000 중 5의 배수 출력
for n in range(1, 1000):
    if n % 5 == 0:
        print(n)


# In[95]:


for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        print(n)


# In[96]:


for n in range(1, 1000):
    if n % 3 == 0 and n % 5 == 0:
        print(n)


# In[114]:


result = 0
for n in range(1, 1001):
    if n % 3 == 0 or n % 5 == 0:
        result += n
print(result)


# In[113]:


# while 문으로 풀기

result = 0
n = 1
while n < 1000:
    n += 1
    if n % 3 == 0 or n % 5 == 0:
        result += n
print(result)


# In[117]:


# 게시판 페이징하기

def getTotalPage(m,n):
    return m // n + 1

print(getTotalPage(5, 10))    # 5 : 총 게시물의 갯수, 10: 한페이지당 게시물 개수
print(getTotalPage(15, 10))
print(getTotalPage(25, 10))
print(getTotalPage(30, 10))    # 4 출력 >>> 틀림


# In[120]:


def getTotalPage(m,n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1

print(getTotalPage(5, 10))    # 5 : 총 게시물의 갯수, 10: 한페이지당 게시물 개수
print(getTotalPage(15, 10))
print(getTotalPage(25, 10))
print(getTotalPage(30, 10))
print(getTotalPage(40, 10)) 
print(getTotalPage(45, 10)) 


# In[122]:


# 메모장 만들기
import sys

option = sys.argv[1]
memo = sys.argv[2]

print(option)
print()
print(memo)


# In[123]:


import sys
option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()


# In[124]:


f = open('memo.txt', 'w')


# In[127]:


import os
os.getcwd()


# In[128]:


import os
os.chdir("C:/Users/82108/Documents/pythonbasic")


# In[130]:


f = open('memo.py', 'w')


# # Regular Expressions 정규표현식

# In[136]:


data = '''
park 800905-1049118
kim 700905-1059119
'''

result = []
for line in data.split('\n'):
    word_result = []
    for word in line.split(' '):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + '-' + '*******'
        word_result.append(word)
    result.append(' '.join(word_result))
print('\n'.join(result))


# In[133]:


txt = "50800"

x = txt.isdigit()

print(x)


# In[134]:


a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²

print(a.isdigit())
print(b.isdigit())


# In[141]:


import re

data = '''
park 800905-1049118
kim 700905-1059119
'''

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))


# In[157]:


import re
p = re.compile('[A-z]+')


# In[158]:


m = p.match('python')    # 'python'이 위의 정규 표현식에 부합하는가


# In[159]:


print(m)


# In[160]:


m = p.match('3 python')


# In[161]:


print(m)


# In[163]:


p = re.compile('[A-z]+')
m = p.match('String goes here')
if m:
    print('Match found: ', m.group())
else:
    print('No match')


# In[ ]:




