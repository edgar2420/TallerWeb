const express = require("express");
const router = express.Router();
const controller = require("../controllers/UsuarioController");
const auth = require("../middlewares/authMiddleware");
const role = require("../middlewares/roleMiddleware");

router.post("/crear", auth, role("administrativo"), controller.crear);
router.post("/login", controller.login);
router.put("/:id", auth, role("administrativo"), controller.editar);
router.delete("/:id", auth, role("administrativo"), controller.eliminar);
router.get("/", auth, role("administrativo"), controller.listar);
router.get("/:id", auth, controller.obtener);

module.exports = router;