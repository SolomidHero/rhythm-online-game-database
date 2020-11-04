-- CREATE DATABASE rhythmdb OWNER sotomi;
CREATE SCHEMA game;
CREATE TYPE play_mode AS ENUM ('easy', 'no fail', 'less time', 'hard rock', 'hidden', 'double time', 'hardcore', 'flashlight');
CREATE TYPE grade_type AS ENUM ('D', 'C', 'B', 'A', 'S', 'SS');

CREATE TABLE game.UserProfile (
  user_id         SERIAL PRIMARY KEY,
  username        varchar(20) NOT NULL,
  country         varchar(20) NOT NULL,
  user_panel      xml,
  avatar          varchar(100),
  supporter_tag   bool DEFAULT false,
  join_time       date NOT NULL,
  birthdate       date,
  pass_word       varchar(256) NOT NULL,
  email           varchar(100) NOT NULL
);

CREATE TABLE game.Beatmap (
  map_id          SERIAL PRIMARY KEY,
  song            varchar(100) NOT NULL,
  artist          varchar(100),
  creator_id      int REFERENCES game.UserProfile(user_id) NOT NULL,
  submitted_date  timestamp NOT NULL,
  approving_date  timestamp NOT NULL,
  genre           varchar(20),
  lang            varchar(20),
  description     xml,
  source          varchar(100) NOT NULL  --  link
);
CREATE INDEX beatmap_index ON game.Beatmap USING btree (song, artist);

CREATE TABLE game.Tag (
  map_id          int REFERENCES game.Beatmap(map_id) NOT NULL,
  tag             varchar(30) NOT NULL
);

CREATE TABLE game.Difficulty (  --  diff chararacteristics
  diff_id         SERIAL PRIMARY KEY,
  map_id          int REFERENCES game.Beatmap(map_id) NOT NULL,
  difficulty      NUMERIC(4, 2) NOT NULL,
  length          int NOT NULL,
  BPM             int NOT NULL,
  object_count    int NOT NULL
);

CREATE TABLE game.Score (
  play_id         SERIAL PRIMARY KEY,
  diff_id         int REFERENCES game.Difficulty(diff_id) NOT NULL,
  user_id         int NOT NULL,
  grade           grade_type NOT NULL,
  score           int NOT NULL,
  accuracy        NUMERIC(5, 2) NOT NULL,
  max_combo       int NOT NULL,
  miss            int NOT NULL,
  pp              int NOT NULL,
  play_date       timestamp,
  play            varchar(100)
);
CREATE INDEX score_index ON game.Score USING btree (diff_id, user_id);

CREATE TABLE game.PlayMode (
  play_id         int REFERENCES game.Score(play_id) NOT NULL,
  mod             play_mode NOT NULL
);

CREATE TABLE game.BeatmapRate (
  map_id          int REFERENCES game.Beatmap(map_id) NOT NULL,
  user_id         int REFERENCES game.UserProfile(user_id) NOT NULL,
  user_rating     int NOT NULL,
  PRIMARY KEY (map_id, user_id)
);

CREATE TABLE game.Tournament (
  tour_id         SERIAL PRIMARY KEY,
  tour_name       varchar(40) NOT NULL,
  icon            varchar(100) NOT NULL,
  start_time      date NOT NULL,
  end_time        date NOT NULL
);

CREATE TABLE game.ParticipantScore (
  tour_id         int REFERENCES game.Tournament(tour_id) NOT NULL,
  play_id         int REFERENCES game.Score(play_id) NOT NULL
);

CREATE TABLE game.TourMap (
  tour_id         int REFERENCES game.Tournament(tour_id) NOT NULL,
  diff_id         int REFERENCES game.Difficulty(diff_id) NOT NULL,
  map_order       int,
  PRIMARY KEY (tour_id, diff_id)
);

CREATE TABLE game.Follower (
  user_id         int REFERENCES game.UserProfile(user_id) NOT NULL,
  follow_id       int REFERENCES game.UserProfile(user_id) NOT NULL,
  accept_time     timestamp,
  PRIMARY KEY (user_id, follow_id)
);