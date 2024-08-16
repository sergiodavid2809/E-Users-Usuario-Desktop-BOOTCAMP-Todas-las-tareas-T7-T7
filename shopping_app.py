from customer import Customer
from item import Item
from seller import Seller

seller = Seller("DIC Store")
for i in range(10):
    Item("CPU", 40830, seller)
    Item("Memory", 13880, seller)
    Item("Motherboard", 28980, seller)
    Item("Power supply", 8980, seller)
    Item("PC Case", 8727, seller)
    Item("3.5 inches HDD", 10980, seller)
    Item("2.5 inches SSD", 13370, seller)
    Item("M.2 SSD", 12980, seller)
    Item("CPU cooler fan", 13400, seller)
    Item("Graphic card", 23800, seller)

print("🤖 tell me your name")
customer = Customer(input())

print("🏧 Enter the amount to top up your wallet")
customer.wallet.deposit(int(input()))

print("🛍️ Start shopping")
end_shopping = False
while not end_shopping:
    print("📜 Product List")
    seller.show_items()

    print("️️⛏ Please insert the product number")
    number = int(input())

    print("⛏ Please insert the product quantity")
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)
    print("🛒 Cart contents")
    customer.cart.show_items()
    print(f"🤑 Total amount: {customer.cart.total_amount()}")
    
    print("😭 Do you want to finish shopping? (yes/no)")
    end_shopping = input() == "yes"


print("💸 Confirm purchase? (yes/no)")
if input() == "yes":
    customer.wallet.deposit((int(customer.cart.total_amount()*-1)))
    seller.wallet.deposit(customer.cart.total_amount())
print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈Result┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ ️{customer.name}'s property")
customer.cart.show_items()
print(f"😱👛 {customer.name} wallet balance: {customer.wallet.balance}")

print(f"📦 {seller.name} availability")
seller.show_items()
print(f"😻👛 {seller.name} Wallet Balance: {seller.wallet.balance}")

customer.cart.transfer_to_customer(customer)
print("🛒 Cart contents")
customer.cart.show_items()
print(f"🌚 Total amount: {customer.cart.total_amount()}")

print("🎉 Done")
