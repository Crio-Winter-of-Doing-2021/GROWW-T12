import Widget from 'rasa-webchat';

const CustomWidget = () => {
  return (
    <Widget
      initPayload={"/greet"}
      socketUrl={"http://localhost:5005"}
      socketPath={"/socket.io/"}
      customData={{"language": "en"}} // arbitrary custom data. Stay minimal as this will be added to the socket
      title={"GROWW"}
    />
  )
}

export default CustomWidget;
