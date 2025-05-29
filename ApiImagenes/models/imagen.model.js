const { DataTypes } = require('sequelize');


module.exports = (sequelize, Sequelize) => {
    const Imagen = sequelize.define("imagen", {
        foto: {
            type: Sequelize.STRING
        },
        usuarioId: {
            type: DataTypes.INTEGER
        }
    });
    return Imagen;
}