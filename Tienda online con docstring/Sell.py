class Sell:
    def __init__(self,order,datee,nombre,tipo,cedula,correo,direccion,telefono,cart_legible,cart,payment_moment,debe,payment_method,moneda,shipping_method,subtotal,discount,iva,igtf,total,enviado):
        self.order = order
        self.datee = datee
        self.nombre = nombre
        self.tipo = tipo
        self.cedula = cedula
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono
        self.cart_legible = cart_legible
        self.cart = cart
        self.payment_moment = payment_moment
        self.debe = debe
        self.payment_method = payment_method
        self.moneda = moneda
        self.shipping_method = shipping_method
        self.subtotal = subtotal
        self.discount = discount
        self.iva = iva
        self.igtf = igtf
        self.total = total
        self.enviado = enviado


    
    def show____(self):
        print(f'\n\n\nOrden: {self.order}\n\nFecha: {self.datee}\n\nCliente:\nNombre y apellido / Razon social: {self.nombre} \nTipo de cliente: {self.tipo} \nID: {self.cedula} \nCorreo electronico: {self.correo} \nDireccion de envio: {self.direccion} \nNumero de telefono: {self.telefono}\n\nCarrito:\n{self.cart_legible}\n\nMomento de pago: {self.payment_moment}\n\nMetodo de pago: {self.payment_method}\n\nMetodo de envio: {self.shipping_method}\n\nSubtotal: {self.subtotal}{self.moneda}\nDescuentos: {self.discount}{self.moneda}\nIVA: {self.iva}{self.moneda}\nIGTF: {self.igtf}{self.moneda}\nTotal: {self.total}{self.moneda}')
