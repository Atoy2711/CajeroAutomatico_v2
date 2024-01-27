import autenticacion
import database
import getpass

#Creacion de usuarios
def crear_usuario():
    try:
        print("Datos Solicitados para creacion de usuario!\n")
        nombre = input("Ingresa nombre completo: ")
        username = input("Ingrese un nombre de usuario: ")
        password = getpass.getpass("Ingrese su contraseña: ")
        password_hashed = autenticacion.hash_password(password)
        tipo_usuario = 'user'
        tipo_documento = ''
        identificacion = 0
        estado_usuario = 1
        
        while True:
            
            tipo_identificacion = input('''
        Ingrese tipo de identificacion                            
Cedula = 1
Documento Identidad = 2 
Pasaporte = 3
Ingresa TipoIdentificacion: ''')
            match tipo_identificacion:
                case '1' :
                    
                    identificacion_cedula = int(input("Ingrese numero de Cedula: "))
                    identificacion = identificacion_cedula
                    tipo_documento = 'Cedula'
                    
                    break
                case '2' :
                    
                    identificacion_documento_identidad = int(input("Ingrese Documento Identidad: "))
                    identificacion = identificacion_documento_identidad
                    tipo_documento = 'Tarjeta identidad'
                    break
                case '3' :
                    
                    identificacion_pasaporte = int(input("Ingrese Pasaporte: "))
                    identificacion = identificacion_pasaporte
                    tipo_documento = 'Pasaporte'
                    break
                case _:
                    print("Opcion Invalida, Intenta nuevamente")
                    
        with database.conn:
            database.cursor.execute('''
                INSERT INTO Usuarios (
                    Nombre, 
                    Usuario, 
                    Password, 
                    Identificacion, 
                    TipoIdentificacion,
                    TipoUsuario,
                    IdEstado
                ) 
                VALUES (?, ?, ?, ?, ?, ?, ?)''', 
                (nombre, username, password_hashed, identificacion, tipo_documento, tipo_usuario, estado_usuario))
            
        print("Usuario creado exitosamente.")
        return True
                                                        
    except Exception as e:
        print(f"Error al crear usuario: {e}")
        return False
        