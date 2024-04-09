#출처: https://school.programmers.co.kr/learn/courses/30/lessons/298518
#문제: 코딩테스트 연습 > GROUP BY >월별 잡은 물고기 수 구하기

select  count(*) as "fish_count", MONTH(time) as "month" from fish_info group by MONTH(time) order by month;

#출처: https://school.programmers.co.kr/learn/courses/30/lessons/298518
#문제: 코딩테스트 연습 > SELECT >특정 물고기를 잡은 총 수 구하기

select count(*) as FISH_COUNT from fish_info as a
left join fish_name_info as b on a.fish_type = b.fish_type where fish_name in ('BASS','SNAPPER')