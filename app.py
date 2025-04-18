import streamlit as st

# Configurações da página
st.set_page_config(page_title="Tela Inicial", layout="centered")

# Cabeçalho
st.title("🎉 Bem-vindo à Sua Tela Inicial!")

# Mensagem principal
st.write("Essa tela foi feita com Python + Streamlit e pode ser acessada de qualquer lugar pela internet.")

# Botão
if st.button("Clique aqui"):
    st.success("Você clicou no botão! Está funcionando perfeitamente 😊")

# Rodapé
st.markdown("---")
st.caption("Criado por [Seu Nome Aqui]")
