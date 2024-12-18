import React from 'react';
import "./Options.css";

const Boost = (props) => {
    const boost = [
        {
            text: "Yes",
            handler: props.actionProvider.handleYesEnergyBoost,
            id: 1
        },
        {
            text: "No",
            handler: props.actionProvider.handleNoEnergyBoost, 
            id: 2
        },
    ];

    const buttonsMarkup = boost.map((b) => (
        <button key={b.id} onClick={b.handler} className="option-button">
            {b.text}
        </button>
    ));

    return <div className="options-container">{buttonsMarkup}</div>;
}

export default Boost;