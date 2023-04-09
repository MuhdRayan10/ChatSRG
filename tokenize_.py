from gensim.corpora import TextCorpus
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('filepath')
args = parser.parse_args()

# base_path = os.getcwd()
base_path = ""

def store(corpus):
    store_path = os.path.join(base_path, './data/tokenized/')
    if not os.path.exists(store_path):
        os.mkdir(store_path)

    print(corpus)

    text = ""
    for text_ in corpus.get_texts():
        print(text_)
        text += ' '.join(text_) + "\n"

    print(text)
    filename = (args.filepath.split('\\')[-1]).split('.')[0]
    
    with open(os.path.join(store_path, f"{filename}.txt"), 'w') as f:
        f.write(text)

# tokenize the data
corpus = TextCorpus(args.filepath)
store(corpus)
