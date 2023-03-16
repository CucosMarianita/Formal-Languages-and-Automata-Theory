const express = require('express')
const {spawn} = require('child_process');
const app = express()
const port = 3000
app.set('view engine', 'ejs');
const {PythonShell} =require('python-shell');


app.use(express.static('static'))
app.get('/', function(req, res) {
  res.render('index');
});

let afisare=[];
app.get("/start", (req, res, next)=>{
    let options = {
        mode: 'text',
        pythonOptions: ['-u'],
        args: [''] 
    };
    console.log("filtre")
    PythonShell.run('filtre.py', options, function (err, result){
          if (err) throw err;
          console.log('result: ', result.toString());

          // res.send(result.toString())
          var fs = require('fs');
          fs.readFile('date.txt', 'utf8', function(err,data){
          // console.log(data);
          afisare = []
          afisare.push(data);
          res.send(afisare);
    })
    });
    // res.send("done")
    
});


app.get("/crawl", (req, res, next)=>{
  let options = {
      mode: 'text',
      pythonOptions: ['-u'],
      args: [''] 
  };
  console.log("crawl");
  PythonShell.run('crawl.py', options, function (err, result){
        if (err) throw err;
        console.log('result: ', result.toString());
        res.send(result.toString())
        
  });
  // res.send("done")
  
});




app.listen(port, () => {
  console.log(`Example app listening on port http://localhost:${port}/`)
})

