// categories component
import React from "react";
import CategoryItem from "./CategoryItem";

export default function Categories(props) {
  const categories = props.categories;
  const fetchCategoryById = props.fetchCategoryById;
  const mapCategories = categories.map((item) => (
    <CategoryItem
      key={item.id}
      id={item.id}
      name={item.name}
      image={item.image}
      description={item.description}
      fetchCategoryById={fetchCategoryById}
    />
  ));
  return (
    <div className="container">
      <h2>Categories</h2>
      <div className="category--container">{mapCategories}</div>
    </div>
  );
}
