# server-sprint1-yongbin
Server Sprint1 yongbin

# Test
유저 데이터 100,000개 중 랜덤으로 1,000개 추출
이를 1000번씩 반복 실행 후 평균시간 추출

# Redis - default settings

|Run #|average time|
|---|---|
| Run 1  | 0.157 |
| Run 2 | 0.083 |
| Run 3 | 0.158 |

# Redis - Max mem: 1GB, LRU

|Run #|average time|
|---|---|
| Run 1  | 0.0817 |
| Run 2 | 0.077 |
| Run 3 | 0.078 |

# MySQL

|Run #|average time|
|---|---|
| Run 1  | 0.150 |
| Run 2 | 0.143 |
| Run 3 | 0.143  |
