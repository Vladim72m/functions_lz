def operation(a):
    if a % 2 == 0:
        print('четное')
    else:
        print('нечетное')

def main():
    a = int(input('введите число:')) # ввод числа
    operation(a)
if __name__ == "__main__":
    main()
    
