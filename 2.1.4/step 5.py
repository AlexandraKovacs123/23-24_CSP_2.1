#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

def test_my_button():
    if(ent_username.get() == "username" and ent_password.get() == "pass"):
        frame_auth.tkraise()

    else:
        fail_label = tk.Label(frame_login, text="Invalid user/pass combination")
        fail_label.pack()

# main window
root = tk.Tk()
root.wm_geometry("300x300")

# create empty frame
frame_login = tk.Frame(root)
frame_auth = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky="news")
frame_auth.grid(row=0, column=0, sticky="news")

lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_password = tk.Label(frame_login, text='Password:')
lbl_password.pack()

ent_password = tk.Entry(frame_login, bd=3, show="*")
ent_password.pack(pady=5)

btn_login = tk.Button(frame_login, text="Login", command=test_my_button)
btn_login.pack()

frame_login.tkraise()

label = tk.Label(frame_auth)



root.mainloop()