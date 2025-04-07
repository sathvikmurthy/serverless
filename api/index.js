const express = require('express');
const mongoose = require("mongoose");
require('dotenv').config()

const Function = require('./models/Function');

const app = express();
app.use(express.json());

mongoose.connect(`${process.env.MONGO_URL}`, console.log("MongoDB Connected!"));

// create a function
app.post('/', async (req, res) => {
    try {
        const newFunc = new Function({
            name: req.body.name,
            route: req.body.route,
            language: req.body.language,
            timeout: req.body.timeout,
            code: req.body.code
        })
        await newFunc.save()
        res.send(newFunc);
    } catch (err) {
        res.status(400).send({ error: err.message });
    }
})

// get all functions
app.get("/", async (req, res) => {
    const functions = await Function.find();
    res.send(functions);
})

// get function by id
app.get("/:id", async (req, res) => {
    try {
        const func = await Function.findById(req.params.id)
        if (!func) return res.status(404).send({ error: 'Function not found' });
        res.send(func);
    } catch (err) {
        res.status(400).send({ error: 'Invalid ID' });
    }
    
})

// update function
app.put("/:id", async (req, res) => {
    try {
        const updatedFunc = await Function.findByIdAndUpdate(
          req.params.id,
          req.body,
          { new: true }
        );
        res.send(updatedFunc);
    } catch (err) {
        res.status(400).send({ error: err.message });
    }
})

// delete function
app.delete("/:id", async (req, res) => {
    try {
        await Function.findByIdAndDelete(req.params.id);
        res.send({ message: 'Function deleted' });
    } catch (err) {
        res.status(400).send({ error: err.message });
    }
})

app.listen(3001, () => {
    console.log("Server is Running!");
})