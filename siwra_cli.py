
import argparse
import sys

# IMPORTA TUS SCRIPTS
# (Asegúrate de que tus scripts tienen funciones que se pueden importar)
# Por ahora, los llamaremos directamente usando 'exec', pero lo ideal es IMPORTAR funciones.
# Asumiremos que cada script ejecuta su acción al ser llamado.

def run_script_file(script_name):
    """Ejecuta un script específico por su nombre."""
    try:
        # Aquí es donde llamas al código.
        # En un proyecto real, se usa 'import' para llamar a las funciones:
        # Ejemplo: if script_name == "autoclick": Autoclickeador.start()
        
        # Para mantenerlo simple AHORA, usaremos un método directo para ejecutar el archivo:
        with open(script_name, 'r') as file:
            script_code = file.read()
            # Ejecuta el código del script. Esto asume que el script corre solo.
            exec(script_code, globals())
            
        print(f"\n✅ Script '{script_name}' ejecutado correctamente.")
        
    except FileNotFoundError:
        print(f"\n❌ ERROR: No se encontró el script '{script_name}'.")
    except Exception as e:
        print(f"\n❌ Ocurrió un error al ejecutar '{script_name}': {e}")


def main():
    """Función principal para la CLI."""
    parser = argparse.ArgumentParser(
        description="siwra CLI: Herramienta de automatización de scripts de mouse y teclado.",
    )

    # Definir los comandos disponibles
    subparsers = parser.add_subparsers(
        dest='command',
        required=True, # Hace que el usuario deba elegir un comando
        help='Comando de automatización a ejecutar'
    )

    # COMANDO 1: Autoclicker
    parser_click = subparsers.add_parser('click', help='Ejecuta el script de Autoclickeador.')
    parser_click.set_defaults(script_to_run='Autoclickeador.py')

    # COMANDO 2: Autoescritor (Básico)
    parser_write = subparsers.add_parser('write', help='Ejecuta el script de Autoescritor básico.')
    parser_write.set_defaults(script_to_run='autoescritor.py')
    
    # COMANDO 3: Autoescritor Avanzado
    parser_write_adv = subparsers.add_parser('write-adv', help='Ejecuta el script de Autoescritor avanzado.')
    parser_write_adv.set_defaults(script_to_run='autoescritor_avanzado.py')

    # COMANDO 4: Mover Mouse (Script específico)
    parser_move = subparsers.add_parser('move', help='Ejecuta el script de Automovedormouse.')
    parser_move.set_defaults(script_to_run='Automovedormouse.py')

    # Otros comandos: puedes agregar más aquí, mapeando a tus otros archivos
    # EJEMPLO: parser_combo = subparsers.add_parser('combo', help='Ejecuta Autoclick y Mover mouse.')
    # EJEMPLO: parser_combo.set_defaults(script_to_run='Autoescritor_y_movedordemouse.py')


    args = parser.parse_args()

    # Ejecutar el script asociado al comando
    if hasattr(args, 'script_to_run'):
        run_script_file(args.script_to_run)
    else:
        # Esto solo pasa si se agregan argumentos/comandos sin 'set_defaults'
        parser.print_help()


if __name__ == "__main__":
    main()