import React from "react";

export default function CartItem(props) {
  const { image, price, name } = props;
  return (
    <div className="cart--item">
      <img src={image} alt="" />
      <div className="cart--detail">
        <p>{name}</p>
        <span>$ {price}</span>
      </div>
      <div className="qty">
          <button>-</button>
          <input type="number" />
          <button>+</button>
        </div>
      <h4>Total</h4>
    </div>
  );
}
