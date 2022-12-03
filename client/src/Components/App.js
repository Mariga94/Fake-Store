import React from "react";
import Navbar from "./Navbar";
import Footer from "./Footer";
import sofaArray from "./data";
import categoryArray from "./category-data";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Cart from "./Cart";
import Shop from "./Shop";
import Home from "./Home";
import Categories from "./Categories";
import About from "./About";
import Product from "./ProductItem";

export default function App() {
  // eslint-disable-next-line no-unused-vars
  const [sofas, setSofas] = React.useState(sofaArray);
  const [categories] = React.useState(categoryArray);
  const [cart, setCart] = React.useState([]);
  const [productDesc, setProductDesc] = React.useState();

  function display(id) {
    for (let i = 0; i < sofas.length; i++) {
      let currentObj = sofas[i];
      if (currentObj.id === id) {
        setProductDesc(currentObj)
        
      }
    }
  }
  console.log(productDesc)

  function addItemToCart(id) {
    // Adds item to cart
    setCart((prev) => {
      const arr = [...prev];
      for (let i = 0; i < sofas.length; i++) {
        let currentSofa = sofas[i];
        if (currentSofa.id === id) {
          arr.push(currentSofa);
        }
      }
      return arr;
    });
  }

  return (
    <div>
      <Navbar len={cart.length} />
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route
            path="/category"
            element={<Categories categories={categories} />}
          />
          <Route
            path="/shop"
            element={
              <Shop sofas={sofas} add={addItemToCart} display={display} />
            }
          />
          <Route path="/cart" element={<Cart cart={cart} />} />
          <Route path="/product" element={<Product />} />
        </Routes>
      </BrowserRouter>
      <Footer />
    </div>
  );
}
