import database
import os
def verSaldo(user,tipo_cuenta):
    # 2. Obtener el saldo actual de la cuenta
        if tipo_cuenta == "ahorro":
            ahorros = database.cursor.execute('SELECT saldo_ahorro FROM Cuentas where Usuario=?', (user,))
            ahorros = database.cursor.fetchone()
            os.system("cls")
            print(f"Su saldo en cuenta de ahorros es {ahorros[0]}")
        elif tipo_cuenta == "corriente":
            corriente = database.cursor.execute('SELECT saldo_corriente FROM Cuentas WHERE Usuario=?', (user,))
            corriente = database.cursor.fetchone()
            os.system("cls")
            print(f"Su saldo en cuenta de corriente es {corriente[0]}")
        else:
            print("Los datos ingresados no son validos.")
        #saldo = database.cursor.fetchone()[0]
        return 