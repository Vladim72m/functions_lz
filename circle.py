def operation(a):   # функция вывода
    b = a * 2 * 3.14 # длина окружности
    c = 3.14 * a * a # площадь круга
    print('площадь круга:', c, 'длина окружности', b)

def main():
    a = int(input('Радиус круга:')) # ввод радиуса
    operation(a)
if __name__ == "__main__":
    main()
