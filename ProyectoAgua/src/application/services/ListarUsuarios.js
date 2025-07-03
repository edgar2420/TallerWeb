class ListarUsuarios {
  constructor(repo) {
    this.repo = repo;
  }
  async ejecutar() {
    return await this.repo.listarTodos();
  }
}
module.exports = ListarUsuarios;