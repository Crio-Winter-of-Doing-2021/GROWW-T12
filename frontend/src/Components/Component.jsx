import React, {useContext} from 'react';
import BotPayloadContext from '../BotPayloadContext';

function Component({id, image, title, displayText, button, componentPayload}) {
    const {value,setValue} = useContext(BotPayloadContext);


    return(
        <div id={id}>
            <div className='landing-page-image'>
                <img src={image} alt=''/>
            </div>
            <div className='landing-page-text'>
                <h2> {title} </h2>
                <p>{displayText}</p>
                <button onClick={() => setValue(componentPayload)}>{button}</button>
                {/* <h1>{value}</h1> */}
            </div>
        </div>
    )
}
export default Component;