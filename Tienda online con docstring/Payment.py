class Payment:
    def __init__(self,nombrep,tipop,cedulap,correop,direccionp,telefonop,dateP,orderP,amountP,coinP,type_of_paymentP):
        self.nombrep = nombrep
        self.tipop = tipop
        self.cedulap = cedulap
        self.correop = correop
        self.direccionp = direccionp
        self.telefonop = telefonop
        self.dateP = dateP
        self.orderP = orderP
        self.amountP = amountP
        self.coinP = coinP
        self.type_of_paymentP = type_of_paymentP
    
    def show__(self):
        print(f'Fecha: {self.dateP}\n\nCliente:\nNombre y apellido / Razon social: {self.nombrep} \nTipo de cliente: {self.tipop} \nID: {self.cedulap} \nCorreo electronico: {self.correop} \nDireccion de envio: {self.direccionp} \nNumero de telefono: {self.telefonop}\n\nTotal: {self.amountP}{self.coinP}\n\nMetodo de pago: {self.type_of_paymentP}')