class ActionProvider {

    constructor(createChatBotMessage, setStateFunc) {
      this.createChatBotMessage = createChatBotMessage;
      this.setState = setStateFunc;
    }

    formatMessage(message){
      var messageToPython = {messageFromChat: message}
      this.sendToLex(messageToPython);
    }
    
    sendToLex(message){
      $.ajax({
        type: 'POST',
        url: "http://127.0.0.1:5000/receiver",
        data: JSON.stringify(message),
        error: function(e) {
          console.log(e);
        },
        dataType: "json",
        contentType: "application/json"
      });
    }

    chatReply(){
      console.log("test 1");
      var lexResponse;
      
      let now = Date.now(),
      end = now + 1000;
      while (now < end) { now = Date.now(); }

      $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/test",
        async: false,
        success: function (result) {
          lexResponse = result
        },
      });


      if(lexResponse != null){
        if('fallback' in lexResponse){
          console.log("fallback")
          const message = this.createChatBotMessage(lexResponse.fallback)
          this.updateChatbotState(message)
        }else if('ending' in lexResponse){
          console.log("ending")
          const message1 = this.createChatBotMessage(lexResponse.ending[0])
          this.updateChatbotState(message1)
          const message2 = this.createChatBotMessage(lexResponse.ending[1])
          this.updateChatbotState(message2)
        }else if('question' in lexResponse){
          console.log("question:", lexResponse.question)
          // const message = this.createChatBotMessage(lexResponse.question, {
          //   widget: "buttons",
          // })
          const message = this.chooseWidget(lexResponse.question)
          this.updateChatbotState(message)
        }else{
          print("what the heck???")
        }
      }
    }

    chooseWidget(lexQuestion) {
      var message
      switch (lexQuestion) {
        case "How are you feeling today?":
          message = this.createChatBotMessage(lexQuestion, {
            widget: "valence",
          })
          break;
        case "Want to cheer up?":
          message = this.createChatBotMessage(lexQuestion, {
            widget: "cheer",
          })
          break;
        case "How awake are you feeling?":
          message = this.createChatBotMessage(lexQuestion, {
            widget: "energy",
          })
          break;
        case "Do you need an energy boost?":
          message = this.createChatBotMessage(lexQuestion, {
            widget: "boost",
          })
          break;
        case "Do you want to relax?":
          message = this.createChatBotMessage(lexQuestion, {
            widget: "relaxation",
          })
          break;
        case "Are you in the mood to dance?":
          message = this.createChatBotMessage(lexQuestion, {
            widget: "danceability",
          })
          break;
        case "How do you feel about singing along to your songs?":
          message = this.createChatBotMessage(lexQuestion, {
            widget: "instrumentalness",
          })
          break;
        case "In the mood to be at a concert?":
          message = this.createChatBotMessage(lexQuestion, {
            widget: "liveness",
          })
          break;
        case "Do you like your music loud?":
          message = this.createChatBotMessage(lexQuestion, {
            widget: "loudness",
          })
          break;
        case "How acoustic do you like your music?":
          message = this.createChatBotMessage(lexQuestion, {
            widget: "acoustic",
          })
          break;
        // case "Do you want entirely new music?":
        //   message = this.createChatBotMessage(lexQuestion, {
        //     widget: "familiarity",
        //   })
        //   break;
      }
      return message
    }

    handleGreatValence = () => {
      const message = this.createChatBotMessage("That's great to hear!")
      this.updateChatbotState(message)
      this.formatMessage("I'm feeling great! :)")
      this.chatReply()
    }
    handleOkayValence = () => {
      const message = this.createChatBotMessage("Okay. :/")
      this.updateChatbotState(message)
      this.formatMessage("I'm okay. :/")
      this.chatReply()
    }
    handleBeenBetterValence = () => {
      const message = this.createChatBotMessage("I'm sorry to hear that.")
      this.updateChatbotState(message)
      this.formatMessage("I've been better. :(")
      this.chatReply()
    }
    // handleBeenBetterValence = () => {
    //   const message = this.createChatBotMessage("I'm sorry to hear that.")
    //   this.updateChatbotState(message)
    //   this.formatMessage("I've been better. :(")
    //   this.chatReply()
    // }

    handleYesCheerUp = () => {
      const message = this.createChatBotMessage("Okay, I think know what'll put you in a better mood!")
      this.updateChatbotState(message)
      this.formatMessage("Yes")
      this.chatReply()
    }
    handleNoCheerUp = () => {
      const message = this.createChatBotMessage("No worries, it's good to let yourself feel your feelings.")
      this.updateChatbotState(message)
      this.formatMessage("No")
      this.chatReply()
    }


    // // Energy question
    // energyMessage() {
    //   const message = this.createChatBotMessage("How awake are you feeling?", {
    //     widget: "energy",
    //   })
    //   this.updateChatbotState(message)
    // }
    handleEnergizedEnergy = () => {
      const message = this.createChatBotMessage("Woohoo!")
      this.updateChatbotState(message)
      this.formatMessage("Energized!")
      this.chatReply()
    }
    handleStillWakingEnergy = () => {
      const message = this.createChatBotMessage("No worries, it's still early.")
      this.updateChatbotState(message)
      this.formatMessage("Slowly waking myself up.")
      this.chatReply()
    }
    handleExhaustedEnergy = () => {
      const message = this.createChatBotMessage("Understood.")
      this.updateChatbotState(message)
      this.formatMessage("Completely exhausted.")
      this.chatReply()
    }



    
    handleYesEnergyBoost = () => {
      const message = this.createChatBotMessage("Okay, consider this your energy boost.")
      this.updateChatbotState(message)
      this.formatMessage("Yes")
      this.chatReply()
    }
    handleNoEnergyBoost = () => {
      const message = this.createChatBotMessage("Got it, keeping it low energy.")
      this.updateChatbotState(message)
      this.formatMessage("No")
      this.chatReply()
    }

    // // Relaxation question
    // relaxationMessage() {
    //   const message = this.createChatBotMessage("Do you need or just want to relax?", {
    //     widget: "relaxation",
    //   })
    //   this.updateChatbotState(message)
    // }
    handleYesRelax = () => {
      const message = this.createChatBotMessage("Okay, we can do that.")
      this.updateChatbotState(message)
      this.formatMessage("Yes")
      this.chatReply()
    }
    handleNoRelax = () => {
      const message = this.createChatBotMessage("Okay, good to know.")
      this.updateChatbotState(message)
      this.formatMessage("No")
      this.chatReply()
    }

    // // Danceability question
    // danceabilityMessage() {
    //   const message = this.createChatBotMessage("Are you in the mood to dance?", {
    //     widget: "danceability",
    //   })
    //   this.updateChatbotState(message)
    // }
    handleYesDance = () => {
      const message = this.createChatBotMessage("Great, let's dance!")
      this.updateChatbotState(message)
      this.formatMessage("Yes!")
      this.chatReply()
    }
    handleMaybeDance = () => {
      const message = this.createChatBotMessage("Okay, we'll surprise you.")
      this.updateChatbotState(message)
      this.formatMessage("Eh, try me!")
      this.chatReply()
    }
    handleNoDance = () => {
      const message = this.createChatBotMessage("Okay, got it. Not too dancey today.")
      this.updateChatbotState(message)
      this.formatMessage("No")
      this.chatReply()
    }
    // 
    // // Instrumentalness question
    // instrumentalnessMessage() {
    //   const message = this.createChatBotMessage("How do you feel about singing a long to your songs?", {
    //     widget: "instrumentalness",
    //   })
    //   this.updateChatbotState(message)
    // }
    handleYesSing = () => {
      const message = this.createChatBotMessage("Alright, get your vocals ready!")
      this.updateChatbotState(message)
      this.formatMessage("Pass me the mic!")
      this.chatReply()
    }
    handleMaybeSing = () => {
      const message = this.createChatBotMessage("Okay, we'll surprise you.")
      this.updateChatbotState(message)
      this.formatMessage("I don't mind.")
      this.chatReply()
    }
    handleNoSing = () => {
      const message = this.createChatBotMessage("Okay, that's fair. We'll help you zone out.")
      this.updateChatbotState(message)
      this.formatMessage("I just want to zone out.")
      this.chatReply()
    }

    // // Liveness question
    // livenessMessage() {
    //   const message = this.createChatBotMessage("In the mood to be at a concert?", {
    //     widget: "liveness",
    //   })
    //   this.updateChatbotState(message)
    // }
    handleYesLive = () => {
      const message = this.createChatBotMessage("We'll make it feel like you're really there.")
      this.updateChatbotState(message)
      this.formatMessage("Yes!")
      this.chatReply()
    }
    handleMaybeLive = () => {
      const message = this.createChatBotMessage("Okay, we'll surprise you.")
      this.updateChatbotState(message)
      this.formatMessage("It doesn't matter!")
      this.chatReply()
    }
    handleNoLive = () => {
      const message = this.createChatBotMessage("Got it, recorded songs only.")
      this.updateChatbotState(message)
      this.formatMessage("No.")
      this.chatReply()
    }

    // // Loudness question
    // loudnessMessage() {
    //   const message = this.createChatBotMessage("Do you like your music loud?", {
    //     widget: "loudness",
    //   })
    //   this.updateChatbotState(message)
    // }
    handleYesLoud = () => {
      const message = this.createChatBotMessage("*screams* Let's go!")
      this.updateChatbotState(message)
      this.formatMessage("Bring it on!")
      this.chatReply()
    }
    handleKindOfLoud = () => {
      const message = this.createChatBotMessage("Okay, we'll keep it somewhere in the middle.")
      this.updateChatbotState(message)
      this.formatMessage("Kind of.")
      this.chatReply()
    }
    handleNotLoud = () => {
      const message = this.createChatBotMessage("*whispers* Got it, let's keep it light.")
      this.updateChatbotState(message)
      this.formatMessage("Not really.")
      this.chatReply()
    }
    
    // // Acoustic question
    // acousticMessage() {
    //   const message = this.createChatBotMessage("How acoustic do you like your music?", {
    //     widget: "acoustic",
    //   })
    //   this.updateChatbotState(message)
    // }
    handleAcousticMusic = () => {
      const message = this.createChatBotMessage("Okay, we'll get you more acoustic songs.")
      this.updateChatbotState(message)
      this.formatMessage("I prefer music from instruments!")
      this.chatReply()
      this.createPlaylist()
    }
    handleMixedMusic = () => {
      const message = this.createChatBotMessage("I like your style.")
      this.updateChatbotState(message)
      this.formatMessage("A bit of both!")
      this.chatReply()
      this.createPlaylist()
    }
    handleElectronicMusic = () => {
      const message = this.createChatBotMessage("Okay, me too.")
      this.updateChatbotState(message)
      this.formatMessage("I prefer music from instruments!")
      this.chatReply()
      this.createPlaylist()
    }

    // // Familiarity question
    // familiarityMessage() {
    //   const message = this.createChatBotMessage("Do you want entirely new music?", {
    //     widget: "familiarity",
    //   })
    //   this.updateChatbotState(message)
    // }
    // handleNewMusic = () => {
    //   // this.handleClosingMessage()
    //   this.formatMessage("Yes!")
    //   this.chatReply()
    //   this.createPlaylist()
    // }
    // handleNewAndKnownMusic = () => {
    //   // this.handleClosingMessage()
    //   this.formatMessage("A bit of both.")
    //   this.chatReply()
    //   this.createPlaylist()
    // }
    // handleKnownMusic = () => {
    //   // this.handleClosingMessage()
    //   this.formatMessage("No, only the songs I know")
    //   this.chatReply()
    //   this.createPlaylist()
    // }

    createPlaylist() {
      // console.log("create playlist before")
      fetch('/spotify/create-playlist')
      // .then(
      //   (response) => response.json()
      // ).then(
      //   (data) => {
      //     window.location.replace(data.url);
      //   }
      // );
      // console.log("create playlist after")

      // var songs;
      // $.ajax({
      //   type: "GET",
      //   url: "/spotify/create-playlist",
      //   async: false,
      //   success: function (result) {
      //     songs = result
      //   },
      // });

      // fetch('http://example.com/movies.json')
      // .then(response => response.json())
      // .then(data => console.log(data));

      // fetch("/spotify/create-playlist");
      // var xmlHttp = new XMLHttpRequest();
      // xmlHttp.open( "GET", "/spotify/create-playlist", false ); // false for synchronous request
      // xmlHttp.send( null );
      // songs = xmlHttp.responseText;
      // songs = requests.get("/spotify/create-playlist")
      // console.log("songs: ", songs)
    }

    // handleClosingMessage = () => {
    //   const message = this.createChatBotMessage("Perfect! We've uploaded your playlist to Spotify. Enjoy! Thanks for using TuneLink!")
    //   this.updateChatbotState(message)
    // }

    delay(time){
      let now = Date.now(),
      end = now + time;
      while (now < end) { now = Date.now(); }
    }


    updateChatbotState(message) {
    // NOTE: This function is set in the constructor, and is passed in
    // from the top level Chatbot component. The setState function here     
    // actually manipulates the top level state of the Chatbot, so it's     
    // important that we make sure that we preserve the previous state.
     this.setState(prevState => ({
          ...prevState, messages: [...prevState.messages, message]
      }))
    }
  }
  
  export default ActionProvider