class Product:
    def __init__(self,name,description,price,category,quantity):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.quantity = quantity

    def show(self):
        print(f"Nombre: {self.name} \nDescripcion: {self.description} \nPrecio: {self.price} \nCategoria: {self.category}\nCantidad disponible: {self.quantity}\n\n")

    def retorno(self):
        return f"""Nombre: {self.name}
        Descripcion: {self.description}
        Precio: {self.price}
        Categoria: {self.category}
        Cantidad disponible: {self.quantity}
        """
