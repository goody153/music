// This block loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// this will be the main class
var ListPlayer = function(songlist){

  // create the list
  var self = this;
  self.list = songlist;
  self.player = undefined;

  // init the player
  function init(){
    self.player = new YT.Player('player', {
    height: '390',
    width: '640',
    videoId: self.list[0],
    events: {
      'onReady': onPlayerReady,
      'onStateChange': onPlayerStateChange
    },
      playerVars: {
          playlist: self.list.slice(1).join(','),
          controls: 0,
          loop: 1,
          showinfo: 0,
      }
    });
  }

  function onPlayerReady(event){
    event.target.playVideo();
  }

  function onPlayerStateChange(event){
    if(event.data == 0){
      console.log("lalalala");
    }
  }

  // start player
  function startPlayer(){
    init();
  }

  // next video
  function next(){
    self.player.nextVideo();
  }

  // previous video
  function prev(){
    self.player.previousVideo();
  }

  function play(){
    self.player.playVideo();
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

  return {
    start: startPlayer,
    next: next,
    prev: prev,
    play: play,
    pause: pause,
    stop: stop,
    mute: mute,
    unmute: unmute
  }

};