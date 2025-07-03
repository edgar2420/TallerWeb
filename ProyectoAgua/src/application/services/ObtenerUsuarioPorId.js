class ObtenerUsuarioPorId {
  constructor(repo) {
    this.repo = repo;
  }
  async ejecutar(id) {
    return await this.repo.obtenerPorId(id);
  }
}
module.exports = ObtenerUsuarioPorId;