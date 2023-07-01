from Product import Product
from Customer import Customer
from Payment import Payment
from Shipment import Shipment
from Sell import Sell
from api import old_list
import pickle
import random
from datetime import date

class App:
    def __init__(self,old_list):
        self.old_list = old_list
        self.old_list_c = []
        self.new_list = []
        self.products1 = []
        self.new_customers = []
        self.carrito = []
        self.list_sells = []
        self.list_payments = []
        self.list_shipments = []
        


#actualiza el inventario de productos. Si ya hay productos dentro del .txt, solo lee el .txt; pero si esta vacio, agrega el de la api. 
    def upgrade_inv(self):
        archivo = open('old_list.txt', 'rb')
        data = pickle.load(archivo)
        archivo.close()
        if data == 'hola mundo!':
            arch = open('old_list.txt', 'wb')
            old_list_txt = pickle.dumps(old_list)
            arch.write(old_list_txt)
            arch.close()
            pata = pickle.loads(old_list_txt)
            for p in pata:
                name = p['name']
                description = p['description']
                price = float(p['price'])
                category = p['category']
                quantity = int(p['quantity'])
                new_product = Product(name, description, price, category, quantity)
                self.new_list.append(new_product)
            arch = open('old_list.txt', 'wb')
            caco = pickle.dumps(self.new_list)
            arch.write(caco)
            arch.close()
        else:
            archivo = open('old_list.txt', 'rb')
            self.new_list = pickle.load(archivo)
            archivo.close()
            
#aniade un producto a la lista de productos.
    def add_product(self):
        name = input('\nIngrese el nombre del producto: ')
        for p in self.new_list:
            while name == p.name or len(name) == 0:
                name = input('\nYa existe un producto con ese nombre. Ingrese otro nombre: ')
        description = input('\nIngrese la descripcion del producto: ')
        price = input('\nIngrese el precio del producto: ')
        while price == '0' or not price.isnumeric():
            price = input('\nValor invalido. Ingrese el precio del producto: ')
            if price.isnumeric() and price == 0:
                while float(price) <= 0:
                    price = input('\nValor invalido. Ingrese el precio del producto: ')
        if price.isnumeric():
            price = float(price)
        category = input('\nCategorias: \n -Industrial \n -Health \n -Books \n -Computers \n -Grocery \n -Garden \n -Shoes \n -Home \n -Jewelery \n -Beauty \n -Baby \n -Music \n -Movies \n -Clothing \n -Sports \n -Games \nIngrese la categoria del producto: ')
        while category  !=  'Industrial' and category  != 'Health' and category  != 'Books' and category  != 'Computers' and category  != 'Grocery' and category  != 'Garden' and category  != 'Shoes' and category  != 'Home' and category  != 'Jewelery' and category  != 'Beauty' and category  != 'Baby' and category  != 'Music' and category  != 'Movies' and category  != 'Clothing' and category  != 'Sports' and category  != 'Games':
            category = input('\nCategoria no permitida.\nCategorias: \n -Industrial \n -Health \n -Books \n -Computers \n -Grocery \n -Garden \n -Shoes \n -Home \n -Jewelery \n -Beauty \n -Baby \n -Music \n -Movies \n -Clothing \n -Sports \n -Games \n Ingrese la categoria del producto: ')
        quantity = input('\nIngrese la cantidad disponible del producto: ')
        while quantity == '0' or not quantity.isnumeric():
            quantity = input('\nValor invalido. Ingrese el precio del producto: ')
            if quantity.isnumeric() and quantity == 0:
                while int(quantity) <= 0:
                    quantity = input('\nValor invalido. Ingrese el precio del producto: ')
        if quantity.isnumeric():
            quantity = int(quantity)
        new_product = Product(name,description,price,category,quantity)
        self.new_list.append(new_product)
        print('\nProducto aniadido exitosamente!')

#busca los productos por nombre.
    def search_products_by_name(self):
        product = []
        search = input('\nIngrese el nombre del producto que desea buscar: ')
        for p in self.new_list:
            if p.name == search:
                product.append(p)
        if product == []:
            print('\nEl producto no fue encontrado.')
            self.search_products_by_name()
        else:
            for a in product:
                a.show()

#busca los productos por precio.
    def search_products_by_price(self):
        search = input('\nIngrese el rango de precio del producto que desea buscar: ')
        if search.isnumeric():
            search = float(search)
        else:
            while not search.isnumeric():
                search = input('\nValor invalido. Ingrese el rango de precio del producto que desea buscar: ')
            if search.isnumeric():
                search = float(search)
        if search >= 1:
            for p in self.new_list:
                if p.price <= search:
                    self.products1.append(p)
            print(f'\nEstos son los productos menores a {search} dolares')
            for a in self.products1:
                a.show()
        else:
            print('\nNo hay productos en ese rango de precio.')
            self.search_products_by_price()
    
#busca los productos por categoria.
    def search_products_by_category(self):
        search = input('\nCategorias: \n -Industrial \n -Health \n -Books \n -Computers \n -Grocery \n -Garden \n -Shoes \n -Home \n -Jewelery \n -Beauty \n -Baby \n -Music \n -Movies \n -Clothing \n -Sports \n -Games \n Ingrese la categoria del producto que desea buscar:')
        for p in self.new_list:
            if p.category == search:
                self.products1.append(p)
        if self.products1 == []:
            print('\nNo hay productos bajo esa categoria.')
            self.search_products_by_category()
        else:
            print(f'\nEstos son los productos bajo la categoria "{search}"')
            for a in self.products1:
                a.show()
    
#busca los productos por disponibilidad.
    def search_products_by_availability(self):
        search = input('\nIngrese la disponibilidad del producto que desea buscar: ')
        if search.isnumeric():
            search = int(search)
        else:
            while not search.isnumeric():
                search = input('\nValor invalido. Ingrese el rango de precio del producto que desea buscar: ')
            if search.isnumeric():
                search = int(search)
        for p in self.new_list:
            if p.quantity <= search:
                self.products1.append(p)
        if self.products1 == []:
            print('\nNo hay productos con la disponibilidad indicada')
            self.search_products_by_availability()
        else:
            print(f'\nEstos son los productos menores a la disponibilidad indicada: ')
            for a in self.products1:
                a.show()

