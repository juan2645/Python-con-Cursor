import tkinter as tk
from tkinter import filedialog, messagebox, font
import os

class EditorNotas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Editor de Notas Avanzado")
        self.geometry("800x600")
        
        # Variable para rastrear el archivo actual
        self.archivo_actual = None
        # Flag para rastrear cambios no guardados
        self.cambios_sin_guardar = False
        
        # Configuración de fuente por defecto
        self.fuente_actual = "Consolas"
        self.tamaño_fuente = 10
        self.zoom_actual = 100
        
        # Crear frame principal
        self.frame_principal = tk.Frame(self)
        self.frame_principal.pack(expand=True, fill=tk.BOTH)
        
        # Crear frame para numeración de líneas
        self.frame_lineas = tk.Frame(self.frame_principal)
        self.frame_lineas.pack(side=tk.LEFT, fill=tk.Y)
        
        # Crear numeración de líneas
        self.numeracion_lineas = tk.Text(self.frame_lineas, width=4, padx=3, pady=3,
                                        takefocus=0, border=0, background='lightgray',
                                        state='disabled', font=(self.fuente_actual, self.tamaño_fuente))
        self.numeracion_lineas.pack(side=tk.LEFT, fill=tk.Y)
        
        # Crear área de texto principal
        self.text_area = tk.Text(self.frame_principal, wrap=tk.NONE, undo=True)
        self.text_area.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        
        # Configurar scrollbars
        self.scrollbar_y = tk.Scrollbar(self.frame_principal, orient=tk.VERTICAL, command=self.on_scroll)
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.scrollbar_x = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.text_area.xview)
        self.scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Configurar el área de texto
        self.text_area.config(yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)
        
        # Configurar el protocolo para manejar el cierre de ventana
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Crear menú
        self.crear_menu()
        
        # Vincular eventos de cambio de texto
        self.text_area.bind('<Key>', self.on_text_change)
        self.text_area.bind('<KeyRelease>', self.on_text_change)
        self.text_area.bind('<Button-1>', self.on_text_change)
        
        # Configurar fuente inicial
        self.aplicar_fuente()
        
        # Actualizar numeración inicial
        self.actualizar_numeracion()
   
    def crear_menu(self):
        menubar = tk.Menu(self)
        
        # Menú Archivo
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Abrir", command=self.abrir_archivo)
        filemenu.add_command(label="Guardar", command=self.guardar_archivo)
        filemenu.add_command(label="Guardar como...", command=self.guardar_como)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.quit)
        menubar.add_cascade(label="Archivo", menu=filemenu)
        
        # Menú Editar
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Deshacer", command=self.deshacer, accelerator="Ctrl+Z")
        editmenu.add_separator()
        editmenu.add_command(label="Cortar", command=self.cortar, accelerator="Ctrl+X")
        editmenu.add_command(label="Copiar", command=self.copiar, accelerator="Ctrl+C")
        editmenu.add_command(label="Pegar", command=self.pegar, accelerator="Ctrl+V")
        editmenu.add_separator()
        editmenu.add_command(label="Seleccionar todo", command=self.seleccionar_todo, accelerator="Ctrl+A")
        menubar.add_cascade(label="Editar", menu=editmenu)
        
        # Menú Formato
        formatmenu = tk.Menu(menubar, tearoff=0)
        
        # Submenú Fuente
        fontmenu = tk.Menu(formatmenu, tearoff=0)
        fuentes_comunes = ["Consolas", "Courier New", "Arial", "Times New Roman", "Verdana", "Tahoma"]
        for fuente in fuentes_comunes:
            fontmenu.add_command(label=fuente, command=lambda f=fuente: self.cambiar_fuente(f))
        formatmenu.add_cascade(label="Fuente", menu=fontmenu)
        
        # Submenú Tamaño
        sizemenu = tk.Menu(formatmenu, tearoff=0)
        tamaños = [8, 9, 10, 11, 12, 14, 16, 18, 20, 24]
        for tamaño in tamaños:
            sizemenu.add_command(label=str(tamaño), command=lambda t=tamaño: self.cambiar_tamaño(t))
        formatmenu.add_cascade(label="Tamaño", menu=sizemenu)
        
        formatmenu.add_separator()
        formatmenu.add_command(label="Zoom +", command=self.zoom_in, accelerator="Ctrl++")
        formatmenu.add_command(label="Zoom -", command=self.zoom_out, accelerator="Ctrl+-")
        formatmenu.add_command(label="Zoom Reset", command=self.zoom_reset, accelerator="Ctrl+0")
        
        menubar.add_cascade(label="Formato", menu=formatmenu)
        
        # Menú Ver
        viewmenu = tk.Menu(menubar, tearoff=0)
        viewmenu.add_checkbutton(label="Numeración de líneas", command=self.toggle_numeracion, onvalue=True, offvalue=False)
        viewmenu.add_separator()
        viewmenu.add_command(label="Ir a línea...", command=self.ir_a_linea, accelerator="Ctrl+G")
        menubar.add_cascade(label="Ver", menu=viewmenu)
        
        self.config(menu=menubar)
        
        # Configurar atajos de teclado
        self.configurar_atajos()
    
    def configurar_atajos(self):
        """Configurar atajos de teclado adicionales"""
        self.bind('<Control-z>', lambda e: self.deshacer())
        self.bind('<Control-x>', lambda e: self.cortar())
        self.bind('<Control-c>', lambda e: self.copiar())
        self.bind('<Control-v>', lambda e: self.pegar())
        self.bind('<Control-a>', lambda e: self.seleccionar_todo())
        self.bind('<Control-plus>', lambda e: self.zoom_in())
        self.bind('<Control-minus>', lambda e: self.zoom_out())
        self.bind('<Control-0>', lambda e: self.zoom_reset())
        self.bind('<Control-g>', lambda e: self.ir_a_linea())
    
    def on_scroll(self, *args):
        """Sincronizar scroll de numeración con el área de texto"""
        self.numeracion_lineas.yview(*args)
        self.text_area.yview(*args)
    
    def actualizar_numeracion(self):
        """Actualizar la numeración de líneas"""
        contenido = self.text_area.get("1.0", tk.END)
        lineas = contenido.count('\n')
        
        # Generar numeración
        numeracion = ""
        for i in range(1, lineas + 1):
            numeracion += f"{i}\n"
        
        # Actualizar widget de numeración
        self.numeracion_lineas.config(state='normal')
        self.numeracion_lineas.delete("1.0", tk.END)
        self.numeracion_lineas.insert("1.0", numeracion)
        self.numeracion_lineas.config(state='disabled')
    
    def toggle_numeracion(self):
        """Mostrar/ocultar numeración de líneas"""
        if self.numeracion_lineas.winfo_viewable():
            self.numeracion_lineas.pack_forget()
        else:
            self.numeracion_lineas.pack(side=tk.LEFT, fill=tk.Y)
    
    def cambiar_fuente(self, fuente):
        """Cambiar la fuente del texto"""
        self.fuente_actual = fuente
        self.aplicar_fuente()
    
    def cambiar_tamaño(self, tamaño):
        """Cambiar el tamaño de la fuente"""
        self.tamaño_fuente = tamaño
        self.aplicar_fuente()
    
    def aplicar_fuente(self):
        """Aplicar la fuente actual al área de texto y numeración"""
        fuente_config = (self.fuente_actual, int(self.tamaño_fuente * self.zoom_actual / 100))
        self.text_area.config(font=fuente_config)
        self.numeracion_lineas.config(font=fuente_config)
    
    def zoom_in(self):
        """Aumentar zoom"""
        if self.zoom_actual < 200:
            self.zoom_actual += 10
            self.aplicar_fuente()
    
    def zoom_out(self):
        """Reducir zoom"""
        if self.zoom_actual > 50:
            self.zoom_actual -= 10
            self.aplicar_fuente()
    
    def zoom_reset(self):
        """Resetear zoom"""
        self.zoom_actual = 100
        self.aplicar_fuente()
    
    def ir_a_linea(self):
        """Ir a una línea específica"""
        from tkinter import simpledialog
        
        try:
            linea = simpledialog.askinteger("Ir a línea", "Número de línea:", 
                                          minvalue=1, maxvalue=10000)
            if linea:
                self.text_area.see(f"{linea}.0")
                self.text_area.mark_set(tk.INSERT, f"{linea}.0")
        except:
            pass
    
    def deshacer(self):
        """Deshacer la última acción"""
        try:
            self.text_area.edit_undo()
        except tk.TclError:
            pass  # No hay nada que deshacer
    
    def cortar(self):
        """Cortar texto seleccionado"""
        try:
            self.text_area.event_generate("<<Cut>>")
        except tk.TclError:
            pass
    
    def copiar(self):
        """Copiar texto seleccionado"""
        try:
            self.text_area.event_generate("<<Copy>>")
        except tk.TclError:
            pass
    
    def pegar(self):
        """Pegar texto desde el portapapeles"""
        try:
            self.text_area.event_generate("<<Paste>>")
        except tk.TclError:
            pass
    
    def seleccionar_todo(self):
        """Seleccionar todo el texto"""
        self.text_area.tag_add(tk.SEL, "1.0", tk.END)
        self.text_area.mark_set(tk.INSERT, "1.0")
        self.text_area.see(tk.INSERT)
        return 'break'
    
    def on_text_change(self, event=None):
        """Marcar que hay cambios sin guardar y actualizar numeración"""
        self.cambios_sin_guardar = True
        # Actualizar el título para mostrar que hay cambios
        titulo_actual = self.title()
        if not titulo_actual.endswith(" *"):
            self.title(titulo_actual + " *")
        
        # Actualizar numeración de líneas
        self.actualizar_numeracion()
    
    def on_closing(self):
        """Manejar el cierre de la ventana"""
        if self.cambios_sin_guardar:
            respuesta = messagebox.askyesnocancel(
                "Guardar cambios",
                "¿Desea guardar los cambios antes de salir?",
                icon=messagebox.QUESTION
            )
            
            if respuesta is True:  # Sí
                if self.archivo_actual is None:
                    # Si no hay archivo actual, usar "Guardar como"
                    if not self.guardar_como():
                        return  # Usuario canceló el guardado
                else:
                    # Guardar en el archivo actual
                    self.guardar_archivo()
                self.quit()
            elif respuesta is False:  # No
                self.quit()
            # Si es None (Cancelar), no hacer nada
        else:
            self.quit()
    
    def abrir_archivo(self):
        # Verificar si hay cambios sin guardar
        if self.cambios_sin_guardar:
            respuesta = messagebox.askyesnocancel(
                "Guardar cambios",
                "¿Desea guardar los cambios antes de abrir un nuevo archivo?",
                icon=messagebox.QUESTION
            )
            
            if respuesta is True:  # Sí
                if self.archivo_actual is None:
                    if not self.guardar_como():
                        return  # Usuario canceló el guardado
                else:
                    self.guardar_archivo()
            elif respuesta is None:  # Cancelar
                return
        
        filepath = filedialog.askopenfilename(
            filetypes=[("Archivos de texto","*.txt"), ("Todos los archivos","*.*")],
            initialdir=os.getcwd()
        )
        if not filepath:
            return
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                contenido = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, contenido)
            self.archivo_actual = filepath
            self.cambios_sin_guardar = False
            self.title(f"Editor de Notas - {filepath}")
            self.actualizar_numeracion()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el archivo:\n{e}")
   
    def guardar_archivo(self):
        # Si no hay archivo actual, usar "Guardar como"
        if self.archivo_actual is None:
            return self.guardar_como()
        
        try:
            contenido = self.text_area.get(1.0, tk.END)
            with open(self.archivo_actual, "w", encoding="utf-8") as file:
                file.write(contenido)
            self.cambios_sin_guardar = False
            # Actualizar título sin el asterisco
            titulo_actual = self.title()
            if titulo_actual.endswith(" *"):
                self.title(titulo_actual[:-2])
            messagebox.showinfo("Éxito", f"Archivo guardado exitosamente")
        except PermissionError as e:
            print(f"Error de permisos: {e}")
            messagebox.showerror("Error de Permisos", 
                               f"No tienes permisos para escribir en esta ubicación:\n{self.archivo_actual}\n\n"
                               f"Error: {str(e)}")
        except OSError as e:
            print(f"Error del sistema: {e}")
            messagebox.showerror("Error del Sistema", 
                               f"Error al guardar el archivo:\n{str(e)}")
        except Exception as e:
            print(f"Error inesperado: {type(e).__name__}: {e}")
            messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{str(e)}")
    
    def guardar_como(self):
        # Usar el directorio actual como ubicación por defecto
        directorio_actual = os.getcwd()
        
        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Archivos de texto","*.txt"), ("Todos los archivos","*.*")],
            initialdir=directorio_actual,
            title="Guardar archivo como"
        )
        if not filepath:
            print("No se seleccionó archivo (usuario canceló)")
            return False
        
        return self._guardar_archivo_en_ruta(filepath)
    
    def _guardar_archivo_en_ruta(self, filepath):
        """Método interno para guardar archivo en una ruta específica"""
        print(f"Intentando guardar en: {filepath}")
        
        try:
            contenido = self.text_area.get(1.0, tk.END)
            print(f"Contenido a guardar: {len(contenido)} caracteres")
            
            # Verificar si el directorio existe y es escribible
            directorio = os.path.dirname(filepath)
            if directorio and not os.path.exists(directorio):
                print(f"Error: El directorio {directorio} no existe")
                messagebox.showerror("Error", f"El directorio no existe:\n{directorio}")
                return False
            
            # Verificar permisos de escritura
            if directorio and not os.access(directorio, os.W_OK):
                print(f"Error: No hay permisos de escritura en {directorio}")
                messagebox.showerror("Error de Permisos", 
                                   f"No tienes permisos para escribir en:\n{directorio}")
                return False
            
            # Probar con encoding UTF-8 explícito
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(contenido)
            
            print("Archivo guardado exitosamente")
            self.archivo_actual = filepath
            self.cambios_sin_guardar = False
            # Actualizar título sin el asterisco
            titulo_actual = self.title()
            if titulo_actual.endswith(" *"):
                self.title(titulo_actual[:-2])
            self.title(f"Editor de Notas - {filepath}")
            messagebox.showinfo("Éxito", f"Archivo guardado exitosamente en:\n{filepath}")
            return True
            
        except PermissionError as e:
            print(f"Error de permisos: {e}")
            messagebox.showerror("Error de Permisos", 
                               f"No tienes permisos para escribir en esta ubicación:\n{filepath}\n\n"
                               f"Error: {str(e)}")
            return False
        except OSError as e:
            print(f"Error del sistema: {e}")
            messagebox.showerror("Error del Sistema", 
                               f"Error al guardar el archivo:\n{str(e)}")
            return False
        except Exception as e:
            print(f"Error inesperado: {type(e).__name__}: {e}")
            messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{str(e)}")
            return False

if __name__ == "__main__":
    app = EditorNotas()
    app.mainloop()
