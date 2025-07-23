import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

class DisplayResultStreamlit:
    def __init__(self, use_case, graph, user_message):
        self.use_case= use_case
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        use_case = self.use_case
        graph = self.graph
        user_message = self.user_message
        
        print(user_message)
        if use_case == "Basic Chatbot":
                for event in graph.stream({'messages':("user", user_message)}):
                    print(event.values())
                    for value in event.values():
                        print(value['messages'])
                        with st.chat_message("user"):
                            st.write(user_message)
                        with st.chat_message("assistant"):
                            st.write(value["messages"].content)
        if use_case == "Maths Chatbot":
                for event in graph.stream({'messages':("user", user_message)}):
                    print(event.values())
                    for value in event.values():
                        print(value['messages'])
                        with st.chat_message("user"):
                            st.write(user_message)
                        with st.chat_message("assistant"):
                            st.write(value["messages"].content)