#modifica un producto de la lista de productos.
    def modify_product(self):
        search = input('\nIngrese el nombre del producto que desea modificar:')
        for p in self.new_list:
            if p.name == search:
                print('\nProducto encontrado!')
                p.show()
                search = input('\nModificar:\n1. Nombre.\n2. Descripcion.\n3. Precio\n4. Categoria.\n5. Cantidad.')
                while search != '1' and search != '2' and search != '3' and search != '4' and search != '5':
                    search = input('\nError.\nModificar:\n1. Nombre.\n2. Descripcion.\n3. Precio\n4. Categoria.\n5. Cantidad.')
                if search == '1':
                    name = input('\nIngrese el nombre del producto: ')
                    for p in self.new_list:
                        while name == p.name or len(name) == 0:
                            name = input('\nYa existe un producto con ese nombre. Ingrese otro nombre: ')
                    p.name = name
                    print('\nNombre modificado exitosamente!')
                    break
                elif search == '2':
                    description = input('\nIngrese la descripcion del producto: ')
                    p.description = description
                    print('\nDescripcion modificada exitosamente!')
                    break
                elif search == '3':
                    price = input('\nIngrese el precio del producto: ')
                    while price == '0' or not price.isnumeric():
                        price = input('\nValor invalido. Ingrese el precio del producto: ')
                        if price.isnumeric() and price == 0:
                            while float(price) <= 0:
                                price = input('\nValor invalido. Ingrese el precio del producto: ')
                    if price.isnumeric():
                        price = float(price)
                    p.price = price
                    print('\nPrecio modificado exitosamente!')
                    break
                elif search == '4':
                    category = input('\nCategorias: \n -Industrial \n -Health \n -Books \n -Computers \n -Grocery \n -Garden \n -Shoes \n -Home \n -Jewelery \n -Beauty \n -Baby \n -Music \n -Movies \n -Clothing \n -Sports \n -Games \nIngrese la categoria del producto: ')
                    while category  !=  'Industrial' and category  != 'Health' and category  != 'Books' and category  != 'Computers' and category  != 'Grocery' and category  != 'Garden' and category  != 'Shoes' and category  != 'Home' and category  != 'Jewelery' and category  != 'Beauty' and category  != 'Baby' and category  != 'Music' and category  != 'Movies' and category  != 'Clothing' and category  != 'Sports' and category  != 'Games':
                        category = input('\nCategoria no permitida.\nCategorias: \n -Industrial \n -Health \n -Books \n -Computers \n -Grocery \n -Garden \n -Shoes \n -Home \n -Jewelery \n -Beauty \n -Baby \n -Music \n -Movies \n -Clothing \n -Sports \n -Games \n Ingrese la categoria del producto: ')
                    p.category = category
                    print('\nCategoria modificada exitosamente!')
                    break
                elif search == '5':
                    quantity = input('\nIngrese la cantidad disponible del producto: ')
                    while quantity == '0' or not quantity.isnumeric():
                        quantity = input('\nValor invalido. Ingrese el precio del producto: ')
                        if quantity.isnumeric() and quantity == 0:
                            while int(quantity) <= 0:
                                quantity = input('\nValor invalido. Ingrese el precio del producto: ')
                    if quantity.isnumeric():
                        quantity = int(quantity)
                    p.quantity = quantity
                    print('\nCantidad modificada exitosamente!')
                    break
        else:  
            print('\nEl producto no fue encontrado.')
            self.modify_product()

#elimina un producto a la lista de productos.
    def eliminate_product(self):
        search = input('\nIngrese el nombre del producto que desea eliminar:')
        for p in self.new_list:
            if p.name == search:
                print('\nProducto encontrado!')
                self.new_list.remove(p)
                print('\nProducto eliminado exitosamente!')
                break
        else:
            print('\nEl producto no fue encontrado.')
            self.eliminate_products()

#reinicia el .txt como si estuviera vacio.
    def reboot_p(self):
        file = open('old_list.txt', 'wb')
        paquito = pickle.dumps('hola mundo!')
        file.write(paquito)
        file.close()





#actualiza la lista de clientes. Si ya hay clientes dentro del .txt, solo lee el .txt; pero si esta vacio, crea una lista vacia.
    def upgrade_cust(self):
        archivo = open('old_list_c.txt', 'rb')
        data = pickle.load(archivo)
        archivo.close()
        if data == 'hola mundo!':
            arch = open('old_list_c.txt', 'wb')
            fac = pickle.dumps([])
            arch.write(fac)
            arch.close()
        else:
            archivo = open('old_list_c.txt', 'rb')
            self.new_customers = pickle.load(archivo)
            archivo.close()

