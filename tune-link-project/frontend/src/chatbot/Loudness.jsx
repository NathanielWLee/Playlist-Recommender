import React from 'react';
import "./Options.css";

const Loudness = (props) => {
    const loudness = [
        {
            text: "Bring it on!",
            handler: props.actionProvider.handleYesLoud,
            id: 1
        },
        {
            text: "Kind of.",
            handler: props.actionProvider.handleKindOfLoud, 
            id: 2
        },
        {
            text: "Not really.",
            handler: props.actionProvider.handleNotLoud,
            id: 3
        }
    ];

    const buttonsMarkup = loudness.map((l) => (
        <button key={l.id} onClick={l.handler} className="option-button">
            {l.text}
        </button>
    ));

    return <div className="options-container">{buttonsMarkup}</div>;
}

export default Loudness;