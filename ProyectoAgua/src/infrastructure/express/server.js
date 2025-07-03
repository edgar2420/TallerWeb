const express = require("express");
const app = express();

const usuarioRoutes = require("./routes/usuario.routes");

app.use(express.json());
app.use("/api/usuarios", usuarioRoutes);

app.get("/", (req, res) => {
  res.send("Servidor funcionando correctamente");
});

module.exports = app;
