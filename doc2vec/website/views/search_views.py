from .modules import *
from website.tfidf.document_similarity import *
from django.contrib.staticfiles import finders

class SearchView(View):
    transcripts_url = "data/transcripts.csv"

    def post(self, request, *args, **kwargs):
        print(request.POST)
        keyword = request.POST.get('keyword')
        min_videos = request.POST.get('min-videos')

        if keyword and min_videos:
            min_videos = int(min_videos)
            result = finders.find(self.transcripts_url)
            searched_locations = finders.searched_locations
            print("LOCATIONS: %s"%searched_locations)

            if len(searched_locations) > 0:
                transcripts_path = "%s/%s"%(searched_locations[0], self.transcripts_url)
                dataframe = read_data(transcripts_path)
                video_ids = tf_idf(keyword, dataframe, 'transcript', min_videos)
                video_urls = []

                for vid in video_ids:
                    url = dataframe.loc[vid, 'url']
                    video_urls.append(url)

                context = { 'videos': video_urls }

                return JsonResponse(context)

        return HttpResponse(status=400)
