import streamlit as st
import os

from src.langgraph_agentic_ai.ui.uiconfig import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(
            page_title=f"🤖 {self.config.get_page_title()}",
            layout="wide"
        )
        st.header(f"🤖 {self.config.get_page_title()}")

        with st.sidebar:
            # get options from config and select the LLM
            llm_options = self.config.get_llm_options()
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options).strip()

            # model selection
            if self.user_controls["selected_llm"] == 'Groq':
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options).strip()
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key", type="password")
                # validate API Key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have one? Refer: https://console.groq.com/keys")

            # use-case selection
            usecase_options = self.config.get_usecase_options()
            self.user_controls["selected_usecase"]=st.selectbox("Select Usecases", usecase_options).strip()

        return self.user_controls