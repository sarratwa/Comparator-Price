const express = require('express');
const app = express();
const mongoose = require('./database/mongoose');
const Prod = require('./database/models/product');

//enable CORS (3000 backend api and 4200 frontend)
app.use((req,res,next) => {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, PATCH, DELETE");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

// create the routes 


//prepare our app to be able to parse json
app.use(express.json());

app.listen(3000, () => console.log("Server is connected on port 3000"));