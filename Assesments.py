def Assesment_reader():
    RAPath= "./RelevanceAssesment/RelevanceAssesment"
    QuertyPath = './Queries/'
    RAFile = open(RAPath, encoding="utf8")
    Tests = RAFile.read().split('\n\n')
    DefaultQdMatch = []
    for test in Tests[:-1] :
        testList = test.split('\n')
        QueryFile = open(QuertyPath +testList[0], encoding="utf8")
        Query = QueryFile.read()
        resultList = testList[1].split(' ')
        DefaultQdMatch.append((Query,resultList))
    return DefaultQdMatch


