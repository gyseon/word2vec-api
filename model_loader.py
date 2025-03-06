from gensim.models import KeyedVectors


def load_model():
    return KeyedVectors.load_word2vec_format("ko_word2vec.bin", binary=True)
