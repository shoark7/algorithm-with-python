# 파일 합치기

### 문제 링크 : https://www.acmicpc.net/problem/11066
### Date : 2017/12/03

<br>

동적 계획법을 활용해 파일 합치기 문제를 해결해보자. 사이트에서 정답률은 53% 정도이다. 

문제의 핵심을 이해하기 위한 유사코드를 작성하자.  
가령 우리가 총 4개의 파일을 합쳐야 한다면(a + b + c + d) 총비용은 다음과 같이 나타낼 수 있을 것이다.  

```python
merge_files(a+b+c+d) = min( 
			merge_files(a) + merge_files(b+c+d),
		     	merge_files(a+b) + merge_files(c+d),
		     	merge_files(a+b+c) + merge_files(d)
			)
		     + cost(a) + cost(b) + cost(c) + cost(d)
```

`merge_files`는 작성할 함수의 이름이다.  
**부분문제의 합의 최소값에 각 파일의 순수 비용을 추가해주면 전체 비용을 추산할 수 있다.**  
이때, `merge_files`와 `cost`를 구분했다는 것을 확인해야 한다.  

`merge_files`라는 함수에서는 부분문제들의 비용을 계산하기 위해 2차원 매트릭스를 사용한다.    
그런데 **파일이 1개일 때는** 파일을 합치기 위한 추가비용이 발생하지 않는다.  

예를 들어 2개의 파일을 더할 때 a와 b 각각의 합치기 비용은 0이라서 a와 b의 순수한 비용만 더하면 된다.  
(1개의 파일을 합친다는 개념 자체가 성립하니까..)  

그런데 ((a + b) + c)에서는 파일의 개수가 2인 부분문제 (a + b)의 합치기 비용이 존재하기 때문에  
전체 비용은 2a + 2b + c가 된다.  

**다시 말해 매트릭스에서 파일의 개수가 1개인 부분문제의 비용은 0으로 기입해야 한다.**


만약 5개의 파일을 합칠 때의 매트릭스는 최종적으로 다음과 같을 것이다.

<Br>

부분문제 개수 | 1  | 2  | 3 | 4 | 5
-------|-------|-------|--------|--------|-------
0개 | . | . | . | . | .
1개 | 0 | 0 | 0 | 0 | 0
2개 | a+b | b+c | c+d | d+e | .
3개 | a+b+c | b+c+d | c+d+e | . | .
4개 | a+b+c+d | b+c+d+e | . | . | .
5개 | a+b+c+d+e | . | . | . | .


**여기서 더하기 수식은 말 그대로 더하기 연산이 아니라 식을 통해 구한 비용이라는 것을 잊지 말자**  
전체 코드는 다음과 같다.

<br>


```python
def merge_files(files):
    import math
    length = len(files)
    total_list = [[math.inf for _ in range(length)] for _ in range(length+1)]
    total_list[:2] = [[0 for _ in range(length)] for _ in range(2)
    for i in range(2, len(total_list)):
        for j in range(length-i+1):
	    for k in range(1, i):
	        total_list[i][j] = min(total_list[i][j],
				      total_list[k][j] + total_list[i-k][j+k])
	    total_list[i][j] += sum(files[j:j+1])
    return total_list[length][0]

n = int(input())
for _ in range(n):
    input()
    files = [int(x) for x in input().split()]
    print(merge_files(files))
```

사실 성능은 좋지 않았다. 파이썬의 문제일지, 나의 문제일지...
