$(document).ready(function(){
    let URL = 'https://fourtonfish.com/hellosalut/?lang=';

     $('#btn_translate').on('click', function(){
        let lang =$('#language_code').val();

        $.get(URL+lang, function(data){
            $('#hello').text(data.hello);
        });
     });

     $('#language_code').on('keyup', function(e){
        if (e.keyCode === 13) {
            let lang =$('#language_code').val();

            $.get(URL+lang, function(data){
                $('#hello').text(data.hello);
            });
        }
     });   
});



