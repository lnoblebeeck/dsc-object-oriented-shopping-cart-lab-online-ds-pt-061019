class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
       self.total = 0
       self.employee_discount = emp_discount
       self.items = []
    def add_item(self, name, price, quantity=1):
       for i in list(range(quantity)):
           self.items.append({"item": name, "price": price})
           self.total += price
       return self.total
       
    def mean_item_price(self):
       prices = [item['price'] for item in self.items]
       length = len(prices)
       mean_price = sum(prices)/length
       return mean_price

    def median_item_price(self):
        prices = [item['price'] for item in self.items]
        sorted_prices = sorted(prices)
        length = len(prices)
        if length%2 == 0:
           mid_one = int(length/2)
           mid_two = mid_one - 1
           median = (sorted_prices[mid_one] + sorted_prices[mid_two])/2
           return median
        else:
            mid = int(length/2)
            median = prices[mid]
        return median

    def apply_discount(self):
       if self.employee_discount:
           discount = self.employee_discount/100
           discount_total = self.total*(1-discount)
       else:
           discount_total = "Sorry, there is no discount to apply to your cart :("
       
       return discount_total

    def void_last_item(self):
        if self.items:
            removed_item = self.items.pop()
        else: 
            return "There are no items in cart"
       
        self.total -= removed_item['price']
    
        