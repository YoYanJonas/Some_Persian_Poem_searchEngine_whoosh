from Assesments import Assesment_reader
from Engine import index_search

def Tester():
    AvgPrecision=0
    tests= Assesment_reader()
    TP,FP,FN=0,0,0
    for test in tests:
        tp,fp,fn,AvgPrecision=0,0,0,0
        realOutput = index_search("SE0", ['body','doc'], test[0])
        expectedOutput = test[1]
        for result in expectedOutput:
            if result in realOutput :
                tp+=1
                realOutput.remove(result)
            else:
                fn+=1
        fp +=  len(realOutput)
        AvgPrecision+= tp / (tp+fp)
        print(tp / (tp+fp))
        FP+=fp
        TP+=tp
        FN+=fn
    Percision = TP / (TP+FP)
    Recall = TP / (TP +FN)
    FMeasure = (2*Percision*Recall/Percision+Recall)
    avgPercision /= len(tests)
    return (Percision,Recall,FMeasure,AvgPrecision)
    
print(Tester())