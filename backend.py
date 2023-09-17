from Password_manager import *
from random import*
from json import *
  
class passwordmanagerbackend(passwordmanagerui):
    def __init__(self):
        self.a=""
        super().__init__()
        
    
    def file_entry(self):
        self.new_data = {self.website:{
            "email": self.email,
            "password":self.password
        }}
        
        is_true = messagebox.askokcancel(title = "Confirm",message="Are you sure you want to save this \n website : {} \n password : {}\n email : {} ".format(self.website,self.password,self.email))
        if is_true == True:
                with open("Password_data.json","r") as password_data :
                    password_dict =  load(password_data)
                    password_dict.update(self.new_data)
                    print(type(password_dict))
                    with open ("Password_data.json","w") as password_data2:
                        dump(password_dict,password_data2,indent=4)
                        self.password_entry.delete(0,END)
                        self.website_entry.delete(0,END)
        
    def save_data(self):
        self.website = self.website_entry.get()
        self.email=self.email_entry.get()
        self.password = self.password_entry.get()
        
        self.file_entry()
        
    def save_work(self):
        self.save_boolean = True
        self.save_data()
        self.save_boolean = False
    
    def password_generator(self):
        self.elements_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ';', ':', '<', '>', ',', '.', '/', '?']
        self.randomint = randint(8,11)
        for i in range(self.randomint):
            character = str(choice(self.elements_list))
            self.a = self.a + character 
        
        self.password_entry.insert(0,self.a)
    def generate_password(self):
        self.pass_boolean = True
        self.password_generator()
        self.pass_boolean = False
    
    def retrieve_details(self):
        with open("password_data.json","r") as data_in_dict : 
            a = load(data_in_dict)
            for i in a :
                if i == self.website_entry.get():
                    messagebox.showinfo(i,f'''email: {a[i]['email']} 
password : {a[i]['password']}''')
                else:
                    messagebox.showinfo("Not Found","Details Not Found")
    def retrieve_choice(self):
        self.retrieve_boolean = True
        self.retrieve_details()
        self.retrieve_boolean = False            
                    
b = passwordmanagerbackend()
