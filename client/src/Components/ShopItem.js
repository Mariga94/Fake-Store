import React from "react";

export default function shopItem(props) {
  const { image, desc, price, id, display, } = props;
  const addToCart = props.addtocart;
  return (
    <div className="shop--item" id={id}>
      <img src={image} alt={desc} onClick={() => display(id)} />
      <h4>{desc}</h4>
      <span className="price">$ {price}</span>
      <button onClick={() => addToCart(id)}>Add to Cart</button>
    </div>
  );
}
