import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import statbotics

#woxicDEV - 2023
#İnstagram : @mert.js_ - @woxicdev
#Yardımcı olması için yorum satırları ekledim,değişken isimlerini sade bir şekilde yazdım.
#Veriler için gerekli olan kısımlar statbotics sitesinin API dökümanlarında mevcut.
#Link:https://www.statbotics.io/api/python

def open_blue_alliance():
    team_number = entry_team_number.get()
    blue_alliance_link = f"https://www.thebluealliance.com/team/{team_number}"
    webbrowser.open(blue_alliance_link)

def open_first_inspires():
    team_number = entry_team_number.get()
    first_inspires_link = f"https://frc-events.firstinspires.org/2023/team/{team_number}"
    webbrowser.open(first_inspires_link)

def get_team_info():
    try:
        team_number = int(entry_team_number.get())
        team_info = sb.get_team(team_number)

        text_box.config(state=tk.NORMAL)
        text_box.delete(1.0, tk.END)

        for key, value in team_info.items():
            if key == 'name':
                text_box.insert(tk.END, f"Takım Adı: {value}\n", 'bold')
            elif key == 'state':
                text_box.insert(tk.END, f"Konum: {value}\n", 'bold')
            elif key == 'rookie_year':
                text_box.insert(tk.END, f"Rookie Yılı: {value}\n", 'bold')
            else:
                text_box.insert(tk.END, f"{key.capitalize()}: {value}\n", 'bold')

        text_box.config(state=tk.DISABLED)

        button_blue_alliance.config(state=tk.NORMAL)
        button_first_inspires.config(state=tk.NORMAL)

    except ValueError:
        text_box.config(state=tk.NORMAL)
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, "Geçerli bir takım numarası girmediniz.", 'error')
        text_box.config(state=tk.DISABLED)
        button_blue_alliance.config(state=tk.DISABLED)
        button_first_inspires.config(state=tk.DISABLED)

def insert_colored_text(widget, text, color):
    widget.insert(tk.END, text, color)
    widget.tag_add(color, 'insert-1c', 'insert')
    widget.tag_configure(color, foreground=color)

# Nesne oluşturdum
sb = statbotics.Statbotics()

root = tk.Tk()
root.title("Takım Bilgi Sorgulama - WoxicDEV")

# Sekmeye logoyu ekledim.
logoo = tk.PhotoImage(file="logooo.png")  
root.tk.call('wm', 'iconphoto', root._w, logoo)

# Arka plan rengini gri yap
root.configure(bg="gray")

label_team_number = tk.Label(root, text="Takım Numarası:", fg="white", bg="black")
label_team_number.pack(pady=5)

entry_team_number = tk.Entry(root)
entry_team_number.pack(pady=5)

button_get_info = tk.Button(root, text="Bilgi Al", command=get_team_info, bg="white", fg="black")
button_get_info.pack(pady=10)

label_result = tk.Label(root, text="Sonuç:", fg="white", bg="gray")
label_result.pack(pady=5)

#   Önemli Stil Kısımları vb.
style = ttk.Style()
style.configure('TButton', borderwidth=2, relief="flat", foreground="black", background="white", font=('Helvetica', 10, 'bold'))

text_box = tk.Text(root, height=22, width=50, state=tk.DISABLED, bg="white", fg="black", relief=tk.GROOVE, borderwidth=2)
text_box.pack(pady=10)

button_blue_alliance = ttk.Button(root, text="Takımın Blue Alliance Sayfasına Git", command=open_blue_alliance, state=tk.DISABLED)
button_blue_alliance.pack(pady=5)

button_first_inspires = ttk.Button(root, text="Takımın First Inspires Sayfasına Git", command=open_first_inspires, state=tk.DISABLED)
button_first_inspires.pack(pady=5)

def about():
    messagebox.showinfo("Hakkında", "WoxicDev - 2023\n\nLinkedIn: Mert Ali Kaya - Github: majestyy01")

button_about = ttk.Button(root, text="Hakkında", command=about, style='TButton')
button_about.pack(pady=5)

label_about = tk.Label(root, text="WoxicDev - 2023", font=("Helvetica", 8, "bold"), fg="white", bg="black")
label_about.pack(side=tk.BOTTOM, pady=5)

text_box.tag_configure('bold', font=('Helvetica', 10, 'bold'))
text_box.tag_configure('error', foreground='red', font=('Helvetica', 10, 'italic'))

root.mainloop()
