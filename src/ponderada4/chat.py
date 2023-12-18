#! /bin/env python3
import gradio as gr
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv

message_history = []

def sabumuntonicola(message, history):
    load_dotenv()

    print(message)
    print(history)

    message_history.append(message)
    content_message = "\n".join(message_history)

    chat = ChatOpenAI()

    messages = [
        SystemMessage(
            content="você é um chatbot simples com instruções customizadas para ajudar um usuário a pesquisar normas de segurança em ambientes industriais. "
        ),
        HumanMessage(
            content=content_message
        ),
    ]

    bot = (chat(messages)).content

    return bot

def main ():
    chatbeto = gr.ChatInterface(sabumuntonicola)
    chatbeto.launch()

if __name__ == "__main__":
    main()