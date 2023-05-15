"""
Шебанг (shebang) — последовательность символов #!, которая указывает операционной системе,
какую программу использовать для анализа остальной части файла. Пример шебанга: #!/bin/bash
"""


class ShellException(Exception):
    pass


class EmptyShellException(Exception):
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self.message = args[0]
        else:
            self.message = 'Файл не может быть ""'


class ShebangShellException(Exception):
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self.message = args[0]
        else:
            self.message = 'Должен быть "#"'


class ShellExecuter:
    def __init__(self, file_content):
        self.file_content = file_content
        if len(self.file_content) == 0:
            raise EmptyShellException  # ('Файл не может быть пустым')

        if self.file_content[0] != '#':
            raise ShebangShellException  # ('Должен быть шебанг')


content_1 = '#!/bin/bash'  # правильно
content_2 = '!/bin/bash'  # Должен быть шебанг или Должен быть "#"
content_3 = ''  # Файл не может быть пустым или Файл не может быть ""

try:
    shell_executer = ShellExecuter(content_1)
except EmptyShellException as ex:
    print(ex.message)
except ShebangShellException as ex:
    print(ex.message)
else:
    print('Всё прошло хорошо')
print('~~~~~~~~~~~~~~~~~~~~~~~~')
try:
    shell_executer = ShellExecuter(content_2)
except EmptyShellException as ex:
    print(ex.message)
except ShebangShellException as ex:
    print(ex.message)
else:
    print('Всё прошло хорошо')
print('~~~~~~~~~~~~~~~~~~~~~~~~')
try:
    shell_executer = ShellExecuter(content_3)
except EmptyShellException as ex:
    print(ex.message)
except ShebangShellException as ex:
    print(ex.message)
else:
    print('Всё прошло хорошо')
