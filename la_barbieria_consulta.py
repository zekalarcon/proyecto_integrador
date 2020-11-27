import csv
import datetime


def la_barbieria_consulta():

    
    with open('barbieria.csv', 'r') as fi:
        reader = list(csv.DictReader(fi))
        len_reader = len(reader)
        
        
        while True:
            total_dia = []
            total_dias = []
            stock_suma = []
            
            
            print(
                    '1- Total dia\n'
                    '2- Total de todos los dias\n'
                    '3- Historial cliente\n'
                    '4- Stock tinturas\n'
                    '5- Stock reflejos\n'
                    '6- Stock agua oxigenada\n'
                    '7- Stock polvo decolorante\n'
                    '8- Stock queratina\n'
                    '9- Stock alisado\n'
                    '10- Stock plastificado\n'
                    '11- Stock biomolecular\n'
                    '12- Stock argan\n'
                    '13- Stock espejo\n'
                    '14- Stock biotina\n'
                    '15- Stock botox\n'
                    '16- Stock lifting\n'
                    '17- Salir programa\n'
                )


            try:
                opcion = int(input('Ingrese opcion para continuar:\n'))
            except:
                print('Opcion incorrecta\n')
                continue


            if opcion > 17:
                print('Opcion incorrecta\n')

            
            if opcion == 17:
                break


            if opcion == 1:
                for i in range(len_reader):
                    row = reader[i]
                    fecha = row.get('FECHA')
                    precio = row.get('PRECIO')
                    
                    if str(datetime.date.today()) == fecha:
                        total_dia.append(int(precio))
                
                
                print(f'El total del dia es: ${sum(total_dia)}')
                
            
            if opcion == 2:
                for i in range(len_reader):
                    row = reader[i]
                    precio = row.get('PRECIO')
                    total_dias.append(int(precio))    
                    
                
                print(f'El total de todos los dia es: ${sum(total_dias)}')


            if opcion == 3:

                cliente_nombre = input('Ingrese nombre y apellido cliente (EJ: JUAN PEREZ):\n').upper()
                datos = []
                for i in range(len_reader):
                    row = reader[i]
                    nombre_cliente = row.get('NOMBRE_CLIENTE')
                    
                    if cliente_nombre == nombre_cliente:
                        datos.append(row)
                        for k, v in row.items():
                            if v != '':
                                print(k,':', v,)
                               
                        
            if opcion == 4:

                opcion =input('Ingrese tintura numero (EJ: TINTURA 2.3):\n')
                suma_producto_stock = stock_cantidad(opcion)
                
                
                for i in range(len_reader):
                    row = reader[i]
                    tintura_uno = row.get('TINTURA_1')
                    cantidad_tintura_uno = row.get('CANT_TINTURA_1')
                    tintura_dos = row.get('TINTURA_2')
                    cantidad_tintura_dos = row.get('CANT_TINTURA_2')
                    tintura_tres = row.get('TINTURA_3')
                    cantidad_tintura_tres = row.get('CANT_TINTURA_3')
                    

                    if opcion == tintura_uno or opcion == tintura_dos or opcion == tintura_tres:
                        stock_suma.append(cantidad_tintura_uno)
                        stock_suma.append(cantidad_tintura_dos)
                        stock_suma.append(cantidad_tintura_tres)
                    tintura_suma = remover(stock_suma)
                        
                
                print(f'El stock de {opcion} es: {suma_producto_stock - tintura_suma} grs.')


            if opcion == 5:

                opcion = input('Ingrese reflejo NUMERO (EJ: REFLEJO 1):\n')
                suma_producto_stock = stock_cantidad(opcion)

                
                for i in range(len_reader):
                    reflejo_uno = row.get('REFLEJO_1')
                    cantidad_reflejo_uno = row.get('CANT_REFLEJO_1')
                    reflejo_dos = row.get('REFLEJO_2')
                    cantidad_reflejo_dos = row.get('CANT_REFLEJO_2')
                    reflejo_tres = row.get('REFLEJO_3')
                    cantidad_reflejo_tres = row.get('CANT_REFLEJO_3')
                    
                    
                    if opcion == reflejo_uno or opcion == reflejo_dos or opcion == reflejo_tres:
                        stock_suma.append(cantidad_reflejo_uno)
                        stock_suma.append(cantidad_reflejo_dos)
                        stock_suma.append(cantidad_reflejo_tres)
                    reflejo_suma = remover(stock_suma) 

                
                print(f'El stock del {opcion} es: {suma_producto_stock - reflejo_suma} grs.')


            if opcion == 6:

                opcion = input('Ingrese oxigenada volumen (EJ: OXIGENADA 30):\n')
                suma_producto_stock = stock_cantidad(opcion)

                
                for i in range(len_reader):
                    row = reader[i]    
                    oxigenada_volumen = row.get('OXIGENADA_VOLUMEN')
                    cantidad_oxigenada = row.get('CANT_OXIGENADA')
                    
                    
                    if opcion == oxigenada_volumen:
                        stock_suma.append(cantidad_oxigenada)
                    oxigenada_suma = remover(stock_suma)

                
                print(f'El stock de {opcion} es: {suma_producto_stock - oxigenada_suma} grs.')


            if opcion == 7:

                opcion = 'POLVO'
                suma_producto_stock = stock_cantidad(opcion)
                
                
                for i in range(len_reader):
                    row = reader[i]
                    cantidad_polvo = row.get('CANT_POLVO')
                    stock_suma.append(cantidad_polvo)
                
                
                polvo_suma = remover(stock_suma)
                print(f'La cantidad de polvo decolorante en stock es: {suma_producto_stock - polvo_suma} grs.')
                

            if opcion == 8:
                opcion = 'QUERATINA'
                suma_producto_stock = stock_cantidad(opcion)
                
                
                for i in range(len_reader):
                    row = reader[i]
                    cantidad_queratina = row.get('CANT_QUERATINA')
                    stock_suma.append(cantidad_queratina)
                
                
                queratina_suma = remover(stock_suma)
                print(f'La cantidad de queratina en stock es: {suma_producto_stock - queratina_suma} grs.')


            if opcion == 9:
                opcion = 'ALISADO'
                suma_producto_stock = stock_cantidad(opcion)
                
                
                for i in range(len_reader):
                    row = reader[i]
                    cantidad_alisado = row.get('CANT_ALISADO')
                    stock_suma.append(cantidad_alisado)
                
                
                alisado_suma = remover(stock_suma)
                print(f'La cantidad de alisado en stock es: {suma_producto_stock - alisado_suma} grs.')


            if opcion == 10:
                opcion = 'PLASTIFICADO'
                suma_producto_stock = stock_cantidad(opcion)
                
                
                for i in range(len_reader):
                    row = reader[i]
                    cantidad_plastificado = row.get('CANT_PLASTIFICADO')
                    stock_suma.append(cantidad_plastificado)
                
                
                plastificado_suma = remover(stock_suma)
                print(f'La cantidad de plastificado en stock es: {suma_producto_stock - plastificado_suma} grs.')


            if opcion == 11:
                opcion = 'BIOMOLECULAR'
                suma_producto_stock = stock_cantidad(opcion)
                
                
                for i in range(len_reader):
                    row = reader[i]
                    cantidad_biomolecular = row.get('CANT_BIOMOLECULAR')
                    stock_suma.append(cantidad_biomolecular)
                
                
                biomolecular_suma = remover(stock_suma)
                print(f'La cantidad de biomolecular en stock es: {suma_producto_stock - biomolecular_suma} grs.') 


            if opcion == 12:
                opcion = 'ARGAN'
                suma_producto_stock = stock_cantidad(opcion)
                
                
                for i in range(len_reader):
                    row = reader[i]
                    cantidad_argan = row.get('CANT_ARGAN')
                    stock_suma.append(cantidad_argan)
                
                
                argan_suma = remover(stock_suma)
                print(f'La cantidad de argan en stock es: {suma_producto_stock - argan_suma} grs.')


            if opcion == 13:
                opcion = 'ESPEJO'
                suma_producto_stock = stock_cantidad(opcion)
                
                
                for i in range(len_reader):
                    row = reader[i]
                    cantidad_espejo = row.get('CANT_ESPEJO')
                    stock_suma.append(cantidad_espejo)
                
                
                espejo_suma = remover(stock_suma)
                print(f'La cantidad de espejo en stock es: {suma_producto_stock - espejo_suma} grs.')


            if opcion == 14:
                opcion = 'BIOTINA'
                suma_producto_stock = stock_cantidad(opcion)
                
                
                for i in range(len_reader):
                    row = reader[i]
                    cantidad_biotina = row.get('CANT_BIOTINA')
                    stock_suma.append(cantidad_biotina)
                
                
                biotina_suma = remover(stock_suma)
                print(f'La cantidad de biotina en stock es: {suma_producto_stock - biotina_suma} grs.')


            if opcion == 15:
                opcion = 'BOTOX'
                suma_producto_stock = stock_cantidad(opcion)
                
                
                for i in range(len_reader):
                    row = reader[i]
                    cantidad_botox = row.get('CANT_BOTOX')
                    stock_suma.append(cantidad_botox)
                
                
                botox_suma = remover(stock_suma)
                print(f'La cantidad de botox en stock es: {suma_producto_stock - botox_suma} grs.')


            if opcion == 16:
                opcion = 'LIFTING'
                suma_producto_stock = stock_cantidad(opcion)
                
                
                for i in range(len_reader):
                    row = reader[i]
                    cantidad_lifting = row.get('CANT_LIFTING')
                    stock_suma.append(cantidad_lifting)
                
                
                lifting_suma = remover(stock_suma)
                print(f'La cantidad de lifting en stock es: {suma_producto_stock - lifting_suma} grs.')                       




def stock_cantidad(opcion):
    with open('barbieria.csv', 'r') as fi:
        reader = list(csv.DictReader(fi))
        len_reader = len(reader)
        suma_stock = []

        
        for i in range(len_reader):
            row = reader[i]
            producto_stock = row.get('PRODUCTO_STOCK')
            cantidad_stock = row.get('CANTIDAD_STOCK')
            if opcion == producto_stock:
                suma_stock.append(cantidad_stock)
                if '' in suma_stock:
                    suma_stock.remove('')
        
        return sum(list(map(int, suma_stock)))


def remover(stock_suma):
    while '' in stock_suma:
        stock_suma.remove('')
    
    return sum(list(map(int, stock_suma)))   






if __name__ == '__main__':
    la_barbieria_consulta()
