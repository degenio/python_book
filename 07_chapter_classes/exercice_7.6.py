# Stock Class and Operations
class Stock:
    """Constructor"""
    def __init__(self, symbol, title, closing_price, current_price):
        self.symbol = symbol
        self.title = title
        self.closing_price = closing_price
        self.current_price = current_price

    def __str__(self):
        return "Stock  Symbol: {:<5} Title: {:<20} " \
               "Closing Price: {:7.2f} Current Price: {:7.2f} " \
               .format(self.symbol, self.title, self.closing_price, self.current_price)

    def percentage_change(self):
        return ((self.current_price / self.closing_price) - 1) * 100


def main():
    """Instantiate an object"""
    stock1 = Stock(title="Microsoft", symbol="MSFT", closing_price=123.24, current_price=127.04)
    print(stock1)

    # Display the percentage change
    percentage = stock1.percentage_change()
    print('Percentage change: {:7.3f}'.format(percentage))


if __name__ == '__main__':
    main()