import pandas as pd

from django.db.models import Sum, F
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Deals
from .serializers import DealsSerializer, ClientsSerializer


class CsvView(APIView):
    def post(self, request):
        file = request.FILES['file']
        df = pd.read_csv(file)
        for index, row in df.iterrows():
            data = {
                'customer': row.get('customer'),
                'item': row.get('item'),
                'total': row.get('total'),
                'quantity': row.get('quantity'),
                'date': row.get('date'),
            }
            serializer = DealsSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                deal_saved = serializer.save()
            else:
                return Response({'Status': f'Error, Desc: {serializer.error_messages}'})
        return Response({'Status': 'OK'})

    def get(self, request):
        """
        get top 5 more spent clients and return only names
        :param request:
        :return:
        """
        data = Deals.objects.annotate(
            username=F('customer')
        ).values(
            'username'
        ).distinct().annotate(
            spent_money=Sum('total')
        ).order_by(
            '-spent_money'
        )[:5].values('username', 'spent_money')
        # get clients
        clients = data.values_list('username', flat=True)
        # get gems of top 5 clients
        gems = Deals.objects.filter(
            customer__in=clients
        ).values(
            'customer',
            'item'
        ).order_by('item').distinct().values('item')
        # get gems which buy 2 min clients
        client_list = list()
        for client in data:
            user = client['username']
            spent_money = client['spent_money']
            gems_without_client = gems.exclude(customer=user)
            gems_per_user = Deals.objects.filter(customer=user).values('item').distinct()
            gems_filtered = gems_without_client.filter(item__in=gems_per_user).values_list('item', flat=True)
            new_gems = gems_filtered.annotate(gems=F('item')).values_list('gems', flat=True)
            client_json = {
                'username': client['username'],
                'spent_money': spent_money,
                'gems': list(new_gems)
            }
            client_json_serialize = ClientsSerializer(data=client_json)
            client_json_serialize.is_valid()
            client_list.append(client_json_serialize.data)
        return Response(
            {
                'response': client_list
            }
        )
