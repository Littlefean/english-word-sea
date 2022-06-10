import tkinter as tk
import time
import locale

locale.setlocale(locale.LC_CTYPE, 'chinese')


class StatusFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.strVar = tk.StringVar()
        self.MesList = ["", "", "", "Info:"]
        self.columnconfigure(0, weight=1)
        self.statusBar = tk.Label(self, relief="sunken", anchor="sw", textvariable=self.strVar)

        self.statusBar.grid(column=0, row=0, sticky="WE")
        self.RunThread()

    def ShowMessage(self):
        self.after(800, self.ShowMessage)
        self.m_UpdateTime()
        self.strVar.set(" || ".join(self.MesList))

    @staticmethod
    def GetTimeStr():
        """
        返回日期字符串 如211103_161722
        """
        return time.strftime(" %y年%m月%d日 %H:%M:%S", time.localtime())

    def RunThread(self):
        self.m_UpdateStatus(1)
        self.m_UpdatePercent(1)

        self.ShowMessage()

    def m_UpdateInfo(self, msg):
        self.MesList[3] = f"Info:{msg}"

    def m_UpdateStatus(self, index):
        """
        0.Ready 1.Running 2.Finish 3.Fail
        """
        self.MesList[2] = ["Ready", "Running", "Finish", "Fail"][index]
        self.statusBar["bg"] = ["green", "yellow", "green", "red"][index]
        if index in [0, 2]:
            self.m_UpdatePercent([0, 100][index > 0])

    def m_UpdatePercent(self, pros):
        self.MesList[1] = "{}>{} {:>3d}%".format("=" * int(pros / 10), "=" * (10 - int(pros / 10)), pros)

    def m_UpdateTime(self):
        self.MesList[0] = self.GetTimeStr()


if __name__ == "__main__":
    import tkinter as tk

    xe = tk.Tk()
    xe.columnconfigure(0, weight=1)
    ggd = tk.Button(xe, text="231")
    ggd.grid(column=0, row=0)
    bb = StatusFrame(xe)
    # bb.ShowMessage('233')
    bb.m_UpdateStatus(2)
    bb.grid(column=0, row=1, sticky="WE")

    xe.mainloop()
