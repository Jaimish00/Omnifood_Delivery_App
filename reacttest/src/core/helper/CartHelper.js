export const addItemToCart = (item, next) => {
	let cart = [];
	if (typeof window !== undefined) {
		//Adding items that are already in the cart
		if (localStorage.getItem("cart")) {
			cart = JSON.parse(localStorage.getItem("cart"));
		}

		cart.push({
			...item,
		});

		localStorage.setItem('cart', JSON.stringify(cart));
		next(); //User can further chain other callback methods wih this
        //This is the javascript function
        //Like adding the item to cart, if user wants to redirect to some other pages like home
        //we can do that, or we can refresh the cart page using this callback method
	}
};


export const loadCart = () => {
    if(typeof window !== undefined){
        if(localStorage.getItem("cart")){
            return JSON.parse(localStorage.getItem("cart")) //Cart array
        }
    }
}

export const removeItemFromCart = (foodId) => {
    let cart = [];
    
    if(typeof window !== undefined){
        if(localStorage.getItem("cart")){
            cart = JSON.parse(localStorage.getItem("cart"))
        }
        console.log(foodId);    
        cart.map((foodItem, i) => { //Loop through all the items and their indices
            if(foodItem.id === foodId){ //food.id and food._id, both will work same for now
                //SQlite and MongoDB has updated this thing for the consistency, so better to use food._id here
                cart.splice(i, 1) //Remove one item from index i
            }
        })
        localStorage.setItem("cart", JSON.stringify(cart))
    }
    //No need of this
    return cart;
}

export const cartEmpty = (next) => {
    if (typeof window !== undefined){
        localStorage.removeItem("cart") //First remove the cart
        let cart = [] //The cart object needs to be there for the loadCart method
        localStorage.setItem("cart", JSON.stringify(cart))
        next();
    }
    
}

