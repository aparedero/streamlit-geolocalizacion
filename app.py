import requests
import streamlit as st
import pandas as pd

#Inicializamos variables
cert_valido = True

# Título de la app
st.header("Geoposicionamiento IP", divider=True)

# Opciones en barra lateral
st.sidebar.subheader("Configuración")
protocolo = st.sidebar.radio("Selecciona protocolo de consulta en ifconfig.me:", ["HTTP", "HTTPS"])
if protocolo == "HTTPS":
    cert_valido = st.sidebar.checkbox("Comprobar certificado válido", value=True)


#Captura la dirección IP y la localización
direccion_ip = requests.get(f"{protocolo.lower()}://ifconfig.me", verify=cert_valido)
localizacion = requests.get(f"http://ip-api.com/json/{direccion_ip.text}", verify=cert_valido)

#Muestra la dirección IP capturada
st.write(f"**Tu dirección es:** {direccion_ip.text}")    

#Crea Dataframe con los datos
st.write("Dataframe con datos")
df2 = pd.DataFrame([localizacion.json()])
st.dataframe(df2) 

#Crea Mapa
st.subheader("Mapa 🌍")
# Muestra la ciudad que ha identificado
st.write(f"**Tu ciudad es:** {localizacion.json()['city']}")
df = pd.DataFrame({"lat": [localizacion.json()['lat']], "lon": [localizacion.json()['lon']] })
st.map(df)

# Muestra el json
with st.expander("Ver JSON"):
    st.write(localizacion.json())