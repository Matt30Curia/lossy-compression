---

# Neural Network-Based ASCII Art Lossy Compression

This project demonstrates how to use a simple neural network to compress ASCII art in a lossy way. The neural network learns to predict the structure of an ASCII image, reducing its size while maintaining a recognizable form.

## Features

- Compress and reconstruct ASCII art images using a neural network.
- Lossy compression:  model reduces the size of 5% of the image while attempting to preserve the important visual structure. Additionally, by reducing the length of the floating point numbers and altering the json structure, it is possible to further reduce the size of     the weights.
- Save and load model weights in JSON format for easy sharing and reusability.

---

## Installation

Follow the instructions below to set up the project.

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- `pip` (Python package manager)

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/ascii-art-compressor.git
cd ascii-art-compressor
```

### Step 2: Install Dependencies

Use `pip` to install the necessary libraries for running the neural network and handling the data:

```bash
pip install -r requirements.txt
```



---

## Usage

Once the installation is complete, you can run the provided Python script to train the neural network and compress ASCII art.

### Run the Code

To train the model and compress an example ASCII art:

```bash
python ascii_compression.py
```

The script will:

1. Convert the input ASCII art into a matrix of 1s (for the `-` character) and 0s (for spaces).
2. Train a neural network on the matrix.
3. Save the model's weights in a JSON file.
4. Load the saved weights and predict the compressed output.
5. Print the reconstructed ASCII art.

---

## How It Works

1. **Input ASCII Art**: The ASCII art is manually defined as a list of strings where `-` represents a visual character, and spaces represent empty areas.
   
2. **Data Preparation**: The `ascii_to_matrix` function converts the ASCII art into a matrix, where each element is either `1` (for `-`) or `0` (for a space).

3. **Model Training**: The neural network is trained to predict each character's position as a binary value (either `-` or space) based on its location in the matrix. The neural network uses a simple architecture with two hidden layers.

4. **Lossy Compression**: During training, the neural network learns to compress the ASCII art into a smaller representation, removing some details to achieve a smaller file size.

5. **Prediction**: After training, the model is used to predict the reconstructed ASCII art by outputting probabilities for each character's position.

6. **Export and Load Weights**: The model's weights can be exported to a JSON file using the `export_weights_to_json()` function. The weights can later be loaded back using `load_weights_from_json()` to recreate the trained model.

---

## Functions

### `ascii_to_matrix()`

Converts the ASCII art into a numerical matrix representation, where `1` represents a character (`-`) and `0` represents space.

### `prepare_data(matrix)`

Prepares the training data by converting the matrix coordinates and labels (0 for space, 1 for `-`).

### `create_model()`

Creates a simple neural network model for binary classification. It uses two hidden layers and outputs a classification of either `-` or a space.

### `export_weights_to_json(model, filename)`

Exports the trained model weights to a JSON file for easy storage or sharing.

### `load_weights_from_json(model, filename)`

Loads the model weights from a JSON file to continue training or perform predictions.

### `print_ascii_from_predictions(predictions, matrix_shape)`

Prints the reconstructed ASCII art based on the model's predictions.

---

## Example Output

After running the script, the neural network will print a compressed version of the original ASCII art.

For example, the neural network might take this:

```
                                        -------                
                                    ---------------       ---  
    --                            -------------------------    
   -----                         -------------------------     
   -------                      -----------------------------  
   ----------                  -----------------------------   
   -------------               ---------------------------     
    ----------------           -------------------------       
     ----------------------    -------------------------       
      --------------------------------------------------       
   ---  ------------------------------------------------       
   -----------------------------------------------------       
    ---------------------------------------------------        
     --------------------------------------------------        
      ------------------------------------------------         
        ----------------------------------------------         
           ------------------------------------------          
        --------------------------------------------           
         ------------------------------------------            
          ----------------------------------------             
            ------------------------------------               
                 ------------------------------                
                 ----------------------------                  
             ------------------------------                    
       ---------------------------------                       
   ----------------------------------                          
        -------------------------                              
               ----------                                      
```

And output something like this:

```


                                     -------------------
                                   -------------------------
    ------                       ---------------------------
   ---------                    ----------------------------
   -----------                -----------------------------
   -------------             ------------------------------
   ---------------         --------------------------------
   -------------------------------------------------------
   ------------------------------------------------------
    -----------------------------------------------------
    ----------------------------------------------------
     --------------------------------------------------
      -------------------------------------------------
       -----------------------------------------------
        ---------------------------------------------
         -------------------------------------------
         ------------------------------------------
          -----------------------------------------
           ---------------------------------------
            -------------------------------------
            ------------------------------------
            -----------------------------------
            ---------------------------------
            -------------------------------
            --------------------------
           ----------------------
           ---------------------
```

---
