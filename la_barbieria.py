'''
Proyecto Integrador

La Barbieria

Descripcion:
Programa para registar transacciones y stock de la peluqueria
'''


__author__ = "Ezequiel Alarcon"
__email__ = "zekalarcon@gamil.com"


import csv
import datetime


def la_barbieria():

    print('Bienvenido!\n')

    
    while True:
        with open('barbieria.csv', 'a') as fi:
            header = ['PELUQUERIA_OPERACION', 'NOMBRE_CLIENTE', 'TELEFONO_CLIENTE', 'TINTURA_1', 'CANT_TINTURA_1',
                      'TINTURA_2', 'CANT_TINTURA_2', 'TINTURA_3', 'CANT_TINTURA_3', 'REFLEJO_1', 'CANT_REFLEJO_1',
                      'REFLEJO_2', 'CANT_REFLEJO_2', 'REFLEJO_3', 'CANT_REFLEJO_3', 'OXIGENADA_VOLUMEN', 'CANT_OXIGENADA',
                      'CANT_POLVO', 'CANT_QUERATINA', 'CANT_ALISADO', 'CANT_PLASTIFICADO', 'CANT_BIOMOLECULAR', 'CANT_ARGAN',
                      'CANT_ESPEJO', 'CANT_BIOTINA', 'CANT_BOTOX', 'CANT_LIFTING', 'PRECIO', 'FECHA', 'PRODUCTO_STOCK',
                      'CANTIDAD_STOCK', 'PRECIO_STOCK']
            writer = csv.DictWriter(fi, fieldnames=header)

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

                    opciones = ['Corte', 'Barba', 'Tintura', 'Balayage', 'Reflejos',
                                'Queratina', 'Alisado', 'Plastificado', 'Biomolecular', 'Argan',
                                'Espejo', 'Biotina', 'Botox', 'Lifting', 'Volver atras']

                    for i in opciones:
                        index = opciones.index(i)
                        print(index + 1 ,'-', i)

                    try:
                        operacion = int(
                            input('Ingrese operacion a realizar:\n'))
                    except:
                        print('Operacion incorrecta. Ingrese un numero del 1 al 15\n')
                        continue

                    if operacion == 15:
                        break

                    if operacion > 15:
                        print('Operacion incorrecta')

                    nombre_cliente, telefono_cliente, precio = datos_cliente()    

                    if operacion == 1:
                        writer.writerow({'PELUQUERIA_OPERACION': opciones[0].upper(), 'NOMBRE_CLIENTE': nombre_cliente.upper(),
                                         'TELEFONO_CLIENTE': telefono_cliente, 'PRECIO': precio, 'FECHA': datetime.date.today()})
                        break

                    if operacion == 2:
                        writer.writerow({'PELUQUERIA_OPERACION': opciones[1], 'NOMBRE_CLIENTE': nombre_cliente.upper(),
                                         'TELEFONO_CLIENTE': telefono_cliente, 'PRECIO': precio, 'FECHA': datetime.date.today()})
                        break

                    if operacion == 3:
                        tintura_numero_uno, cantidad_tintura_uno = tintura(
                            operacion)
                        oxigenada_volumen, cantidad_oxigenada, cantidad_polvo = adicionales()
                        hacer_reflejo = input(
                            'Desea utilizar reflejos? Ingrese SI o NO:\n').upper()
                        if hacer_reflejo != 'SI' or hacer_reflejo != 'NO':
                            print('Incorrecto! Debe ingresar SI o NO')
                            continue
                        if hacer_reflejo == 'NO':
                            writer.writerow({'PELUQUERIA_OPERACION': opciones[2], 'NOMBRE_CLIENTE': nombre_cliente.upper(),
                                             'TELEFONO_CLIENTE': telefono_cliente, 'TINTURA_1': tintura_numero_uno.upper(),
                                             'CANT_TINTURA_1': cantidad_tintura_uno, 'OXIGENADA_VOLUMEN': oxigenada_volumen.upper(),
                                             'CANT_OXIGENADA': cantidad_oxigenada, 'CANT_POLVO': cantidad_polvo,
                                             'PRECIO': precio, 'FECHA': datetime.date.today()})
                        if hacer_reflejo == 'SI':
                            reflejo_uno, cantidad_reflejo_uno, reflejo_dos, cantidad_reflejo_dos, reflejo_tres, cantidad_reflejo_tres = reflejo()
                            writer.writerow({'PELUQUERIA_OPERACION': opciones[2], 'NOMBRE_CLIENTE': nombre_cliente.upper(),
                                             'TELEFONO_CLIENTE': telefono_cliente, 'TINTURA_1': tintura_numero_uno.upper(),
                                             'CANT_TINTURA_1': cantidad_tintura_uno, 'OXIGENADA_VOLUMEN': oxigenada_volumen.upper(),
                                             'CANT_OXIGENADA': cantidad_oxigenada, 'CANT_POLVO': cantidad_polvo, 'REFLEJO_1': reflejo_uno.upper(),
                                             'CANT_REFLEJO_1': cantidad_reflejo_uno, 'REFLEJO_2': reflejo_dos.upper(), 'CANT_REFLEJO_2': cantidad_reflejo_dos,
                                             'REFLEJO_3': reflejo_tres.upper(), 'CANT_REFLEJO_3': cantidad_reflejo_tres,
                                             'PRECIO': precio, 'FECHA': datetime.date.today()})
                        break

                    if operacion == 4:
                        tintura_numero_uno, cantidad_tintura_uno, tintura_numero_dos, cantidad_tintura_dos, tintura_numero_tres, cantidad_tintura_tres = tintura(
                            operacion)
                        oxigenada_volumen, cantidad_oxigenada, cantidad_polvo = adicionales()
                        hacer_reflejo = input(
                            'Desea utilizar reflejos? Ingrese SI o NO:\n').upper()
                        if hacer_reflejo != 'SI' or hacer_reflejo != 'NO':
                            print('Incorrecto! Debe ingresar SI o NO')
                            continue
                        if hacer_reflejo == 'NO':
                            writer.writerow({'PELUQUERIA_OPERACION': opciones[3], 'NOMBRE_CLIENTE': nombre_cliente.upper(),
                                             'TELEFONO_CLIENTE': telefono_cliente, 'TINTURA_1': tintura_numero_uno.upper(),
                                             'CANT_TINTURA_1': cantidad_tintura_uno, 'TINTURA_2': tintura_numero_dos.upper(),
                                             'CANT_TINTURA_2': cantidad_tintura_dos, 'TINTURA_3': tintura_numero_tres.upper(),
                                             'CANT_TINTURA_3': cantidad_tintura_tres, 'OXIGENADA_VOLUMEN': oxigenada_volumen.upper(),
                                             'CANT_OXIGENADA': cantidad_oxigenada, 'CANT_POLVO': cantidad_polvo,
                                             'PRECIO': precio, 'FECHA': datetime.date.today()})
                        if hacer_reflejo == 'SI':
                            reflejo_uno, cantidad_reflejo_uno, reflejo_dos, cantidad_reflejo_dos, reflejo_tres, cantidad_reflejo_tres = reflejo()
                            writer.writerow({'PELUQUERIA_OPERACION': opciones[3], 'NOMBRE_CLIENTE': nombre_cliente.upper(),
                                             'TELEFONO_CLIENTE': telefono_cliente, 'TINTURA_1': tintura_numero_uno.upper(),
                                             'CANT_TINTURA_1': cantidad_tintura_uno, 'TINTURA_2': tintura_numero_dos.upper(),
                                             'CANT_TINTURA_2': cantidad_tintura_dos, 'TINTURA_3': tintura_numero_tres.upper(),
                                             'CANT_TINTURA_3': cantidad_tintura_tres, 'OXIGENADA_VOLUMEN': oxigenada_volumen.upper(),
                                             'CANT_OXIGENADA': cantidad_oxigenada, 'CANT_POLVO': cantidad_polvo, 'REFLEJO_1': reflejo_uno.upper(),
                                             'CANT_REFLEJO_1': cantidad_reflejo_uno, 'REFLEJO_2': reflejo_dos.upper(),
                                             'CANT_REFLEJO_2': cantidad_reflejo_dos, 'REFLEJO_3': reflejo_tres.upper(),
                                             'CANT_REFLEJO_3': cantidad_reflejo_tres, 'PRECIO': precio, 'FECHA': datetime.date.today()})
                        break

                    if operacion == 5:
                        reflejo_uno, cantidad_reflejo_uno, reflejo_dos, cantidad_reflejo_dos, reflejo_tres, cantidad_reflejo_tres = reflejo()
                        oxigenada_volumen, cantidad_oxigenada, cantidad_polvo = adicionales()
                        writer.writerow({'PELUQUERIA_OPERACION': opciones[4], 'NOMBRE_CLIENTE': nombre_cliente.upper(),
                                         'TELEFONO_CLIENTE': telefono_cliente, 'REFLEJO_1': reflejo_uno.upper(),
                                         'CANT_REFLEJO_1': cantidad_reflejo_uno, 'REFLEJO_2': reflejo_dos.upper(),
                                         'CANT_REFLEJO_2': cantidad_reflejo_dos, 'REFLEJO_3': reflejo_tres.upper(),
                                         'CANT_REFLEJO_3': cantidad_reflejo_tres, 'OXIGENADA_VOLUMEN': oxigenada_volumen.upper(),
                                         'CANT_OXIGENADA': cantidad_oxigenada, 'CANT_POLVO': cantidad_polvo,
                                         'PRECIO': precio, 'FECHA': datetime.date.today()})
                        break

                    if operacion == 6:
                        try:
                            cantidad_queratina = int(input(
                                'Ingrese cantidad de queratina a utilizar (EJ: 100):\n'))
                        except:
                            print('Incorrecto! Solo puede ingresar numeros')
                            continue
                        writer.writerow({'PELUQUERIA_OPERACION': opciones[5], 'NOMBRE_CLIENTE': nombre_cliente.upper(),
                                         'TELEFONO_CLIENTE': telefono_cliente, 'CANT_QUERATINA': cantidad_queratina,
                                         'PRECIO': precio, 'FECHA': datetime.date.today()})
                        break

                    if operacion == 7:
                        try:
                            cantidad_alisado = int(input(
                                'Ingrese cantidad de alisado a utilizar (EJ: 100):\n'))
                        except:
                            print('Incorrecto! Solo puede ingresar numeros')
                            continue
                        writer.writerow({'PELUQUERIA_OPERACION': opciones[6], 'NOMBRE_CLIENTE': nombre_cliente.upper(),
                                         'TELEFONO_CLIENTE': telefono_cliente, 'CANT_ALISADO': cantidad_alisado,
                                         'PRECIO': precio, 'FECHA': datetime.date.today()})
                        break

                    if operacion == 8:
                        try:
                            cantidad_plastificado = int(input(
                                'Ingrese cantidad de plastificado a utilizar (EJ: 100):\n'))
                        except:
                            print('Incorrecto! Solo puede ingresar numeros')
                            continue
                        writer.writerow({'PELUQUERIA_OPERACION': opciones[7], 'NOMBRE_CLIENTE': nombre_cliente.upper(),
                                         'TELEFONO_CLIENTE': telefono_cliente, 'CANT_PLASTIFICADO': cantidad_plastificado,
                                         'PRECIO': precio, 'FECHA': datetime.date.today()})
                        break

                    if operacion == 9:
                        try:
                            cantidad_biomolecular = int(input(
                                'Ingrese cantidad de biomolecular a utilizar (EJ: 100):\n'))
                        except:
                            print('Incorrecto! Solo puede ingresar numeros')
                            continue
                        writer.writerow({'PELUQUERIA_OPERACION': opciones[8], 'NOMBRE_CLIENTE': nombre_cliente.upper(),
                                         'TELEFONO_CLIENTE': telefono_cliente, 'CANT_BIOMOLECULAR': cantidad_biomolecular,
                                         'PRECIO': precio, 'FECHA': datetime.date.today()})
                        break

                    if operacion == 10:
                        try:
                            cantidad_argan = int(input(
                                'Ingrese cantidad de argan a utilizar (EJ: 100):\n'))
                        except:
                            print('Incorrecto! Solo puede ingresar numeros')
                            continue
                        writer.writerow({'PELUQUERIA_OPERACION': opciones[9], 'NOMBRE_CLIENTE': nombre_cliente.upper(),
                                         'TELEFONO_CLIENTE': telefono_cliente, 'CANT_ARGAN': cantidad_argan,
                                         'PRECIO': precio, 'FECHA': datetime.date.today()})
                        break

                    if operacion == 11:
                        try:
                            cantidad_espejo = int(input(
                                'Ingrese cantidad de espejo a utilizar (EJ: 100):\n'))
                        except:
                            print('Incorrecto! Solo puede ingresar numeros')
                            continue
                        writer.writerow({'PELUQUERIA_OPERACION': opciones[10], 'NOMBRE_CLIENTE': nombre_cliente.upper(),
                                         'TELEFONO_CLIENTE': telefono_cliente, 'CANT_ESPEJO': cantidad_espejo,
                                         'PRECIO': precio, 'FECHA': datetime.date.today()})
                        break

                    if operacion == 12:
                        try:
                            cantidad_biotina = int(input(
                                'Ingrese cantidad de biotina a utilizar (EJ: 100):\n'))
                        except:
                            print('Incorrecto! Solo puede ingresar numeros')
                            continue
                        writer.writerow({'PELUQUERIA_OPERACION': opciones[11], 'NOMBRE_CLIENTE': nombre_cliente.upper(),
                                         'TELEFONO_CLIENTE': telefono_cliente, 'CANT_BIOTINA': cantidad_biotina,
                                         'PRECIO': precio, 'FECHA': datetime.date.today()})
                        break

                    if operacion == 13:
                        try:
                            cantidad_botox = int(input(
                                'Ingrese cantidad de botox a utilizar (EJ: 100):\n'))
                        except:
                            print('Incorrecto! Solo puede ingresar numeros')
                            continue
                        writer.writerow({'PELUQUERIA_OPERACION': opciones[12], 'NOMBRE_CLIENTE': nombre_cliente.upper(),
                                         'TELEFONO_CLIENTE': telefono_cliente, 'CANT_BOTOX': cantidad_botox,
                                         'PRECIO': precio, 'FECHA': datetime.date.today()})
                        break

                    if operacion == 14:
                        try:
                            cantidad_lifting = int(input(
                                'Ingrese cantidad de lifting a utilizar (EJ: 100):\n'))
                        except:
                            print('Incorrecto! Solo puede ingresar numeros')
                            continue
                        writer.writerow({'PELUQUERIA_OPERACION': opciones[13], 'NOMBRE_CLIENTE': nombre_cliente.upper(),
                                         'TELEFONO_CLIENTE': telefono_cliente, 'CANT_LIFTING': cantidad_lifting,
                                         'PRECIO': precio, 'FECHA': datetime.date.today()})
                        break

            if opcion == 2:
                while True:
                    producto_stock = input(
                        'Ingrese producto a stockear (EJ: TINTURA 9.1, ) o FIN para terminar:\n')
                    if producto_stock == 'FIN':
                        break
                    cantidad_stock = int(
                        input('Ingrese cantidad (EJ: 100):\n'))

                    try:
                        precio_stock = int(
                            input('Ingrese precio producto (EJ: 500):\n'))
                    except:
                        print('Solo puede ingresar numeros')

                    writer.writerow({'FECHA': datetime.date.today(), 'PRODUCTO_STOCK': producto_stock.upper(),
                                     'CANTIDAD_STOCK': cantidad_stock, 'PRECIO_STOCK': precio_stock})


