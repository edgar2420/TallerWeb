require("dotenv").config();
const sequelize = require("./config/database");
const app = require("./infrastructure/express/server");

const PORT = process.env.PORT || 3000;

async function main() {
  try {
    await sequelize.authenticate();
    console.log("Conexión a la base de datos establecida.");
    await sequelize.sync();

    app.listen(PORT, () => {
      console.log(`Servidor corriendo en http://localhost:${PORT}`);
    });
  } catch (error) {
    console.error("Error al iniciar el servidor:", error);
  }
}

main();
