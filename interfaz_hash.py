import tkinter as tk
from tkinter import ttk
from estilos_visuales import EstilosVisuales

def recursive_caesar_hash(s, n):
    if n == 0:
        return 0
    return (recursive_caesar_hash(s, n - 1) + (ord(s[(n - 1)]) + n)) % 256

def recursive_caesar_hash_con_pasos(s, n, pasos):
    if n == 0:
        pasos.append("H(0) = 0")
        return 0
    prev = recursive_caesar_hash_con_pasos(s, n - 1, pasos)
    char_val = ord(s[(n - 1) % len(s)])
    current = (prev + char_val + n) % 256
    pasos.append(f"H({n}) = H({n-1}) + ord('{s[(n-1) % len(s)]}') + {n} = {prev} + {char_val} + {n} (mod 256) = {current}")
    return current

def cifrar():
    texto = entrada_cifrar.get()
    if not texto:
        resultado_cifrar.set("⚠️ Ingresa texto para continuar")
        text_pasos.config(state="normal")
        text_pasos.delete("1.0", tk.END)
        text_pasos.insert(tk.END, "📝 Esperando texto para procesar...")
        text_pasos.config(state="disabled")
        return
    try:
        valor = int(entry_posicion.get())
    except ValueError:
        resultado_cifrar.set("⚠️ La posición debe ser un número entero")
        text_pasos.config(state="normal")
        text_pasos.delete("1.0", tk.END)
        text_pasos.insert(tk.END, "✖️Error: Posición inválida. Debe ser un entero.")
        text_pasos.config(state="disabled")
        return

    hash_resultado = recursive_caesar_hash(texto, valor)
    resultado_cifrar.set(f"🔒 Hash Calculado: {hash_resultado}")

    pasos = []
    recursive_caesar_hash_con_pasos(texto, valor, pasos)

    text_pasos.config(state="normal")
    text_pasos.delete("1.0", tk.END)
    text_pasos.insert(tk.END, "H(n)=(H(n-1)+ord(s(n-1))+n)mod256:\n\n")
    text_pasos.insert(tk.END, "\n".join(pasos))
    text_pasos.insert(tk.END, f"\n\n-Resultado final: {hash_resultado}")
    text_pasos.config(state="disabled") 

ventana = tk.Tk()
ventana.title("🔐 Funcion Recursiva de Caesar mediante ASCI")
ventana.resizable(False, False)
estilos = EstilosVisuales(ventana)
frame_principal = estilos.crear_frame_principal()
estilos.crear_titulo(frame_principal, "🔐 Cesar Recursivo")

entrada_cifrar, entry_posicion = estilos.crear_seccion_entrada(frame_principal)
resultado_cifrar = estilos.crear_seccion_resultado(frame_principal)
estilos.crear_boton_accion(frame_principal, "🚀 Generar Hash", cifrar)
text_pasos = estilos.crear_seccion_pasos(frame_principal)

ventana.mainloop()