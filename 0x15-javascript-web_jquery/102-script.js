$(document).ready(function(){
    let URL = 'https://fourtonfish.com/hellosalut/?lang='
    

     $('#btn_translate').click(function(){
         let lang =$('#language_code').val();

        $.get(URL+lang,  function(data){
            $('#hello').text(data.hello);
        });
     });
    
});