def datos_cliente():
    nombre_cliente = input(
        'Ingrese nombre y apellido del cliente (EJ: JUAN PEREZ):\n')
    try:    
        telefono_cliente = int(
            input('Ingrese telefono del cliente (EJ: 223456789):\n'))
    except:
        print('Incorrecto! Solo puede ingresar numeros')
    precio = int(input('Ingrese importe:\n'))

    return nombre_cliente, telefono_cliente, precio


def reflejo():
    reflejo_uno = input(
        'Ingrese el numero del primer reflejo (EJ: REFLEJO 3):\n')
    try:
        cantidad_reflejo_uno = int(input(
            'Ingrese cantidad de reflejo a utilizar (EJ: 20):\n'))
    except:
        print('Incorrecto! Solo puede ingresar numeros')

    reflejo_dos = input(
        'Ingrese el numero del segundo reflejo (EJ: REFLEJO 3):\n')
    try:
        cantidad_reflejo_dos = int(input(
            'Ingrese cantidad de reflejo a utilizar (EJ: 20):\n'))
    except:
        print('Incorrecto! Solo puede ingresar numeros')

    reflejo_tres = input(
        'Ingrese el numero del tercer reflejo (EJ: REFLEJO 3):\n')
    try:
        cantidad_reflejo_tres = int(input(
            'Ingrese cantidad de reflejo a utilizar (EJ: 20):\n'))
    except:
        print('Incorrecto! Solo puede ingresar numeros')

    return reflejo_uno, cantidad_reflejo_uno, reflejo_dos, cantidad_reflejo_dos, reflejo_tres, cantidad_reflejo_tres


