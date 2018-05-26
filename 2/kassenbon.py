products = ['Wurst', 'Kaese', 'Brot', 'DVD']

numbers_to_buy = [1, 1, 1, 2]

products_prices = {
            'Wurst': 4.2,
            'Kaese': 2.3,
            'Brot': 2.1,
            'DVD': 12
        }

prices = []
for i in range(len(products)):
    total = numbers_to_buy[i] * products_prices[products[i]]
    prices.append(total)

# get correct price format
# shall be right-padded price
maxprice = max(prices)
maxprice_field_length = len('{0:5.2f}'.format(maxprice))
pricestring_format = '{}.2f'.format(maxprice_field_length)
pricestring_format = '{0:' + pricestring_format + '} EUR'
def pricestring(price):
    return pricestring_format.format(price)

for i in range(len(products)):
    product = products[i]
    number = numbers_to_buy[i]
    price = products_prices[product]
    
    s = product + '\t'
    s += str(number) + ' x ' + pricestring(price)
    print s
    print "\t\t\t" + pricestring(number * price)
