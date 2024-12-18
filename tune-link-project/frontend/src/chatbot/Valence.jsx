import React from 'react';
import "./Options.css";

const Valence = (props) => {
    const valence = [
        {
            text: "I'm feeling great! :)",
            handler: props.actionProvider.handleGreatValence,
            id: 1
        },
        {
            text: "I'm okay. :/",
            handler: props.actionProvider.handleOkayValence, 
            id: 2
        },
        {
            text: "I've been better. :(",
            handler: props.actionProvider.handleBeenBetterValence,
            id: 3
        }
    ];

    const buttonsMarkup = valence.map((v) => (
        <button key={v.id} onClick={v.handler} className="option-button">
            {v.text}
        </button>
    ));

    return <div className="options-container">{buttonsMarkup}</div>;
}

export default Valence;