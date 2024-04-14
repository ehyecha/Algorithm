#출처: https://school.programmers.co.kr/learn/courses/30/lessons/131536
#문제: 코딩테스트 연습 > SELECT >재구매가 일어난 상품과 회원 리스트 구하기

SELECT user_id, product_id from online_sale group by user_id, product_id  
having count(*) > 1 order by user_id asc,  product_id desc