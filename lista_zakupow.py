purchase_list ={'piekarnia':['chleb','bułki','pączek'], 'warzywniak':['Marchew', 'Seler', 'Rukola'], 'Rossmann':['szampon','mydło']}

quantity_of_products=0
for place, products in purchase_list.items():
    products =[product.capitalize() for product in products]
    print(f'Idę do {place.capitalize()} i kupuję tam {products}')
    quantity_of_products += len(products)
print(f'Kupuję w sumie {quantity_of_products} produktów')