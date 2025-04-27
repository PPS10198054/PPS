# Weak Session IDs - DVWA

## Security Level: Low

En el nivel de seguridad bajo, el valor de la cookie es fácilmente predecible. Inicialmente, el valor es `0` y se incrementa en `1` cada vez que se regenera.

## Security Level: Medium

En el nivel de seguridad medio, el valor de la cookie se establece utilizando el método `time();`. Esto hace que el valor de la cookie dependa del tiempo, lo que lo hace más difícil de predecir que en el nivel bajo, pero aún puede ser vulnerable dependiendo de la implementación.
