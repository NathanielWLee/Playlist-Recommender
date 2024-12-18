import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";
import LoginPage from "./LoginPage";
import SongsPage from "./SongsPage";

export class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        // return <h1>Natalie</h1>;
        return (
            <div className="center">
                <HomePage />
            </div>
        );
    }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);
