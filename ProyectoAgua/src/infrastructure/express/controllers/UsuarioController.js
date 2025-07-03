const SequelizeUsuarioRepo = require("../../database/repositories/SequelizeUsuarioRepo");
const CrearUsuario = require("../../../application/services/CrearUsuario");
const LoginUsuario = require("../../../application/services/LoginUsuario");
const EditarUsuario = require("../../../application/services/EditarUsuario");
const EliminarUsuario = require("../../../application/services/EliminarUsuario");
const ListarUsuarios = require("../../../application/services/ListarUsuarios");
const ObtenerUsuarioPorId = require("../../../application/services/ObtenerUsuarioPorId");
const repo = new SequelizeUsuarioRepo();
module.exports = {
  crear: async (req, res) => {
    try {
      const servicio = new CrearUsuario(repo);
      const result = await servicio.ejecutar(req.body);
      res.status(201).json(result);
    } catch (e) {
      res.status(400).json({ error: e.message });
    }
  },
  login: async (req, res) => {
    try {
      const servicio = new LoginUsuario(repo);
      const result = await servicio.ejecutar(req.body);
      res.json(result);
    } catch (e) {
      res.status(401).json({ error: e.message });
    }
  },
  editar: async (req, res) => {
    try {
      const servicio = new EditarUsuario(repo);
      const result = await servicio.ejecutar(req.params.id, req.body);
      res.json(result);
    } catch (e) {
      res.status(400).json({ error: e.message });
    }
  },
  eliminar: async (req, res) => {
    try {
      const servicio = new EliminarUsuario(repo);
      await servicio.ejecutar(req.params.id);
      res.status(204).end();
    } catch (e) {
      res.status(400).json({ error: e.message });
    }
  },
  listar: async (_req, res) => {
    try {
      const servicio = new ListarUsuarios(repo);
      const result = await servicio.ejecutar();
      res.json(result);
    } catch (e) {
      res.status(500).json({ error: e.message });
    }
  },
  obtener: async (req, res) => {
    try {
      const servicio = new ObtenerUsuarioPorId(repo);
      const result = await servicio.ejecutar(req.params.id);
      res.json(result);
    } catch (e) {
      res.status(404).json({ error: e.message });
    }
  }
};
