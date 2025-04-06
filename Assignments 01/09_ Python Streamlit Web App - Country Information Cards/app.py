import streamlit as st
import requests

def fetchCounry(countryName):
    url = f"https://restcountries.com/v3.1/name/{countryName}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        country_data = data[0]
        name = country_data['name']['common']
        capital = country_data.get('capital', ['No capital'])[0]
        population = country_data.get('population', 'No population data')
        area = country_data.get('area', 'No area data')
        currency = country_data.get('currencies', {'No currency': {}})
        region = country_data.get('region', 'No region data')

        return name, capital, population, area, currency, region
    else:
        return None
    

def main():
    st.title("Country Information App")

    country_name = st.text_input("Enter country name:")

    if st.button("Get Country Info"):
        if country_name:
            country_info = fetchCounry(country_name)
            if country_info:
                name, capital, population, area, currency, region = country_info
                st.subheader("Country Details")
                st.write(f"**Country Name:** {name}")
                st.write(f"**Capital:** {capital}")
                st.write(f"**Population:** {population}")
                st.write(f"**Area:** {area} km²")
                st.write(f"**Currency:** {list(currency.keys())[0]}")
                st.write(f"**Region:** {region}")
            else:
                st.error("Country not found!")
        else:
            st.warning("Please enter a country name.")  




if __name__ == "__main__":
    main()