def adicionales():
    oxigenada_volumen = input(
        'Ingrese oxigenada volumen (EJ: OXIGENADA 30):\n')
    try:
        cantidad_oxigenada = int(input(
            'Ingrese cantidad de agua oxigenada a utilizar (EJ: 150):\n'))
    except:
        print('Incorrecto! Solo puede ingresar numeros')
    try:
        cantidad_polvo = int(input(
            'Ingrese cantidad de polvo decolorante a utilizar (EJ: 100):\n'))
    except:
        print('Incorrecto! Solo puede ingresar numeros')

    return oxigenada_volumen, cantidad_oxigenada, cantidad_polvo


def tintura(operacion):
    if operacion == 3:
        tintura_numero_uno = input(
            'Ingrese numero de tintura (EJ: TINTURA 7 o TINTURA 9.2):\n')
        try:
            cantidad_tintura_uno = int(input(
                'Ingrese cantidad de tintura a utilizar (EJ: 45):\n'))
        except:
            print('Incorrecto! Solo puede ingresar numeros')

        return tintura_numero_uno, cantidad_tintura_uno

    else:
        tintura_numero_uno = input(
                'Ingrese numero de tintura (EJ: TINTURA 7 o TINTURA 9.2):\n')
        try:
            cantidad_tintura_uno = int(input(
                'Ingrese cantidad de tintura a utilizar (EJ: 45):\n'))
        except:
            print('Incorrecto! Solo puede ingresar numeros')

        tintura_numero_dos = input(
            'Ingrese numero de segunda tintura a utilizar (EJ: TINTURA 7 o TINTURA 9.2):\n')
        try:
            cantidad_tintura_dos = int(input(
                'Ingrese cantidad de tintura a utilizar (EJ: 45):\n'))
        except:
            print('Incorrecto! Solo puede ingresar numeros')

        tintura_numero_tres = input(
            'Ingrese numero de tercera tintura a utilizar (EJ: TINTURA 7 o TINTURA 9.2):\n')
        try:
            cantidad_tintura_tres = int(input(
                'Ingrese cantidad de tintura a utilizar (EJ: 45):\n'))
        except:
            print('Incorrecto! Solo puede ingresar numeros')

        return tintura_numero_uno, cantidad_tintura_uno, tintura_numero_dos, cantidad_tintura_dos, tintura_numero_tres, cantidad_tintura_tres


if __name__ == '__main__':
    la_barbieria()
