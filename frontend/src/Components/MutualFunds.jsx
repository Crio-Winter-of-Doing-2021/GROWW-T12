import React from 'react';

function MutualFunds(props) {
    return(
        <div id='mutual-funds'>
            <div className='landing-page-image'>
                <img src={props.image} alt=''/>
            </div>
            <div className='landing-page-text'>
                <h2> {props.title} </h2>
                <p>Select from 5000+ direct mutual funds and get higher return than regular funds.</p>
                <button>{props.button}</button>
            </div>
        </div>
    )
}
export default MutualFunds;