// This block loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// onYouTubeIframeAPIReady is needed so that YT won't have any errors
function onYouTubeIframeAPIReady() {
 var ListPlayer = function(songlist){
  // create the list
  var self = this;
  self.list = songlist;
  var index = 0;

  // initialize the player, autoplay when ready
  function init(code){
    self.player = new YT.Player('player', {
      height: '390',
      width: '640',
      videoId: code,
      events: {
        'onReady': play,
        'onStateChange': stateChange,
      },
      playerVars: {
        controls: 0,
        showinfo: 0,
      }
    });
  }

  // control functions
  function next(){
    $('#song-state-'+(index+1)).removeClass("active");
    // destroy the current player
    self.player.destroy();
    // check if the index is greater than the list length
    if(getIndex() >= self.list.length-1){
      index = 0;
    }
    else{
      // set the index
      index = getIndex()+1;
    }
    init(self.list[index]);
  }

  function prev(){
    $('#song-state-'+(index+1)).removeClass("active");
    // destroy the current player
    self.player.destroy();
    // check if the index is greater than the list length
    if(getIndex() <= 0){
      index = self.list.length-1;
    }
    else{
      // set the index
      index = getIndex()-1;
    }
    init(self.list[index]);
  }

  function start(){
    init(self.list[0]);
  }

  function getLength(){
    return self.list.length;
  }

  function getIndex(){
    return index;
  }

  function stateChange(event){
    if(event.data == 1){
      $('#song-state-'+(index+1)).addClass("active");
    }
    if(event.data == 0){
      $('#song-state-'+(index+1)).removeClass("active");
      next();
    }
  }

  function play(){
    self.player.playVideo();
  }

  function stop(){
    self.player.stopVideo();
  }

  function pause(){
    self.player.pauseVideo();
  }

  function stop(){
    self.player.stopVideo();
  }

  function mute(){
    self.player.mute();
  }

  function unmute(){
    self.player.unMute();
  }
  
  // returns
  return {
    start: start,
    play: play,
    stop: stop,
    pause: pause,
    next: next,
    prev: prev,
    mute: mute,
    unmute: unmute,
    getlength: getLength,
    init: init,
  }

  };

  // this control is for when a the playlist is empty
  $('#btn_add').on('click', function(){
    if(listplayer.getlength() == 0){
      // Remove alert
      $('#noPlaylistAlert').hide();

      var code = $("[name=link]").val();
      listplayer.init(code);
    }
  });

  $('#btn_next').on('click',function(){
    listplayer.next();
  });

  $('#btn_prev').on('click',function(){
    listplayer.prev();
  });

  $('#btn_pause').on('click',function(){
    listplayer.pause();
  });

  $('#btn_stop').on('click',function(){
    listplayer.stop();
  });

  $('#btn_play').on('click',function(){
    listplayer.play();
  });

  $('#btn_mute').on('click',function(){
    listplayer.mute();
  });

  $('#btn_unmute').on('click',function(){
    listplayer.unmute();
  });

  var listplayer = new ListPlayer(song_ids);
  if(song_ids.length > 0){
    listplayer.start();
  }

}