import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('cajero.db')
cursor = conn.cursor()

def ingresar_cantidad_billetes():
    try:
        cantidad_billetes = {}

        # Solicita al usuario la cantidad de cada denominación de billetes
        for denominacion in ['Billete de $100000',
                            'Billete de $50000',
                            'Billete de $20000',
                            'Billete de $10000',
                            'Billete de $5000',
                            'Billete de $2000',
                            'Billete de $1000',
                            'Moneda de $1000',
                            'Moneda de $500',
                            'Moneda de $200',
                            'Moneda de $100',
                            'Moneda de $50']:
            cantidad_actual = cursor.execute('SELECT Cantidad FROM Dinero WHERE Nombre = ?', (denominacion,)).fetchone()
            print(cantidad_actual)
            while True:
                try:
                    cantidad = int(input(f"Ingrese la cantidad de billetes de {denominacion}: "))
                    
                    nueva_cantidad = cantidad_actual[0] + cantidad
                    
                    if nueva_cantidad > 200:
                        print(f"La cantidad total de billetes de {denominacion} en el cajero es {cantidad_actual[0]}.")
                        print("Por favor, ingrese nuevamente una cantidad válida.")
                        continue
                    
                    break
                except ValueError:
                    print("Por favor, ingrese un número entero válido.")

            cantidad_billetes[denominacion] = nueva_cantidad

            cursor.execute('UPDATE Dinero SET Cantidad = ? WHERE Nombre = ?', (nueva_cantidad, denominacion))

        conn.commit()

        print("Cantidad de billetes ingresada con éxito.")

    except sqlite3.Error as e:
        print(f"Error al actualizar la cantidad de billetes en la base de datos: {type(e).__name__}: {e}")

    finally:
        # Asegúrate de cerrar la conexión incluso si ocurre una excepción
        if 'database' in locals() and conn:
            conn.close()




