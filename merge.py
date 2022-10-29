class Concatenation:
        def __init__(self):
            pass
# Функция сложения двух аргументов.
# Если оба числа - без проблем.
# Если один из аргументов строка, то делается попытка привести его к численному значению,
# и если это возможно то опять происходит сложение числоваых аргументов.
# Если строку невозможно представить в виде числа, то произойдет конткатенация строк
# и на выходе будет строка

        def concat(self, a, b):

            def is_digit(c):
                if c.isdigit():
                    return True
                else:
                    try:
                        float(c)
                        return True
                    except ValueError:
                        return False


            # Оба аргумента числовые (не строки), просто суммируем
            if (not isinstance(a, str)) and (not isinstance(b, str)):
                return a + b
            else:
                # a число, b преобразующаяся в число строка, суммируем
                if (not isinstance(a, str)) and is_digit(b):
                    return a + float(b)
                else:
                    # b число, a преобразующаяся в число строка, суммируем
                    if (not isinstance(b, str)) and is_digit(a):
                        return float(a) + b
                    else:
                        # Оба агрумента строки, но их можно привести к числу - суммируем
                        if is_digit(a) and is_digit(b):
                            return float(a) + float(b)
                        else:
                            # суммирование не пройдет в любом варианте, конкатенируем
                            return str(a)+str(b)

