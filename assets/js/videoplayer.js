// This block loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// global variables
var list = []
var currentVideo = 0;
var player;

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
  // this will return an integer that will represent index
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
  // this will return an integer that will represent index
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
};

// this will server as the videoplayer class
var videoPlayer = function(){
  /*
    this block will handle the player
  */
  var pList = playList();

  // handles the initialization of a video
  // must get passed by a video id
  function init(code){
    player =  new YT.Player('player', {
      height: '390',
      width: '640', 
      videoId: code,
      events: {
        'onReady': playVideo,
        'onStateChange': onPlayerStateChange
      },
    });
  }

  // play the video
  function playVideo(){
    player.playVideo();
  }

  // pause the video
  function pauseVideo(){
    player.pauseVideo();
  }

  // trigger the next video
  function videoNext(code){
    // destroy the current player
    player.destroy();
    // get the next video id
    var code = list[pList.getNext()];
    // recreate the player
    init(code);
  }

  // this will trigger every time the state of the video changes
  function onPlayerStateChange(event){
    console.log(event.data) // for debugging
    if(event.data === 0){
      videoNext();
    }
  }

  return {
    init: function(code){
      init(code);
    },
    play: function(){
      playVideo();
    },
    pause: function(){
      pauseVideo();
    },
    next: function(){
      videoNext();
    }
  }
};