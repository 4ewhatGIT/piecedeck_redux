import os
import sys


class echo:
    def script():
        print(input('> '))


class explorer:

    def script():
        os.chdir('../workplace')
        while True:
            select = input('> ')
            if int(select) == 0:
                print(os.getcwd())
                os.chdir(input())
                print(os.getcwd())
            elif int(select) == 1:
                print(os.getcwd())
                input_ = input()
                if not os.path.isdir(input_):
                    os.mkdir(input_)
                print(os.getcwd())
            elif int(select) == 2:
                for dirpath, dirnames, filenames in os.walk("."):
                    # перебрать каталоги
                    for dirname in dirnames:
                        print("Каталог:", os.path.join(dirpath, dirname))
                    # перебрать файлы
                    for filename in filenames:
                        print("Файл:", os.path.join(dirpath, filename))



explorer.script()





stock_plugins = ['echo']
