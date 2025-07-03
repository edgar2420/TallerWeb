class EliminarUsuario {
  constructor(repo) {
    this.repo = repo;
  }
  async ejecutar(id) {
    return await this.repo.eliminar(id);
  }
}
module.exports = EliminarUsuario;