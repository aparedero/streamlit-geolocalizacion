import requests
import streamlit as st
import pandas as pd

# Initializing variable for certificate validation
valid_cert = True

# Streamlit page configuration
st.set_page_config(
    page_title="IP geolocation using API REST",
    page_icon="world_map",
    layout="wide",
    )

# Streamlit app title
st.info("Source code of this example can be found on: https://github.com/aparedero/streamlit-geolocation-example")
st.header("IP geolocation 🗺️ using API REST", divider=True)

# Streamlit sidebar configuration parameters
st.sidebar.subheader("Settings")
protocol = st.sidebar.radio("Select API protocol to request at ifconfig.me:", ["HTTP", "HTTPS"])
if protocol == "HTTPS":
    valid_cert = st.sidebar.checkbox("Validate certficate", value=True)

#Python requests to get the IP address and location
ip_address = requests.get(f"{protocol.lower()}://ifconfig.me", verify=valid_cert)
location = requests.get(f"http://ip-api.com/json/{ip_address.text}", verify=valid_cert)

#Show IP address
st.write(f"**Your IP address is:** {ip_address.text}")    

#Show capture information as dataframe
st.write("Dataframe")
df2 = pd.DataFrame([location.json()])
st.dataframe(df2) 

#Create map section
st.subheader("Map 🌍")

# Show captured city and create map object
st.write(f"**Your city is:** {location.json()['city']}")
df = pd.DataFrame({"lat": [location.json()['lat']], "lon": [location.json()['lon']] })
st.map(df)

# Show json contents as expander
with st.expander("See JSON content from ip-api.com"):
    st.write(location.json())