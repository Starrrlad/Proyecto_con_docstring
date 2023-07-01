from App import App
from api import old_list

def main():
    sis = App(old_list)
    sis.upgrade_sells()
    sis.upgrade_cust()
    sis.upgrade_inv()
    sis.upgrade_payments()
    sis.upgrade_shipments()
    while True:
        print('\n//////////Tienda en línea de productos naturales//////////\n')
        q = input('\nSeleccione una opcion:\n1. Gestion de productos.\n2. Gestión de ventas.\n3. Gestión de clientes.\n4. Gestión de pagos.\n5. Gestión de envíos.\n6. Indicadores de gestión.\n7. Reiniciar...\nIngrese cualquier otro valor para salir.\n>>')
        if q == '1':
            w = input('\nSeleccione una opcion de Gestion de productos:\n1. Agregar nuevo producto.\n2. Buscar producto.\n3. Modificar informacion de un producto\n4. Eliminar producto.\nIngrese cualquier otro valor para volver.\n>>')
            if w == '1':
                sis.add_product()
                sis.exit_general()
                main()
            elif w == '2':
                e = input('\nSeleccione una opcion para buscar el producto:\n1. Buscar por nombre.\n2. Buscar por precio.\n3. Buscar por categoria\n4. Buscar por disponibilidad.\nIngrese cualquier otro valor para volver.\n>>')
                if e == '1':
                    sis.search_products_by_name()
                    main()
                elif e == '2':
                    sis.search_products_by_price()
                    main()
                elif e == '3':
                    sis.search_products_by_category()
                    main()
                elif e == '4':
                    sis.search_products_by_availability()
                    main()
                else:
                    main()
            elif w == '3':
                sis.modify_product()
                sis.exit_general()
                main()
            elif w == '4':
                sis.eliminate_product()
                sis.exit_general()
                main()
            else:
                main()
        elif q == '2':
            r = input('\nSeleccione una opcion de Gestion de ventas:\n1. Registrar venta.\n2. Buscar venta.\nIngrese cualquier otro valor para volver.\n>>')
            if r == '1':
                sis.register_sell()
                sis.exit_general()
                main()
            elif r == '2':
                t = input('\nSeleccione una opcion para buscar el la venta:\n1. Buscar por cedula o rif del cliente.\n2. Buscar por fecha.\n3. Buscar por monto total\nIngrese cualquier otro valor para volver.\n>>')
                if t == '1':
                    sis.search_sells_by_dni()
                    main()
                elif t == '2':
                    sis.search_sells_by_date()
                    main()
                elif t == '3':
                    sis.search_sells_by_price()
                    main()
                else:
                    main()
            else:
                main()
        elif q == '3':
            y = input('\nSeleccione una opcion de Gestion de clientes:\n1. Registrar cliente.\n2. Modificar informacion de un cliente.\n3. Eliminar cliente.\n4. Buscar cliente.\nIngrese cualquier otro valor para volver.\n>>')
            if y == '1':
                sis.add_customer()
                sis.exit_general()
                main()
            elif y == '2':
                sis.modify_customer()
                sis.exit_general()
                main()
            elif y == '3':
                sis.eliminate_customer()
                sis.exit_general()
                main()
            elif y == '4':
                u = input('\nSeleccione una opcion para buscar el cliente:\n1. Buscar por cedula o RIF.\n2. Buscar por correo electronico.\nIngrese cualquier otro valor para volver.\n>>')
                if u == '1':
                    sis.search_customer_by_dni()
                    main()
                elif u == '2':
                    sis.search_customer_by_email()
                    main()
                else:
                    main()
            else:
                main()
        elif q == '4':
            i = input('\nSeleccione una opcion de Gestion de pagos:\n1. Registrar pago.\n2. Buscar pago.\nIngrese cualquier otro valor para volver.\n>>')
            if i == '1':
                sis.create_bill()
                sis.exit_general()
                main()
            elif i == '2':
                o = input('\nSeleccione una opcion para buscar el pago:\n1. Buscar por cedula o RIF del cliente.\n2. Buscar por fecha.\n3. Buscar por tipo de pago.\n4. Buscar por moneda de pago.\nIngrese cualquier otro valor para volver.\n>>')
                if o == '1':
                    sis.search_payments_by_dni()
                    main()
                elif o == '2':
                    sis.search_payments_by_date()
                    main()
                elif o == '3':
                    sis.search_payments_by_method()
                    main()
                elif o == '4':
                    sis.search_payments_by_coin()
                    main()
                else:
                    main()
            else:
                main()
        elif q == '5':
            p = input('\nSeleccione una opcion de Gestion de envios:\n1. Registrar envio.\n2. Buscar envio.\nIngrese cualquier otro valor para volver.\n>>')
            if p == '1':
                sis.create_shipment()
                sis.exit_general()
                sis.main()
            elif p == '2':
                a = input('\nSeleccione una opcion para buscar el envio:\n1. Buscar por cedula o RIF del cliente.\n2. Buscar por fecha.\nIngrese cualquier otro valor para volver.\n>>')
                if a == '1':
                    sis.search_shipments_by_dni()
                    main()
                elif a == '2':
                    sis.search_shipments_by_date()
                    main()
                else:
                    main()
            else:
                main()

        elif q == '6':
            s = input('\nSeleccione una opcion de Indicadores de gestion:\n1. Informes de venta.\n2. Informes de pago.\n3. Informes de envios.\nIngrese cualquier otro valor para volver.\n>>')
            if s == '1':
                sis.sells_stats_by_date()
                main()
            elif s == '2':
                d = input('\nSeleccione una opcion para el informe de pago:\n1. Pagos totales por fecha.\n2. Clientes con pagos pendientes.\nIngrese cualquier otro valor para volver.\n>>')
                if d == '1':
                    sis.sells_payments_by_date()
                elif d == '2':
                    sis.pending_payments()
                else:
                    main()
            elif s == '3':
                f = input('\nSeleccione una opcion para buscar el informe del envio:\n1. Envios totales por fecha.\n2. Productos mas enviados.\n3. Clientes con envios pendientes.\nIngrese cualquier otro valor para volver.\n>>')
                if f == '1':
                    sis.sells_shipments_by_date()
                    main()
                if f == '2':
                    sis.most_deliveried_products()
                    main()
                elif f == '3':
                    sis.pending_shipments()
                    main()
            else:
                main()
        elif q == '7':
            g = input('\nSeleccione la carpeta que desea reiniciar desde su estado inicial:\n1. Reiniciar productos.\n2. Reiniciar ventas.\n3. Reiniciar clientes.\n4. Reiniciar pagos.\n5. Reiniciar envios.\nIngrese cualquier otro valor para volver.\n>>')
            if g == '1':
                sis.reboot_p()
                main()
            elif g == '2':
                sis.reboot_sells()
                main()
            elif g == '3':
                sis.reboot_c()
                main()
            elif g == '4':
                sis.reboot_payments()
                main()
            elif g == '5':
                sis.reboot_shipments()
                main()
            else:
                main()
        else:
            print('Salida exitosa')
            break


        
main()