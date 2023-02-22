SELECT * FROM recipes;
--- 
INSERT INTO recipes (name, description, instructions, date, under_30, user_id) 
VALUES ('baked pie', 'very hot pies', 'cook with assistant', '2022-03-24', 1, '1');
--  

UPDATE recipes
SET 
name = "bob",
description = "eijueiudeuidbwuiebduwibd",
instructions = "iujnediuwenduiwndiubewuid",
date = "2022-12-23",
under_30 = 1
WHERE id = 1;