const express = require('express');
const bodyParser = require('body-parser');
const fileUpload = require('express-fileupload');
const app = express();


app.use(fileUpload({
    limits: { fileSize: 50 * 1024 * 1024 },
}));

app.use(bodyParser.urlencoded({ extended: false }));


app.use('/uploads', express.static('uploads'));
app.use(express.static('public'));


const db = require("./models");
db.sequelize.sync().then(() => {
    console.log("DB resync");
});

require('./routes')(app);

app.listen(3000, function () {
    console.log('Ingrese a http://localhost:3000');
});
