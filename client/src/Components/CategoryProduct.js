import React from "react";
import ShopItem from "./ShopItem";

export default function CategoryProduct(props) {
    const items = props.categoryProduct
    console.log(items)
    const elements = items.map((item) => (
        <ShopItem
          key={item.id}
          id={item.id}
          image={item.image}
          desc={item.description}
          price={item.price}
        />
      ));
  return <div className="shop--container">{elements ? elements:<h2>Loading...</h2>}</div>;
}
