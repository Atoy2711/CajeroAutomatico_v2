# Importaciones relacionadas con la autenticación y usuarios
import autenticacion
import createUser

# Importaciones relacionadas con transacciones y operaciones financieras
import IngresarDinero
import retirar
import Consiganciones
import Saldo

# Importaciones relacionadas con la gestión de cuentas y tarjetas
import createCuenta
import createTarjeta

#Importaciones para pago de recibos publicos
import Servicios_Publicos

# Importación para generación de reportes PDF
import reportePDF

# Importación del módulo os
import os


#opcion = ""

def menu_principal():
    print("\t\t\u001b[34m\u001b[1mBienvenido al Cajero Automático Multifuncional\u001b[0m")
    #user = ""
    
    while True:
        opcion = input("""
Cajero Automático

1. Iniciar sesión
2. Crear usuario
3. Salir
Seleccione una opción: """)
        match opcion:
            case '1':
                
                user, name, identificacion, user_id, cuenta_id, tarjeta_id = autenticacion.autenticar_usuario()
                if user == '':
                    print("Autenticación fallida. La cuenta está bloqueada.")
                elif user == 'camilo':   
                    while True:
                        os.system("cls")
                        print(f"!!!Bienvenido {name}, Que deseas realizar hoy!!")
                                
                        opcion = input("""
Cajero Automático

1. Ingresar Dinero al Cajero
2. Imprimir Informe Diario
3. Salir

Seleccione una opción: """)
                        match opcion:
                            case '1':
                                IngresarDinero.ingresar_cantidad_billetes()
                                os.system('pause')
                            case '2':
                                reportePDF.generar_reporte()
                                os.system('pause')
                            case '3':
                                os.system("cls")
                                print("Gracias por utilizar el Cajero Automático Multifuncional. ¡Hasta luego!")
                                break
                            case _:
                                os.system("cls")#limpiar consola
                                print("Opcion fallida. Intente nuevamente.")
                                continue
                else:    
                    os.system("cls")
                    print(f"!!!Bienvenido {name}, Que deseas realizar hoy!!")
                    
                    while True:
                        opcion = input("""
Cajero Automático

1. Retirar Dinero
2. Consignar Dinero
3. Pagar Recibo
4. Ver Saldo
5. Salir

Seleccione una opción: """)
                        match opcion:
                            case '1':
                                while True:
                                    subopcion = input("""
Realizar Retiro de Cuenta

1. Ahorros
2. Corriente
3. Cancelar Operación

Seleccione una opción: """)
                                    match subopcion:
                                        case '1':
                                            #Retiro de cuenta ahorro
                                            retirar.realizar_retiro(user_id, identificacion, cuenta_id, tarjeta_id, "ahorro")
                                            #print(user)
                                        case '2':
                                            #Retiro de cuenta Corriente
                                            retirar.realizar_retiro(user_id, identificacion, cuenta_id, tarjeta_id,"corriente")
                                            #print(user)
                                        case '3':
                                            print("operacion Cancelada. ¡Hasta luego!")
                                            break
                                        case _:
                                            os.system("cls")
                                            print("Opcion Incorrecta. Intente nuevamente.")
                                            
                                        
                            case '2':
                                while True:
                                    subopcion = input("""
Realizar Consignacion en Cuenta

1. Ahorros
2. Corriente
3. Cancelar Operación

Seleccione una opción: """)
                                    match subopcion:
                                        case '1':
                                            #Retiro de cuenta ahorro
                                            Consiganciones.realizar_consignacion(user_id, identificacion, cuenta_id, tarjeta_id, "ahorro")
                                            
                                        case '2':
                                            #Retiro de cuenta Corriente
                                            Consiganciones.realizar_consignacion(user_id, identificacion, cuenta_id, tarjeta_id, "corriente")
                                            
                                        case '3':
                                            print("operacion Cancelada. ¡Hasta luego!")
                                            break
                                        case _:
                                            os.system("cls")
                                            print("Opcion Incorrecta. Intente nuevamente.")
                            
                            case '3':
                                Servicios_Publicos.realizar_pago_servicios(name,user_id, identificacion, cuenta_id, tarjeta_id)
                            case '4':
                                while True:
                                    subopcion = input("""
Ver Saldo en Cuenta de

1. Ahorros
2. Corriente
3. Cancelar Operación

Seleccione una opción: """)
                                    match subopcion:
                                        case '1':
                                            #Retiro de cuenta ahorro
                                            Saldo.verSaldo(user_id,'ahorro')
                                        case '2':
                                            #Retiro de cuenta Corriente
                                            Saldo.verSaldo(user_id,'corriente')
                                        case '3':
                                            os.system("cls")
                                            print("operacion Cancelada. ¡Hasta luego!")
                                            break
                                        case _:
                                            os.system("cls")
                                            print("Opcion Incorrecta. Intente nuevamente.")
                            case '5':
                                print("Gracias por utilizar el Cajero Automático Multifuncional. ¡Hasta luego!")
                                break
                            case _:
                                os.system("cls")
                                print("Opcion Incorrecta. Intente nuevamente.")
                            
            case '2':
                #Crear usuario
                os.system("cls")
                result = createUser.crear_usuario()
                if result is not None:
                    print("Inicia sesion para continuar con el proceso")
                    #inicia sesion por contingencia
                    _ , _, _, id_user, _, _ = autenticacion.autenticar_usuario()
                    if id_user is not None:
                        #Crear cuenta
                        id_cuenta = createCuenta.crear_cuenta(id_user) 
                        if id_cuenta is not None:
                            #crear Tarjeta
                            createTarjeta.crear_tarjeta(id_cuenta)
                        else:
                            print("Error al crear tarjeta")
                            
                    else:
                        print("Error al crear Cuenta")
                else:
                    print("Error al crear Usuario")
                    
            case '3':
                
                os.system("cls")
                print("Gracias por utilizar el Cajero Automático Multifuncional. ¡Hasta luego!")
                break
            
            case _:
                os.system("cls")
                print("Opcion fallida. Intente nuevamente.")
                continue


if __name__ == "__main__":
    menu_principal()