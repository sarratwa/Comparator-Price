const express = require('express');
const app = express();
const mongoose = require('./database/mongoose');
const Prod = require('./database/models/product');
var multer = require('multer');
var path = require('path');
var csv = require('csvtojson');
var bodyparser = require('body-parser');

/*
var storage = multer.diskStorage({
    destination:(req,file,cb)=>{
        cb(null,'./public/uploads');
    },
    filename:(req,file,cb)=>{
        cb(null,file.originalname);
    }
});

var uploads = multer({storage:storage});*/

//prepare our app to be able to parse json
app.use(express.json());

//enable CORS (3000 backend api and 4200 frontend)
app.use((req,res,next) => {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, PATCH, DELETE");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});


//set the template engine
app.set('view engine','ejs');

//fetch data from the request
app.use(bodyparser.urlencoded({extended:false}));

//static folder
app.use(express.static(path.resolve(__dirname,'public')));

// create the routes 
// create product

app.post('/products', (req, res) => {
    (new Prod({'title' : req.body.title, 'price' : req.body.price, 'reduction' : req.body.reduction, 'description' : req.body.description, 'link' : req.body.link}))
        .save()
        .then((prod) => res.send(prod))
        .catch((error) => console.log(error));
});

/*

app.post('/',uploads.single('csv'),(req,res)=>{
    //convert csvfile to jsonArray   
   csv()
   .fromFile(req.file.path)
   .then((jsonObj)=>{
       console.log(jsonObj);
       for(var x=0;x<jsonObj;x++){
            temp = parseFloat(jsonObj[x].title)
            jsonObj[x].Test1 = temp;
            temp = parseFloat(jsonObj[x].price)
            jsonObj[x].Test2 = temp;
            temp = parseFloat(jsonObj[x].reduction)
            jsonObj[x].Test3 = temp;
            temp = parseFloat(jsonObj[x].description)
            jsonObj[x].Test4 = temp;
            temp = parseFloat(jsonObj[x].link)
            jsonObj[x].Final = temp;
        }
        Prod.insertMany(jsonObj,(err,data)=>{
               if(err){
                   console.log(err);
               }else{
                   res.redirect('/');
               }
        });
      });
   });

   app.get('/',(req,res)=>{
    Prod.find((err,data)=>{
         if(err){
             console.log(err);
         }else{
              if(data!=''){
                  res.render('demo',{data:data});
              }else{
                  res.render('demo',{data:''});
              }
         }
    });
});

var temp ;*/

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
app.get('/product-detail/:productId', (req, res) => {
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
/*
app.delete('/products/:productId', (req,res) => {
    Prod.findByIdAndDelete(req.params.productId)
        .then(products => res.send(products))
        .catch((error) => console.log(error));
});*/

app.delete('/products', (req,res) => {
    Prod.deleteMany()
        .then(products => res.send(products))
        .catch((error) => console.log(error));
});



app.listen(3000, () => console.log("Server is connected on port 3000"));