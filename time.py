def operation(a, b, c):
    return ((a * 3600) + (b * 60) + c) # количество секунд

def main():
    a = int(input('часы:'))   # ввод часов
    b = int(input('минуты:'))  # ввод минут
    c = int(input('секунды:'))  # ввод секунд
    abc = operation(a, b, c)
    print("В секундах:", abc)
    
if __name__ == "__main__":
    main()
    
