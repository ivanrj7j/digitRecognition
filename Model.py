import torch
import torch.nn as nn
import time 
import numpy as np


def accuracy(yhat, y):
    return round((np.array(torch.argmax(yhat, 1)) == np.array(torch.argmax(y, 1))).astype(np.uint8).sum() / yhat.shape[0] * 100, 2)

class ImageRecogniser(nn.Module):
    def __init__(self) -> None:
        super(ImageRecogniser, self).__init__()
        self.layer1 = nn.Linear(784, 100)
        self.layer2 = nn.Linear(100, 10)
        # 3 layers 
    
    def forward(self, x):
        x = torch.relu(self.layer1(x))
        x = torch.softmax(self.layer2(x), 1)
        return x
    
    def train(self, labels:torch.Tensor, features:torch.Tensor, learningRate=0.05, epochs=250, batchsize=2000):
        if labels.shape[0] != features.shape[0]:
            raise IndexError("The number of label samples should match feature sample")
        self.optimizer = torch.optim.SGD(self.parameters(), lr=learningRate)
        self.criterion = torch.nn.CrossEntropyLoss()
        
        startTime = time.time()

        for epoch in range(epochs):
            trainLoss = 0
            epochStart = time.time()
            for i in range(0, labels.shape[0], batchsize):
                X = features[i: i+batchsize]
                Y = labels[i:i+batchsize]

                self.optimizer.zero_grad()
                # clearing the gradinets 

                target = self(X)
                # forward pass 

                loss = self.criterion(target, Y)
                # calculating loss 

                loss.backward()
                # back propogation 

                self.optimizer.step()
                # updating values 

                trainLoss += loss.item()
                
                print(f'[Epoch {epoch+1} Batch {(i/batchsize) + 1}] \t\t Training Loss: {trainLoss / len(Y)}', end='\r')
            
            print(f'[Epoch {epoch+1}]\t\t Training Loss: {trainLoss / len(Y)} \t {round(time.time()-epochStart, 1)} secs  \t accuracy: {accuracy(target, Y)} \t test accuracy: {accuracy(self(testfeatures[:450]), testlabels[:450])}')
        print(f"Training took {(time.time()-startTime) / 60} minutes")