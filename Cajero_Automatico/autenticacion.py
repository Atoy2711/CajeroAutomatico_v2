import hashlib
import database
import menu
import getpass
import os

#Variable Global para conteo de rrores de inicio de sesion
#cont = 3
# Encriptar la contraseña antes de almacenarla
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

#autenticacion de contraseña
import getpass
import os
import menu  # Asegúrate de tener un módulo llamado 'menu' con la función 'menu_principal'

def autenticar_usuario():
    cont = 3
    
    while cont > 0:
        
        username = input("Ingrese su nombre de usuario: ")
        password = getpass.getpass("Ingrese su contraseña: ")
        
        # Realiza la consulta SQL para obtener el usuario y la contraseña de la base de datos
        database.cursor.execute(''' SELECT 
                                        Usuarios.id, 
                                        Usuarios.Nombre, 
                                        Usuarios.Usuario, 
                                        Usuarios.Identificacion, 
                                        Usuarios.Password,
                                        Cuentas.Usuario AS CuentasUsuario,
                                        Tarjetas.id AS TarjetasId
                                    FROM 
                                        Usuarios
                                    LEFT JOIN 
                                        Cuentas ON Usuarios.id = Cuentas.Usuario
                                    LEFT JOIN 
                                        Tarjetas ON Cuentas.id = Tarjetas.cuenta WHERE Usuarios.Usuario=?''', (username, ))
        result = database.cursor.fetchone()
        
        if result is None:
            print("Usuario invalido")
        elif len(result) == 7:
                (user_id,stored_name, stored_username, stored_identificacion, stored_password,cuenta_id,tarjeta_id) = result
                #compara la dos contraseñas encriptadas
                if stored_password == hash_password(password):
                    print(f"Autenticacion exitosa.")
                    return stored_username,stored_name,stored_identificacion,user_id,cuenta_id,tarjeta_id
                else:
                    cont -= 1
                    os.system("cls")
                    print(f"Contraseña Incorrecta. Intentos restantes: {cont}")
        else:
            print("Error en la consulta SQL. No se devolvieron tres columnas.")

    print("Intentos agotados, cuenta bloqueada.")
    os.system("pause")
    os.system("cls")
    menu.menu_principal()
    return ('', '', '', '', '', '')

#def validar_tipo_úsuario():
#    database.cursor.execute(f'SELECT Usuario, TipoUsuario FROM usuario WHERE {}')