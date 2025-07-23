import streamlit as st
from src.langgraph_agentic_ai.ui.streamlitui.load_ui import LoadStreamlitUI
from src.langgraph_agentic_ai.llms.groq_llm import GroqLLM
from src.langgraph_agentic_ai.graph.graph_builder import GraphBuilder
from src.langgraph_agentic_ai.ui.streamlitui.display_results import DisplayResultStreamlit

def load_langgraph_agentic_ai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.
    """

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return
    
    user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            # configure the LLM
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model could not be initialized.")
                return
            
            # initialize and set up the graph based on use case
            user_case = user_input.get("selected_usecase")
            if not user_case:
                st.error("Error: No use case selected.")
                return
            
            # graph builder
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(user_case)
                
                DisplayResultStreamlit(user_case, graph, user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph setup failed: {e}")
                return
        
        except Exception as e:
                st.error(f"Error: Graph setup failed: {e}")
                return
