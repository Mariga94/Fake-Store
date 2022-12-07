import React from "react";
import ShopItem from "./ShopItem";

export default function Product(props) {
  const product = props.product;
  const add = props.add;
  return (
    <div className="product--page">
      <ShopItem
        key={product.id}
        id={product.id}
        image={product.image}
        desc={product.description}
        price={product.price}
        addtocart={add}
      />
    </div>
  );
}
