first = int(input("Введите произвольное число: "))
second = int(input("Введите пограничное число: "))
if first > second * 3:
    print("Произвольное число больше пограничного более, чем в три раза")
elif first > second:
    print("Произвольное больше, чем пограничное")
elif first < second:
    print("Пограничное число больше, чем произвольное")
