import React from "react";

export default function CartItem(props) {
  const { image, price, name, deleted, cartId } = props;
  console.log(props);
  return (
    <div className="cart--item" id={cartId}>
      <img src={image} alt="" />
      <div className="cart--detail">
        <h3>{name}</h3>
        <h4>$ {parseFloat(price).toFixed(2)}</h4>
        {/* <div className="qty">
          <button>-</button>
          <input type="number" />
          <button>+</button>
        </div> */}
      </div>
      <div className="btn-div">
        <button className="remove" onClick={() => deleted(cartId)}>
          Remove
        </button>
      </div>
    </div>
  );
}
