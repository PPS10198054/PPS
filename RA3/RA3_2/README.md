# Instalación de DVWA en Docker

Este repositorio contiene un conjunto de scripts y herramientas para realizar pruebas de seguridad en DVWA (Damn Vulnerable Web Application) utilizando técnicas de fuerza bruta, SQLi, XSS y más.

## Requisitos Previos

Antes de comenzar, asegúrate de tener Docker instalado en tu máquina. Puedes descargar Docker desde [aquí](https://www.docker.com/get-started).

## Pasos para Instalar DVWA en Docker

1. **Descargar la Imagen de Docker de DVWA**

   Primero, necesitas descargar la imagen de DVWA desde Docker Hub. Para ello, ejecuta el siguiente comando en tu terminal:

```bash
docker pull vulnerables/web-dvwa
```
   
## Descargar la Imagen de Docker de DVWA

Este comando descargará la última versión de DVWA, que es una aplicación web vulnerable diseñada para pruebas de penetración y aprendizaje de seguridad.

## Iniciar un Contenedor con DVWA

Una vez que la imagen se haya descargado, puedes iniciar un contenedor con DVWA usando el siguiente comando:

```bash
docker run --rm -it -p 80:80 vulnerables/web-dvwa
```
## Descargar la Imagen de Docker de DVWA

Este comando descargará la última versión de DVWA, que es una aplicación web vulnerable diseñada para pruebas de penetración y aprendizaje de seguridad.

## Iniciar un Contenedor con DVWA

Una vez que la imagen se haya descargado, puedes iniciar un contenedor con DVWA usando el siguiente comando:

```bash
docker run --rm -it -p 80:80 vulnerables/web-dvwa
```

Este comando hará lo siguiente:

- `--rm`: El contenedor se eliminará automáticamente cuando termine.
- `-it`: Permite la ejecución interactiva del contenedor.
- `-p 80:80`: Mapea el puerto 80 del contenedor al puerto 80 de tu máquina, lo que te permitirá acceder a DVWA en tu navegador local.
- `vulnerables/web-dvwa`: Especifica la imagen que se ejecutará.

Una vez que el contenedor esté en funcionamiento, podrás acceder a DVWA desde tu navegador en `http://localhost` o `http://127.0.0.1`.

## Configurar DVWA

Al acceder a la página, se te pedirá configurar DVWA. Para hacerlo, sigue los pasos a continuación:

1. Accede a `http://localhost` o `http://127.0.0.1`.
2. Inicia sesión con las credenciales predeterminadas:
   - **Usuario:** `admin`
   - **Contraseña:** `password`
3. Después de iniciar sesión, ve a la sección de "DVWA Security" y cambia el nivel de seguridad a "High" para practicar las técnicas de seguridad con un nivel más avanzado.
