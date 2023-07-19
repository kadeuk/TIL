```sql
SELECT 열 이름
	FROM 테이블 이름
	WHERE 조건식
	GROUP BY 열 이름
	HAVING 조건식
	ORDER BY 열이름 DESC
	LIMIT 숫자
```
- **순서가 달라지면 안된다** 
ex) where 조건식 from 테이블이름 이러면 안된다.
- order by: 기본은 `asc;`로 오름차순이다. 내림차순은 `desc;`
- limit: pandas의 head()와 같다 앞에서 몇줄을 볼것인가.
	- limit 3, 2; : 3번째 이후부터 2개 그러니까 4, 5번째를 보여준다
- select distinct 컬럼: 중복된 컬럼을 하나씩만 보여준다.