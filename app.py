import gradio as gr
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModel

# download internlm2 to the base_path directory using git tool
base_path = './internlm2_5-1_8b-chat'
os.system(f'git clone https://oauth2:SvJo8x76g57C2Cog5joj@www.modelscope.cn/nuistmj001/InternLM2-Chat-1.8B-weifeng.git {base_path}')
os.system(f'cd {base_path} && git lfs pull')

# base_path = '/root/InternLM/XTuner/internlm2_5-1_8b-chat'

tokenizer = AutoTokenizer.from_pretrained(base_path,trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(base_path,trust_remote_code=True, torch_dtype=torch.float16)#.cuda()

def chat(message,history):
    for response,history in model.stream_chat(tokenizer,message,history,max_length=2048,top_p=0.7,temperature=1):
        yield response

gr.ChatInterface(chat,
                 title="internlm2_5-1_8b-chat",
                description="""
InternLM is mainly developed by Shanghai AI Laboratory.  
                 """,
                 ).queue(1).launch()