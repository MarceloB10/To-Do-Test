# To-Do List API

Esta es una API REST para gestionar una lista de tareas (To-Do List) creada con Django Rest Framework. La API incluye operaciones básicas de CRUD para las tareas, además de pruebas unitarias, pruebas de integración, documentación swagger, Docker, y más.

## Requerimientos

- Python 3.9 o superior
- Django 3.0 o superior
- Django Rest Framework
- Docker

## Instrucciones para configurar el entorno local

### Paso 1: Clonar el repositorio
Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/MarceloB10/To-Do-Test
cd To-Do-Test
```

### Paso 2: Crear un entorno virtual
Crea y activa un entorno virtual para instalar las dependencias:

```bash
python3 -m venv env
source env/bin/activate  # En macOS/Linux
env\Scripts\activate  # En Windows
```

### Paso 3: Instalar las dependencias
Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

### Paso 4: Configurar la base de datos
Realiza las migraciones para configurar la base de datos local (SQLite):

```bash
python manage.py migrate
```

### Paso 5: Correr el servidor de desarrollo
Inicia el servidor de desarrollo de Django:

```bash
python manage.py runserver
```
El servidor estará disponible en http://localhost:8000.

### Documentación con Swagger

La API incluye documentación automática con Swagger. Una vez que la aplicación esté corriendo, puedes acceder a la documentación en:

- **Swagger UI**: `http://localhost:8000/api/schema/swagger-ui/` (Permite realizar pruebas con la API)
- **ReDoc UI**: `http://localhost:8000//api/schema/redoc/`

## Endpoints de la API

### La API expone los siguientes endpoints:

- GET /api/tasks/ - Obtener todas las tareas.
- POST /api/tasks/ - Crear una nueva tarea.
- GET /api/tasks/{id}/ - Obtener una tarea por su ID.
- PUT /api/tasks/{id}/ - Actualizar una tarea por su ID.
- DELETE /api/tasks/{id}/ - Eliminar una tarea por su ID.

#### Ejemplo de formato de una tarea:

```bash
{
  "id": 1,
  "title": "Sample Task",
  "description": "This is a sample task",
  "completed": false
}
```

## Ejecución de pruebas

### Las pruebas unitarias están incluidas y se ejecutan con el comando:

```bash
python manage.py test
```
Estas pruebas validan que los endpoints de la API funcionen correctamente, incluyendo operaciones de creación, lectura, actualización y eliminación de tareas.


## Linting y Formateo de Código

Se ha configurado flake8 como linter y black para el formateo del código. Puedes ejecutar los comandos de linting y formateo con:

### Linting con flake8:
```bash
flake8
```

### Formateo con black:
```bash
black .
```

### Ordenar imports con isort:
```bash
isort .
```

## Configuración de Docker

También puedes levantar la aplicación usando Docker.

### Paso 1: Construir la imagen de Docker
Desde el directorio raíz del proyecto, ejecuta:

```bash
docker-compose up --build
```
Esto levantará el contenedor con la aplicación y la base de datos. La API estará disponible en 
```bash
http://localhost:8000
```

### Paso 2: Detener y remover los contenedores
Para detener y eliminar los contenedores de Docker, ejecuta:

```bash
docker-compose down
```