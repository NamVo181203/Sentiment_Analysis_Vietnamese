import torch
from tqdm import tqdm
from underthesea import word_tokenize


# Class vocabulary được sử dụng để ghi lại các từ, được sử dụng để chuyển đổi văn bản thành số và ngược lại.
class Vocab:
    def __init__(self):
        self.word2id = dict()
        self.word2id['<pad>'] = 0  # Padding token
        self.word2id['<unk>'] = 1  # Unknown token
        self.unk_id = self.word2id['<unk>']
        self.id2word = {v: k for k, v in self.word2id.items()}

    # Trả về index word bất kì nếu có trong vocab
    def __getitem__(self, word):
        return self.word2id.get(word, self.unk_id)

    # True nếu có word - False nếu không có word trong vocab
    def __contain__(self, word):
        return word in self.word2id

    # Trả về chiều dài của vocab
    def __len__(self):
        return len(self.word2id)

    # Trả về word theo index
    def id2word(self, word_index):
        """
        @param word_index (int)
        @return word (str)
    """
        return self.id2word[word_index]

    # Thêm word vào vocab
    def add(self, word):
        """
        :param word: word(str)
        :return index (str): index của word vừa thêm
        """
        if word not in self.word2id:
            word_index = len(self.word2id)
            self.word2id[word] = word_index
            self.id2word[word_index] = word
            return word_index
        else:
            return self.word2id[word]

    # Tách một document corpus thành các từ
    @staticmethod
    def tokenize_corpus(corpus):
        """
        :param corpus: corpus(list(str)): list của documents
        :return tokenized_corpus (list(list(str))): list của words
        """
        tokenized_corpus = list()
        for document in tqdm(corpus):
            tokenized_document = [word.replace(" ", "_") for word in word_tokenize(document)]
            tokenized_corpus.append(tokenized_document)

        return tokenized_corpus

    # Chuyển corpus thành list của indices tensor
    def corpus_to_tensor(self, corpus, is_tokenized=False):
        """
        @param corpus (list(str)
        @param is_tokenized (bool)
        @return indicies_corpus (list(tensor))
        """
        # Nếu is_tokenized == True -> Không cần tách từ.
        if is_tokenized:
            tokenized_corpus = corpus
        else:
            tokenized_corpus = self.tokenize_corpus(corpus)

        indicies_corpus = list()

        for document in tqdm(tokenized_corpus):
            indicies_document = torch.tensor(list(map(lambda word: self[word], document)), dtype=torch.int64)
            indicies_corpus.append(indicies_document)

        return indicies_corpus

    # Chuyển list của indices tensor thành list của tokenized documents
    def tensor_to_corpus(self, tensor):
        """
        @param indicies_corpus (list(tensor))
        @return corpus (list(list(str)))
        """
        corpus = list()
        for indicies in tqdm(tensor):
            document = list(map(lambda index: self.id2word[index.item()], indicies))
            corpus.append(document)

        return corpus

    def run_add_vocab(self, embedding):
        word_list = list(embedding[0])
        print(embedding[2].shape)
        print("Adding vocab, Wait a minute!")
        for word in tqdm(word_list):
            self.add(word)
        print("Adding vocab complete!")


# Tạo vocab from pretrained word2vec
if __name__ == "__main__":
    word_embedding = torch.load("../dataset/data/vi_word2vec.pt")

    vocab = Vocab()
    vocab.run_add_vocab(word_embedding)

    # print(vocab.word2id)
    # print(vocab.id2word)

    corpus_sample = ["Với cộng đồng người Bách Việt trước đây, việc thuần hóa mèo cũng có thể theo cách thức như vậy."]

    token_corpus = vocab.tokenize_corpus(corpus_sample)
    corpus_tensor = vocab.corpus_to_tensor(token_corpus, is_tokenized=True)
    corpus = vocab.tensor_to_corpus(corpus_tensor)

    # print(f"Tokenize: {token_corpus}")
    print(f"Tensor: {corpus_tensor}")
    # print(f"""Corpus: {" ".join(corpus[0])}""")
