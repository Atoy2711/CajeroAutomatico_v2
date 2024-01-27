import database

#Creacion de cuentas
def crear_cuenta(Usuario):
    
    try:
        print("Datos Solicitados para creacion de la cuenta!\n")
        saldo_ahorro = 0
        saldo_corriente = 0
        
            
        while True:
            print("\tIngrese la informacion de la cuenta")
            while True:
                numero_cuenta = input("Ingrese NumeroCuenta: ")

                # Verificar si la entrada es un número
                if numero_cuenta.isdigit():
                    numero = int(numero_cuenta)
                    break
                else:
                    print("Por favor, ingresa un número válido.")
                    
            
            cuenta = input("Ingrese tipoCuenta ahorro = 1 , corriente = 2: ")
            match cuenta:
                case '1':
                    tipo_cuenta = 'ahorro'
                    break         
                case '2':
                    tipo_cuenta = 'corriente'
                    break            
                case _:
                    print("Opcion Invalida, Intenta nuevamente")
                            
        with database.conn:
            database.cursor.execute('''
                INSERT INTO Cuentas ( 
                    Usuario, 
                    TipoCuenta, 
                    NumeroCuenta,
                    saldo_ahorro,
                    saldo_corriente
                ) 
                VALUES (?, ?, ?, ?, ?)''', 
                (Usuario, tipo_cuenta, numero_cuenta, saldo_ahorro, saldo_corriente))
            
        print("Cuenta creada exitosamente.")
        
        #consulta la cuenta creada
        with database.conn:
            database.cursor.execute('SELECT id FROM Cuentas WHERE Usuario=?', (Usuario,))
            result = database.cursor.fetchone()
            if result:
                id_cuenta = result[0]
                print(f"ID de la cuenta creada: {id_cuenta}")
                return id_cuenta
            else:
                print("No se encontró ninguna cuenta.")
                return None
                                                    
    except Exception as e:
        print(f"Error al crear la cuenta: {e}")
        return False
    