#aniade un cliente a la lista de clientes.
    def add_customer(self):
        complete_name = input('\nIngrese su nombre o razon social: ')
        while len(complete_name) == 0:
            complete_name = input('\nNombre invalido. Ingrese su nombre o razon social: ')
        customer_type = input('\nNatural: n \nJuridico: j \nIngrese su tipo de cliente: ')
        while customer_type != 'n' and customer_type != 'j':
            customer_type = input('\nEso no es una opcion permitida. \n\nNatural: n \nJuridico: j \nIngrese su tipo de cliente: ')
        if customer_type == 'n':
            customer_type = 'Natural'
        elif customer_type == 'j':
            customer_type = 'Juridico'
        dni = input('\nIngrese su cedula o RIF: ')
        while len(dni) <= 6 or len(dni) >= 10 or not dni.isnumeric():
            dni = input('\nCedula o RIF invalido. Ingrese su cedula o RIF: ')
        for p in self.new_customers:
            while not dni.isnumeric() or dni == p.dni or len(dni) >= 6 or len(dni) <= 10:
                if not dni.isnumeric():
                    dni = input('\nEso no es un numero. Ingrese su cedula o RIF en numeros: ')
                elif dni == p.dni:
                    dni = input('\nYa existe esa cedula o RIF, ingrese otro valor: ')
                elif len(dni) <= 6 or len(dni) >= 10:
                    dni = input('\nEso no es una cedula o RIF, ingrese una cedula o RIF: ')
                else:
                    break
        email = input('\nIngrese su correo electronico: ')
        while "@" not in email or "." not in email or ' ' in email:
            email = input('\nCorreo electronico invalido \nIngrese su correo electronico: ')
        for d in self.new_customers:
            while "@" not in email or "." not in email or ' ' in email or email == d.email:
                if "@" or "." not in email:
                    email = input('\nCorreo electronico invalido \nIngrese su correo electronico: ')
                elif email == d.email:
                    email = input('\nEl correo electronico ya esta registrado \nIngrese su correo electronico: ')
                else:
                    break
        address = input('\nIngrese su direccion: ')
        while len(address) == 0:
            address = input('\nDireccion invalida. Ingrese su direccion: ')
        telef_numb = input('Ejemplo: 04127180545 \nIngrese su numero telefonico: ')
        while not telef_numb.isnumeric() or len(telef_numb) != 11:
            telef_numb = input('\nEso no es un numero o no es un numero telefonico valido \nIngrese su numero telefonico: ')
            if telef_numb.isnumeric() or len(telef_numb) == 11:
                break
        new_cust = Customer(complete_name,customer_type,dni,email,address,telef_numb)
        self.new_customers.append(new_cust)
    
#modifica un cliente de la lista de clientes.
    def modify_customer(self):
        paco = []
        search = input('\nIngrese la cedula o RIF del cliente que desea modificar:')
        for t in self.new_customers:
            if search == t.dni:
                paco.append('pepo')
        if len(paco) == 0:
            print('\nCedula o RIF no encontrado.')
            self.modify_customer()
        else:
            for c in self.new_customers:
                if search == c.dni:
                    print('\nCliente encontrado!')
                    c.show_()
                    search = input('\nModificar:\n1. Nombre o razon social.\n2. Cedula.\n3. Correo electronico.\n4. Direccion.\n5. Numero telefonico.')
                    while search != '1' and search != '2' and search != '3' and search != '4' and search != '5':
                        search = input('\nError.\n\nModificar:\n1. Nombre o razon social.\n2. Cedula.\n3. Correo electronico.\n4. Direccion.\n5. Numero telefonico.')
                    if search == '1':
                        complete_name = input('\nIngrese su nombre o razon social: ')
                        while len(complete_name) == 0:
                            complete_name = input('\nNombre invalido. Ingrese su nombre o razon social: ')
                        c.complete_name = complete_name
                        print('\nNombre o razon social modificada exitosamente.')
                        break
                    elif search == '2':
                        dni = input('\nIngrese su cedula o RIF: ')
                        for p in self.new_customers:
                            while not dni.isnumeric() or dni == p.dni or len(dni) >= 6 or len(dni) <= 10:
                                if not dni.isnumeric():
                                    dni = input('\nEso no es un numero. Ingrese su cedula o RIF en numeros: ')
                                elif dni == p.dni:
                                    dni = input('\nYa existe esa cedula o RIF. Ingrese su cedula o RIF: ')
                                elif len(dni) <= 6 or len(dni) >= 10:
                                    dni = input('\nEso no es una cedula o RIF, Ingrese su cedula o RIF: ')
                                else:
                                    break
                        c.dni = dni
                        print('\nCedula o RIF modificada exitosamente.')
                        break
                    elif search == '3':
                        email = input('\nIngrese su correo electronico: ')
                        for d in self.new_customers:
                            while "@" not in email or "." not in email or ' ' in email or email == d.email:
                                if "@" or "." not in email:
                                    email = input('\nCorreo electronico invalido \nIngrese su correo electronico: ')
                                elif email == d.email:
                                    email = input('\nEl correo electronico ya esta registrado \nIngrese su correo electronico: ')
                                else:
                                    break
                        c.email = email
                        print('\nCorreo electronico modificado exitosamente.')
                        break
                    elif search == '4':
                        address = input('\nIngrese su direccion: ')
                        while len(address) == 0:
                            address = input('\nDireccion invalida. Ingrese su direccion: ')
                        c.address = address
                        print('\nDireccion modificada exitosamente.')
                        break
                    elif search == '5':
                        telef_numb = input('Ejemplo: 04127180545 \nIngrese su numero telefonico: ')
                        while not telef_numb.isnumeric() or len(telef_numb) != 11:
                            telef_numb = input('\nEso no es un numero o no es un numero telefonico valido \nIngrese su numero telefonico: ')
                            if telef_numb.isnumeric() or len(telef_numb) == 11:
                                break
                        c.telef_numb = telef_numb
                        print('\nNumero telefonico modificado exitosamente.')
                        break
                    print('\nCliente modificado exitosamente.')
                    break

#elimina un cliente de la lista de clientes.
    def eliminate_customer(self):
        paco = []
        search = input('\nIngrese la cedula o RIF del cliente que desea eliminar:')
        for t in self.new_customers:
            if search == t.dni:
                paco.append(t.dni)
        if len(paco) == 0:
            print('\nCedula o RIF no encontrado.\n')
            self.eliminate_customer()
        else:
            for c in self.new_customers:
                if search == c.dni:
                    self.new_customers.remove(c)
                    print('\nCliente eliminado exitosamente.')

#busca los clientes por cedula o RIF.
    def search_customer_by_dni(self):
        paco = []
        search = input('\nIngrese la cedula o RIF del cliente que desea buscar:')
        for p in self.new_customers:
            if p.dni == search:
                paco.append(p)
        if paco == []:
            print('\nEl cliente no fue encontrado.')
            self.search_customers_by_dni()
        else:
            for a in paco:
                a.show_()

#busca los clientes por correo electronico.
    def search_customer_by_email(self):
        paco = []
        search = input('\nIngrese el email del cliente que desea buscar:')
        for p in self.new_customers:
            if p.email == search:
                paco.append(p)
        if paco == []:
            print('\nEl cliente no fue encontrado.')
            self.search_customers_by_email()
        else:
            for a in paco:
                a.show_()

