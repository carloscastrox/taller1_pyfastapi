from views import trainee_view


def main():
    # Inicia el controlador principal que contiene el bucle del menú
    trainee_view.main_menu_controller()


if __name__ == "__main__":
    main()

# 1. Refactorizar ruta del archivo JSON en la carpeta data/
# 2. Refactorizar validaciones de los datos de entrada(incluir el correo electrónico) en la vista para que sean más robustas y claras.(Númerica, alfabética, correo electrónico, etc.)
# 3. Implementar el editar de aprendices para permitir modificar los datos de un aprendiz existente.
# 4. Implementar la eliminación de aprendices para permitir borrar un aprendiz existente de la lista.
# 5. Implementar la búsqueda de aprendices por nombre o ficha para facilitar la localización de registros específicos.
# 6. Implementar la exportación de la lista de aprendices a un archivo CSV para facilitar el manejo de datos fuera del programa.
# 7. Implementar un menú principal para que el usuario pueda elegir entre registrar, editar, eliminar, buscar o exportar aprendices, en lugar de solo registrar uno tras otro.
