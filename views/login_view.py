# Kelompok 4
import customtkinter as ctk

class LoginView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login Sistem Penyewaan Kendaraan")
        self.geometry("400x350")
        self.resizable(False, False)
        
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=20, padx=40, fill="both", expand=True)
        
        ctk.CTkLabel(self.frame, text="LOGIN SISTEM", font=("Arial", 20, "bold")).pack(pady=25)
        
        self.entry_username = ctk.CTkEntry(self.frame, placeholder_text="Username")
        self.entry_username.pack(pady=12, padx=10, fill="x")
        
        # Parameter show="*" menyembunyikan karakter password
        self.entry_password = ctk.CTkEntry(self.frame, placeholder_text="Password", show="*")
        self.entry_password.pack(pady=12, padx=10, fill="x")
        
        self.btn_login = ctk.CTkButton(self.frame, text="Masuk", fg_color="blue")
        self.btn_login.pack(pady=25, padx=10, fill="x")