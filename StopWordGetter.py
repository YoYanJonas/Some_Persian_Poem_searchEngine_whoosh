def StopWords():
    stopwordFile = open('./Stopwords/Stopwords', encoding="utf8")
    return frozenset(stopwordFile.read().splitlines())