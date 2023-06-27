def pack_backpack(items, max_weight):
    possible_items = []
    for item, weight in items.items():
        if weight <= max_weight:
            possible_items.append(item)
            max_weight -= weight
    return possible_items

items = {'tent': 5, 'water': 3, 'food': 4, 'clothes': 2, 'first aid kit': 1}
max_weight = 10
print(pack_backpack(items, max_weight)) 