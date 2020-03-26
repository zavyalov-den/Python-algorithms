# 1) Определение количества различных подстрок с использованием хеш-функции. 
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:

# func("papa")
# 6
# func("sova")
# 9


import hashlib

def substr(string):

    arr = []

    for index, char in enumerate(string):
        i = index
        # subs = ''
        while i <= len(string)  and len(string[index:i]) < len(string):
            if i > index:
                subs = string[index:i]
                arr.append(hashlib.sha1(subs.encode('utf-8')).hexdigest())
            i += 1
    arr = set(arr)
    
    return len(arr)
    

print(substr('sova'))
