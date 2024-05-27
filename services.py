import torch

from model.model_RNN import RNN
from vocabulary.vocabulary import Vocab


def sent_analysis_service(sentence):
    word_embedding = torch.load("./dataset/data/vi_word2vec.pt")
    vocabulary = Vocab()
    vocabulary.run_add_vocab(word_embedding)

    file_model = "./save_model/model_RNN.pth"

    def predict_sentiment(Model, path_model, sentence, vocab):
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        INPUT_DIM, EMBEDDING_DIM = word_embedding[2].shape
        HIDDEN_DIM = 256
        N_LAYERS = 2
        BIDIRECTIONAL = True
        DROPOUT = 0.5
        PAX_IDX = vocab['<pad>']

        model = Model(INPUT_DIM,
                      EMBEDDING_DIM,
                      HIDDEN_DIM,
                      N_LAYERS,
                      BIDIRECTIONAL,
                      DROPOUT,
                      PAX_IDX)

        model.load_state_dict(torch.load(path_model))
        model.to(device)
        model.eval()

        corpus = [sentence]
        tensor = vocab.corpus_to_tensor(corpus)[0].to(device)
        tensor = tensor.unsqueeze(1)
        length = [len(tensor)]
        length_tensor = torch.LongTensor(length)
        input = (tensor, length_tensor)
        prediction = torch.sigmoid(model(input))

        return prediction.item()

    pred = predict_sentiment(RNN, file_model, sentence, vocabulary)

    return pred
