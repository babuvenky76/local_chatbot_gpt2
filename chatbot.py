import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the fine-tuned model and tokenizer
model = GPT2LMHeadModel.from_pretrained("./gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("./gpt2")

# Streamlit UI setup
st.set_page_config(page_title="GPT2 Chatbot", layout="centered")
st.title("🔍 GPT2 Chatbot")

# Initialize chat history if not already stored
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.write(chat["message"])

# User input
user_input = st.text_input("You: ")

if user_input:
    # Append user input to chat history
    st.session_state.chat_history.append({"role": "user", "message": user_input})
    
    # Process user input and generate a response
    inputs = tokenizer(user_input, return_tensors="pt")
    outputs = model.generate(
        inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=100,
        temperature=0.1,  # Lower temperature for more deterministic output
        top_k=40,         # Adjust top-k sampling
        top_p=0.85,       # Adjust top-p (nucleus) sampling
        repetition_penalty=1.2,  # Penalty for repetition
        num_beams=5,      # Use beam search with 5 beams
        early_stopping=True  # Stop early when all beams reach the end
   
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Append chatbot response to chat history
    st.session_state.chat_history.append({"role": "assistant", "message": response})
    
    # Refresh the page to show updated chat
    st.query_params["rerun"] = "true"

# Display chat history
for chat in st.session_state.chat_history:
    st.write(f"{chat['role'].capitalize()}: {chat['message']}")