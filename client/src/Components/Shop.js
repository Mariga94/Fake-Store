// shop component
import React from "react";
import ShopItem from "./ShopItem";

export default function Shop(props) {
  const products = props.products;
  const add = props.add;
  const display = props.display;

  const sofaElements = products.map((product) => (
    <ShopItem
      key={product.id}
      id={product.id}
      image={product.image}
      desc={product.description}
      price={product.price}
      addtocart={add}
      display={display}
    />
  ));

  return (
    <div>
      <div id="snackbar"></div>
      <div className="shop--container">{sofaElements}</div>
    </div>
  );
}
