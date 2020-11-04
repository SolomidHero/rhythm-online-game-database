# Rhythm online game database
Example of normalised database for rhythm online game like 'osu!'

## Prerequisites

Any SQL-based database. All scripts were tested with PostgreSQL

## Installation

Most important files are `db.sql`, `data_fill.sql`.

First build the database using `db.sql`, then fill it up using `data_fill.sql`.

You can drop the database using `db_drop.sql` script.

Use `queries.sql` to see example of sql queries to the database.

## More

Files here are not used, but provided for better understanding how data was generated

- `gen.py` was used to generate random data for different tables
- `gen_text.txt` and `rate_text.txt` used for data generation too


