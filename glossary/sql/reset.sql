BEGIN;
DELETE FROM "glossary_term";
DELETE FROM "glossary_termtype";
DELETE FROM "glossary_subdomein";
DELETE FROM "glossary_context";
DELETE FROM "glossary_domein";
UPDATE "sqlite_sequence" SET "seq" = 0 WHERE "name" IN ( 'glossary_term', 'glossary_termtype', 'glossary_subdomein', 'glossary_context', 'glossary_domein');
COMMIT;