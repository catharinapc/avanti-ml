#### 1. Explique, com suas palavras, o que é machine learning? 

Machine learning é um ramo da inteligência artificial que foca na construção de sistemas que aprendem, melhoram o desempenho, predizem ou classificam com base nos dados que os são ofertados, sem serem explicitamente programados - seja isso feito de forma supervisionada ou não supervisionada. 

#### 2. Explique o conceito de conjunto de treinamento, conjunto de validação e conjunto de teste em machine learning. 

Conjunto de treinamento são os dados ofertados para "ensinar" o modelo, de forma com que ele aprenda os padrões que se apresentam nos dados e ajuste seus parâmetros intertos com base neles, geralmente representam a maior parte dos dados. 

Conjuntos de validação permitem avaliar o desempenho do modelo em dados que ele não viu durante o treinamento antes de testar no conjunto final, atuando como uma verificação intermediária durante o processo de desenvolvimento. Pode ajustar os hiperparâmetros do modelo, monitorar o progresso do treinamento e detectar e prevenir o overfitting.

Conjuntos de teste são mantidos completamente separado até a fase final de avaliação, sendo usados apenas uma vez, no final do processo, para avaliar o desempenho real do modelo em dados completamente novos - fornecendo uma estimativa de quão bem o modelo generaliza para dados desconhecidos.

#### 3. Explique como você lidaria com dados ausentes em um conjunto de dados de treinamento. 

Se a quantidade for pequena, pode-se remover linhas ou colunas afetadas. Caso contrário, a imputação é uma alternativa, preenchendo valores numéricos com média, mediana ou interpolação e valores categóricos com a moda. Modelos preditivos como regressão ou KNN também podem imputar valores ausentes. Além disso, alguns algoritmos, como árvores de decisão, lidam naturalmente com dados faltantes. Outra abordagem é criar uma variável indicativa da ausência de dados, o que pode agregar informação útil ao modelo. 

#### 4. O que é uma matriz de confusão e como ela é usada para avaliar o desempenho de um modelo preditivo? 

A matriz de confusão é uma tabela que avalia o desempenho de um modelo de classificação comparando os valores previstos com os reais. Para problemas binários, ela é composta por quatro elementos: Verdadeiro Positivo, quando o modelo acerta ao prever um positivo; Verdadeiro Negativo, quando acerta ao prever um negativo; Falso Positivo, quando prevê um positivo de forma errada; e Falso Negativo, quando prevê um negativo de forma errada. 

A partir dela, calculam-se métricas como acurácia (proporção total de acertos), precisão (proporção de previsões positivas corretas), recall (proporção de positivos reais corretamente identificados) e F1-score (média harmônica entre precisão e recall).

#### 5. Em quais áreas (tais como construção civil, agricultura, saúde, manufatura, entre outras) você acha mais interessante aplicar algoritmos de machine learning?

Pessoalmente, por ter um background de um curso na área da saúde, acredito ter uma afinidade maior por projetos na área médica.






