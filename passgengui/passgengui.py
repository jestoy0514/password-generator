#!/usr/bin/python
#
#  passgengui.py
#
#  Copyright (c) 2015 Jesus Vedasto Olazo <jestoy.olazo@gmail.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.


import Tkinter as tk
import ttk   
import string
import random
import tkMessageBox as mb


class MainApplication:

    def __init__(self, parent):
        self.parent = parent
        self.parent.protocol('WM_DELETE_WINDOW', self.app_exit_function)
        self.main_window()

    def main_window(self):
        """
        This is the user interface consisting of a menu bar,
        a frame for character sets, a frame where you can
        select the length of the password, and the generate
        button and output result.
        """
        #  Menu Bar
        self.menubar = tk.Menu(self.parent)
        self.parent.config(menu=self.menubar)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Exit", command=self.app_exit_function)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.helpmenu.add_command(label="About", command=self.about_dialog)

        # Character sets frame.
        self.chars_frame = ttk.LabelFrame(self.parent, text='Sets of Characters')
        self.chars_frame.pack(padx=5, pady=5, ipadx=5, ipady=5, expand='y', fill='both')
        self.intvar1 = tk.IntVar()
        self.intvar1.set(1)
        self.intvar2 = tk.IntVar()
        self.intvar2.set(0)
        self.intvar3 = tk.IntVar()
        self.intvar3.set(0)
        self.upper_char = ttk.Checkbutton(self.chars_frame, text='Capital Letters (A..Z)', variable=self.intvar1)
        self.upper_char.pack(anchor='w')
        self.lower_char = ttk.Checkbutton(self.chars_frame, text='Small Letters (a..z)', variable=self.intvar2)
        self.lower_char.pack(anchor='w')
        self.numer_char = ttk.Checkbutton(self.chars_frame, text='Numbers (0..9)', variable=self.intvar3)
        self.numer_char.pack(anchor='w')
        
        # Length of the pass word frame.
        self.length_frame = ttk.LabelFrame(self.parent, text='Length of the Password.')
        self.length_frame.pack(padx=5, pady=5, ipadx=5, ipady=5, expand='y', fill='both')
        self.spinvar = tk.IntVar()
        self.spinvar.set(8)
        self.length_spin = tk.Spinbox(self.length_frame, from_=0, to=16,)
        self.length_spin.pack(padx=5, pady=5)
        self.length_spin.config(textvariable=self.spinvar)
        
        #  Button & Entry frame.
        self.labelframe = ttk.LabelFrame(self.parent, text="Generate Password")
        self.labelframe.pack(padx=5, pady=5, ipadx=5, ipady=5, expand='y', fill='both', side='bottom')

        #  Generate Button
        self.resultbutton = ttk.Button(self.labelframe, text="Generate")
        self.resultbutton.grid(row=0, column=0, sticky="nesw", padx=5, pady=5)
        self.resultbutton.config(command=self.password_generator)

        #  Entry
        self.myvar = tk.StringVar()
        self.myvar.set("Please press the generate button!")
        self.resulttext = tk.Entry(self.labelframe, width=30, textvariable=self.myvar, justify="center")
        self.resulttext.grid(row=0, column=1, sticky="nesw", padx=5, pady=5)

    def password_generator(self):
        """
        This is where the generation of password will
        occur. It will take the data from the spinvar
        variable and will test if the it exceed to the
        maximum length of 16 characters. If not it will
        be generated using the selection characters variables
        and randomly selecting it.
        """
        if self.spinvar.get() > 16:
            mb.showinfo("Warning", "Invalid length of password.\nMaximum is 16.")
            self.length_spin.focus_set()
            return
            
        #  Generate password from letters & numbers.
        if self.intvar1.get() == 1 and self.intvar2.get() == 1 and self.intvar3.get() == 1:
            self.chars = string.ascii_letters + string.digits
        elif self.intvar1.get() == 1 and self.intvar2.get() == 1 and self.intvar3.get() == 0:
            self.chars = string.ascii_letters
        elif self.intvar1.get() == 0 and self.intvar2.get() == 0 and self.intvar3.get() == 1:
            self.chars = string.digits
        elif self.intvar1.get() == 1 and self.intvar2.get() == 0 and self.intvar3.get() == 0:
            self.chars = string.ascii_uppercase
        elif self.intvar1.get() == 1 and self.intvar2.get() == 0 and self.intvar3.get() == 1:
            self.chars = string.digits + string.ascii_uppercase
        elif self.intvar1.get() == 0 and self.intvar2.get() == 1 and self.intvar3.get() == 1:
            self.chars = string.digits + string.ascii_lowercase
        elif self.intvar1.get() == 0 and self.intvar2.get() == 1 and self.intvar3.get() == 0:
            self.chars = string.ascii_lowercase
        else:
            self.chars = " "
            
        self.password = ""
        self.pass_length = int(self.length_spin.get()) + 1
        for char in range(1, self.pass_length):
            self.password = self.password + random.choice(self.chars)   
        self.myvar.set(self.password)

    def app_exit_function(self):
        #  Exit option for the application.
        self.parent.destroy()
        
    def about_dialog(self):
        """
        This area will be the about dialog for the application.
        This includes the application name, version number,
        a description of the application, author's name, e-mail,
        and the license.
        """
        self.about = tk.Toplevel(self.parent)
        self.about.title('About')
        self.about.geometry('300x200')
        self.about_frame = tk.Frame(self.about)
        self.about_frame.pack()
        self.app_name = tk.Label(self.about_frame, text='Password Generator', font=('Times', 20, 'bold'))
        self.app_name.pack()
        self.app_version = tk.Label(self.about_frame, text='version: 1.0')
        self.app_version.pack()
        self.app_desc = tk.Label(self.about_frame, text='"A simple password generator."')
        self.app_desc.pack()
        self.app_author = tk.Label(self.about_frame, text='Author: Jesus Vedasto A. Olazo', font=('Times', 10,'bold'))
        self.app_author.pack()
        self.app_email = tk.Label(self.about_frame, text='E-mail: jestoy.olazo@gmail.com', font=('Times', 10,'bold'))
        self.app_email.pack()
        self.app_license = tk.Label(self.about_frame, text='License: GNU Public License v2', font=('Times', 10,'bold'))
        self.app_license.pack()
        self.close_button = ttk.Button(self.about_frame, text='Close', command=self.about.destroy)
        self.close_button.pack(pady=5, padx=5)

def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.title("Password Generator")
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()    

if __name__ == '__main__':
    main()
