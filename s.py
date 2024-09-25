import time

# Menu class
class Menu:
    def __init__(self):
        # Items and their respective prices (in rupees) and preparation times
        self.items = {
            # Vegetarian items
            "Veg Burger": {"price": 449, "prep_time": 10, "category": "Vegetarian"},
            "Veg Pizza": {"price": 599, "prep_time": 15, "category": "Vegetarian"},
            "Pasta Primavera": {"price": 619, "prep_time": 12, "category": "Vegetarian"},
            "Vegetable Salad": {"price": 349, "prep_time": 5, "category": "Vegetarian"},
            "Grilled Veggie Wrap": {"price": 499, "prep_time": 10, "category": "Vegetarian"},
            "Spinach Dip": {"price": 529, "prep_time": 6, "category": "Vegetarian"},
            "Stuffed Peppers": {"price": 749, "prep_time": 15, "category": "Vegetarian"},
            "Veggie Tacos": {"price": 529, "prep_time": 12, "category": "Vegetarian"},
            "Mushroom Risotto": {"price": 899, "prep_time": 18, "category": "Vegetarian"},
            "Caprese Salad": {"price": 499, "prep_time": 4, "category": "Vegetarian"},

            # Non-Vegetarian items
            "Chicken Burger": {"price": 599, "prep_time": 10, "category": "Non-Vegetarian"},
            "Beef Pizza": {"price": 799, "prep_time": 15, "category": "Non-Vegetarian"},
            "Pasta Alfredo": {"price": 679, "prep_time": 12, "category": "Non-Vegetarian"},
            "Grilled Chicken Salad": {"price": 799, "prep_time": 10, "category": "Non-Vegetarian"},
            "BBQ Ribs": {"price": 1299, "prep_time": 25, "category": "Non-Vegetarian"},
            "Fish Tacos": {"price": 599, "prep_time": 12, "category": "Non-Vegetarian"},
            "Lamb Chops": {"price": 1699, "prep_time": 30, "category": "Non-Vegetarian"},
            "Shrimp Scampi": {"price": 1099, "prep_time": 20, "category": "Non-Vegetarian"},
            "Chicken Curry": {"price": 999, "prep_time": 15, "category": "Non-Vegetarian"},
            "Steak Frites": {"price": 1299, "prep_time": 20, "category": "Non-Vegetarian"},

            # Dessert items
            "Cheesecake": {"price": 399, "prep_time": 5, "category": "Dessert"},
            "Brownie Sundae": {"price": 449, "prep_time": 4, "category": "Dessert"},
            "Fruit Tart": {"price": 399, "prep_time": 6, "category": "Dessert"},
            "Tiramisu": {"price": 499, "prep_time": 5, "category": "Dessert"},
            "Panna Cotta": {"price": 449, "prep_time": 4, "category": "Dessert"},
            "Cupcakes": {"price": 349, "prep_time": 5, "category": "Dessert"},

            # Drinks
            "Fresh Lemonade": {"price": 199, "prep_time": 2, "category": "Drinks"},
            "Iced Tea": {"price": 249, "prep_time": 2, "category": "Drinks"},
            "Coffee": {"price": 149, "prep_time": 2, "category": "Drinks"},
            "Tea": {"price": 99, "prep_time": 1, "category": "Drinks"},
            "Sparkling Water": {"price": 149, "prep_time": 0, "category": "Drinks"},
            "Fruit Smoothie": {"price": 349, "prep_time": 5, "category": "Drinks"},
            "Milkshake": {"price": 399, "prep_time": 5, "category": "Drinks"},
            "Craft Beer": {"price": 599, "prep_time": 0, "category": "Drinks"},
            "Red Wine": {"price": 899, "prep_time": 0, "category": "Drinks"},
            "White Wine": {"price": 899, "prep_time": 0, "category": "Drinks"}
        }

    def display_menu(self):
        print("\n" + "="*40)
        print("    WELCOME TO OUR RESTAURANT!")
        print("      We hope you enjoy your meal!")
        print("="*40)
        print("                MENU")
        print("="*40)
        index = 1  # Initialize index for menu items
        for category in ["Vegetarian", "Non-Vegetarian", "Dessert", "Drinks"]:
            print(f"\n{category.upper()}")
            for item, details in self.items.items():
                if details["category"] == category:
                    print(f"{index}. {item:20} : ₹{details['price']:.2f} (Prep time: {details['prep_time']} min)")
                    index += 1  # Increment index for each menu item
        print("="*40)

    def get_item_by_index(self, index):
        if index < 1 or index > len(self.items):
            return None
        item_name = list(self.items.keys())[index - 1]
        return self.get_price_and_prep_time(item_name)

    def get_price_and_prep_time(self, item):
        return self.items.get(item, None)


