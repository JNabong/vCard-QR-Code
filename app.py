import streamlit as st
import qrcode
from io import BytesIO

# Function to create vCard string
def create_vcard(first_name, last_name, phone, email, company, title, website):
    vcard = f"""BEGIN:VCARD
VERSION:3.0
N:{last_name};{first_name}
FN:{first_name} {last_name}
ORG:{company}
TITLE:{title}
TEL;TYPE=CELL:{phone}
EMAIL:{email}
URL:{website}
END:VCARD"""
    return vcard

# Function to generate QR code
def generate_qr(data):
    qr = qrcode.make(data)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    return buffer

# Streamlit UI
st.title("📇 vCard QR Code Generator")

st.subheader("Enter Contact Details")

first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
phone = st.text_input("Phone Number")
email = st.text_input("Email")
company = st.text_input("Company")
title = st.text_input("Job Title")
website = st.text_input("Website")

if st.button("Generate QR Code"):
    if first_name and phone:
        vcard = create_vcard(first_name, last_name, phone, email, company, title, website)
        qr_image = generate_qr(vcard)

        st.success("QR Code Generated!")
        st.image(qr_image)

        st.download_button(
            label="Download QR Code",
            data=qr_image.getvalue(),
            file_name="vcard_qr.png",
            mime="image/png"
        )
    else:
        st.error("Please at least enter First Name and Phone Number.")