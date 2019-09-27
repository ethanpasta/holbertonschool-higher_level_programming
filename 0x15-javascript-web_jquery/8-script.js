$.get('https://swapi.co/api/films/?format=json', function (data) {
  $.each(data.results, function (index, film) {
    $('ul#list_movies').append('<li>' + film.title + '</li>');
  });
});
