<?php
require 'functions.php';

if (isset($_COOKIE['session'])) {
  echo '
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Unhackable website</title>
    <meta name="Author" content="Michel Le Bihan">
    <meta name="contact" content="michel@lebihan.pl">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="/static/bootstrap/css/bootstrap.min.css">
  </head>

  <body>
    <form action="login.php" method="post" style="padding-top: 4rem;">
      <div class="card mx-auto h-100" style="width: 20rem">
        <div class="card-header">Your tasks:</div>
        <div class="card-body">
          '.data_for_session($_COOKIE['session']).'
        </div>
      </div>
    </form>
  </body>
</html>
';
} else {
  header("Location: /login.php");
}
?>
