Moral Story Generator using Ollama and Llama-3.2
================================================

This project is a Generative AI application that produces short moral stories based on user input prompts. It uses a locally running Llama-3.2-1B-Instruct-GGUF model served via Ollama.

Features
--------
- Generates short stories (150–300 words) with a clear moral.
- Accepts natural language prompts from the user.
- Ensures age-appropriate, coherent storytelling.
- Uses a structured prompt with system-role formatting for better quality.
- Powered by a locally hosted model via the ollama Python API.

Requirements
------------
- Python 3.8+
- Ollama installed and running locally: https://ollama.com
- ollama Python package

To install the Python package:
------------------------------
pip install ollama

How to Run
----------
1. Make sure Ollama is running and the model is available locally:
   ollama run hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF

2. Run the Python script:
   python moral_story_generator.py

3. Example prompt:
   Write a story about a greedy monkey who learns to share with his jungle friends.

File Structure
--------------
- moral_story_generator.py : Main script for generating moral stories
- README.txt               : Project documentation

Prompt Strategy
---------------
The system prompt is designed to guide the model to act as a storyteller who creates engaging and appropriate stories that always end with a clear moral. Formatting tokens such as <|begin_of_text|> and <|start_header_id|> are used to better structure input for LLaMA-based models.

Future Improvements
-------------------
- Add a Gradio or Streamlit UI for interactive use
- Enable story length and tone customization
- Support multilingual storytelling
- Introduce feedback-based model refinement

License
-------
This project is intended for educational and non-commercial use only. For model usage rights, refer to the license on Hugging Face for hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF.

Contact
-------
For feedback, questions, or contributions, please contact:

Name   : Rahul Khatwani 
Email  : rahul.23bce10658@vitbhopal.ac.in 
GitHub : 
