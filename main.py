from tkinter import *
from tkinter import messagebox
from db import database
from api import myapp

class NLPApp:

    def __init__(self):
        self.root = Tk()
        self.root.title('NLPApp')
        self.root.iconbitmap(r'C:\Users\bhava\PycharmProjects\nlpapp\images\projectpic.ico')
        self.root.geometry('600x600')
        self.root.configure(bg= '#103092')
        self.dbo = database()
        self.api = myapp()
        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        #to display text we should have "labelclass"
        self.clear()
        heading = Label(self.root,text = "NLPApp",bg='#103092',fg='white')
        heading.configure(font=('verdana','24','italic'))
        heading.pack(pady=(30,30))

        heading1 = Label(self.root,text = "Login",bg='#103092',fg='white')
        heading1.configure(font=('verdana','15','italic'))
        heading1.pack(pady=(5,5))

        heading2 = Label(self.root, text="Enter email", bg='#103092', fg='white')
        heading2.configure(font=('verdana', '15', 'italic'))
        heading2.pack()

        self.email_input = Entry(self.root,width=35,)
        self.email_input.pack(ipady=3)

        heading2 = Label(self.root, text="Enter password", bg='#103092', fg='white')
        heading2.configure(font=('verdana', '15', 'italic'))
        heading2.pack()

        self.password_input = Entry(self.root,width=35,show='*')
        self.password_input.pack(ipady=3)

        heading3 = Button(self.root, width=10, text='login now', command=self.search)
        heading3.configure(font=('verdana', '10', 'italic'))
        heading3.pack(pady=(7, 7))

        heading2 = Label(self.root, text="Not a member?", bg='#103092', fg='white')
        heading2.configure(font=('verdana', '10', 'italic'))
        heading2.pack(pady=(5,5))


        self.text = Button(self.root, width=10,text='Register',command=self.register)
        self.text.pack(pady=(5,5),ipady=3)


    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
    def register(self):
        self.clear()
        head1 = Label(self.root, text="Name", bg='#103092', fg='white')
        head1.configure(font=('verdana', '15', 'italic'))
        head1.pack()

        self.name = Entry(self.root, width=35)
        self.name.pack(pady=(10,10),ipady=3)

        head2 = Label(self.root, text="Enter email", bg='#103092', fg='white')
        head2.configure(font=('verdana', '15', 'italic'))
        head2.pack(pady=(10,10))

        self.email= Entry(self.root, width=35)
        self.email.pack(pady=(5,5),ipady=3)

        head3 = Label(self.root, text="Password", bg='#103092', fg='white')
        head3.configure(font=('verdana', '15', 'italic'))
        head3.pack(pady=(10, 10))

        self.password = Entry(self.root, width=35)
        self.password.pack(pady=(5,5),ipady=3)

        self.register_ = Button(self.root, width=35,text='Register Now',command=self.perform_registration)
        self.register_.pack(pady=(10, 10), ipady=3)

        self.regi = Button(self.root, width=35, text='already a member ? login Now',command=self.login_gui)
        self.regi.pack(pady=(10, 10), ipady=3)

    def home_gui(self):
        self.clear()

        heading = Label(self.root, text="NLPApp", bg='#103092', fg='white')
        heading.configure(font=('verdana', '24', 'italic'))
        heading.pack(pady=(30, 30))

        heading = Button(self.root, text="Sentiment analysis", bg='#103092', fg='white',command=self.sentiment_analysis)
        heading.configure(font=('verdana', '24', 'italic'))
        heading.pack(pady=(30, 30))

        heading = Button(self.root, text="Language detection", bg='#103092', fg='white',command=self.language_detection)
        heading.configure(font=('verdana', '24', 'italic'))
        heading.pack(pady=(30, 30))

        heading = Button(self.root, text="Headline Generation", bg='#103092', fg='white',command=self.headline_generation)
        heading.configure(font=('verdana', '24', 'italic'))
        heading.pack(pady=(30, 30))

    def headline_generation(self):
        self.clear()
        heading = Label(self.root, text="Headline generation", bg='#103092', fg='white')
        heading.configure(font=('verdana', '24', 'italic'))
        heading.pack(pady=(30, 30))

        self.text = Entry(self.root, width=50)
        self.text.pack(pady=(5, 5), ipady=10)

        heading = Button(self.root, text="generate  headline",bg='#103092',fg = 'white',command=self.headline_generation)
        heading.configure(font=('verdana', '20', 'italic'))
        heading.pack(pady=(20, 20))

        heading = Button(self.root, text="Back", bg='#103092', fg='white',command=self.home_gui)
        heading.configure(font=('verdana', '15', 'italic'))
        heading.pack(pady=(5, 5))

    def do_headline(self):
        text1 = self.text.get()
        response1 = self.api.headline_generation(text1)
        heading = Label(self.root, text=response1, bg='#103092', fg='white')
        heading.configure(font=('verdana', '20', 'italic'))
        heading.pack(pady=(5, 5))


    def language_detection(self):
        self.clear()
        heading = Label(self.root, text="Language Detection", bg='#103092', fg='white')
        heading.configure(font=('verdana', '24', 'italic'))
        heading.pack(pady=(30, 30))

        self.text = Entry(self.root, width=50)
        self.text.pack(pady=(5, 5), ipady=10)

        heading = Button(self.root, text="detect the language", bg='#103092', fg='white',command=self.do_language)
        heading.configure(font=('verdana', '20', 'italic'))
        heading.pack(pady=(20, 20))

        heading = Button(self.root, text="Back", bg='#103092', fg='white', command=self.home_gui)
        heading.configure(font=('verdana', '15', 'italic'))
        heading.pack(pady=(5, 5))

    def do_language(self):
        text1 = self.text.get()
        response1 = self.api.language_detection(text1)
        heading = Label(self.root, text=response1, bg='#103092', fg='white')
        heading.configure(font=('verdana', '20', 'italic'))
        heading.pack(pady=(5, 5))

    def sentiment_analysis(self):
        self.clear()
        heading = Label(self.root, text="Sentiment Analysis", bg='#103092', fg='white')
        heading.configure(font=('verdana', '24', 'italic'))
        heading.pack(pady=(30, 30))

        self.text = Entry(self.root, width=50)
        self.text.pack(pady=(5, 5), ipady=10)

        heading = Button(self.root, text="analyze the text ", bg='#103092', fg='white',command=self.do_sentiment_analysis)
        heading.configure(font=('verdana', '20', 'italic'))
        heading.pack(pady=(20, 20))

        heading = Button(self.root, text="Back", bg='#103092', fg='white', command=self.home_gui)
        heading.configure(font=('verdana', '15', 'italic'))
        heading.pack(pady=(5,5))


    def do_sentiment_analysis(self):
        text1 = self.text.get()
        response1 =self.api.sentiment(text1)
        heading = Label(self.root, text=response1, bg='#103092', fg='white')
        heading.configure(font=('verdana', '20', 'italic'))
        heading.pack(pady=(20, 20))

    def perform_registration(self):
        name = self.name.get()
        password = self.password.get()
        email = self.email.get()
        response = self.dbo.add_data(name,password,email)

        if response:
            messagebox.showinfo('success','registration successful')
            self.login_gui()
        else:
            messagebox.showerror('error','try again email already exists')

    def search(self):
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.search_info(email,password)
        if response == 1:
            messagebox.showinfo('success','login successful')
            self.home_gui()
        else:
            messagebox.showerror('error','Incorrect email/password')





ob = NLPApp()
