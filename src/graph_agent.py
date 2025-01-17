from ollama import chat
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np

def extract_python_code(llm_output):
    """Extract Python code from LLM output."""
    import re
    code_blocks = re.findall(r"```python(.*?)```", llm_output, re.DOTALL)
    return "\n".join(code_blocks).strip()

def call_llm(prompt):
    """Call llm to parse user input."""
    messages=[
        {"role": "system", "content": "You are an assistant that generates and save the graph based on specifications."},
        {"role": "user", "content": prompt}
    ]
    final_response = chat('llama3.2:1b', messages=messages)
    return final_response.message.content


def create_graph(instruction):
    """Create a graph based on user input."""
    try:
        # Call OpenAI to parse the instruction
        llm_output = call_llm(instruction)
        llm_output = extract_python_code(llm_output=llm_output)
        # Evaluate the response as Python code

        # saving code to see it
        with open('code.py', 'w') as file:
            file.write(llm_output)

        exec(llm_output, globals())

        # If the LLM specifies a library and graph, execute the appropriate code
        if 'sns.' in llm_output:
            print("Seaborn graph created.")
        elif 'plt.' in llm_output:
            print("Matplotlib graph created.")
        elif 'px.' in llm_output:
            print("Plotly graph created.")

    except Exception as e:
        print(f"Error creating graph: {e}")

if __name__ == "__main__":

    # "Create a bar plot using Seaborn with 'Category' on the x-axis and 'Values' on the y-axis, using the sample data."
    user_input = (
        "Create a correlation plot using Seaborn and use a small sample data "
    )
    
    create_graph(user_input)
