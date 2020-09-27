import React, {useState, useEffect} from 'react'
import Base from './Base';
import { getFood } from './helper/coreapicalls'
import "../styles.css"
import Card from './Card';

export default function Home() {

    const [food, setFood] = useState([]);
    const [error, setError] = useState(false);

    const loadAllFood = () => {
        getFood()
        .then(data => {
            if(data.error){
                setError(data.error);
                console.log(error);
            } else{
                setFood(data);
            }
        })
        .catch(err => console.log(err))
    };

    useEffect(() => {
        loadAllFood();
    }, []);

    return (
        <Base title="Omnifood" description="Top dishes across the India">
            <h1>Home Component</h1>
            <div className="row">
                {food.map(
                    (foodItem, index) => {
                        return(
                            <div key={index} className="col-4 mb-4">
                                <Card foodItem={foodItem}/>
                            </div>
                        )
                    }
                )}
            </div>
        </Base>
    );
}

