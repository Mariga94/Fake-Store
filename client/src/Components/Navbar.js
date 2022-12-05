import React from "react";


export default function Navbar(props) {
  return (
    <div>
      <nav className="navbar">
        <span className="logo">Furnish</span>
        {/* <a href="home">Home</a> */}
        <a href="/products">Products</a>
        <a href="/cart">Cart {props.len > 0 ? `(${props.len})`: ""}</a>
      </nav>
    </div>
  );
}


