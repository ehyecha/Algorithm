# 출처: https://school.programmers.co.kr/learn/courses/30/lessons/276034
# 문제: 코딩테스트 연습 > SELECT >조건에 맞는 개발자 찾기

SELECT ID, EMAIL, FIRST_NAME, LAST_NAME FROM DEVELOPERS
WHERE SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'Python')
    OR SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'C#')
ORDER BY ID;