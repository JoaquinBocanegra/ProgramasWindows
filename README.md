# Temporizador de Apagado

Este es un programa en Python con una interfaz gráfica (Tkinter) que permite apagar la PC después de un tiempo seleccionado.

## Características

- Selección de tiempo predefinido (en minutos).
- Apaga la PC automáticamente después del tiempo configurado.
- Interfaz gráfica sencilla.

## Requisitos

- Python 3.7 o superior.
- Módulo Tkinter (generalmente incluido con Python).
- PyInstaller (opcional para generar el archivo `.exe`).

## Cómo usar

1. **Clona el repositorio**:
    ```bash
    git clone https://github.com/usuario/temporizador-apagado.git
    cd temporizador-apagado
    ```

2. **Ejecuta el programa**:
    Si solo quieres usar el script Python, ejecuta:
    ```bash
    python shutdown_timer.py
    ```

3. **Crear un ejecutable (.exe)** (opcional):
    Si deseas distribuir el programa como un archivo `.exe`, sigue estos pasos:
    ```bash
    pip install pyinstaller
    pyinstaller --onefile --windowed shutdown_timer.py
    ```
    El archivo `.exe` estará disponible en la carpeta `dist`.

## Licencia

Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE](LICENSE) para más detalles.
