'''
Created on Oct 12, 2015 5:36:27 PM
@author: cx

what I do:

what's my input:

what's my output:


'''






import gzip
import json

from KgIRBase.KeyBasedFileReader import KeyBasedFileReaderC
 
class FreebaseDumpReaderC(KeyBasedFileReaderC):
    
    
    def Init(self):
        super(FreebaseDumpReaderC,self).Init()
        self.UseGzip = True #always
    
            
    def ReadNextKey(self):
        lvCol = super(FreebaseDumpReaderC,self).ReadNextKey()
        lvCol = [self.ProcessOneLine(vCol) for vCol in lvCol]
        return lvCol
        
    def ProcessOneLine(self,vCol):
        if len(vCol) < 3:
            return []
#         print "processing %s" %(json.dumps(vCol))
#        vCol = [DiscardPrefix(col) for col in vCol[:3]]      
        return vCol
        
    
    