
import gradio as gr
from openai import OpenAI


NOUS = "NousResearch/Llama-2-7b-chat-hf"
MISTRAL = "mistralai/Mistral-7B-Instruct-v0.2"
MIX = "mistralai/Mixtral-8x7B-Instruct-v0.1"
MIX_AWQ = "TheBloke/Nous-Hermes-2-Mixtral-8x7B-SFT-AWQ"

model_id=MIX_AWQ

temperature=0.25

title = "Basic Chatbot Demo"
description = f"model = {model_id} <br>"
               #embedings = {embed_model_name} <br> \
               #chromadb = 100 record {collection_name}"       
article = " <p>"




# Gradio function upon submit
def predict(prompt, temperature, model_id):
    
    
    if model_id=="mistralai/Mistral-7B-Instruct-v0.2":
        # Connect to vLLM using openai client
        client = OpenAI(
            base_url="http://localhost:8001/v1",
            api_key="token-abc123",
        )
    else:
        # Connect to vLLM using openai client
        client = OpenAI(
            base_url="http://localhost:8002/v1",
            api_key="token-abc123",
        )
    
    history_openai_format = []
    #for human, assistant in history:
    #    history_openai_format.append({"role": "user", "content": human })
    #    history_openai_format.append({"role": "assistant", "content":assistant})
    history_openai_format.append({"role": "user", "content": prompt})
  
    response = client.chat.completions.create(
        model=model_id,
        messages= history_openai_format,
        temperature=temperature,
        stream=True
        )

    partial_message = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
              partial_message = partial_message + chunk.choices[0].delta.content
              yield partial_message


demo = gr.Interface(
                   predict,
                   #fn=predict, 
                   inputs=[
                            gr.Textbox(label="Prompt", placeholder="select an Example to submit"),
                            gr.Slider(label="Temperature", minimum=0.0, maximum=1.0, value=temperature),
                            gr.Dropdown(label="Model", 
                                        choices=[
                                            "NousResearch/Llama-2-7b-chat-hf",
                                            "mistralai/Mistral-7B-Instruct-v0.2",
                                            "mistralai/Mixtral-8x7B-Instruct-v0.1",
                                            "TheBloke/Nous-Hermes-2-Mixtral-8x7B-SFT-AWQ"
                                        ],
                                        value=model_id
                                        )
                            ],
                   outputs=[
                            #gr.Textbox(label="Guarded Response"),
                            gr.Textbox(label="Generated Response", elem_id="warning"), 
                            ],
                   title=title, 
                   description=description, 
                   allow_flagging="never", 
                   #multimodal=True,
                   
                   theme='upsatwal/mlsc_tiet', # Dark theme large fonts  huggingface hosted
                   examples=[
                              ["Tell me about HPE!"],
                              ["What is the ProLiant DL380A Gen11?"],
                              ["Explain what the Apollo 6500 server is"],
                              ["When did you first learn about RAG?"],
                              ["Write me a poem about GPU performance"],
                              ["Do you think Stuart Russell come to HPE Tech Con again next year?"],

                            ],
                    article=article, # HTML to display under the Example prompt buttons
                    # removes default gradio footer
                    css="footer{display:none !important}"
                   )

# this binds to all interfaces which is needed for proxy forwarding
demo.launch(server_name="0.0.0.0", server_port=443)
#demo.launch(server_name="10.14.56.23", server_port=7866)


