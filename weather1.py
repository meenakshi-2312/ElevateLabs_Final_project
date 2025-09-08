import streamlit as st
import requests as rt
api="8ef0b79686e0ffe26e8d542f15072dd4"
st.title(" simple weather app")
city =st.text_input("Enter the city")
if st.button("enter"):
    st.write(f"Here is your results of {city}")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"
    data = rt.get(url).json()
    if data.get("cod") != 200:
        st.error("City not found or invalid API key!")
    else:
        st.subheader(f"Weather in {city}")
        st.write(" Temperature:", data["main"]["temp"], "°C")
        st.write(" Humidity:", data["main"]["humidity"], "%")
        st.write("Condition:", data["weather"][0]["description"].capitalize())
        st.write("sunrise:",data["sys"]["sunrise"])
        st.write("sunset:",data["sys"]["sunset"])
