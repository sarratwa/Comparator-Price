const express = require('express');
const app = express();
const mongoose = require('./database/mongoose');
const Prod = require('./database/models/product');

//prepare our app to be able to parse json
app.use(express.json());

//enable CORS (3000 backend api and 4200 frontend)
app.use((req,res,next) => {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, PATCH, DELETE");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

// create the routes 
// create product
app.post('/products', (req, res) => {
    (new Prod({'title' : req.body.title, 'price' : req.body.price, 'reduction' : req.body.reduction, 'description' : req.body.description, 'link' : req.body.link}))
        .save()
        .then((prod) => res.send(prod))
        .catch((error) => console.log(error));
});

// update product
app.patch('/products/:productId', (req,res) => {
    Prod.findOneAndUpdate(
        {'_id' : req.params.productId }, 
        { "$set": { 
            'title' : req.body.title, 
            'price' : req.body.price, 
            'reduction' : req.body.reduction, 
            'description' : req.body.description, 
            'link': req.body.link}
        }
    )
    .then((prod) => res.send(prod))
    .catch((error) => console.log(error));
});

// Read One 
app.get('/products/:productId', (req, res) => {
    Prod.find({_id : req.params.productId})
    .then((prod) => res.send(prod))
    .catch((error) => console.log(error));
});

// Read All
app.get('/products', (req, res) => {
    Prod.find({})
        .then(products => res.send(products))
        .catch((error) => console.log(error));
});

// Delete
app.delete('/products/:productId', (req,res) => {
    Prod.findByIdAndDelete(req.params.productId)
        .then(products => res.send(products))
        .catch((error) => console.log(error));
});

app.listen(3000, () => console.log("Server is connected on port 3000"));