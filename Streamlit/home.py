import requests
import streamlit as st
from streamlit import secrets

# Get the API_URL from secrets.toml
api_url = secrets["API_URL"]

st.markdown(
    """
    # Predict
    """
)

# Create a form with three fields that take numbers
with st.form("number_form") as form:
    number1 = st.number_input("Enter the PUlocationID:", step=1)
    number2 = st.number_input("Enter the DOLocationID:", step=1)
    number3 = st.number_input("Enter the passenger count:", step=1)
    submit_button = st.form_submit_button(label="Submit")


# Display the numbers if the form is submitted
if submit_button:
    st.write(
        requests.post(
            f"{api_url}/predict",
            json={
                "PULocationID": number1,
                "DOLocationID": number2,
                "passenger_count": number3,
            },
        ).json()
    )
