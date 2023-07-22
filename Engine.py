import os
from whoosh import index
from whoosh.filedb.filestore import FileStorage
from whoosh.fields import Schema, TEXT
from whoosh import qparser
from hazm import *
import Tokenizer


def indexing(str):
    pnames = os.listdir('./Poems')
    schema = Schema(body=TEXT(stored=True), doc=TEXT(stored=True))
    if not os.path.exists(str):
        os.mkdir(str)
        storage = FileStorage(str)
        ix = storage.create_index(schema)
        ix = storage.open_index()
        writer = ix.writer()
        print('indexing...\n')
        i = 0
        for doc in pnames:
            with open('./Poems/'+doc, encoding="utf8") as fh:
                if str=="SE0":
                    tokenized_list = Tokenizer.SE0(fh.read())
                elif str=="SE1":
                    tokenized_list = Tokenizer.SE1(fh.read())
                elif str=="SE1_2":
                    tokenized_list = Tokenizer.SE1_2(fh.read())
                elif str=="SE2":
                    tokenized_list = Tokenizer.SE2(fh.read())
                elif str=="SE2_2":
                    tokenized_list = Tokenizer.SE2_2(fh.read())
                elif str=="SE3":
                    tokenized_list = Tokenizer.SE3(fh.read())
                elif str=="SE3_2":
                    tokenized_list = Tokenizer.SE3_2(fh.read())
                elif str=="SE4":
                    tokenized_list = Tokenizer.SE4(fh.read())
                elif str=="SE4_2":
                    tokenized_list = Tokenizer.SE4_2(fh.read())
                os.system('cls')
                writer.add_document(body=tokenized_list, doc=doc)
                i = i + 1
                print(doc)       
                print(f"Indexing...\n{i}/{len(pnames)} indexed...")
        writer.commit()
    print('Done!')


def index_search(dirname, search_fields, search_query):
    indexing(dirname)
    ix = index.open_dir(dirname)
    schema = ix.schema    
    og = qparser.OrGroup.factory(0.9)
    mp = qparser.MultifieldParser(search_fields, schema, group = og)
    if dirname=="SE0":
        tokenized_list = Tokenizer.SE0(search_query)
    elif dirname=="SE1":
        tokenized_list = Tokenizer.SE1(search_query)
    elif dirname=="SE1_2":
        tokenized_list = Tokenizer.SE1_2(search_query)
    elif dirname=="SE2":
        tokenized_list = Tokenizer.SE2(search_query)
    elif dirname=="SE2_2":
        tokenized_list = Tokenizer.SE2_2(search_query)
    elif dirname=="SE3":
        tokenized_list = Tokenizer.SE3(search_query)
    elif dirname=="SE3_2":
        tokenized_list = Tokenizer.SE3_2(search_query)
    elif dirname=="SE4":
        tokenized_list = Tokenizer.SE4(search_query)
    elif dirname=="SE4_2":
        tokenized_list = Tokenizer.SE4_2(search_query)
    parsedQuery = ' '.join(tokenized_list)
    q = mp.parse(parsedQuery)    
    with ix.searcher() as s:
        results = s.search(q, terms=True, limit = 17)
        resultNames = [] 
        for result in results[:]:       
            resultNames.append(result.items()[1][1])
        return resultNames
        
results_dict = index_search("SE3_2", ['body','doc'], "مگس تولیدن شیر")
print(results_dict)