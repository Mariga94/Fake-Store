import React from "react";
import ShopItem from "./ShopItem";

export default function Shop(props) {
  const sofas = props.sofas;
  const add = props.add
  const display = props.display

  const sofaElements = sofas.map((sofa) => (
    <ShopItem
      key={sofa.id}
      id={sofa.id}
      image={sofa.image}
      desc={sofa.description}
      price={sofa.price}
      addtocart={add}
      display={display}
    />
  ));

  return <div className="shop--container">{sofaElements}</div>;
}
