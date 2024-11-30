# streamlit_projeto_teste run application/main.py
# pyi-makespec --onefile --additional-hooks-dir=./hooks myapp.py
# pyinstaller launcher.spec --clean
import streamlit as st
import time

def run():
    # Tirar a margem do Streamlit:
    hide_streamlit_style = """
    <style>
        .stMainBlockContainer {padding-top: 0rem;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stAppDeployButton {visibility: hidden;}
        .stAppHeader {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # Programa:
    menu = st.sidebar.selectbox("Menu", ["Preferências", "Relatórios"])

    if menu == "Preferências":
        st.header("Painel de Preferências do Usuário")
        st.write("Este painel permite que você configure e ajuste suas preferências.")

        # Nome de usuário:
        nome_usuario = st.text_input("Digite seu nome:")
        if nome_usuario:
            st.write(f"Bem-vindo(a), {nome_usuario}!")

        # Cor:
        cor_preferida = st.selectbox("Escolha sua cor preferida:", ["Azul", "Verde", "Vermelho"])
        st.write(f"Sua cor preferida é: {cor_preferida}")

        # Idade
        idade = st.slider("Selecione sua idade:", 10, 100, 25)
        st.write(f"Sua idade é: {idade} anos.")

        # Notificações:
        notificacoes = st.checkbox("Deseja receber notificações?")
        if notificacoes:
            st.write("Notificações ativadas.")
        else:
            st.write("Notificações desativadas.")

        # Botão de salvar:
        if st.button("Salvar Preferências"):
            with st.spinner("Salvando suas preferências..."):
                time.sleep(3)
            st.success("Preferências salvas com sucesso!")

        # Upload de arquivos:
        ultimo_arquivo = st.file_uploader("Faça o upload de uma imagem ou documento:")
        if ultimo_arquivo:
            st.write(f"Arquivo carregado: {ultimo_arquivo.name}")
        else:
            st.write("Nenhum arquivo carregado.")

        # Salvar:
        st.session_state.nome_usuario = nome_usuario
        st.session_state.cor_preferida = cor_preferida
        st.session_state.idade = idade
        st.session_state.notificacoes = notificacoes

    elif menu == "Relatórios":
        st.header("Relatórios")
        st.write("Aqui você pode visualizar relatórios e históricos.")

        # Gráfico Simples
        st.write("Quantidade de Logins por Semana:")
        dados = [3, 5, 2, 8, 6, 9, 4]  # Dados fictícios
        st.line_chart(dados)

# Executar a aplicação
if __name__ == "__main__":
    run()