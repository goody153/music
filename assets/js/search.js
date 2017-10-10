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
  	$.ajax({
  	  method: 'POST',
  	  url: $(this).attr('action'),
  	  data: $(this).serialize()
  	}).done(function(response){
  	  $('#afterAdd').html('<div class="success"><span class="bold">' 
                  + response.songtitle
  	  					  + '</span> was successfully added to <span class="bold">' 
                  + response.playlist + '</span></div>');
  	}).fail(function(error){
  	  if(error.status == 400){
        $('#afterAdd').html('<div class="error">Cannot add to <span class="bold">' 
                  + error.responseJSON.playlist + '</span>: ' 
                  + error.responseJSON.error.link + "</div>");
  	  }
  	});
  	event.preventDefault();
  });