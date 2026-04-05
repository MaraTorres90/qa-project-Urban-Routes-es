Pruebas Automatizadas Urban Routes
Nombre del Proyecto

Urban Routes - Automatización de Pruebas End-to-End (Sprint 9)

Descripción del Proyecto

Este proyecto contiene pruebas automatizadas end-to-end para la aplicación web Urban Routes. El objetivo es validar el flujo completo de solicitud de un taxi utilizando Selenium y pytest.

Las pruebas automatizadas simulan el comportamiento real de un usuario, cubriendo funcionalidades clave como:

Configuración de dirección de origen y destino
Selección de la tarifa Comfort
Ingreso del número de teléfono
Agregar una tarjeta de crédito
Escribir un mensaje para el conductor
Seleccionar opciones adicionales (manta y pañuelos)
Solicitar productos (helados)
Pedir un taxi
Validar que el proceso de asignación de conductor inicia correctamente

Este proyecto sigue buenas prácticas de automatización utilizando el patrón de diseño Page Object Model (POM).

Tecnologías y Técnicas Utilizadas
Tecnologías
Python 3
Selenium WebDriver
pytest
Técnicas y Conceptos
Page Object Model (POM)
Esperas explícitas (WebDriverWait)
Automatización de pruebas UI
Separación de datos de prueba (data.py)
Estructura modular y escalable
Pruebas End-to-End (E2E)
Estructura del Proyecto
qa-project-Urban-Routes-es/
│
├── data.py                    # Datos de prueba y configuración
├── main.py                    # Casos de prueba (pytest)
├── pages/
│   └── urban_routes_page.py  # Page Object (localizadores + métodos)
├── conftest.py                # Fixtures y configuración de pruebas
└── README.md                  # Documentación del proyecto

Cómo Ejecutar las Pruebas
1. Clonar el repositorio
git clone <repository_url>
cd urban_routes_tests
2. Instalar dependencias

Asegúrate de tener Python instalado y ejecuta:

pip install -r requirements.txt

(Si no tienes requirements.txt, instala manualmente:)

pip install selenium pytest
3. Ejecutar las pruebas
pytest main.py
4. (Opcional) Ejecutar con salida detallada
pytest -v
Configuración
Actualiza la variable BASE_URL en data.py con el entorno asignado.
Asegúrate de tener ChromeDriver instalado y compatible con tu navegador.
Notas
El proyecto utiliza esperas explícitas para mejorar la estabilidad de las pruebas.
Todas las interacciones con la interfaz están encapsuladas en la clase Page Object.
Los datos de prueba están separados para facilitar el mantenimiento.

Autor

Reyna Maarabid de Jesús Torres García