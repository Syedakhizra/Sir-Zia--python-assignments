import streamlit as st

def convert_units(value, unit_from, unit_to):

    conversions = {
        "meter_kilometer": 0.001,
        "kilometer_meter":1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000
    }

    if unit_from == unit_to:
        return value

    key = f"{unit_from}_{unit_to}"
    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not supported"
    
st.title("Unit Converter")

result = None

value = st.number_input("Enter the value:",0.0)

unit_from = st.selectbox("Convert from:", ["meter", "kilometer", "gram", "kilogram"])

unit_to = st.selectbox("Convert to:", ["meter", "kilometer", "gram", "kilogram"])

if st.button("Convert"):
   result =  convert_units(value, unit_from, unit_to)
if result is not None:
    st.write(f"Converted value: {result}")