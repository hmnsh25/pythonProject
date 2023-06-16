# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import openai

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = "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"


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message["content"]


text = f"""
You should express what you want a model to do by
providing instructions that are as clear and
specific as you can possibly make them.
This will guide the model towards the desired output,
and reduce the chances of receiving irrelevant
or incorrect responses. Don't confuse writing a
clear prompt with writing a short prompt.
In many cases, longer prompts provide more clarity
and context for the model, which can lead to
more detailed and relevant outputs.
"""
prompt = f"""
generate an AI model written as python code which does following.
tracks all payment failures
identify the type of failure and segregate into different text files
text file should contain log message, date and time, type
"""
response = get_completion(prompt)
print(response)

# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
