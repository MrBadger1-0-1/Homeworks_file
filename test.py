count_dict = {}
with open('1.txt', encoding='utf-8') as file:
    count_1 = 0
    text_1 = []
    for line in file.readlines():
        count_1 += 1
        text_1.append(line)
    count_dict['1.txt'] = text_1

with open('2.txt', encoding='utf-8') as file:
    count_2 = 0
    text_2 = []
    for line in file.readlines():
        count_2 += 1
        text_2.append(line)
    count_dict['2.txt'] = text_2

with open('3.txt', encoding='utf-8') as file:
    count_3 = 0
    text_3 = []
    for line in file.readlines():
        count_3 += 1
        text_3.append(line)
    count_dict['3.txt'] = text_3


sorted_dict = sorted(count_dict.items(), key=lambda x: len(x[1]))
# print(sorted_dict)

with open('result.txt', 'w', encoding='utf-8') as file:
    for line in sorted_dict:
        file.write('\n'.join(line[0]))
        print(line)
        # for second_line in line:
        #     file.write('\n'.join(second_line))