#reinicia el .txt como si estuviera vacio.
    def reboot_c(self):
        file = open('old_list_c.txt', 'wb')
        paquito = pickle.dumps('hola mundo!')
        file.write(paquito)
        file.close()





#actualiza la lista de ventas. Si ya hay ventas dentro del .txt, solo lee el .txt; pero si esta vacio, crea una lista vacia.
    def upgrade_sells(self):
        archivo = open('old_list_sells.txt', 'rb')
        data = pickle.load(archivo)
        archivo.close()
        if data == 'hola mundo!':
            arch = open('old_list_sells.txt', 'wb')
            fac = pickle.dumps([])
            arch.write(fac)
            arch.close()
        else:
            archivo = open('old_list_sells.txt', 'rb')
            self.list_sells = pickle.load(archivo)
            archivo.close()

#registra una venta a la lista de ventas.
    def register_sell(self):
        verify = True
        pepo = False
        order = str(random.randrange(0,100000000000000000000000000000))
        datee = date.today()
        precios = []
        dni = input('\nIngrese su cedula o RIF: ')
        while len(dni) <= 6 or len(dni) >= 10 or not dni.isnumeric():
            dni = input('\nCedula o RIF invalido. Ingrese su cedula o RIF: ')
        for i in self.new_customers:
            if dni == i.dni:
                cliente = i
                nombre = i.complete_name
                tipo = i.customer_type
                cedula = i.dni
                correo = i.email
                direccion = i.address
                telefono = i.telef_numb
                verify = False
        if verify == True:
            self.add_customer()
            for i in self.new_customers:
                if dni == i.dni:
                    cliente = i
                    nombre = i.complete_name
                    tipo = i.customer_type
                    cedula = i.dni
                    correo = i.email
                    direccion = i.address
                    telefono = i.telef_numb
                    print('\nCliente agregado.\n')
        cart = []
        legible_cart = []
        poco = True
        while poco == True:
            producto = []
            verify1 = True
            search = input('\nIngrese el nombre del producto que desea buscar: ')
            for p in self.new_list:
                if search == p.name:
                    verify1 = False
                    puco = True
                    print('\nProducto encontrado!')
                    while puco == True:
                        quantity = input('\nIngrese la cantidad deseada del producto: ')
                        if quantity.isnumeric():
                            quantity = int(quantity)
                            if quantity >= 1 and quantity <= p.quantity:
                                puco = False
                                break
                            else:
                                print('Error.')
                        else:
                            print('\nError.')
                    quantity = int(quantity)
                    p.quantity -= quantity
                    cart.append(p)
                    for i in cart:
                        if search == i.name:
                            i.quantity = quantity
                            i.price *= quantity
                            precios.append(float(i.price))                  
                    break
            if verify1 == True:
                print('Producto no encontrado.')
            if verify1 == False:
                siono = input('\nDesea seguir aniadiendo productos a la lista? Escriba si o no para registrar su respuesta: ')
                while siono != 'si' and siono != 'no':
                    siono = input('\nError\nDesea seguir aniadiendo productos a la lista? Escriba si o no para registrar su respuesta: ')
                if siono == 'si':
                    continue
                elif siono == 'no':
                    break
        for i in cart:
            aa = f"{i.name}, {i.description}, Precio: {i.price}, Categoria: {i.category}, Cantidad: {i.quantity}"
            legible_cart.append(aa)
        pepo = True
        while pepo == True:
            payment_moment = input('\n1. Pagar de contado.\n2. Pagar a creditos solo si eres un cliente juridico.\nIngrese el numero correspondiente a su momento de pago: ')
            if payment_moment == '1':
                payment_moment = 'De contado'
                debe = 'no'
                pepo = False
                break
            elif payment_moment == '2' and tipo == 'Juridico':
                payment_moment = 'A creditos'
                debe = 'si'
                pepo = False
                break
            else:
                print('Error.')
        papo = True
        while papo == True:
            payment_method = input('\n1. Punto de venta.\n2. Pago movil.\n3. Zelle.\n4. Cash.\nIngrese el numero correspondiente a su forma de pago: ')
            if payment_method == '1':
                payment_method = 'PdV'
                for i in range(len(precios)):
                    precios[i] *= 28
                moneda = 'Bs.'
                papo = False
                break    
            elif payment_method == '2':
                payment_method = 'PM'
                for i in range(len(precios)):
                    precios[i] *= 28
                moneda = 'Bs.'
                papo = False
                break    
            elif payment_method == '3':
                payment_method = 'Zelle'
                moneda = '$'
                papo = False
                break
            elif payment_method == '4':
                payment_method = 'Cash'
                moneda = '$'
                papo = False
                break
            else:
                print('Error.')
        pipo = True
        while pipo == True:
            shipping_method = input('\n1. MRW.\n2. Zoom.\n3. Delivery.\nIngrese el numero correspondiente a su metodo de envio:')
            if shipping_method == '1':
                shipping_method = 'MRW'
                pipo = False
                break
            elif shipping_method == '2':
                shipping_method = 'Zoom'
                pipo = False
                break
            elif shipping_method == '3':
                shipping_method = 'Delivery'
                pipo = False
                break
            else:
                print('Error.')
        subtotal = sum(precios)
        if tipo == 'Juridico' and payment_moment != 'A creditos':
            discount = 5*subtotal/100
        else:
            discount = 0
        iva = 16*subtotal/100
        if payment_method == 'Cash' or payment_method == 'Zelle':
            igtf = 3*subtotal/100
        else:
            igtf = 0
        total = round((subtotal-discount+iva+igtf),2)
        enviado = 'no'
        new_sell = Sell(order,datee,nombre,tipo,cedula,correo,direccion,telefono,legible_cart,cart,payment_moment,debe,payment_method,moneda,shipping_method,subtotal,discount,iva,igtf,total,enviado)
        self.list_sells.append(new_sell)
        new_sell.show____()
        if debe == 'no':
            new_bill = Payment(nombre,tipo,cedula,correo,direccion,telefono,datee,order,total,moneda,payment_method)
            self.list_payments.append(new_bill)
        elif debe == 'si':
            print('\nEl pago se debe realizar entre los proximos 15 y 30 dias.')

