import React from "react";
import Navbar from "./Navbar";
import Footer from "./Footer";
import { Routes, Route, useNavigate } from "react-router-dom";
import Cart from "./Cart";
import Shop from "./Shop";
import Home from "./Home";
import Categories from "./Categories";
import CategoryProduct from "./CategoryProduct";
import About from "./About";
import Product from "./ProductItem";
import axios from "axios";


export default function App() {
  const [categoryProduct, setCategoryProduct] = React.useState([]);
  const [products, setProducts] = React.useState([]);
  const [categories, setCategories] = React.useState([]);
  const [cart, setCart] = React.useState([]);
  // const [error, setError] = React.useState(null);
  // const [isLoaded, setIsLoaded] = React.useState(false);
  const navigate = useNavigate();

  const fetchProducts = () => {
    axios.get("http://127.0.0.1:5000/api/v1/products").then((res) => {
      setProducts(res.data);
    });
  };

  const fetchCategories = () => {
    axios.get("http://127.0.0.1:5000/api/v1/categories").then((res) => {
      setCategories(res.data);
    });
  };

  const fetchCategoryById = (id) => {
    axios
      .get(`http://127.0.0.1:5000/api/v1/categories/${id}/product`)
      .then((res) => {
        const categoryProduct = res.data;
        setCategoryProduct(
          window.localStorage.setItem(
            "categoryProduct",
            JSON.stringify(categoryProduct)
          )
        );
        navigateToCategoryProduct();
      });
  };

  function fetchCart() {
    axios.get("http://127.0.0.1:5000/api/v1/cart").then((res) => {
      setCart(res.data);
    });
  }

  function AddToCart(id) {
    let obj = {};
    for (let i = 0; i < products.length; i++) {
      let current = products[i];
      if (current.id === id) {
        obj["id"] = current.id;
        console.log(obj);
        axios.post(`http://127.0.0.1:5000/api/v1/cart/${id}`, obj).then(
          (res) => {
            console.log(res);
          },
          (error) => {
            console.log(error);
          }
        );
      }
    }
  }

  function deleteItemFromCart(cartId) {
    axios.delete(`http://127.0.0.1:5000/api/v1/cart/${cartId}`).then(
      (res) => {
        console.log(res);
      },
      (error) => {
        console.log(error);
      }
    );
  }

  React.useEffect(() => {
    fetchProducts();
    fetchCategories();
    fetchCart();
    setCategoryProduct(
      JSON.parse(window.localStorage.getItem("categoryProduct"))
    );
  }, []);

  // Navigation
  function navigateToCategoryProduct() {
    navigate("/category/:id/product");
  }

  return (
    <div>
      <Navbar len={cart.length} />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route
          path="/products"
          element={<Shop products={products} add={AddToCart} />}
        />
        <Route
          path="/cart"
          element={<Cart cart={cart} deleted={deleteItemFromCart} />}
        />
        <Route path="/product" element={<Product />} />
        <Route
          path="/categories"
          element={
            <Categories
              categories={categories}
              fetchCategoryById={fetchCategoryById}
            />
          }
        />
        <Route
          element={<CategoryProduct categoryProduct={categoryProduct} />}
        />
      </Routes>
      <Footer />
    </div>
  );
}