import database
import os

# Creacion de cuentas
def crear_tarjeta(Cuenta):
    try:
        print("Datos Solicitados para creacion de la tarjeta!\n")
        saldo = 0
        estado = 1
        retiro = 0

        while True:
            print("\tIngrese la informacion de la Tarjeta")
            while True:
                numero_tarjeta = input("Ingrese NumeroTarjeta: ")

                # Verificar si la entrada es un número
                if numero_tarjeta.isdigit():
                    numero = int(numero_tarjeta)
                    break
                else:
                    print("Por favor, ingresa un número válido.")
            
            Tarjeta = input("Ingresa el tipo de Tarjeta debito = 1 , Credito = 2: ")

            match Tarjeta:
                case '1':
                    tipo_tarjeta = "Debito"
                    break
                case '2':
                    tipo_tarjeta = "Credito"
                    saldo = 1000000
                    break
                case _:
                    print("Opcion Invalida, Intenta nuevamente")

        with database.conn:
            database.cursor.execute('''
                INSERT INTO Tarjetas ( 
                    cuenta, 
                    numero_tarjeta,
                    tipo_tarjeta,
                    saldo,
                    retiro,
                    estado
                ) 
                VALUES (?, ?, ?, ?, ?, ?)''',
                (Cuenta, numero_tarjeta, tipo_tarjeta, saldo, retiro, estado))

        print("Tarjeta creada exitosamente.")
        os.system("cls")
        return True

    except Exception as e:
        print(f"Error al crear la tarjeta: {e}")
        return False
