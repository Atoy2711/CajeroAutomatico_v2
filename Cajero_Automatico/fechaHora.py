import datetime

def fechaActual():
    # Obtén la fecha y hora actual
    fecha_actual = datetime.datetime.now()

    # Formatea la fecha y la hora como una cadena
    fechaTotal = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")

    return fechaTotal
    
    