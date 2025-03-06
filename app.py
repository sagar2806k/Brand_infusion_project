import streamlit as st
from generator import generate_ad_copy

# Setup the page - make it look slick
st.set_page_config(page_title="Brands by Infusion", page_icon="🚀")

# Title and intro
st.title("AI-Powered Marketing Copy Generator")
st.write("Bhai, enter details and get a mast ad copy!")

# Inputs from user
brand_name = st.text_input("Brand Name", placeholder="e.g., FitPulse")
product_desc = st.text_input("Product/Service Description", placeholder="e.g., High-performance gym wear")
target_audience = st.text_input("Target Audience", placeholder="e.g., Fitness enthusiasts")
tone = st.selectbox("Tone", ["Exciting", "Professional", "Casual"])  # Tone dropdown

# Generate button logic
if st.button("Generate Ad Copy"):
    # Check if all fields are filled
    if brand_name and product_desc and target_audience:
        print("===> User clicked generate, let’s do this!")  # Simple log
        with st.spinner("Whipping up your ad copy..."):
            headline, description = generate_ad_copy(brand_name, product_desc, target_audience, tone)
            # Show the ad copy
            st.subheader("Your Killer Ad Copy")
            st.write(f"**Headline:** {headline}")
            st.write(f"**Description:** {description}")
            print("===> Ad copy done and shown!")  # Another log
    else:
        st.error("Sab fields bharo bhai, kya kar rahe ho!")
        print("===> Error: User forgot to fill stuff")  # Log for empty input

# Footer - some credit
st.write("---")
st.write("Built by [Your Name] with chai and code!")