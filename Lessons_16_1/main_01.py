class TryExec:

    def func_1(self):
        # try:
        self.func_2()
        # except ZeroDivisionError:
        #     print('Возникновение ошибки в методе func_1')
        print('Штатная работа метода func_1')

    def func_2(self):
        # try:
        self.func_3()
        # except ZeroDivisionError:
        #     print('Возникновение ошибки в методе func_2')
        print('Штатная работа метода func_2')

    def func_3(self):
        try:
            100 / 0
        except ZeroDivisionError:
            print('Возникновение ошибки в методе func_3')
        print('Штатная работа метода func_3')

somr_obj = TryExec()
somr_obj.func_1()
