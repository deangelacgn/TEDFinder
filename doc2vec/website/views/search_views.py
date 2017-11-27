from .modules import *
from website.doc2vec_model.document_similarity import *
from django.contrib.staticfiles import finders

class SearchView(View):
    transcripts_url = "data/transcripts.csv"

    def post(self, request, *args, **kwargs):
        print(request.POST)
        keyword = request.POST.get('keyword')

        if keyword:
            result = finders.find(self.transcripts_url)
            searched_locations = finders.searched_locations
            print("LOCATIONS: %s"%searched_locations)

            if len(searched_locations) > 0:
                transcripts_path = "%s/%s"%(searched_locations[0], self.transcripts_url)
                print(transcripts_path)
                dataframe = read_data(transcripts_path)
                print("DATA FRAME: %s"%dataframe)
                video_id = tf_idf(keyword, dataframe, 'transcript')
                video_url = dataframe.loc[video_id, 'url']
                print("VID: %s, url: %s"%(video_id, video_url))

                context = { 'video': video_url }

                return JsonResponse(context)

        return HttpResponse(status=400)
