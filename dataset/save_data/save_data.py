import torch
import torchtext.vocab as tt_vocab
import time

start = time.time()
word_embedding = tt_vocab.Vectors(name="../dataset/vi_word2vec.txt", cache="../dataset/vi_word2vec.pt", unk_init=torch.Tensor.normal_)
end = time.time()

print(word_embedding.vectors.shape)
print(f"Time running save data: {end - start}")
