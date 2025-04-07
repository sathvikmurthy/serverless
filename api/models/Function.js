const mongoose = require("mongoose");

const schema = new mongoose.Schema({
    name: { type: String, required: true },
    route: { type: String, required: true },
    language: { type: String, enum: ['python', 'javascript'], required: true },
    timeout: { type: Number, default: 5 },
    code: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
})

module.exports = mongoose.model('Function', schema);