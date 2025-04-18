--
-- Файл сгенерирован с помощью SQLiteStudio v3.3.3 в Пт апр 18 16:11:12 2025
--
-- Использованная кодировка текста: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: sites
CREATE TABLE sites (
	id INTEGER NOT NULL, 
	name VARCHAR(100), 
	url VARCHAR(200), 
	filename VARCHAR(100), 
	PRIMARY KEY (id), 
	UNIQUE (name), 
	UNIQUE (url), 
	UNIQUE (filename)
);
INSERT INTO sites (id, name, url, filename) VALUES (1, 'На все случаи', 'https://navsl.ru/', 'navsl.xml');
INSERT INTO sites (id, name, url, filename) VALUES (2, 'Профиль 21', 'https://profil21.ru/', 'profil21.xml');
INSERT INTO sites (id, name, url, filename) VALUES (3, 'Промкух', 'https://promkuh.ru/', 'promkuh.xml');
INSERT INTO sites (id, name, url, filename) VALUES (4, 'Основа', 'https://osnovarest.ru/', 'osnova.xml');

-- Индекс: ix_sites_id
CREATE INDEX ix_sites_id ON sites (id);

-- Индекс: sqlite_autoindex_sites_1
CREATE INDEX sqlite_autoindex_sites_1 ON sites (name COLLATE BINARY);

-- Индекс: sqlite_autoindex_sites_2
CREATE INDEX sqlite_autoindex_sites_2 ON sites (url COLLATE BINARY);

-- Индекс: sqlite_autoindex_sites_3
CREATE INDEX sqlite_autoindex_sites_3 ON sites (filename COLLATE BINARY);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
