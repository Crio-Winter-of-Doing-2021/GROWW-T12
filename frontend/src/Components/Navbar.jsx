import React, {useState, useContext} from 'react';
import logo from '../images/cwodGrowwLogo.png';
import BotPayloadContext from '../BotPayloadContext';
function Navbar() {
    const {value,setValue} = useContext(BotPayloadContext);
    
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
                <li><button onClick= {() => setValue("stocks")}><a href='#stocks'>Stocks</a></button></li>
                <li><button onClick= {() => setValue("mutual funds")}><a href='#mutual-funds'>Mutual Funds</a></button></li>
                <li><button onClick= {() => setValue("fds")}><a href='#fds'>Fixed Deposits</a></button></li>
                <li><button onClick= {() => setValue("Gold")}><a href='#gold'>Gold</a></button></li>
                <li><button onClick= {() => setValue("US stocks")}><a href='#us-stocks'>US Stocks</a></button></li>
                <li><button onClick= {() => setValue("update database")}><a href=''>UPDATE DATABASE</a></button></li>
            </ul>
        </nav>
    )
}
export default Navbar;