# Mostrar IP pública (Streamlit)

Esta pequeña app muestra la IP pública del usuario usando la API pública de api.ipify.org y Streamlit.

Requisitos
- Python 3.10+ (necesario por la sintaxis de tipos `str | None`)
- pip

Instalación
1. Crear y activar un entorno virtual (opcional pero recomendado):

   Windows (cmd.exe):

   python -m venv .venv
   .venv\Scripts\activate

2. Instalar dependencias:

   pip install -r requirements.txt

Ejecución

En el directorio del proyecto, ejecutar:

   python -m streamlit run main.py

La app abrirá en el navegador en http://localhost:8501 por defecto.

Notas
- Hay un botón "Refrescar" que fuerza una nueva llamada a la API (se usa cache por 60s para evitar demasiadas peticiones).
- Si no se obtiene la IP, revisa la conectividad o intenta abrir https://api.ipify.org en el navegador.

Licencia
- Código de ejemplo, libre para usar y modificar.
