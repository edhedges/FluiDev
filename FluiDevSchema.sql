--- Table Creation ---
CREATE TABLE IF NOT EXISTS FluiDevWebsite (
    website_id integer primary key autoincrement not null,
    website_name text,
    website_path text,
    date_created date,
    date_edited date
);