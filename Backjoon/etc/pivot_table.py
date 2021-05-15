# .pivot : 데이터 테이블 재배치(구조 변경)
# - 1개 이상의 column을 index, values, columns 값으로 사용 가능하다
# - Group 연산, 테이블 요약, 그래프 등을 위해 사용할 수 있다
# - set_index 로 계층적 색인 생성 후, unstack method로 형태를 변경하는 과정의 축약형이다


# pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, margins_name='All')
# data: 분석할 데이터프레임 (메서드일 때는 필요하지 않음)
# values: 분석할 데이터프레임에서 분석할 열
# index: 행 인덱스로 들어갈 키 열 또는 키 열의 리스트
# columns: 열 인덱스로 들어갈 키 열 또는 키 열의 리스트
# aggfunc: 분석 메서드
# fill_value: NaN 대체 값
# margins: 모든 데이터를 분석한 결과를 오른쪽과 아래에 붙일지 여부
# margins_name: 마진 열(행)의 이름


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


print("--------------------------")

data = {
    "도시": ["서울", "서울", "서울", "부산", "부산", "부산", "인천", "인천"],
    "연도": ["2015", "2010", "2005", "2015", "2010", "2005", "2015", "2010"],
    "인구": [9904312, 9631482, 9762546, 3448737, 3393191, 3512547, 2890451, 263203],
    "지역": ["수도권", "수도권", "수도권", "경상권", "경상권", "경상권", "수도권", "수도권"]
}
columns = ["도시", "연도", "인구", "지역"]
df1 = pd.DataFrame(data, columns=columns)
print(df1)

print("--------------------------")

print(df1.set_index(["도시", "연도"])[["인구"]].unstack())

print("--------------------------")

print(df1["인구"].groupby([df1["지역"], df1["연도"]]).sum().unstack("연도"))

print("--------------------------")

print(df1.pivot_table("인구", "도시", "연도", margins=True, margins_name="합계"))