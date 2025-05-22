# 🛠️ Proyecto de Automatización con Terraform y Ansible

Este proyecto utiliza **Terraform** para aprovisionar máquinas virtuales y **Ansible** para configurarlas automáticamente (por ejemplo, instalando Apache y desplegando contenido web).

---

## ⚙️ Requisitos previos

- VirtualBox
- Vagrant
- Git (opcional pero recomendado)
- Conexión a Internet

---

## ✅ Instalación de Terraform

### 1. Descargar binario oficial
Descarga la versión adecuada desde el sitio oficial:

👉 https://developer.hashicorp.com/terraform/downloads

### 2. Instalar manualmente

Ejemplo para sistemas Linux de 64 bits:

```bash
wget https://releases.hashicorp.com/terraform/1.8.4/terraform_1.8.4_linux_amd64.zip
unzip terraform_1.8.4_linux_amd64.zip
sudo mv terraform /usr/local/bin/
terraform -v  # Verifica la instalación
```

## ✅ Instalación de Ansible

### Para sistemas basados en Debian/Ubuntu/Kali

```bash
sudo apt update
sudo apt install ansible -y
```

### 🔍 Verificar la instalación

Para comprobar que Ansible se instaló correctamente, ejecuta:

```bash
ansible --version
```
