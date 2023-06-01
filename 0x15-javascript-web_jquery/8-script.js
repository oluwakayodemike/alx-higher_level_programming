$(document).ready(function() {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    var movies = data.results;
    var list = $('#list_movies');
    
    for (var i = 0; i < movies.length; i++) {
      var title = movies[i].title;
      var listItem = $('<li>').text(title);
      list.append(listItem);
    }
  });
});

