import torch
import time


# Lấy embedding vector của 1 từ
def get_vector(embeddings, word):
    """
    @param embeddings (torchtext.vocab.vectors.Vectors)
    @param word (str)
    @return vector (torch.Tensor)
    """
    word_idx = embeddings[1][word]

    assert word in embeddings[0], f'*{word}* is not in the vocab!'
    return embeddings[2][word_idx]


# # Trả về list words gần nghĩa với word
def closest_word(embeddings, vector, n=10):
    """
    @param embeddings (torchtext.vocab.vectors.Vectors)
    @param vector (torch.Tensor)
    @param n (int)
    @return words (list(tuple(str, float)))
    """
    distances = [(word, torch.dist(vector, get_vector(embeddings, word))) for word in embeddings[0][:1000]]
    print("Running done!")

    return sorted(distances, key=lambda w: w[1])[:n]


# Load file vector pretrained word2vec
start = time.time()
word_embedding = torch.load("../dataset/data/vi_word2vec.pt")
end = time.time()

# Location: 0-words, 1-words:index, 2-Tensor
print(len(word_embedding[0]))
print(len(word_embedding[1]))
print(word_embedding[2].shape)
print(f"Time running: {end - start}")
# word2vec = get_vector(word_embedding, "Việt_Nam")
# print("Running...")
# print(closest_word(word_embedding, word2vec))
