const path = require('path');
const db = require('../models');
const Imagen = db.imagen;

exports.subirImagen = async (req, res) => {
    console.log('Archivos recibidos:', req.files);

    if (!req.files || !req.files.foto) {
        return res.status(400).json({ message: 'No se envió ninguna imagen' });
    }

    const archivos = Array.isArray(req.files.foto) ? req.files.foto : [req.files.foto];
    const resultados = [];

    for (const archivo of archivos) {
        const extension = path.extname(archivo.name).toLowerCase();
        const nombre = `img-${Date.now()}-${Math.floor(Math.random() * 1000)}${extension}`;
        const ruta = path.join(__dirname, '../uploads', nombre);

        try {
            await archivo.mv(ruta);
            const imagen = await Imagen.create({ foto: nombre });
            resultados.push(imagen);
        } catch (error) {
            resultados.push({ error: `Error al guardar ${archivo.name}` });
        }
    }

    res.json(resultados);
};
