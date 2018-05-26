to_buy = [
            ('Wurst', 1),
            ('Kaese', 1),
            ('Brot', 1),
            ('DVD', 2)
        ]

prices = {
            'Wurst': 4.20,
            'Kaese': 2.30,
            'Brot': 2.10,
            'DVD': 12.00
        }

def pricestring(price):
    return '{0:5.2f} EUR'.format(price)

for product, number in to_buy:
    price = prices[product]
    s = product + '\t'
    s += str(number) + ' x '
    s += pricestring(price)
    print s
    
    total = number * price
    euro = int(total)
    cent = int((total - euro) * 100)
    s = str(euro) + '.' + str(cent)
    print "\t\t\t" + pricestring(total)
