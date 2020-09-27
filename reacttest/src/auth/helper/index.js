import { API } from '../../backend';
import { cartEmpty } from '../../core/helper/CartHelper';

export const customerSignup = (user) => {
	return fetch(`${API}user/customer/`, {
		method: 'POST',
		headers: {
			Accept: 'application/json', //This needs to be there
			'Content-Type': 'application/json',
		},
		body: JSON.stringify(user),
	})
		.then((response) => {
			//If response if coming up then pass json response back
			return response.json();
		})
		.catch((err) => console.log(err));
};

export const customerSignin = (user) => {
	const formData = new FormData(); //We have to use this, since in login page it accepts form data
	//In formdata, name of field is to be passed. "The name of the field whose data is contained in value."(From Docs)
	for (const name in user) {
		//Basically this "name" is the field name of append
		formData.append(name, user[name]);
	}

	return fetch(`${API}user/customer/login/`, {
		method: 'POST',
		body: formData,
	})
		.then((response) => {
			return response.json();
		})
		.err((err) => console.log(err));
};

export const authenticate = (data, next) => {
	if (typeof window !== undefined) {
		//It's an idiomatic check to see if the script is being run in a web-page inside a web-browser or not.
		localStorage.setItem('jwt', JSON.stringify(data)); //Nothing to do with Json Web Token, but works in similar manner
		next();
	}
};

export const isAuthenticated = () => {
	if (typeof window == undefined) {
		return false;
	}
	if (localStorage.getItem('jwt')) {
		//TODO: Add more security in this
		//TODO: Compare this with session token from backend etc.
		return JSON.parse(localStorage.getItem('jwt'));
	} else {
		return false;
	}
};

export const customerSignout = (next) => {
	const userId = isAuthenticated() && isAuthenticated().user.id;

	if (typeof window !== undefined) {
        localStorage.removeItem("jwt");
        cartEmpty(() => {}); //Empty out cart
        //next();

        return fetch(`${API}user/customer/logout/`, {
            method: 'GET'
        })
        .then(response => {
            console.log("Signout success");
            next();
        })
        .catch(err => console.log(err))
    }
};
