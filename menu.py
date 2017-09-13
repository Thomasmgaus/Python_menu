#this class presents the menu
from tkinter import *
import sys
class Menu:
    def exit_command(self, lst,lst2):
        self.update_list(lst,lst2)
        self.write_file(lst,lst2)
        sys.exit()
    def write_file(self, lst, lst2):
        output = open("out_data.txt", "w")
        for x in lst:
            tmp = x
            output.write(tmp["drug"]+':'+tmp["screen"]+':'+tmp["confirm"]+"\n")
        for x in lst2:
            tmp = x
            output.write(tmp["drug"].get()+':'+tmp["screen"]+':'+tmp["confirm"]+"\n")
        output.write("Total Sample Per Month:"+ self.total.get())
        output.write("Signature:"+self.sig_entry.get()+"  "+"Initial:"+self.initial_entry.get()+"  "+"Date:"+self.date_entry.get())
        output.close()
    def toggle(self, button):
        if button["text"] == "False":
            button["text"] = "True"
        else:
            button["text"] = "False"
    def onFrameConfigure(self,canvas):
            canvas.configure(scrollregion = canvas.bbox("all"))
    #def print_button(self):
        #for i in self.screen_button1:
            #print(i["text"])
    def update_list(self,lst,lst2):
        i = 0
        xt = 0
        for x in range(len(lst)):
            #print(lst[x])
            tmp=lst[x]
            try:
                tmp2 = self.screen_button1[x]
            except:
                tmp2 = self.screen_button2[x-1]
            print(tmp2["text"])
            if tmp["drug"] != "ADULTERANTS":
                tmp["screen"]=tmp2["text"]
                lst[x] = tmp
            else:
                i = x
                x+=2
        for x in range(len(lst)):
            tmp = lst[x]
            try:
                tmp2 = self.screen_button2[x]
            except:
                tmp2 = self.screen_button2[x-1]
            if tmp["drug"] != "ADULTERANTS":
                tmp["confirm"] = tmp2["text"]
                lst[x]=tmp
            else:
                x+=2
        for x in range(len(lst2)):
            tmp = lst2[x]
            tmp2 = self.screen_button3[x]
            tmp3 = self.screen_button4[x]
            tmp["confirm"] = tmp2["text"]
            tmp["screen"] = tmp3["text"]


        self.write_file(lst,lst2)
    def __init__(self,master,lst = []):
        self.master = master
        master.title("Flyer")
        self.canvas = Canvas(master, borderwidth = 0, background = "#ffffff")
        self.frame = Frame(self.canvas,background = "#ffffff")
        self.vsb = Scrollbar(master, orient = "vertical", command = self.canvas.yview)
        self.canvas.configure(yscrollcommand = self.vsb.set)
        self.vsb.pack(side="right",fill = "y")
        self.canvas.pack(side = "left",fill = "both",expand = True)
        self.canvas.create_window((8,8),window = self.frame,anchor = "nw")

        self.frame.bind("<Configure>", lambda event, canvas=self.canvas: self.onFrameConfigure(canvas))
        i = 1
        drug_entry =[]
        drug_label = {}
        self.screen_button1 = []
        self.screen_button2 = []
        self.screen_button3 = []
        self.screen_button4 = []
        #creates the list and the corresponding buttons
        self.drug = Label(self.frame, text = "Drugs")
        self.screen = Label(self.frame, text="Screen")
        self.confirmatory = Label(self.frame,text = "Confirmatory")
        change = False
        ignore = False
        for drugs in lst:
            #e = Entry(self.master)
            #e.grid(sticky= W)
            #drug_entry[drugs["drug"]] = e
            if drugs["drug"] == "ADULTERANTS":
                self.adult = Label(self.frame, text = "----------"+drugs["drug"]+"----------")
                self.adult.grid(row = i, column = 0, sticky = W)
                ignore = True
                change = True
            if ignore == True:
                ignore = False
            else:
                lb = Label(self.frame,text = drugs["drug"])
                lb.grid(row=i,column=0, sticky = W)
                drug_label[drugs["drug"]] = lb
                self.bt = Button(self.frame, text = "False")
                self.bt.grid(row=i, column = 1, sticky = W)
                self.screen1 = self.screen_button1.append(self.bt)
                self.bt2 = Button(self.frame, text = "False")
                self.bt2.grid(row = i, column = 2, sticky = E)
                self.screen2 = self.screen_button2.append(self.bt2)
                if change == True:
                    self.bt.configure(command = lambda i = i: self.toggle(self.screen_button1[i-2]))
                    self.bt2.configure(command = lambda i = i: self.toggle(self.screen_button2[i-2]))
                else:
                    self.bt.configure(command = lambda i = i: self.toggle(self.screen_button1[i-1]))
                    self.bt2.configure(command = lambda i = i: self.toggle(self.screen_button2[i-1]))
            i +=1
        x = 0
        t = 0
        self.label_title = Label(self.frame, text = "----------Other----------")
        self.label_title.grid(row = i, column = 0, sticky = W)
        i+=1
        while x <= 5:
            self.e = Entry(self.frame)
            self.e.insert(0,"Custom")
            self.e.grid(row = i, column = 0, sticky= W)
            drug_label[drugs["drug"]] = self.e
            self.bt = Button(self.frame, text = "False")
            self.bt.grid(row=i, column = 1, sticky = W)
            self.screen1 = self.screen_button3.append(self.bt)
            self.bt2 = Button(self.frame, text = "False")
            self.bt2.grid(row = i, column = 2, sticky = E)
            self.screen2 = self.screen_button4.append(self.bt2)
            self.bt.configure(command = lambda t = t: self.toggle(self.screen_button3[t]))
            self.bt2.configure(command = lambda t = t: self.toggle(self.screen_button4[t]))
            dict_insert = {"drug":self.e,"screen":self.bt["text"],"confirm":self.bt2["text"]}
            drug_entry.append(dict_insert)
            t+=1
            i+=1
            x+=1
        self.sig_label = Label(self.frame,text = "Menu Approval E-Signature")
        self.sig_label.grid(row = i+3, column = 0, sticky = W)
        self.initial = Label(self.frame, text = "LESSE INITIAL")
        self.initial.grid(row = i+3, column = 1, sticky = W)
        self.date = Label(self.frame , text = "Todays Date")
        self.date.grid(row = i+3, column = 2, sticky = E)
        self.sig_entry = Entry(self.frame)
        self.sig_entry.insert(0,"")
        self.sig_entry.grid(row = i+4, column = 0, sticky = W)
        self.initial_entry = Entry(self.frame)
        self.initial_entry.insert(0,"")
        self.initial_entry.grid(row = i+4, column = 1, sticky = W)
        self.date_entry = Entry(self.frame)
        self.date_entry.insert(0,"")
        self.date_entry.grid(row = i+4,column = 2, sticky = E)
        self.total_label = Label(self.frame, text = "Total sample per month")
        self.total_label.grid(row = i+1,column = 2, sticky = E)
        self.total = Entry(self.frame)
        self.total.insert(0,"")
        self.total.grid(row = i+2, column = 2, sticky = E)

        i +=2
        self.exit_button = Button(self.frame, text = "Save and exit", command = lambda lst = lst, drug_entry = drug_entry:self.exit_command(lst,drug_entry))
        self.exit_button.grid(row=i+3, column = 2, sticky = E)
        self.drug.grid(row=0, column=0)
        self.screen.grid(row=0, column = 1, sticky = W)
        self.confirmatory.grid(row = 0, column = 2, sticky = W)


def file_open():
    lst = []
    input = open("data.txt",'r')
    lst = fill_list(input)
    return lst
#need to add in a try to this incase of data.txt's removal
#creats a list of dictionaries
def fill_list(str):
    menu_list = []
    line = "temp"
    while line != "":
        line = str.readline()
        line = line.rstrip('\n') #strip newline
        if line.find(":") == -1:
            break
        line = line.split(':')
        drug_quantity = {"drug":line[0],"screen":line[1],"confirm":line[2]}
        menu_list.append(drug_quantity)
    return menu_list
def main():
    lst = []
    lst = file_open()
    root = Tk()
    my_gui = Menu(root,lst)
    root.mainloop()

main()
