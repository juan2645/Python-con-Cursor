import schedule
import time
import sys
import os
from pathlib import Path
from datetime import datetime
import logging
from organizar import OrganizadorArchivos

class ProgramadorOrganizador:
    def __init__(self, directorio_origen, intervalo_horas=24):
        """
        Inicializa el programador del organizador de archivos.
        
        Args:
            directorio_origen (str): Ruta del directorio a organizar
            intervalo_horas (int): Intervalo en horas para ejecutar la organización
        """
        self.directorio_origen = directorio_origen
        self.intervalo_horas = intervalo_horas
        self.organizador = OrganizadorArchivos(directorio_origen)
        
        # Configurar logging específico para el programador
        self.configurar_logging()
    
    def configurar_logging(self):
        """Configura el sistema de logging para el programador."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('programador_organizador.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def ejecutar_organizacion(self):
        """
        Ejecuta la organización de archivos y registra la actividad.
        """
        try:
            self.logger.info(f"Iniciando organización programada en: {self.directorio_origen}")
            
            # Ejecutar organización
            self.organizador.organizar_archivos()
            
            # Mostrar estadísticas
            self.organizador.mostrar_estadisticas()
            
            self.logger.info("Organización programada completada exitosamente")
            
        except Exception as e:
            self.logger.error(f"Error en la organización programada: {str(e)}")
    
    def programar_ejecucion(self):
        """
        Programa la ejecución automática del organizador.
        """
        # Programar ejecución cada X horas
        schedule.every(self.intervalo_horas).hours.do(self.ejecutar_organizacion)
        
        # También programar una ejecución diaria a las 2:00 AM
        schedule.every().day.at("02:00").do(self.ejecutar_organizacion)
        
        self.logger.info(f"Programador iniciado. Organización cada {self.intervalo_horas} horas")
        self.logger.info("Ejecución diaria programada a las 02:00 AM")
        
        # Ejecutar una vez al inicio
        self.ejecutar_organizacion()
        
        # Mantener el programa ejecutándose
        while True:
            try:
                schedule.run_pending()
                time.sleep(60)  # Verificar cada minuto
                
            except KeyboardInterrupt:
                self.logger.info("Programador detenido por el usuario")
                break
            except Exception as e:
                self.logger.error(f"Error en el programador: {str(e)}")
                time.sleep(300)  # Esperar 5 minutos antes de reintentar
    
    def mostrar_programacion(self):
        """
        Muestra las tareas programadas actuales.
        """
        print("\n=== TAREAS PROGRAMADAS ===")
        print(f"Directorio a organizar: {self.directorio_origen}")
        print(f"Intervalo: cada {self.intervalo_horas} horas")
        print("Tareas:")
        
        for job in schedule.get_jobs():
            print(f"  - {job}")
        
        print("\nPara detener el programador, presiona Ctrl+C")


def main():
    """
    Función principal del programador.
    """
    import argparse
    
    parser = argparse.ArgumentParser(description='Programador del organizador de archivos')
    parser.add_argument('directorio', nargs='?', default='.', 
                       help='Directorio a organizar (por defecto: directorio actual)')
    parser.add_argument('--intervalo', type=int, default=24,
                       help='Intervalo en horas entre ejecuciones (por defecto: 24)')
    parser.add_argument('--mostrar', action='store_true',
                       help='Solo mostrar la programación sin ejecutar')
    
    args = parser.parse_args()
    
    # Verificar que el directorio existe
    if not Path(args.directorio).exists():
        print(f"Error: El directorio {args.directorio} no existe")
        sys.exit(1)
    
    # Crear instancia del programador
    programador = ProgramadorOrganizador(args.directorio, args.intervalo)
    
    if args.mostrar:
        programador.mostrar_programacion()
        return
    
    print("=== PROGRAMADOR DE ORGANIZADOR DE ARCHIVOS ===")
    print(f"Directorio: {args.directorio}")
    print(f"Intervalo: cada {args.intervalo} horas")
    print("Presiona Ctrl+C para detener")
    print("-" * 50)
    
    try:
        programador.programar_ejecucion()
    except KeyboardInterrupt:
        print("\nProgramador detenido.")


if __name__ == "__main__":
    main() 