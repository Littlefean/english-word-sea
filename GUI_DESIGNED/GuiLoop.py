import tkinter as tk
import tktk
from StatusFrame import StatusFrame
class PraticeGui:
    def __init__(self) -> None:
        self.win = tk.Tk()
        self.win.title("PraticeGui")
        self.wordshow = tk.StringVar()
        self.wordshow.set("NONE")
        self.design()
    def run(self):
        self.WegitsStatus(self.cmd3,False)
        self.win.mainloop()
    def design(self):
        tk.Label(self.win,textvariable=self.wordshow).grid(column=0,row=0,columnspan=3,sticky="WE")
        self.log=tktk.LogFrame(self.win,text="释意:")
        self.log.grid(column=0,row=1,columnspan=3,sticky="WE")
        self.cmd1=tk.Button(self.win,text="熟练",width=20,bg="#FFEE33",command=lambda : self.CallBack(1))
        self.cmd1.grid(column=0,row=2)
        self.cmd2=tk.Button(self.win,text="不熟练",width=20,bg="#33EEFF",command=lambda : self.CallBack(2))
        self.cmd2.grid(column=1,row=2)
        self.cmd3=tk.Button(self.win,text="Next",width=20,bg="#EE33FF",command=lambda : self.CallBack(3))
        self.cmd3.grid(column=2,row=2)
        self.status=StatusFrame(self.win)
        self.status.grid(column=0,row=4,columnspan=3,sticky="WE")
    def WegitsStatus(self,obj:tk.Button,status:bool):
        '''
        true able
        '''
        obj["state"]=[tk.DISABLED,tk.ACTIVE][status]
    def CallBack(self,idx):
        if idx==1:
            self.CallBackcom1()
            self.WegitsStatus(self.cmd1,False)
            self.WegitsStatus(self.cmd2,False)
            self.WegitsStatus(self.cmd3,True)
        if idx==2:
            self.CallBackcom2()
            self.WegitsStatus(self.cmd1,False)
            self.WegitsStatus(self.cmd2,False)
            self.WegitsStatus(self.cmd3,True)
        if idx==3:
            self.CallBackcom3()
            self.WegitsStatus(self.cmd1,True)
            self.WegitsStatus(self.cmd2,True)
            self.WegitsStatus(self.cmd3,False)
    def CallBackcom1(self):
        print("com1")

    def CallBackcom2(self):
        print("com2")

    def CallBackcom3(self):
        print("com2")

if __name__=="__main__":
    xe = PraticeGui()
    xe.run()