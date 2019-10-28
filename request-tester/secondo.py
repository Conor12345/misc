#!/usr/bin/env python3

import tkinter as tk
import requests

class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("200x230+1200+300")
        self.title("Light Controls")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in [Home]:
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Home)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Home(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)

        deskONButton = tk.Button(self, text="Desk Light ON", command=self.desk_light_on)
        deskONButton.pack()

        deskOFFButton = tk.Button(self, text="Desk Light OFF", command=self.desk_light_off)
        deskOFFButton.pack()

        L1 = tk.Label(self, text=" ")
        L1.pack()

        bedsideONButton = tk.Button(self, text="Bedside Light ON", command=self.bedside_light_on)
        bedsideONButton.pack()

        bedsideOFFButton = tk.Button(self, text="Bedside Light OFF", command=self.bedside_light_off)
        bedsideOFFButton.pack()

        L2 = tk.Label(self, text=" ")
        L2.pack()

        allONButton = tk.Button(self, text="All Lights ON", command=self.all_light_on)
        allONButton.pack()

        allOFFButton = tk.Button(self, text="All Lights OFF", command=self.all_light_off)
        allOFFButton.pack()

    def desk_light_on(self):
        r = requests.post('https://maker.ifttt.com/trigger/' + 'desk_light_on' + '/with/key/fQc9wPk6IwnJm0zSwpwYxo5MXreMprz8NfcmXIjwPWR',params={"value1": "None", "value2": "None", "value3": "None"})

    def desk_light_off(self):
        r = requests.post('https://maker.ifttt.com/trigger/' + 'desk_light_off' + '/with/key/fQc9wPk6IwnJm0zSwpwYxo5MXreMprz8NfcmXIjwPWR',params={"value1": "None", "value2": "None", "value3": "None"})

    def bedside_light_on(self):
        r = requests.post('https://maker.ifttt.com/trigger/' + 'bedside_light_on' + '/with/key/fQc9wPk6IwnJm0zSwpwYxo5MXreMprz8NfcmXIjwPWR',params={"value1": "None", "value2": "None", "value3": "None"})

    def bedside_light_off(self):
        r = requests.post('https://maker.ifttt.com/trigger/' + 'bedside_light_off' + '/with/key/fQc9wPk6IwnJm0zSwpwYxo5MXreMprz8NfcmXIjwPWR',params={"value1": "None", "value2": "None", "value3": "None"})

    def all_light_on(self):
        self.desk_light_on()
        self.bedside_light_on()

    def all_light_off(self):
        self.desk_light_off()
        self.bedside_light_off()

app = Main()
app.mainloop()
