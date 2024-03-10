def open_file():
    with open('cook_book.txt', 'r', encoding = 'utf-8') as file:
        cook_book = {}
        for foot in file:
            cook_book.update({foot: []})
            i = int(file.readline().strip())
            for _ in range(i):
                scroll = file.readline().strip(' | ')
                dict = {'ingredient_name': scroll[0], 'quantity': scroll[1], 'measure': scroll[2]}
                cook_book[foot].append(dict)
            file.readline()
    return cook_book

def cook_book():
    for cook, book in open_file().items():
        print(f'\n {book}')
        for i in book:
            print(f' {i['ingredient_name'] + ' - ' + i['quantity'] + ' ' + i['measure']}')


def list_shopping(shop):
    print('\nНужны следующие ингредиенты для блюда:\n')
    count = 1
    for lst, value in shop.items():
        print(f' {count}. {list} {value['quantity']} {value['measure']}')
        count +=1

def get_shop_list_by_dishes(dishes, person_count):
    list_shopping_1 = {}
    for ingredient in dishes:
        for ingred in open_file()[ingredient]:
            name = ingred.pop('ingredient_name')
            ingred['quantity'] = int(ingred['quantity']) * int(person_count)
            if name in list_shopping_1:
                ingred['quantity'] += list_shopping_1[name]['quantity']
                list_shopping_1.update({name: ingred})
    list_shopping(list_shopping_1)

def input_():
    try:
        scroll = list(input('Введите блюдо: ').split(', '))
        person = int(input('Введите количество персон: '))
        get_shop_list_by_dishes(scroll, person)
    except Exception:
        print('Ошибка')








