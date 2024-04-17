import torch
import torch.optim as optim
import torch.nn as nn
import time

from vocabulary.vocabulary import Vocab
from model.model_RNN import RNN
from dataset.data_loader.data_loader import data_loader
from dataset.IMDB.IMDBDataset import IMDBDataset


# CÁC HÀM CẦN THIẾT #
def binary_accuracy(preds, y):
    """
    Trả về acc trên batch, nếu model đúng 8/10 => 0.8
    :param preds: (torch.Tensor) shape = [batch_size]
    :param y: (torch.Tensor) shape = [batch_size]
    :return: accuracy (torch.Tensor) shape = [1]
    """
    # Làm tròn predicted
    rounded_preds = torch.round(torch.sigmoid(preds))
    correct = (rounded_preds == y).float()
    acc = correct.sum() / len(correct)

    return acc


def train(model, dataloader, optimizer, criterion, device):
    """
    :param model: RNN/Transformer
    :param dataloader: DataLoader
    :param optimizer: Adam
    :param criterion: BCEWithLogitsLoss
    :param device: GPU/CPU
    :return: epoch_loss(float): loss của model trên mỗi epoch
    :return: epoch_acc(float): accuracy của model trên mỗi epoch
    """

    epoch_loss = 0
    epoch_acc = 0

    model.train()

    for batch in dataloader:
        optimizer.zero_grad()
        reviews, reviews_length = batch["reviews"]
        reviews = reviews.to(device)

        predictions = model(reviews, reviews_length).squeeze(1)
        sentiments = batch["sentiments"].to(device)
        loss = criterion(predictions, sentiments)
        acc = binary_accuracy(predictions, sentiments)

        loss.backward()
        optimizer.step()

        epoch_loss += loss.item()
        epoch_acc += acc.item()

    batch_num = len(dataloader)

    return epoch_loss / batch_num, epoch_acc / batch_num


def evaluate(model, dataloader, criterion, device):
    """
    :param model: RNN/Transformer
    :param dataloader: DataLoader
    :param criterion: BCEWithLogitsLoss
    :param device: GPU/CPU
    :return: epoch_loss(float): loss của model trên mỗi epoch
    :return: epoch_acc(float): accuracy của model trên mỗi epoch
    """
    epoch_loss = 0
    epoch_acc = 0

    model.eval()

    with torch.no_grad():
        for batch in dataloader:
            reviews, reviews_length = batch["reviews"]
            reviews = reviews.to(device)

            predictions = model(reviews, reviews_length).squeeze(1)
            sentiments = batch["sentiments"].to(device)
            loss = criterion(predictions, sentiments)
            acc = binary_accuracy(predictions, sentiments)

            epoch_loss += loss.item()
            epoch_acc += acc.item()

    batch_num = len(dataloader)

    return epoch_loss / batch_num, epoch_acc / batch_num


def epoch_time(start_time, end_time):
    elapsed_time = end_time - start_time
    elapsed_mins = int(elapsed_time / 60)
    elapsed_secs = int(elapsed_time - (elapsed_mins * 60))
    return elapsed_mins, elapsed_secs


# TRAIN MODEL #

# Load word_embedding có sẵn
word_embedding = torch.load("../dataset/data/vi_word2vec.pt")

# Tạo vocab => add word_embedding vào vocab
vocab = Vocab()
vocab.run_add_vocab(word_embedding)

# Khai báo biến
INPUT_DIM, EMBEDDING_DIM = word_embedding[2].shape
BATCH_SIZE = 100
HIDDEN_DIM = 256
N_LAYERS = 2
BIDIRECTIONAL = True
DROPOUT = 0.5
PAX_IDX = vocab['<pad>']
UKN_IDX = vocab['<unk>']
N_EPOCHS = 10

# Load data => {"reviews": (reviews, reviews_length), "sentiments": sentiments}
train_dataloader, val_dataloader, test_dataloader = data_loader(vocab, IMDBDataset, BATCH_SIZE)

# Tạo model
model = RNN(INPUT_DIM,
            EMBEDDING_DIM,
            HIDDEN_DIM,
            N_LAYERS,
            BIDIRECTIONAL,
            DROPOUT,
            PAX_IDX)

# Add word_embedding có sẵn/pad embedding/unknown embedding vào model embedding
model.embedding.weight.data.copy_(word_embedding[2])
model.embedding.weight.data[UKN_IDX] = torch.zeros(EMBEDDING_DIM)
model.embedding.weight.data[PAX_IDX] = torch.zeros(EMBEDDING_DIM)

print(f'Model parameter: {sum(p.numel() for p in model.parameters() if p.requires_grad):,}')

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
optimizer = optim.Adam(model.parameters())
criterion = nn.BCEWithLogitsLoss().to(device)

model = model.to(device)

best_valid_loss = float("inf")

# Training model
for epoch in range(N_EPOCHS):
    start_time = time.time()

    train_loss, train_acc = train(model, train_dataloader, optimizer, criterion, device)
    valid_loss, valid_acc = evaluate(model, val_dataloader, criterion, device)

    end_time = time.time()

    epoch_mins, epoch_secs = epoch_time(start_time, end_time)

    if valid_loss < best_valid_loss:
        best_valid_loss = valid_loss
        torch.save(model.state_dict(), "model_RNN.pt")

    print(f"Epoch: {epoch + 1:02} | Epoch Time: {epoch_mins}m {epoch_secs}s")
    print(f"\tTrain Loss: {train_loss:.3f} | Train Acc: {train_acc * 100:.2f}")
    print(f"\tValidation Loss: {valid_loss:.3f} | Validation Acc: {valid_acc * 100:.2f}")
