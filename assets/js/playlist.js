  //ajax for adding songs
  $(document).on('submit', '#songForm' , function( event ){
    event.preventDefault();
    // submit new song on the playlist
    $.ajax({
      method: 'POST',
      url: $(this).attr('action'),
      data: $(this).serialize()
    }).done(function(response){
      // songEntry will be used to append on the songlist
      songEntry = '<li class="list-group-item">' 
        + response.title + '<small class="pull-right"><a href="' 
        + response.edit_url + '">Edit</a> <a href="'
        + response.delete_url + '">Delete</a></small></li>';
      $('#songlist').append(songEntry);
    }).fail(function(error){
      if(error.status === 400){
        // clean the error containers
        $('#title_error').text('');
        $('#link_error').text('');
        if(error.responseJSON.title !== undefined)
          $('#title_error').text(error.responseJSON.title);
        if(error.responseJSON.link !== undefined)
          $('#link_error').text(error.responseJSON.link);
      }
    });
  });

  // https://www.youtube.com/watch?v=93OCi10BsX4
  // https://www.youtube.com/watch?v=7_8_G_uj-kU
  // https://www.youtube.com/watch?v=YraOnCD9bVQ
  // https://www.youtube.com/watch?v=2DpHMwhiSvE