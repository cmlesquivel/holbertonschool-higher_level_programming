$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function( json ) {
    
    list_movies = json.results;
    for (let i = 0; i < list_movies.length; i++) 
    {
        $('#list_movies').append('<li>' + list_movies[i].title + '</li>');
    }
    
   });