import React from 'react';
import "./Options.css";

const Cheer = (props) => {
    const cheer = [
        {
            text: "Yes",
            handler: props.actionProvider.handleYesCheerUp,
            id: 1
        },
        {
            text: "No",
            handler: props.actionProvider.handleNoCheerUp, 
            id: 2
        },
    ];

    const buttonsMarkup = cheer.map((c) => (
        <button key={c.id} onClick={c.handler} className="option-button">
            {c.text}
        </button>
    ));

    return <div className="options-container">{buttonsMarkup}</div>;
}

export default Cheer;