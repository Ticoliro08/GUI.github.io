import streamlit as st

st.title ("Loggin do meu lovinho")

nome=st.text_input ("Digite seu nome")
print('vc não é minha namorada! se manda vagabunda')
endereco=st.text_input("Digite sua cidade ")
dt_nasc=st.date_input("Selecione a data de hoje")
tipo_cliente=st.selectbox("Qual rede social você mais usa",["Tik Tok", "Instagram","Facebook", "Whatsapp"])

cadastrar=st.button(" Enviar")
if nome!=('karen pereira gesulado'):
 print('erro, vá embora vagabunda')
if cadastrar:
    with open("Cliente.csv", "a") as arquivo:
        arquivo.write(f"{nome},{endereco},{dt_nasc},{tipo_cliente}\n")
        st.success("Enviado com sucesso!")