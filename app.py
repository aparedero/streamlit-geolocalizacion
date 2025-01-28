import requests
import streamlit as st
import pandas as pd

#Initializing variable for certificate validation
cert_valido = True

# Streamlit app title
st.header("Geoposicionamiento IP", divider=True)

# Streamlit sidebar configuration parameters
st.sidebar.subheader("Configuración")
protocolo = st.sidebar.radio("Selecciona protocolo de consulta en ifconfig.me:", ["HTTP", "HTTPS"])
if protocolo == "HTTPS":
    cert_valido = st.sidebar.checkbox("Comprobar certificado válido", value=True)

#Python requests to get the IP address and location
direccion_ip = requests.get(f"{protocolo.lower()}://ifconfig.me", verify=cert_valido)
localizacion = requests.get(f"http://ip-api.com/json/{direccion_ip.text}", verify=cert_valido)

#Show IP address
st.write(f"**Tu dirección es:** {direccion_ip.text}")    

#Show capture information as dataframe
st.write("Dataframe con datos")
df2 = pd.DataFrame([localizacion.json()])
st.dataframe(df2) 

#Create map section
st.subheader("Mapa 🌍")

# Show captured city and create map object
st.write(f"**Tu ciudad es:** {localizacion.json()['city']}")
df = pd.DataFrame({"lat": [localizacion.json()['lat']], "lon": [localizacion.json()['lon']] })
st.map(df)

# Show json contents as expander
with st.expander("Ver JSON"):
    st.write(localizacion.json())