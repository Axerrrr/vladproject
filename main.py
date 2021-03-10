import os                                                           # Подключаю os для создания директории
import uuid                                                         # Для создания универсального ключа

path = "tables"
if os.path.exist and os.path.isdir:
    fout = open('tables.json', 'wt')
else:
    os.makedirs(path)                                               # Создаю директорию vladprojec
    fout = open('tables.json', 'wt')


class Metacalss(type):                                              # Создаю метакласс для реализации
    uuid.uuid4()                                                    # Уникальный ключ доступа для бд
    def __new__(cls, name, parents, attrs):
        if 'class id' not in attrs:
            attrs ['class_id'] = name.lower()
        return super().__new__(cls, name, parents, attrs)
    fout = open('table1.json', 'wt')
    print('oops/i/did/it/again',uuid(), file=fout)
    fout.close()
fout.close()


class Int(Metacalss,type):
    pass

class String(Metacalss,type):
    pass

class Float(Metacalss,type):
    pass

class Data(Metacalss,type):
    pass







"""
fout=open('table1.json','wt')
print('oops',file=fout)
fout.close()
 
 
 
 
 uuid.uuid4()
 
 """