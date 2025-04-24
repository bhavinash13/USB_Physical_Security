import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image
from datetime import datetime
import subprocess
import webbrowser
import os
import sqlite3
import hashlib
import sys

root = tk.Tk()
root.geometry("410x240")
root.configure(bg="#00ffff")
root.title("Login/Register Form")
root.resizable(False,False)
global admin_password
admin_password = "cyberpasscode"
script_dir = os.path.dirname(os.path.abspath(__file__))
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle
    base_path = sys._MEIPASS
else:
    # If the application is run as a script
    base_path = os.path.dirname(os.path.abspath(__file__))
#============================================

# SQLite3 database connection
conn = sqlite3.connect('login_database.db')
c = conn.cursor()
# Users table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT)''')
conn.commit()
#============================================
# Login frame


#script_dir = os.path.dirname(os.path.abspath(__file__))
my_image_path = os.path.join(base_path, "Anonymous.png")
#my_image_path="Anonymous.png"
#my_image_path=Image.open(r"C:\Users\Bhavinash\Downloads\Usb project\Anonymous.png")
my_image = Image.open(my_image_path)
my_image=my_image.resize((150,100))
photo=ImageTk.PhotoImage(my_image)
my_label=tk.Label(root,image=photo)
my_label.image=photo
my_label.grid(row=1,column=1)

tk.Label(root, text="Username:",bg="#00ffff",fg="#000033",font=("Harlow Solid Italic",11)).grid(row=2, column=0)
username_entry = tk.Entry(root, width=20)
username_entry.grid(row=2, column=1)

tk.Label(root, text="Password:",bg="#00ffff",fg="#000033",font=("Harlow Solid Italic",11)).grid(row=3, column=0)
password_entry = tk.Entry(root, width=20, show="*")
password_entry.grid(row=3, column=1)
    
def record_login_time():
    # Get the current date and time
   now = datetime.now()
   formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    # Append the timestamp to the log file
   with open('app.log', 'a') as log_file:
       log_file.write(f"Login time: {formatted_time}\n")

def login():
    username = username_entry.get()
    password = password_entry.get()
    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # Check if the username and password match
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
    row = c.fetchone()
    if row:
        record_login_time()
        messagebox.showinfo("Login", "Login successful!")
        USBPage()
    else:
        messagebox.showerror("Login", "Invalid username or password")
    
def register():
    #New window for registration
    register_window = tk.Toplevel(root)
    register_window.title("Register")
    register_window.configure(bg="#ffcccc")
    register_window.geometry("320x160")
    register_window.resizable(False,False)

    tk.Label(register_window, text="Username:",bg="#ffcccc",font=("Harlow Solid Italic",12)).grid(row=0, column=0)
    username_entry = tk.Entry(register_window, width=20)
    username_entry.grid(row=0, column=1)

    tk.Label(register_window, text="Password:",bg="#ffcccc",font=("Harlow Solid Italic",12)).grid(row=1, column=0)
    password_entry = tk.Entry(register_window, width=20, show="*")
    password_entry.grid(row=1, column=1)

    tk.Label(register_window, text="Confirm Password:",bg="#ffcccc",font=("Harlow Solid Italic",12)).grid(row=2, column=0)
    confirm_password_entry = tk.Entry(register_window, width=20, show="*")
    confirm_password_entry.grid(row=2, column=1)

    tk.Label(register_window, text="Admin Pass: ",bg="#ffcccc",font=("Harlow Solid Italic",12)).grid(row=3,column=0)
    admin_pass_entry = tk.Entry(register_window,width=20, show="*")
    admin_pass_entry.grid(row=3,column=1)

    def register_user():
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()
        admin_pass = admin_pass_entry.get()
        if admin_pass!= admin_password:
            messagebox.showerror("Admin Pass", "Pass do not match try again..")
            return

        if password!= confirm_password:
            messagebox.showerror("Register", "Passwords do not match")
            return
            # Hash the password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

            # Insert the user into the database
        c.execute("INSERT INTO users (username, password) VALUES (?,?)", (username, hashed_password))
        conn.commit()

        messagebox.showinfo("Register", "Registration successful!")
        register_window.destroy()

    tk.Button(register_window, text="Register",bg="#ff8080", command=register_user,font=("Harlow Solid Italic",10)).grid(row=4, column=1, columnspan=2)

tk.Button(root, text="Login",bg="#ffff99", command=login,font=("Script MT Bold",11)).grid(row=4, column=1)
tk.Button(root, text="Register",bg="#00e6e6", command=register,font=("Script MT Bold",10)).grid(row=4, column=0)
#====================================

