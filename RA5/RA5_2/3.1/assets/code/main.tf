resource "null_resource" "ubuntu_vagrant" {
  provisioner "local-exec" {
    command = "cd ../vagrant && vagrant up"
  }
}
