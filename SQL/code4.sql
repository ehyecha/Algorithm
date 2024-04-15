#출처: https://school.programmers.co.kr/learn/courses/30/lessons/299308
#문제: 코딩테스트 연습 > String, Date > 분기별 분화된 대장균의 개체 수 구하기


select  concat(QUARTER(DIFFERENTIATION_DATE), "Q") as QUARTER,  
count(*) as ECOLI_COUNT from ecoli_data group 
by QUARTER order by QUARTER ASC;