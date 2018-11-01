from django.utils import timezone # import datetime
from django.shortcuts import render, redirect

import requests
from bs4 import BeautifulSoup as bs

from .models import SearchResult, Movie

# 5. Views 작성
def search_movie(request, keyword=None):
    print(keyword)
    # 크롤링
    if request.method == "POST":
        keyword = request.POST['keyword']
        if not keyword:
            return redirect('search')
        
        results = SearchResult.objects.filter(keyword=keyword).order_by('-search_date')
        if results:
            recent = results[0]
            if recent.search_date - timezone.now() < timezone.timedelta(days=1):
                return redirect('search-result', keyword=keyword)

        i = 1
        search_result = SearchResult.objects.create(
            keyword = keyword
        )
        while True:
            print("크롤링 시작")
            url = "http://www.cgv.co.kr/search/movie.aspx?query={}&page={}".format(keyword, i)
            response = requests.get(url)
            result = bs(response.text, "html.parser")
            
            try:
                ul = result.find('div', {'class': 'sect-chart'}).ul

                for li in ul.findAll("li"):
                    Movie.objects.create(
                        name = li.find('strong').text,
                        img_url = li.img['src'],
                        release_date = '-'.join(li.i.text.split('.')),
                        search_result = search_result
                    )
                i += 1
            except AttributeError:
                break
        return redirect('search-result', keyword=keyword)

    # GET메소드 redirect된 경우, keyword가 있는 경우
    if keyword:
        result = SearchResult.objects.filter(keyword=keyword).order_by('-search_date')
        if result and result[0].movie_set.all():
            return render(request, 'search.html', {'result': result[0]})
        else:
            return render(request, 'search.html', {'result': False})

    # GET메소드
    return render(request, 'search.html')