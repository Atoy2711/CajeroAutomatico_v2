import database


def crear_cuenta(tipo_cuenta, usuario_id, saldo_inicial, numero_tarjeta):
    # Inserta los datos de la nueva cuenta en la base de datos
    database.cursor.execute('INSERT INTO cuentas (usuario_id, tipo_cuenta, saldo, numero_tarjeta, contrasena) VALUES (?, ?, ?, ?, ?)',
                            (usuario_id, tipo_cuenta, saldo_inicial, numero_tarjeta))
    database.conn.commit()

def actualizar_cuenta(cuenta_id, nuevo_saldo, nueva_contrasena):
    # Actualiza el saldo y contraseña de la cuenta en la base de datos
    database.cursor.execute('UPDATE cuentas SET saldo = ?, contrasena = ? WHERE id = ?', 
                            (nuevo_saldo, nueva_contrasena, cuenta_id))
    database.conn.commit()

def eliminar_cuenta(cuenta_id):
    # Elimina la cuenta de la base de datos
    database.cursor.execute('DELETE FROM cuentas WHERE id = ?', 
                           (cuenta_id,))
    database.conn.commit()

def buscar_cuenta(numero_tarjeta):
    # Busca la cuenta por número de tarjeta en la base de datos
    database.cursor.execute('SELECT * FROM cuentas WHERE numero_tarjeta = ?', 
                           (numero_tarjeta,))
    cuenta = database.cursor.fetchone()
    return cuenta  # Devuelve la cuenta encontrada o None si no existe
