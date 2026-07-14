USE streaming_analytics;

INSERT INTO user_listening_history
(user_id, timestamp, song, artist, session_id, duration)
VALUES
(1001, toTimestamp(now()), 'Bohemian Rhapsody', 'Queen', 5001, 5.55);

INSERT INTO user_listening_history
(user_id, timestamp, song, artist, session_id, duration)
VALUES
(1002, toTimestamp(now()), 'Hey Jude', 'The Beatles', 5002, 7.11);

INSERT INTO user_listening_history
(user_id, timestamp, song, artist, session_id, duration)
VALUES
(1003, toTimestamp(now()), 'Stairway to Heaven', 'Led Zeppelin', 5003, 8.02);

UPDATE current_top_songs
SET play_count = play_count + 1
WHERE date = toDate(now())
AND song = 'Bohemian Rhapsody';

UPDATE current_top_songs
SET play_count = play_count + 1
WHERE date = toDate(now())
AND song = 'Hey Jude';

UPDATE current_top_songs
SET play_count = play_count + 1
WHERE date = toDate(now())
AND song = 'Comfortably Numb';

UPDATE hourly_stats
SET total_plays = total_plays + 1
WHERE hour = toTimestamp(now());

UPDATE hourly_stats
SET unique_users = unique_users + 1
WHERE hour = toTimestamp(now());

INSERT INTO user_sessions
(user_id, session_id, start_time, end_time, songs_count, total_duration)
VALUES
(1001, 5001, toTimestamp(now()), toTimestamp(now()), 1, 5.55);

INSERT INTO user_sessions
(user_id, session_id, start_time, end_time, songs_count, total_duration)
VALUES
(1002, 5002, toTimestamp(now()), toTimestamp(now()), 1, 7.11);

SELECT * FROM current_top_songs;

SELECT * FROM user_listening_history LIMIT 5;

SELECT * FROM hourly_stats;
