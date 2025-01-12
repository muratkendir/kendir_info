let list_id = null;
let tag_id = null;

$(document).ready(function() {
  // Handle the click event on the dropdown items
  $('.dropdown-item').on('click', function(event) {
      event.preventDefault(); // Prevent the default anchor behavior

      const selectedText = $(this).text();
      $('#note_lists').text(selectedText);
      list_id= $(this).data('value');
      //console.log('Selected value:', list_id); // Log or use as needed
  });

const filter_button = document.getElementById("filter_button")

filter_button.onclick = function () {
    console.log(list_id);
    if (list_id == 0 || list_id == null) {
      location.href = "{% url 'allnotes' %}";
    }
    else {
      location.href = "list/" + list_id ;
    }
};

  // Take the tag buttons and forward to related page
  $('.tag').on('click', function(event) {
      event.preventDefault(); // Prevent the default anchor behavior

      tag_id= $(this).val();
      console.log('Selected value:', tag_id); // Log or use as needed
      if (tag_id == 0 || tag_id == null) {
        location.href = "{% url 'allnotes' %}";
      }
      else {
        location.href = "tag/" + tag_id;
      }
  });
});