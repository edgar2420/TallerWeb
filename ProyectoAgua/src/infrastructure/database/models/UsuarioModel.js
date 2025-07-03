const { DataTypes } = require("sequelize");
const sequelize = require("../../../config/database");

const UsuarioModel = sequelize.define("Usuario", {
  nombre: DataTypes.STRING,
  correo: { type: DataTypes.STRING, unique: true },
  contrasena: DataTypes.STRING,
  rol: { type: DataTypes.ENUM("administrativo", "tecnico") },
  estado: { type: DataTypes.BOOLEAN, defaultValue: true }
});

module.exports = UsuarioModel;