#busca las ventas realizadas por el mismo cliente a traves de la cedula o RIF.
    def search_sells_by_dni(self):
        paco = []
        search = input('\nIngrese la cedula o RIF del cliente en la lista de ventas que desea buscar: ')
        for p in self.list_sells:
            if p.cedula == search:
                paco.append(p)
        if paco == []:
            print('\nCedula o RIF invalido.')
            self.search_sells_by_dni()
        else:
            for a in paco:
                a.show____()

#busca las ventas realizadas en cierta fecha.
    def search_sells_by_date(self):
        paco = []
        while True:
            day = input('\nIngrese el numero del dia que se realizo el pago: ')
            if day.isnumeric():
                day = int(day)
                if day <= 31 and day >= 1:
                    break
                else:
                    print('\nError.') 
            else:
                print('\nError.')
        while True:
            month = input('\nIngrese el numero del mes que se realizo el pago: ')
            if month.isnumeric():
                month = int(month)
                if month <= 12 and month >= 1:
                    break
                else:
                    print('\nError.') 
            else:
                print('\nError.')
        while True:
            year = input('\nIngrese el numero del anio que se realizo el pago: ')
            if year.isnumeric():
                year = int(year)
                if year >= 2023 and year <= 2100:
                    break
                else:
                    print('\nError.') 
            else:
                print('\nError.')
        fecha = date(year,month,day)
        for p in self.list_sells:
            if p.datee == fecha:
                paco.append(p)
        if paco == []:
            print('\nFecha invalida.')
            self.search_sells_by_date()
        else:
            for a in paco:
                a.show____()

#busca las ventas realizadas por su precio total.
    def search_sells_by_price(self):
        paco = []
        search = input('\nIngrese el monto total de la/s venta/s que desea buscar: ')
        test = search
        test1 = test.replace('.','')
        while not test1.isnumeric():
            search = input('\nIngrese el monto total de la/s venta/s que desea buscar: ')
            test = search
            test1 = test.replace('.','')
        search = float(search)
        for p in self.list_sells:
            if p.total == search:
                paco.append(p)
        if paco == []:
            print('\nMonto invalido.')
            self.search_sells_by_price()
        else:
            for a in paco:
                a.show____()

#reinicia el .txt como si estuviera vacio.
    def reboot_sells(self):
        file = open('old_list_sells.txt', 'wb')
        paquito = pickle.dumps('hola mundo!')
        file.write(paquito)
        file.close()
    



#actualiza la lista de pagos. Si ya hay pagos dentro del .txt, solo lee el .txt; pero si esta vacio, crea una lista vacia.
    def upgrade_payments(self):
        archivo = open('old_list_payments.txt', 'rb')
        data = pickle.load(archivo)
        archivo.close()
        if data == 'hola mundo!':
            arch = open('old_list_payments.txt', 'wb')
            fac = pickle.dumps([])
            arch.write(fac)
            arch.close()
        else:
            archivo = open('old_list_payments.txt', 'rb')
            self.list_payments = pickle.load(archivo)
            archivo.close()

#registra un pago a la lista de pagos.
    def create_bill(self):
        maco = 'pico'
        order = input('\nIngrese el numero de la orden dada en la venta: ')
        for i in self.list_sells:
            if i.order == order:
                maco = 'paso'
                if i.debe == 'si':
                    nombre = i.nombre
                    tipo = i.tipo
                    cedula = i.cedula
                    correo = i.correo
                    direccion = i.direccion
                    telefono = i.telefono
                    total = i.total
                    moneda = i.moneda
                    metodo_de_pago = i.payment_method
                    fecha = date.today()
                    new_bill = Payment(nombre,tipo,cedula,correo,direccion,telefono,fecha,order,total,moneda,metodo_de_pago)
                    self.list_payments.append(new_bill)
                    i.debe = 'no'
                    print('\nPago registrado.\n')
                    for i in self.list_payments:
                        if order == i.orderP:
                            i.show__()
                    break
                elif i.debe == 'no':
                    print('\nEl pago ya fue registrado.\n')
                    prueba = i.order
                    for h in self.list_payments:
                        if h.orderP == prueba:
                            h.show__()
        if maco != 'paso':
            print('\nNumero de orden no encontrada.')
            self.create_bill()

#busca los pagos realizados por el mismo cliente a traves de la cedula o RIF.                
    def search_payments_by_dni(self):
        paco = []
        search = input('\nIngrese la cedula o RIF del cliente en la lista de pagos que desea buscar: ')
        for p in self.list_payments:
            if p.cedulap == search:
                paco.append(p)
        if paco == []:
            print('\nCedula o RIF invalido.')
            self.search_payments_by_dni()
        else:
            for a in paco:
                a.show__()

#busca los pagos realizados en cierta fecha.
    def search_payments_by_date(self):
        paco = []
        while True:
            day = input('\nIngrese el numero del dia que se realizo el pago: ')
            if day.isnumeric():
                day = int(day)
                if day <= 31 and day >= 1:
                    break
                else:
                    print('\nError.') 
            else:
                print('\nError.')
        while True:
            month = input('\nIngrese el numero del mes que se realizo el pago: ')
            if month.isnumeric():
                month = int(month)
                if month <= 12 and month >= 1:
                    break
                else:
                    print('\nError.') 
            else:
                print('\nError.')
        while True:
            year = input('\nIngrese el numero del anio que se realizo el pago: ')
            if year.isnumeric():
                year = int(year)
                if year >= 2023 and year <= 2100:
                    break
                else:
                    print('\nError.') 
            else:
                print('\nError.')
        fecha = date(year,month,day)
        for p in self.list_payments:
            if p.dateP == fecha:
                paco.append(p)
        if paco == []:
            print('\nFecha invalida.')
            self.search_payments_by_date()
        else:
            for a in paco:
                a.show__()

