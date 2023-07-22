from hazm import *





lemmatizer = Lemmatizer()
normalizer = Normalizer()
stemmer = Stemmer()

def H_lemmatizer(input):
    
    return lemmatizer.lemmatize(input)

def H_normalizer(input):
    
    return normalizer.normalize(input)


def H_stemmer(input):
    
    return stemmer.stem(input)
