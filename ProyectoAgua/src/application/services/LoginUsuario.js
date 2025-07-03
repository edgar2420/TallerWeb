const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");

class LoginUsuario {
  constructor(repo) {
    this.repo = repo;
  }

  async ejecutar({ correo, contrasena }) {
    const usuario = await this.repo.obtenerPorCorreo(correo);
    if (!usuario || !usuario.estado) throw new Error("Usuario no válido");

    const valido = await bcrypt.compare(contrasena, usuario.contrasena);
    if (!valido) throw new Error("Contraseña incorrecta");

    const token = jwt.sign({ id: usuario.id, rol: usuario.rol }, process.env.JWT_SECRET, { expiresIn: "1d" });
    return { token, usuario };
  }
}

module.exports = LoginUsuario;
