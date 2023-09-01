from flask import Flask, render_template
import requests
# URL de la API de OpenAQ para obtener información de ubicación específica
url = "https://api.openaq.org/v2/locations/278619"  #278619 <-UTP 2178<-EEUU
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
for location in sorted_location_data:
    print("Nombre:", location["name"])
    print("Ciudad:", location["city"])
    print("País:", location["country"])
    print("-----")
    #if location["country"]== "EEUU"
    # Creamos las listas para los valores
    Contaminantes= []
    Unidad= []
    Promedio= []
    Ultimo_Valor= []
    Ultima_Actualizacion= []
    if location["country"]== "US":
        Contaminantes1= []
        Unidad1= []
        Promedio1= []
        Ultimo_Valor1= []
        Ultima_Actualizacion1= []
    if location["country"]== "PE":
        Contaminantes1= []
        Unidad1= []
        Promedio1= []
        Ultimo_Valor1= []
        Ultima_Actualizacion1= []
    colores = ["bg-primary", "bg-secondary", "bg-success", "bg-danger", "bg-warning", "bg-info"]
for parameter in location['parameters']:
    print(parameter['parameter'])
    print(parameter['unit'])
    #print(parameter['average'])
    #print(parameter['lastValue'])
    #print(parameter['lastUpdated'])
    Contaminantes.append(parameter['parameter'])
    Unidad.append(parameter['unit'])
    Promedio.append(parameter['average'])
    Ultimo_Valor.append(parameter['lastValue'])
    Ultima_Actualizacion.append(parameter['lastUpdated'])
    print("-----")
app = Flask(__name__)
app.static_folder = 'static'
@app.route('/')
def index():
    return render_template('index.html',Contaminantes=Contaminantes,Unidad=Unidad,Promedio=Promedio,
                           Ultimo_Valor=Ultimo_Valor,Ultima_Actualizacion=Ultima_Actualizacion,
                           Contaminantes1=Contaminantes1,Unidad1=Unidad1,Promedio1=Promedio1,
                           Ultimo_Valor1=Ultimo_Valor1,Ultima_Actualizacion1=Ultima_Actualizacion1,
                           colores=colores)
if __name__ == '__main__':
    app.run(debug=True)




