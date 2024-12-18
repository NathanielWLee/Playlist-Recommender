// class MessageParser {
//     constructor(actionProvider, state) {
//         this.actionProvider = actionProvider;
//         this.state = state;
//     }

//     parse(message) {
//         console.log(message);
//         const lowercase = message.toLowerCase();

//         if (lowercase.includes("yes")) {
//             this.actionProvider.greet();
//         }
//     }
// }

// export default MessageParser;

class MessageParser {
    constructor(actionProvider) {
      this.actionProvider = actionProvider;
    }
    
    parse(message) {
      this.actionProvider.formatMessage(message);
      this.actionProvider.chatReply();
      
      // const lowerCaseMessage = message.toLowerCase()
      
      // // Hi, need a playlist rec?
      // if (lowerCaseMessage.includes("create playlist") || lowerCaseMessage.includes("yeah") || lowerCaseMessage.includes("sure") || lowerCaseMessage.includes("maybe") || lowerCaseMessage.includes("i guess")) {
      //   this.actionProvider.valenceMessage()
      // }
      
      // // What mood are you in today?
      // if (lowerCaseMessage.includes("i've been better")) {
      //     this.actionProvider.sorryMessage()
      //     this.actionProvider.energyMessage()
      // } else if (lowerCaseMessage.includes("over the moon")){
      //     this.actionProvider.happyMessage()
      //     this.actionProvider.energyMessage()
      // }
    }
  }
  
  export default MessageParser