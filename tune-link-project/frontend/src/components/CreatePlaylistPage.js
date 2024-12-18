import React, { Component } from 'react';
// import Button from "@material-ui/core/Button";
// import Grid from "@material-ui/core/Grid";
// import Typography from "@material-ui/core/Typography";
// import TextField from "@material-ui/core/TextField";
// import FormHelperText from "@material-ui/core/FormHelperText";
// import FormControl from "@material-ui/core/FormControl";
// import { Link } from "react-router-dom";
// import Radio from "@material-ui/core/Radio";
// import RadioGroup from "@material-ui/core/RadioGroup";
// import FormControlLabel from "@material-ui/core/FormControlLabel";

export default class CreatePlaylistPage extends Component {
  // defaultSongs = 20
  // defaultMood = "happy"

  constructor(props) {
    super(props);
    // this.state = {
    //   // addToMyPlaylists: true,
    //   // mood: this.defaultMood,
    //   // numSongs: this.defaultSongs,
    // };

    // this.handleNumSongsChange = this.handleNumSongsChange.bind(this);
    // this.handleMoodChange = this.handleMoodChange.bind(this);
    // this.handleCreatePlaylistButtonPressed = this.handleCreatePlaylistButtonPressed.bind(this);
  }

  // Takes object (e.g. text field) which calls this function and obtains the value of the object 
  // handleNumSongsChange(e) {
  //   this.setState({
  //     numSongs: e.target.value,
  //   });
  // }

  // handleMoodChange(e) {
  //   this.setState({
  //     mood: e.target.value === "1" ? "happy" : "angry"
  //   });
  // }

  // handleCreatePlaylistButtonPressed() {
  //   const requestOptions = {
  //     method: 'POST',
  //     headers: {'Content-Type': 'application/json'},
  //     body: JSON.stringify({
  //       numSongs: this.state.numSongs,
  //       mood: this.state.mood,
  //     }),
  //   };
  //   fetch('/api/create-pl', requestOptions).then((response) => response.json()).then((data) => console.log(data));
  // }

  render() {
    return (
      <div>
        <div>
          <div id="loader"></div>
          <script type="text/javascript">
            {
              setTimeout(function(){
                document.getElementById("loader").style.display="none";
                window.location.href = 'http://127.0.0.1:8000/songs'
              }, 25000)
            }
          </script>
        </div>
        <h2 class="wait" style={{position:"relative", top:"200px"}}>Please wait while your playlist is being created.</h2>
      </div>
    );
  //   return <Grid container spacing={1}>
  //     <Grid item xs={12} align="center">
  //       <Typography component='h4' variant='h4'>
  //         Create A Playlist
  //       </Typography>
  //     </Grid>
  //     <Grid item xs={12} align="center">
  //       <FormControl component="fieldset">
  //         <FormHelperText>
  //           <div align="center">Playlist Parameter Control Panel</div>
  //         </FormHelperText>
  //         <RadioGroup row defaultValue="1" onChange={this.handleMoodChange}>
  //           <FormControlLabel value="1" control={<Radio color="primary" />} label="Happy" labelPlacement="bottom"/>
  //           <FormControlLabel value="2" control={<Radio color="secondary" />} label="Angry" labelPlacement="bottom"/>
  //         </RadioGroup>
  //         <RadioGroup row defaultValue="true">
  //           <FormControlLabel value="true" control={<Radio color="primary" />} label="Add to My Playlists" labelPlacement="bottom"/>
  //           <FormControlLabel value="false" control={<Radio color="secondary" />} label="Don't Add" labelPlacement="bottom"/>
  //         </RadioGroup>
  //       </FormControl>
  //     </Grid>
  //     <Grid item xs={12} align="center">
  //       <FormControl>
  //         <TextField required={true} type="number" onChange={this.handleNumSongsChange} defaultValue={this.defaultSongs} inputProps={{min: 1, style: { textAlign: "center"}, }}/>
  //         <FormHelperText>
  //           <div align="center">Number of Songs</div>
  //         </FormHelperText>
  //       </FormControl>
  //     </Grid>
  //     <Grid item xs={12} align="center">
  //       <Button color="primary" variant="contained" onClick={this.handleCreatePlaylistButtonPressed}>
  //         Create Playlist
  //       </Button>
  //     </Grid>
  //     <Grid item xs={12} align="center">
  //       <Button color="secondary" variant="contained" to="/login" component={Link}>
  //         Back
  //       </Button>
  //     </Grid>
  //   </Grid>;
  }
}