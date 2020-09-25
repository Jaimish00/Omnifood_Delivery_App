import React from 'react'

const def_img = `https://images.pexels.com/photos/616404/pexels-photo-616404.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260`;

const ImageHelper = ({food}) => {
    const imageurl = food ? food.image : def_img
    return ( 
        //TODO: Add the card styles instead of bootstrap cards
        <div className="rounded border border-success p-2">
            <img src={imageurl} 
            style={{maxHeight:"100%", maxWidth: "100%"}}
            className="mb-3 rounded"
            alt=""/>
        </div>
    )
}


export default ImageHelper