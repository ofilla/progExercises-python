# input parameter
products = ['Wurst', 'Kaese', 'Brot', 'DVD']
numbers_to_buy = [1, 1, 1, 2]
wallet = {50: 1}

products_prices = {
    'Wurst': 4.2,
    'Kaese': 2.3,
    'Brot': 2.1,
    'DVD': 12
}
    
# init
preceeding_spaces = " "*24 # 24 = 3*\t
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

# what is given?
given = 0
rest = total
while rest > 0:
    # bills only, coins are not implemented
    for bill in (500, 200, 100, 50, 20, 10, 5):
        if wallet.get(bill, 0) > 0:
            # wallet contains at least one of this kind of bill
            wallet[bill] -= 1
            given += bill # pay
            rest = total - given
            break
    if bill == 5:
        # wallet is empty
        print
        print "not enough money to buy all items"
        break

if rest <= 0:
    print 'Gegeben                 ' + pricestring(given)
    print
    print 'Zurueck                 ' + pricestring(- rest)
