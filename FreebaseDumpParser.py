'''
Created on Oct 12, 2015 5:49:26 PM
@author: cx

what I do:
    i parse the freebase dump lines readed by FreebaseDumpReader
what's my input:

what's my output:


'''


import json

class FbDumpOpeC(object):
    def __init__(self):
        self.TypeEdge = "<http://rdf.freebase.com/ns/type.object.type>"
        self.DespEdge = "<http://rdf.freebase.com/ns/common.topic.description>"
        self.NameEdge = "<http://www.w3.org/2000/01/rdf-schema#label>"
        self.AliasEdge = "<http://rdf.freebase.com/ns/common.topic.alias>"
        self.NotableEdge = "<http://rdf.freebase.com/ns/common.topic.notable_types>"
        self.InstanceEdge = "<http://rdf.freebase.com/ns/type.type.instance>"
        self.lWikiUrlEdge = ["<http://rdf.freebase.com/ns/common.topic.topic_equivalent_webpage>","<http://rdf.freebase.com/ns/common.topic.topical_webpage>"]
        self.WikiEnIdEdge = '<http://rdf.freebase.com/key/wikipedia.en_id>'
    @staticmethod
    def GetObjId(lvCol):
        if lvCol == []:
            return ""
        return FbDumpOpeC.GetIdForCol(lvCol[0][0])        
    
    @staticmethod
    def DiscardPrefix(col):
        if len(col) < 2:
            return col
        if (col[0] != '<') | (col[len(col) - 1] !=">"):
            return col    
        mid = col.strip("<").strip(">")
        vCol = mid.split("/")
        target = vCol[len(vCol)-1]
        return '/' + target.replace('.','/')
    
    @staticmethod
    def GetIdForCol(col):
        target = FbDumpOpeC.DiscardPrefix(col)
        if len(target) < 2:
            return ""
        if (target[:len('/m/')] == "/m/") | (target[:len('/en/')]=='/en/'):
            return target
        return ""
    
    @staticmethod
    def FetchTargetsWithEdge(lvCol,Edge):
        '''
        fetch col with edge (obj edge col)
        '''
        lTar = []
        for vCol in lvCol:
            if vCol[1] == Edge:
                lTar.append(vCol[2])

        return lTar
    
    @staticmethod
    def FetchTargetStringWithEdge(lvCol,Edge):
        '''
        same, but only look for english strings
        '''
        lTar = FbDumpOpeC.FetchTargetsWithEdge(lvCol, Edge)        
#         print 'curent obj:%s' %(json.dumps(lvCol))
#         print 'edge [%s] get targets [%s]' %(Edge,json.dumps(lTar))
        lStr = []
        for tar in lTar:
            if not FbDumpOpeC.IsString(tar):
                continue
            text,tag = FbDumpOpeC.SegLanguageTag(tar)
            if (tag == "") | (tag == 'en'):
                lStr.append(text)
#         print 'get text [%s]' %(json.dumps(lStr))
        return lStr
    
    
    
    
    def GetName(self,lvCol):
        lStr = self.FetchTargetStringWithEdge(lvCol, self.NameEdge)
        if [] == lStr:
            return ""
        return lStr[0]
    
    def GetAlias(self,lvCol):
        return self.FetchTargetStringWithEdge(lvCol, self.AliasEdge)
    
    def GetDesp(self,lvCol):
        return '\n'.join(self.FetchTargetStringWithEdge(lvCol, self.DespEdge))
    
    def GetWikiId(self,lvCol):
        lWikiId = self.FetchTargetStringWithEdge(lvCol, self.WikiEnIdEdge)
        if [] == lWikiId:
            return ""
        return lWikiId[0]
    
    def GetNeighbor(self,lvCol):
        lNeighbor = []
        for vCol in lvCol:
            NeighborId = self.GetIdForCol(vCol[2])
            if "" != NeighborId:
                NeighborEdge = self.DiscardPrefix(vCol[1])
                lNeighbor.append([NeighborEdge,NeighborId])
        return lNeighbor
    
    def GetWikiUrl(self,lvCol):
        lWikiUrl = []
        for edge in self.lWikiUrlEdge:
            lTar = self.FetchTargetsWithEdge(lvCol, edge)
#             if [] != lTar:
#                 print 'wiki target %s' %(json.dumps(lTar))
            
            for tar in lTar:
                if not 'http' in tar:
                    continue
                if not 'en.wikipedia' in tar:
                    continue
                lWikiUrl.append(tar.strip('<').strip('>'))
#         if [] != lWikiUrl:
#             print 'wikiurl: %s' %(json.dumps(lWikiUrl))
        return lWikiUrl
    
    def GetType(self,lvCol):
        lTar = self.FetchTargetsWithEdge(lvCol, self.TypeEdge)
        lType = []
        for tar in lTar:
            Type = self.DiscardPrefix(tar)
#             if '/common' == Type[:len('/common')]:
#                 continue          
            lType.append(Type)
        return lType
    
    def GetNotable(self,lvCol):
        lTar = self.FetchTargetsWithEdge(lvCol, self.NotableEdge)
        if [] == lTar:
            return ""
        return self.DiscardPrefix(lTar[0]) 
        
    