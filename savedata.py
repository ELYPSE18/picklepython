import pickle

# Exemple de données à sauvegarder
data = [{
    'name': 'John Doe',
    'age': 30,
    'email': 'john.doe@example.com'
}]

# Sauvegarder les données dans un fichier
with open('data.pickle', 'wb') as file:
    pickle.dump(data, file)

# Charger les données à partir du fichier
with open('data.pickle', 'rb') as file:
    loaded_data = pickle.load(file)

# On ajoute une donnée
loaded_data.append({
    'name': 'John Doe 2',
    'age': 31,
    'email': 'john.doe@example.com3'
})

# // Sauvegarde la donnée
with open('data.pickle', 'wb') as file:
    pickle.dump(loaded_data, file)



print(loaded_data)
