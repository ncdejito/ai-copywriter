import streamlit as st

from ai import write_ad

prompt = st.text_area(
    label="Prompt",
    height=150,
    value="Write a creative ad for the following product to run on Facebook aimed at lovers:\n\nProduct: Ferrero Bouquet is a collection of quality red roses and 12 pieces of chocolate to express love this Valentine's Day.",
    max_chars=250,
)

if st.button("Write ad"):
    st.write(write_ad(prompt))
