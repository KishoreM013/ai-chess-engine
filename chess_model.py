from torch import nn

class ChessAI(nn.Module):

    def __init__(self, num_classes):
        super(ChessAI, self).__init__()
        self.conv1 = nn.Conv2d(13, 64, kernel_size=3, padding= 1)
        self.conv2 = nn.Conv2d(64, 128, kernel_size=3, padding= 1)
        self.relu = nn.ReLU()
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(8*8*128, 256)
        self.fc2 = nn.Linear(256, num_classes)

        nn.init.kaiming_uniform_(self.conv1.weight, nonlinearity='relu')
        nn.init.kaiming_uniform_(self.conv2.weight, nonlinearity='relu')
        nn.init.xavier_uniform_(self.fc1.weight)
        nn.init.xavier_uniform_(self.fc2.weight)
        
    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.conv2(x)
        x = self.relu(x)
        x = self.flatten(x)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
        