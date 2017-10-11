//doesn't allow to search if textfield is empty
  $(document).on('mouseover', '#search_form', function(){
    if($('#search_field').val() !== ''){
      $('#search_submit').attr('disabled', false);
    }
    else{
      $('#search_submit').attr('disabled', true);
    }
  });

 // ajax add song from youtubesearch
  $(document).on('submit', '.addYoutubeSong', function( event ){
    var target = $('#afterAdd');
    target.addClass('hidden');
    $.ajax({
      method: 'POST',
      url: $(this).attr('action'),
      data: $(this).serialize()
    }).done(function(response){
      target.html('<div><span class="bold">'
            + response.songtitle
            + '</span> was successfully added to <strong>'
            + response.playlist + '</strong>'
            + '<br><a href="'
            + response.playlist_url
            + '">Click Here to View Playlist!</a></div>');
      target.removeClass();
      target.addClass('alert alert-success');
    }).fail(function(error){
      if(error.status == 400){
        target.html('<div>Cannot add to <strong>'
          + error.responseJSON.playlist + '</strong>: '
          + error.responseJSON.error.link
          + '<br><a href="' + error.responseJSON.playlist_url
          + '">Click Here to View Playlist!</a></div>');
        target.removeClass();
        target.addClass('alert alert-danger');
      }
    }).always(function(){
      target.removeClass('hidden');
    });
    event.preventDefault();
  });