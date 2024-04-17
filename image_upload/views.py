# Create your views here.
from django.shortcuts import render
from .forms import UploadFileForm
from . import model_handler
from django.conf import settings
from .user_satisfaction import user_satisfaction_rate, filter_pet_friendly
import pandas as pd
from django.core.paginator import Paginator

def image_search(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save()
            image_url = settings.MEDIA_URL + str(file_instance.file)
            image_tensor = model_handler.preprocess_image(file_instance.file)
            prediction_name, top_predictions = model_handler.get_prediction_from_image(
                image_tensor,
                model_handler.model_path,
                model_handler.num_classes
            )

            # 데이터 로드
            bakery_df = pd.read_csv(r"C:\PYWork\myproject10\image_upload\data\bakery_total_20240412.csv")
            # 만족도 계산
            recommended_bakery = user_satisfaction_rate(bakery_df)
            # 애견 동반 필터링
            recommended_pet_friendly = filter_pet_friendly(recommended_bakery)
            # need to convert a Pandas data frame into a list in a dictionary.
            recommended_bakery_list = recommended_bakery.to_dict('records')
            recommended_pet_friendly_list = recommended_pet_friendly.to_dict('records')
            # set Pagenator
            paginator = Paginator(recommended_bakery_list, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            context = {
                'image_url': image_url,
                'result': prediction_name,
                'top_results': top_predictions,
                'recommended_bakery': recommended_bakery_list,
                'recommended_pet_friendly': recommended_pet_friendly_list,
                'page_obj': page_obj
            }
            return render(request, 'image_upload/results.html', context)
    else:
        form = UploadFileForm()

    return render(request, 'image_upload/search.html', {'form': form})

# def image_upload(request):
#     return render(request, 'image_upload/yes.html')
# ─────────────────────────────────────────────────────────────────────── 추가
# def bakery_view(request):
#     # 데이터 로드
#     bakery_df = pd.read_csv(r"C:\Users\binny\Desktop\bakery_total_20240412.csv")
#     # 만족도 계산
#     recommended_bakery = user_satisfaction_rate(bakery_df)
#     # 애견 동반 필터링
#     recommended_pet_friendly = filter_pet_friendly(recommended_bakery)
#     context = {
#         'recommended_bakery': recommended_bakery,
#         'recommended_pet_friendly': recommended_pet_friendly
#     }
#     return render(request, 'image_upload/results.html', context)
