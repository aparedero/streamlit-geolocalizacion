# IP Geolocation App

This is a simple Streamlit web application that allows users to fetch their IP address and obtain its geographic location. It visualizes the results on a map and displays additional details in a table and JSON format.

---

## Features

- **Fetch IP Address**: Automatically retrieves the user's public IP address.
- **Geolocation Data**: Fetches geographic details based on the IP address (e.g., city, latitude, longitude).
- **Interactive Map**: Displays the detected location on a world map.
- **Data Visualization**: Shows the geolocation data in a DataFrame and as a raw JSON object.
- **Protocol Configuration**: Choose between HTTP or HTTPS for data requests.
- **Certificate Validation**: Option to validate SSL certificates when using HTTPS.

---

## Live Demo

Live demo of this app is on https://geolocation-example.streamlit.app/

Please note you will see the IP address from the server this app is actually running, not your own IP :)

## Installation

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>

2. Run the app
    ```bash
    streamlit run app.py
    ```

3. Enjoy!