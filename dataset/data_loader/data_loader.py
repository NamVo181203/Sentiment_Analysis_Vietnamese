import torch
from torch.utils.data import random_split
from torch.utils.data import DataLoader

from vocabulary.vocabulary import Vocab
from dataset.IMDB.IMDBDataset import IMDBDataset


def data_loader(vocab, imdb_dataset, batch_size):
    # Khởi tạo dataset
    dataset = imdb_dataset(vocab, "../data/VI_IMDB.csv", "../data/tokenized_reviews.pt")
    # dataset = imdb_dataset(vocab, "../dataset/data/VI_IMDB.csv", "../dataset/data/tokenized_reviews.pt")

    split_rate = 0.8
    full_size = len(dataset)
    train_size = int(split_rate * full_size)  # 8
    val_size = int((full_size - train_size) / 2)  # 1
    test_size = full_size - train_size - val_size  # 1

    train_dataset, val_dataset, test_dataset = random_split(dataset, lengths=[train_size, val_size, test_size])

    print(f"Train: {len(train_dataset)} | Validation: {len(val_dataset)} | Test: {len(test_dataset)}")

    train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, collate_fn=dataset.collate_fn)
    val_dataloader = DataLoader(val_dataset, batch_size=batch_size, shuffle=True, collate_fn=dataset.collate_fn)
    test_dataloader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, collate_fn=dataset.collate_fn)

    return train_dataloader, val_dataloader, test_dataloader


if __name__ == "__main__":
    word_embedding = torch.load("../data/vi_word2vec.pt")

    # Tạo vocab => add word_embedding vào vocab
    vocab = Vocab()
    vocab.run_add_vocab(word_embedding)

    train_data, val_data, test_datar = data_loader(vocab, IMDBDataset, 100)
