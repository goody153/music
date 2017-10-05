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
      // songEntry will be used to append on the songlist
      songEntry = '<div class="media">'
                    + '<div class="media-left media-middle">'
                    +    '<img class="media-object" src="'+ response.thumb_url +'">'
                    + '</div>'
                    + '<div class="media-body">'
                    +  '<h4 class="media-heading">'+ response.title +'</h4>'
                    + 'Duration: '+ response.duration +''
                    + '<br>'
                    + 'By: '+ response.user +''
                    + '<br>'
                    + '<a href="' 
                    + response.edit_url + '">Edit</a>'
                    + ' '
                    + '<a href="'
                    + response.delete_url + '">Delete</a>'
                    + '</div>'
                    + '</div>';
      $('#songlist').append(songEntry);

      song_ids.push(response.link);

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
      $('#playlists').html(response)
    });
  });

    $(document).on('click', '#all_playlist', function(event){
      event.preventDefault();
    $.ajax({
      type: 'Get',
      url: $(this).attr('url'),
      data: $(this).serialize()
    }).done(function(response){
      $('#playlists').html(response)
    });
  });