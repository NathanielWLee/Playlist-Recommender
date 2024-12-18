import React from 'react';
import "./Options.css";

const Danceability = (props) => {
    const danceability = [
        {
            text: "Yes I want to dance!",
            handler: props.actionProvider.handleYesDance,
            id: 1
        },
        {
            text: "Eh, try me.",
            handler: props.actionProvider.handleMaybeDance, 
            id: 2
        },
        {
            text: "Not really.",
            handler: props.actionProvider.handleNoDance,
            id: 3
        }
    ];

    const buttonsMarkup = danceability.map((d) => (
        <button key={d.id} onClick={d.handler} className="option-button">
            {d.text}
        </button>
    ));

    return <div className="options-container">{buttonsMarkup}</div>;
}

export default Danceability;