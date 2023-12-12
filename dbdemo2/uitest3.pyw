#!/usr/bin/python3
import tkinter as tk
import pymysql
from tkinter import messagebox

class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.configure(height=200, width=200)
        toplevel1.geometry("352x288")
        toplevel1.title("Tkinter Demo 2")
        label1 = tk.Label(toplevel1)
        label1.configure(
            cursor="arrow",
            font="{Verdana} 11 {}",
            justify="left",
            state="normal",
            text='Employees Management')
        label1.place(
            anchor="nw",
            relwidth=0.86,
            relx=0.06,
            rely=0.17,
            x=0,
            y=0)
        label2 = tk.Label(toplevel1)
        label2.configure(justify="left", text='First Name')
        label2.place(anchor="nw", relx=0.13, rely=0.39, x=0, y=0)
        entry1 = tk.Entry(toplevel1)
        self.fi = tk.StringVar()
        entry1.configure(
            justify="left",
            state="normal",
            takefocus=False,
            textvariable=self.fi)
        entry1.place(relwidth=0.55, relx=0.35, rely=0.39, x=0, y=0)
        button1 = tk.Button(toplevel1)
        button1.configure(
            background="#ffff80",
            font="{Algerian} 11 {}",
            foreground="#0080ff",
            overrelief="flat",
            text='submit')
        button1.place(
            relheight=0.08,
            relwidth=0.44,
            relx=0.43,
            rely=0.88,
            x=0,
            y=0)
        button1.configure(command=self.addrecord)
        label4 = tk.Label(toplevel1)
        label4.configure(text='Year hired')
        label4.place(anchor="nw", relx=0.13, rely=0.69, x=0, y=0)
        label5 = tk.Label(toplevel1)
        label5.configure(text='Department')
        label5.place(anchor="nw", relx=0.13, rely=0.59, x=0, y=0)
        label6 = tk.Label(toplevel1)
        label6.configure(text='Last Name')
        label6.place(anchor="nw", relx=0.13, rely=0.49, x=0, y=0)
        entry2 = tk.Entry(toplevel1)
        self.la = tk.StringVar()
        entry2.configure(textvariable=self.la)
        entry2.place(
            anchor="nw",
            relwidth=0.55,
            relx=0.35,
            rely=0.49,
            x=0,
            y=0)
        entry3 = tk.Entry(toplevel1)
        self.de = tk.StringVar()
        entry3.configure(textvariable=self.de)
        entry3.place(
            anchor="nw",
            relwidth=0.55,
            relx=0.35,
            rely=0.59,
            x=0,
            y=0)
        entry4 = tk.Entry(toplevel1)
        self.ye = tk.StringVar()
        entry4.configure(textvariable=self.ye)
        entry4.place(
            anchor="nw",
            relwidth=0.55,
            relx=0.35,
            rely=0.69,
            x=0,
            y=0)

        # Main widget
        self.mainwindow = toplevel1
        # Main menu
        _main_menu = self.create_menu2(self.mainwindow)
        self.mainwindow.configure(menu=_main_menu)

    def run(self):
        self.mainwindow.mainloop()

    def create_menu2(self, master):
        menu2 = tk.Menu(master)
        submenu1 = tk.Menu(menu2, cursor="arrow")
        menu2.add(tk.CASCADE, menu=submenu1, columnbreak=False, label='File')
        submenu1.add("command", label='command1')
        submenu1.add("command", label='command2')
        submenu1.add("command", label='command3')
        submenu2 = tk.Menu(menu2, relief="groove", takefocus=False)
        menu2.add(tk.CASCADE, menu=submenu2, label='Edit')
        submenu2.add("command", label='command4')
        submenu2.add("command", label='command5')
        return menu2

    def addrecord(self):
        try:
            connection = pymysql.connect(
                host="localhost", #10.241.42.218
                user="eyadmin",
                password="123",
                database="eygds"
            )
            cursor = connection.cursor()
            f = self.fi.get()
            l = self.la.get()
            d = self.de.get()
            y = self.ye.get()

            sql = f"""
                insert into employees 
                (firstname,lastname,department,yearhired)
                values
                ('{f}','{l}','{d}',{y})
            """
            cursor.execute(sql)
            connection.commit()
            messagebox.showinfo("","SUCCESS!")
        except Exception as e:
            messagebox.showerror("Error",f"{e}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()


if __name__ == "__main__":
    app = NewprojectApp()
    app.run()
