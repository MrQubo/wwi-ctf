<?php
require 'functions.php';

if (isset($_COOKIE['session'])) {
  print_data($_COOKIE['session']);
} else {
  header("Location: /login.php");
}
?>