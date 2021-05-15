# .pivot : 데이터 테이블 재배치(구조 변경)
# - 1개 이상의 column을 index, values, columns 값으로 사용 가능하다
# - Group 연산, 테이블 요약, 그래프 등을 위해 사용할 수 있다
# - set_index 로 계층적 색인 생성 후, unstack method로 형태를 변경하는 과정의 축약형이다

import pandas as pd

df = pd.DataFrame([
    ['20210501', 'C', 1000],
    ['20210501', 'A', 2000],
    ['20210502', 'B', 1500],
    ['20210502', 'A', 5000],
    ['20210503', 'C', 500],
    ['20210503', 'A', 3000],
], columns=['date', 'name', 'score'])

print(df)

print("--------------------------")

df_pivoted1 = df.pivot(index='date', columns='name', values='score')

df_pivoted2 = df_pivoted1.copy()
df_pivoted2.columns = df_pivoted2.columns.values
df_pivoted2.reset_index(level=0, inplace=True)

print(df_pivoted2)