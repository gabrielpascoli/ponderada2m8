#! /bin/env python3
import gradio as gr
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests

message_history = []

def japodiaumussanicola(link):
    response = requests.get(link)
    response.raise_for_status()
    soap = BeautifulSoup(response.text, 'html.parser')
    main = soap.find('main')
    text = main.get_text(separator='\n', strip=True)
    return text
    

def sabumuntonicola(message, history, link):
    load_dotenv()

    print(message)
    print(history)

    message_history.append(message)
    content_message = "\n".join(message_history)

    chat = ChatOpenAI()

    text = "According to: "

    if link:
        text += japodiaumussanicola(link)

    messages = [
        SystemMessage(
            content="you are a simple chatbot with customized instructions to help a user research safety standards in industrial environments."
        ),
        HumanMessage(
            content=text + content_message
        ),
    ]

    bot = (chat(messages)).content

    return bot

def main ():
    chatbeto = gr.ChatInterface(fn=sabumuntonicola, additional_inputs=[gr.Textbox(label="Link")])
    chatbeto.launch()

if __name__ == "__main__":
    main()