import React from 'react'

const def_img = "https://images.pexels.com/photos/616404/pexels-photo-616404.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260";

const ImageHelper = ({foodItem}) => { //Here destructuring of props is going on
    //Here props will be coming up instead of simply just food
    //So we are destructuring the array by doing {food} this.
    const imageurl = foodItem ? foodItem.image : def_img;
    //console.log(food.image);
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