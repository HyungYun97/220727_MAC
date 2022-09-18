-- 코드를 입력하세요
SELECT COUNT(DISTINCT(NAME)) AS '중복 제거하기'
FROM ANIMAL_INS
where NAME IS NOT NULL;

level 2 