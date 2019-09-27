$(document).ready(function () {
  $('input#language_code').keypress(function (event) {
    if (event.which === 13) {
      $('input#btn_translate').click();
    }
  });
  $('input#btn_translate').click(function () {
    const lan = $('input#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/?lang=' + lan, function (data) {
      $('div#hello').html(data.hello);
    });
  });
});
