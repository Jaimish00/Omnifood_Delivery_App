import { API } from '../../backend';

export const getFood = () => {
  return fetch(`${API}food`, { 
      method: 'GET',
    })
    .then((response) => {
      return response.json();
    })
    .catch((err) => console.log(err));
};
