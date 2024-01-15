import streamlit as st
import requests

WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjUwNTY5MDYzZTA0Mzc1MjZjNTUzZDUxMzUi_pc"


# Function to post data to the webhook using argument unpacking
def post_to_webhook(**data):
    response = requests.post(WEBHOOK_URL, json=data)
    return response


st.title("🎬 Entrar com dados básicos 2")

st.markdown(
    """
Tela para entrar dados básicos e automaticamente subir para uma planilha google.
"""
)

with st.form(key="idea_form"):
    name = st.text_input("Nome (opcional)", placeholder="Seu Nome")
    email = st.text_input("e-mail (opcional)", placeholder="Seu e-mail")
    video_idea = st.text_area("idéia de vídeo", placeholder="Sua idéia...")

    submit_button = st.form_submit_button(label="Submiter Idéia 🚀")

    if submit_button:
        if not video_idea.strip():
            st.error("Favor entrar com sua idéia 💡")
            st.stop()

        data = {"nome": name, "email": email, "video_ideia": video_idea}
        response = post_to_webhook(**data)
        if response.status_code == 200:
            st.success("Obrigado! 🌟")
        else:
            st.error("ERRO: Tente novamente. 🛠️")
