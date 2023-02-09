from datetime import datetime
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        self.start_time = datetime.strptime(str(self.start_time), '%H%M').strftime('%I %p')
        self.end_time = datetime.strptime(str(self.end_time), '%H%M').strftime('%I %p')
        return self.name + " menu available from " + str(self.start_time) + " - " + str(self.end_time)

    def calculate_bill(self, purchased_items):
        bill = 0
        for data in purchased_items:
            if data in self.items:
                bill += self.items[data]
        return bill

class Franchise:
    def __init__(self, address, menu_list):
        self.address = address
        self.menu_list = menu_list

    def __repr__(self):
        return "The address of the restaurant is " + self.address

    def available_menus(self, time):
        available_items = []
        for data in self.menu_list:
            if time >= data.start_time and time <= data.end_time:
                available_items.append(data)
        return available_items

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
  def __refe__(self):
      return self.franchises


# brunch--------------------------------------------------------------------------------------
brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
    'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)
#print(brunch_menu)
#print("for brunch: " + str(brunch_menu.calculate_bill(['pancakes','home fries','coffee'])))

# early_bird-----------------------------------------------------------------------------------
early_bird_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00, }

early_bird_menu = Menu("Early_Bird", early_bird_items, 1500, 1800)
#print("for early_bird: "+ str(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])))

# dinner----------------------------------------------------------------------------------------
dinner_items = {
    'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00, }
dinner_menu = Menu("Dinner", dinner_items, 1700, 2300)

# kids-------------------------------------------------------------------------------------------
kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids_menu = Menu("Kids", kids_items, 1100, 2100)
# -----------------------------------------------------------------------------------------------

menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

print(flagship_store.available_menus(1700))


basta = Business("Basta Fazoolin' with my Heart", [flagship_store,new_installment])
print(Business("Basta Fazoolin' with my Heart", [flagship_store,new_installment]))

arepa_items = {  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepa_menu = Menu("Take a Arepa",arepa_items,1000,2000)
arepa_location = Franchise("189 Fitzgerald Avenue",[arepa_menu])

arepa  = Business("Take a Arepa", [arepa_location])