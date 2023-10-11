# Homeworks Klimentii
#------------------------------------------------------ Задание № 1
def my_cook_book():
    with open('recept.txt', encoding='utf-8') as file:
        cookbook = {}
        for line in file.read().split('\n\n'):
            name, values, *args = line.split('\n')
            cook_li = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                cook_li.append({'ingredient_name': ingredient_name,'quantity': quantity,'measure': measure})
                cookbook[name] = cook_li
    return cookbook

# print(my_cook_book())
# print(my_cook_book()['Омлет'])
#------------------------------------------------------ Задание № 2
def get_shop_list_by_dishes(dishes, person_count):
    dish_list = {}
    for dish in dishes:
        for ingredient in my_cook_book()[dish]:
            ingredient['quantity'] = ingredient['quantity'] * person_count
            dish_list[ingredient['ingredient_name']] = {ingredient['measure'], ingredient['quantity']}

    return dish_list

# print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
#------------------------------------------------------ Задание № 3
count_dict = {}
with open('1.txt', encoding='utf-8') as file:
    text_1 = []
    for line in file.readlines():
        text_1.append(line)
    count_dict['1.txt'] = text_1

with open('2.txt', encoding='utf-8') as file:
    text_2 = []
    for line in file.readlines():
        text_2.append(line)
    count_dict['2.txt'] = text_2

with open('3.txt', encoding='utf-8') as file:
    text_3 = []
    for line in file.readlines():
        text_3.append(line)
    count_dict['3.txt'] = text_3

sorted_dict = sorted(count_dict.items(), key=lambda x: len(x[1]))

with open('result.txt', 'w', encoding='utf-8') as file:
    count = 1
    for element in sorted_dict:
        for j in element:
            if type(j) == str:
                file.write(f'{j}\n{count}\n')
                count += 1
            else:
                conver = ''.join(map(str,j))
                file.write(f'{conver}\n')
