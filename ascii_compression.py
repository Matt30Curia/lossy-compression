import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import json

# Funzione per convertire l'ASCII art in una matrice numerica
def ascii_to_matrix():
    ascii_art = [
        "                                        -------                ",                
        "                                    ---------------       ---  ",   
        "    --                            -------------------------    ",   
        "   -----                         -------------------------     ",   
        "   -------                      -----------------------------  ",   
        "   ----------                  -----------------------------   ",   
        "   -------------               ---------------------------     ",   
        "    ----------------           -------------------------       ",   
        "     ----------------------    -------------------------       ",   
        "      --------------------------------------------------       ",   
        "   ---  ------------------------------------------------       ",   
        "   -----------------------------------------------------       ",   
        "    ---------------------------------------------------        ",   
        "     --------------------------------------------------        ",   
        "      ------------------------------------------------         ",   
        "        ----------------------------------------------         ",   
        "           ------------------------------------------          ",   
        "        --------------------------------------------           ",   
        "         ------------------------------------------            ",   
        "          ----------------------------------------             ",   
        "            ------------------------------------               ",   
        "                 ------------------------------                ",   
        "                 ----------------------------                  ",   
        "             ------------------------------                    ",   
        "       ---------------------------------                       ",   
        "   ----------------------------------                          ",   
        "        -------------------------                              ",   
        "               ----------                                      "
    ]
    
    matrix = []
    for row in ascii_art:
        matrix.append([1 if char == '-' else 0 for char in row])
    return np.array(matrix)

#prepara i dati (x, y) e le etichette con 1 - e o " "
def prepare_data(matrix):
    x = []
    y = []
    labels = []
    
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            x.append(i)
            y.append(j)
            labels.append(matrix[i][j])  #1 se + e 0 se spazio vuoto

    X = np.array(list(zip(x, y)))  #coordinate
    y = np.array(labels)  #etichette binarie (0 o 1)
    return X, y

#crea il modello della rete neurale (un solo neurone finale)
def create_model():
    model = Sequential([
        Dense(9, input_dim=2, activation='sigmoid'),
        Dense(5, activation='sigmoid'),
        Dense(2, activation='softmax')
    ])  #probabilità di "+" o spazio bianco
    
    model.compile(loss='sparse_categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])
    return model

#esportara i pesi in json
def export_weights_to_json(model, filename):
   
    weights = model.get_weights()
    
    weights_as_list = [w.tolist() for w in weights]
    
    with open(filename, 'w') as json_file:
        json.dump(weights_as_list, json_file)

#carica i pesi
def load_weights_from_json(model, filename):
    with open(filename, 'r') as json_file:
        weights_as_list = json.load(json_file)
    weights = [np.array(w) for w in weights_as_list]
    model.set_weights(weights)

# Funzione per ricostruire l'ASCII art in base alle previsioni del modello
def print_ascii_from_predictions(predictions, matrix_shape):
   
    index = 0
    for i in range(matrix_shape[0]):
        row = ""
        for j in range(matrix_shape[1]):
            if predictions[index] > 0.6:  
                print("-",end="") 
            else:
                print(" ",end="") 
            index += 1
        print()
       
    
   
model = create_model()


matrix = ascii_to_matrix()


X, y = prepare_data(matrix)


model.fit(X, y, epochs=500, verbose=1)


export_weights_to_json(model, 'model_weights.json')


load_weights_from_json(model, 'model_weights.json')


predictions = model.predict(X)


final_predictions = np.argmax(predictions, axis=1)


print_ascii_from_predictions(final_predictions, matrix.shape)
