import streamlit as st
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load GPT-2 model and tokenizer
@st.cache_resource
def load_model():
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    # GPT-2 does not have a padding token, so we use the EOS token instead
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    return tokenizer, model

tokenizer_gen, model_gen = load_model()

# Initialize session state
if "chat_history_ids" not in st.session_state:
    st.session_state.chat_history_ids = None

st.title("PADI GPT-2")

user_input = st.text_input("You:", "")

if user_input:
    # Tokenize user input
    bot_input_ids = tokenizer_gen.encode(user_input + tokenizer_gen.eos_token, return_tensors="pt")

    # Ensure tensors are on the same device as the model
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    bot_input_ids = bot_input_ids.to(device)
    model_gen = model_gen.to(device)

    # Ensure chat history is initialized properly
    if st.session_state.chat_history_ids is None:
        st.session_state.chat_history_ids = bot_input_ids
    else:
        st.session_state.chat_history_ids = torch.cat([st.session_state.chat_history_ids, bot_input_ids], dim=-1)

    # Generate a response from GPT-2
    with torch.no_grad():
        bot_attention_mask = torch.ones_like(st.session_state.chat_history_ids)  # Ensure proper mask
        new_chat_history_ids = model_gen.generate(
            st.session_state.chat_history_ids,
            max_length=st.session_state.chat_history_ids.shape[-1] + 50,  # Avoid going beyond context
            pad_token_id=tokenizer_gen.eos_token_id,  # Use EOS token as padding
            do_sample=False,
            top_k=10,
            top_p=0.95
        )

    # Extract new response safely
    if new_chat_history_ids.shape[-1] > st.session_state.chat_history_ids.shape[-1]:
        response_tokens = new_chat_history_ids[:, st.session_state.chat_history_ids.shape[-1]:]
    else:
        response_tokens = new_chat_history_ids

    response = tokenizer_gen.decode(response_tokens[0], skip_special_tokens=True)

    # Update session state
    st.session_state.chat_history_ids = new_chat_history_ids

    # Display chatbot response
    st.text_area("PADI:", response, height=100)