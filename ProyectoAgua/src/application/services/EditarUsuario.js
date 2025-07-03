class EditarUsuario {
  constructor(repo) {
    this.repo = repo;
  }

  async ejecutar(id, datosActualizados) {
    const usuarioExistente = await this.repo.obtenerPorId(id);
    if (!usuarioExistente) {
      throw new Error("Usuario no encontrado");
    }
    return await this.repo.actualizar(id, datosActualizados);
  }
}