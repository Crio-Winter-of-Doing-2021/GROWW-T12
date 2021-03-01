import React from 'react';
import Header from './Components/Header';
import Stocks from './Components/Stocks';
import MutualFunds from './Components/MutualFunds';
import Footer from './Components/Footer';
import stockimage from './images/stocks.png';
import mutualfundsimage from './images/mutualfunds.png';


function App() {
  return (
    <div className="App">
      <Header/>
      <Stocks image={stockimage} title='Stock' button='Explore Stocks'/>
      <MutualFunds image={mutualfundsimage} title='Mutual Funds' button='Explore Mutual Funds'/>
      <Footer/>
    </div>
  );
}

export default App;
