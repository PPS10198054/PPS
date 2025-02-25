# Usa la imagen existente que subiste a Docker Hub como base
FROM pps10198054/pr3.1.1
 
# Establecer el directorio de trabajo
WORKDIR /root
 
# Instalar las dependencias necesarias
RUN apt-get update && apt-get install -y \
    libapache2-mod-security2 \
    git \
    nano \
    curl \
    && apt-get clean
 
# Clonar el repositorio de reglas OWASP ModSecurity CRS
RUN git clone https://github.com/SpiderLabs/owasp-modsecurity-crs.git
 
# Mover el archivo de configuración de OWASP y las reglas al lugar correcto
RUN mv /root/owasp-modsecurity-crs/crs-setup.conf.example /etc/modsecurity/crs-setup.conf \
    && mv /root/owasp-modsecurity-crs/rules /etc/modsecurity/rules
 
# Habilitar el motor de ModSecurity y asegurarse de que las reglas OWASP se incluyan en la configuración de Apache
RUN sed -i 's/SecRuleEngine DetectionOnly/SecRuleEngine On/' /etc/modsecurity/modsecurity.conf-recommended \
    && mv /etc/modsecurity/modsecurity.conf-recommended /etc/modsecurity/modsecurity.conf \
    && echo "IncludeOptional /etc/modsecurity/*.conf" >> /etc/apache2/mods-enabled/security2.conf \
    && echo "Include /etc/modsecurity/rules/*.conf" >> /etc/apache2/mods-enabled/security2.conf
 
# Añadir una regla de ejemplo de ModSecurity (de la práctica 2)
RUN echo "SecRuleEngine On" >> /etc/apache2/sites-available/000-default.conf \
    && echo "SecRule ARGS:testparam \"@contains test\" \"id:1234,deny,status:403,msg:'Cazado por Ciberseguridad'\"" >> /etc/apache2/sites-available/000-default.conf
 
# Exponer los puertos 80 y 443 para el tráfico HTTP y HTTPS
EXPOSE 80 443
 
# Comando para iniciar Apache
CMD ["apache2ctl", "-D", "FOREGROUND"]
