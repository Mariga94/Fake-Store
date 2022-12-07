// Navbar component
import React from "react";

export default function Navbar(props) {
  return (
    <div>
      <nav className="navbar">
        <a href="/" className="logo">
          Furnish
        </a>
        <div className="links">
          <a href="/categories">Categories</a>
          <a href="/products">Products</a>
          <a href="/cart">Cart {props.len > 0 ? `(${props.len})` : ""}</a>
        </div>
      </nav>
    </div>
  );
}
