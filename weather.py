import requests
import streamlit as st

# Define a function to get weather data from Open-Meteo API
def get_weather_data(latitude, longitude):
    response = requests.get(
         f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
#         f"https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

    )
    return response.json()

# Streamlit app layout
st.title('Weather Data App')

# User input for latitude and longitude
latitude = st.number_input('Enter latitude', value=0.0, format="%.2f")
longitude = st.number_input('Enter longitude', value=0.0, format="%.2f")

# Button to request weather data
if st.button('Get Weather Data'):
    # Get weather data
    weather_data = get_weather_data(latitude, longitude)
    
    # Display weather data
    if 'hourly' in weather_data:
        st.write('Hourly Temperature (°C):')
        st.write(weather_data['hourly']['temperature_2m'])
    else:
        st.error('Error retrieving weather data')

# Run the Streamlit app

if __name__ == '__get_weather_data__':
    main()
