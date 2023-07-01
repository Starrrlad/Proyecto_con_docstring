class Customer:
    def __init__(self,complete_name,customer_type,dni,email,address,telef_numb):
        self.complete_name = complete_name
        self.customer_type = customer_type
        self.dni = dni
        self.email = email
        self.address = address
        self.telef_numb = telef_numb

    def show_(self):
        print(f"Nombre y apellido / Razon social: {self.complete_name} \nTipo de cliente: {self.customer_type} \nID: {self.dni} \nCorreo electronico: {self.email} \nDireccion de envio: {self.address} \nNumero de telefono: {self.telef_numb}\n\n")
    
    def retorno_(self):
        return f"Nombre y apellido / Razon social: {self.complete_name} \nTipo de cliente: {self.customer_type} \nID: {self.dni} \nCorreo electronico: {self.email} \nDireccion de envio: {self.address} \nNumero de telefono: {self.telef_numb}\n\n"