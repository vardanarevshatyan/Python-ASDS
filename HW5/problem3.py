from time import sleep


class Cook:
    def __init__(self, name='Peter'):
        self.name = name

    def cook_order(self, order_details):
        for order in order_details:
            print(f'{self.name} is making {order}...')
            sleep(.3)
        print('Your order is ready!')
        return order_details


class Delivery:
    def __init__(self, name='John'):
        self.name = name

    def deliver_oder(self, expected_time=45):
        print(f'{self.name} will deliver your order in {expected_time} minutes.')


class Restaurant:
    """All the restaurants share the same menu."""
    menu = {'pizza margarita': 10, 'mexican burger': 7, 'lemon juice': 3, 'pizza pepperoni': 7}

    def __init__(self, name, cook: Cook):
        self.name = name
        self.cook = cook

    @classmethod
    def get_the_recipe(cls, order_details):
        total = 0
        for order in order_details:
            price = cls.menu.get(order, None)
            if price is None:
                print(f'Sorry, we do not have {order}. ')
                continue
            total += price
        print(f'Total price: {total}')
        return total

    def get_order(self, order_details):
        price_total = self.get_the_recipe(order_details)
        order_details = self.cook.cook_order(order_details)
        return price_total, order_details


class Dispatcher:
    def __init__(self, restaurant, delivery_guy: Delivery):
        self._restaurant = restaurant
        self._delivery_guy = delivery_guy

    def place_order(self, order_details):
        print(f'{self._restaurant.name} order placed. Details {order_details}')
        price_total, order = self._restaurant.get_order(order_details)
        self._delivery_guy.deliver_oder()
        return price_total, order


class App:
    def __init__(self, restaurant_name):
        self.restaurant = Restaurant(restaurant_name, Cook())
        self.dispatcher = Dispatcher(self.restaurant, Delivery())

    def make_order(self, order_details, print_recipe=False):
        price_total, order = self.dispatcher.place_order(order_details)
        if print_recipe:
            print(f'Order: {order}, Price: {price_total}')


def get_order(restaurant, order_details):
    app = App(restaurant)
    app.make_order(order_details)


if __name__ == '__main__':
    restaurant = 'Pizza Hut'
    order_details = ['pizza pepperoni', 'pizza margarita', 'lemon juice']
    get_order(restaurant, order_details)

