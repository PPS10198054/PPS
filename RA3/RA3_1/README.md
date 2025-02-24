# Prácticas Docker - Seguridad Web y ModSecurity

Este repositorio contiene varias prácticas centradas en la creación, configuración y protección de servidores web Apache dentro de contenedores Docker. Las prácticas están orientadas a mejorar la seguridad de las aplicaciones web mediante herramientas como **OWASP ModSecurity CRS** y el módulo **mod_evasive** para prevenir ataques de denegación de servicio (DoS).

## Resumen del Proceso

### Práctica 1: Instalación y Configuración de Apache en Docker

En esta práctica, creamos un contenedor Docker basado en Ubuntu. Dentro del contenedor, instalamos Apache y configuramos una página web estática simple. Esta práctica tiene como objetivo establecer un servidor web básico en Docker, con el cual comenzamos a familiarizarnos con la gestión de contenedores Docker para servidores web.

El proceso incluye la construcción de la imagen Docker a partir de un `Dockerfile` y la exposición del puerto del contenedor para que el servidor Apache pueda ser accedido desde el navegador. Finalmente, al acceder a la URL correspondiente en el navegador, el servidor Apache debe mostrar la página estática configurada.

### Práctica 2: Instalación y Configuración de OWASP ModSecurity

En esta fase, añadimos una capa adicional de seguridad al servidor web instalando **OWASP ModSecurity CRS (Core Rule Set)**. ModSecurity es un cortafuegos para aplicaciones web (WAF) que se integra con Apache para detectar y prevenir ataques como inyecciones SQL, cross-site scripting (XSS), y otros ataques comunes.

La configuración de ModSecurity incluye la instalación del módulo `mod_security2`, la integración de las reglas de seguridad OWASP CRS, y la modificación de archivos de configuración para asegurar que el servidor esté protegido. El resultado es un servidor Apache mucho más seguro frente a una gran variedad de amenazas web.

### Práctica 3: Instalación de Módulo mod_evasive

El siguiente paso consiste en la instalación y configuración de **mod_evasive**, un módulo de Apache diseñado para proteger el servidor web contra ataques de denegación de servicio (DoS) o ataques de fuerza bruta, mediante la limitación de la tasa de solicitudes de un cliente.

Al instalar y configurar `mod_evasive`, establecemos reglas que bloquean a los clientes que envían solicitudes excesivas en un corto período de tiempo, mitigando así la posibilidad de que el servidor sea abrumado por tráfico malicioso.

### Práctica 4: Pruebas de Carga y Validación de mod_evasive

Para verificar que el módulo `mod_evasive` está funcionando correctamente, realizamos pruebas de carga utilizando **ApacheBench**. Este es un protocolo de pruebas que simula múltiples solicitudes concurrentes al servidor web para determinar si está protegido contra intentos de sobrecarga.

Al realizar estas pruebas, podemos observar que si el servidor es atacado con demasiadas solicitudes en un corto período de tiempo, el módulo `mod_evasive` bloquea las IPs que están realizando estas solicitudes excesivas, evitando así que el servidor se caiga debido a un ataque DoS.

---

## Enlaces a Docker Hub

A continuación, se incluyen los enlaces a Docker Hub donde se pueden encontrar las imágenes Docker utilizadas durante las prácticas:

- **Imagen Docker de Apache (Práctica 1)**: [Enlace a Docker Hub](https://hub.docker.com/r/yourusername/apache-practica1)
- **Imagen Docker con ModSecurity (Práctica 2)**: [Enlace a Docker Hub](https://hub.docker.com/r/yourusername/apache-modsecurity)
- **Imagen Docker con mod_evasive (Práctica 3)**: [Enlace a Docker Hub](https://hub.docker.com/r/yourusername/apache-modevasive)

---

## Imágenes de Validación

A continuación se muestran algunas imágenes de validación durante las prácticas para verificar la correcta configuración y funcionamiento de los servidores web:

1. **Página web servida por Apache**:
   ![Página web estática servida por Apache](images/pagina_estatica.png)

2. **Respuesta bloqueada por ModSecurity**:
   ![Respuesta 403 bloqueada por ModSecurity](images/response_403_modsecurity.png)

3. **Respuesta bloqueada por mod_evasive (Ataque DoS)**:
   ![Respuesta bloqueada por mod_evasive](images/response_modevasive.png)

---

Este README resume los pasos seguidos en cada práctica y proporciona los enlaces necesarios para acceder a las imágenes Docker y las capturas de pantalla de las validaciones realizadas.