#busca los pagos realizados a traves del metodo de pago.
    def search_payments_by_method(self):
        paco = []
        search = input('\n1. Punto de venta.\n2. Pago movil.\n3. Zelle.\n4. Cash.\nIngrese el numero correspondiente a la forma de pago que desea buscar: ')
        while search != '1' and search != '2' and search != '3' and search != '4':
            search = input('\nError.\n\n1. Punto de venta.\n2. Pago movil.\n3. Zelle.\n4. Cash.\nIngrese el numero correspondiente a la forma de pago que desea buscar: ')
        if search == '1':
            search = 'PdV'
        elif search == '2':
            search = 'PM'
        elif search == '3':
            search = 'Zelle'
        elif search == '4':
            search = 'Cash'
        for p in self.list_payments:
            if p.type_of_paymentP == search:
                paco.append(p)
        if paco == []:
            print('\nNo han habido pagos con este metodo.')
            self.search_payments_by_method()
        else:
            for a in paco:
                a.show__()

#busca los pagos realizados a traves de la moneda de pago.
    def search_payments_by_coin(self):
        paco = []
        search = input('\n1. Bolivares.\n2. Dolares.\nIngrese el numero correspondiente a la moneda de pago que desea buscar: ')
        while search != '1' and search != '2':
            search = input('\nError.\n\n1. Bolivares.\n2. Dolares.\nIngrese el numero correspondiente a la moneda de pago que desea buscar: ')
        if search == '1':
            search = 'Bs.'
        elif search == '2':
            search = '$'
        for p in self.list_payments:
            if p.coinP == search:
                paco.append(p)
        if paco == []:
            print('\nNo han habido pagos con esta moneda.')
            self.search_payments_by_coin()
        else:
            for a in paco:
                a.show__()
                break

#reinicia el .txt como si estuviera vacio.
    def reboot_payments(self):
        file = open('old_list_payments.txt', 'wb')
        paquito = pickle.dumps('hola mundo!')
        file.write(paquito)
        file.close()        
        



#actualiza la lista de envios. Si ya hay envios dentro del .txt, solo lee el .txt; pero si esta vacio, crea una lista vacia.
    def upgrade_shipments(self):
        archivo = open('old_list_shipments.txt', 'rb')
        data = pickle.load(archivo)
        archivo.close()
        if data == 'hola mundo!':
            arch = open('old_list_shipments.txt', 'wb')
            fac = pickle.dumps([])
            arch.write(fac)
            arch.close()
        else:
            archivo = open('old_list_shipments.txt', 'rb')
            self.list_shipments = pickle.load(archivo)
            archivo.close()

#registra un envio a la lista de pagos.
    def create_shipment(self):
        maco = 'pico'
        order = input('\nIngrese el numero de la orden dada en la venta: ')
        for i in self.list_sells:
            if i.order == order:
                maco = 'paso'
                if i.enviado == 'no':
                    nombre = i.nombre
                    tipo = i.tipo
                    cedula = i.cedula
                    correo = i.correo
                    direccion = i.direccion
                    telefono = i.telefono
                    moneda = i.moneda
                    if i.shipping_method == 'Delivery':
                        costo = 5
                        rider = 'Nombre: Car Ses\nNumero telefonico: 04123819302'
                    else:
                        costo = 10
                        rider = 'None'
                    metodo_de_envio = i.shipping_method
                    fecha = date.today()
                    new_shipment = Shipment(nombre,tipo,cedula,correo,direccion,telefono,fecha,order,metodo_de_envio,rider,costo,moneda)
                    self.list_shipments.append(new_shipment)
                    i.enviado = 'si'
                    print('\nEnvio registrado.\n')
                    for i in self.list_shipments:
                        if order == i.orderS:
                            i.show___()
                    break
                elif i.enviado == 'si':
                    print('\nEl envio ya fue registrado/n')
                    prueba = i.order
                    for h in self.list_shipments:
                        if h.orderS == prueba:
                            h.show___()
        if maco != 'paso':
            print('\nNumero de orden no encontrada.')
            self.create_shipment()

#busca los envios realizados para el mismo cliente a traves de la cedula o RIF.
    def search_shipments_by_dni(self):
        paco = []
        search = input('\nIngrese la cedula o RIF del cliente en la lista de envios que desea buscar: ')
        for p in self.list_shipments:
            if p.cedulaS == search:
                paco.append(p)
        if paco == []:
            print('\nCedula o RIF invalido.')
            self.search_shipments_by_dni()
        else:
            for a in paco:
                a.show___()

#busca los envios realizados en cierta fecha.
    def search_shipments_by_date(self):
        paco = []
        while True:
            day = input('\nIngrese el numero del dia que se realizo el pago: ')
            if day.isnumeric():
                day = int(day)
                if day <= 31 and day >= 1:
                    break
                else:
                    print('\nError.') 
            else:
                print('\nError.')
        while True:
            month = input('\nIngrese el numero del mes que se realizo el pago: ')
            if month.isnumeric():
                month = int(month)
                if month <= 12 and month >= 1:
                    break
                else:
                    print('\nError.') 
            else:
                print('\nError.')
        while True:
            year = input('\nIngrese el numero del anio que se realizo el pago: ')
            if year.isnumeric():
                year = int(year)
                if year >= 2023 and year <= 2100:
                    break
                else:
                    print('\nError.') 
            else:
                print('\nError.')
        fecha = date(year,month,day)
        for p in self.list_shipments:
            if p.dateS == fecha:
                paco.append(p)
        if paco == []:
            print('\nFecha invalida.')
            self.search_shipments_by_date()
        else:
            for a in paco:
                a.show___()
    
#reinicia el .txt como si estuviera vacio.
    def reboot_shipments(self):
        file = open('old_list_shipments.txt', 'wb')
        paquito = pickle.dumps('hola mundo!')
        file.write(paquito)
        file.close()   




