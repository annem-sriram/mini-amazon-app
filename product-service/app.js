const express = require('express');
const app = express();
const PORT = process.env.PORT || 5001;

// Mock database of products
const products = [
    { id: "101", name: "Wireless Mouse", price: 29.99 },
    { id: "102", name: "Mechanical Keyboard", price: 79.99 },
    { id: "103", name: "Gaming Monitor", price: 249.99 }
];

app.use(express.json());

// Endpoint to fetch all products
app.get('/products', (req, res) => {
    res.json(products);
});

// Endpoint to fetch a single product by ID (used internally by Order Service)
app.get('/products/:id', (req, res) => {
    const product = products.find(p => p.id === req.params.id);
    if (product) {
        res.json(product);
    } else {
        res.status(404).json({ error: "Product not found" });
    }
});

app.listen(PORT, () => {
    console.log(`Product Service running on port ${PORT}`);
});
