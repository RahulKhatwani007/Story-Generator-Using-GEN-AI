Moral Story Generator using Ollama and Llama-3.2
================================================

This project is a Generative AI application that produces short moral stories based on user input prompts. It uses a locally running Llama-3.2-1B-Instruct-GGUF model served via Ollama.

Features
--------
- Generates short stories (150–300 words) with a clear moral.
- Accepts natural language prompts from the user.
- Ensures age-appropriate, coherent storytelling.
- Uses a structured prompt with system-role instructions for better output quality.
- Powered by a locally hosted model via the ollama Python API.

Requirements
------------
- Python 3.8+
- Ollama installed and running locally: https://ollama.com
- ollama Python package (install using pip)

Installation:
-------------
pip install ollama

How to Run
----------
1. Make sure Ollama is running and the model is available locally:

   ollama run hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF

2. Run the Python script:

   python moral_story_generator.py

3. Example Prompt:
   Write a story about a greedy monkey who learns to share with his jungle friends.

File Structure
--------------
- moral_story_generator.py : Main script to generate moral stories
- README.txt               : Project documentation

Prompt Strategy
---------------
The system prompt guides the model to act as a storyteller who writes engaging, age-appropriate stories that always end with a moral. Special prompt formatting is used to align with LLaMA model token instructions (e.g., <|begin_of_text|>, <|start_header_id|>, etc.).

Future Improvements
-------------------
- Add a Gradio or Streamlit UI for interactive use
- Enable dynamic story length and tone settings
- Extend support for multilingual storytelling

License
-------
MIT license

**Contact**
-Rahul Khatwani
-rahul.23bce10658@vitbhopal.ac.in
-https://github.com/RahulKhatwani007/Story-Generator-Using-GEN-AI
