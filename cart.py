
class Cart:
    from item_manager import show_items
    from ownable import set_owner
    def __init__(self, owner):
        self.set_owner(owner)
        self.items = []

    def add(self, item):
        self.items.append(item)

    def transfer_to_customer(self, customer):
        for item in self.items:
            item.set_owner(customer)
        self.items = []


    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

         
        # Eliminar pase al codificar el método check_out.
        # Requisitos
        #: el monto de la compra de todos los artículos en el carrito (Cart#items) se transfiere de la billetera del propietario del carrito a la billetera del propietario del artículo.
        #: la propiedad de todos los artículos del carrito (Cart#items) se transfiere al propietario del carrito.
        # - El contenido del carrito (Cart#items) está vacío.
        # Consejo
        # - Cartera del propietario del carrito ==> self.owner.wallet
        # - Cartera del propietario del artículo ==> item.owner.wallet
        # - El dinero se transferirá ==> Esa cantidad se retirará de la billetera de (?) y se depositará en la billetera de (?).
        # - La propiedad del artículo se transfiere al propietario del carrito ==> Reescribir propietario (item.owner =?)