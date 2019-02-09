import wx
import time

class MyFrame(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title, size=(400,400))
        self.control = wx.Button(self)
        self.CreateStatusBar()

        filemenu = wx.Menu()

        menuAbout = filemenu.Append(wx.ID_ABOUT,"&About","Information about this program")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        self.Bind(wx.EVT_MENU,self.OnAbout,menuAbout)
        self.Bind(wx.EVT_MENU,self.OnExit,menuExit)

        menuBar=wx.MenuBar()
        menuBar.Append(filemenu,"&File")
        self.SetMenuBar(menuBar)
        self.Show(True)

    def OnAbout(self,event):
        dl = wx.MessageDialog(self, "A small text editor", "About Sample Editor",wx.OK)
        dl.ShowModal()
        dl.Destroy()

    def OnExit(self,e):
        self.Close(True)

app = wx.App(False)
frame = MyFrame(None, 'Small Editor')
app.MainLoop()