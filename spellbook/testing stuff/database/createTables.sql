CREATE TABLE IF NOT EXISTS "player" (
	"id"			INTEGER NOT NULL UNIQUE,
	"discord_id"	INTEGER NOT NULL UNIQUE,
	"char_name"		TEXT NOT NULL UNIQUE,
	"wizard_school"	TEXT NOT NULL,
	"wizard_level"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "spell" (
	"id"			INTEGER NOT NULL UNIQUE,
	"name"			TEXT NOT NULL UNIQUE,
	"school"		TEXT NOT NULL,
	"level"			INTEGER NOT NULL,
	"isDunamancy"	INTEGER NOT NULL DEFAULT 0,
	"isValid"		INTEGER NOT NULL DEFAULT 1,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "player_spell" (
	"id"		INTEGER NOT NULL UNIQUE,
	"player"	INTEGER NOT NULL,
	"spell"		INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("player") REFERENCES "player"("id"),
	FOREIGN KEY("spell") REFERENCES "spell"("id"),
	UNIQUE("player","spell")
);