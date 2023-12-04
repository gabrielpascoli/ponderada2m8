README
Objetivo

Este código implementa um chatbot simples que compreende e processa comandos do usuário relacionados a movimentação ou navegação. A função principal do bot é interpretar a entrada do usuário e determinar o destino pretendido.


Visão Geral do Código
Funções

vate(objetivo)
Esta função recebe uma lista de objetivos como entrada e constrói uma resposta indicando a intenção do bot de ir para o destino especificado. Itera pela lista de objetivos e os acrescenta à string de resposta.
Dicionários
intent_dict

Este dicionário contém expressões regulares como chaves e nomes de ação correspondentes como valores. Cada expressão regular é projetada para coincidir com um tipo específico de comando do usuário relacionado a movimentação ou navegação. O nome da ação associado especifica a função a ser executada quando uma correspondência é encontrada.
action_dict

Este dicionário mapeia nomes de ação para suas respectivas funções. Neste caso, associa a ação "vate" à função vate.
Interação com o Usuário

O código entra em um loop onde solicita repetidamente a entrada do usuário. O usuário pode digitar comandos, e o bot os interpretará usando as expressões regulares definidas. Se uma correspondência for encontrada, a função associada será executada, produzindo uma resposta.

O loop continua até que o usuário digite "sair", momento em que o programa é encerrado.
Exemplo de Uso

    Entrada:css
```vá para a praia```

Saída:

```Vou até praia```

Entrada:

```dirija-se ao mercado```

Saída:

```Vou até mercado```

Entrada:

```sair```
O programa é encerado 

Observações

    As expressões regulares em intent_dict são projetadas para capturar várias formas de comandos relacionados à navegação em português.
    O código é insensível a maiúsculas e minúsculas (input().lower()), permitindo que os usuários insiram comandos em qualquer caso.
    Os usuários podem sair do programa digitando "sair" quando solicitado.


video [https://youtu.be/aRu0P3sXxfM]