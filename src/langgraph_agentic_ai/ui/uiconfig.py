from configparser import ConfigParser

class Config:
    def __init__(self, config_file="./src/langgraph_agentic_ai/ui/uiconfig.ini"):
        self.config=ConfigParser()
        self.config.read(config_file)

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS", "").split(",")
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS", "").split(",")

    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS", "").split(",")

