## Description   
An automatic Chinese poem generator based on LSTM is implemented in this file.   
In data.py[https://github.com/JoyyTj/RNN_FUN/blob/master/Chinese%20Poetry/data.py] and data
   
## Training data from:   
https://github.com/chinese-poetry/chinese-poetry   
The json file contains about 250000 Songshi in total.   
Since it took me about 3 hours to run 25 batches(each of size 256) on cpu, I didn't train the model on the whole dateset and randomly picked 2560 poems to train.   
   
##   Code reference:   
https://github.com/justdark/pytorch-poetry-gen   
https://github.com/braveryCHR/LSTM_poem
