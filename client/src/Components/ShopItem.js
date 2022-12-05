import React from "react";


export default function shopItem(props) {
  const { image, desc, price, id } = props;
  const addToCart = props.addtocart;
  return (
    <div className="shop--item" id={id}>
      <img src={image} alt={desc} />
      <p>{desc}</p>
      <span className="price">$ {price}</span>
      <button onClick={() => addToCart(id)}>Add to Cart</button>
    </div>
  );
}
