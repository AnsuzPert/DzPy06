#     Дан список, содержащий искажённые данные с должностями и именами сотрудников: ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

# Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду. Можно ли при этом не создавать новый список?

a = ['инженер-конструктор ИгоРь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in a:
    j = 0
    p=0
    while j < len(i):
        if i[j] ==" ":
            p=j
        j+=1
    # print (p, ' ' ,len(i))
    i[p:p+2].upper()
    i[p+2:len(i)].lower()
    s  =i[p:p+2].upper()+ i[p+2:len(i)].lower()
    print ('Привет, ',s)
