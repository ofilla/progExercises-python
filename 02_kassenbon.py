products = ['Wurst', 'Kaese', 'Brot', 'DVD']
numbers_to_buy = [1, 1, 1, 2]


class Bon:
    preceeding_spaces = " "*24 # 24 = 3*\t
    products_prices = {
                'Wurst': 4.2,
                'Kaese': 2.3,
                'Brot': 2.1,
                'DVD': 12
        }
    
    def __init__(self, products, numbers_to_buy):
        self.maxprice = 0
        self.total = 0
        self.bon = []
        
        self.basket = zip(numbers_to_buy, products)
        
        self.calc()
        
    def calc(self):
        self.get_upper_part()
        self.add_seperator()
        self.add_sum()

    def pricestring(self, price):
        return '{0:6.2f} EUR'.format(price)
    
    def get_upper_part(self):
        for number, product in self.basket:
            price = self.products_prices[product]
            
            item_line = product + '\t'
            item_line += str(number) + ' x ' + self.pricestring(price)
            self.bon.append(item_line)
            
            sum = number * price
            sum_line = self.preceeding_spaces + self.pricestring(sum)
            self.bon.append(sum_line)
            self.total += sum

    def add_seperator(self):
        self.bon.append('-' * len(self.preceeding_spaces + self.pricestring(self.maxprice)))

    def add_sum(self):
        self.bon.append('Gesamt                  ' + self.pricestring(self.total))
        self.bon.append('Gegeben                 ' + self.pricestring(50))
        
        self.bon.append('\n')
        self.bon.append('Zurueck                 ' + self.pricestring(50 - self.total))

    def __str__(self):
        s = ''
        for line in self.bon:
            s += line + '\n'
        return s

bon = Bon(products, numbers_to_buy)

print bon