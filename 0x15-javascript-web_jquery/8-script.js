$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (json) {
  const listMovies = json.results;
  for (let i = 0; i < listMovies.length; i++) {
    $('#listMovies').append('<li>' + listMovies[i].title + '</li>');
  }
});
