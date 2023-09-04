from flask import Flask, render_template
import requests
# URL de la API de OpenAQ para obtener información de ubicación específica
url = "https://api.openaq.org/v2/locations/2178"  #278619 <-UTP 2178<-EEUU
    # Encabezados con la clave de API
headers = {
"4955719a99abf12460ae6e3677eedb74eebd04dd0b379a0444d5131d73bb9d0f": "my-openaq-api-key-12345-6789"
}
# Realizar la solicitud GET a la API con los encabezados
response = requests.get(url, headers=headers)
# Procesar la respuesta JSON
data = response.json()
# Acceder a los datos de la ubicación y mostrarlos
location_data = data["results"]
# Ordenar la lista de datos por el nombre de la ubicación
sorted_location_data = sorted(location_data, key=lambda x: x["name"])
# Mostrar los datos ordenados
Contaminantes1= []
Unidad1= []
Promedio1= []
Ultimo_Valor1= []
Ultima_Actualizacion1= []
Calidad= []
for location in sorted_location_data:
    print("Nombre:", location["name"])
    print("Ciudad:", location["city"])
    print("País:", location["country"])
    print("-----")
    # Creamos las listas para los valores
    Contaminantes= []
    Unidad= []
    Promedio= []
    Ultimo_Valor= []
    Ultima_Actualizacion= []
for parameter in location['parameters']:
    Contaminantes.append(parameter['parameter'])
    Unidad.append(parameter['unit'])
    Promedio.append(parameter['average'])
    Ultimo_Valor.append(parameter['lastValue'])
    Ultima_Actualizacion.append(parameter['lastUpdated'])
    #DEMO
    parameter['lastValue']=1
    #DEMO
    if parameter['lastValue']<parameter['average']:
        Calidad.append('Bueno')
    else:
        Calidad.append('Malo')
#Para las enfermedades
Enfermedades=[]
Sintomas=[]
Descripcion=[]
Posicion=[]
con1=[]
con2=[]
img=[]
for i, palabra in enumerate(Calidad):
    if palabra == 'Malo':
        Posicion.append(i)
#para Problemas Respiratorios
for i in Posicion:
    if Contaminantes[i]=='pm10':
        con1='Sí'
for i in Posicion:
    if Contaminantes[i]=='o3':
        con2='Sí'
if con1=='Sí' and con2=='Sí':
    Enfermedades.append("Problemas Respiratorios")
    Sintomas.append("Tos, dificultad para respirar, aumento de la producción de moco y sibilancias.")
    Descripcion.append("La exposición a contaminantes como el ozono (O3) y las partículas gruesas (PM10) puede causar problemas respiratorios agudos, especialmente en personas con enfermedades respiratorias preexistentes.")
    img.append("EnfRes.jpg")
#para Asma
for i in Posicion:
    if Contaminantes[i]=='nox':
        con1='Sí'
for i in Posicion:
    if Contaminantes[i]=='pm25':
        con2='Sí'
if con1=='Sí' and con2=='Sí':
    Enfermedades.append("Asma")
    Sintomas.append("Tos, sibilancias (silbido al respirar), dificultad para respirar y opresión en el pecho.")
    Descripcion.append("La exposición a contaminantes como el dióxido de nitrógeno (NO2) y las partículas finas (PM2.5) puede desencadenar o agravar los síntomas del asma en personas que ya padecen la enfermedad.")
    img.append("asma.jpg")
#para Enfermedades Cardiovasculares
for i in Posicion:
    if Contaminantes[i]=='pm25':
        con1='Sí'
for i in Posicion:
    if Contaminantes[i]=='co':
        con2='Sí'
if con1=='Sí' and con2=='Sí':
    Enfermedades.append("Enfermedades Cardiovasculares")
    Sintomas.append("Varían según la enfermedad cardiovascular, pero pueden incluir dolor en el pecho, dificultad para respirar, fatiga y edema (hinchazón de piernas y tobillos).")
    Descripcion.append(" La exposición crónica a contaminantes como los óxidos de nitrógeno (NOx), el monóxido de carbono (CO) y las partículas finas (PM2.5) puede aumentar el riesgo de enfermedades cardiovasculares, incluyendo enfermedades cardíacas y accidentes cerebrovasculares.")
    img.append("EC.jpg")

#para Irritación Respiratoria
for i in Posicion:
    if Contaminantes[i]=='nox':
        con1='Sí'
for i in Posicion:
    if Contaminantes[i]=='so2':
        con2='Sí'
if con1=='Sí' and con2=='Sí':
    Enfermedades.append("Irritación Respiratoria")
    Sintomas.append("Irritación de las vías respiratorias, tos, dolor de garganta, ojos llorosos y congestión nasal.")
    Descripcion.append("Contaminantes como el dióxido de azufre (SO2) y los óxidos de nitrógeno (NOx) pueden causar irritación aguda de las vías respiratorias y síntomas respiratorios.")
    img.append("IR.jpg")
#para Síntomas Leves
for i in Posicion:
    if Contaminantes[i]=='nox':
        con1='Sí'
for i in Posicion:
    if Contaminantes[i]=='co':
        con2='Sí'
if con1=='Sí' and con2=='Sí':
    Enfermedades.append("Síntomas Leves")
    Sintomas.append("Dolor de cabeza, fatiga, náuseas y posiblemente mareos.")
    Descripcion.append("La exposición a bajos niveles de contaminantes como los óxidos de nitrógeno (NOx) y el monóxido de carbono (CO) puede causar síntomas leves.") 
    img.append("SL.png")
colores = ["bg-primary", "bg-secondary", "bg-success", "bg-danger", "bg-warning", "bg-info"]   
app = Flask(__name__)
app.static_folder = 'static'
@app.route('/')
def index():
    return render_template('index.html',Contaminantes=Contaminantes,Unidad=Unidad,Promedio=Promedio,
                           Ultimo_Valor=Ultimo_Valor,Ultima_Actualizacion=Ultima_Actualizacion,
                           colores=colores, Calidad=Calidad, Enfermedades=Enfermedades, Sintomas=Sintomas,Descripcion=Descripcion, img=img)
if __name__ == '__main__':
    app.run(debug=True)




