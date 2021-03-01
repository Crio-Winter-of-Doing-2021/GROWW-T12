import React, {useState} from 'react';
import logo from '../images/cwodGrowwLogo.png';
function Navbar() {

    const [nav,setnav] = useState(false);
    const changeBackground = () => {
        if(window.scrollY >= 50){
            setnav(true);
        }
        else{
            setnav(false);
        }
    }
    window.addEventListener('scroll',changeBackground);
    return(
        <nav className={nav ? 'nav active':'nav'}>
            <a href='#' className='logo'>
                <img src={logo} alt=''/>    
            </a> 
            <ul className='menu'>
                <li><a href='#stocks'>Stocks</a></li>
                <li><a href='#mutual-funds'>Mutual Funds</a></li>
                <li><a href='#'>Fixed Deposits</a></li>
                <li><a href='#'>Gold</a></li>
                <li><a href='#'>US Stocks</a></li>
            </ul>
        </nav>
    )
}
export default Navbar;