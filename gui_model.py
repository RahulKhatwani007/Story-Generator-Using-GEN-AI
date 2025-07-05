import gradio as gr
import ollama

def generate_moral_story(user_prompt, max_tokens=400):
    # System prompt to set the storyteller persona
    system_prompt = (
        "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n"
        "You are a storyteller who creates engaging short stories with clear moral lessons. "
        "Each story should be appropriate for all ages, between 150-300 words, "
        "and end with a clearly stated moral. Write in clear English.\n<|eot_id|>"
        "<|start_header_id|>user<|end_header_id|>\n"
    )
    assistant_tag = "\n<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
    full_prompt = system_prompt + user_prompt + assistant_tag

    response = ollama.generate(
        model="hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF",
        prompt=full_prompt,
        options={
            "temperature": 0.7,  # Slightly lower temperature for coherent stories
            "num_predict": max_tokens
        }
    )
    return response['response']

with gr.Blocks(title="Moral Story Generator") as demo:
    gr.Markdown(
        "# 📖 Moral Story Generator\n"
        "Enter a story prompt and get a complete story with a moral lesson!\n"
        "*(Powered by Llama 3.2 1B Instruct on Ollama)*"
    )
    with gr.Row():
        inp = gr.Textbox(
            label="Enter your story prompt",
            lines=2,
            placeholder="e.g., Write a story about a greedy monkey who learns to share."
        )
    with gr.Row():
        out = gr.Textbox(
            label="Generated Moral Story",
            lines=10  # Increased lines for longer stories
        )
    btn = gr.Button("Generate Story")
    btn.click(fn=generate_moral_story, inputs=inp, outputs=out)

demo.launch()