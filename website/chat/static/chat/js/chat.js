const roomName = JSON.parse(document.getElementById('room-name').textContent);      // get room name
const username = JSON.parse(document.getElementById('username').textContent);       // get username

// Establish WebSocket connection
const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + '/'
);

// Close connection
chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

// Receive a message
chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);

    const chatContent = document.querySelector('#chat-content');

    let lastMessage = getLastMessageHtml();

    if ( username == data.sender ){                                                // if received message was sent from this client
        if ( lastMessage ){                                                             // if chat is not empty
            if ( !isMessageIncoming(lastMessage) ){                                         // if last message was sent from this client 
                appendMessage(lastMessage, data.message);
            }
            else{                                                                           // if last message was sent from another cliend 
                chatContent.innerHTML += generateMessageHtml(data.message, false);
            }
        }
        else{                                                                           // if chat is empty
            chatContent.innerHTML += generateMessageHtml(data.message, false);
        }
    }
    else{                                                                           // if received message was sent from another client
        if ( lastMessage ){                                                             // if chat is not empty
            if ( !isMessageIncoming(lastMessage) ){                                         // if last message was sent from this client
                chatContent.innerHTML += generateMessageHtml(data.message, true);
            }
            else{                                                                           // if last message was sent from another client
                appendMessage(lastMessage, data.message);
            }
        }
        else{                                                                           // if chat is empty
            chatContent.innerHTML += generateMessageHtml(data.message, true);
        }
    }
};    

// Catch message submition 
document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

// Send message
document.querySelector('#chat-message-submit').onclick = function(e) {
    // Get message content
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;

    // Send message to the server
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
};

function generateCurrentDateHtml(){
    // Get current date
    const currentDate = new Date();
    const currentYear = currentDate.getFullYear();
    const currentHours = currentDate.getHours();
    const currentMinutes = currentDate.getMinutes();

    return `<p class="meta"><time datetime="${currentYear}">${currentHours}:${currentMinutes}</time></p>`;
}

// Appends message to an existing message group
function appendMessage(messageHtml, messageText){
        // Remove last message time
        const date = messageHtml.lastElementChild;
        messageHtml.removeChild(date);

        // Add last message
        messageHtml.innerHtml += `<p>${messageText}</p>`;

        // Add date and time
        messageHtml.innerHtml += generateCurrentDateHtml();
}

// Returns the last message object if there are any.
// Returns null otherwise.
function getLastMessageHtml(){
    let chatContent = document.querySelector('#chat-content');
    let lastMessage = chatContent.lastElementChild;

    if ( lastMessage.classList.contains('media-chat') ){
        return lastMessage;
    }
    else{
        return null;
    }
}

// Checks if the chat contains any messages
function isChatEmpty(){
    const lastMessage = getLastMessageHtml;

    if (lastMessage === null){
        return false;
    }
    else{
        return true;
    }
}

// Checks if the message in the chat is send from this client
function isMessageIncoming(messageHtml){
    if ( messageHtml.classList.contains('media-chat-reverce') ){                // if last message was sent from this client (if last message has a class of an outgoing message)
        return false;
    }
    else{                                                                       // if last message was sent from another cliend (if last message has a class of an incoming message)
        return true;
    }
}

// Generates html for messages
function generateMessageHtml(messageText, isIncoming){
    let htmlClass = 'media media-chat';
    // Get proper class
    if ( !isIncoming ){
        htmlClass += ' media-chat-reverse';
    }

    return `<div class="${htmlClass}">
                <div class="media-body">
                    <p>${messageText}</p>
                    ${generateCurrentDateHtml()}
                </div>
            </div>`;
}