import csv
import datetime


def la_barbieria_consulta():

    
    with open('barbieria.csv', 'r') as fi:
        reader = list(csv.DictReader(fi))
        len_reader = len(reader)
        
        
        while True:
            total_dia = []
            total_dias = []
            tintura_resta = []
            
            
            print(
                    '1- Total dia\n'
                    '2- Total de todos los dias\n'
                    '3- Historial cliente\n'
                    '4- Consultar stock\n'
                    '5- Salir programa\n'
                )


            try:
                opcion = int(input('Ingrese opcion para continuar:\n'))
            except:
                print('Opcion incorrecta\n')
                continue


            if opcion > 6:
                print('Opcion incorrecta\n')

            
            if opcion == 5:
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
                for i in range(len_reader):
                    row = reader[i]
                    nombre_cliente = row.get('NOMBRE_CLIENTE')
                    if cliente_nombre == nombre_cliente:
                        print(row)


            if opcion == 4:
                opcion = input('Ingrese producto para saber stock:\n')
                for i in range(len_reader):
                    pass






if __name__ == '__main__':
    la_barbieria_consulta()
