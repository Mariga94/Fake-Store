import React from "react";
import axios from "axios";
import { Routes, Route, useNavigate } from "react-router-dom";
import Navbar from "./Navbar";
import Footer from "./Footer";
import Cart from "./Cart";
import Shop from "./Shop";
import Home from "./Home";
import Categories from "./Categories";
import CategoryProduct from "./CategoryProduct";
import About from "./About";
import Product from "./ProductItem";

// main app
export default function App() {
  const [categoryProduct, setCategoryProduct] = React.useState([]);
  const [products, setProducts] = React.useState([]);
  const [categories, setCategories] = React.useState([]);
  const [cart, setCart] = React.useState([]);
  const [product, setProduct] = React.useState();
  const navigate = useNavigate();

  // Navigation
  function navigateToCategoryProduct(category_id) {
    navigate(`/categories/${category_id}/products`);
  }

  function navigateToProduct(id) {
    navigate(`/products/${id}`)
  }

  // fetch one product based on product id
  const fetchProduct = (id) => {
    axios.get(`http://127.0.0.1:5000/api/v1/products/${id}`).then(
      (res) => {
        setProduct(res.data);
        navigateToProduct(id)
      },
      (error) => {
        console.log(error);
      }
    );
  };

  // fetch products from the REST API
  const fetchProducts = () => {
    axios.get("http://127.0.0.1:5000/api/v1/products").then(
      (res) => {
        setProducts(res.data);
      },
      (error) => {
        console.log(error);
      }
    );
  };

  // fetch categories from the REST API
  const fetchCategories = () => {
    axios.get("http://127.0.0.1:5000/api/v1/categories").then((res) => {
      setCategories(res.data);
    });
  };

  // fetch one category from the REST API
  const fetchCategoryById = (category_id) => {
    axios
      .get(`http://127.0.0.1:5000/api/v1/categories/${category_id}/product`)
      .then((res) => {
        const categoryProduct = res.data;
        setCategoryProduct(
          window.localStorage.setItem(
            "categoryProduct",
            JSON.stringify(categoryProduct)
          )
        );
        navigateToCategoryProduct(category_id);
      });
  };
  
  // fetch cart items from the database
  function fetchCart() {
    axios.get("http://127.0.0.1:5000/api/v1/cart").then(
      (res) => {
        setCart(res.data);
      },
      (error) => {
        console.log(error);
      }
    );
  }

  // add item to cart
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

  //delete item from cart
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


  return (
    <div>
      <Navbar len={cart.length} />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route
          path="/products"
          element={<Shop products={products} 
            add={AddToCart} 
            display={fetchProduct}/>}
        />
        <Route
          path="/cart"
          element={<Cart cart={cart} 
          deleted={deleteItemFromCart} />}
        />
        <Route path="/products/:id" 
          element={<Product product={product} 
          add={AddToCart} />}
           />
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
          path="categories/:id/products"
          element={<CategoryProduct 
            categoryProduct={categoryProduct} 
            add={AddToCart} />}
        />
      </Routes>
      <Footer />
    </div>
  );
}