#muestra las ventas realizadas en ciertas fechas junto a sus 5 productos mas vendidos y sus 5 clientes mas recurrentes.
    def sells_stats_by_date(self):
        paco = []
        search = input('\n1. Buscar por anio.\n2. Buscar por mes.\n3. Buscar por semana.\n4. Buscar por dia.\nEscoja el tipo de busqueda por fecha que desee: ')
        while search != '1' and search != '2' and search != '3' and search != '4':
            print('\nError.')
            self.sells_stats_by_date()
        if search == '1':
            search = 'anio'
            while True:
                year = input('\nIngrese el numero del anio que se realizaron las ventas: ')
                if year.isnumeric():
                    year = int(year)
                    if year >= 2023 and year <= 2100:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            for i in self.list_sells:
                if int(i.datee.year) == year:
                    paco.append(i)
        elif search == '2':
            search = 'mes'
            while True:
                year = input('\nIngrese el numero del anio que se realizaron las ventas: ')
                if year.isnumeric():
                    year = int(year)
                    if year >= 2023 and year <= 2100:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            while True:
                month = input('\nIngrese el numero del mes que se realizaron las ventas: ')
                if month.isnumeric():
                    month = int(month)
                    if month <= 12 and month >= 1:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            for i in self.list_sells:
                if int(i.datee.month) == month and int(i.datee.year) == year:
                    paco.append(i)
        elif search == '3':
            search = 'semana'
            while True:
                day = input('\nIngrese el numero del dia de la semana que se realizaron las ventas: ')
                if day.isnumeric():
                    day = int(day)
                    if day <= 31 and day >= 1:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            while True:
                month = input('\nIngrese el numero del mes que se realizaron las ventas: ')
                if month.isnumeric():
                    month = int(month)
                    if month <= 12 and month >= 1:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            while True:
                year = input('\nIngrese el numero del anio que se realizaron las ventas: ')
                if year.isnumeric():
                    year = int(year)
                    if year >= 2023 and year <= 2100:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            week = date(year,month,day).strftime("%V")
            for i in self.list_sells:
                a = date(i.datee.year,i.datee.month,i.datee.day).strftime("%V")
                if a == week:
                    paco.append(i)
        elif search == '4':
            search = 'dia'
            while True:
                day = input('\nIngrese el numero del dia que se realizaron las ventas: ')
                if day.isnumeric():
                    day = int(day)
                    if day <= 31 and day >= 1:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            while True:
                month = input('\nIngrese el numero del mes que se realizaron las ventas: ')
                if month.isnumeric():
                    month = int(month)
                    if month <= 12 and month >= 1:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            while True:
                year = input('\nIngrese el numero del anio que se realizaron las ventas: ')
                if year.isnumeric():
                    year = int(year)
                    if year >= 2023 and year <= 2100:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            fecha = date(year,month,day)
            for i in self.list_sells:
                if i.datee == fecha:
                    paco.append(i)
        print(f'\nEstas fueron las ventas por {search} que fue indicado:')
        for l in paco:
            l.show____()
        peco = {}
        pico = {}
        for i in paco:
            for k in i.cart:
                if k.name in peco:
                    peco[k.name] += k.quantity
                else:
                    peco[k.name] = k.quantity
        times = 5
        while times != 0:
            a = max(peco.values())
            for o,r in peco.items():
                if a == r:
                    pico[o] = a
                    peco.pop(o)
                    break
            times -= 1
        print('Los 5 productos mas vendidos fueron: {}'.format(pico))

        poco = {}
        puco = {}
        for i in paco:
            if i.cedula in poco:
                poco[i.cedula] += 1
            else:
                poco[i.cedula] = 1
        times = 5
        while times != 0:
            s = max(poco.values())
            for o,r in poco.items():
                if r == s:
                    puco[o] = s
                    poco.pop(o)
                    break
            times -= 1
        print(f'Los 5 clientes mas recurrentes fueron: {puco}')

#muestra los pagos realizados en ciertas fechas.
    def sells_payments_by_date(self):
        paco = []
        search = input('\n1. Buscar por anio.\n2. Buscar por mes.\n3.Buscar por semana.\n4. Buscar por dia.\nEscoja el tipo de busqueda por fecha que desee: ')
        while search != '1' and search != '2' and search != '3' and search != '4':
            print('\nError.')
            self.sells_payments_by_date()
        if search == '1':
            search = 'anio'
            while True:
                year = input('\nIngrese el numero del anio que se realizaron los pagos: ')
                if year.isnumeric():
                    year = int(year)
                    if year >= 2023 and year <= 2100:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            for i in self.list_payments:
                if int(i.dateP.year) == year:
                    paco.append(i)
        elif search == '2':
            search = 'mes'
            while True:
                year = input('\nIngrese el numero del anio que se realizaron los pagos: ')
                if year.isnumeric():
                    year = int(year)
                    if year >= 2023 and year <= 2100:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            while True:
                month = input('\nIngrese el numero del mes que se realizaron los pagos: ')
                if month.isnumeric():
                    month = int(month)
                    if month <= 12 and month >= 1:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            for i in self.list_payments:
                if int(i.dateP.month) == month and int(i.dateP.year) == year:
                    paco.append(i)
        elif search == '3':
            search = 'semana'
            while True:
                day = input('\nIngrese el numero del dia de la semana que se realizaron los pagos: ')
                if day.isnumeric():
                    day = int(day)
                    if day <= 31 and day >= 1:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            while True:
                month = input('\nIngrese el numero del mes que se realizaron los pagos: ')
                if month.isnumeric():
                    month = int(month)
                    if month <= 12 and month >= 1:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            while True:
                year = input('\nIngrese el numero del anio que se realizaron los pagos: ')
                if year.isnumeric():
                    year = int(year)
                    if year >= 2023 and year <= 2100:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            week = date(year,month,day).strftime("%V")
            for i in self.list_payments:
                a = date(i.dateP.year,i.dateP.month,i.dateP.day).strftime("%V")
                if a == week:
                    paco.append(i)
        elif search == '4':
            search = 'dia'
            while True:
                day = input('\nIngrese el numero del dia que se realizaron los pagos: ')
                if day.isnumeric():
                    day = int(day)
                    if day <= 31 and day >= 1:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            while True:
                month = input('\nIngrese el numero del mes que se realizaron los pagos: ')
                if month.isnumeric():
                    month = int(month)
                    if month <= 12 and month >= 1:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            while True:
                year = input('\nIngrese el numero del anio que se realizaron los pagos: ')
                if year.isnumeric():
                    year = int(year)
                    if year >= 2023 and year <= 2100:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            fecha = date(year,month,day)
            for i in self.list_payments:
                if i.dateP == fecha:
                    paco.append(i)
        print(f'\nEstos fueron los pagos por {search} que fue indicado:')
        for i in paco:
            i.show__()

