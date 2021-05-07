#!/usr/bin/python
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth

### INPUT ###
Fecha = "Octubre 2020"
Titulo = "Reporte Sismicidad: %s" % Fecha
Subtitulo = "Alerta temprana CSN-AMSA\n\nCentro Sismológico Nacional \n%s" % Fecha
file_name = "test.pdf"
#############

### Titulo ###
width, height = A4
canvas = Canvas(file_name, pagesize=A4)
canvas.setFont("Helvetica-Bold", 14)
text_width = stringWidth(Titulo)
text = canvas.beginText((width - text_width) / 2.0, height - 1*cm)
text.textLines(Titulo)
canvas.setFont("Helvetica-Bold", 14)
text_width = stringWidth(Subitulo)
text = canvas.beginText((width - text_width) / 2.0, height - 1.5*cm)
text.textLines(Subitulo)
canvas.drawImage("CSN.png", 0.2*cm, height - 0.2*cm)

### Intro ###

canvas.setFont("Helvetica", 12)
text = canvas.beginText(2*cm, height - 4*cm)
Texto = "1. Contexto sísmico del norte chileno"
text.textLines(Texto)

canvas.setFont("Helvetica", 12)
text = canvas.beginText(2*cm, height - 4*cm)
Texto = "El Norte chileno se caracteriza por ser considerado uno de los gaps sísmicos o lagunas sísmicas más importantes del mundo, esto quiere decir que es una región en la que existe mucha energía sísmica acumulada que no ha sido liberada por terremotos de gran magnitud (M>8). En la historia sísmica de la región el terremoto más grande en la zona corresponde al de 1877 con una magnitud aproximada a M ~ 8.8 y una ruptura estimada entre la península de Mejillones y el codo de Arica. Luego de este evento transcurrieron 137 años de quietud sísmica hasta el terremoto de Iquique el 2014 con magnitud Mw 8.1, este terremoto no libera toda la energía sísmica acumulada en la región por lo que en la región se puede esperar un sismo de magnitud similar o superior en el futuro. Otros sismos importantes son el terremoto de Antofagasta 1995 Mw 8.1, al sur de la península de Mejillones y el terremoto de Tocopilla 2007 Mw 7.8 al norte de la península de Mejillones."
text.textLines(Texto)

canvas.drawImage("SismicidadTipica.png", 2*cm, height - 8*cm)
text = canvas.beginText(2*cm, height - 14*cm)
Texto = "Catalogo CSN sismos M>4.0 en el periodo 2013 - 2020 para el norte de Chile"
text.textLines(Texto)

text = canvas.beginText(2*cm, height - 15*cm)
Texto = "En la Figura 1 se tiene la sismicidad típica de la zona, usando los datos del catálogo de eventos sísmicos reportados por el CSN se muestran todos los eventos de magnitud superior o igual a M=4.0 ocurridos durante el periodo comprendido entre el 2013 y la totalidad del 2020, contando con un total de XXX sismos."
text.textLines(Texto)
PageBreak()

text = canvas.beginText(2*cm, height - 2*cm)
"En la distribución hipocentral se identifican 3 grupos o tipos de sismicidad que caracterizan la zona: \n\n     -\033[1mSismicidad somera (interplaca)\033[0m o de poca profundidad, este tipo de sismicidad corresponde a los eventos denominados interplaca y la definimos en este trabajo como la que no supera los 70 km, pero principalmente concentrada en los primeros 50 km del contacto de placas. Como se aprecia en la Figura \ref{fig:catalogo45}.a la mayor parte de la sismicidad somera de magnitud significativa (M>4.5) corresponde a sismicidad asociada al terremoto de Illapel del 2014, ya sean sismicidad precursora o réplicas de este evento. En general la sismicidad de gran magnitud (M>8.0) cae dentro de esta categoría.\n     -\033[1mSismicidad intermedia\033[0m o intraplaca, corresponde a eventos entre los 70 y los 150 km, principalmente concentrada entre los 90 y 130 km aproximadamente y se encuentra presente a lo largo de toda la región. Por lo general este tipo de sismicidad tiene una magnitud moderada(M$\sim$5-7) y los eventos de gran magnitud son poco comunes.\n     -\033[1mSismicidad profunda\033[0m corresponden a sismos a más de 150 km y principalmente se concentran en el sur de esta región, en la parte más ancha de Antofagasta junto a la frontera con Argentina y Bolivia en torno a las latitudes 23-24$^\circ$ Sur. Al igual que los sismos de profundidad intermedia, estos terremotos tienden a ser de magnitudes moderadas."
text.textLines(Texto)
PageBreak()
