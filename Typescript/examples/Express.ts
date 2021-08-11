// first install express for typescript with this command:
// `npm install @types/express`
import express from "express";

// create app and a port
const app = express();
const port = 3000;

// make a very simple route with get method
app.get('/', (req, resp): void => {
    // send a hello world to browser
    resp.send("Hello, World!");
});

// listen app in port 3000 
app.listen(port, () => {
    // whene app started log this on console
    console.log(`app is running in port ${port}`);
});
