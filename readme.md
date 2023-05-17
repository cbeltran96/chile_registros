# Test CHR

Este proyecto es un test de la empresa Chile Registros 

## Instalación

A continuación, se detallan los pasos para instalar y ejecutar el proyecto en un entorno local.

1. Clona el repositorio en tu máquina local:

   git clone https://github.com/cbeltran96/chile_registros

2. Accede al directorio del proyecto:

    cd chile_registros

3. Crea un entorno virtual:
    python -m venv env

4. Activa el entorno virtual:

    - En Windows:
    env\Scripts\activate
    
    - En macOS y Linux:
    source env/bin/activate
    
5. Instala las dependencias del proyecto:
    pip install -r requirements.txt

6. Cambia las credenciales de la base de datos:
    en el archivo settings.py de la carpeta chile_registros deberas cambiar los parametros NAME, USER, PASSWORD por los tuyos

7. Ejecuta las migraciones del proyecto:
    python manage.py makemigrations
    python manage.py migrate

8. Crea un superusuario para el administrador Django e ingresa los datos requeridos:
    python manage.py createsuperuser
    
9. Ejecuta el proyecto:
    python manage.py runserver



## Uso
Para utilizar el software, sigue estos pasos:

1. Abre tu navegador web e ingresa la siguiente dirección: localhost:8000 o http://127.0.0.1:8000 si la primera no funciona.

2. En la página que se carga, encontrarás dos botones. Cada botón te llevará a un listado de datos diferente, uno para bicicletas y otro para sancionatorios.

3. Al cargar la página por primera vez, el software buscará los datos correspondientes y los guardará en ambas opciones.

4. En el caso de los sancionatorios, se creará un archivo JSON en la raiz del proyecto con los datos en el siguiente formato:
    ```json
    [
        {
            "numero": "1",
            "expediente": "A-020-2023",
            "unidad_fiscalizable": "LOTEO CONJUNTO HABITACIONAL EX FUNDICION",
            "nombre_razon_social": "SERVICIO REGIONAL DE VIVIENDA Y URBANISMO SERVIU VIII REGION",
            "categoria": "Vivienda e Inmobiliarios",
            "region": "Region del Biobio",
            "estado": "En curso"
        },
        {
            "numero": "2",
            "expediente": "D-116-2023",
            "unidad_fiscalizable": "PLANTA PROCESADORA DE RECURSOS HIDROBIOLOGICOS PUERTO DEMAISTRE",
            "nombre_razon_social": "PROCESADORA DUMESTRE LIMITADA",
            "categoria": "Pesca y Acuicultura",
            "region": "Region de Magallanes y la Antartica Chilena",
            "estado": "En curso"
        }
    ]
    ```

5. Si accedes a la página de administrador en localhost:8000/admin, encontrarás las listas de datos guardados para administrarlos de manera conveniente.