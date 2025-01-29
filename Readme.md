# GPT2 Chatbot

This project is a chatbot using Streamlit and a fine-tuned GPT-2 model.

## Setup Instructions

### Prerequisites

- Python 3.10.13
- `pyenv` and `pyenv-virtualenv` installed

### Step-by-Step Setup

1. **Install `pyenv` and `pyenv-virtualenv`**:

    ```bash
    curl https://pyenv.run | bash
    ```

    Add the following lines to your shell configuration file (`~/.bashrc`, `~/.zshrc`, etc.):

    ```bash
    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init --path)"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    ```

    Apply the changes by restarting your shell or running:

    ```bash
    source ~/.zshrc  # or ~/.bashrc, etc.
    ```

2. **Install Python 3.10.13**:

    ```bash
    pyenv install 3.10.13
    ```

3. **Create a virtual environment**:

    ```bash
    pyenv virtualenv 3.10.13 gpt2_chatbot
    ```

4. **Activate the virtual environment**:

    ```bash
    pyenv activate gpt2_chatbot
    ```

5. **Download and save the pre-trained GPT-2 model and tokenizer locally**:

    ```sh
    python download_model.py
    ```

6. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

7. **Run the Streamlit app**:

    ```bash
    streamlit run /path/to/your/chatbot.py
    ```

## File Structure

- `chatbot.py`: The main script for the chatbot.
- `requirements.txt`: The dependencies required for the project.
- `README.md`: This file with setup instructions.

## Notes

- Ensure that the path to the fine-tuned model in `chatbot.py` is correct.
- If you encounter any issues, please refer to the official documentation of the respective libraries.