# Order class (Encapsulation: Private attributes)
class Order:
    def __init__(self, customer_name):
        self.__items = []  # Private list of items
        self.__total_price = 0.0  # Private total price
        self.__status = "Pending"  # Order status (Pending, In Progress, Completed)
        self.customer_name = customer_name  # The name of the customer
        self.preparation_time = 0  # Total preparation time for the order

    def add_item(self, item, quantity, price, prep_time):
        self.__items.append((item, quantity))  # Store item and its quantity
        self.__total_price += price * quantity
        self.preparation_time += prep_time * quantity
        print(f"Added {quantity} x {item} to the order. Total: ₹{self.__total_price:.2f}")

    def view_order(self):
        print("\nCurrent Order:")
        for item, quantity in self.__items:
            print(f"{quantity} x {item}")
        print(f"Total: ₹{self.__total_price:.2f}")
        print(f"Order Status: {self.__status}")
        if self.__status == "In Progress":
            print(f"Estimated preparation time: {self.preparation_time} minutes")

    def update_status(self, status):
        self.__status = status
        print(f"Order status updated to: {self.__status}")


# User class (Polymorphism: place_order method)
class User:
    def __init__(self, name):
        self.name = name

    def place_order(self, menu, order):
        raise NotImplementedError("Subclass must implement place_order method")


# Customer class inherits from User
class Customer(User):
    def __init__(self, name):
        super().__init__(name)

    def place_order(self, menu, order):
        occasion = input(f"\n{self.name}, are you here for a family dinner, date, birthday celebration, or party? ").lower()
        self.recommend_dishes(occasion, menu)

        menu.display_menu()
        while True:
            try:
                item_index = int(input(f"{self.name}, enter the item number to add to your order (or '0' to finish): "))
                if item_index == 0:
                    break

                details = menu.get_item_by_index(item_index)
                if details is not None:
                    quantity = int(input(f"How many {list(menu.items.keys())[item_index - 1]}(s) would you like to order? "))
                    if quantity <= 0:
                        print("Please enter a valid quantity.")
                        continue
                    order.add_item(list(menu.items.keys())[item_index - 1], quantity, details['price'], details['prep_time'])
                else:
                    print("Item not available on the menu.")
            except (ValueError, IndexError):
                print("Invalid selection, please try again.")

        # Informing the customer about the preparation time
        print(f"\n{self.name}, your order will take approximately {order.preparation_time} minutes to prepare.")

    def recommend_dishes(self, occasion, menu):
        recommendations = {
            "family dinner": ["Pasta", "Grilled Chicken", "Salad"],
            "date": ["Pizza", "Steak", "Wine"],
            "birthday celebration": ["Ice Cream", "Chocolate Cake", "Cocktail"],
            "party": ["Beer", "Fries", "Tacos"]
        }
        recommended_items = recommendations.get(occasion, [])
        if recommended_items:
            print(f"\nBased on your occasion ({occasion}), we recommend: {', '.join(recommended_items)}")
        else:
            print("\nWe have a wide selection of dishes available for you!")

    def get_feedback(self):
        feedback = input(f"\n{self.name}, we hope you enjoyed your meal! Please leave us a review: ")

        if "bad" in feedback.lower() or "poor" in feedback.lower() or "not good" in feedback.lower():
            print(f"Thank you for your feedback: '{feedback}'! We're sorry to hear that. 😔 We will work on improving the things that made you unhappy.")
        else:
            print(f"Thank you for your feedback: '{feedback}'! We're glad you had a wonderful experience! 😊")


# Staff class inherits from User (Polymorphism)
class Staff(User):
    def __init__(self, name):
        super().__init__(name)

    def manage_order(self, order):
        print(f"\nStaff {self.name} is managing the order.")
        order.update_status("In Progress")
        order.view_order()

        # Simulate preparation time
        time.sleep(order.preparation_time // 10)  # Simulate the preparation time (shortened for demo)
        order.update_status("Completed")
        print(f"Order for {order.customer_name} is now ready!")

# Admin class inherits from User (Polymorphism)
class Admin(User):
    def __init__(self, name):
        super().__init__(name)

    def manage_order(self, order):
        print(f"\nAdmin {self.name} is overseeing the order.")
        order.view_order()  # View the order details

# Main function to demonstrate the system
def main():
    print("Welcome to the Restaurant Management System".center(50, "="))

    # Create a menu
    menu = Menu()

    # Create users
    customer_name = input("Please enter your name: ")
    customer = Customer(customer_name)
    staff = Staff("Bob")
    admin = Admin("Alice")

    # Create an order for the customer
    order = Order(customer_name)

    # Customer placing an order
    print("\nCustomer placing an order:")
    customer.place_order(menu, order)

    # Staff managing the order
    print("\nStaff managing the order:")
    staff.manage_order(order)

    # Admin managing the order
    print("\nAdmin managing the order:")
    admin.manage_order(order)

    # Get feedback after the meal
    customer.get_feedback()

if __name__ == "__main__":
    main()
