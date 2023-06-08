import torch
import torch.nn as nn
import data_provider
import torchvision
import torch.optim as optim
import numpy

# load data --------------------------------------------------------------------
file = open("dataset.txt", "r")
data = []
for line in file.readlines():
    data.append([float(line.split()[0]), float(line.split()[1])])

file.close()
print(data)

# build NN ---------------------------------------------------------------------
dev = torch.device("cpu")
print(dev)

input_len = 8
model = nn.Sequential(
    nn.Linear(input_len * 2, 4096),
    nn.ReLU(),
    nn.Linear(4096, 1024),
    nn.ReLU(),
    nn.Linear(1024, 512),
    nn.ReLU(),
    nn.Linear(512, input_len * 2)
)

model = torch.load("model.pth")
model.eval()

optimizer = optim.SGD(model.parameters(), lr=0.0000001)

buf = 0
cutoff = 0.01
for i in range(1000):
    data_in, data_out = data_provider.get_set(data, input_len)

    data_in = torch.flatten(torch.tensor(data_in))
    data_out = torch.flatten(torch.tensor(data_out))

    output = model.forward(data_in)
    optimizer.zero_grad()
    loss = nn.MSELoss()(output, data_out)
    buf += cutoff * (loss - buf)
    loss.backward()
    optimizer.step()
    print("loss:", buf)

torch.save(model, "model.pth")