$(document).ready(function() {
  console.log($(document))
  var namespace = '/main'
  var socket = io(namespace);
  
  socket.on('connect', function() {
    socket.emit('connected event', {
      user: 'tim'
    });
  });
  
  var form = $('form').on('submit', function(e) {
    e.preventDefault()
    let user_name = $('input.username').val()
    let user_input = $('input.message').val()
    
    socket.emit('message event', {
      user_name : user_name,
      message : user_input
    })
    $('input.message').val( '' ).focus()
  });
  
  socket.on('server response', function(json) {
    console.log('the message was: ' + json.message)
    if( typeof json.user_name !== 'undefined' ) {
      $('h3').remove()
      $('div.message_holder').append('<div><b style="color: #000">'+
                                      json.user_name+'</b> '+
                                      json.message+'</div>')
    }
  })
});
