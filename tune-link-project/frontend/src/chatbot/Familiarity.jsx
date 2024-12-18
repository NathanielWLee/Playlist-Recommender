import React from 'react';
import "./Options.css";

const Familiarity = (props) => {
    const familiarity = [
        {
            text: "Yeah, put me on to something new.",
            handler: props.actionProvider.handleNewMusic,
            id: 1
        },
        {
            text: "A bit of both would be great.",
            handler: props.actionProvider.handleNewAndKnownMusic, 
            id: 2
        },
        {
            text: "No, only the songs I know.",
            handler: props.actionProvider.handleKnownMusic,
            id: 3
        }
    ];

    const buttonsMarkup = familiarity.map((f) => (
        <button key={f.id} onClick={f.handler} className="option-button">
            {f.text}
        </button>
    ));

    return <div className="options-container">{buttonsMarkup}</div>;
}

export default Familiarity;