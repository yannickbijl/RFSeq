import wx

class GUI_RFSeq_Input(wx.Panel):
    def __init__(self, bb_parent):
        
        def explain():
            text = ("Give a file with a single line containing the sequence." +
                    " Only A, T, C, G are allowed. The program generates all" +
                    " six reading frames. The first three on the forward " +
                    "strand, and the last three on the complement strand. " +
                    "Please note that these are reading frames, not open " +
                    "reading frames.")
            return text
        
        wx.Panel.__init__(self, bb_parent, style=wx.BORDER_SUNKEN)
        # Input parameters
        self.filename = wx.FilePickerCtrl(self, path="") 
        
        # Buttons
        self.stop = wx.Button(self, label="Quit")
        self.next = wx.Button(self, label="Next")
        
        # Text
        self.explain = wx.StaticText(self, label=explain())
        
        # Placing of items in frame
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(self.explain, 2, wx.EXPAND | wx.ALL)
        box.Add(self.filename, 1, wx.EXPAND | wx.ALL)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.stop, 1, wx.EXPAND | wx.ALL)
        hbox.Add(self.next, 1, wx.EXPAND | wx.ALL)
        box.Add(hbox, 1, wx.EXPAND | wx.ALL)
        self.SetSizer(box)

if __name__ == "__main__":
    class Frame(wx.Frame):
        def __init__(self, s_parent, s_title="GUI_RFSeq_Input"):
            wx.Frame.__init__(self, s_parent, title=s_title, size=(200, 300))
            panel = wx.Panel(self)
            panel1 = GUI_RFSeq_Input(panel)
            box = wx.BoxSizer()
            box.Add(panel1, 1, wx.EXPAND | wx.ALL)
            panel.SetSizer(box)
            self.Centre()
            self.Show(True)
    app = wx.App(False)
    Frame(None)
    app.MainLoop()
