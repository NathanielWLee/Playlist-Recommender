import React from 'react';
import "./Options.css";

const Energy = (props) => {
    const energy = [
        {
            text: "Energized!",
            handler: props.actionProvider.handleEnergizedEnergy,
            id: 1
        },
        {
            text: "Slowly waking myself up.",
            handler: props.actionProvider.handleStillWakingEnergy, 
            id: 2
        },
        {
            text: "Completely exhausted.",
            handler: props.actionProvider.handleExhaustedEnergy,
            id: 3
        }
    ];

    const buttonsMarkup = energy.map((e) => (
        <button key={e.id} onClick={e.handler} className="option-button">
            {e.text}
        </button>
    ));

    return <div className="options-container">{buttonsMarkup}</div>;
}

export default Energy;