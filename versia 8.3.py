#рост йолки
kk = ""
while kk != 000:
    print ("Сколько лет вашей ели? Введите число.")
    print ("Если не хотите продолжить, наберите 000.")
    kk = int(input())
    ch = kk - 1 
    g = 0
    r = 2
    p = 2
    n = 3
    while True:
        if kk == 000:
            break
        if ch == g:
            break
        if p == 50:
            n = 0
        p = p + n
        g = g + 1
        r = r + p
        if r > 3500:
            n = p / 100 * 30
            p = p - n
            p % 1
        if r > 200:
            n = 5
    print ("Рост вашей ели:")
    print (r)
    print ("Последний прирост:")
    print (p)        
print ("СПАСИБО ЗА ИСПОЛЬЗОВАНИЕ ПРОГРАММЫ!")


