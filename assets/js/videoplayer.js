// This block loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);


var list = []
var currentVideo = 0;

// this will server as the videoplayer class
var videoPlayer = function(){
  /*
    this block will handle the player
  */
  var player;
  var pList = playList();

  // handles the initialization of 
  function init(code){
    player =  new YT.Player('player', {
      height: '390',
      width: '640', 
      videoId: code,
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

  function videoNext(){
    // destroy the current player
    console.log(pList.getList());
    console.log(pList.getCurrent());
    console.log(pList.getNext());
    console.log(pList.getPrev());
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
    next = getCurrentVideo() + 1;
    if(next > songlist.length){
      currentVideo = next;
      return next = 0;
    }
    currentVideo = next;
    return next
  }

  // get the previous video
  function getPrevVideo(){
    prev = getCurrentVideo() - 1;
    if(prev < 0){
      return prev = songlist.length;
    }
    return prev;
  }

  // start playing the playlist
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
}