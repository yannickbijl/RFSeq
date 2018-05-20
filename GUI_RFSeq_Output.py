import wx

class GUI_RFSeq_Output(wx.Panel):
    def __init__(self, bb_parent):
        
        wx.Panel.__init__(self, bb_parent, style=wx.BORDER_SUNKEN)
        # Input parameters
        self.fseq = wx.TextCtrl(self, style=wx.TE_READONLY | wx.HSCROLL)
        self.cseq = wx.TextCtrl(self, style=wx.TE_READONLY | wx.HSCROLL)
        self.rf1 = wx.TextCtrl(self, style=wx.TE_READONLY | wx.HSCROLL)
        self.rf2 = wx.TextCtrl(self, style=wx.TE_READONLY | wx.HSCROLL)
        self.rf3 = wx.TextCtrl(self, style=wx.TE_READONLY | wx.HSCROLL)
        self.rf4 = wx.TextCtrl(self, style=wx.TE_READONLY | wx.HSCROLL)
        self.rf5 = wx.TextCtrl(self, style=wx.TE_READONLY | wx.HSCROLL)
        self.rf6 = wx.TextCtrl(self, style=wx.TE_READONLY | wx.HSCROLL)
        
        # Buttons
        self.stop = wx.Button(self, label="Quit")
        self.prev = wx.Button(self, label="Previous")
        
        # Placing of items in frame
        box = wx.BoxSizer(wx.VERTICAL)
        
        box.Add(wx.StaticText(self, label="Forward Sequence:"), 1, wx.EXPAND | wx.ALL)
        box.Add(self.fseq, 1, wx.EXPAND | wx.ALL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(wx.StaticText(self, label="RF1:"), 1, wx.EXPAND | wx.ALL)
        hbox1.Add(self.rf1, 2, wx.EXPAND | wx.ALL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(wx.StaticText(self, label="RF2:"), 1, wx.EXPAND | wx.ALL)
        hbox2.Add(self.rf2, 2, wx.EXPAND | wx.ALL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(wx.StaticText(self, label="RF3:"), 1, wx.EXPAND | wx.ALL)
        hbox3.Add(self.rf3, 2, wx.EXPAND | wx.ALL)
        box.Add(hbox1, 1, wx.EXPAND | wx.ALL)
        box.Add(hbox2, 1, wx.EXPAND | wx.ALL)
        box.Add(hbox3, 1, wx.EXPAND | wx.ALL)
        
        box.Add(wx.StaticText(self, label="Complement Sequence:"), 1, wx.EXPAND | wx.ALL)
        box.Add(self.cseq, 1, wx.EXPAND | wx.ALL)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4.Add(wx.StaticText(self, label="RF4:"), 1, wx.EXPAND | wx.ALL)
        hbox4.Add(self.rf4, 2, wx.EXPAND | wx.ALL)
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        hbox5.Add(wx.StaticText(self, label="RF5:"), 1, wx.EXPAND | wx.ALL)
        hbox5.Add(self.rf5, 2, wx.EXPAND | wx.ALL)
        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        hbox6.Add(wx.StaticText(self, label="RF6:"), 1, wx.EXPAND | wx.ALL)
        hbox6.Add(self.rf6, 2, wx.EXPAND | wx.ALL)
        box.Add(hbox4, 1, wx.EXPAND | wx.ALL)
        box.Add(hbox5, 1, wx.EXPAND | wx.ALL)
        box.Add(hbox6, 1, wx.EXPAND | wx.ALL)
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.stop, 1, wx.EXPAND | wx.ALL)
        hbox.Add(self.prev, 1, wx.EXPAND | wx.ALL)
        box.Add(hbox, 1, wx.EXPAND | wx.ALL)
        self.SetSizer(box)

if __name__ == "__main__":
    class Frame(wx.Frame):
        def __init__(self, s_parent, s_title="GUI_RFSeq_Output"):
            wx.Frame.__init__(self, s_parent, title=s_title, size=(200, 300))
            panel = wx.Panel(self)
            panel1 = GUI_RFSeq_Output(panel)
            box = wx.BoxSizer()
            box.Add(panel1, 1, wx.EXPAND | wx.ALL)
            panel.SetSizer(box)
            self.Centre()
            self.Show(True)
    app = wx.App(False)
    Frame(None)
    app.MainLoop()
