// category item component
import React from "react";

export default function CategoryItem(props) {
    const { id, name, description, fetchCategoryById } = props;

  return (
    <div className="category" id={id} onClick={() => fetchCategoryById(id, name)}>
      <h3>{name}</h3>
      <p>{description}</p>
    </div>
  );
}
