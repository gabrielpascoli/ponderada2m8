Nicola, rode o comando:
```
./chat.py
```

# ChatBot para Pesquisa de Normas de Segurança Industrial

Este é um simples chatbot Python desenvolvido para ajudar os usuários a pesquisar normas de segurança em ambientes industriais. O chatbot utiliza o modelo de linguagem da OpenAI e interage com os usuários por meio da biblioteca Gradio.

## Pré-requisitos

Antes de executar o código, certifique-se de ter os seguintes pré-requisitos instalados:

```- Python 3```
```- Bibliotecas necessárias (instaláveis via pip):```
  ```- gradio```
  ```- langchain```
  ```- python-dotenv```

Você pode instalar as bibliotecas necessárias executando o seguinte comando:

```bash
pip install gradio langchain python-dotenv
```

## Como Executar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Crie um arquivo `.env` no diretório do projeto e adicione suas credenciais OpenAI, caso necessário.

```env
OPENAI_API_KEY=SuaChaveDeAPIOpenAI
```

3. Execute o script principal:

```bash
python nome-do-script.py
```

O chatbot será iniciado e estará pronto para interagir.

## Estrutura do Código

O código consiste em um script Python (`nome-do-script.py`) que utiliza a biblioteca Gradio para criar uma interface de chat interativa. O chatbot é alimentado pelo modelo de linguagem da OpenAI e está configurado para fornecer informações sobre normas de segurança industrial.

A função principal `sabumuntonicola` recebe as mensagens do usuário, mantém um histórico das mensagens e utiliza o modelo de linguagem para gerar respostas apropriadas.

## Contribuições

Contribuições são bem-vindas! Se você encontrar problemas ou tiver sugestões para melhorar o chatbot, sinta-se à vontade para criar issues ou enviar pull requests.

**Divirta-se interagindo com o chatbot!**