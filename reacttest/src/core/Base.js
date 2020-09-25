import React from 'react';

const Base = ({
  title = 'Default Title',
  description = 'Default Description',
  className = 'bg-dark text-white p-4',
  children,
}) => {
  return (
    <div>
     <div className='container-fluid'>
        <div className='jumbotron bg-dark text-white text-center'>
          <h2 className='display-4'>{title}</h2>
          <p className='lead'>{description}</p>
        </div>
        <div className={className}>{children}</div>
      </div>
      <footer className='footer bg-dark mt-auto py-3'>
        <div className='container-fluid bg-success text-white text-center py-3'>
          <h4>Have any Questions?</h4>
          <button className='btn btn-warning btn-lg'>Contact us</button>
          <div className='container'>
            <span className='text-warning'>Omnifood Delivery</span>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default Base;

/*

*/

/*
 <header className='Index-head'>
        <nav>
          <div className='row'>
            <img
              src='./img/logo.png'
              alt='Omnifood logo'
              className='logo'
            />
            <img
              src='./img/logo1.png'
              alt='Omnifood logo'
              className='logo-black'
            />
            <ul className='main-nav js--main-nav'>
              <li>
                <a href='#'>Log in</a>
              </li>
              <li>
                <a href='#'>Home</a>
              </li>
              <li>
                <a href='#'>Menu </a>
              </li>
              <li>
                <a href='#'>Cart</a>
              </li>
              <li>
                <a href='#'>Profile </a>
              </li>
            </ul>
          </div>
        </nav>
        <div className='hero-text-box'>
          <h1>OmniFood</h1>
          <a className='btn btn-full js--scroll-to-plans' href='#'>
            Log In{' '}
          </a>
          <a
            className='btn btn-ghost js--scroll-to-start'
            href='#'
          >
            Sign Up{' '}
          </a>
        </div>
      </header>
      <div>{children}</div>
      <footer>
        <div className='col span-1-of-2'>
          <ul className='right-nav'>
            <li>
              <a href='#'>
                <i className='icon ion-logo-facebook'></i>
              </a>
            </li>
            <li>
              <a href='#'>
                <i className='icon ion-logo-twitter'></i>
              </a>
            </li>
            <li>
              <a href='#'>
                <i className='icon ion-logo-googleplus'></i>
              </a>
            </li>
            <li>
              <a href='#'>
                <i className='icon ion-logo-instagram'></i>
              </a>
            </li>
          </ul>
        </div>

        <div className='row'>
          <p>Copyright &copy;,2020 by Omnifood. All rights reserved.</p>
        </div>
      
      </footer>
*/