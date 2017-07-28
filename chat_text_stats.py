textfile = '/chatbot/saschat_final.txt'
lines=0
wordCountLst=[]
mostWordsInLine = -1
fileHandler=open(textfile, 'r')


for lineOfText in fileHandler.readlines():
    lines += 1
    #print(str(lines),str(lineOfText))
    f1=lineOfText.split()
    wordCountLst.append(len(f1))
    if len(f1) > mostWordsInLine:
        mostWordsInLine = len(f1)
    
def median(lst):
    quotient, remainder = divmod(len(lst), 2)
    if remainder:
        return sorted(lst)[quotient]
    return sum(sorted(lst)[quotient - 1:quotient + 1]) / 2.
    
    
print "Mean words per line: {}".format(sum(wordCountLst) / lines)
print "Median words per line: {}".format(median(wordCountLst))
print "Max words in a single line: {}".format(mostWordsInLine)
print "Total lines: {}".format(lines)