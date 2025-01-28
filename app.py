import requests
import streamlit as st
import pandas as pd

#Initializing variable for certificate validation
cert_valido = True

# Streamlit app title
st.header("IP geolocation", divider=True)

# Streamlit sidebar configuration parameters
st.sidebar.subheader("Settings")
protocolo = st.sidebar.radio("Select API protocol to request at ifconfig.me:", ["HTTP", "HTTPS"])
if protocolo == "HTTPS":
    cert_valido = st.sidebar.checkbox("Validate certficate", value=True)

#Python requests to get the IP address and location
direccion_ip = requests.get(f"{protocolo.lower()}://ifconfig.me", verify=cert_valido)
localizacion = requests.get(f"http://ip-api.com/json/{direccion_ip.text}", verify=cert_valido)

#Show IP address
st.write(f"**Your IP address is:** {direccion_ip.text}")    

#Show capture information as dataframe
st.write("Dataframe")
df2 = pd.DataFrame([localizacion.json()])
st.dataframe(df2) 

#Create map section
st.subheader("Map 🌍")

# Show captured city and create map object
st.write(f"**Your city is:** {localizacion.json()['city']}")
df = pd.DataFrame({"lat": [localizacion.json()['lat']], "lon": [localizacion.json()['lon']] })
st.map(df)

# Show json contents as expander
with st.expander("See JSON content from ip-api.com"):
    st.write(localizacion.json())