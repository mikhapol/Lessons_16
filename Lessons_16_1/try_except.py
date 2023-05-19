try:
    a, b = map(int, input().split())
    result = a / b
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
else:
    print('Код, который выполняется, когда не возникло исключений.')
finally:
    print('Код, который выполняется всегда.')
