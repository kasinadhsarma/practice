-- ============================================================
-- Set operations: UNION, UNION ALL, INTERSECT, EXCEPT
-- ============================================================
-- Combine the results of two SELECT statements as if they were sets.
-- Both sides must return the same number of columns with compatible types.
--
--   UNION      — rows from either query, DUPLICATES REMOVED
--   UNION ALL  — rows from either query, duplicates KEPT (faster)
--   INTERSECT  — only rows that appear in BOTH queries
--   EXCEPT     — rows from the first query that do NOT appear in the second
-- ============================================================

CREATE TABLE this_year (name TEXT);
CREATE TABLE last_year (name TEXT);

INSERT INTO this_year (name) VALUES ('Alice'), ('Bob'), ('Carol');
INSERT INTO last_year (name) VALUES ('Bob'), ('Carol'), ('Dave');

-- UNION: everyone active in either year, no duplicates
SELECT name FROM this_year
UNION
SELECT name FROM last_year
ORDER BY name;

-- UNION ALL: same, but Bob and Carol appear twice (once per table)
SELECT name FROM this_year
UNION ALL
SELECT name FROM last_year
ORDER BY name;

-- INTERSECT: active in BOTH years
SELECT name FROM this_year
INTERSECT
SELECT name FROM last_year
ORDER BY name;

-- EXCEPT: new this year (active this year but NOT last year)
SELECT name FROM this_year
EXCEPT
SELECT name FROM last_year
ORDER BY name;

-- EXCEPT (other direction): churned (active last year but NOT this year)
SELECT name FROM last_year
EXCEPT
SELECT name FROM this_year
ORDER BY name;
