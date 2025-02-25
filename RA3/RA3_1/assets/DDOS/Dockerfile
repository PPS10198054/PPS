# Usar la imagen base que subiste a Docker Hub
FROM pps10198054/pr3.1.2
 
# Establecer variables de entorno para evitar que el sistema pida confirmación
ENV DEBIAN_FRONTEND=noninteractive
 
# Actualizar e instalar apache y mod_evasive
RUN apt-get update && \
    apt-get install -y libapache2-mod-evasive apache2-utils && \
    apt-get clean
 
# Habilitar mod_evasive
RUN a2enmod evasive
 
# Configuración del mod_evasive: Copiar el archivo de configuración
COPY mod_evasive.conf /etc/apache2/mods-enabled/evasive.conf
 
# Exponer el puerto 80 para acceder al servidor
EXPOSE 80
 
# Reiniciar Apache para aplicar cambios
CMD ["apache2ctl", "-D", "FOREGROUND"]
