const UsuarioModel = require("../models/UsuarioModel");

class SequelizeUsuarioRepo {
  async crear(usuario) {
    return await UsuarioModel.create(usuario);
  }

  async editar(id, datos) {
    await UsuarioModel.update(datos, { where: { id } });
    return await UsuarioModel.findByPk(id);
  }

  async eliminar(id) {
    return await UsuarioModel.update({ estado: false }, { where: { id } });
  }

  async obtenerPorCorreo(correo) {
    return await UsuarioModel.findOne({ where: { correo, estado: true } });
  }

  async obtenerPorId(id) {
    return await UsuarioModel.findByPk(id);
  }

  async listarTodos() {
    return await UsuarioModel.findAll({ where: { estado: true } });
  }
}

module.exports = SequelizeUsuarioRepo;
