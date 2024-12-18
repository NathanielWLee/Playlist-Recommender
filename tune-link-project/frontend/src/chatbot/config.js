import React from "react";
import { createChatBotMessage } from "react-chatbot-kit";
import Buttons from "./Buttons";
import Valence from "./Valence";
import Cheer from "./Cheer";
import Energy from "./Energy";
import Boost from "./Boost";
import Relaxation from "./Relaxation";
import Danceability from "./Danceability";
import Instrumentalness from "./Instrumentalness";
import Liveness from "./Liveness";
import Loudness from "./Loudness";
import Acoustic from "./Acoustic";
import Familiarity from "./Familiarity";
import { BluetoothSearchingSharp } from "@material-ui/icons";

const config = {
    botName: "Tune Link",
    initialMessages: [createChatBotMessage("Hi, do you want to create a Spotify playlist?")],
    widgets: [
        {
            widgetName: "buttons",
            // inject widget with props to get access to the actions; returns jsx
            widgetFunc: (props) => <Buttons {...props} />,
        },
        {
            widgetName: "valence",
            // inject widget with props to get access to the actions; returns jsx
            widgetFunc: (props) => <Valence {...props} />,
        },
        {
            widgetName: "cheer",
            widgetFunc: (props) => <Cheer {...props} />,
        },
        {
            widgetName: "energy",
            // inject widget with props to get access to the actions; returns jsx
            widgetFunc: (props) => <Energy {...props} />,
        },
        {
            widgetName: "boost",
            // inject widget with props to get access to the actions; returns jsx
            widgetFunc: (props) => <Boost {...props} />,
        },
        {
            widgetName: "relaxation",
            // inject widget with props to get access to the actions; returns jsx
            widgetFunc: (props) => <Relaxation {...props} />,
        },
        {
            widgetName: "danceability",
            // inject widget with props to get access to the actions; returns jsx
            widgetFunc: (props) => <Danceability {...props} />,
        },
        {
            widgetName: "instrumentalness",
            // inject widget with props to get access to the actions; returns jsx
            widgetFunc: (props) => <Instrumentalness {...props} />,
        },
        {
            widgetName: "liveness",
            // inject widget with props to get access to the actions; returns jsx
            widgetFunc: (props) => <Liveness {...props} />,
        },
        {
            widgetName: "loudness",
            // inject widget with props to get access to the actions; returns jsx
            widgetFunc: (props) => <Loudness {...props} />,
        },
        {
            widgetName: "acoustic",
            // inject widget with props to get access to the actions; returns jsx
            widgetFunc: (props) => <Acoustic {...props} />,
        },
        {
            widgetName: "familiarity",
            // inject widget with props to get access to the actions; returns jsx
            widgetFunc: (props) => <Familiarity {...props} />,
        },
    ],
};

export default config;