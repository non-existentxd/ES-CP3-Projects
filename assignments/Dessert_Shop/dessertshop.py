from dessert import Candy, Cookie, IceCream, Sundae, Order
from receipt import *


def main():
    order = Order()
    order.add(Candy("Candy Corn", 1.5, 0.25))
    order.add(Candy("Gummy Bears", 0.25, 0.35))
    order.add(Cookie("Chocolate Chip", 6, 3.99))
    order.add(IceCream("Pistachio", 2, 0.79))
    order.add(Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29))
    order.add(Cookie("Oatmeal Raisin", 2, 3.45))

    for item in order.order:
        print(item.name)
    print(f"Total number of items in order: {len(order)}")

    data = [
        [item.name, f"${item.calculate_cost():.2f}", f"${item.calculate_tax():.2f}"]
        for item in order.order
    ]
    data.append(["Order Subtotals", f"${order.order_cost():.2f}", f"${order.order_tax():.2f}"])
    data.append(["Order Total", "", f"${order.order_cost() + order.order_tax():.2f}"])
    data.append(["Total items in the order", "", len(order)])

    receipt.make_receipt(data, "receipt.pdf")

if __name__ == "__main__":
    main()
