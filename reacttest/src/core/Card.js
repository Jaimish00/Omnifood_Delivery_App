import React from 'react';
import ImageHelper from './helper/ImageHelper';
import { Redirect } from 'react-router-dom';
import { addItemToCart, removeItemFromCart } from './helper/CartHelper';

//TODO:
const isAuthenticated = true;

const Card = ({ foodItem, add = true, remove = true }) => {
  const cardTitle = foodItem ? foodItem.name : "A Great Food item";
  const cardDecription = foodItem
    ? foodItem.description
    : "From one of the states of India";
  const cardPrice = foodItem ? foodItem.price : "100RS.";

  const addToCart = () => {
    if (isAuthenticated) {
      addItemToCart(foodItem, () => {})
      console.log('Added to cart');
    } else {
      console.log('Login first');
    }
  };

  const removeFromCart = (foodId) => {
    console.log(foodItem);
    removeItemFromCart(foodId);
    console.log("Removed from cart");
  };

  const getAredirect = (redirect) => {
    if (redirect) {
      return <Redirect to='/cart' />;
    }
  };

  const showAddToCart = add => {
    return (
      add && (
        <button
          onClick={addToCart}
          className='btn btn-block btn-outline-success mt-2 mb-2'
        >
          Add to Cart
        </button>
      )
    );
  };

  const showRemoveFromCart = remove => {
    return (
      remove && (
        <button
          onClick={() => {
            removeFromCart(foodItem.id);
          }}
          className='btn btn-block btn-outline-danger mt-2 mb-2'
        >
          Remove from cart
        </button>
      )
    );
  };

  return (
    <div className='card text-white bg-dark border border-info ' style={{width: "15rem"}}>
      <div className='card-header lead'>{cardTitle}</div>
      <div className='card-body'>
        <ImageHelper foodItem={foodItem} />
        <p className='lead bg-success font-weight-normal text-wrap'>
          {cardDecription}
        </p>
        <p className='btn btn-success rounded  btn-sm px-4'>{cardPrice}</p>
        <div className='row'>
          <div className='col-12'>{showAddToCart(add)}</div>
          <div className='col-12'>{showRemoveFromCart(remove)}</div>
        </div>
      </div>
    </div>
  );
};

export default Card;
