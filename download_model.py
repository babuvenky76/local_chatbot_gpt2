from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Download pre-trained GPT-2 model and tokenizer
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Save the model locally
model.save_pretrained("./gpt2")
tokenizer.save_pretrained("./gpt2")
