from tkinter import *


class passwordmanagerui:
    def __init__(self):
        win = Tk()
        self.img()
        self.labels()
        self.entries()
        self.buttons()
        
        self.save_boolean = False
        self.pass_boolean = False
       
        win.minsize(width=500,height=500)
        win.title("Password Manager")
        win.config(padx=100,pady=50) 
        win.mainloop()
    def img(self):
        self.canvas_img = Canvas(height=500,width=500)
        self.amg = PhotoImage(file="password_manager_img.png")
        self.canvas_img.create_image(200,170,image= self.amg)
        self.canvas_img.grid(column=1,row=0)
    def labels(self):
        self.website = Label(text="Website")
        self.website.grid(row=2,column=0)
        self.email = Label(text='''Email/Username''')
        self.email.grid(row=3,column=0)
        self.password = Label(text='''Password''')
        self.password.grid(row=4,column=0)
        
    def entries(self):
        self.password_entry= Entry(width=20)
        self.password_entry.grid(row=4,column=1,columnspan=1)
        
        
        self.website_entry= Entry(width=36)
        self.website_entry.grid(row=2,column=1,columnspan=2)
        self.website_entry.focus()
        self.email_entry = Entry(width=36)
        self.email_entry.grid(row=3,column=1,columnspan=2,padx=5,pady=5)
        self.email_entry.insert(0,"tanmayshukla@gmail.com")
        
    def buttons(self):
        global generated_pass
        self.generate_password = Button(text="Generate Password",command= self.password_generator)
        
        self.generate_password.grid(row=4,column=2)
        
        self.save_button = Button(text="Save",width=36,command=self.save_work)
        self.save_button.grid(row=5,column=1,columnspan=2)
        
