import React from 'react';
import "./Options.css";

const Relaxation = (props) => {
    const relaxation = [
        {
            text: "That would be nice.",
            handler: props.actionProvider.handleYesRelax,
            id: 1
        },
        {
            text: "Nah, I'm good.",
            handler: props.actionProvider.handleNoRelax, 
            id: 2
        },
    ];

    const buttonsMarkup = relaxation.map((r) => (
        <button key={r.id} onClick={r.handler} className="option-button">
            {r.text}
        </button>
    ));

    return <div className="options-container">{buttonsMarkup}</div>;
}

export default Relaxation;