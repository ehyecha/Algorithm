#출처: https://school.programmers.co.kr/learn/courses/30/lessons/299310
#문제: 코딩테스트 연습 > SUM, MAX, MIN > 연도별 대장균 크기의 편차 구하기 


with T1(maxc, year1) as (select max(SIZE_OF_COLONY) as maxc, YEAR(DIFFERENTIATION_DATE)  as year1  from ECOLI_DATA group by year1)

select year(differentiation_date) as year, abs(size_of_colony - T1.maxc) as year_dev, id from ecoli_data join T1 on year(ecoli_data.differentiation_date) = T1.year1
order by year, year_dev asc;