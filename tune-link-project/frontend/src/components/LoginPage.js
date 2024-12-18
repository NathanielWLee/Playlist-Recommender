import React, { Component } from 'react';
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import { Link } from "react-router-dom";
import { LocationSearching } from '@material-ui/icons';
// import '.../static/css/index.css';

export default class LoginPage extends Component {

  // static defaultProps = {
  //   tempVar: true
  // };

  constructor(props) {
    super(props);
    this.state = {
      tempVar: true,
      spotifyAuthenticated: false
    };
    this.handleAuthenticateButtonPressed = this.handleAuthenticateButtonPressed.bind(this);
    this.authenticateSpotify = this.authenticateSpotify.bind(this);
  }

  handleAuthenticateButtonPressed() {
    console.log(this.state);
    // const requestOptions = {
    //   method: "POST",
    //   headers: {"Content-Type": "application/json"},
    //   body: JSON.stringify({
    //     temp_var: this.state.tempVar
    //   }),
    // };
    // fetch("/api/create-room", requestOptions).then((response) => response.json()).then((data) => console.log(data));
    // if (!this.state.spotifyAuthenticated) {
    this.authenticateSpotify();
    console.log(this.state);
    // }
  }

  authenticateSpotify() { // send request
    fetch("/spotify/is-authenticated").then((response) => response.json()).then((data) => {this.setState({ spotifyAuthenticated: data.status })
        if (!data.status) {
          fetch('/spotify/get-auth-url').then((response) => response.json()).then((data) => {window.location.replace(data.url);});
        }
      });
  }

  render() {
    return (
      <Grid container spacing={1}>
        <Grid item xs={12} align="center">
          <Typography component="h2" variant="h2">
            Welcome to Tune Link!
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <Button style={{backgroundColor:"#1db954", color:"black"}} variant="contained" onClick={this.handleAuthenticateButtonPressed}>
            Sign In
          </Button>
        </Grid>
        <Grid item xs={12} align="center">
          <Button style={{backgroundColor:"black", color:"#1db954"}} variant="contained" href="http://127.0.0.1:8000/">
              Continue without signing in
            </Button>
          </Grid>
      </Grid>
    );
  }
}
