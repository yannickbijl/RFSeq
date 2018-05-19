import sys

import wx

from ESC_RFSeq import ESC_RFSeq
from GUI_RFSeq_Input import GUI_RFSeq_Input
from GUI_RFSeq_Output import GUI_RFSeq_Output

class RFSeq(wx.Frame):
    def __init__(self, s_parent, s_title="RFSeq"):
        wx.Frame.__init__(self, s_parent, title=s_title, style=wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)
        self.panel = wx.Panel(self)
        box = wx.BoxSizer()
        self.frames()
        self.hiding()
        self.panel.SetSizer(self.box2)
        self.dic['A'].Show()
        self.binder()
        self.Show(True)
        self.Centre()
        self.SetSize((300, 225))
        box.Add(self.panel, 1, wx.ALL | wx.EXPAND)
        self.SetSizer(box)

    def frames(self):
        def dic_make():
            self.dic = {}
            self.dic['A'] = self.rfinput
            self.dic['B'] = self.rfoutput

        self.rfinput = GUI_RFSeq_Input(self.panel)
        self.rfoutput = GUI_RFSeq_Output(self.panel)
        dic_make()
        self.box2 = wx.BoxSizer()
        for x in self.dic:
            self.box2.Add(self.dic[x], 1, wx.ALL | wx.EXPAND)

    def hiding(self):
        for x in self.dic:
            self.dic[x].Hide()

    def binder(self):
        def stop_buttons():
            for x in self.dic:
                self.dic[x].stop.Bind(wx.EVT_BUTTON, self.quitting)

        def other_buttons():
            self.rfinput.next.Bind(wx.EVT_BUTTON, self.next_frame)
            self.rfoutput.prev.Bind(wx.EVT_BUTTON, self.prev_frame)

        stop_buttons()
        other_buttons()

    def quitting(self, event):
        sys.exit()

    def next_frame(self, event):
        def get_seq():
            with open(self.rfinput.filename.GetPath(), "r") as f:
                seq = f.readline().strip()
            return seq
        
        def set_rf(seq):
            seqs = ESC_RFSeq(seq)
            self.rfoutput.fseq.SetValue(seqs.get_fseq())
            self.rfoutput.cseq.SetValue(seqs.get_cseq())
            self.rfoutput.rf1.SetValue(seqs.get_rf1())
            self.rfoutput.rf2.SetValue(seqs.get_rf2())
            self.rfoutput.rf3.SetValue(seqs.get_rf3())
            self.rfoutput.rf4.SetValue(seqs.get_rf4())
            self.rfoutput.rf5.SetValue(seqs.get_rf5())
            self.rfoutput.rf6.SetValue(seqs.get_rf6())
        
        set_rf(get_seq())
        self.hiding()
        self.SetSize((300, 450))
        self.Refresh()
        self.dic['B'].Show()
        self.Layout()
        self.Centre()
    
    def prev_frame(self, event):
        self.rfinput.filename.SetPath("")
        self.hiding()
        self.SetSize((300, 225))
        self.Refresh()
        self.dic['A'].Show()
        self.Layout()
        self.Centre()


# Is called when this script is used as the MAIN.
if __name__ == "__main__":
    class MyApp(wx.App):
        def OnInit(self):
            frame = RFSeq(None)
            frame.Show(True)
            frame.Centre()
            self.SetTopWindow(frame)
            return True

    # The application-loop
    app = MyApp(0)
    app.MainLoop()