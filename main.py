import json

def get_shop_list_by_dishes(dish_list, person_count):
    ingr_dict = {}
    for dish in dish_list:
        if dish in cookbook.keys():
            for ingr in cookbook[dish]:
                if ingr['name'] in ingr_dict:
                    ingr_dict[ingr['name']]['quantity'] += person_count * int(ingr['quantity'])
                else:
                    ingr_dict[ingr['name']] = {
                        'measure': ingr['measure'],
                        'quantity': int(ingr['quantity']) * person_count
                    }
        else:
            print(f'{dish} - такого рецепта нет в моей книге')
    res = json.dumps(ingr_dict, ensure_ascii=False, indent=2)
    print(res)


with open('cookbook.txt', 'rt', encoding='utf-8') as f:
    cookbook = {}
    for dish in f:
        ingr_list = []
        for ingr in range(int(f.readline())):
            name, quantity, measure = f.readline().strip().split(' | ')
            ingr_list.append({
                        'name': name,
                        'quantity': quantity,
                        'measure': measure
                             })
        f.readline()
        cookbook[dish.strip()] = ingr_list

res = json.dumps(cookbook, ensure_ascii=False, indent=2)
print(res)
get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)