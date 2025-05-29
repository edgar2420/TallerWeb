const path = require('path');
const db = require('../models');
const Imagen = db.imagen;

exports.subirImagen = async (req, res) => {
    console.log('Archivos recibidos:', req.files);

    if (!req.files || !req.files.foto) {
        return res.status(400).json({ message: 'No se envió ninguna imagen' });
    }

    const { usuarioId } = req.body;
    if (!usuarioId) {
        return res.status(400).json({ message: 'El usuarioId es obligatorio' });
    }

    const archivos = Array.isArray(req.files.foto) ? req.files.foto : [req.files.foto];
    const resultados = [];

    for (const archivo of archivos) {
        const extension = path.extname(archivo.name).toLowerCase();
        const nombre = `img-${Date.now()}-${Math.floor(Math.random() * 1000)}${extension}`;
        const ruta = path.join(__dirname, '../uploads', nombre);

        try {
            await archivo.mv(ruta);
            const imagen = await Imagen.create({
                foto: `/uploads/${nombre}`,
                usuarioId: usuarioId || null,
            });

            resultados.push(imagen);
        } catch (error) {
            console.error(`Error al guardar ${archivo.name}:`, error);
            resultados.push({ error: `Error al guardar ${archivo.name}` });
        }
    }

    res.json(resultados);
};


exports.obtenerImagenes = async (req, res) => {
    try {
        const imagenes = await Imagen.findAll();
        res.json(imagenes);
    } catch (error) {
        console.error('Error al obtener imágenes:', error);
        res.status(500).json({ message: 'Error al obtener imágenes' });
    }
}

exports.eliminarImagen = async (req, res) => {
    const { id } = req.params;

    try {
        const imagen = await Imagen.findByPk(id);
        if (!imagen) {
            return res.status(404).json({ message: 'Imagen no encontrada' });
        }

        const ruta = path.join(__dirname, '../uploads', imagen.foto);
        await Imagen.destroy({ where: { id } });


        const fs = require('fs');
        fs.unlink(ruta, (err) => {
            if (err) {
                console.error('Error al eliminar el archivo:', err);
            }
        });

        res.json({ message: 'Imagen eliminada correctamente' });
    } catch (error) {
        console.error('Error al eliminar la imagen:', error);
        res.status(500).json({ message: 'Error al eliminar la imagen' });
    }
}