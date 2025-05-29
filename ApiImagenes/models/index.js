const dbConfig = require("../config/db.config.js");
const Sequelize = require("sequelize");

const sequelize = new Sequelize(
    dbConfig.DB,
    dbConfig.USER,
    dbConfig.PASSWORD,
    {
        host: dbConfig.HOST,
        port: dbConfig.PORT,
        dialect: "mysql",
    }
);

const db = {};

db.Sequelize = Sequelize;
db.sequelize = sequelize;

db.imagen = require("./imagen.model.js")(sequelize, Sequelize);

module.exports = db;