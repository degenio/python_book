# Contact Management with Inheritance
#Base class
class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return "Name: {0:<15s} and Email: {1:<15s}".format(self.name, self.email)

#Child class
class Supplier(Contact):
    def __init__(self, name, email, supplier_code):
        super().__init__(name, email)
        self.supplier_code = supplier_code

    def place_order(self, order):
        print('The order is for: {}'.format(order))

    def __str__(self):
        return super().__str__() + " Supplier Code: {0:25s}".format(self.supplier_code)


obj1 = Contact("Alain Flouflou", "a.flouflou@monsite.com")
print(obj1)

objF = Supplier("Annie ClairClair", "a.clairclair@monsite.com", "1234")
print(objF)