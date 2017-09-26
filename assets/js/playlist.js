  //ajax for adding songs
  $(document).on('submit', '#songForm' , function( event ){
    event.preventDefault();
    $('#validation_error').text('');
    // submit new song on the playlist
    $.ajax({
      method: 'POST',
      url: $(this).attr('action'),
      data: $(this).serialize()
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
                     + '<a href="' 
                    + response.edit_url + '">Edit</a>'
                    + ' '
                     + '<a href="'
                    + response.delete_url + '">Delete</a>'
                   + '</div>'
                + '</div>';
      $('#songlist').append(songEntry);
      $('#id_link').val('');
    }).fail(function(error){
      if(error.status === 400){
        // clean the error containers
        if(error.responseJSON.link !== undefined)
          $('#validation_error').append(error.responseJSON.link);
      }
    });
  });