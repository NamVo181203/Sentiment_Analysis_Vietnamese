import torch

word_embedding = torch.load("./dataset/data/vi_word2vec.pt")

print(word_embedding[2].shape)
