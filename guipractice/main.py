import sqlite3
import tkinter as tk


class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("700x600+1200+300")
        self.title("Main")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.loggedInUser = ""

        self.frames = {}

        for F in [Login, viewActivities, viewPeople]:
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Login)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Login(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        L1 = tk.Label(self, text="Welcome to the activities database!")
        L1.pack()
        L2 = tk.Label(self, text="Please log in")
        L2.pack()

        uNameLabel = tk.Label(self, text="Username:")
        uNameLabel.pack()

        self.uNameBox = tk.Entry(self)
        self.uNameBox.pack()

        pWordLabel = tk.Label(self, text="Password:")
        pWordLabel.pack()

        self.pWordBox = tk.Entry(self, show="*")
        self.pWordBox.pack()

        submitButton = tk.Button(self, text="Submit", command=self.loginSubmit)
        submitButton.pack()

        self.loginFeedback = tk.Label(self, text="", foreground="red")
        self.loginFeedback.pack()

    def loginSubmit(self):
        new_db = sqlite3.connect("activitiesDatabase.db")
        c = new_db.cursor()
        result = c.execute("SELECT * FROM tblUsers WHERE username = ?", (self.uNameBox.get(),))

        result = result.fetchall()
        if len(result) == 0:
            self.loginFeedback.config(text="Error - Unknown User")
        else:
            if self.pWordBox.get() == result[0][1]:
                self.loginFeedback.config(text="")
                self.controller.show_frame(viewActivities)
            else:
                self.loginFeedback.config(text="Error - Incorrect password")

class viewActivities(tk.Frame):
    def __init__(self,parent,controller):
        self.controller = controller
        tk.Frame.__init__(self,parent)

        TitleLabel = tk.Label(self, text="View or Edit Activities - Form View")
        TitleLabel.grid(row=2, column=0, columnspan=4, sticky="NSWE")
        TitleLabel.config(font=("Arial", 24))

        self.rowconfigure(3, minsize=30) # row 3 is blank, so we set a minimum height
        self.columnconfigure(1, minsize=10)
        self.columnconfigure(3, weight=1)

        label_0 = tk.Label(self, text="ID:")  # a plain label for the ID box
        label_0.grid(row=4, column=0, sticky="E")

        self.ID = tk.StringVar()  # For this field, we will create a StringVar (See Firefly page for description)
        self.IDBox = tk.Entry(self, textvariable=self.ID) # we link this Entry box to the textvariable
        self.IDBox.grid(row=4, column=2, sticky = "W")


        # Same again for the ActivityName box and label
        label_1 = tk.Label(self, text="Activity Name:")
        label_1.grid(row=5, column=0, sticky="E")

        self.activityName = tk.StringVar()
        self.activityNameBox = tk.Entry(self, textvariable=self.activityName)
        self.activityNameBox.grid(row=5, column=2, sticky = "W")

        #Enter code for the other Entry Boxes and labels here.
        label_2 = tk.Label(self, text="Description:")
        label_2.grid(row=6, column=0, sticky="E")

        self.activityDescription = tk.StringVar()
        self.descriptionBox = tk.Entry(self, textvariable=self.activityDescription)
        self.descriptionBox.grid(row=6, column=2, sticky="W")

        label_3 = tk.Label(self, text="Day:")
        label_3.grid(row=7, column=0, sticky="E")

        self.activityDay = tk.StringVar()
        self.dayBox = tk.Entry(self, textvariable=self.activityDay)
        self.dayBox.grid(row=7, column=2, sticky="W")

        label_4 = tk.Label(self, text="Time:")
        label_4.grid(row=8, column=0, sticky="E")

        self.activityTime = tk.StringVar()
        self.timeBox = tk.Entry(self, textvariable=self.activityTime)
        self.timeBox.grid(row=8, column=2, sticky="W")

        buttonFrame= tk.Frame(self)
        buttonFrame.grid(row=10,column=0, columnspan=4, sticky="NSEW")

        prevBtn = tk.Button(buttonFrame, text="<< Previous", command = self.prev)
        prevBtn.grid(row=10,column=0) # Row 10 to give enough room for all the fields above

        newBtn = tk.Button(buttonFrame, text="Create New", command=self.new)
        newBtn.grid(row=10, column=2)

        # add 3 more buttons for Saving Changes, Delete and Next
        saveBtn = tk.Button(buttonFrame, text="Save Changes", command=self.saveData)
        saveBtn.grid(row=10, column=3)

        deleteBtn = tk.Button(buttonFrame, text="Delete", command=self.deleteData)
        deleteBtn.grid(row=10, column=4)

        nextBtn = tk.Button(buttonFrame, text="Next", command=self.next)
        nextBtn.grid(row=10, column=5)

        for i in range(0,5):
            buttonFrame.columnconfigure(i, weight=1)

        self.refreshData()
        self.recnum = 0
        self.showRecord()

        changeFrame = tk.Frame(self)
        changeFrame.grid(row=15, column=0, columnspan=4, sticky="S")

        activityBtn = tk.Button(changeFrame, text="View People", command=lambda: self.changeFrame(viewPeople))
        activityBtn.grid(row=20, column=3)

    def refreshData(self):
        db = sqlite3.connect("activitiesDatabase.db")
        c = db.cursor()

        result = c.execute("SELECT * FROM tblActivities")
        self.data = result.fetchall()

    def showRecord(self):
        self.ID.set(self.data[self.recnum][0])
        self.activityName.set(self.data[self.recnum][1])
        self.activityDescription.set(self.data[self.recnum][4])
        self.activityDay.set(self.data[self.recnum][2])
        self.activityTime.set(self.data[self.recnum][3])

    def next(self):
        self.recnum = (self.recnum + 1) %  len(self.data)
        self.showRecord()

    def prev(self):
        self.recnum = (self.recnum - 1) %  len(self.data)
        self.showRecord()

    def new(self):
        self.ID.set("")
        self.activityName.set("")
        self.activityDescription.set("")
        self.activityDay.set("")
        self.activityTime.set("")
        self.recnum = -1

    def saveData(self):
        db = sqlite3.connect("activitiesDatabase.db")
        c = db.cursor()  # and get a cursor as before
        if self.recnum == -1:
            # this is a new activity
            if self.ID.get() in [str(activity[0]) for activity in self.data]:
                tk.messagebox.showerror("Error", "That ID Number exists")
                return
            else:
                c.execute("INSERT INTO tblActivities VALUES (?,?,?,?, ?)", [self.ID.get(),
                    self.activityName.get(), self.activityDay.get(), self.activityTime.get(),
                                                                            self.activityDescription.get()])
                self.recnum = len(self.data)
                self.refreshData()

        else:
            c.execute("UPDATE tblActivities SET ActivityID = ?, activityName = ?, activityDay = ?, activityTime = ?,"
                      " activityDescription = ? WHERE activityID = ?", [self.ID.get(), self.activityName.get(),
                      self.activityDay.get(), self.activityTime.get(), self.activityDescription.get(),
                      self.data[self.recnum][0]])
        db.commit()
        self.refreshData()

    def deleteData(self):
        db = sqlite3.connect("activitiesDatabase.db")
        c = db.cursor()
        c.execute("DELETE FROM tblActivities WHERE activityID = ?", (self.ID.get(),))
        db.commit()
        self.recnum = 0
        self.refreshData()
        self.showRecord()

    def changeFrame(self, frame):
        self.controller.show_frame(frame)


class viewPeople(tk.Frame):
    def __init__(self,parent,controller):
        self.controller = controller
        tk.Frame.__init__(self,parent)

        TitleLabel = tk.Label(self, text="View or Edit People - Form View")
        TitleLabel.grid(row=2, column=0, columnspan=4, sticky="NSWE")
        TitleLabel.config(font=("Arial", 24))

        self.rowconfigure(3, minsize=30) # row 3 is blank, so we set a minimum height
        self.columnconfigure(1, minsize=10)
        self.columnconfigure(3, weight=1)

        label_0 = tk.Label(self, text="ID:")  # a plain label for the ID box
        label_0.grid(row=4, column=0, sticky="E")

        self.ID = tk.StringVar()  # For this field, we will create a StringVar (See Firefly page for description)
        self.IDBox = tk.Entry(self, textvariable=self.ID) # we link this Entry box to the textvariable
        self.IDBox.grid(row=4, column=2, sticky = "W")


        # Same again for the ActivityName box and label
        label_1 = tk.Label(self, text="Firstname:")
        label_1.grid(row=5, column=0, sticky="E")

        self.firstname = tk.StringVar()
        self.firstnameBox = tk.Entry(self, textvariable=self.firstname)
        self.firstnameBox.grid(row=5, column=2, sticky = "W")

        #Enter code for the other Entry Boxes and labels here.
        label_2 = tk.Label(self, text="Surname:")
        label_2.grid(row=6, column=0, sticky="E")

        self.surname = tk.StringVar()
        self.surnameBox = tk.Entry(self, textvariable=self.surname)
        self.surnameBox.grid(row=6, column=2, sticky="W")

        label_3 = tk.Label(self, text="Form:")
        label_3.grid(row=7, column=0, sticky="E")

        self.form = tk.StringVar()
        self.formBox = tk.Entry(self, textvariable=self.form)
        self.formBox.grid(row=7, column=2, sticky="W")

        buttonFrame= tk.Frame(self)
        buttonFrame.grid(row=10,column=0, columnspan=4, sticky="NSEW")

        prevBtn = tk.Button(buttonFrame, text="<< Previous", command = self.prev)
        prevBtn.grid(row=10,column=0) # Row 10 to give enough room for all the fields above

        newBtn = tk.Button(buttonFrame, text="Create New", command=self.new)
        newBtn.grid(row=10, column=2)

        # add 3 more buttons for Saving Changes, Delete and Next
        saveBtn = tk.Button(buttonFrame, text="Save Changes", command=self.saveData)
        saveBtn.grid(row=10, column=3)

        deleteBtn = tk.Button(buttonFrame, text="Delete", command=self.deleteData)
        deleteBtn.grid(row=10, column=4)

        nextBtn = tk.Button(buttonFrame, text="Next", command=self.next)
        nextBtn.grid(row=10, column=5)

        for i in range(0,5):
            buttonFrame.columnconfigure(i, weight=1)

        self.refreshData()
        self.recnum = 0
        self.showRecord()

        changeFrame = tk.Frame(self)
        changeFrame.grid(row=15, column=0, columnspan=4, sticky="S")

        activityBtn = tk.Button(changeFrame, text="View Activities", command=lambda: self.changeFrame(viewActivities))
        activityBtn.grid(row=20, column=3)

    def refreshData(self):
        db = sqlite3.connect("activitiesDatabase.db")
        c = db.cursor()

        result = c.execute("SELECT * FROM tblPeople")
        self.data = result.fetchall()

    def showRecord(self):
        self.ID.set(self.data[self.recnum][0])
        self.firstname.set(self.data[self.recnum][1])
        self.surname.set(self.data[self.recnum][2])
        self.form.set(self.data[self.recnum][3])

    def next(self):
        self.recnum = (self.recnum + 1) %  len(self.data)
        self.showRecord()

    def prev(self):
        self.recnum = (self.recnum - 1) %  len(self.data)
        self.showRecord()

    def new(self):
        self.ID.set("")
        self.firstname.set("")
        self.surname.set("")
        self.form.set("")
        self.recnum = -1

    def saveData(self):
        db = sqlite3.connect("activitiesDatabase.db")
        c = db.cursor()  # and get a cursor as before
        if self.recnum == -1:
            # this is a new activity
            if self.ID.get() in [str(activity[0]) for activity in self.data]:
                tk.messagebox.showerror("Error", "That ID Number exists")
                return
            else:
                c.execute("INSERT INTO tblPeople VALUES (?,?,?,?)", [self.ID.get(),
                    self.firstname.get(), self.surname.get(), self.form.get()])
                self.recnum = len(self.data)
                self.refreshData()

        else:
            c.execute("UPDATE tblPeople SET personID = ?, firstname = ?, surname = ?, form = ?, WHERE activityID = ?", [self.ID.get(), self.firstname.get(),
                      self.surname.get(), self.form.get(), self.data[self.recnum][0]])
        db.commit()
        self.refreshData()

    def deleteData(self):
        db = sqlite3.connect("activitiesDatabase.db")
        c = db.cursor()
        c.execute("DELETE FROM tblpeople WHERE personID = ?", (self.ID.get(),))
        db.commit()
        self.recnum = 0
        self.refreshData()
        self.showRecord()

    def changeFrame(self, frame):
        self.controller.show_frame(frame)

app = Main()
app.mainloop()



