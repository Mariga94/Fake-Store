// category item component
import React from "react";
import { useParams } from "react-router-dom";
export default function CategoryItem(props) {
    const {category_id} = useParams()
    const { id, name, description, fetchCategoryById } = props;

  return (
    <div className="category" id={id} onClick={() => fetchCategoryById(id)}>
      <h3>{name}</h3>
      <p>{description}</p>
    </div>
  );
}
