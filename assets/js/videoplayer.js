// This block loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// global variables
var list = []
var currentVideo = 0;
var player;

// this will be the playList class, which will "inherit" the videoplayer "class"
var playList = function(){
  /*
    this block will hold the list functions
  */

  // load the playlist from the template to the JS file
  function loadPlaylist(){
    list = songlist;
  }

  // add a video to the list
  function addVideo(code){
    list.append(code);
  }

  // get the playlist
  function getPlaylist(){
    return list;
  }

  // get the current video that's playing
  function getCurrentVideo(){
    return currentVideo;
  }

  // get the next video
  function getNextVideo(){
    // destroy the current player
    player.destroy();
    // set the next index
    next = getCurrentVideo() + 1;
    // if the current video is the last video on the list
    if(next >= songlist.length){
      // reset the index of the current video
      next = 0;
    }
    // set the index of the current video
    currentVideo = next;
    // reinstantiate
    videoPlayer().init(list[currentVideo]);
  }

  function getPrevVideo(){
    // destroy the current player
    player.destroy();
    // set the next index
    next = getCurrentVideo() - 1;
    // if the current video is the last video on the list
    if(next <= 0){
      // reset the index of the current video
      next = songlist.length-1;
    }
    // set the index of the current video
    currentVideo = next;
    // reinstantiate
    videoPlayer().init(list[currentVideo]);
  }

  // start playing the playlist starting with the first song
  function startPlaylist(){
    loadPlaylist();
    videoPlayer().init(list[0])
  }

  return {
    load: function(){
      loadPlaylist();
    },
    playall: function(){
      startPlaylist();
    },
    getCurrent: function(){
      return getCurrentVideo();
    },
    getList: function(){
      return getPlaylist();
    },
    getNext: function(){
      return getNextVideo();
    },
    getPrev: function(){
      return getPrevVideo();
    }
  }
};


// this will server as the videoplayer class
var videoPlayer = function(){
  /*
    this block will handle the player
  */

  // handles the initialization of a video
  // must get passed by a video id
  function init(code){
    player =  new YT.Player('player', {
      height: '390',
      width: '640', 
      videoId: code,
      events: {
        'onReady': videoPlay,
        'onStateChange': onPlayerStateChange
      },
      playerVars: {
        'controls': 0,
      },
    });
  }

  // play the video
  function videoPlay(){
    player.playVideo();
  }

  // pause the video
  function videoPause(){
    player.pauseVideo();
  }

  // this will trigger every time the state of the video changes
  function onPlayerStateChange(event){
    console.log(event.data) // for debugging
    if(event.data === 0){
      playList().getNext();
    }
  }

  return {
    init: function(code){
      init(code);
    },
    play: function(){
      videoPlay();
    },
    pause: function(){
      videoPause();
    }
  }
};