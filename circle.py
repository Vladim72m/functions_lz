a = int(input('Радиус круга:'))
def operation(a):
    b = a * 2 * 3.14
    c = 3.14 * a * a
    return ('площадь круга:', c, 'длина окружности', b)
print (operation(a))
