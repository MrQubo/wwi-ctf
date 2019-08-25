<?php
require 'functions.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
  if (array_key_exists('username', $_POST) and array_key_exists('password', $_POST)) {
    login($_POST['username'], $_POST['password']);
  }

  exit();
}
?>

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
        <div class="card-header">Please sign in to continue</div>
        <div class="card-body">
          <div class="form-group">
            <label for="exampleInputEmail1">Username:</label>
            <input type="text" class="form-control" name="username" placeholder="Username" required>
          </div>
          <div class="form-group">
            <label for="exampleInputPassword1">Password:</label>
            <input type="password" class="form-control" name="password" placeholder="Password" required>
          </div>
          <button type="submit" class="btn btn-primary">Sign in</button>
        </div>
      </div>
    </form>
  </body>
</html>