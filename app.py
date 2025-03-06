import streamlit as st
from generator import generate_ad_copy

st.set_page_config(page_title = "Brands by Infusion",page_icon="🚀")

st.title("AI-Powered Marketing Copy Generator BY SAGAR DABGAR")
st.write("Enter details below to generate a catchy ad copy for your brand!")

brand_name = st.text_input("Brand Name", placeholder="e.g., GreenVibe")
product_desc = st.text_input("Product/Service Description", placeholder="e.g., Eco-friendly reusable water bottles")
target_audience = st.text_input("Target Audience", placeholder="e.g., Eco-conscious consumers")
tone = st.selectbox("Tone", ["Exciting", "Professional", "Casual"])


# Generate button
if st.button("Generate Ad Copy"):
    if brand_name and product_desc and target_audience:
        with st.spinner("Generating your ad copy..."):
            headline, description = generate_ad_copy(brand_name, product_desc, target_audience, tone)
            st.subheader("Your Ad Copy")
            st.write(f"**Headline:** {headline}")
            st.write(f"**Description:** {description}")
    else:
        st.error("Please fill all fields!")

# Footer
st.write("---")
st.write("Built with ❤️ by [Your Name] for Brands by Infusion Test")