#muestra los clientes con pagos pendientes.
    def pending_payments(self):
        paco = []
        for i in self.list_sells:
            if i.debe == 'si':
                a = i.cedula
                for w in self.new_customers:
                    if a == w.dni:
                        paco.append(w)
        if paco == []:
            print('\nTodos los clientes estan solventes.')
        else:
            print('\nEstos son los clientes con pagos pendientes:\n')
            for e in paco:
                e.show_()

#muestra los envios realizados en ciertas fechas 
    def sells_shipments_by_date(self):
        paco = []
        search = input('\n1. Buscar por anio.\n2. Buscar por mes.\n3.Buscar por semana.\n4. Buscar por dia.\nEscoja el tipo de busqueda por fecha que desee: ')
        while search != '1' and search != '2' and search != '3' and search != '4':
            print('\nError.')
            self.sells_shipments_by_date()
        if search == '1':
            search = 'anio'
            while True:
                year = input('\nIngrese el numero del anio que se realizaron los envios: ')
                if year.isnumeric():
                    year = int(year)
                    if year >= 2023 and year <= 2100:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            for i in self.list_shipments:
                if int(i.dateS.year) == year:
                    paco.append(i)
        elif search == '2':
            search = 'mes'
            while True:
                year = input('\nIngrese el numero del anio que se realizaron los envios: ')
                if year.isnumeric():
                    year = int(year)
                    if year >= 2023 and year <= 2100:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            while True:
                month = input('\nIngrese el numero del mes que se realizaron los envios: ')
                if month.isnumeric():
                    month = int(month)
                    if month <= 12 and month >= 1:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            for i in self.list_shipments:
                if int(i.dateS.month) == month and int(i.dateS.year) == year:
                    paco.append(i)
        elif search == '3':
            search = 'semana'
            while True:
                day = input('\nIngrese el numero del dia de la semana que se realizaron los envios: ')
                if day.isnumeric():
                    day = int(day)
                    if day <= 31 and day >= 1:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            while True:
                month = input('\nIngrese el numero del mes que se realizaron los envios: ')
                if month.isnumeric():
                    month = int(month)
                    if month <= 12 and month >= 1:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            while True:
                year = input('\nIngrese el numero del anio que se realizaron los envios: ')
                if year.isnumeric():
                    year = int(year)
                    if year >= 2023 and year <= 2100:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            week = date(year,month,day).strftime("%V")
            for i in self.list_shipments:
                a = date(i.dateS.year,i.dateS.month,i.dateS.day).strftime("%V")
                if a == week:
                    paco.append(i)
        elif search == '4':
            search = 'dia'
            while True:
                day = input('\nIngrese el numero del dia que se realizaron los envios: ')
                if day.isnumeric():
                    day = int(day)
                    if day <= 31 and day >= 1:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            while True:
                month = input('\nIngrese el numero del mes que se realizaron los envios: ')
                if month.isnumeric():
                    month = int(month)
                    if month <= 12 and month >= 1:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            while True:
                year = input('\nIngrese el numero del anio que se realizaron los envios: ')
                if year.isnumeric():
                    year = int(year)
                    if year >= 2023 and year <= 2100:
                        break
                    else:
                        print('\nError.') 
                else:
                    print('\nError.')
            fecha = date(year,month,day)
            for i in self.list_shipments:
                if i.dateS == fecha:
                    paco.append(i)
        print(f'\nEstos fueron los pagos por {search} que fue indicado:')
        for i in paco:
            i.show___()

#muestra los productos mas enviados.
    def most_deliveried_products(self):
        paco = self.list_sells
        peco = {}
        pico = {}
        for i in paco:
            if i.enviado == 'si':
                for k in i.cart:
                    if k.name in peco:
                        peco[k.name] += 1
                    else:
                        peco[k.name] = 1
        times = 5
        while times != 0:
            a = max(peco.values())
            for o,r in peco.items():
                if a == r:
                    pico[o] = a
                    peco.pop(o)
                    break
            times -= 1
        print('Los 5 productos mas enviados fueron: {}'.format(pico))

#muestra los clientes con envios pendientes.
    def pending_shipments(self):
        paco = []
        for i in self.list_sells:
            if i.enviado == 'no':
                a = i.cedula
                for w in self.new_customers:
                    if a == w.dni:
                        paco.append(w)
        if paco == []:
            print('\nNo hay envios pendientes.')
        else:
            print('\nEstos son los clientes con envios pendientes:\n')
            for e in paco:
                e.show_()




#guarda los datos de las listas dentro de los .txt.
    def exit_general(self):
        file = open('old_list.txt', 'wb')
        paquito = pickle.dumps(self.new_list)
        file.write(paquito)
        file.close()
        file = open('old_list_c.txt', 'wb')
        paquito = pickle.dumps(self.new_customers)
        file.write(paquito)
        file.close()
        file = open('old_list_sells.txt', 'wb')
        paquito = pickle.dumps(self.list_sells)
        file.write(paquito)
        file.close()
        file = open('old_list_payments.txt', 'wb')
        paquito = pickle.dumps(self.list_payments)
        file.write(paquito)
        file.close()
        file = open('old_list_shipments.txt', 'wb')
        paquito = pickle.dumps(self.list_shipments)
        file.write(paquito)
        file.close()


#muestra la lista de productos.
    def show(self):
        for p in self.new_list:
            p.show()

#muestra la lista de clientes.
    def show_(self):
        for p in self.new_customers:
            p.show_()

#muestra la lista de pagos.
    def show__(self):
        for p in self.list_payments:
            p.show__()

#muestra la lista de envios.
    def show___(self):
        for p in self.list_shipment:
            p.show___()  

#muestra la lista de ventas.
    def show____(self):
        for p in self.list_sells:
            p.show____()