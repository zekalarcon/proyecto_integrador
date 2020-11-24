import csv
import datetime


def la_barbieria():

    with open('barbieria.csv', 'a') as fi:
        header = ['PELUQUERIA_OPERACION','NOMBRE_CLIENTE','TELEFONO_CLIENTE','TINTURA_1','CANT_TINTURA_1',
        'TINTURA_2','CANT_TINTURA_2','TINTURA_3','CANT_TINTURA_3','REFLEJO_1','CANT_REFLEJO_1',
        'REFLEJO_2','CANT_REFLEJO_2','REFLEJO_3','CANT_REFLEJO_3','OXIGENADA_VOLUMEN','CANT_OXIGENADA',
        'CANT_POLVO','CANT_QUERATINA','CANT_ALISADO','CANT_PLASTIFICADO','CANT_BIOMOLECULAR','CANT_ARGAN',
        'CANT_ESPEJO','CANT_BIOTINA','CANT_BOTOX','CANT_LIFTING','PRECIO','FECHA','PRODUCTO_STOCK',
        'CANTIDAD_STOCK','PRECIO_STOCK']
        writer = csv.DictWriter(fi, fieldnames=header)

                    
    
        print('Bienvenido!\n')
    
        
        while True:

            print(
                '                   *****************************************************************************************************\n'
                '                   **                                                                                                 **\n'
                '                   **      $$        $$$         $$$$$     $$$    $$$$$   $$$$$   $$  $$$$$  $$$$$   $$    $$$        **\n'
                '                   **      $$      $$   $$       $$  $$  $$   $$  $$  $$  $$  $$  $$  $$     $$  $$  $$  $$   $$      **\n' 
                '                   **      $$      $$$$$$$       $$$$$   $$$$$$$  $$$$$   $$$$$   $$  $$$$   $$$$$   $$  $$$$$$$      **\n'
                '                   **      $$      $$   $$       $$  $$  $$   $$  $$  $$  $$  $$  $$  $$     $$  $$  $$  $$   $$      **\n'
                '                   **      $$$$$$                $$$$$                    $$$$$       $$$$$                           **\n'
                '                   **                                                                                                 **\n'
                '                   *****************************************************************************************************                                                                                    '
            )


            print(
                '1- Peluqueria\n'
                '2- Agregar stock\n'
                '3- Fin programa\n'  
            )



            try:
                opcion = int(input('Ingrese opcion para continuar:\n'))
            except:
                print('Opcion incorrecta\n')
                continue
        
            if opcion == 3:
                break
        
            if opcion > 3:
                print('Opcion incorrecta')
        
            if opcion == 1:
                while True:
                    print(
                        '1- Corte\n'
                        '2- Barba\n'
                        '3- Tintura\n'
                        '4- Balayage\n'
                        '5- Reflejos\n'
                        '6- Queratina\n'
                        '7- Alisado\n'
                        '8- Plastificado\n'
                        '9- Biomolecular\n'
                        '10- Argan\n'
                        '11- Espejo\n'
                        '12- Biotina\n'
                        '13- Botox\n'
                        '14- Lifting\n'
                        '15- Volver atras\n'
                    )
            
                    
                    try:
                        operacion = int(input('Ingrese operacion a realizar:\n'))
                    except:
                        print('Operacion incorrecta\n')
                        continue
                    
                    
                    if operacion == 15:
                        break

                    
                    if operacion > 15:
                        print('Operacion incorrecta')
                    
                    
                    if operacion == 1:
                        nombre_cliente = input('Ingrese nombre y apellido del cliente:\n')
                        telefono_cliente = input('Ingrese telefono del cliente:\n') 
                        precio = input('Ingrese importe:\n')
                        writer.writerow({'PELUQUERIA_OPERACION':'CORTE','NOMBRE_CLIENTE':nombre_cliente.upper(),
                                        'TELEFONO_CLIENTE':telefono_cliente,'PRECIO':precio,'FECHA':datetime.date.today()})

                    
                    if operacion == 2:
                        nombre_cliente = input('Ingrese nombre y apellido del cliente:\n')
                        telefono_cliente = input('Ingrese telefono del cliente:\n') 
                        precio = input('Ingrese importe:\n')
                        writer.writerow({'PELUQUERIA_OPERACION':'BARBA','NOMBRE_CLIENTE':nombre_cliente.upper(),
                                        'TELEFONO_CLIENTE':telefono_cliente,'PRECIO':precio,'FECHA':datetime.date.today()})
                    
                    
                    if operacion == 3:
                        nombre_cliente = input('Ingrese nombre y apellido del cliente:\n')
                        telefono_cliente = input('Ingrese telefono del cliente:\n')
                        tintura_numero_uno = input('Ingrese numero de tintura (EJ: 7 o 9.2):\n')
                        cantidad_tintura_uno = input('Ingrese cantidad de tintura a utilizar:\n')
                        oxigenada_volumen = input('Ingrese el numero de volumen del agua oxigena (EJ: 30):\n')
                        cantidad_oxigenada = input('Ingrese cantidad de agua oxigenada a utilizar:\n')
                        cantidad_polvo = input('Ingrese cantidad de polvo decolorante a utilizar:\n')
                        hacer_reflejo = input('Desea utilizar reflejos? Ingrese SI o NO:\n').upper()
                        if hacer_reflejo == 'NO':
                            precio = input('Ingrese importe:\n')
                            writer.writerow({'PELUQUERIA_OPERACION':'TINTURA','NOMBRE_CLIENTE':nombre_cliente.upper(),
                                            'TELEFONO_CLIENTE':telefono_cliente,'TINTURA_1':tintura_numero_uno,
                                            'CANT_TINTURA_1':cantidad_tintura_uno,'OXIGENADA_VOLUMEN':oxigenada_volumen,
                                            'CANT_OXIGENADA':cantidad_oxigenada,'CANT_POLVO':cantidad_polvo,
                                            'PRECIO':precio,'FECHA':datetime.date.today()})
                        if hacer_reflejo == 'SI':
                            reflejo_uno = input('Ingrese el numero del primer reflejo (EJ: 3):\n')
                            cantidad_reflejo_uno = input('Ingrese cantidad de reflejo a utilizar (EJ: 20):\n')
                            reflejo_dos = input('Ingrese el numero del segundo reflejo (EJ: 3):\n')
                            cantidad_reflejo_dos = input('Ingrese cantidad de reflejo a utilizar (EJ: 20):\n')
                            reflejo_tres = input('Ingrese el numero del tercer reflejo (EJ: 3):\n')
                            cantidad_reflejo_tres = input('Ingrese cantidad de reflejo a utilizar (EJ: 20):\n')
                            precio = input('Ingrese importe:\n')
                            writer.writerow({'PELUQUERIA_OPERACION':'TINTURA','NOMBRE_CLIENTE':nombre_cliente.upper(),
                                            'TELEFONO_CLIENTE':telefono_cliente,'TINTURA_1':tintura_numero_uno,
                                            'CANT_TINTURA_1':cantidad_tintura_uno,'OXIGENADA_VOLUMEN':oxigenada_volumen,
                                            'CANT_OXIGENADA':cantidad_oxigenada,'CANT_POLVO':cantidad_polvo,'REFLEJO_1':reflejo_uno,
                                            'CANT_REFLEJO_1':cantidad_reflejo_uno,'REFLEJO_2':reflejo_dos,'CANT_REFLEJO_2':cantidad_reflejo_dos,
                                            'REFLEJO_3':reflejo_tres,'CANT_REFLEJO_3':cantidad_reflejo_tres,
                                            'PRECIO':precio,'FECHA':datetime.date.today()}) 

                    
                    if operacion == 4:
                        nombre_cliente = input('Ingrese nombre y apellido del cliente:\n')
                        telefono_cliente = input('Ingrese telefono del cliente:\n')
                        tintura_numero_uno = input('Ingrese numero de tintura (EJ: 7 o 9.2):\n')
                        cantidad_tintura_uno = input('Ingrese cantidad de tintura a utilizar:\n')
                        tintura_numero_dos = input('Ingrese numero de segunda tintura a utilizar (EJ: 7 o 9.2):\n')
                        cantidad_tintura_dos = input('Ingrese cantidad de tintura a utilizar:\n')
                        tintura_numero_tres = input('Ingrese numero de tercera tintura a utilizar (EJ: 7 o 9.2):\n')
                        cantidad_tintura_tres = input('Ingrese cantidad de tintura a utilizar:\n')
                        oxigenada_volumen = input('Ingrese el numero de volumen del agua oxigena (EJ: 30):\n')
                        cantidad_oxigenada = input('Ingrese cantidad de agua oxigenada a utilizar:\n')
                        cantidad_polvo = input('Ingrese cantidad de polvo decolorante a utilizar:\n')
                        hacer_reflejo = input('Desea utilizar reflejos? Ingrese SI o NO:\n').upper()
                        if hacer_reflejo == 'NO':
                            precio = input('Ingrese importe:\n')
                            writer.writerow({'PELUQUERIA_OPERACION':'BALAYAGE','NOMBRE_CLIENTE':nombre_cliente.upper(),
                                            'TELEFONO_CLIENTE':telefono_cliente,'TINTURA_1':tintura_numero_uno,
                                            'CANT_TINTURA_1':cantidad_tintura_uno,'TINTURA_2':tintura_numero_dos,
                                            'CANT_TINTURA_2':cantidad_tintura_dos,'TINTURA_3':tintura_numero_tres,
                                            'CANT_TINTURA_3':cantidad_tintura_tres,'OXIGENADA_VOLUMEN':oxigenada_volumen,
                                            'CANT_OXIGENADA':cantidad_oxigenada,'CANT_POLVO':cantidad_polvo,
                                            'PRECIO':precio,'FECHA':datetime.date.today()})
                        if hacer_reflejo == 'SI':
                            reflejo_uno = input('Ingrese el numero del primer reflejo (EJ: 3):\n')
                            cantidad_reflejo_uno = input('Ingrese cantidad de reflejo a utilizar (EJ: 20):\n')
                            reflejo_dos = input('Ingrese el numero del segundo reflejo (EJ: 3):\n')
                            cantidad_reflejo_dos = input('Ingrese cantidad de reflejo a utilizar (EJ: 20):\n')
                            reflejo_tres = input('Ingrese el numero del tercer reflejo (EJ: 3):\n')
                            cantidad_reflejo_tres = input('Ingrese cantidad de reflejo a utilizar (EJ: 20):\n')
                            precio = input('Ingrese importe:\n')
                            writer.writerow({'PELUQUERIA_OPERACION':'BALAYAGE','NOMBRE_CLIENTE':nombre_cliente.upper(),
                                            'TELEFONO_CLIENTE':telefono_cliente,'TINTURA_1':tintura_numero_uno,
                                            'CANT_TINTURA_1':cantidad_tintura_uno,'TINTURA_2':tintura_numero_dos,
                                            'CANT_TINTURA_2':cantidad_tintura_dos,'TINTURA_3':tintura_numero_tres,
                                            'CANT_TINTURA_3':cantidad_tintura_tres,'OXIGENADA_VOLUMEN':oxigenada_volumen,
                                            'CANT_OXIGENADA':cantidad_oxigenada,'CANT_POLVO':cantidad_polvo,'REFLEJO_1':reflejo_uno,
                                            'CANT_REFLEJO_1':cantidad_reflejo_uno,'REFLEJO_2':reflejo_dos,
                                            'CANT_REFLEJO_2':cantidad_reflejo_dos,'REFLEJO_3':reflejo_tres,
                                            'CANT_REFLEJO_3':cantidad_reflejo_tres,'PRECIO':precio,'FECHA':datetime.date.today()})
                    
                    
                    if operacion == 5:
                        nombre_cliente = input('Ingrese nombre y apellido del cliente:\n')
                        telefono_cliente = input('Ingrese telefono del cliente:\n')
                        reflejo_uno = input('Ingrese el numero del primer reflejo (EJ: 3):\n')
                        cantidad_reflejo_uno = input('Ingrese cantidad de reflejo a utilizar (EJ: 20):\n')
                        reflejo_dos = input('Ingrese el numero del segundo reflejo (EJ: 3):\n')
                        cantidad_reflejo_dos = input('Ingrese cantidad de reflejo a utilizar (EJ: 20):\n')
                        reflejo_tres = input('Ingrese el numero del tercer reflejo (EJ: 3):\n')
                        cantidad_reflejo_tres = input('Ingrese cantidad de reflejo a utilizar (EJ: 20):\n')
                        oxigenada_volumen = input('Ingrese el numero de volumen del agua oxigena (EJ: 30):\n')
                        cantidad_oxigenada = input('Ingrese cantidad de agua oxigenada a utilizar:\n')
                        cantidad_polvo = input('Ingrese cantidad de polvo decolorante a utilizar:\n')
                        precio = input('Ingrese importe:\n')
                        writer.writerow({'PELUQUERIA_OPERACION':'REFLEJOS','NOMBRE_CLIENTE':nombre_cliente.upper(),
                                        'TELEFONO_CLIENTE':telefono_cliente,'REFLEJO_1':reflejo_uno,
                                        'CANT_REFLEJO_1':cantidad_reflejo_uno,'REFLEJO_2':reflejo_dos,
                                        'CANT_REFLEJO_2':cantidad_reflejo_dos,'REFLEJO_3':reflejo_tres,
                                        'CANT_REFLEJO_3':cantidad_reflejo_tres,'OXIGENADA_VOLUMEN':oxigenada_volumen,
                                        'CANT_OXIGENADA':cantidad_oxigenada,'CANT_POLVO':cantidad_polvo,
                                        'PRECIO':precio,'FECHA':datetime.date.today()})
                    
                    
                    if operacion == 6:
                        nombre_cliente = input('Ingrese nombre y apellido del cliente:\n')
                        telefono_cliente = input('Ingrese telefono del cliente:\n')
                        cantidad_queratina = input('Ingrese cantidad de queratina a utilizar:\n')
                        precio = input('Ingrese importe:\n')
                        writer.writerow({'PELUQUERIA_OPERACION':'QUERATINA','NOMBRE_CLIENTE':nombre_cliente.upper(),
                                        'TELEFONO_CLIENTE':telefono_cliente,'CANT_QUERATINA':cantidad_queratina,
                                        'PRECIO':precio,'FECHA':datetime.date.today()})
                    
                    
                    if operacion == 7:
                        nombre_cliente = input('Ingrese nombre y apellido del cliente:\n')
                        telefono_cliente = input('Ingrese telefono del cliente:\n')
                        cantidad_alisado = input('Ingrese cantidad de alisado a utilizar:\n')
                        precio = input('Ingrese importe:\n')
                        writer.writerow({'PELUQUERIA_OPERACION':'ALISADO','NOMBRE_CLIENTE':nombre_cliente.upper(),
                                        'TELEFONO_CLIENTE':telefono_cliente,'CANT_ALISADO':cantidad_alisado,
                                        'PRECIO':precio,'FECHA':datetime.date.today()})
                    
                    
                    if operacion == 8:
                        nombre_cliente = input('Ingrese nombre y apellido del cliente:\n')
                        telefono_cliente = input('Ingrese telefono del cliente:\n')
                        cantidad_plastificado = input('Ingrese cantidad de plastificado a utilizar:\n')
                        precio = input('Ingrese importe:\n')
                        writer.writerow({'PELUQUERIA_OPERACION':'PLASTIFICADO','NOMBRE_CLIENTE':nombre_cliente.upper(),
                                        'TELEFONO_CLIENTE':telefono_cliente,'CANT_PLASTIFICADO':cantidad_plastificado,
                                        'PRECIO':precio,'FECHA':datetime.date.today()})
                    
                    
                    if operacion == 9:
                        nombre_cliente = input('Ingrese nombre y apellido del cliente:\n')
                        telefono_cliente = input('Ingrese telefono del cliente:\n')
                        cantidad_biomolecular = input('Ingrese cantidad de biomolecular a utilizar:\n')
                        precio = input('Ingrese importe:\n')
                        writer.writerow({'PELUQUERIA_OPERACION':'ALISADO','NOMBRE_CLIENTE':nombre_cliente.upper(),
                                        'TELEFONO_CLIENTE':telefono_cliente,'CANT_BIOMOLECULAR':cantidad_biomolecular,
                                        'PRECIO':precio,'FECHA':datetime.date.today()})
                    
                    
                    if operacion == 10:
                        nombre_cliente = input('Ingrese nombre y apellido del cliente:\n')
                        telefono_cliente = input('Ingrese telefono del cliente:\n')
                        cantidad_argan = input('Ingrese cantidad de argan a utilizar:\n')
                        precio = input('Ingrese importe:\n')
                        writer.writerow({'PELUQUERIA_OPERACION':'ALISADO','NOMBRE_CLIENTE':nombre_cliente.upper(),
                                        'TELEFONO_CLIENTE':telefono_cliente,'CANT_ARGAN':cantidad_argan,
                                        'PRECIO':precio,'FECHA':datetime.date.today()})
                    
                    
                    if operacion == 11:
                        nombre_cliente = input('Ingrese nombre y apellido del cliente:\n')
                        telefono_cliente = input('Ingrese telefono del cliente:\n')
                        cantidad_espejo = input('Ingrese cantidad de espejo a utilizar:\n')
                        precio = input('Ingrese importe:\n')
                        writer.writerow({'PELUQUERIA_OPERACION':'ALISADO','NOMBRE_CLIENTE':nombre_cliente.upper(),
                                        'TELEFONO_CLIENTE':telefono_cliente,'CANT_ESPEJO':cantidad_espejo,
                                        'PRECIO':precio,'FECHA':datetime.date.today()})
                    
                    
                    if operacion == 12:
                        nombre_cliente = input('Ingrese nombre y apellido del cliente:\n')
                        telefono_cliente = input('Ingrese telefono del cliente:\n')
                        cantidad_biotina = input('Ingrese cantidad de biotina a utilizar:\n')
                        precio = input('Ingrese importe:\n')
                        writer.writerow({'PELUQUERIA_OPERACION':'ALISADO','NOMBRE_CLIENTE':nombre_cliente.upper(),
                                        'TELEFONO_CLIENTE':telefono_cliente,'CANT_BIOTINA':cantidad_biotina,
                                        'PRECIO':precio,'FECHA':datetime.date.today()})
                    
                    
                    if operacion == 13:
                        nombre_cliente = input('Ingrese nombre y apellido del cliente:\n')
                        telefono_cliente = input('Ingrese telefono del cliente:\n')
                        cantidad_botox = input('Ingrese cantidad de botox a utilizar:\n')
                        precio = input('Ingrese importe:\n')
                        writer.writerow({'PELUQUERIA_OPERACION':'ALISADO','NOMBRE_CLIENTE':nombre_cliente.upper(),
                                        'TELEFONO_CLIENTE':telefono_cliente,'CANT_BOTOX':cantidad_botox,
                                        'PRECIO':precio,'FECHA':datetime.date.today()})
                    
                    
                    if operacion == 14:
                        nombre_cliente = input('Ingrese nombre y apellido del cliente:\n')
                        telefono_cliente = input('Ingrese telefono del cliente:\n')
                        cantidad_lifting = input('Ingrese cantidad de lifting a utilizar:\n')
                        precio = input('Ingrese importe:\n')
                        writer.writerow({'PELUQUERIA_OPERACION':'ALISADO','NOMBRE_CLIENTE':nombre_cliente.upper(),
                                        'TELEFONO_CLIENTE':telefono_cliente,'CANT_LIFTING':cantidad_lifting,
                                        'PRECIO':precio,'FECHA':datetime.date.today()})                    
        
            
            if opcion == 2:
                while True:                
                    producto_stock = input('Ingrese producto a stockear (EJ: TINTURA 9.1) o FIN para terminar:\n')
                    producto_stock = producto_stock.upper()
                    if producto_stock == 'FIN':
                        break
                    cantidad_stock = input('Ingrese cantidad (EJ: 100):\n')
                    precio_stock = input('Ingrese precio producto:\n')
                    writer.writerow({'FECHA':datetime.date.today(),'PRODUCTO_STOCK':producto_stock,
                                    'CANTIDAD_STOCK':cantidad_stock,'PRECIO_STOCK':precio_stock})

        

if __name__ == '__main__':
    la_barbieria()