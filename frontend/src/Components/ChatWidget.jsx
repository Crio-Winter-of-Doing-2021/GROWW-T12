import React, {useRef, useEffect, useContext} from 'react';
import Widget from 'rasa-webchat';
import BotPayloadContext from '../BotPayloadContext';

const CustomWidget = () => {
  const {value,setValue} = useContext(BotPayloadContext) ;
  // const value = 'ipo';
  const webchatRef = useRef(null);
  // useEffect(() => {
  //   if (value !== '') {
  //     callback();
  //   }}
  // );
  callback();
  function callback() {
    if (webchatRef.current && webchatRef.current.sendMessage) {
      webchatRef.current.sendMessage(value);
    }
  }
  return (
    <Widget
      initPayload={value}
      socketUrl={"http://localhost:5005"}
      socketPath={"/socket.io/"}
      customData={{"language": "en"}} // arbitrary custom data. Stay minimal as this will be added to the socket
      title={"GROWW"}
      showFullScreenButton={"true"}
      ref={webchatRef}
    />
  )
}

export default CustomWidget;
