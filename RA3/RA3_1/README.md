# Prácticas Docker - Seguridad Web y ModSecurity

Este repositorio contiene varias prácticas centradas en la creación, configuración y protección de servidores web Apache dentro de contenedores Docker. Las prácticas están orientadas a mejorar la seguridad de las aplicaciones web mediante herramientas como **OWASP ModSecurity CRS** y el módulo **mod_evasive** para prevenir ataques de denegación de servicio (DoS). Además, se incluyen pasos para la instalación de un certificado SSL autofirmado en el servidor Apache para mejorar la seguridad en las comunicaciones.

## Resumen del Proceso

### Práctica 1: Instalación y Configuración de Apache en Docker

En esta práctica, se creó un contenedor Docker basado en Ubuntu. Dentro de este contenedor, se instaló el servidor web **Apache** y se configuró una página web estática simple. El objetivo principal de esta práctica era crear un servidor web básico en Docker y familiarizarnos con el uso de contenedores en un entorno de desarrollo.

**Pasos realizados:**
- Instalación de Apache mediante los paquetes estándar de Ubuntu.
- Creación de una página estática en HTML que se sirvió desde el servidor web.
- Exposición del puerto 80 en el contenedor para permitir el acceso a la página desde el navegador.

Finalmente, al acceder a la URL `http://localhost:8080`, el servidor Apache mostró correctamente la página web estática configurada.

**Imagen Docker de Apache (Práctica 1)**:  
[Enlace a Docker Hub](https://hub.docker.com/repository/docker/pps10198054/pr3.1.1/general)

### Práctica 2: Instalación y Configuración de OWASP ModSecurity

La segunda práctica consistió en la instalación y configuración de **OWASP ModSecurity CRS** (Core Rule Set) para proteger el servidor Apache contra una amplia gama de ataques web, incluyendo inyecciones SQL, XSS (cross-site scripting) y otros ataques comunes. ModSecurity es un **firewall de aplicaciones web** (WAF) que actúa como una capa de seguridad adicional.

**Pasos realizados:**
- Instalación del módulo **mod_security2** en Apache.
- Clonación del repositorio oficial de **OWASP ModSecurity CRS** y configuración de las reglas de seguridad estándar.
- Configuración de Apache para cargar las reglas de ModSecurity y asegurar el servidor contra ataques.

**Prueba de funcionamiento:**
- Se creó un archivo `index.php` con una vulnerabilidad XSS a propósito.
- Se intentó realizar un ataque XSS utilizando el parámetro `?name=<script>alert('XSS')</script>`.
- El **ModSecurity CRS** bloqueó el ataque, generando una respuesta **403 Forbidden**.

**Imagen Docker con ModSecurity (Práctica 2)**:  
[Enlace a Docker Hub](https://hub.docker.com/repository/docker/pps10198054/pr3.1.2/general)

**Captura de pantalla de la respuesta bloqueada por ModSecurity:**
![Respuesta bloqueada por ModSecurity](assets/pruebaWAF.png)

### Práctica 3: Instalación de Módulo mod_evasive

La siguiente fase fue la instalación de **mod_evasive**, un módulo de Apache diseñado para mitigar ataques de **denegación de servicio** (DoS) y **fuerza bruta**. Este módulo protege el servidor limitando la cantidad de solicitudes de un cliente en un corto período de tiempo, previniendo que el servidor se vea sobrecargado por tráfico malicioso.

**Pasos realizados:**
- Instalación del módulo `mod_evasive` en Apache.
- Configuración de las reglas de protección, como limitar el número de solicitudes por minuto y bloquear a los clientes que superen este umbral.
- Configuración de los logs y notificaciones por correo electrónico en caso de ataques.

**Pruebas de carga:**
- Para comprobar el funcionamiento de **mod_evasive**, se utilizó **ApacheBench** (herramienta de benchmarking de Apache) para realizar un ataque DoS simulado con **1000 solicitudes** concurrentes.
- Se verificó que las IPs que intentaban realizar el ataque fueron bloqueadas correctamente después de superar el umbral de solicitudes.

**Imagen Docker con mod_evasive (Práctica 3)**:  
[Enlace a Docker Hub](https://hub.docker.com/repository/docker/pps10198054/pr3.1.4/general)

**Captura de pantalla de la respuesta bloqueada por mod_evasive:**
![Respuesta bloqueada por mod_evasive](assets/validacionAtaqueDDos.png)

### Práctica 3.2.1: Instalación de un Certificado Digital Autofirmado en Apache

Como paso adicional de seguridad, se instaló un **certificado SSL autofirmado** en el servidor Apache. El propósito de este paso fue asegurar las comunicaciones entre el cliente y el servidor utilizando el protocolo HTTPS, lo cual encripta los datos transmitidos para proteger la privacidad y seguridad de los usuarios.

**Pasos realizados:**
- Generación de un certificado SSL autofirmado utilizando herramientas como **OpenSSL**.
- Instalación y configuración de Apache para utilizar este certificado en el puerto 443 (HTTPS).
- Creación de un `Dockerfile` que incluye la instalación del certificado SSL, permitiendo que el servidor Apache sirviera contenido encriptado a través de HTTPS.

![Certificado dentro de la web](images/certificado.png)

El certificado SSL autofirmado fue utilizado para verificar la configuración en entornos de desarrollo, mientras que en producción se recomienda utilizar un certificado de una **autoridad certificadora confiable**.

Para probar esto, se debe iniciar el contenedor, una vez esté iniciado el contenedor se debe acceder mediante https.

**Imagen Docker con certificado SSL (Práctica 3.2.1)**:  
[Enlace a Docker Hub](https://hub.docker.com/repository/docker/pps10198054/pr3.1.4/general)

### Práctica 4: Pruebas de Carga y Validación de mod_evasive

En esta práctica, se realizó una prueba de carga para validar que **mod_evasive** estaba funcionando correctamente. Se utilizó **ApacheBench** para simular múltiples solicitudes concurrentes al servidor web, asegurando que **mod_evasive** bloqueara correctamente las solicitudes excesivas.

El comando utilizado fue:

```bash
ab -n 1000 -c 10 http://localhost:8080/



