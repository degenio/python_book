# Contact Management with Inheritance
class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return "Name: {0:<15s} and Email: {1:<15s}".format(self.name, self.email)

class Supplier(Contact):
    def __init__(self, name, email, supplier_code):
        super().__init__(name, email)
        self.supplier_code = supplier_code

    def place_order(self, order):
        print('The order is for: {}'.format(order))

    def __str__(self):
        return super().__str__() + " Supplier Code: {0:25s}".format(self.supplier_code)


class ContactRegister:
    def __init__(self, name, register=()):
        self.name = "contact list"
        self.register = list()

    def search_contact(self, keyword):
        results = list()
        for contact in self.register:
            if keyword in contact.name:
                results.append(contact)
        return results

    def display_contacts(self):
        print("Number of contacts: {:<4d}".format(len(self.register)))
        for tmp in self.register:
            print(tmp)

    def add_contact(self, contact):
        self.register.append(contact)
        
        
# Create the contact register
listing = ContactRegister("contact list")

obj1 = Contact("Alain Flouflou", "a.flouflou@monsite.com")
# print(obj1)
listing.add_contact(obj1)

objF = Supplier("Annie ClairClair", "a.clairclair@monsite.com", "1234")
# print(objF)
listing.add_contact(objF)

# Display the content of the register
listing.display_contacts()

# Search for a contact
keyword = "Clair"
results = listing.search_contact(keyword)
print("*" * 25)
print("Elements found")
print("*" * 25)
for res in results:
    print(res) 