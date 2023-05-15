class ShellScriptError(Exception):
    """Общий класс исключения для скриптов"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Неизвестная ошибка скрипта.'

    def __str__(self):
        return self.message


class ShellScriptEmpty(ShellScriptError):
    """Класс исключения при отсутствии кода скрипта"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл пустой.'


class ShellScriptShebang(ShellScriptError):
    """Класс исключения при отсутствии shebang"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'В файле отсутствует shebang.'


class ShellScript:
    """Класс для работы с шелл-скриптами."""

    def __init__(self, script: str):
        if not script:  # Если скрипт пустой
            raise ShellScriptEmpty
        elif script[0:2] != '#!':  # Если отсутствует shebang
            raise ShellScriptShebang
        else:
            self.script = script

    def evaluate(self):
        # Код исполнения скрипта
        pass


content_1 = '#!/bin/bash'  # правильно
content_2 = '!/bin/bash'  # Должен быть шебанг или Должен быть "#"
content_3 = ''  # Файл не может быть пустым или Файл не может быть ""
try:
    script = ShellScript(content_3)
except ShellScriptEmpty:
    print('Отсутствует текст скрипта.')
except ShellScriptShebang:
    print('Добавьте шебанг в скрипт.')
except ShellScriptError:
    print('Ошибка при работе скрипта.')
