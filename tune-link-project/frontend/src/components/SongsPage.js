import React, { Component } from 'react';
import songjson from "../../../songs.js";
import "./Pages.css";
// import {ScrollView} from 'react-native';
// import GetSongs from "./songs.js";
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
// import Typography from "@material-ui/core/Typography";
// import TextField from "@material-ui/core/TextField";
// import FormHelperText from "@material-ui/core/FormHelperText";
// import FormControl from "@material-ui/core/FormControl";
// import { Link } from "react-router-dom";
// import Radio from "@material-ui/core/Radio";
// import RadioGroup from "@material-ui/core/RadioGroup";
// import FormControlLabel from "@material-ui/core/FormControlLabel";

export default class SongsPage extends Component {

  // constructor(props) {
  //   super(props);
  //   this.songs = "original value"
  //   this.getSongs = this.getSongs.bind(this);

  //   // this.songs = this.getSongs.bind(this)

  // }

  render() {
    var songsList = JSON.parse(songjson);
    console.log(songsList);
    return (
      <div class="scroll-container">
        <h1 class="header">Songs to check out based on your preferences:</h1>
          <ul>
            {songsList.map((item) => (
              <div class="item">
                <img class="image" src={item.image} alt={item.song} width="150" height="150"/> 
                <div class="info">
                  <h1><a class="spotify" href={item.songlink}>{item.song}</a></h1>
                  <h2>{item.artist}</h2>
                </div>
              </div>
            ))}
            <br />
          </ul>
          <Grid item xs={12} align="center">
              <Button style={{backgroundColor:"#1db954", color:"black"}} variant="contained" href="http://127.0.0.1:8000/" >    
                  Create new Playlist
              </Button>
          </Grid>
          <Grid style={{position:"relative", top:"10px"}} item xs={12} align="center">
              <Button style={{backgroundColor:"black", color:"#1db954"}} variant="contained" href="http://127.0.0.1:8000/login" >    
                  Home
              </Button>
          </Grid>
      </div>
    );
  }
}