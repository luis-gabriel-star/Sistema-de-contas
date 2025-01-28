import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib

def connect_db():
    return sqlite3.connect("users.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL
                    );''')
    conn.commit()
    conn.close()

def register_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        messagebox.showinfo("Sucesso", "Conta criada com sucesso!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "Usuário já existe!")
    finally:
        conn.close()

def login_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
    user = cursor.fetchone()
    conn.close()

    if user:
        messagebox.showinfo("Sucesso", "Login bem-sucedido!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos!")
      
def main_screen():
    def show_register_screen():
        register_screen()

    def show_login_screen():
        login_screen()

    root = tk.Tk()
    root.title("Sistema de Login e Registro")
    root.geometry("400x300")
    root.config(bg="#121212")

    label_title = tk.Label(root, text="Bem-vindo!", font=("Helvetica", 24), bg="#121212", fg="#f4f4f4")
    label_title.pack(pady=20)

    button_login = tk.Button(root, text="Login", width=20, height=2, command=show_login_screen, font=("Helvetica", 12), bg="#4CAF50", fg="white", relief="flat")
    button_login.pack(pady=10)

    button_register = tk.Button(root, text="Registrar", width=20, height=2, command=show_register_screen, font=("Helvetica", 12), bg="#2196F3", fg="white", relief="flat")
    button_register.pack(pady=10)

    root.mainloop()

def register_screen():
    def submit_registration():
        username = entry_username.get()
        password = entry_password.get()
        if username and password:
            register_user(username, password)
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    register_window = tk.Tk()
    register_window.title("Registrar Conta")
    register_window.geometry("400x300")
    register_window.config(bg="#121212")

    label_title = tk.Label(register_window, text="Criar Conta", font=("Helvetica", 24), bg="#121212", fg="#f4f4f4")
    label_title.pack(pady=20)

    label_username = tk.Label(register_window, text="Nome de usuário", font=("Helvetica", 12), bg="#f4f4f4")
    label_username.pack()
    entry_username = tk.Entry(register_window, font=("Helvetica", 12))
    entry_username.pack(pady=5)

    label_password = tk.Label(register_window, text="Senha", font=("Helvetica", 12), bg="#f4f4f4")
    label_password.pack()
    entry_password = tk.Entry(register_window, show="*", font=("Helvetica", 12))
    entry_password.pack(pady=5)

    button_submit = tk.Button(register_window, text="Registrar", width=20, height=2, command=submit_registration, font=("Helvetica", 12), bg="#4CAF50", fg="white", relief="flat")
    button_submit.pack(pady=20)

    register_window.mainloop()

def login_screen():
    def submit_login():
        username = entry_username.get()
        password = entry_password.get()
        if username and password:
            login_user(username, password)
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("400x300")
    login_window.config(bg="#121212")

    label_title = tk.Label(login_window, text="Login", font=("Helvetica", 24), bg="#121212", fg="#f4f4f4")
    label_title.pack(pady=20)

    label_username = tk.Label(login_window, text="Nome de usuário", font=("Helvetica", 12), bg="#f4f4f4")
    label_username.pack()
    entry_username = tk.Entry(login_window, font=("Helvetica", 12))
    entry_username.pack(pady=5)

    label_password = tk.Label(login_window, text="Senha", font=("Helvetica", 12), bg="#f4f4f4")
    label_password.pack()
    entry_password = tk.Entry(login_window, show="*", font=("Helvetica", 12))
    entry_password.pack(pady=5)

    button_submit = tk.Button(login_window, text="Entrar", width=20, height=2, command=submit_login, font=("Helvetica", 12), bg="#4CAF50", fg="white", relief="flat")
    button_submit.pack(pady=20)

    login_window.mainloop()

if __name__ == "__main__":
    create_table()
    main_screen()

