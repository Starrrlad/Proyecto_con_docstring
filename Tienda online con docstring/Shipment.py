class Shipment:
    def __init__(self,nombreS,tipoS,cedulaS,correoS,direccionS,telefonoS,dateS,orderS,ship_methodS,riderS,costS,monedaS):
        self.nombreS = nombreS
        self.tipoS = tipoS
        self.cedulaS = cedulaS
        self.correoS = correoS
        self.direccionS = direccionS
        self.telefonoS = telefonoS
        self.dateS = dateS
        self.orderS = orderS
        self.ship_methodS = ship_methodS
        self.riderS = riderS
        self.costS = costS
        self.monedaS = monedaS
    
    def show___(self):
        print(f'Fecha: {self.dateS}\n\nOrden de la compra: {self.orderS}\n\nCliente:\nNombre y apellido / Razon social: {self.nombreS} \nTipo de cliente: {self.tipoS} \nID: {self.cedulaS} \nCorreo electronico: {self.correoS} \nDireccion de envio: {self.direccionS} \nNumero de telefono: {self.telefonoS}\n\nMetodo de envio: {self.ship_methodS}\n\nDatos del motorizado:\n{self.riderS}\n\nCosto de envio: {self.costS}{self.monedaS}')