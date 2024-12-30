from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from huggingface_hub import login
from config import hf_token

login(hf_token)

tokenizer = AutoTokenizer.from_pretrained("allmalab/gpt2-aze")
model = AutoModelForCausalLM.from_pretrained('allmalab/gpt2-aze')

def scoring_function(seq, action):
    
    if len(seq) == 0:
        return 1
        
    tokens = tokenizer.tokenize(action)
    token_ids = tokenizer.encode(action)

    prob = 1
    for i, token_id in enumerate(token_ids):    
        input_text = " ".join(seq) + " " + "".join(tokens[:i])
        
        input_ids = tokenizer.encode(input_text, return_tensors="pt")
        outputs = model(input_ids)

        logits = outputs.logits
        next_token_logits = logits[0, -1, :]

        probabilities = torch.softmax(next_token_logits, dim=-1)
        
        prob *= probabilities[token_id].item()
    
    return prob