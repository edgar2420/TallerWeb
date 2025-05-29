module.exports = (sequelize, Sequelize) => {
    const Imagen = sequelize.define("imagen", {
        foto: {
            type: Sequelize.STRING
        }
    });
    return Imagen;
}