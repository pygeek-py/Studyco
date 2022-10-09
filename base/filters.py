import django_filters
from django_filters import CharFilter
from django_filters import filters

from .models import box, movieimg

class boxfilter(django_filters.FilterSet):
    topic = CharFilter(field_name="topic", lookup_expr="icontains")
    
    class Meta:
        model = box
        fields = '__all__'
        exclude = ['host', 'person', 'name', 'description', 'based', 'date']

 
class userfilter(django_filters.FilterSet):
	bio = CharFilter(field_name="bio", lookup_expr="icontains")

	class Meta:
		model = movieimg
		fields = '__all__'
		exclude = ['img', 'user']  