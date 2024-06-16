# Load model directly
from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("markusbayer/CySecBERT")
model = AutoModelForMaskedLM.from_pretrained("markusbayer/CySecBERT")

import torch
from transformers import AutoModel, AutoTokenizer

# Load the model and tokenizer
model_name = "markusbayer/CySecBERT"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Your input word
king_input_word = "King"
Queen_input_word = "Queen"
Man_input_word = "Man"
Woman_input_word = "Woman"

# Preprocess the input word
king_inputs = tokenizer(king_input_word, return_tensors='pt')
Queen_inputs = tokenizer(Queen_input_word, return_tensors='pt')
Man_inputs = tokenizer(Man_input_word, return_tensors='pt')
Woman_inputs = tokenizer(Woman_input_word, return_tensors='pt')

# Get the embeddings
with torch.no_grad():
    king_outputs = model(**king_inputs)
    Queen_outputs = model(**Queen_inputs)
    Man_outputs = model(**Man_inputs)
    Woman_outputs = model(**Woman_inputs)

# Extract the embeddings for the input word
king_inputsembeddings = king_outputs.last_hidden_state[:, 0, :].numpy()
Queen_inputsembeddings = Queen_outputs.last_hidden_state[:, 0, :].numpy()
Man_inputsembeddings = Man_outputs.last_hidden_state[:, 0, :].numpy()
Woman_inputsembeddings = Woman_outputs.last_hidden_state[:, 0, :].numpy()
