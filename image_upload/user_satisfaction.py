import pandas as pd
import numpy as np

bakery_df = pd.read_csv(r"C:\PYWork\myproject10\image_upload\data\bakery_total_20240412.csv")  # ──────── 경로 지정 필수 (박용빈)

def user_satisfaction_rate(df):
    # 데이터 유형 변환
    df['visitors_number'] = df['visitors_number'].astype(float)
    df['rating'] = df['rating'].astype(float)

    # NaN 값 처리
    # NaN 값을 0으로 대체 하거나 다른 값으로 대체 가능
    df['rating'] = df['rating'].fillna(0)
    df.loc[:, 'visitors_number'] = df['visitors_number'].fillna(0)
    # 사용자 만족도 계산
    df['user_satisfaction'] = np.log1p(df['rating']) * np.log1p(df['visitors_number'])
    df = df[~((df['rating'] == 0) & (df['visitors_number'] == 0))]  # ────────── 둘 다 0인 값 목록 에서 제거 (박용빈)

    # 사용자 만족도 정렬
    recommended_bakery = df.sort_values(by='user_satisfaction', ascending=False)
    return recommended_bakery

recommended_bakery = user_satisfaction_rate(bakery_df)
print(recommended_bakery)
def filter_pet_friendly(df):
    # 애견동반 필터링
    pet_friendly_df = df[df['with'] == '애견동반']
    # 사용자 만족도 정렬
    recommended_pet_friendly = pet_friendly_df.sort_values(by='user_satisfaction', ascending=False)
    return recommended_pet_friendly

recommended_pet_friendly = filter_pet_friendly(recommended_bakery)
print(recommended_pet_friendly)

# def get_user_satisfaction_recommended(csv_path):
#     bakery_df = pd.read_csv(csv_path)
#     df = bakery_df.copy()
#     df['visitors_number'] = df['visitors_number'].astype(float)
#     df['rating'] = df['rating'].astype(float)
#     # NaN 값을 0으로 대체하거나 다른 값으로 대체 가능
#     df.loc[:, 'rating'] = df['rating'].fillna(0)
#     df.loc[:, 'visitors_number'] = df['visitors_number'].fillna(0)  # ────────── NaN 값 보기 싫어서 수정 (박용빈)
#     df = df[~((df['rating'] == 0) & (df['visitors_number'] == 0))]  # ────────── 둘 다 0인 값 리스트에서 제거 (박용빈)
#
# # ──────────────────────────────────────────────── 변경 ( 박용빈 )
#     # 사용자 만족도 계산
#     df.loc[:, 'user_satisfaction'] = np.log1p(df['rating']) * np.log1p(df['visitors_number'])
#     # 사용자 만족도를 기준으로 정렬
#     df.sort_values(by='user_satisfaction', ascending=False, inplace=True)
#     # 선택한 컬럼만 포함하는 딕셔너리로 변환
#     recommended_bakeries = df[['store_name', 'mart_cate', 'tel', 'address', 'link']].to_dict('records')
#     return recommended_bakeries
#
# if __name__ == '__main__':
#     csv_file_path = r"C:\Users\binny\Desktop\bakery_total_20240412.csv"
#     recommended_bakeries = get_user_satisfaction_recommended(csv_file_path)
#     print(recommended_bakeries)
