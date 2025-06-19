import customtkinter as ctk
import random
import string

#Creating the class for Password Generation
class PasswordGeneratorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PassWord Generator")
        self.geometry("800x500")
        self.resizable(False,False)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        
        self.create_widgets()

    #Labeling all the elements in the page
    def create_widgets(self):
        self.title_label = ctk.CTkLabel(self,text="PASSWORD GENERATOR",font=("Arial",28,"bold"),text_color="#5e35b1")
        self.title_label.pack(pady=20)

        self.lenght_frame = ctk.CTkFrame(self,fg_color="transparent")
        self.lenght_frame.pack(pady=20)

        self.lenght_label=ctk.CTkLabel(self.lenght_frame,text="Enter Password Length",font=("Arial",18),text_color="#5e35b1")
        self.lenght_label.grid(row=0,column=0,padx=10)

        self.lenght_entry = ctk.CTkEntry(self.lenght_frame,width=100,font=("Arial",18))
        self.lenght_entry.grid(row=1,column=0)

        self.gen_button= ctk.CTkButton(self,text="Generate Password",fg_color="#5e35b1",command=self.generate_password,width=200,)
        self.gen_button.pack(pady=20)

        self.password_out = ctk.CTkEntry(self,width=400,font=("Arial",18),justify="center")
        self.password_out.pack(pady=10)

    #Function for Password generation using random module.
    def generate_password(self):
        try:
            length = int(self.lenght_entry.get())
            if length <=0:
                self.password_out.delete(0,'end')
                self.password_out.insert(0,"Enter positive number!")
                return
            

            chars = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(chars) for _ in range(length))

            self.password_out.delete(0,'end')
            self.password_out.insert(0,password)
        except ValueError:
            self.password_out.delete(0,'end')
            self.password_out.insert(0,"Please Enter a Valid Number!!")

app=PasswordGeneratorApp()
app.mainloop()