products = ['Wurst', 'Kaese', 'Brot', 'DVD']
numbers_to_buy = [1, 1, 1, 2]


preceeding_spaces = " "*24 # 24 = 3*\t
products_prices = {
    'Wurst': 4.2,
    'Kaese': 2.3,
    'Brot': 2.1,
    'DVD': 12
}
    
# init
maxprice = 0
total = 0
bon = []

basket = zip(numbers_to_buy, products)

def pricestring(price):
    return '{0:6.2f} EUR'.format(price)

# upper part    
for number, product in basket:
    price = products_prices[product]
    
    item_line = product + '\t'
    item_line += str(number) + ' x ' + pricestring(price)
    print item_line
    
    sum = number * price
    print preceeding_spaces + pricestring(sum)
    total += sum

# seperator
print '-' * len(preceeding_spaces + pricestring(maxprice))

# lower part
print 'Gesamt                  ' + pricestring(total)
print 'Gegeben                 ' + pricestring(50)

print
print 'Zurueck                 ' + pricestring(50 - total)
