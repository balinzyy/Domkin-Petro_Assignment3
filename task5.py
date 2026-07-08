sales_data = [{"product": "Смартфон","category": "Електроніка","quantity": 1,"price": 15000},
              {"product": "Книга 'Python для всіх'","category":"Книги","quantity": 2,"price": 700},
              {"product": "Навушники","category": "Електроніка","quantity": 2,"price": 2500},
              {"product": "Чайник","category": "Побутова техніка","quantity": 1,"price": 1200},
              {"product": "Книга 'Алгоритми'","category": "Книги","quantity": 1,"price": 900},
              {"product": "Ноутбук","category": "Електроніка","quantity": 1,"price": 32000}]

category_report = {}

for i in sales_data:
    category = i["category"]
    if category not in category_report:
        category_report[category] = {'total_revenue': 0, 'total_items_sold': 0}
        category_report[category]['total_revenue'] += i["price"] * i["quantity"]
        category_report[category]['total_items_sold'] += i["quantity"]
    else:
        category_report[category]['total_revenue'] += i["price"]*i["quantity"]
        category_report[category]['total_items_sold'] += i["quantity"]

for i in category_report:
    print(f"'{i}': {category_report[i]}")