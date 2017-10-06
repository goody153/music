  //ajax for adding songs
  $(document).on('submit', '#songForm' , function( event ){
    event.preventDefault();
    $('#validation_error').text('');
    // submit new song on the playlist
    var data = $(this).serialize();
    $('#id_link').val('');
    $.ajax({
      method: 'POST',
      url: $(this).attr('action'),
      data: data
    }).done(function(response){
      // add videoID to player
      song_ids.push(response.link);
      // create the necessary csrftoken for the delete song form
      var csrftoken = getCookie('csrftoken');
      // songEntry will be used to append on the songlist
      songEntry = '<li id="song-state-'+ ( song_ids.length ) +'" class="">'
                    + '<div class="media" id="'+ response.id +'">'
                    + '<div class="media-left media-middle">'
                    + '<img class="media-object" src="'+ response.thumb_url +'">'
                    + '</div>'
                    + '<div class="media-body">'
                    +  '<h4 class="media-heading">'+ response.title +'</h4>'
                    + 'Duration: '+ response.duration +''
                    + '<br>'
                    + 'By: '+ response.user +''
                    + '<br>'
                    + '<a href="' 
                    + response.edit_url + '">Edit</a>'
                    + '<form method="post" class="deleteSong" action="'
                    + response.delete_url + '" class="deleteSong">'
                    + '<input type="hidden" name="csrfmiddlewaretoken" value="' + csrftoken
                    + '"><button type="submit">Delete</button>'
                    + '</form></div>'
                    + '</div></li>';
      $('#songlist').append(songEntry);
    }).fail(function(error){
      if(error.status === 400){
        // clean the error containers
        if(error.responseJSON.link !== undefined)
          $('#validation_error').append(error.responseJSON.link);
      }
    });
  });

  $(document).on('submit', '#search_playlist', function(event){
    event.preventDefault();
    $.ajax({
      type: 'POST',
      url: $(this).attr('action-url'),
      data: $(this).serialize()
    }).done(function(response){
      $('#playlists').html(response);
    });
  });

  $(document).on('click', '#all_playlist', function(event){
    event.preventDefault();
    $.ajax({
      type: 'Get',
      url: $(this).attr('url'),
      data: $(this).serialize()
    }).done(function(response){
      $('#playlists').html(response);
    });
  });

  // ajax for deleting songs
  $(document).on('submit', '.deleteSong', function( event ){
    event.preventDefault();
    $.ajax({
      method: 'POST',
      url: $(this).attr('action'),
      data: $(this).serialize()
    }).done(function(response){
      //remove song from the template
      $("#"+response.song_id).parent( "li" ).remove()
      song_ids.pop();
      console.log(song_ids);
    });
  });

  // function for creating csrf_token 
  function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie !== '') {
          var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
              var cookie = jQuery.trim(cookies[i]);
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }