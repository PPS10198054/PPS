# Stored Cross Site Scripting (XSS) - DVWA

## Descripción del Ataque

El **Stored Cross Site Scripting (XSS)** es una vulnerabilidad donde un atacante puede inyectar código malicioso que se almacena de manera persistente en el servidor y es reflejado a los usuarios cuando acceden a la página. En este caso, la vulnerabilidad está presente en el campo de mensaje de DVWA.

## Security Level: Low

En el nivel de seguridad bajo, la aplicación no valida correctamente las entradas de los usuarios, lo que permite que un atacante inyecte código malicioso fácilmente.

## Proceso para Realizar el Ataque

### Paso 1: Identificar la Vulnerabilidad

En la aplicación DVWA, se nos presentan dos campos: **nombre** y **mensaje**. Para realizar el ataque de XSS almacenado, insertamos un payload malicioso en el campo de mensaje.

### Paso 2: Inyectar el Payload

Introduce el siguiente **payload** en el campo de mensaje:

```html
<img src="x" onerror="alert(document.cookie)">
```


