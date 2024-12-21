










Estructura de carpetas propuesta:

├── main.py        # Punto de entrada principal de la aplicación
├── utils/         # Funciones utilitarias generales
│   ├── scraping.py   # Funciones relacionadas con el scraping
│   └── scheduler.py # Funciones relacionadas con la programación de tareas
├── schemas/       # Definiciones de esquemas Pydantic
├── routes/        # Definiciones de las rutas de la API
├── models/        # Definiciones de modelos de base de datos (si los usas)
├── middleware/    # Middleware de la aplicación
├── env/           # Archivos de configuración de entorno
├── controllers/   # Lógica de negocio (controladores)
└── ...