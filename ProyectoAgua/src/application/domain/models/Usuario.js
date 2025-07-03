class Usuario {
  constructor({ id, nombre, correo, contrasena, rol, estado }) {
    this.id = id;
    this.nombre = nombre;
    this.correo = correo;
    this.contrasena = contrasena;
    this.rol = rol;
    this.estado = estado ?? true;
  }
}

module.exports = Usuario;
