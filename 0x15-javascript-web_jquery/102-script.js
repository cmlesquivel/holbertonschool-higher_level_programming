$(document).ready(function () {
  const URL = 'https://fourtonfish.com/hellosalut/?lang=';

  $('#btn_translate').click(function () {
    const lang = $('#language_code').val();

    $.get(URL + lang, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
