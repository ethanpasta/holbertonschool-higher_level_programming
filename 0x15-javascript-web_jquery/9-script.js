$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  $('div#hello').html(data.hello);
});
