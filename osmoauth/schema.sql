DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS group;
DROP TABLE IF EXISTS event;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
);

CREATE TABLE group (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  m_id INTEGER NOT NULL,
  m_name TEXT NOT NULL,
  m_status TEXT NOT NULL,
  m_link TEXT NOT NULL,
  m_urlname TEXT NOT NULL,
  m_description TEXT NOT NULL,
  m_created TIMESTAMP NOT NULL,
  m_city TEXT NOT NULL,
  m_unstranslated_city TEXT NOT NULL,
  m_country TEXT NOT NULL,
  m_localized_country_name TEXT NOT NULL,
  m_localized_location TEXT NOT NULL,
  m_region2 TEXT NOT NULL,
  m_state TEXT NOT NULL,
  m_join_mode TEXT NOT NULL,
  m_visibility TEXT NOT NULL,
  m_lat REAL NOT NULL,
  m_lon REAL NOT NULL,
  m_members INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE event (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  group_id INTEGER NOT NULL,
  access_token TEXT NOT NULL,
  m_created TIMESTAMP NOT NULL,
  m_duration INTEGER NOT NULL,
  m_id INTEGER NOT NULL,
  m_name TEXT NOT NULL,
  m_rsvp_limit INTEGER NOT NULL,
  m_date_in_series_pattern INTEGER NOT NULL,
  m_status INTEGER NOT NULL,
  m_time TIMESTAMP NOT NULL,
  m_local_date TEXT NOT NULL,
  m_local_time TEXT NOT NULL,
  m_updated TIMESTAMP NOT NULL,
  m_utc_offset INTEGER NOT NULL,
  m_waitlist_count INTEGER NOT NULL,
  m_yes_rsvp_count INTEGER NOT NULL,
  m_venue_name TEXT NOT NULL,
  m_venue_lat REAL NOT NULL,
  m_venue_lon REAL NOT NULL,
  m_venue_repinned INTEGER NOT NULL,
  m_venue_address_1 TEXT NOT NULL,
  m_venue_city TEXT NOT NULL,
  m_venue_country TEXT NOT NULL,
  m_venue_localized_country_name TEXT NOT NULL,
  m_venue_zip TEXT NOT NULL,
  m_venue_state TEXT NOT NULL,
  m_link TEXT NOT NULL,
  m_description TEXT NOT NULL,
  m_visibility TEXT NOT NULL,
  m_member_pay_fee INTEGER NOT NULL
);