import pandas as pd
import torch
from torch.utils.data import Dataset
from vocabulary import vocabulary

# from scipy.linalg.special_matrices import dft


class IMDBDataset(Dataset):
    # Load dataset từ file csv
    def __init__(self, vocab, csv_fpath=None, tokenized_fpath=None):
        """
        @param vocab (vocabulary)
        @param csv_fpath (str)
        @param tokenized_fpath (str)
        """
        self.vocab = vocab
        self.pad_idx = vocab['<pad>']
        df = pd.read_csv(csv_fpath)
        self.sentiments_list = list(df.sentiment)
        self.reviews_list = list(df.vi_review)

        # Lưu nhãn cảm xúc trong dataset -> {'negative': 0, 'positive': 1}
        sentiment_type = list(set(self.sentiments_list))
        sentiment_type.sort()

        # Chuyển nhãn thành index
        self.sentiment2id = {sentiment: i for i, sentiment in enumerate(sentiment_type)}

        # Nếu có file tokenized sẵn -> load file
        if tokenized_fpath:
            self.tokenized_reviews = torch.load(tokenized_fpath)
        else:
            self.tokenized_reviews = self.vocab.tokenize_corpus(self.reviews_list)

        # Chuyển token -> Tensor[idx_token]
        self.tensor_data = self.vocab.corpus_to_tensor(self.tokenized_reviews, is_tokenized=True)

        # Chuyển label -> Tensor[idx_label]
        self.tensor_label = torch.tensor([self.sentiment2id[sentiment] for sentiment in self.sentiments_list],
                                         dtype=torch.float64)

    # Trả về [Tensor data], [Tensor label]
    def __getitem__(self, idx):
        return self.tensor_data[idx], self.tensor_label[idx]

    def __len__(self):
        return len(self.tensor_data)

    def collate_fn(self, examples):
        examples = sorted(examples, key=lambda e: len(e[0]), reverse=True)

        reviews = [e[0] for e in examples]
        reviews = torch.nn.utils.rnn.pad_sequence(reviews, batch_first=False, padding_value=self.pad_idx)

        reviews_length = torch.tensor([len(e[0] for e in examples)])
        sentiments = torch.tensor([e[1] for e in examples])

        return {"reviews": (reviews, reviews_length), "sentiments": sentiments}


if __name__ == "__main__":
    vocab = vocabulary.Vocab()
    vocab.run_add_vocab("../data/vi_word2vec.pt")

    dataset = IMDBDataset(vocab, "../data/VI_IMDB.csv", "../data/tokenized_reviews.pt")

    print(dataset[:5])

    # Run để tạo dataset và lưu vào file tokenized.pt -> Mất khoảng 15p
    # dataset = IMDBDataset(vocab, "../VI_IMDB.csv")
    # torch.save(dataset.tokenized_reviews, "../data/tokenized.pt")
