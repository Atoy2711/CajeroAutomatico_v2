import database

try:
    # Verificar la conexión a la base de datos
    print("Conectado a la base de datos:", database.cursor.execute("PRAGMA database_list").fetchone()[2])

    # # Inserción de datos en la tabla Estado
    # database.cursor.execute('''
    # INSERT INTO Estado (Id, Nombre)
    # VALUES (1, 'Activo'),
    #     (2, 'Inactivo');
    # ''')
    
    # # Inserción de datos en la tabla TipoCuenta
    # database.cursor.execute('''
    # INSERT INTO TipoCuenta (Id, Nombre)
    # VALUES (1, 'Cuenta de Ahorro'),
    #     (2, 'Cuenta Corriente');
    # ''')

    # # Inserción de datos en la tabla Usuario
    # database.cursor.execute('''
    # INSERT INTO Usuario (Id, Nombre, Usuario, Password, Identificacion, TipoIdentificacion, TipoUsuario, NumeroCuenta, saldo_ahorro, saldo_corriente, NumeroTarjeta, Cupo, Retiro, IdEstado)
    # VALUES (1, 'Administrador', 'Admin', 'admin', '123456789', 'Cédula','admin','12345', 0, 0, '1111222233334444', 10000, 500, 1),
    #     (2, 'Usuario2', 'user2', 'password2', '987654321', 'Pasaporte','user', '123456', 0, 0, '5555666677778888', 20000, 1000, 1);
    # ''')

    # Inserción de datos en la tabla Dinero
    database.cursor.execute('''
    INSERT INTO Dinero (Id, Nombre, Denominacion, Cantidad)
    VALUES
        (1, 'Billete de $100000', 100000, 0),
        (2, 'Billete de $50000', 50000, 0),
        (3, 'Billete de $20000', 20000, 0),
        (4, 'Billete de $10000', 10000, 0),
        (5, 'Billete de $5000', 5000, 0),
        (6, 'Billete de $2000', 2000, 0),
        (7, 'Billete de $1000', 1000, 0),
        (8, 'Moneda de $1000', 1000, 0),
        (9, 'Moneda de $500', 500, 0),
        (10, 'Moneda de $200', 200, 0),
        (11, 'Moneda de $100', 100, 0),
        (12, 'Moneda de $50', 50, 0);
    ''')

    # # Inserción de datos en la tabla TipoTransaccion
    # database.cursor.execute('''
    # INSERT INTO TipoTransaccion (Id, Transaccion)
    # VALUES (1, 'Deposito'),
    #     (2, 'Retiro');
    # ''')

    # # Inserción de datos en la tabla Transaccion
    # database.cursor.execute('''
    # INSERT INTO Transaccion (Id, Usuario, Identificacion, FechaTransaccion, Cuenta, Valor, Tarjeta, Detalle, TipoTransaccion)
    # VALUES (1, 1, '123456789', '2023-10-21', 1, 500.00, 1, 'Deposito en efectivo', 1),
    #     (2, 2, '987654321', '2023-10-21', 2, 100.00, 2, 'Retiro en cajero', 2);
    # ''')

    # # Inserción de datos en la tabla ServiciosPublicos
    # database.cursor.execute('''
    # INSERT INTO ServiciosPublicos (Id, NumeroRecibo, Nombre, Valor, TipoPago)
    # VALUES (1, '12345', 'Agua', 50.00, 'Pago en línea'),
    #     (2, '67890', 'Luz', 60.00, 'Pago en efectivo');
    # ''')

    # Verificar la conexión a la base de datos
    print("Datos Insertados.")
    
    database.conn.commit()
except Exception as e:
    print("Error durante la inserción de datos:", str(e))
