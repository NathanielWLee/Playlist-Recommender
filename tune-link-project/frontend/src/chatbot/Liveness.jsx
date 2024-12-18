import React from 'react';
import "./Options.css";

const Liveness = (props) => {
    const liveness = [
        {
            text: "Yes, I wish I could hear things live.",
            handler: props.actionProvider.handleYesLive,
            id: 1
        },
        {
            text: "It doesn't matter!",
            handler: props.actionProvider.handleMaybeLive, 
            id: 2
        },
        {
            text: "Not really.",
            handler: props.actionProvider.handleNoLive,
            id: 3
        }
    ];

    const buttonsMarkup = liveness.map((l) => (
        <button key={l.id} onClick={l.handler} className="option-button">
            {l.text}
        </button>
    ));

    return <div className="options-container">{buttonsMarkup}</div>;
}

export default Liveness;