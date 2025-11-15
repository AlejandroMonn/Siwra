import argparse
import sys

# Import automation modules
import Autoclickeador
import autoescritor
import autoescritor_avanzado
import Automovedormouse


def main():
    """Función principal para la CLI."""
    parser = argparse.ArgumentParser(
        description="siwra CLI: Herramienta de automatización de scripts de mouse y teclado.",
    )

    # Definir los comandos disponibles
    subparsers = parser.add_subparsers(
        dest='command',
        required=True,
        help='Comando de automatización a ejecutar'
    )

    # COMANDO 1: Autoclicker
    parser_click = subparsers.add_parser('click', help='Ejecuta el script de Autoclickeador.')
    
    # COMANDO 2: Autoescritor (Básico)
    parser_write = subparsers.add_parser('write', help='Ejecuta el script de Autoescritor básico.')
    
    # COMANDO 3: Autoescritor Avanzado
    parser_write_adv = subparsers.add_parser('write-adv', help='Ejecuta el script de Autoescritor avanzado.')

    # COMANDO 4: Mover Mouse
    parser_move = subparsers.add_parser('move', help='Ejecuta el script de Automovedormouse.')

    args = parser.parse_args()

    # Ejecutar el módulo correspondiente
    try:
        if args.command == 'click':
            Autoclickeador.main()
        elif args.command == 'write':
            autoescritor.main()
        elif args.command == 'write-adv':
            autoescritor_avanzado.main()
        elif args.command == 'move':
            Automovedormouse.main()
        else:
            parser.print_help()
    except KeyboardInterrupt:
        print("\n\n⛔ Programa interrumpido por el usuario.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error al ejecutar el comando: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
