import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('cajero.db')
cursor = conn.cursor()


#Creación de la tabla Cuenta
cursor.execute('''
CREATE TABLE IF NOT EXISTS Cuentas (
    Id INT,
    Usuario INT,
    TipoCuenta INT,
    NumeroCuenta VARCHAR(20),
    saldo_ahorro DECIMAL(10, 2), 
    saldo_corriente DECIMAL(10, 2),
    FOREIGN KEY (Usuario) REFERENCES Usuarios(Id)
    PRIMARY KEY("Id" AUTOINCREMENT)
)
''')


#Creación de la tabla Estado
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Estado (
#     Id INT PRIMARY KEY,
#     Nombre VARCHAR(50)
# )
# ''')

#Creación de la tabla Dinero
cursor.execute('''
CREATE TABLE IF NOT EXISTS Dinero (
    Id INT  PRIMARY KEY,
    Nombre VARCHAR(50),
    Denominacion DECIMAL(10, 2),
    Cantidad INT
)
''')


#Creación de la tabla TipoTransaccion
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS TipoTransaccion (
#     Id INT PRIMARY KEY,
#     Transaccion VARCHAR(50)
# )
# ''')
#Creación de la tabla ServiciosPublicos
cursor.execute('''
CREATE TABLE IF NOT EXISTS ServiciosPublicos (
    Id INT  PRIMARY KEY,
    NumeroRecibo VARCHAR(20),
    Nombre VARCHAR(50),
    Valor DECIMAL(10, 2),
    Estado VARCHAR(50)
)
''')
#Creación de la tabla TipoCuenta
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS TipoCuenta (
#     Id INT PRIMARY KEY,
#     Nombre VARCHAR(50)
# )

# ''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tarjetas (
        id INT  PRIMARY KEY,
        cuenta INT,
        numero_tarjeta INT,
        saldo REAL,
        FOREIGN KEY (cuenta) REFERENCES Cuentas(Id)
    )
''')
#Creación de la tabla Transaccion
cursor.execute('''
CREATE TABLE IF NOT EXISTS Transaccion (
    Id INT  PRIMARY KEY,
    Usuario INT,
    Identificacion VARCHAR(20),
    FechaTransaccion DATETIME,
    Cuenta INT,
    Valor DECIMAL(10, 2),
    Tarjeta INT,
    Detalle VARCHAR(255),
    TipoTransaccion VARCHAR(20)
)
''')



# Crear tablas usuarios
cursor.execute('''
    
CREATE TABLE IF NOT EXISTS Usuarios (
    Id INT  PRIMARY KEY,
    Nombre VARCHAR(255),
    Usuario VARCHAR(50),
    Password VARCHAR(50),
    Identificacion VARCHAR(20),
    TipoIdentificacion VARCHAR(20),
    TipoUsuario VARCHAR(50), 
    IdEstado INT
)
''')

conn.commit()