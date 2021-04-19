import React, { useState, useMemo } from 'react';

import Header from './Components/Header';
import Component from './Components/Component';
import Footer from './Components/Footer';

import stockImage from './images/stocks.png';
import mutualFundsImage from './images/mutualfunds.png';
import fdImage from './images/FDs.png';
import goldImage from './images/gold.png';
import usStocksImage from './images/usstocks.png';

import BotPayloadContext from './BotPayloadContext';
import UserContext from './UserContext';

import Chatbot from './Components/ChatWidget';

import Routes from "./Routes";

function App() {
  const [value, setValue] = useState("/greet");
  const providerValue = useMemo(() => ({ value, setValue }), [value, setValue]);
  const [isAdmin, setIsAdmin] = useState(false);
  const initialValue = useMemo(() => ({ isAdmin, setIsAdmin }), [isAdmin, setIsAdmin]);

  return (
    <BotPayloadContext.Provider value={providerValue}>
      <div className="App">
        <UserContext.Provider value={initialValue}>
          <Header />
          {/* <Component id='stocks' image={stockImage} title='Stocks'
          displayText='You don’t have to pay a single rupee for opening a stocks account or account maintenance.'
          button='Explore Stocks' componentPayload='/query_stocks' />
        <Component id='mutual-funds' image={mutualFundsImage} title='Mutual Funds'
          displayText='Select from 5000+ direct mutual funds and get higher return than regular funds.'
          button='Explore Mutual Funds' componentPayload='/query_mutual_funds' />
        <Component id='fixed-deposits' image={fdImage} title='Fixed Deposits'
          displayText='Open fixed deposits in any bank with higher interest rates without opening a bank account.'
          button='Explore FDs' componentPayload='' />
        <Component id='gold' image={goldImage} title='Gold'
          displayText='Invest in digital gold as low as ₹10 without any extra commission or making charges.'
          button='Explore Gold' componentPayload='' />
        <Component id='us-stocks' image={usStocksImage} title='US Stocks'
          displayText='Invest in Apple, Google, Netflix and many more US companies that you love without any brokerage fee.'
          button='Explore US Stocks' componentPayload='' /> */}
          <Routes />
          <Footer />
          <Chatbot />
        </UserContext.Provider>
      </div>
    </BotPayloadContext.Provider>
  );
}

export default App;
