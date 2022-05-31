import tkinter as tk
import time
class StatusFrame(tk.Frame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.strvar = tk.StringVar()
        self.MesList=["","","","Info:"]
        self.columnconfigure(0,weight=1)
        self.statusbar = tk.Label(self,relief="sunken",anchor="sw",textvariable=self.strvar)
        
        self.statusbar.grid(column=0,row=0,sticky="WE")
        self.RunThread()
    def ShowMessage(self):
        self.after(800,self.ShowMessage)
        self.m_UpdateTime()
        self.strvar.set(" || ".join(self.MesList))
    @staticmethod
    def GetTimeStr():
        '''
        返回日期字符串 如211103_161722
        '''
        return time.strftime(" %y年%m月%d日 %H:%M:%S", time.localtime())
   
    def RunThread(self):
        
        self.m_UpdateStatus(1)
        self.m_UpdatePercent(1)
        
        self.ShowMessage()
    def m_UpdateInfo(self,msg):
        self.MesList[3]="Info:{}".format(msg)
    def m_UpdateStatus(self,index):
        '''
        0.Ready 1.Running 2.Finish 3.Fail 
        '''
        self.MesList[2]=["Ready","Running","Finish","Fail"][index]
        self.statusbar["bg"]=["green","yellow","green","red"][index]
        if index == 0 or index == 2:
            self.m_UpdatePercent([0,100][index>0])
    def m_UpdatePercent(self,pros):
        self.MesList[1]="{}>{} {:>3d}%".format("="*int(pros/10),"="*(10-int(pros/10)),pros)
    def m_UpdateTime(self):
        self.MesList[0]=self.GetTimeStr()

if __name__=="__main__":
    import tkinter as tk

    xe = tk.Tk()
    xe.columnconfigure(0,weight=1)
    ggd = tk.Button(xe,text="231")
    ggd.grid(column=0,row=0)
    bb=StatusFrame(xe)
    # bb.ShowMessage('233')
    bb.m_UpdateStatus(2)
    bb.grid(column=0,row=1,sticky="WE")

    xe.mainloop()