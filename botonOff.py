import os
import tkinter as tk
from tkinter import messagebox

# Función para programar el apagado
def program_shutdown():
    try:
        minutes = int(entry.get())
        seconds = minutes * 60
        os.system(f"shutdown -s -t {seconds}")
        messagebox.showinfo("Éxito", f"El sistema se apagará en {minutes} minutos.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido.")

# Función para cancelar el apagado automático.
def cancel_shutdown():
    os.system("shutdown -a")
    messagebox.showinfo("Cancelado", "El apagado ha sido cancelado.")

# Crear la ventana principal
window = tk.Tk()
window.title("Programar Apagado")
window.geometry("400x200")  # Dimensiones de la ventana (ancho x alto)

# Centrar la ventana en la pantalla
window.eval('tk::PlaceWindow . center')

# Cambiar el color de fondo de la ventana
window.configure(bg='#f0f0f0')

# Etiqueta y entrada para minutos
label = tk.Label(window, text="Ingrese el tiempo en minutos:", font=("Arial", 12), bg='#f0f0f0')
label.pack(pady=20)

entry = tk.Entry(window, font=("Arial", 12), justify='center')
entry.pack(pady=10)

# Botón para programar apagado
shutdown_button = tk.Button(window, text="Programar Apagado", font=("Arial", 12), bg='#4CAF50', fg='white', command=program_shutdown)
shutdown_button.pack(pady=10)

# Botón para cancelar apagado
cancel_button = tk.Button(window, text="Cancelar Apagado", font=("Arial", 12), bg='#f44336', fg='white', command=cancel_shutdown)
cancel_button.pack(pady=10)

# Ejecutar la aplicación
window.mainloop()
