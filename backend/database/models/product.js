const mongoose = require('mongoose');

const ProdSchema = new mongoose.Schema({
    title: {
        type: String,
        trum: true,
        minlength: 3,
    }
});

const Prod = mongoose.model('Prod', ProdSchema);

module.exports = Prod;