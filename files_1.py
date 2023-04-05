from pprint import pprint

files_name = 'resipes.txt'

cook_book = {}
def сook_book_creation():

    with open(files_name, encoding='UTF-8') as file:
        for line in file:
            dep_name = line.strip()
            ingredients_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredients_count):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            file.readline()
            cook_book[dep_name] = ingredients

    return pprint(cook_book, sort_dicts=False, width=100)

сook_book_creation()

def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = {}

    for dish in dishes:
        for ingredient in cook_book[dish]:
            shop_list_new = dict(ingredient)

            shop_list_new['quantity'] *= person_count
            if shop_list_new['ingredient_name'] not in ingr_list:
                ingr_list[shop_list_new['ingredient_name']] = shop_list_new
            else:
                ingr_list[shop_list_new['ingredient_name']['quantity']] += ingr_list
    for i in ingr_list.values():
         del i['ingredient_name']
    pprint(ingr_list, sort_dicts=False)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)



