try:
    5 / 0
except (ZeroDivisionError, ArithmeticError, AssertionError) as e:
    if isinstance(e, ArithmeticError) and not isinstance(e, ZeroDivisionError):
        print('ArithmeticError')
    else:
        print(type(e).__name__)
