//handle routes
const express = require('express')
//req body
const bodyParser = require("body-parser");
//so any other can use
const cors = require('cors');

const app = express()
app.use(bodyParser.json());

//python
const { spawn } = require('child_process');

// Specify the path to your Python executable
const pythonPath = 'C:/Users/Parth/anaconda3/python.exe'; // Update this with your Python path

// Arguments for the Python script



// Allow requests from specific origin (replace '*' with your frontend URL in production)
app.use(cors({ origin: 'http://localhost:3000' }));

app.get("/api", (req, res) => {
    res.json(`hello how are you sir`)
})
app.post("/getmoney", async (req, res) => {
    try {
      const { location, bhk, bath, sqft } = req.body;
      const pythonPath = 'C:/Users/Parth/anaconda3/python.exe';// Update with your Python path
      const pythonArgs = ['./model/modeluse.py', location, bhk, bath, sqft];
  
      const pythonProcess = spawn(pythonPath, pythonArgs);
  
      let result = await new Promise((resolve, reject) => {
        let dataBuffer = '';
  
        pythonProcess.stdout.on('data', (data) => {
          dataBuffer += data.toString();
        });
  
        pythonProcess.on('close', (code) => {
          if (code !== 0) {
            reject(`Python process exited with code ${code}`);
          } else {
            const parsedResult = parseFloat(dataBuffer.trim());
            if (isNaN(parsedResult)) {
              reject('Invalid result from Python script');
            } else {
              resolve(parsedResult);
            }
          }
        });
        pythonProcess.on('error', (err) => {
          reject(err);
        });
      });
  
      // Handle negative values
      if (result < 0) {
        result = 0;
      }
  
      console.log(`${result}`);
  
      // Send JSON response
      res.status(200).json(result);
    } catch (error) {
      console.error('Error:', error);
      res.status(500).json({ error: 'Internal server error' });
    }
  });
  
  
  

app.listen(5000, () => { console.log("Server started on port 5000") })