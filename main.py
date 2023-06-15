from surprise import Dataset, KNNBasic #Importando biblioteca

# Carrega os filmes (é possível usar o próprio conjunto de dados)
data = Dataset.load_builtin('ml-100k')

algo = KNNBasic()

trainset = data.build_full_trainset() #Conjunto de treinamento
algo.fit(trainset)#Treinando o modelo

# Recomendações para um usuário em específico 
user_id = str(12)  # ID do usuário
user_items = trainset.ur[trainset.to_inner_uid(user_id)]#Acessando os itens avaliados pelo usuário

# Previsões de classificação para itens não avaliados 
predictions = [algo.predict(user_id, item_id, verbose=False) for item_id in trainset.all_items() if item_id not in user_items]

# Classificando as previsões com base na classificação prevista
top_recommendations = sorted(predictions, key=lambda x: x.est, reverse=True)[:5]

# Mapeando os IDs dos filmes os nomes
movie_name_map = {}# Criando um dicionário vazio 
for movie_id in trainset.all_items():
    movie_name = trainset.to_raw_iid(movie_id)
    movie_name_map[movie_id] = movie_name

# Imprimindo as recomendações com os nomes dos filmes
print("5 recomendações para o usuário", user_id)
for recommendation in top_recommendations:
    movie_id = recommendation.iid
    movie_name = movie_name_map[movie_id]
    print("Filme:", f"'{movie_name}'", "- Classificação prevista:", recommendation.est)
