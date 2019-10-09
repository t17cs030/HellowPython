'''
Created on 2019/10/09

@author: t17cs030
'''
import random
a=random.randint(1,3)
b=random.randint(1,3)

if a==1:
    aH = "グー"
elif a==2:
    aH = "チョキ"
else:
    aH = "パー"

if b==1:
    bH = "グー"
elif b==2:
    bH = "チョキ"
else:
    bH = "パー"

if a==b:
    w="引き分け"
elif a+1==b:
    w="Aの勝ち"
elif a==b+1:
    w="Bの勝ち"
elif a-2==b:
    w="Aの勝ち"
elif a==b-2:
    w="Bの勝ち"
    
print("Aの手: " + aH + " vs Bの手: " + bH + " -> " + w)