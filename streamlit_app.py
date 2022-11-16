
from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
from datetime import date



def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    """
    # El Spot Prices!
    """

    today = date.today()
    iso_date = today.isoformat()
    url = "https://api.energidataservice.dk/dataset/Elspotprices?start=" + str(iso_date) + "&filter={%22PriceArea%22:%22dk2%22}"
    data = requests.get(url).json()
    records = data["records"]


    st.dataframe(records)



