from company_app.models import Job
from haystack import indexes
 
 
class JobIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    job_name = indexes.CharField(model_attr='job_name')
    location = indexes.CharField(model_attr='location')
    skills_req = indexes.CharField(model_attr='skills_req')
    description = indexes.CharField(model_attr='description')
    requirements = indexes.CharField(model_attr='requirements')
    benifits = indexes.IntegerField(model_attr='benifits')
    
    def get_model(self):
        return Job
 
    def index_queryset(self, using=None):
        return self.get_model().objects.all()