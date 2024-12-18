import React, { Component } from 'react';
import LoginPage from './LoginPage';
import CreatePlaylistPage from './CreatePlaylistPage';
import SongsPage from './SongsPage';
import { BrowserRouter as Router, Routes, Route, Link, Redirect } from "react-router-dom";
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
// import './index.css';
// import { Link } from "react-router-dom";

import Chatbot from 'react-chatbot-kit';
import 'react-chatbot-kit/build/main.css';


// import './index.scss';
import config from "../chatbot/config";
import ActionProvider from "../chatbot/ActionProvider";
import MessageParser from "../chatbot/MessageParser";


export default class HomePage extends Component {
    constructor(props) {
        super(props);
        this.popupFunction = this.popupFunction.bind(this);
        this.showPage = this.showPage.bind(this);
        var delay;
    }

    handleButtonPressed() {
        // const requestOptions = {
        //     method: "PUT",
        //     headers: { "Content-Type": "application/json" },
        //   };
        fetch("/spotify/create-playlist");//.then((response) => response.json()).then((data) => console.log(data));
    }

    render() {
        return (
            <Router>
                <Routes>
                    <Route exact path='/' element={<div><Chatbot 
                        config={config}
                        actionProvider={ActionProvider}
                        messageParser={MessageParser}
                        />
                        {/* <div id="loader" onLoad={this.showPage} style={{display:"none"}}></div> */}
                        <Grid item xs={12} align="center">
                            {/* <Button style={{backgroundColor:"black", color:"#1db954"}} variant="contained" onclick="popupFunction()" href="javascript:setTimeout(()=>{window.location = 'http://127.0.0.1:8000/songs'},200);"> */}
                            <Button style={{backgroundColor:"black", color:"#1db954"}} variant="contained" href="http://127.0.0.1:8000/create" >    
                                Go to playlist
                            </Button>
                        </Grid>
                        {/* <p>please wait</p> */}
                            {/* <Grid container spacing={1}>
                                <Grid item xs={12} align="center">
                                    <Button color="primary" variant="contained" onClick={this.handleButtonPressed}>
                                        Create Playlist
                                    </Button>
                                </Grid>
                            </Grid> */}
                        </div>} />
                    <Route path='/login' element={<LoginPage/>} />
                    <Route path='/create' element={<CreatePlaylistPage/>} />
                    <Route path='/songs' element={<SongsPage/>} />
                    
                </Routes>
                
            </Router>
            
        );
    }

    popupFunction(){
        document.getElementById("loader").style.display = "block";
        console.log("pop up!!")
        this.loading();
        let now = Date.now(),
        end = now + 3000;
        while (now < end) { now = Date.now(); }
        this.showPage();

        // console.log("after");

        // setTimeout(()=>{window.location = 'http://127.0.0.1:8000/songs'},200);

        // this.delay = setTimeout(this.showPage(), 3000);
        // this.showPage();
    }

    loading(){
        console.log("loading!")
    }

    showPage(){
        console.log("show page!")
        // // var delay = setTimeout(this.popupFunction(), 3000);
        // let now = Date.now(),
        // end = now + 3000;
        // while (now < end) { now = Date.now(); }
        // console.log("after");
        // wait(3000);
        // this.popupFunction();
    }
}
