import React from 'react';
import Navbar from './Navbar';

function Header() {
    return(
        <div id='main'>
            <Navbar/>
            <div className='name'>
                <h1><span>Invest in </span>Stocks</h1>
                <p className='details'>Grow by investing with GROWW</p>
                <a href='#' className='getstart-btn'>Get Started</a>
            </div>
        </div>
    )
}
export default Header;