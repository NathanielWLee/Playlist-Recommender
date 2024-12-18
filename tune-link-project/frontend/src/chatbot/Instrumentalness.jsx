import React from 'react';
import "./Options.css";

const Instrumentalness = (props) => {
    const instrumentalness = [
        {
            text: "Pass me the mic!",
            handler: props.actionProvider.handleYesSing,
            id: 1
        },
        {
            text: "I don't mind.",
            handler: props.actionProvider.handleMaybeSing, 
            id: 2
        },
        {
            text: "I just want to zone out.",
            handler: props.actionProvider.handleNoSing,
            id: 3
        }
    ];

    const buttonsMarkup = instrumentalness.map((i) => (
        <button key={i.id} onClick={i.handler} className="option-button">
            {i.text}
        </button>
    ));

    return <div className="options-container">{buttonsMarkup}</div>;
}

export default Instrumentalness;