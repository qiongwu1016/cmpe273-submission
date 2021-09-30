BEGIN;
-- INSERT INTO students values(450, 'Zusio', 'Zap', 'ABC333341', 'zus@mao.com', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
-- INSERT INTO students values(451, 'Puee', 'Saee', 'ASS330554', 'puee@mao.com', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
-- DELETE FROM students WHERE id=440;
UPDATE students SET email='morning@gmail.com' WHERE id=450;
COMMIT;
