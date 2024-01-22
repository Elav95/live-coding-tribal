# Proyecto Tribal Live Coding 

Este proyecto utiliza [FastAPI](https://fastapi.tiangolo.com/) para crear una API que obtiene chistes aleatorios de Chuck Norris desde [api.chucknorris.io](https://api.chucknorris.io/jokes/random/). El código principal se encuentra en el archivo `main.py`. A continuación, se proporcionan instrucciones básicas para configurar y ejecutar el proyecto.

## Requisitos

Asegúrate de tener instaladas las dependencias necesarias. Puedes hacerlo ejecutando el siguiente comando:

```bash
pip install -r requirements.txt
```

Claro, aquí está el README en formato Markdown (md) con las instrucciones sobre el entorno virtual:

markdown
Copy code
# Proyecto FastAPI

Este proyecto utiliza [FastAPI](https://fastapi.tiangolo.com/) para crear una API que obtiene chistes aleatorios de Chuck Norris desde [api.chucknorris.io](https://api.chucknorris.io/jokes/random/). El código principal se encuentra en el archivo `main.py`. A continuación, se proporcionan instrucciones básicas para configurar y ejecutar el proyecto.

## Requisitos

Asegúrate de tener instaladas las dependencias necesarias. Puedes hacerlo ejecutando el siguiente comando:

```bash
pip install -r requirements.txt
```

## Entorno Virtual
Se recomienda utilizar un entorno virtual para evitar conflictos con otras dependencias. Sigue los pasos a continuación para configurar y activar un entorno virtual:

Abre una terminal en el directorio de tu proyecto.

Instala virtualenv si aún no lo has hecho:

```bash
pip install virtualenv
```
Crea un entorno virtual en el directorio del proyecto (puedes cambiar "venv" por el nombre que desees):

```bash
virtualenv venv
```

Activa el entorno virtual:
### En Windows:

```bash
.\venv\Scripts\activate
```

### En Linux o macOS:

```bash
source venv/bin/activate
```

Una vez activado el entorno virtual, verás el nombre del entorno virtual en el indicador del terminal, indicando que estás trabajando dentro del entorno virtual.

```ruby
(venv) $
```

Para desactivar el entorno virtual, simplemente ejecuta deactivate.

```bash
deactivate
```

## Ejecución

Para ejecutar la aplicación, utiliza el siguiente comando:

```bash
uvicorn main:app --reload
```

Esto iniciará el servidor y permitirá recargar automáticamente en cada cambio durante el desarrollo.

## Endpoints

### `/`

- **Método:** GET
- **Descripción:** Redirige a la documentación de la API.

### `/random`

- **Método:** POST
- **Descripción:** Obtiene una lista de 25 chistes aleatorios de Chuck Norris.
- **Modelo de respuesta:** Lista de cadenas (list[str]).
