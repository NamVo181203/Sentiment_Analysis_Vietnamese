import torch
import torch.nn as nn

from vocabulary.vocabulary import Vocab


class RNN(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, n_layers, bidirectional, dropout, pax_idx):
        """
        :param vocab_size: size của vocab(int)
        :param embedding_dim: dimension embedding(int)
        :param hidden_dim: dimension hidden(int)
        :param n_layers: số layer(int)
        :param bidirectional: x2(bool)
        :param dropout: tỉ lệ bỏ học(float
        :param pax_idx:
        """
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim, padding_idx=pax_idx)

        self.rnn = nn.LSTM(embedding_dim,
                           hidden_dim,
                           num_layers=n_layers,
                           bidirectional=bidirectional,
                           dropout=dropout)

        self.fc = nn.Linear(hidden_dim * 2, 1)

        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        """
        :param text: shape[sent len, batch size]
        :param text_lengths: shape[batch size]
        :return:
        """
        (text, text_lengths) = x
        # text = [sent len, batch size]
        embedded = self.dropout(self.embedding(text))
        # embedded = [sent len, batch size, emb dim]

        # Hàm pack_padded_sequence =? bỏ qua các vị trí <pad>
        packed_embedded = nn.utils.rnn.pack_padded_sequence(embedded, text_lengths.to('cpu'))

        packed_output, (hidden, cell) = self.rnn(packed_embedded)

        output, output_lengths = nn.utils.rnn.pad_packed_sequence(packed_output)
        # output = [sent len, batch size, hid dim * num directions]
        # output over padding tokens are zero tensors

        # hidden = [num layers * num directions, batch size, hid dim]
        # cell = [num layers * num directions, batch size, hid dim]

        # concat the final forward (hidden[-2,:,:]) and backward (hidden[-1,:,:]) hidden layers
        # and apply dropout

        hidden = self.dropout(torch.cat((hidden[-2, :, :], hidden[-1, :, :]), dim=1))

        # hidden = [batch size, hid dim * num directions]

        return self.fc(hidden)


if __name__ == "__main__":
    word_embedding = torch.load("../dataset/data/vi_word2vec.pt")
    vocab = Vocab()
    INPUT_DIM, EMBEDDING_DIM = word_embedding[2].shape
    BATCH_SIZE = 100
    HIDDEN_DIM = 256
    N_LAYERS = 2
    BIDIRECTIONAL = True
    DROPOUT = 0.5
    PAX_IDX = vocab['<pad>']
    UKN_IDX = vocab['<unk>']

    model = RNN(INPUT_DIM,
                EMBEDDING_DIM,
                HIDDEN_DIM,
                N_LAYERS,
                BIDIRECTIONAL,
                DROPOUT,
                PAX_IDX)

    model.embedding.weight.data.copy_(word_embedding[2])
    model.embedding.weight.data[UKN_IDX] = torch.zeros(EMBEDDING_DIM)
    model.embedding.weight.data[PAX_IDX] = torch.zeros(EMBEDDING_DIM)

    print(f'Model parameter: {sum(p.numel() for p in model.parameters() if p.requires_grad):,}')
