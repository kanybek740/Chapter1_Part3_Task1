# Попросить пользователя ввести текст. В результате вывести процент букв в верхнем
# регистре (заглавные) и в нижнем регистре (прописные).


a = input('vvedite text: ')
dlina = len(a)
lower = upper = 0
for i in a:
    if i.islower():
        lower = lower + 1
    elif i.isupper():
        upper = upper + 1
print(f' procsent malenkih slov {lower/dlina * 100} %')
print(f' procsent bolwih slov {upper/dlina * 100} %')