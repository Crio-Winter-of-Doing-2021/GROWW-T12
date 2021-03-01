import React from 'react';

function Stocks(props) {
    return(
        <div id='stocks'>
            <div className='landing-page-image'>
                <img src={props.image} alt=''/>
            </div>
            <div className='landing-page-text'>
                <h2> {props.title} </h2>
                <p>You don’t have to pay a single rupee for opening a stocks account or account maintenance.</p>
                <button>{props.button}</button>
            </div>
        </div>
    )
}
export default Stocks;