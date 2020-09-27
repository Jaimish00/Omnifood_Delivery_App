import {API} from '../../backend'
import {cartEmpty} from '../../core/helper/CartHelper'

export const customerSignup = (user) => {
    return fetch(`${API}user/customer/`, {
        method: 'POST',
        headers: {
            Accept: 'application/json', //This needs to be there
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(user)
    })
    .then(response => { //If response if coming up then pass json response back
        return response.json()
    })
    .catch(err => console.log(err))
};

export const customerSignin = (user) => {
    const formData = new FormData() //We have to use this, since in login page it accepts form data
    //In formdata, name of field is to be passed. "The name of the field whose data is contained in value."(From Docs)
    for(const name in user){
        formData.append(name, user[name])
    }

    return fetch(`${API}user/customer/login/`, {
        method: 'POST',
        body: formData
    })
    .then(response => {
        return response.json()
    })
    .err(err => console.log(err))
};
