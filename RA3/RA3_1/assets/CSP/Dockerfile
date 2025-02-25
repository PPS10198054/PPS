# Usamos una imagen base de Ubuntu
FROM ubuntu:20.04

# Actualizamos los paquetes e instalamos Apache
RUN apt-get update && apt-get install -y \
    apache2 \
    curl \
    vim \
    && apt-get clean

# Copiamos nuestra página web estática al contenedor
COPY ./index.html /var/www/html/index.html

# Habilitamos el módulo mod_headers para configurar CSP
RUN a2enmod headers

# Configuración de Content Security Policy (CSP) en Apache
RUN echo 'Header set Content-Security-Policy "default-src \'self\'; script-src \'self\' https://trusted-cdn.com;"' >> /etc/apache2/apache2.conf

# Exponemos el puerto 80 para acceder al servidor
EXPOSE 80

# Iniciamos Apache en primer plano
CMD ["apache2ctl", "-D", "FOREGROUND"]
