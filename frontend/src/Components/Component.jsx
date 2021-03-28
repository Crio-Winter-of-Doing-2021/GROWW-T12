import React from 'react';

function Component({id, image, title, displayText, button}) {
    return(
        <div id={id}>
            <div className='landing-page-image'>
                <img src={image} alt=''/>
            </div>
            <div className='landing-page-text'>
                <h2> {title} </h2>
                <p>{displayText}</p>
                <button>{button}</button>
            </div>
        </div>
    )
}
export default Component;