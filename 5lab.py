words_list = input("Введите список слов через запятую: ").split(", ")  # ввод строки
words_lots = set(words_list)  # формирование множества
lots_length = len(words_lots)
print("Создано множество из {} слов(-а): ".format(lots_length))
print(words_lots)

values_list = []
for i in range(lots_length):
    print("Дайте толкование {} слова".format(i + 1))
    value = input()
    values_list.append(value)

new_dict = dict(zip(words_lots, values_list))
print("Словарь: {}".format(new_dict))
