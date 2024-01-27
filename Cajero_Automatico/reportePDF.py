# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       reportePDF.py
# Autor:        Juan Camilo Quintero Atoy
# Creado:       6 de Noviembre 2023
# Modificado:   9 de Diciembre 2023
# Copyright:    (c) 2023 by Juan Camilo Quintero Atoy, 2023
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__versión__ = "1.0"

from sqlite3 import connect

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.units import inch, mm
from reportlab.pdfgen import canvas
from datetime import datetime
from sqlite3 import connect
import locale
import subprocess
import os

# Función para crear el encabezado y pie de página del PDF
def encabezado_pie_pagina(canvas, archivoPDF):
    
    estilos = getSampleStyleSheet()
    alineacion = ParagraphStyle(name="alineacion", alignment=TA_RIGHT, parent=estilos["Normal"])

    encabezado_nombre = Paragraph("Camilo 1.0", estilos["Normal"])
    anchura, altura = encabezado_nombre.wrap(archivoPDF.width, archivoPDF.topMargin)
    encabezado_nombre.drawOn(canvas, archivoPDF.leftMargin, 736)
    
    #se define la localidad para el idioma
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    
    #muestra la fecha en el reporte
    fecha = datetime.now().strftime("%A, %d - %B - %Y")
    fecha_reporte = fecha.replace("-", "de")

    encabezado_fecha = Paragraph(fecha_reporte, alineacion)
    anchura, altura = encabezado_fecha.wrap(archivoPDF.width, archivoPDF.topMargin)
    encabezado_fecha.drawOn(canvas, archivoPDF.leftMargin, 736)

    pie_pagina = Paragraph("Reporte generado por Camilo", estilos["Normal"])
    anchura, altura = pie_pagina.wrap(archivoPDF.width, archivoPDF.bottomMargin)
    pie_pagina.drawOn(canvas, archivoPDF.leftMargin, 15 * mm + (0.2 * inch))

# Función para convertir los datos en formato adecuado para el PDF
def convertir_datos(cabecera, datos):
    estilo_encabezado = ParagraphStyle(name="estiloEncabezado", alignment=TA_LEFT,
                                        fontSize=8, textColor=colors.white,
                                        fontName="Helvetica-Bold")
    estilo_normal = getSampleStyleSheet()["Normal"]
    estilo_normal.alignment = TA_LEFT

    claves, nombres = zip(*cabecera)
    encabezado = [Paragraph(nombre, estilo_encabezado) for nombre in nombres]
    
    nuevos_datos = [tuple(encabezado)]

    for dato in datos:
        nuevos_datos.append(tuple([Paragraph(str(dato[clave]), estilo_normal) for clave in claves]))

    return nuevos_datos

# Función para exportar datos a un archivo PDF
def exportar_pdf(titulo, cabecera, datos, nombre_pdf):
    alineacion_titulo = ParagraphStyle(name="centrar", alignment=TA_CENTER, fontSize=9, leading=15,
                                        textColor=colors.black, parent=getSampleStyleSheet()["Heading1"])
    ancho, alto = letter
    convertir_dato = convertir_datos(cabecera, datos)
    
    # Ajuste de anchos de columna
    col_widths = [ancho * 0.05,ancho * 0.12,ancho * 0.13,ancho * 0.11,ancho * 0.1,ancho * 0.1,ancho * 0.12,ancho * 0.14,ancho * 0.12] + [ancho * 0.8] * (len(cabecera) - 1)
    
    tabla = Table(convertir_dato,colWidths=col_widths , hAlign="CENTER")
    
    tabla.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("ALIGN", (0, 0), (0, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("INNERGRID", (0, 0), (-1, -1), 0.50, colors.black),
        ("BOX", (0, 0), (-1, -1), 0.50, colors.black),
    ]))
    
    historia = []
    historia.append(Paragraph(titulo, alineacion_titulo))
    historia.append(Spacer(1, 0.16 * inch))
    historia.append(tabla)

    archivo_pdf = SimpleDocTemplate(nombre_pdf, leftMargin=50, rightMargin=50, pagesize=letter,
                                    title="Reporte PDF", author="Juan Quintero")

    try:
        archivo_pdf.build(historia, onFirstPage=lambda canvas, pdf: encabezado_pie_pagina(canvas, pdf),
                            onLaterPages=lambda canvas, pdf: encabezado_pie_pagina(canvas, pdf))
        return "Reporte generado con éxito."
    
    except PermissionError:
        return "Error inesperado: Permiso denegado."

# Función para generar el reporte
def generar_reporte():
    def dict_factory(cursor, row):
        return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}

    conexion_db = connect("cajero.db")
    conexion_db.row_factory = dict_factory
    cursor = conexion_db.cursor()

    cursor.execute("""
    SELECT
        Transaccion.Id,
        Usuarios.Nombre,
        Transaccion.Identificacion,
        Transaccion.FechaTransaccion,
        Cuentas.NumeroCuenta,
        Transaccion.Valor,
        Tarjetas.numero_tarjeta,
        Transaccion.Detalle,
        Transaccion.TipoTransaccion
    FROM
        Transaccion
	left join Usuarios ON Transaccion.Usuario = Usuarios.Id
	left join Cuentas ON Transaccion.Cuenta = Cuentas.Usuario
	left join Tarjetas ON Transaccion.Tarjeta = Tarjetas.id;
""")
    datos = cursor.fetchall()
    conexion_db.close()

    titulo = "LISTADO DE USUARIOS"
    cabecera = (
        ("Id", "ID"),
        ("Nombre", "NOMBRE"),
        ("Identificacion", "IDENTIFICACION"),
        ("FechaTransaccion", "FECHA"),
        ("NumeroCuenta", "NUMERO CUENTA"),
        ("Valor", "VALOR"),
        ("numero_tarjeta", "TARJETA"),
        ("Detalle", "DETALLE"),
        ("TipoTransaccion", "TRANSACCION")
    )
    ruta_reportes = "Registro_Transacciones"
    fecha = datetime.now().strftime("%d-%m-%Y_%H-%M")
    nombre_pdf = os.path.join( ruta_reportes, f"Transacciones_{fecha}.pdf")
    reporte = exportar_pdf(titulo, cabecera, datos, nombre_pdf)
    
    
    #condicion para abrir automatico el PDF generado
    if reporte.startswith("Reporte generado con éxito."):
        #Para sistemas Windows
        subprocess.run(["start", "", nombre_pdf], shell=True)
        
        #Para sistemas Unix
        #subprocess.run(["open", nombre_pdf])

# Llamar la función para generar el reporte
#generar_reporte()