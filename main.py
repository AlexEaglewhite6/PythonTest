print("0 в качестве знака операции"
      "\nзавершит работу программы\n")

def calc(s,a,b):
    if s == '+':
        return a + b
    elif s == '-':
        return a - b
    elif s == '*':
        return a * b
    elif s == '/':
        if b != 0:
            return a / b
        else:
            return ZeroDivisionError

while True:
    s = input("Знак (+, -, *, /): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        a = float(input("a = "))
        b = float(input("b = "))
        if s == '+':
            print("%.2f" % calc(s, a, b))
        elif s == '-':
            print("%.2f" % calc(s, a, b))
        elif s == '*':
            print("%.2f" % calc(s, a, b))
        elif s == '/':
            if b != 0:
                print("%.2f" % calc(s, a, b))
            else:
                print("Деление на ноль!")


