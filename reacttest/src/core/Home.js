import React, {useState, useEffect} from 'react'
import Base from './Base';
import { getFood } from './helper/coreapicalls'
import "../styles.css"

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
    }

    useEffect(() => {
        loadAllFood();
    }, []);

    return (
        <Base title="Omnifood" description="Top dishes across the India">
            <h1>Home Component</h1>
            <div classNameName="row">
                {food.map(
                    (food_item, index) => {
                        return(
                            <div key={index}>
                                <h1>{food_item.name}</h1>
                            </div>
                        )
                    }
                )}
            </div>
        </Base>
    )
}


/*

*/


/*
<section className="section-features js--section-features" id="features">
			<div className="row1">
			<div className="column">
				<div className="card">
					<img src="./img/Chhole.jpg" alt="Chhole"/>
					<div className="con-text">
						<h2>Chhole Bhature</h2>
						<p> <br /> 55 Rs. <br /> Dvar Indian Restaurant
							<button>Add Cart</button>
						</p>
					</div>
				</div>
			</div>

			<div className="column">
				<div className="card">
					<img src="./img/Vadapav.jpg" alt="Vadapav"/>
					<div className="con-text">
						<h2>Vada Pav</h2>
						<p> <br /> 55 Rs. <br /> Dvar Indian Restaurant
							<button>Add Cart</button>
						</p>
					</div>
				</div>
			</div>

			<div className="column">
				<div className="card">
					<img src="./img/Ghari.jpg" alt="Ghari"/>
					<div className="con-text">
						<h2>Ghari</h2>
						<p> <br /> 55 Rs. <br /> Dvar Indian Restaurant
							<button>See more</button>
						</p>
					</div>
				</div>
			</div>
			</div>
		</section>

		<section className="section-steps" id="steps">
			<div className="row">
				<h3>About us</h3>
				<div className="col span-1-of-2 steps-box">
					<div className="works-step">
						<div>1</div>
						<p>Choose the subscription plan that best fits your needs and sign up today.</p>
					</div>
					<div className="works-step">
						<div>2</div>
						<p>Order your delicious meal using our mobile app or website. Or you can even call us!</p>
					</div>
					<div className="works-step">
						<div>3</div>
						<p>Enjoy your meal after less than 20 minutes. See you the next time!</p>
					</div>
				</div>
			</div>
		</section>

		<section className="section-cities" id="cities">
			<div className="row">
				<h3>We're currently in these cities</h3>
			</div>
			<div className="row1">
			</div>
			<div className="column">
				<div className="card1">
					<img src="./img/surat.jpg" alt="Paris"/>
					<div className="con-text">
						<h2>SURAT</h2>
						<p> Surat is a district in the state of Gujarat India with Surat city as the administrative
							headquarters of this district. It is the second-most advanced district in Gujarat. It is
							known as Diamond City.
						</p>
					</div>
				</div>
			</div>

			<div className="column">
				<div className="card1">
					<img src="./img/bombay.jpg" alt="Paris"/>
					<div className="con-text">
						<h2>BOMBAY</h2>
						<p> The Bombay is a shorthair breed of domestic cat, closely related to the Burmese.The
							close-lying, sleek and glossy black coat is generally coloured to the roots, with little or
							no paling. Capital Of Maharashtra.
						</p>
					</div>
				</div>
			</div>

			<div className="column">
				<div className="card1">
					<img src="./img/banglore.jpg" alt="Paris"/>
					<div className="con-text">
						<h2>BANGLORE</h2>
						<p> Bangalore officially known as Bengaluru is the capital of the Indian state of Karnataka. It
							has a population of more than 8 million population of around 11 million, fifth most populous
							urban agglomeration in India.
						</p>
					</div>
				</div>
			</div>

			<div className="row1">
			</div>
			<div className="column">
				<div className="card1">
					<img src="./img/amd.jpg" alt="Paris"/>
					<div className="con-text">
						<h2>AHEMDABAD</h2>
						<p> Ahmedabad is the largest city in the state of Gujarat. It is located in western India on the
							banks of the River Sabarmati. The city served as political as well as economical capital of
							the region since its establishment.
						</p>
					</div>
				</div>
			</div>

			<div className="column">
				<div className="card1">
					<img src="./img/delhi.jpg" alt="Paris"/>
					<div className="con-text">
						<h2>DELHI</h2>
						<p> Delhi is a territory in India. It includes the country's capital New Delhi. It covers an
							area of 573 square miles. Delhi is a part of the National Capital Region, which has 12.5
							million residents. </p>
					</div>
				</div>
			</div>

			<div className="column">
				<div className="card1">
					<img src="./img/jaipur.jpg" alt="Paris"/>
					<div className="con-text">
						<h2>JAIPUR</h2>
						<p> Jaipur is the present-day capital of the state of Rajasthan, and until 1949 the City Palace
							was the ceremonial and administrative seat of the Maharaja of Jaipur. The Palace was also
							the cultural events.
						</p>
					</div>
				</div>
			</div>

			<div className="row1">
			</div>
			<div className="column">
				<div className="card1">
					<img src="./img/hyedrabad.jpg" alt="Paris"/>
					<div className="con-text">
						<h2>HYEDRABAD</h2>
						<p> Hyderabad is the capital of the Indian state of Telangana. It is a historic city noted for
							its many monuments, temples, mosques and bazaars. The city of Hyderabad was founded in 1591
							CE.
						</p>
					</div>
				</div>
			</div>

			<div className="column">
				<div className="card1">
					<img src="./img/pune.jpg" alt="Paris"/>
					<div className="con-text">
						<h2>PUNE</h2>
						<p> Pune is the 9th most populous city in India and the second-largest in the state of
							Maharashtra, after the state capital Mumbai.It is closely related to the rise of the Maratha
							empire from the 17thâ€“18th century.
						</p>
					</div>
				</div>
			</div>

			<div className="column">
				<div className="card1">
					<img src="./img/chennai.jpg" alt="Paris"/>
					<div className="con-text">
						<h2>CHENNAI</h2>
						<p> Chennai, Formerly known as Madras, is the capital of Tamil Nadu and is India's fifth largest
							city.With an estimated population of 8.9 million,the 31st largest metropolitan area in the
							world.
						</p>
					</div>
				</div>
			</div>
		</section>
*/