PRAGMA FOREIGN_KEYS = ON;

DROP TABLE attending;
DROP TABLE memberships;
DROP TABLE members;
DROP TABLE classes;

CREATE TABLE memberships (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    level VARCHAR(6) NOT NULL,
    description VARCHAR
);

CREATE TABLE members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    membership_id INTEGER NOT NULL,
    FOREIGN KEY (membership_id) REFERENCES memberships(id)
);

CREATE TABLE classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(30) NOT NULL,
    capacity INTEGER NOT NULL,
    time DATETIME NOT NULL
);

CREATE TABLE attending (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    member_id INTEGER NOT NULL,
    class_id INTEGER NOT NULL,
    FOREIGN KEY (member_id) REFERENCES members(id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE CASCADE
);