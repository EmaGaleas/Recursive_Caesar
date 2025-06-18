import tkinter as tk
from tkinter import ttk

class EstilosVisuales:
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.configurar_ventana()
        self.configurar_estilos()
    
    def configurar_ventana(self):
        """Configura la apariencia general de la ventana"""
        self.ventana.configure(bg='#1f0034') 
        self.ventana.geometry("620x520")
        self.ventana.resizable(False, False)
        
        self.ventana.update_idletasks()
        width = self.ventana.winfo_width()
        height = self.ventana.winfo_height()
        x = (self.ventana.winfo_screenwidth() // 2) - (width // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (height // 2)
        self.ventana.geometry(f'{width}x{height}+{x}+{y}')
    
    def configurar_estilos(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Titulo.TLabel', 
                        font=('Segoe UI Semibold', 14),
                        background='#ffffff',
                        foreground='#4a5a6a')
        
        style.configure('SubTitulo.TLabel',
                        font=('Segoe UI', 11),
                        background='#ffffff',
                        foreground='#4a5a6a')
        
        style.configure('Accion.TButton',
                        font=('Segoe UI Semibold', 12),
                        padding=(15, 8),
                        foreground='#ea9267',
                        background='#1f0034',
                        borderwidth=0,
                        focusthickness=3,
                        focuscolor='none')
        style.map('Accion.TButton',
                  background=[('active', '#d2ddcf')],
                  foreground=[('disabled', '#ffead7')])
        
        # Entradas (Entry)
        style.configure('Custom.TEntry',
                        fieldbackground='white',
                        borderwidth=1,
                        relief='solid',
                        padding=5,
                        font=('Segoe UI', 11))
        
        # Frame tipo "card" para fondo y bordes suaves
        style.configure('Card.TFrame',
                        background='white',
                        borderwidth=1,
                        relief='flat')
    
    def crear_frame_principal(self):
        """el marco lit"""
        frame = ttk.Frame(self.ventana, style='Card.TFrame', padding=20)
        frame.pack(fill='both', expand=True, padx=20, pady=20)
        return frame
    
    def crear_titulo(self, parent, texto):
        titulo = ttk.Label(parent, text=texto, style='Titulo.TLabel')
        titulo.pack(pady=(0, 15))
        return titulo
    
    def crear_seccion_entrada(self, parent):
        """parte de entradas"""
        frame_entradas = ttk.Frame(parent, style='Card.TFrame', padding=(15, 10, 15, 15))
        frame_entradas.pack(fill='x', pady=(0, 10))
        
        # Texto a cifrar
        ttk.Label(frame_entradas, text="Texto a cifrar:", style='SubTitulo.TLabel').pack(anchor='w', pady=(0, 5))
        entrada_cifrar = ttk.Entry(frame_entradas, width=60, style='Custom.TEntry')
        entrada_cifrar.pack(fill='x', pady=(0, 10))
        
        # Posición (junto en línea)
        frame_posicion = ttk.Frame(frame_entradas, style='Card.TFrame')
        frame_posicion.pack(fill='x')
        
        ttk.Label(frame_posicion, text="Posición (entero):", style='SubTitulo.TLabel').pack(side='left')
        entry_posicion = ttk.Entry(frame_posicion, width=15, style='Custom.TEntry')
        entry_posicion.pack(side='left', padx=(10, 0))
        
        return entrada_cifrar, entry_posicion
    
    def crear_seccion_resultado(self, parent):
        """Crea la sección de resultado con mejor presentación"""   
        frame_resultado = ttk.Frame(parent, style='Card.TFrame', padding=0)
        frame_resultado.pack(fill='x', pady=5)
        
        resultado_cifrar = tk.StringVar(value="Resultado aparecerá aquí...")
        label_resultado = ttk.Label(frame_resultado, textvariable=resultado_cifrar,
                                   font=('Consolas', 12, 'bold'),
                                   foreground='#ea9267',
                                   background='white',
                                   anchor='center')
        label_resultado.pack(fill='x', pady=3)
        
        return resultado_cifrar
    
    def crear_boton_accion(self, parent, texto, comando):
        """Crea el botón de acción principal"""
        boton = ttk.Button(parent, text=texto, command=comando, style='Accion.TButton')
        boton.pack(pady=6)
        return boton
    
    def crear_seccion_pasos(self, parent):
        """Crea la sección de pasos con mejor diseño"""
        ttk.Label(parent, text="Proceso de Cálculo:", style='Titulo.TLabel').pack(anchor='w', pady=(5, 5))
        
        frame_texto = ttk.Frame(parent, style='Card.TFrame', padding=8)
        frame_texto.pack(fill='both', expand=True)
        
        text_pasos = tk.Text(frame_texto, 
                             height=12, 
                             state="normal",  
                             bg="#fafbfc",     
                             fg="#2c3e50",    
                             font=('Consolas', 9),
                             wrap='word',
                             borderwidth=1,
                             relief='solid',
                             selectbackground='#3498db',
                             selectforeground='white',
                             padx=8,
                             pady=5)
        
        scrollbar = ttk.Scrollbar(frame_texto, orient="vertical", command=text_pasos.yview)
        text_pasos.configure(yscrollcommand=scrollbar.set)
        
        text_pasos.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        return text_pasos