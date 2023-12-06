Perceptron README
Descrição

Este é um código Python que implementa um perceptron simples, uma unidade básica de rede neural. O perceptron é treinado para realizar a operação lógica AND em conjuntos de dados de entrada.
Classe Perceptron
Métodos

    __init__(self, learning_rate=0.1, n_iterations=100, threshold=0.5): O construtor da classe Perceptron. Inicializa os hiperparâmetros, pesos e viés do perceptron.

    activation_function(self, x): Função de ativação que retorna 1 se a entrada for maior ou igual ao limiar (threshold) e 0 caso contrário.

    predict(self, inputs): Realiza a predição do perceptron para um conjunto de entradas. Calcula a soma ponderada das entradas, aplica a função de ativação e retorna a saída predita.

    train(self, X, y): Treina o perceptron usando o algoritmo de aprendizado do perceptron. Itera sobre o conjunto de treinamento por um número fixo de iterações, ajustando os pesos e o viés com base nos erros de predição.

Atributos

    learning_rate: Taxa de aprendizado, controla o tamanho dos passos durante o treinamento.

    n_iterations: Número de iterações de treinamento.

    threshold: Limiar para a função de ativação.

    weights: Pesos do perceptron, inicializados como um array de zeros.

    bias: Viés do perceptron, inicializado como zero.

Exemplo de Uso

O exemplo de uso do perceptron é fornecido para a operação lógica AND. Os conjuntos de entrada X e as saídas esperadas y_list são definidos para quatro combinações de valores booleanos (0 ou 1).

Para cada conjunto de saída y, um perceptron é treinado e testado. Os resultados de cada teste são exibidos, mostrando as saídas previstas para as combinações de entrada (0, 0), (0, 1), (1, 0) e (1, 1).
Execução do Código

O código pode ser executado como um script Python. Os resultados do treinamento para cada conjunto de saída são exibidos, demonstrando como o perceptron aprende a realizar a operação lógica AND.