import streamlit as st

# Title
st.title("🔁 Simple Unit Converter")

# Choose type of conversion
conversion_type = st.selectbox("Choose conversion type", ["Length", "Weight"])

if conversion_type == "Length":
    units = ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"]
    unit_factors = {
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254,
    }

elif conversion_type == "Weight":
    units = ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"]
    unit_factors = {
        "Kilogram": 1,
        "Gram": 0.001,
        "Milligram": 0.000001,
        "Pound": 0.453592,
        "Ounce": 0.0283495,
    }

# User inputs
input_unit = st.selectbox("From", units)
output_unit = st.selectbox("To", units)
input_value = st.number_input("Enter value to convert", min_value=0.0, format="%.4f")

# Conversion
result = (input_value * unit_factors[input_unit]) / unit_factors[output_unit]

# Display result
st.write(f"### 🔹 Result: {input_value} {input_unit} = {result:.4f} {output_unit}")
