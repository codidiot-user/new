import streamlit as st
import google.generativeai as genai
genai.configure(api_key=st.secrets["gemini_api"])
def ai(txt):
    
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(" explain everything in detail with it's corresponding definition"+txt)
    return response.text





st.title("QuantWeb.AI")
st.header("Developed by Codidioter")
st.write("\n" * 20)
st.markdown("---")
st.write("This Ai can make mistakes check important info", align="bottom")
st.write(align="top")
st.markdown("---")  
input=st.chat_input("Ask QuantWeb")

if "message" not in st.session_state:
    st.session_state.message = []
for chat in st.session_state.message:
    with st.chat_message(chat["role"]):
         st.write(chat["message"])


if input:
    with st.chat_message("user"):
        st.write(input)
        st.session_state.message.append({"role":"user","message":input})
    if "Hello" in input or "hi" in input:
        with st.chat_message("bot"):
            st.write("How can I help with you 🙂!")
            st.session_state.message.append({"role":"bot","message":"How can I help with you 🙂!"})
    elif "Who are you" in input:
        with st.chat_message("bot"):
            st.write("I'm a updated version of CI-gpt. I have fed with lot of information and details!")
            st.session_state.message.append({"role":"bot","message":"I'm a updated version of CI-gpt. I have fed with lot of information and details!"})
    elif "How many lines code does quantweb have?" in input: 
        with st.chat_message("bot"):
            st.write("Here my work is to assist with you. Your are asking about personel information that would illegeal according me! ")
            st.session_state.message.append({"role":"bot","message":"Here my work is to assist with you. Your are asking about personel information that would illegeal according me! "})
    elif "Tell about logesh" in input or "tell about logesh" in input:
        with st.chat_message("bot"):
            st.write("Logesh who is the founder of the Codidiot. Well he had developed the QuantWeb background remover and QuantWeb.AI. \n Still he is working to develop more and more Web app using Python!")
            st.session_state.message.append({"role":"bot","message":"Logesh who is the founder of the Codidiot. Well he had developed the QuantWeb background remover and QuantWeb.AI. \n Still he is working to develop more and more Web app using Python!"})
    elif "you like logesh" in input or "You like logesh" in input:
        with st.chat_message("bot"):
            st.write("Yeah! I like Logesh who is the founder of the Codidiot. Well he had developed the QuantWeb background remover and QuantWeb.AI. \n Still he is working to develop more and more Web app using Python!")
            st.session_state.message.append({"role":"bot","message":"Yeah! I like Logesh who is the founder of the Codidiot. Well he had developed the QuantWeb background remover and QuantWeb.AI. \n Still he is working to develop more and more Web app using Python!"})

 

    else:
     with st.chat_message("bot"):
      data=ai(input)
      st.write(data)
      st.session_state.message.append({"role":"bot","message":data})

print(st.session_state.message)
