## Description   
An automatic Chinese poem generator based on LSTM is implemented in this file.   
Process for raw json data is in [data.py](https://github.com/JoyyTj/RNN_FUN/blob/master/Chinese%20Poetry/data.py) and [data_utils.py](https://github.com/JoyyTj/RNN_FUN/blob/master/Chinese%20Poetry/data_utils.py)    
Codes for the model, training, testing and final results are in [main.ipynb](https://github.com/JoyyTj/RNN_FUN/blob/master/Chinese%20Poetry/main.ipynb) 
   
## Training data from:   
https://github.com/chinese-poetry/chinese-poetry   
The json file contains about 250000 Songshi in total.   
Since it took me about 3 hours to run 25 batches(each of size 256) on cpu, I didn't train the model on the whole dateset but randomly picked 2560 poems to train.   
   
##   Code reference:   
https://github.com/justdark/pytorch-poetry-gen   
https://github.com/braveryCHR/LSTM_poem
