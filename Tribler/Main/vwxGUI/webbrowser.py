import wx
import wx.html2

from Tribler.Main.vwxGUI.list import XRCPanel

class WebBrowser(XRCPanel):
    '''WebView is a class that allows you to browse the worldwideweb.'''
    
   
    def __init__(self, parent=None):
        XRCPanel.__init__(self, parent)
        
        vSizer = wx.BoxSizer(wx.VERTICAL)
             
        '''Create the toolbar'''
        toolBar = wx.BoxSizer(wx.HORIZONTAL)
        #Create the toolbar buttons.
        backwardButton = wx.Button(self, label="Backward")
        forwardButton = wx.Button(self, label="Forward")    
        goButton = wx.Button(self, label="Go!")
        #Register the actions
        self.Bind(wx.EVT_BUTTON, self.goBackward, backwardButton)
        self.Bind(wx.EVT_BUTTON, self.goForward, forwardButton)
        self.Bind(wx.EVT_BUTTON, self.loadURLFromAdressBar, goButton)
        #Create the adressbar.
        self.adressBar = wx.TextCtrl(self,1)
        #Add all the components to the toolbar.
        toolBar.Add(backwardButton, 0)
        toolBar.Add(forwardButton, 0)
        toolBar.Add(self.adressBar, 1, wx.EXPAND)
        toolBar.Add(goButton, 0)
        #Add the toolbar to the panel.
        vSizer.Add(toolBar, 0, wx.EXPAND)
        
        '''Create the webview'''
        self.webview = wx.html2.WebView.New(self)
        #Clear the blank page loaded on startup.        
        self.webview.ClearHistory()
        self.webview.LoadURL("http://www.google.com") 
        
        vSizer.Add(self.webview, 1, wx.EXPAND) 
        
        '''Add all components'''
        self.SetSizer(vSizer)
        self.Layout()
        
        '''Register the onLoadAction'''
        self.Bind(wx.html2.EVT_WEB_VIEW_LOADED , self.onLoadURL, self.webview)
        
    def goBackward(self, event):
        if self.webview.CanGoBack():
            self.webview.GoBack()
        
    def goForward(self, event):
        if self.webview.CanGoForward():
            self.webview.GoForward()
    
    def loadURLFromAdressBar(self, event):
        '''Load an URL from the adressbar'''
        url = self.adressBar.GetValue()
        if not url.startswith("http://"):
            url = "http://%s" %url
        self.adressBar.SetValue(url)
        self.webview.LoadURL(url)
        
    def onLoadURL(self, event):
        '''Update the adressbar'''
        self.adressBar.SetValue(self.webview.GetCurrentURL())