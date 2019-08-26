\set POSTGRES_APP_USER `echo $POSTGRES_APP_USER`
\set POSTGRES_APP_PASSWORD `echo $POSTGRES_APP_PASSWORD`
\set POSTGRES_DB `echo $POSTGRES_DB`

\c :POSTGRES_DB;

CREATE TABLE users (
    id SERIAL NOT NULL PRIMARY KEY,
    username varchar(255) NOT NULL UNIQUE,
    password varchar(60) NOT NULL
);

CREATE TABLE sessions (
    user_id INT NOT NULL REFERENCES users(id),
    session VARCHAR(30) NOT NULL
);

CREATE TABLE data (
    user_id INT NOT NULL UNIQUE REFERENCES users(id),
    data TEXT
);

CREATE ROLE :POSTGRES_APP_USER WITH LOGIN ENCRYPTED PASSWORD :'POSTGRES_APP_PASSWORD';

GRANT SELECT ON TABLE users, sessions, data TO :POSTGRES_APP_USER;
GRANT INSERT ON TABLE sessions TO :POSTGRES_APP_USER;

INSERT INTO users (id, username, password) VALUES
    (1, 'admin', '$2y$10$HE570XU.gSfl.g0mJE8e0eBfilxpaUqx9PZwbbFyd1JbfaS7mAyjm'),
    (2, 'ert', '$2y$10$KRLgCYDje6kvF4iYgyifguuOfYUm/CXzcrjLSG./vrsBPXsOg2Gym');

INSERT INTO sessions (user_id, session) VALUES
    (2, 'e75958c61727b1c5ad77e631f15633'),
    (2, '70c6609d1323bce5c4f5ccab5067fb'),
    (1, 'e60287e730f29937230255ade1b696');

INSERT INTO data (user_id, data) VALUES
    (1, '<h4>The flag:</h4>wwi{1_pR3Fer_n0SQL:P}'),
    (2, '<ul><li>Opracować lepszy skrypt do generowania flag</li>
         <li>Refactoring dockera</li></ul>');
