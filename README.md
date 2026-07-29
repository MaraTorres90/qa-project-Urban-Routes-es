# Proyecto Urban Routes

## Descripción del proyecto

En este proyecto realicé pruebas automatizadas para la aplicación Urban Routes.
El objetivo fue comprobar el proceso completo para pedir un taxi.

Las pruebas realizan los siguientes pasos:

- Escribir las direcciones de origen y destino.
- Seleccionar la tarifa Comfort.
- Agregar un número de teléfono.
- Agregar una tarjeta.
- Escribir un mensaje para el conductor.
- Pedir una manta y pañuelos.
- Pedir dos helados.
- Solicitar el taxi.
- Comprobar que aparece la ventana de búsqueda del conductor.
- Esperar la información del conductor.

## Tecnologías y técnicas utilizadas

Para realizar el proyecto utilicé:

- Python para escribir el código.
- Selenium WebDriver para controlar el navegador.
- Pytest para crear y ejecutar las pruebas.
- Localizadores como ID, CSS Selector y XPath para encontrar los elementos.
- Esperas explícitas para esperar a que los elementos aparezcan.
- Page Object Model para separar las acciones de la página de las pruebas.

## Cómo ejecutar las pruebas

Primero se debe iniciar el servidor de Urban Routes y copiar su dirección en la
variable `BASE_URL` del archivo `data.py`.

Después, se abre una terminal en la carpeta del proyecto y se instalan las
dependencias:

```powershell
pip install -r requirements.txt
```

Para ejecutar todas las pruebas:

```powershell
pytest main.py -v
```

Al ejecutar el comando, Chrome se abre automáticamente y las pruebas realizan
el proceso de pedir un taxi.
