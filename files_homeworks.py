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
    count_1 = 0
    for line in file.readlines():
        count_1 += 1
    count_dict['1.txt'] = count_1

with open('2.txt', encoding='utf-8') as file:
    count_2 = 0
    for line in file.readlines():
        count_2 += 1
    count_dict['2.txt'] = count_2

with open('3.txt', encoding='utf-8') as file:
    count_3 = 0
    for line in file.readlines():
        count_3 += 1
    count_dict['3.txt'] = count_3

# print(sorted(count_list))
# sorted_dict = dict(sorted(count_dict.items()))
# print(sorted_dict)
# with open('result.txt', 'w', encoding='utf-8') as file:
#     file.write('')