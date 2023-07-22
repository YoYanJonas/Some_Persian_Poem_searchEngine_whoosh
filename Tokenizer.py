import Hazm
import Parsivar
from whoosh.analysis import StandardAnalyzer
from StopWordGetter import StopWords

def SE0(input) :
    Standard_Analyzer = StandardAnalyzer()
    tokenized_list = [token.text for token in Standard_Analyzer(input)]
    return tokenized_list

def SE1(input) :
    Standard_Analyzer = StandardAnalyzer()
    string = Hazm.H_normalizer(input)
    tokenized_list = [token.text for token in Standard_Analyzer(string)]
    return tokenized_list

def SE1_2(input) :
    Standard_Analyzer = StandardAnalyzer()
    string = Parsivar.P_normalizer(input)
    tokenized_list = [token.text for token in Standard_Analyzer(string)]
    return tokenized_list

def SE2(input) :
    stop = StopWords()
    Standard_Analyzer = StandardAnalyzer(stoplist=frozenset(stop))
    string = Hazm.H_normalizer(input)
    tokenized_list = [token.text for token in Standard_Analyzer(string)]
    return tokenized_list

def SE2_2(input) :
    stop = StopWords()
    Standard_Analyzer = StandardAnalyzer(stoplist=frozenset(stop))
    string = Parsivar.P_normalizer(input)
    tokenized_list = [token.text for token in Standard_Analyzer(string)]
    return tokenized_list

def SE3(input) :
    stop = StopWords()
    Standard_Analyzer = StandardAnalyzer(stoplist=frozenset(stop))
    string = Hazm.H_normalizer(input)
    tokenized_list = [Hazm.H_lemmatizer(token.text) for token in Standard_Analyzer(string)]
    return tokenized_list

def SE3_2(input) :
    stop = StopWords()
    Standard_Analyzer = StandardAnalyzer(stoplist=frozenset(stop))
    string = Parsivar.P_normalizer(input)
    tokenized_list = [Parsivar.P_Stemmer(token.text) for token in Standard_Analyzer(string)]
    return tokenized_list

def SE4(input) :
    stop = StopWords()
    Standard_Analyzer = StandardAnalyzer()
    string = Hazm.H_normalizer(input)
    tokenized_list = [Hazm.H_stemmer(token.text) for token in Standard_Analyzer(string)]
    return tokenized_list

def SE4_2(input) :
    stop = StopWords()
    Standard_Analyzer = StandardAnalyzer(stoplist=frozenset(stop))
    string = Hazm.H_normalizer(input)
    tokenized_list = [Hazm.H_stemmer(token.text) for token in Standard_Analyzer(string)]
    return tokenized_list