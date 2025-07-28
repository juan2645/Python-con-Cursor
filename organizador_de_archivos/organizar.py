import os
import shutil
import time
from pathlib import Path
from datetime import datetime
import logging

class OrganizadorArchivos:
    def __init__(self, directorio_origen):
        """
        Inicializa el organizador de archivos.
        
        Args:
            directorio_origen (str): Ruta del directorio a organizar
        """
        self.directorio_origen = Path(directorio_origen)
        self.extensiones = {
            'Imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp'],
            'Documentos': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'],
            'Videos': ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm', '.m4v'],
            'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
            'Comprimidos': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
            'Programas': ['.exe', '.msi', '.dmg', '.pkg', '.deb', '.rpm'],
            'Otros': []
        }
        
        # Configurar logging
        self.configurar_logging()
    
    def configurar_logging(self):
        """Configura el sistema de logging para registrar las operaciones."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('organizador_archivos.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def obtener_tipo_archivo(self, archivo):
        """
        Determina el tipo de archivo basado en su extensión.
        
        Args:
            archivo (Path): Ruta del archivo
            
        Returns:
            str: Nombre de la carpeta destino
        """
        extension = archivo.suffix.lower()
        
        # Si no hay extensión, clasificar como "Sin_Extension"
        if not extension:
            return 'Sin_Extension'
        
        # Buscar en las categorías existentes
        for tipo, extensiones in self.extensiones.items():
            if extension in extensiones:
                return tipo
        
        # Si no existe la categoría, crear una nueva basada en la extensión
        nueva_categoria = self.crear_nueva_categoria(extension)
        return nueva_categoria
    
    def obtener_categoria_por_extension(self, extension):
        """
        Obtiene la categoría para una extensión específica.
        
        Args:
            extension (str): Extensión del archivo (con punto)
            
        Returns:
            str: Nombre de la categoría
        """
        # Mapeo directo de extensiones a categorías
        extension_a_categoria = {
            # Imágenes
            '.jpg': 'Imagenes', '.jpeg': 'Imagenes', '.png': 'Imagenes',
            '.gif': 'Imagenes', '.bmp': 'Imagenes', '.tiff': 'Imagenes',
            '.svg': 'Imagenes', '.webp': 'Imagenes',
            
            # Documentos
            '.pdf': 'Documentos', '.doc': 'Documentos', '.docx': 'Documentos',
            '.txt': 'Documentos', '.rtf': 'Documentos', '.odt': 'Documentos',
            '.xls': 'Documentos', '.xlsx': 'Documentos', '.ppt': 'Documentos',
            '.pptx': 'Documentos',
            
            # Videos
            '.mp4': 'Videos', '.avi': 'Videos', '.mov': 'Videos',
            '.wmv': 'Videos', '.flv': 'Videos', '.mkv': 'Videos',
            '.webm': 'Videos', '.m4v': 'Videos',
            
            # Audio
            '.mp3': 'Audio', '.wav': 'Audio', '.flac': 'Audio',
            '.aac': 'Audio', '.ogg': 'Audio', '.wma': 'Audio',
            '.m4a': 'Audio',
            
            # Comprimidos
            '.zip': 'Comprimidos', '.rar': 'Comprimidos', '.7z': 'Comprimidos',
            '.tar': 'Comprimidos', '.gz': 'Comprimidos', '.bz2': 'Comprimidos',
            
            # Programas
            '.exe': 'Programas', '.msi': 'Programas', '.dmg': 'Programas',
            '.pkg': 'Programas', '.deb': 'Programas', '.rpm': 'Programas'
        }
        
        return extension_a_categoria.get(extension, 'Otros')
    
    def crear_nueva_categoria(self, extension):
        """
        Crea una nueva categoría para una extensión no clasificada.
        
        Args:
            extension (str): Extensión del archivo
            
        Returns:
            str: Nombre de la nueva categoría
        """
        # Remover el punto de la extensión
        extension_limpia = extension.lstrip('.')
        
        # Crear nombre de categoría en mayúsculas
        categoria = extension_limpia.upper()
        
        # Agregar la nueva categoría al diccionario
        if categoria not in self.extensiones:
            self.extensiones[categoria] = [extension]
            self.logger.info(f"Nueva categoría creada: {categoria} para archivos {extension}")
        
        return categoria
    
    def crear_directorios(self):
        """Crea los directorios de destino si no existen."""
        for tipo in self.extensiones.keys():
            directorio_destino = self.directorio_origen / tipo
            if not directorio_destino.exists():
                directorio_destino.mkdir()
                self.logger.info(f"Creado directorio: {directorio_destino}")
    
    def crear_directorio_categoria(self, categoria):
        """
        Crea un directorio para una nueva categoría.
        
        Args:
            categoria (str): Nombre de la categoría
        """
        directorio_destino = self.directorio_origen / categoria
        if not directorio_destino.exists():
            directorio_destino.mkdir()
            self.logger.info(f"Creado directorio para nueva categoría: {directorio_destino}")
    
    def es_archivo_excluido(self, nombre_archivo):
        """
        Verifica si un archivo debe ser excluido de la organización.
        
        Args:
            nombre_archivo (str): Nombre del archivo
            
        Returns:
            bool: True si debe ser excluido, False en caso contrario
        """
        # Archivos del sistema y scripts que no deben moverse
        archivos_excluidos = {
            'organizar.py', 'programador.py', 'ejemplo_uso.py',
            'requirements.txt', 'README.md',
            'organizador_archivos.log', 'programador_organizador.log',
            'Thumbs.db', '.DS_Store', 'desktop.ini'
        }
        
        return nombre_archivo in archivos_excluidos
    
    def archivo_existe(self, origen, destino):
        """
        Verifica si ya existe un archivo con el mismo nombre en el destino.
        
        Args:
            origen (Path): Ruta del archivo origen
            destino (Path): Ruta del archivo destino
            
        Returns:
            bool: True si existe, False en caso contrario
        """
        return destino.exists()
    
    def renombrar_archivo(self, archivo_destino):
        """
        Renombra un archivo agregando un sufijo numérico si ya existe.
        
        Args:
            archivo_destino (Path): Ruta del archivo destino
            
        Returns:
            Path: Nueva ruta del archivo
        """
        contador = 1
        nombre_base = archivo_destino.stem
        extension = archivo_destino.suffix
        directorio = archivo_destino.parent
        
        while archivo_destino.exists():
            nuevo_nombre = f"{nombre_base}_{contador}{extension}"
            archivo_destino = directorio / nuevo_nombre
            contador += 1
        
        return archivo_destino
    
    def mover_archivo(self, archivo_origen, archivo_destino):
        """
        Mueve un archivo de forma segura, manejando conflictos de nombres.
        
        Args:
            archivo_origen (Path): Ruta del archivo origen
            archivo_destino (Path): Ruta del archivo destino
        """
        try:
            if self.archivo_existe(archivo_origen, archivo_destino):
                archivo_destino = self.renombrar_archivo(archivo_destino)
                self.logger.info(f"Archivo renombrado para evitar conflicto: {archivo_destino.name}")
            
            shutil.move(str(archivo_origen), str(archivo_destino))
            self.logger.info(f"Movido: {archivo_origen.name} -> {archivo_destino}")
            
        except Exception as e:
            self.logger.error(f"Error al mover {archivo_origen.name}: {str(e)}")
    
    def organizar_archivos(self):
        """
        Organiza todos los archivos en el directorio de origen.
        """
        if not self.directorio_origen.exists():
            self.logger.error(f"El directorio {self.directorio_origen} no existe")
            return
        
        # Obtener lista de archivos (no directorios) y excluir archivos del sistema
        archivos = [f for f in self.directorio_origen.iterdir() 
                   if f.is_file() and not self.es_archivo_excluido(f.name)]
        
        if not archivos:
            self.logger.info("No se encontraron archivos para organizar")
            return
        
        self.logger.info(f"Iniciando organización de {len(archivos)} archivos...")
        
        archivos_procesados = 0
        errores = 0
        
        for archivo in archivos:
            try:
                # Obtener extensión y categoría
                extension = archivo.suffix.lower()
                
                # Si no hay extensión, clasificar como "Sin_Extension"
                if not extension:
                    categoria = 'Sin_Extension'
                else:
                    # Usar mapeo directo para mayor eficiencia
                    categoria = self.obtener_categoria_por_extension(extension)
                    
                    # Si es "Otros", crear categoría automática
                    if categoria == 'Otros':
                        categoria = self.crear_nueva_categoria(extension)
                
                # Crear directorio de destino
                destino_dir = self.directorio_origen / categoria
                destino_dir.mkdir(exist_ok=True)
                
                # Verificar si existe archivo con el mismo nombre
                archivo_destino = destino_dir / archivo.name
                if archivo_destino.exists():
                    # Renombrar con sufijo numérico
                    archivo_destino = self.renombrar_archivo(archivo_destino)
                    self.logger.info(f"Archivo renombrado para evitar conflicto: {archivo_destino.name}")
                
                # Mover archivo usando rename (más eficiente que shutil.move)
                archivo.rename(archivo_destino)
                
                self.logger.info(f"Movido {archivo.name} a {categoria}/")
                archivos_procesados += 1
                
            except Exception as e:
                self.logger.error(f"Error procesando {archivo.name}: {str(e)}")
                errores += 1
        
        self.logger.info(f"Organización completada. Archivos procesados: {archivos_procesados}, Errores: {errores}")
    
    def mostrar_estadisticas(self):
        """
        Muestra estadísticas de los archivos organizados.
        """
        if not self.directorio_origen.exists():
            return
        
        print("\n=== ESTADÍSTICAS DE ORGANIZACIÓN ===")
        print(f"Directorio: {self.directorio_origen}")
        print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 40)
        
        total_archivos = 0
        categorias_creadas = []
        
        # Obtener todas las carpetas creadas (incluyendo nuevas categorías)
        carpetas_existentes = [d for d in self.directorio_origen.iterdir() if d.is_dir()]
        
        for carpeta in carpetas_existentes:
            archivos = list(carpeta.iterdir())
            cantidad = len([f for f in archivos if f.is_file()])
            if cantidad > 0:
                nombre_carpeta = carpeta.name
                print(f"{nombre_carpeta}: {cantidad} archivos")
                total_archivos += cantidad
                
                # Marcar si es una categoría nueva (no está en la lista original)
                if nombre_carpeta not in ['Imagenes', 'Documentos', 'Videos', 'Audio', 'Comprimidos', 'Programas', 'Otros']:
                    categorias_creadas.append(nombre_carpeta)
        
        print("-" * 40)
        print(f"Total: {total_archivos} archivos organizados")
        
        if categorias_creadas:
            print(f"\nNuevas categorías creadas: {', '.join(categorias_creadas)}")
            print("Estas categorías se crearon automáticamente para tipos de archivo no clasificados.")


def main():
    """
    Función principal que ejecuta el organizador de archivos.
    """
    import argparse
    
    parser = argparse.ArgumentParser(description='Organizador de archivos por tipo')
    parser.add_argument('directorio', nargs='?', default=None, 
                       help='Directorio a organizar (opcional)')
    parser.add_argument('--estadisticas', action='store_true',
                       help='Mostrar estadísticas después de organizar')
    parser.add_argument('--auto', action='store_true',
                       help='Ejecutar en modo automático (sin confirmación)')
    
    args = parser.parse_args()
    
    # Si no se especifica directorio, preguntar interactivamente
    if args.directorio is None:
        directorio = preguntar_directorio()
        if directorio is None:
            print("Operación cancelada.")
            return
    else:
        directorio = args.directorio
    
    # Crear instancia del organizador
    organizador = OrganizadorArchivos(directorio)
    
    if not args.auto:
        print(f"\n¿Deseas organizar los archivos en: {directorio}?")
        respuesta = input("(s/n): ").lower().strip()
        
        if respuesta not in ['s', 'si', 'sí', 'y', 'yes']:
            print("Operación cancelada.")
            return
    
    # Ejecutar organización
    print("Iniciando organización de archivos...")
    organizador.organizar_archivos()
    
    if args.estadisticas:
        organizador.mostrar_estadisticas()


def preguntar_directorio():
    """
    Pregunta al usuario qué directorio quiere organizar.
    
    Returns:
        str: Ruta del directorio seleccionado, o None si se cancela
    """
    print("=== ORGANIZADOR DE ARCHIVOS ===")
    print("¿Qué carpeta quieres organizar?")
    print("\nOpciones:")
    print("1. Carpeta actual")
    print("2. Carpeta de Descargas")
    print("3. Carpeta de Escritorio")
    print("4. Otra carpeta (especificar ruta)")
    print("5. Cancelar")
    
    while True:
        try:
            opcion = input("\nSelecciona una opción (1-5): ").strip()
            
            if opcion == "1":
                return "."
            elif opcion == "2":
                # Intentar encontrar la carpeta de Descargas
                descargas = obtener_carpeta_descargas()
                if descargas:
                    print(f"Carpeta de Descargas encontrada: {descargas}")
                    return descargas
                else:
                    print("No se pudo encontrar la carpeta de Descargas.")
                    return preguntar_ruta_manual()
            elif opcion == "3":
                # Intentar encontrar la carpeta de Escritorio
                escritorio = obtener_carpeta_escritorio()
                if escritorio:
                    print(f"Carpeta de Escritorio encontrada: {escritorio}")
                    return escritorio
                else:
                    print("No se pudo encontrar la carpeta de Escritorio.")
                    return preguntar_ruta_manual()
            elif opcion == "4":
                return preguntar_ruta_manual()
            elif opcion == "5":
                return None
            else:
                print("Opción no válida. Por favor selecciona 1-5.")
                
        except KeyboardInterrupt:
            print("\nOperación cancelada.")
            return None


def obtener_carpeta_descargas():
    """
    Intenta obtener la ruta de la carpeta de Descargas.
    
    Returns:
        str: Ruta de la carpeta de Descargas, o None si no se encuentra
    """
    import os
    
    # Rutas comunes de Descargas en Windows
    rutas_posibles = [
        os.path.expanduser("~/Downloads"),
        os.path.expanduser("~/Descargas"),
        os.path.expanduser("~/Desktop/Downloads"),
        "C:/Users/Public/Downloads"
    ]
    
    for ruta in rutas_posibles:
        if os.path.exists(ruta):
            return ruta
    
    return None


def obtener_carpeta_escritorio():
    """
    Intenta obtener la ruta de la carpeta de Escritorio.
    
    Returns:
        str: Ruta de la carpeta de Escritorio, o None si no se encuentra
    """
    import os
    
    # Rutas comunes de Escritorio en Windows
    rutas_posibles = [
        os.path.expanduser("~/Desktop"),
        os.path.expanduser("~/Escritorio"),
        "C:/Users/Public/Desktop"
    ]
    
    for ruta in rutas_posibles:
        if os.path.exists(ruta):
            return ruta
    
    return None


def preguntar_ruta_manual():
    """
    Pide al usuario que especifique manualmente la ruta de la carpeta.
    
    Returns:
        str: Ruta del directorio especificado, o None si se cancela
    """
    print("\nEspecifica la ruta completa de la carpeta que quieres organizar:")
    print("Ejemplos:")
    print("  C:\\Users\\TuUsuario\\Downloads")
    print("  C:\\MiCarpeta\\Archivos")
    print("  . (para el directorio actual)")
    
    while True:
        try:
            ruta = input("\nRuta de la carpeta: ").strip().strip('"')
            
            if ruta.lower() in ['cancelar', 'cancel', 'salir', 'exit']:
                return None
            
            # Verificar si la ruta existe
            if os.path.exists(ruta):
                if os.path.isdir(ruta):
                    return ruta
                else:
                    print("Error: La ruta especificada no es una carpeta.")
            else:
                print("Error: La carpeta no existe.")
                crear = input("¿Deseas crear esta carpeta? (s/n): ").lower().strip()
                if crear in ['s', 'si', 'sí', 'y', 'yes']:
                    try:
                        os.makedirs(ruta, exist_ok=True)
                        print(f"Carpeta creada: {ruta}")
                        return ruta
                    except Exception as e:
                        print(f"Error al crear la carpeta: {e}")
                
        except KeyboardInterrupt:
            print("\nOperación cancelada.")
            return None


if __name__ == "__main__":
    main()
