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
  	  $('#afterAdd').html('<div class="success">' + response.result + "</div>");
  	}).fail(function(error){
  	  if(error.status == 400){
        $('#afterAdd').html('<div class="error">' + error.responseJSON.link + "</div>");
  	  }
  	});
  	event.preventDefault();
  });