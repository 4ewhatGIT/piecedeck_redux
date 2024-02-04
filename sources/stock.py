import os


class explorer:

    @staticmethod
    def script():
        os.chdir('../workplace')
        while True:
            select = input('> ')
            match select.split()[0]:
                case 'cd':
                    os.chdir(' '.join(select.split()[1:]))
                case 'cd..':
                    os.chdir('..')
                case 'dir':
                    folders = [fname for fname in os.listdir(".") if os.path.isdir(fname)]
                    files = [fname for fname in os.listdir(".") if not os.path.isdir(fname)]
                    for f in folders:
                        print('}--', f)
                    for f in files:
                        print('}', f)
                case 'mkdir':
                    if not os.path.isdir(''.join(select.split()[1:])):
                        os.mkdir(' '.join(select.split()[1:]))
                case 'rmdir':
                    if os.path.isdir(''.join(select.split()[1:])):
                        os.rmdir(' '.join(select.split()[1:]))
                case 'echo':
                    if '>' in select.split()[1:]:
                        with open(select.split('>')[1].strip(), 'w') as file:
                            file.write(select.split('>')[0].removeprefix('echo '))
                case 'exit':
                    break


# explorer.script()


stock_plugins = ['explorer']
