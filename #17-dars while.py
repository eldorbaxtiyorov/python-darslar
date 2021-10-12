# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 16:24:50 2021

@author: User
"""
# %% Task 1
"""
savol="Yaxshi ko'rgan kitobingizni ayting? "
savol += "(barcha kitoblarni kiritib bo'lgach 'exit' deb yozing): "
while  True:
    kitob=input(savol)
    if kitob== 'exit':
        break
    
print('Rahmat')

"""
# %% Task 2
"""
savol="Yoshingiz nechida? "
savol+="Dasturdan chiqish uchun 'exit' yoki 'quit' deb yozing "

while True:
    qiymat=input(savol)
    if qiymat=='exit' or qiymat=='quit':
        break
    yosh = int(qiymat)
    
    if yosh<7:
        narh = 2000
    elif 7<=yosh<18:
        narh = 3000
    elif 18<=yosh<65:
        narh = 10000
    else: narh = 0
    
    if narh==0:
        print("Sizga chipta bepul")
    else:
        print(f"Chipta {narh} so'm")

"""
# %% Task  3
"""
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if float(qiymat)<0:
        continue
    elif qiymat=='Exit':
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")    
"""