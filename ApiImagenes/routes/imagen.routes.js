const express = require("express");
const router = express.Router();
const controller = require("../controllers/imagen.controller");

router.post("/subir", controller.subirImagen);
router.get("/obtener", controller.obtenerImagenes);
router.delete("/eliminar/:id", controller.eliminarImagen);

module.exports = app => {
  app.use("/imagenes", router);
};
