from parsivar import FindStems, Normalizer


my_normalizer = Normalizer()
my_stemmer = FindStems()

def P_Stemmer(input):
    
    return my_stemmer.convert_to_stem(input)

def P_normalizer(input):
    
    return (my_normalizer.normalize(input))
