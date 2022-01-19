const mongoose = require('mongoose');

const ProdSchema = new mongoose.Schema({
    title: {
        type: String,
        trum: true,
        minlength: 3,
    },
    price: {
        type: String,
        trum: true,
    },
    reduction: {
        type: String,
        trum: true,
    },
    description: {
        type: String,
        trum: true,
    },
    link: {
        type: String,
        trum: true,
    },
    image: {
        type: String,
        trum: true,
    },
    categorie: {
        type: String,
        trum: true,
    },
});

const Prod = mongoose.model('Prod', ProdSchema);

module.exports = Prod;