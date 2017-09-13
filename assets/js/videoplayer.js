// This block loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

var list = [];
var currentlyPlaying = 0;
var player;

// this will server as the videoplayer class
var videoPlayer = function(){
  /*
    this block will handle the player
  */

  // handles the initialization of 
  function init(code){
    player =  new YT.Player('player', {
      height: '390',
      width: '640', 
      videoId: list[code],
      events: {
        'onReady': play,
        'onStateChange': onPlayerStateChange
      },
    });
  }

  function play(){
    player.playVideo();
  }

  function pause(){
    player.pauseVideo();
  }

  function videoNext(event){
    // destroy the current player
    player.destroy();
    // check if the video playing is the last on the list
    if(currentlyPlaying >= list.length-1){
      currentlyPlaying = 0;
    }
    else{
      currentlyPlaying += 1;
    }
    init(currentlyPlaying);
  }

  function onPlayerStateChange(event){
    console.log(event.data)
    if(event.data === 0){
      videoNext();
    }
  }

  return {
    init: function(code){
      init(code);
    },
    play: function(){
      play();
    },
    pause: function(){
      pause();
    }
  }
}

var playList = function(){
  /*
    this block will hold the list functions
  */

  function loadPlaylist(){
    list = songlist;
  }

  return{
    load: function(){
      loadPlaylist();
    }
  }
}