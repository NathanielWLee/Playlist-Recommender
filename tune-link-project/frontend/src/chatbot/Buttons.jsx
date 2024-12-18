import React from 'react';
// import actionProvider from './ActionProvider';
import "./Options.css";

const Buttons = (props) => {
    // ap = new ActionProvider;
    // lexResponse = ap.ActionProvider.getLexResponse()
    // console.log("buttons: ", lexResponse)
    // console.log("button: ", lexResponse.buttons[0].text)
    var lexInfo;
      $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/test",
        async: false,
        success: function (result) {
          lexInfo = result
        },
      });
      const buttons = []
      for(var i = 0; i < lexInfo.buttons.length; i++){
          buttons[i] = {
              text: lexInfo.buttons[i].text,
              handler: props.actionProvider.handleAnswer,
            //   handler: props.actionProvider.handleAnswer,
              id: i
          }
      }
    // const buttons = [
    //     {
    //         text: lexInfo.buttons[0].text,
    //         handler: props.actionProvider.handleYesDance,
    //         id: 1
    //     },
    //     {
    //         text: "test 2", //lexResponse.buttons[1].text,
    //         handler: props.actionProvider.handleMaybeDance, 
    //         id: 2
    //     },
    //     {
    //         text: "Not really.",
    //         handler: props.actionProvider.handleNoDance,
    //         id: 3
    //     }
    // ];

    const buttonsMarkup = buttons.map((d) => (
        // <div>
        //     <button key={d.id} onClick={"buttonHandler()"} className="option-button">
        //         {d.text}
        //     </button>
        //     <script>
        //         function buttonHandler(){
        //             // console.log("testing button handler method: ", d.text)
        //         }
        //     </script>
        // </div>
        <button key={d.id} onClick={d.handler} className="option-button">
            {d.text}
        </button>
    ));

    return <div className="options-container">{buttonsMarkup}</div>;
}

export default Buttons;