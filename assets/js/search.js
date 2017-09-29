//doesn't allow to search if textfield is empty
  $(document).on('mouseover', '#search_form', function(){
    if($('#search_field').val() !== '')
      $('#search_submit').attr('disabled', false);
    else
      $('#search_submit').attr('disabled', true);
  });