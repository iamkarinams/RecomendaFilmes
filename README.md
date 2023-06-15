# RecomendaFilmes

  <img align="center" alt="Ka-Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"> <img align="center" alt="Ka-pycharm" height="30" width="120" src="https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white"> 
  
##

O código fornecido implementa um sistema de recomendação baseado em filtragem colaborativa usando o algoritmo KNN (K-Nearest Neighbors) da biblioteca Surprise.

1. Carregamento do conjunto de dados:
   - O conjunto de dados de filmes "ml-100k" é carregado usando o método `load_builtin()` da classe `Dataset` da biblioteca Surprise.

2. Definição do algoritmo de filtragem colaborativa:
   - O algoritmo KNNBasic é usado para realizar a filtragem colaborativa.

3. Construção do conjunto de treinamento:
   - O conjunto de treinamento completo é construído usando o método `build_full_trainset()` do objeto `data`. Isso fornece os dados de treinamento necessários para o algoritmo de filtragem colaborativa.

4. Treinamento do modelo:
   - O modelo é treinado chamando o método `fit()` do objeto `algo` com o conjunto de treinamento `trainset`. Isso ajusta o modelo aos dados de treinamento.

5. Obtendo as recomendações para um usuário específico:
   - Um usuário específico é selecionado pelo seu ID e os itens avaliados por esse usuário são obtidos do conjunto de treinamento.

6. Fazendo previsões de classificação para itens não avaliados:
   - São feitas previsões de classificação para os itens não avaliados pelo usuário usando o método `predict()` do objeto `algo`.

7. Classificação das previsões com base na classificação prevista:
   - As previsões são classificadas em ordem decrescente com base na classificação prevista.

8. Mapeamento dos IDs dos filmes para seus nomes:
   - Os IDs dos filmes são mapeados para seus nomes usando o método `to_raw_iid()` do objeto `trainset`.

9. Impressão das recomendações com os nomes dos filmes:
   - As principais recomendações são impressas juntamente com os nomes dos filmes correspondentes.

O que pode ser modificado:
- Conjunto de dados: Você pode usar seu próprio conjunto de dados em vez do conjunto de dados pré-carregado "ml-100k".
- Algoritmo de filtragem colaborativa: Você pode experimentar outros algoritmos de filtragem colaborativa disponíveis na biblioteca Surprise.
- Número de recomendações: Você pode modificar o número de recomendações alterando o valor `[:5]` para um valor diferente na linha `top_recommendations = sorted(predictions, key=lambda x: x.est, reverse=True)[:5]`.
- ID do usuário: Você pode alterar o ID do usuário na variável `user_id` para obter recomendações para um usuário diferente.
- Formato de impressão: Você pode modificar o formato de impressão das recomendações para atender às suas necessidades específicas.