def USBPage():
    usbpage = tk.Toplevel()
    usbpage.geometry("610x697")
    usbpage.title("USB Physical Security")
    usbpage.resizable(False,False)
    usbpage.configure(bg="#000033")

    def htmlpage():
        f = open('GFG.html', 'w') 

        # html code will go in the file GFG.html 
        html_template = """
        <html>
        <head>
        <title>Project Profile</title>
        <meta name="viewport" width="device-width, initial-scale=1.0">

        </head>
        <style>
        table, th, td {
        border:1px solid black;
        }
        #myheader{
        text-align: center;
        font-family: Arial, Helvetica, sans-serif;
        }
        </style>
        <body>
        <bold><h1 id="myheader">Project Profile</h1></bold>
        <h1 style="color:red">USB Physical Security</h1>
        <h2>Project Overview:</h2>
        <p>The USB Physical Security System is designed to enhance the security of computer systems by controlling access to USB ports. This project provides a mechanism to block or unblock USB ports, thereby preventing unauthorized use of USB devices. The system is particularly useful in environments where data security is paramount, such as corporate offices, educational institutions, and government agencies.</p>
        <h2>Details of developers:</h2>
        <table size="width:100">
        <tr>
        <th>Name of the developer</th>
        <th>Profession</th>
        <th>College</th>
        </tr>
        <tr>
        <td>Bhavinash</td>
        <td>Student</td>
        <td>Prasad V Potluri Siddhartha Institute Of Technology,Vijayawada</td>
        </tr>
        <tr>
        <td>Lakshmi Manasa</td>
        <td>Student</td>
        <td>Prasad V Potluri Siddhartha Institute Of Technology,Vijayawada</td>
        </tr>
        </table>

        <br>
        <h2>Company Details: </h2>
        <ul>
        <li><h4>Name of the Company:</h4> Supraja Technologies</li>
        <li><h4>Details about company:</h4>  </li>

        </ul>
        <p>As a part of intern in Supraja Technologies, we developed a project Usb physical Security system that can used to block the usb port of a system also used maily to enable and disable the ports. Not only that we also add some enhancements to the project idea and you can view the project for more information.</p>
        <p id="myheader">The USB Physical Security System provides a robust solution for managing USB port access, enhancing the security of computer systems by preventing unauthorized use of USB devices.</p>
        </body>
        </html>
        """

        # writing the code into the file 
        f.write(html_template) 

        # close the file 
        f.close() 

        # method how to open html files in chrome
        filename = 'file:///'+os.getcwd()+'/' + 'GFG.html'
        webbrowser.open_new_tab(filename) 


    profilepg=tk.Button(usbpage, text="Profile Page", fg="#00ffff", bg="black", command=htmlpage, width=15, height=2, font=("Algerian",12))
    profilepg.place(x=224,y=55)

    
    #script_dir = os.path.dirname(os.path.abspath(__file__))
    my_image_path = os.path.join(base_path, "Anonymous.png")
    #my_image_path="Anonymous.png"
    #my_image_path=Image.open(r"C:\Users\Bhavinash\Downloads\Usb project\Anonymous.png")
    my_image = Image.open(my_image_path)
    my_image=my_image.resize((260,170))
    photo=ImageTk.PhotoImage(my_image)
    my_label=tk.Label(usbpage,image=photo)
    my_label.image=photo
    my_label.place(x=320,y=140)

    
    #script_dir1 = os.path.dirname(os.path.abspath(__file__))
    my_image_path1 = os.path.join(base_path, "USB_pendrive.png")
    #my_image_path1="USB_pendrive.png"
    #my_image_path1=Image.open(r"C:\Users\Bhavinash\Downloads\Usb project\USB_pendrive.png")
    my_image1 = Image.open(my_image_path1)
    my_image1=my_image1.resize((260,170))
    photo1=ImageTk.PhotoImage(my_image1)
    my_label1=tk.Label(usbpage,image=photo1)
    my_label1.image=photo1
    my_label1.place(x=40,y=140)

    title=tk.Label(usbpage, text="USB Physical Security Application",bg="#000033",fg="white",font=("Script MT Bold",14)).place(x=190,y=350)

    ##=================================================
    def record_login_time():
    # Get the current date and time
       now = datetime.now()
       formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    # Append the timestamp to the log file
       with open('app.log', 'a') as log_file:
          log_file.write(f"Login time: {formatted_time}\n")


    def create_password_window(title, ok_command):
        password_window = tk.Toplevel(usbpage)
        password_window.title(title)
        password_window.geometry("300x200")

        password_label = tk.Label(password_window, text="Enter Password:")
        password_label.pack()

        password_entry = tk.Entry(password_window, show="*")
        password_entry.pack()

        def ok_button():
            if password_entry.get() == admin_password:
                ok_command()
                record_login_time()
                password_window.destroy()
            else:
                messagebox.showerror("Incorrect Password", "Incorrect password. Please try again.")
                password_entry.delete(0, tk.END)

        ok_button = tk.Button(password_window, text="OK", command=ok_button)
        ok_button.pack()

    # the function to be executed when the enable button is clicked
    def button2_clicked():
        def enable_usb_ports():
            try:
                #subprocess.run([r'C:\Users\Bhavinash\Downloads\Usb project\unblock_usb.bat'], shell=True)
                #subprocess.run([os.path.join(base_path, "unblock_usb.bat")], shell=True)
                #subprocess.run([os.path.join(base_path, "unblock_usb.bat")], shell=True, check=True)
                subprocess.run([os.path.abspath(os.path.join(base_path, "unblock_usb.bat"))], shell=True, check=True)
                #subprocess.run([os.path.join(script_dir, "unblock_usb.bat")], shell=True)
                #os.system(os.path.join(base_path, "unblock_usb.bat"))
                success_label.config(text="USB Ports Enabled Successfully")
            except subprocess.CalledProcessError as e:
                print(f"Error executing unblock_usb.bat: {e}")
                messagebox.showerror("Error", "Failed to enable USB ports. Check permissions and paths.")
            except Exception as e:
                print(f"Error executing unblock_usb.bat: {e}")
                messagebox.showerror("Error", "Failed to enable USB ports. Check permissions and paths.")
        #subprocess.run([r'C:\Users\Bhavinash\Downloads\Usb project\unblock_usb.bat'], shell=True)
        #success_label.config(text="USB Ports Enabled Successfully")

        create_password_window("Enable USB Ports", enable_usb_ports)

    # the function to be executed when the disable button is clicked
    def button1_clicked():
        def disable_usb_ports():
            try:
                #subprocess.run([r'C:\Users\Bhavinash\Downloads\Usb project\block_usb.bat'], shell=True)
                #subprocess.run([os.path.join(base_path, "block_usb.bat")], shell=True)
                #subprocess.run([os.path.join(script_dir, "block_usb.bat")], shell=True)
                #subprocess.run([os.path.join(base_path, "block_usb.bat")], shell=True, check=True)
                subprocess.run([os.path.abspath(os.path.join(base_path, "block_usb.bat"))], shell=True, check=True)
                #os.system(os.path.join(base_path, "block_usb.bat"))
                success_label.config(text="USB Ports Disabled Successfully")
            except subprocess.CalledProcessError as e:
                print(f"Error executing block_usb.bat: {e}")
                messagebox.showerror("Error", "Failed to disable USB ports. Check permissions and paths.")
            except Exception as e:
                print(f"Error executing block_usb.bat: {e}")
                messagebox.showerror("Error", "Failed to disable USB ports. Check permissions and paths.")
        #subprocess.run([r'C:\Users\Bhavinash\Downloads\Usb project\block_usb.bat'], shell=True)
        #uccess_label.config(text="USB Ports Disabled Successfully")

        create_password_window("Disable USB Ports", disable_usb_ports)

    def Log_events():
        def display_log():
            try:
                with open('app.log', 'r') as log_file:
                   log_content = log_file.read()
                   log_text.delete(1.0, tk.END)  # Clear existing text
                   log_text.insert(tk.END, log_content)
            except FileNotFoundError:
                   log_text.delete(1.0, tk.END)
                   log_text.insert(tk.END, "Log file not found.")
        log_bt= tk.Toplevel(usbpage)
        log_bt.title("Log Events with Time stamps")
        log_bt.geometry("350x390")
        log_button = tk.Button(log_bt, text="Show Log", bg="#3385ff",fg="white",command=display_log, font=("Harlow Solid Italic", 12))
        log_button.pack()

        # widget to display log content
        log_text = tk.Text(log_bt, height=10, width=40)
        log_text.pack()

    todisable=tk.Button(usbpage, text="Disable", fg="#ffff4d",bg="red", command=button1_clicked, width=13, height=2, font=("Eras Demi ITC", 12))
    todisable.place(x=90,y=400)

    toenable = tk.Button(usbpage, text="Enable", fg="red", bg="#ffff4d", command=button2_clicked, width=13, height=2, font=("Eras Demi ITC", 12))
    toenable.place(x=390,y=400)

    success_label = tk.Label(usbpage, text="", font=("Arial", 12), bg="#f2f2f2", fg="#ff0000")
    success_label.pack()
    
    log=tk.Button(usbpage,text="Log/Events",command=Log_events,fg="#ff4d4d",bg="white",font=("Harlow Solid Italic", 12)).place(x=270,y=590)
    
#=================================================================

head=tk.Label(root, text="Login/Register Form",bg="#00ffff",fg="#000033",font=("Script MT Bold",11)).grid(row=0,column=0)
#btn = tk.Button(root,text="Login",command=USBPage).grid(row=0,column=3)


root.mainloop()
