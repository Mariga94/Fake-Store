import React from "react";
import CartItem from "./CartItem";

export default function Cart(props) {
  const cartItems = props.cart;
  const cartElements = cartItems.map((cartItem) => (
    <CartItem
      key={cartItem.id}
      name={cartItem.name}
      image={cartItem.image}
      price={cartItem.price}
    />
  ));

  return (
    <div className="cart">
      <h4>Shopping Cart</h4>
      {cartElements.length === 0 && (
        <div className="empty--cart">
          <h3> Your Cart is Empty</h3>
          <a href="/shop">Back to Shop</a>
        </div>
      )}
    </div>
  );
}
