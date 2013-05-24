import unittest
from Tribler.TUPT.Parser.IMDbParserPlugin import IMDbParserPlugin

class TestIMDbParserPlugin(unittest.TestCase):
    '''Test class to test the IMDbParserPlugin.'''
    
    __result = {'title' : 'The Matrix', 'releaseYear' : 1999, 'director' : ['Andy Wachowski', 'Lana Wachowski']}

    def test_ParseWebsiteCombinedDetails(self):
        '''Test parsing the combined details page'''
        #Arrange
        file = open('test_ParseWebsiteCombinedDetails.html','r')
        html = file.read()
        parser = IMDbParserPlugin()
        #Act
        result = parser.ParseWebSite(html)[0]
        #Assert        
        self.__AssertResult(result)
        
        
    def test_ParseWebsiteMainPage(self):
        '''Test parsing the main details page'''
        #Arrange
        file = open('test_ParseWebsiteMainPage.html','r')
        html = file.read()
        parser = IMDbParserPlugin()
        #Act
        result = parser.ParseWebSite(html)[0]
        #Assert
        self.__AssertResult(result)
       
        
    def __AssertResult(self, result):
       '''Asserts the result for the parser'''
       for key in self.__result:
           self.assertEqual(self.__result[key], result.dictionary[key])
           
if __name__ == '__main__':
    unittest.main()
    
    