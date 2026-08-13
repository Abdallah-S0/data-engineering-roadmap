#1. Write a list named products of 10 dicts, each with keys name, price, category.



prod1={'name': 'pizza',
       'price': 50 ,
       'category':'food'}

prod2={'name': 'burger',
       'price': 30 ,
       'category':'food'}

prod3={'name': 'shawerma',
       'price': 30 ,
       'category':'food'}

prod4={'name': 'orange juice',
       'price': 15 ,
       'category':'drinks'}

prod5={'name': 'water',
       'price': 5 ,
       'category':'drinks'}

prod6={'name': 'cola',
       'price': 10 ,
       'category':'drinks'}

prod7={'name': 'doner',
       'price': 30 ,
       'category':'food'}

prod8={'name': 'ayran',
       'price': 15 ,
       'category':'drinks'}

prod9={'name': 'borito',
       'price': 30 ,
       'category':'food'}

prod10={'name': 'falafel',
       'price': 20 ,
       'category':'food'}
products = [prod1, prod2, prod3, prod4, prod5, prod6, prod7,prod8, prod9, prod10]

"""for i in products:
    for x , y in i.items():
        print(x, ':' , y)"""

for product in products:
    print(f'\n---{product['name'].title()}---')
    for k,v in product.items():
        print(f'{k}: {v}')
        
       