##  titulo: Web Scraping

* Extrayendo datos de Amazon con Selenium | Web Scraping | FastApi

* Esta API utiliza técnicas de scraping para obtener información relevante de Airbnb y ponerla a disposición de los usuarios.

## Tecnologías Utilizadas
* FastAPI
* Python
* PostgreSQL
* Selenium
* BeautifulSoup
* Docker


## Instalacion:

    Bash

        Clonar el repositorio:

        git clone https://github.com/tu_usuario/tu_repositorio.git

    Crear un entorno virtual:

    python -m venv env

    Activar el entorno virtual:
    
        # En Windows
        env\Scripts\activate

        # En Linux/macOS
        source env/bin/activate

    Instalar las dependencias:

    pip install -r requirements.txt

    Ejecutar la API

    uvicorn main:app --reload

Estructura de carpetas propuesta:


├── .env            # variebles 
├── README.md           # instrucciones y inf de la api
├── LICENSE             # licencia de la api
├── requirements.txt.py # las dependencias
├── main.py             # arranca la api
├── dockerfile          # define como construir la imagen para la api
├── .gitignore          # Especifica los archivos y carpetas que no deben ser versionados
├── api.code-workspacee # Configuración para un entorno de desarrollo integrado (IDE) específico
├── .dockerignore       # Similar a .gitignore, pero para Docker
├── utils/              # Funciones utilitarias generales
│   ├── scraping.py     # Funciones relacionadas con el scraping
│   └── scheduler.py    # Funciones relacionadas con la programación de tareas
├── templates/          #
│   ├── email_templete/ # 
│   └── generic_templete/   #  
├── schemas/       # Definiciones de esquemas Pydantic
├── routes/        # Definiciones de las rutas de la API
├── models/        # Definiciones de modelos de base de datos (si los usas)
├── middleware/    # Middleware de la aplicación
├── env/           # Archivos de configuración de entorno
├── test/          # pruebas unitarias de las api
├── controllers/   # Lógica de negocio (controladores)
├── config/         # Lógica de negocio (controladores)
└── ...

## Clonar:

https://github.com/jhonshua/Web_Scraping.git

## documentacion:

https://app.getpostman.com/join-team?invite_code=271a7be96486bacc2dec27d68191660a9394da106257c2a95f0f06c120cc7210&target_code=88e5b57a52f6a3e7af7438cf6cb542e3


**by: Julio cesar llinas**
**www.linkedin.com/in/julio-cesar-llinas-ba65a6127**

