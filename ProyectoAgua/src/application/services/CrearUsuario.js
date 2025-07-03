const bcrypt = require("bcryptjs");

class CrearUsuario {
  constructor(repo) {
    this.repo = repo;
  }

  async ejecutar({ nombre, correo, contrasena, rol }) {
    const existente = await this.repo.obtenerPorCorreo(correo);
    if (existente) throw new Error("Correo ya registrado");

    const hash = await bcrypt.hash(contrasena, 10);
    return await this.repo.crear({ nombre, correo, contrasena: hash, rol });
  }
}

module.exports = CrearUsuario;
