import pygal

from chp.models import Complain
from users.models import Profile
from django.db.models import Count


class DeptComplainBarChart():

    def __init__(self, **kwargs):
        self.chart = pygal.Bar(**kwargs)
        self.chart.title = 'Department wise Complain Chart'

    def get_data(self):
        '''
        Query the db for chart data, pack them into a dict and return it.
        '''
        cd = 'complain_department'
        q2 = Complain.objects.values(cd).order_by(cd).annotate(count = Count(cd))
        data = {q.get('complain_department'): q.get('count') for q in q2}
        return data

    def generate(self):
        # Get chart data
        chart_data = self.get_data()

        # Add data to chart
        for key, value in chart_data.items():
            self.chart.add(key, value)

        # Return the rendered SVG
        return self.chart.render(is_unicode=True)




class ResidenceComplainPieChart():

    def __init__(self, **kwargs):
        self.chart = pygal.Pie(**kwargs)
        self.chart.title = 'Residence wise Complain Chart'

    def get_data(self):
        '''
        Query the db for chart data, pack them into a dict and return it.
        '''
        
        q2 = Complain.objects.values('complain_user__profile__residence').annotate(count=Count('id'))
        data = {q.get('complain_user__profile__residence'): q.get('count') for q in q2}
        return data

    def generate(self):
        # Get chart data
        chart_data = self.get_data()

        # Add data to chart
        for key, value in chart_data.items():
            self.chart.add(key, value)

        # Return the rendered SVG
        return self.chart.render(is_unicode=True)

class StatusComplainBarChart():

    def __init__(self, **kwargs):
        self.chart = pygal.Bar(**kwargs)
        self.chart.title = 'Status wise Complain Chart'

    def get_data(self):
        '''
        Query the db for chart data, pack them into a dict and return it.
        '''
        d = 'status'
        q2 = Complain.objects.values(d).order_by(d).annotate(count = Count(d))
        data = {q.get('status'): q.get('count') for q in q2}
        return data

    def generate(self):
        # Get chart data
        chart_data = self.get_data()

        # Add data to chart
        for key, value in chart_data.items():
            self.chart.add(key, value)

        # Return the rendered SVG
        return self.chart.render(is_unicode=True)