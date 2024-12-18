import React from 'react';
import "./Options.css";

const Acoustic = (props) => {
    const acoustic = [
        {
            text: "I prefer music from instruments.",
            handler: props.actionProvider.handleAcousticMusic,
            id: 1
        },
        {
            text: "A bit of both.",
            handler: props.actionProvider.handleMixedMusic, 
            id: 2
        },
        {
            text: "I like electronic music!",
            handler: props.actionProvider.handleElectronicMusic,
            id: 3
        }
    ];

    const buttonsMarkup = acoustic.map((a) => (
        <button key={a.id} onClick={a.handler} className="option-button">
            {a.text}
        </button>
    ));

    return <div className="options-container">{buttonsMarkup}</div>;
}

export default Acoustic;