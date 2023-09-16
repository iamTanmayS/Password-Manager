from Password_manager import *
from random import*
  
class passwordmanagerbackend(passwordmanagerui):
    def __init__(self):
        self.a=""
        super().__init__()
        
    
    def file_entry(self):
        password_data= open("Password_data.txt","a")
        self.password_format = "\n {} | {}  | {} \n ".format(self.email,self.website,self.password)
        password_data.writelines(self.password_format)
        
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
b = passwordmanagerbackend()
