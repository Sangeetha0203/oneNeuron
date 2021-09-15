from utils.model import Perceptron
from utils.all_utils import prepare_data, save_plot, save_model
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main(data,eta,epochs,filename,plot_filename):
    
    df = pd.DataFrame(data)
    print(df)
    X,y = prepare_data(df)

    model = Perceptron(eta = eta, epochs = epochs)
    model.fit(X , y)

    _ = model.total_loss()

    save_model(model,filename)
    save_plot(df,plot_filename,model)

if __name__ == '__main__':   # entry point
    
    OR = {
        "x1": [0,0,1,1],
        "x2": [0,1,0,1],
        "y": [0,1,1,1]
    }

    ETA = 0.3
    EPOCHS = 10

    main(data=OR,eta=ETA,epochs=EPOCHS,filename="or.model",plot_filename="or.png")

