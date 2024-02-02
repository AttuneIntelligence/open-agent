import sys
import time
from datetime import datetime

sys.path.append('/workspace/open-agent/src')
from bin.keys import set_keys
from bin.utilities import *
from chat_templates.prompt_engineering import *
from functions.toolkit import *

class OpenAgent:
    def __init__(self,
                 verbose=False):
        ### INITIALIZATION
        self.verbose = verbose
        set_keys(self)
        self.timestamp = datetime.now().isoformat(timespec='minutes')
        self.ai_name = "Indra"
        self.home = "/workspace/open-agent/"
        self.Utilities = Utilities(self)
        self.ContextEngineering = ContextEngineering(self)
        self.Toolkit = Toolkit(self)
        
        ### HYPERPARAMETERS
        self.max_tokens = 2400
        self.max_agent_iterations = 3
        self.memory_context_len = 3
        self.streaming = True

        ### OPENAI INFERENCE
        self.gpt_model = "gpt-4-1106-preview"
        self.gpt_vision_model = "gpt-4-vision-preview"

        ### INITIALIZE CLASS WITH MODELS
        self.instantiate_model_apis()

    def personalize_message_thread(self,
                                   user_json):
        self.human_name = user_json["full_name"]
        self.username = user_json["username"]
        self.question = user_json["question"]
        
    #########################
    ### CONNECT TO MODELS ###
    #########################
    def instantiate_model_apis(self):
        print(f"Connecting to LLM APIs...")
        ### ATTEMPT RUNPOD CONNECTION...
        if self.try_self_hosted:
            ### AGENT
            if self.Utilities.test_api_up(self.agent_model_url):
                self.Agent = Mixtral7x8B_Agent(self)
                print(f"=> Agent Model: {self.agent_model_name}")
            else:
                self.Agent = OpenAI_Agent(self)
                print(f"=> Agent Model: {self.gpt_model} (failed to connect to {self.agent_model_name}")
                
            ### INSTRUCT
            if self.Utilities.test_api_up(self.instruct_model_url):
                self.Instruct = Mixtral7x8B_Instruct(self)
                print(f"=> Instruct Model: {self.instruct_model_name}")
            else:
                self.Instruct = OpenAI_Completion(self)
                print(f"=> Instruct Model: {self.gpt_model} (failed to connect to {self.instruct_model_name})")
                
            ### VISION
            if self.Utilities.test_api_up(self.vision_model_url):
                self.Vision = LLaVA_Vision(self)
                print(f"=> Vision Model: {self.vision_model_name}")
            else:
                self.Vision = OpenAI_Vision(self)
                print(f"=> Vision Model: {self.gpt_vision_model} (failed to connect to {self.vision_model_name})")


        ### ...OR JUST CONNECT TO OPENAI
        else:
            self.Agent = OpenAI_Agent(self)
            self.Instruct = OpenAI_Instruct(self)
            self.Vision = OpenAI_Vision(self)
            print(f"=> Agent Model: {self.gpt_model}")
            print(f"=> Vision Model: {self.gpt_vision_model}")
            print(f"=> Instruct Model: {self.gpt_model}")





    