import torch
import torch.optim as optim
import torch.nn as nn

from dataset.IMDB.IMDBDataset import IMDBDataset
from dataset.data_loader.data_loader import data_loader
from train.training import run_epoch
from vocabulary.vocabulary import Vocab


def predict_sentiment(model, sentence, vocab, device):
    model.eval()
    corpus = [sentence]
    tensor = vocab.corpus_to_tensor(corpus)[0].to(device)
    tensor = tensor.unsqueeze(1)
    length = [len(tensor)]
    length_tensor = torch.LongTensor(length)
    input = (tensor, length_tensor)
    prediction = torch.sigmoid(model(input))

    return prediction.item()


# Load word_embedding có sẵn
word_embedding = torch.load("../dataset/data/vi_word2vec.pt")

# Tạo vocab => add word_embedding vào vocab
vocab = Vocab()
vocab.run_add_vocab(word_embedding)

_, _, test_dataloader = data_loader(vocab, IMDBDataset, 100)

model = torch.load()
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
optimizer = optim.Adam(model.parameters())
criterion = nn.BCEWithLogitsLoss().to(device)

# Testing model

test_loss, test_acc = run_epoch(model=model, dataloader=test_dataloader,
                                device=device, criterion=criterion,
                                optimizer=None, is_training=False)

print(f'Test Loss: {test_loss:.3f} | Test Acc: {test_acc * 100:.2f}%')

sentence_1 = "Bộ phim rất hay! Nội dung cực kì lôi cuốn!"
sentence_2 = "Bộ phim tệ hại! Nội dung cực kì dỡ!"

print(f"Câu 1: {predict_sentiment(model, sentence_1, vocab, device)}")
print(f"Câu 2: {predict_sentiment(model, sentence_2, vocab, device)}")
