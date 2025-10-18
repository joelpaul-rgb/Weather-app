import streamlit as st
import requests
st.title("🌤️Simple weather app")
api_key = "2270f3939c1049169be51636251810"
city = st.text_input("Enter your city name")
if st.button("Get weather"):
    if city:
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
        response = requests.get(url)
        data = response.json()
        if "current" in data:
            current = data["current"]#storing the weather details json file in a variable named current
            location = data["location"]#storing the location details  json file in a variable named location
            st.subheader(f"Weather in {location['name']},{location['country']}")
            st.write(f"🌡️Temperatute:{current['temp_c']}in C")
            st.write(f"💧Humidity:{current['humidity']}%")
            st.write(f"🌬️Wind_speed:{current['wind_kph']}in km/h")
            st.write(f"☁️ Condition:{current['condition']}in km/h")
        else:
            st.error("City not found ,pls enter the right city name")





                         

            
    

