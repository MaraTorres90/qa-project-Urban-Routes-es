Urban Routes — Pruebas con Selenium

Descripción
Urban Routes es una aplicación para solicitar viajes. En este proyecto escribí pruebas con Python y Selenium para revisar el proceso de pedir un taxi con la tarifa Comfort.

Objetivo
Comprobar que el usuario pueda configurar su viaje, ingresar sus datos y avanzar hasta la solicitud del taxi.

Qué hice
- Ingresé las direcciones de origen y destino.
- Seleccioné la tarifa Comfort.
- Agregué y verifiqué un número de teléfono.
- Completé el proceso para agregar una tarjeta.
- Escribí un mensaje para el conductor.
- Seleccioné manta, pañuelos y dos helados.
- Solicité el taxi.
- Comprobé que apareciera la ventana del pedido y una estimación de llegada.

Herramientas
Python, Selenium WebDriver, pytest y Google Chrome.

Cómo organicé el proyecto
- main.py contiene las acciones de la página y las pruebas.
- data.py contiene la dirección del servidor y los datos utilizados.
- requirements.txt contiene las dependencias necesarias.

Utilicé Page Object Model para organizar las acciones de la página y esperas explícitas para interactuar con los elementos cuando estuvieran disponibles.

Cómo ejecutar las pruebas
1. Tener Python y Google Chrome instalados.
2. Iniciar el servidor de Urban Routes.
3. Actualizar BASE_URL en data.py con la dirección del servidor.
4. Instalar las dependencias con
   python -m pip install -r requirements.txt
5. Ejecutar
   python -m pytest main.py -v

Las pruebas deben ejecutarse juntas porque siguen los pasos de un mismo pedido.

Resultados y evidencia
Implementé nueve pruebas para revisar las etapas del pedido. El código comprueba los datos ingresados, las opciones seleccionadas y la aparición de la ventana del pedido.

La comprobación de la tarjeta verifica que el control del método de pago esté visible después de agregarla; no revisa los datos de la tarjeta guardada.

No incluyo un porcentaje de pruebas aprobadas porque no tengo adjunto un reporte actualizado de ejecución.

Video del proyecto
httpsdrive.google.comfiled1CeqLvhGMAkbcWo1lWsNRFJ6zArprfyKuview

Mi aportación
Organicé el flujo en pasos y agregué comprobaciones para identificar en qué parte del pedido puede ocurrir un problema.

Autora
Maarabid Torres — QA Engineer Jr.

Portafolio
httpsmaratorres90.github.io