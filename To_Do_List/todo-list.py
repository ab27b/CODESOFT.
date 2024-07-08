from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To Do List')
        self.root.geometry('650x450+300+150')
        
        self.label = Label(self.root, text="To-Do-list-App", font="ariel, 25 bold", width=10, bd=5, bg="cyan", fg="black")
        self.label.pack(side='top', fill=BOTH)
        
        self.label2 = Label(self.root, text= "Add", font ="ariel, 20 bold", width= 20, bd=4, bg="grey", fg="salmon")
        self.label.pack(side='top', fill=BOTH)
        
        self.label2.place(x=300, y=60)
        
        self.label3 = Label(self.root, text= "Tasks", font ="ariel, 20 bold", width= 20, bd=2, bg="grey", fg="salmon")
        self.label.pack(side='top', fill=BOTH)
        
        self.label3.place(x=34, y=63)
        self.main_text =Listbox(self.root, height=8, width=40, bd=5, font="ariel, 20 italic bold")
        
        self.main_text.place(x=50, y=150)
        self.text = Text(self.root,bd=5,height=2, width=30)
        font_tuple =("Ariel", 20, "bold")
        self.text.configure(font=font_tuple)
        self.text.place(x=20, y=100)
        
        def add():
            content =self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open('data.txt', 'w') as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END)
            
        def delete():
            delete_= self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open('data.txt', 'r+')as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    item =str(look)
                    if item not in line:
                        f.write(line)
                    f.truncate()
            self.main_text.delete(delete_)
            
            with open('data.txt', 'r') as file:
                read = file.readlines()
                for i in read:
                    ready= i.split()
                    self.main_text.insert(END, ready)
                    file.close()
        self.add_button = Button(self.root, text='Add', font=("Arial", 20, "bold", "italic"),
                                 width=10, bd=5, bg='grey', fg='salmon', command=add)
        self.add_button.place(x=450, y=100)
        
        self.delete_button = Button(self.root, text='Delete', font=("Arial", 20, "bold", "italic"),
                                    width=10, bd=5, bg='grey', fg='salmon', command=delete)
        self.delete_button.place(x=450, y=200)
            
            
def main():
    root = Tk()
    ui = todo(root)

    root.mainloop()

if __name__ == "__main__":
    main()