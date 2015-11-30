import os, sys
from genQueryDict import readQueryDictionary

class TrecWebFileReaderC(object):
    def Init(self):
        self.InFile = ""
        self.UseGzip = False
        self.Spliter = '\t'
        self.MaxLinePerKey = 1000000

        self.LastDoc = ""
        self.InName = ""

        self.lines = []
        self.FieldBuilder = ["names", "category", "attributes", "SimEn", "RelEn"]

    def __init__(self):
        self.Init()
        

    def open(self,InName,mode = 'r'):
        self.InName = InName
        if self.UseGzip:
            self.InFile = gzip.open(InName,mode)
        else:
            self.InFile = open(InName,mode)
            #self.lines = self.InFile.readlines()
            

    def empty(self):
        return "" == self.InName
            

    def close(self):
        if not self.empty():
            self.InFile.close()
            self.InName = ""


    def write2File(self, docName, docContent, output):
        output.write("<DOC>\n<DOCNO> "+docName+" </DOCNO>\n<DOCHDR>\n"+docName+"\n</DOCHDR>\n")
        for fieldName, fieldContent in docContent.items():
            output.write("<"+fieldName+">\n"+fieldContent+"\n</"+fieldName+">\n")
        output.write("</DOC>\n\n")


    def ReadNextDoc(self):
        Doc = {} #one object's all contents
        content = []
        ThisDoc = ""
        flag = False
        for line in self.InFile:
            if line.find("<DOC>") > -1:
                flag = True
            if flag and line.find("</DOC>") > -1:
                break
            content.append(line.strip())
        #print content
        flag = False
        word = ""
        fieldName = ""
        for item in content:
            if item.find("<DOCNO>") > -1:
                ThisDoc = item.strip().split("<DOCNO>")[1].split("</DOCNO>")[0].strip()
                continue

            for field in self.FieldBuilder:
                if not flag and item.find("<"+field+">") > -1:
                    fieldName = field
                    flag = True
                    word = ""
                    continue
            if flag:
                if item.find("</"+fieldName+">") > -1:
                    flag = False
                    if not word.strip() == "":
                        Doc[fieldName] = word
                    continue
                else:
                    if item.find("<"+fieldName+">") == -1:
                        word += item+" "
        return [ThisDoc, Doc]


    
    def __iter__(self):
        return self
    
    def next(self):
        Doc = self.ReadNextDoc()
        return Doc


if __name__ == "__main__":

    FieldBuilder = ["names", "category", "attributes", "SimEn", "RelEn"]

    # Statistical Param Initialization
    docNum = 0
    fieldInfo = {}
    for field in FieldBuilder:
        fieldInfo[field] = [0, 0]
    #termDict = readQueryDictionary("Path")
    termDict = {'musical': [0, 0], 'groups': [0, 0], 'Overkill': [0, 0]}

    #docNameList = readDocList("Path")

    r = TrecWebFileReaderC()
    r.open("/Users/jane_C/Desktop/data", 'r')
    output = open("/Users/jane_C/Desktop/data.out", 'w')

    '''
    print fieldInfo
    print docList
    print termDict
    '''

    while True:
        res = r.next()
        if res == ['', {}]:
            break
        docName = res[0]
        docContent = res[1]

        # Extract top ranked docs in TrecWebFormat
        #if docName in docNameList:
        #    r.write2File(docName, docContent, output)

        # Statistical Calculation for docnum, terms, fields, etc.
        isExam = {}
        for k, v in termDict.items():
            isExam[k] = False

        docNum += 1
        for fieldName, fieldContent in docContent.items():
            fieldWord = fieldContent.split(" ")
            fieldInfo[fieldName][0] += 1
            fieldInfo[fieldName][1] += len(fieldWord)

            for word in fieldWord:
                word = word.strip('().?!')
                if termDict.has_key(word):
                    if not isExam[word]:
                        termDict[word][0] += 1
                        isExam[word] = True
                    termDict[word][1] += 1

    docInfoOutput = open(docInfoPath, 'w')
    termInfoOutput = open(termInfoPath, 'w')
    docInfoOutput.write(str(docNum)+"\n")
    for k, v in fieldInfo.items():
        docInfoOutput.write2File(k+"\t"+str(v[0])+"\t"+str(v[1])+"\n")
    for k, v in termDict.items():
        termInfoOutput.write(k+"\t"+str(v[0])+"\t"+str(v[1])+"\n")
    docInfoOutput.close()
    termInfoOutput.close()

    #print docNum
    #for k, v in fieldInfo.items():
    #    print k+"\t"+str(v[0])+"\t"+str(v[1])
    #for k, v in termDict.items():
    #    print k+"\t"+str(v[0])+"\t"+str(v[1])


    output.close()
    r.close()