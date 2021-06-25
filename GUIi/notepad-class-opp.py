from tkinter import *
# from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import filedialog
from tkinter import simpledialog as sim
from tkinter import messagebox as msg


class text_editer:
    current="no"



    def newfile(self):
        self.tex.delete(1.0, END)
        current = "no"

    def openfile(self):

        opens=filedialog.askopenfile(initialdir="/",title="select file to open",filetype=(("text files","*.txt"),("all files","*.*")))
        if opens != None:
            self.tex.delete(1.0, END)
            for line in opens:
                self.tex.insert(END, line)
            self.current=opens.name
            print(self.current)
            opens.close()
        # opens = filedialog.askopenfile(filetype=[("text files", "*.txt"), ("all files", "*.*")])
        # if opens=="":
        #     opens=None
        # else:
        #     # master.title(os.path.basename(self.opens) + " - Notepad")
        #     self.tex.delete(1.0, END)
        #     f = open(opens, "r")
        #     self.tex.insert(1.0, f.read())
        #     f.close()




    def save_as(self):
        f = filedialog.asksaveasfile(mode="w",defaultextension=".txt")
        if f is None:
            return
        textsave=self.tex.get(1.0,END)
        self.current = f.name
        f.write(textsave)
        f.close()

    def save(self):
        if  self.current=="no":
            self.save_as()
        else:
            f=open(self.current,"w")
            f.write(self.tex.get(1.0,END))
            f.close()

    def cut(self):
        self.tex.event_generate(("<<Cut>>"))

    def copy(self):
        self.tex.event_generate(("<<Copy>>"))

    def paste(self):
        self.tex.event_generate(("<<Paste>>"))


    def need(self):
        ret=msg.askquestion("Help","Do you need any help?")
        if ret=="yes":
            msg.askokcancel("Answer","please check in google.")



    def report(self):
        vall = sim.askstring("Send Your problem", "Please enter your name...")
        val=sim.askstring("Send Your problem","Please enter your report...")
        ff=open("report.txt","a")
        cur=ff.write(vall+" => ")
        cur=ff.write(val+"\n")
        ff.close()



    def __init__(self,master):
        self.master=master
        master.title("Untitle-Notepad")
        self.tex=Text(master,font="lucida 13" ,wrap=WORD, padx=10,pady=10,undo=True)
        self.tex.pack(expand=True,fill="both")
        self.main_manu=Menu(master)
        self.master.config(menu=self.main_manu)

        self.file_manu=Menu(self.main_manu,tearoff=0)
        self.main_manu.add_cascade(label="File",menu=self.file_manu)
        self.file_manu.add_command(label="New",command=self.newfile)
        self.file_manu.add_command(label="Open", command=self.openfile)
        self.file_manu.add_separator()
        self.file_manu.add_command(label="Save as", command=self.save_as)
        self.file_manu.add_command(label="Save", command=self.save)
        self.file_manu.add_separator()
        self.file_manu.add_command(label="Exit", command=master.quit)

        self.edit_manu = Menu(self.main_manu, tearoff=0)
        self.main_manu.add_cascade(label="Edit", menu=self.edit_manu)
        self.edit_manu.add_command(label="cut",command=self.cut)
        self.edit_manu.add_command(label="copy", command=self.copy)
        self.edit_manu.add_command(label="paste", command=self.paste)
        self.edit_manu.add_separator()
        self.edit_manu.add_command(label="Undo", command=self.tex.edit_undo)
        self.edit_manu.add_command(label="Redo", command=self.tex.edit_redo)

        self.help_manu = Menu(self.main_manu, tearoff=0)
        self.main_manu.add_cascade(label="Help", menu=self.help_manu)
        self.help_manu.add_command(label="Need help",command=self.need)
        self.help_manu.add_command(label="Report", command=self.report)



        self.scroll=Scrollbar(self.tex)
        self.scroll.pack(side=RIGHT,fill=Y)
        self.scroll.config(command=self.tex.yview)
        self.tex.config(yscrollcommand=self.scroll.set)




root=Tk()
root.wm_iconbitmap("pyy.ico")
root.geometry("500x500")
te=text_editer(root)
root.mainloop()