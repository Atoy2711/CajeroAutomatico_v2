import database
import fechaHora

def realizar_consignacion(usuario_id,identificacion,cuenta_id,tarjeta_id, tipo_cuenta):
    
    #Trae la hora actual
    fecha = fechaHora.fechaActual()
    #ingresa el monto a retirar
    monto = int(input("Ingrese el monto a retirar 'debe ser multiplo de $10.000': "))
    
    # 1. Verificar que el monto sea un múltiplo de 10,000
    if monto % 10000 != 0:
        print("El cajero solo entrega múltiplos de 10,000.")
        return None
    
    # 2. Obtener el saldo actual de la cuenta
    if tipo_cuenta == "ahorro":
        database.cursor.execute('SELECT saldo_ahorro FROM Cuentas WHERE Usuario=?', (usuario_id,))
    else:
        database.cursor.execute('SELECT saldo_corriente FROM Cuentas WHERE Usuario=?', (usuario_id,))
    saldo = database.cursor.fetchone()[0]
    #print(saldo)
    # 3. Verificar que haya suficiente saldo en la cuenta
    if monto > 2000000:
        print("Consigancion mayor a 2 millones")
        return True
    
    # 4. Realizar el retiro y actualizar el saldo
    nuevo_saldo = saldo + monto
    
    if tipo_cuenta == "ahorro":
        
        database.cursor.execute('UPDATE Cuentas SET saldo_ahorro=? WHERE Usuario=?', (nuevo_saldo, usuario_id))
        #database.conn.commit()
    else:
        
        database.cursor.execute('UPDATE Cuentas SET saldo_corriente=? WHERE Usuario=?', (nuevo_saldo, usuario_id))
        #database.conn.commit()
    
    # Registrar la transacción en la base de datos
    database.cursor.execute('INSERT INTO Transaccion (Usuario, Identificacion, FechaTransaccion,Cuenta, Valor, Tarjeta, Detalle, TipoTransaccion) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', 
                            (usuario_id,identificacion,fecha,cuenta_id,monto,tarjeta_id, f"retiro cuenta de {tipo_cuenta}", "Retiro"))
    database.conn.commit()
    
    return monto
