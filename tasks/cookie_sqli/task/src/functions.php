<?php

function connect() {
  require 'config.php';

  $conn = pg_connect("host=$db_server dbname=$db_name user=$db_username password=$db_password");

  if(!$conn) {
    echo "Error : Unable to connect to database\n";
    exit(1);
  }

  return $conn;
}

function login($username, $password) {
  $conn = connect();

  $user_query = pg_query_params($conn, 'SELECT id, password FROM users WHERE
                                username = $1', array($username));
  $user_data = pg_fetch_array($user_query);

  if (password_verify($password, $user_data['password'])) {
    $session = bin2hex(random_bytes(15));

    setcookie('session', $session);

    pg_query_params($conn, 'INSERT INTO sessions VALUES($1, $2)', array($user_data['id'], $session));

    header("Location: /");
  } else {
    echo 'Wrong username or password';
  }
}

function data_for_session($session) {
  $conn = connect();

  $data_query = pg_query($conn, 'SELECT data FROM data JOIN sessions ON
                                data.user_id = sessions.user_id WHERE session = \''
                                . $session . '\'');
  $data_data = pg_fetch_array($data_query)['data'];

  return $data_data;
}
?>
