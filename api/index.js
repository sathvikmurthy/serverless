const express = require('express');
const mongoose = require("mongoose");

const app = express();

app.get("/", (req, res) => {
    res.send("Hello World");
})

app.listen(3001, () => {
    console.log("Server is Running!");
})