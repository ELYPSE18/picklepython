import pickle

# Charger les données à partir du fichier
with open('data.pickle', 'rb') as file:
    loaded_data = pickle.load(file)

# Les données sont maintenant stockées sur loaded_data


print(loaded_data)
