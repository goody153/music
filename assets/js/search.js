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
    var targetBody = $('#afterAddBody');

    target.addClass('hidden');

    $.ajax({
      method: 'POST',
      url: $(this).attr('action'),
      data: $(this).serialize()
    }).done(function(response){
      targetBody.html('<div class="text-success"><span class="bold">'
            + response.songtitle
            + '</span> was successfully added to <strong>'
            + response.playlist + '</strong></div>');
      target.removeClass();
      target.addClass('panel panel-success');
    }).fail(function(error){
      if(error.status == 400){
        targetBody.html('<div class="text-danger">Cannot add to <strong>'
          + error.responseJSON.playlist + '</strong>: '
          + error.responseJSON.error.link + "</div>");
        target.removeClass();
        target.addClass('panel panel-danger');
      }
    }).always(function(){
      target.removeClass('hidden');
    });
    event.preventDefault();
  });