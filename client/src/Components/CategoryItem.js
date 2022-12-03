import React from 'react'

export default function CategoryItem(props) {
    const {id, name, image} = props
    return(
        <div className='category' id={id}>
            <h3>{name}</h3>
        </div>
    )
}

