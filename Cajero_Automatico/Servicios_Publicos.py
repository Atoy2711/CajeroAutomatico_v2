from ast import While
from unittest import result
import fechaHora
import database
import os

def realizar_pago_servicios(usuario,usuario_id,identificacion,tarjeta_id,cuenta_id):
    
    #Ingresa numero del recibo
    numero_recibo = int(input("Ingrese el numero del recibo: "))
    
    #Trae la hora actual
    fecha = fechaHora.fechaActual()
    
    #estado del recibo pendiente = 1, pago = 2
    estado = 0
    
    #Extrae el recibo ingresado
    database.cursor.execute('SELECT NumeroRecibo, Valor, Estado FROM ServiciosPublicos WHERE NumeroRecibo=?', (numero_recibo,))
    result = database.cursor.fetchone()
    
    if result is None:
        print("Numero de Recibo no encontrado")
    elif len(result) == 3:
        os.system("cls")
        stored_numero, stored_valor, stored_estado = result
    
        if stored_estado == '2':
            print("\t\t*********El recibo ya se pagó***********")
        else:
            print(f"""            ***Recibo encontrado***
                Numero: {stored_numero} 
                Valor a pagar: {stored_valor} """)
            #ingresa el medio de pago
            while True:
                opcion = input("""
                Ingresa el medio de pago a utilizar
    1. Cuenta ahorros
    2. Cuenta corriente
    3. Efectivo
    4. Salir

    Ingrese el numero correspondiente: """)
                
                match opcion:
                    case '1':
                        tipo_cuenta = "ahorro"
                        database.cursor.execute('SELECT saldo_ahorro FROM Cuentas WHERE Usuario=?', (usuario_id,))   
                        Valor = database.cursor.fetchone()[0]
                        
                        if Valor >= stored_valor:
                            # 2. Obtener el saldo actual de la cuenta
                            devuelta = Valor - stored_valor
                            #defino el estado en dos
                            estado = 2
                            print(f"El valor del recibo fue {stored_valor}, se devuelve el valor de ${devuelta}")
                            database.cursor.execute('UPDATE ServiciosPublicos SET Nombre=?, FechaPago=?, Estado=? WHERE NumeroRecibo=?', (usuario, fecha, estado,stored_numero))
                            database.cursor.execute('UPDATE Cuentas SET saldo_ahorro=? WHERE Usuario=?', (stored_valor,usuario_id ))
                            # Registrar la transacción en la base de datos
                            database.cursor.execute('INSERT INTO Transaccion (Usuario, Identificacion, FechaTransaccion,Cuenta, Valor, Tarjeta, Detalle, TipoTransaccion) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', 
                                                    (usuario,identificacion,fecha,tarjeta_id,stored_valor,cuenta_id, f"Pagó con {tipo_cuenta}", "Recibo"))
                            database.conn.commit()
                            break
                        else:
                            print(f"El valor ingresado que tiene en la cuenta es menor a {stored_valor}.")
                    case '2':
                        tipo_cuenta = "corriente"
                        database.cursor.execute('SELECT saldo_corriente FROM Cuentas WHERE Usuario=?', (usuario_id,))
                        Valor = database.cursor.fetchone()[0]
                        
                        if Valor >= stored_valor:
                            # 2. Obtener el saldo actual de la cuenta
                            devuelta = Valor - stored_valor
                            #defino el estado en dos
                            estado = 2
                            print(f"El valor del recibo fue {stored_valor}, se devuelve el valor de ${devuelta}")
                            database.cursor.execute('UPDATE ServiciosPublicos SET Nombre=?, FechaPago=?, Estado=? WHERE NumeroRecibo=?', (usuario, fecha, estado,stored_numero))
                            database.cursor.execute('UPDATE Cuentas SET saldo_corriente=? WHERE Usuario=?', (stored_valor,usuario_id ))
                            # Registrar la transacción en la base de datos
                            database.cursor.execute('INSERT INTO Transaccion (Usuario, Identificacion, FechaTransaccion,Cuenta, Valor, Tarjeta, Detalle, TipoTransaccion) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', 
                                                    (usuario,identificacion,fecha,tarjeta_id,stored_valor,cuenta_id, f"Pagó con {tipo_cuenta}", "Recibo"))
                            database.conn.commit()
                            break
                        else:
                            print(f"El valor ingresado que tiene en la cuenta es menor a {stored_valor}.")
                    case '3':
                        tipo_cuenta = "efectivo"
                        Valor = int(input("Ingrese el valor a pagar: "))
                        # Verificar si el Valor es mayor o igual al almacenado
                        if Valor >= stored_valor:
                            # 2. Obtener el saldo actual de la cuenta
                            devuelta = Valor - stored_valor
                            #defino el estado en dos
                            estado = 2
                            print(f"El valor del recibo fue {stored_valor}, se devuelve el valor de ${devuelta}")
                            database.cursor.execute('UPDATE ServiciosPublicos SET Nombre=?, FechaPago=?, Estado=? WHERE NumeroRecibo=?', (usuario, fecha, estado,stored_numero))
                            
                            # Registrar la transacción en la base de datos
                            database.cursor.execute('INSERT INTO Transaccion (Usuario, Identificacion, FechaTransaccion,Cuenta, Valor, Tarjeta, Detalle, TipoTransaccion) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', 
                                                    (usuario,identificacion,fecha,'NULL',stored_valor,'NULL', f"Pagó con {tipo_cuenta}", "Recibo"))
                            database.conn.commit()
                            break
                        else:
                            print(f"El valor ingresado en efectivo es menor a {stored_valor}.")
                    
                    case '4':
                        print("operacion Cancelada. ¡Hasta luego!")
                        break
                    case _:
                        os.system("cls")
                        print("Opcion Incorrecta. Intente nuevamente.")

        
    else:
        print("Error en la consulta SQL. No se devolvieron dos columnas.")
        
