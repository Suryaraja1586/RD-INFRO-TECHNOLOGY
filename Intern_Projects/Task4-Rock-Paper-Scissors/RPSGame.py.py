import customtkinter as ctk
import random
#Creating a class named RPSGame 
class RPSGame(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Rock Paper Scissors")
        self.configure(fg_color="#1e1e1e")
        self.resizable(False,False)
    #Setting the initial Scores and round!
        self.user_score=0
        self.com_score=0
        self.round_no=1
        self.history_lines=[]

        self.create_widgets()
    #Creating the widgtes!
    def create_widgets(self):
        self.title_label=ctk.CTkLabel(self,text="Rock Paper Scissors",font=("Arial",28,'bold'),text_color="white")
        self.title_label.pack(pady=20)
        #creating the buttons rock,paper,scissors
        self.button_frame = ctk.CTkFrame(self,fg_color="transparent")
        self.button_frame.pack(pady=30)
        self.rockbtn = ctk.CTkButton(self.button_frame,text="Rock",width=120,command=lambda:self.play("rock"))
        self.rockbtn.grid(row=0,column=0,padx=15)
        self.paperbtn=ctk.CTkButton(self.button_frame,text="Paper",width=120,command=lambda:self.play("paper"))
        self.paperbtn.grid(row=0,column=1,padx=15)
        self.scissorsbtn=ctk.CTkButton(self.button_frame,text="Scissors",width=120,command=lambda:self.play("scissors"))
        self.scissorsbtn.grid(row=0,column=2,padx=15)
        self.result_label = ctk.CTkLabel(self,text="",font=("Arial",20),text_color='white')
        self.result_label.pack(pady=10)
        self.score_label=ctk.CTkLabel(self,text="YOU: 0 || COMPUTER: 0",font=("Arial",18),text_color='white')
        self.score_label.pack(pady=10)
        self.history_label= ctk.CTkLabel(self,text="Game History",font=("Arial",16,'bold'),text_color='white')
        self.history_label.pack(pady=(10,0))
        self.hist_box=ctk.CTkTextbox(self,width=700,height=150,font=("Arial",14))
        self.hist_box.pack(pady=10)
        self.hist_box.configure(state="disabled")
        self.bottomframe=ctk.CTkFrame(self,fg_color="transparent")
        self.bottomframe.pack(pady=10)
        self.resetbtn =ctk.CTkButton(self.bottomframe,text="Play Again",command=self.reset,width=150)
        self.resetbtn.grid(row=0,column=0,padx=10)
        self.savebtn=ctk.CTkButton(self.bottomframe,text="Save History to file",command=self.save_history,width=200)
        self.savebtn.grid(row=0,column=1,padx=10)


    def play(self,user_choice):
        options=['rock','paper','scissors']
        comp_choice=random.choice(options)

        if user_choice == comp_choice:
            result = "It's a Tie!!"
            color ="#cccccc"
        elif (user_choice == 'rock' and comp_choice == 'scissors') or \
            (user_choice == 'scissors' and comp_choice == 'paper') or  \
            (user_choice == 'paper' and comp_choice == 'rock'):
            result ="You Win!!"
            self.user_score+=1
            color = "#00cc66"
        else:
            result = "Computer Wins!!"
            self.com_score+=1
            color = "#ff4444"
        
        self.result_label.configure(text=f"You Chose : {user_choice.capitalize()} | Computer Chose: {comp_choice.capitalize()}\n{result}",text_color=color)
        self.score_label.configure(text=f"You: {self.user_score} | Computer: {self.com_score}")
        history_entry = f"Round {self.round_no}: You Chose: {user_choice.capitalize()},Computer Chose: {comp_choice.capitalize()} --> {result}"
        self.history_lines.append(history_entry)
        self.hist_box.configure(state = 'normal')
        self.hist_box.insert('end',history_entry+"\n")
        self.hist_box.see('end')
        self.round_no+=1

    def reset(self):
        self.user_score = 0
        self.com_score = 0
        self.round_no = 1
        self.result_label.configure(text="",text_color='white')
        self.score_label.configure(text="You: 0 | Computer: 0")
        self.history_lines=[]
        self.hist_box.configure(state= 'normal')
        self.hist_box.delete("0.0","end")
        self.hist_box.configure(state="disabled")
    def save_history(self):
        with open("rps_game.txt","w",encoding="utf-8") as file:
            for line in self.history_lines:
                file.write(line + "\n")
        self.result_label.configure(text="History Saved to rps_game.txt",text_color="yellow")

#launching the game.
app=RPSGame()
app.mainloop()