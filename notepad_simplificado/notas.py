import tkinter as tk
from tkinter import filedialog, messagebox
import os

class EditorNotas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Editor de Notas")
        self.geometry("600x400")
        
        # Variable para rastrear el archivo actual
        self.archivo_actual = None
        
        # Crear área de texto
        self.text_area = tk.Text(self)
        self.text_area.pack(expand=True, fill=tk.BOTH)
        
        # Crear menú
        self.crear_menu()
   
    def crear_menu(self):
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Abrir", command=self.abrir_archivo)
        filemenu.add_command(label="Guardar", command=self.guardar_archivo)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.quit)
        menubar.add_cascade(label="Archivo", menu=filemenu)
        self.config(menu=menubar)
    
    def abrir_archivo(self):
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
            self.title(f"Editor de Notas - {filepath}")
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
            return
        
        self._guardar_archivo_en_ruta(filepath)
    
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
                return
            
            # Verificar permisos de escritura
            if directorio and not os.access(directorio, os.W_OK):
                print(f"Error: No hay permisos de escritura en {directorio}")
                messagebox.showerror("Error de Permisos", 
                                   f"No tienes permisos para escribir en:\n{directorio}")
                return
            
            # Probar con encoding UTF-8 explícito
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(contenido)
            
            print("Archivo guardado exitosamente")
            self.archivo_actual = filepath
            self.title(f"Editor de Notas - {filepath}")
            messagebox.showinfo("Éxito", f"Archivo guardado exitosamente en:\n{filepath}")
            
        except PermissionError as e:
            print(f"Error de permisos: {e}")
            messagebox.showerror("Error de Permisos", 
                               f"No tienes permisos para escribir en esta ubicación:\n{filepath}\n\n"
                               f"Error: {str(e)}")
        except OSError as e:
            print(f"Error del sistema: {e}")
            messagebox.showerror("Error del Sistema", 
                               f"Error al guardar el archivo:\n{str(e)}")
        except Exception as e:
            print(f"Error inesperado: {type(e).__name__}: {e}")
            messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{str(e)}")

if __name__ == "__main__":
    app = EditorNotas()
    app.mainloop()
