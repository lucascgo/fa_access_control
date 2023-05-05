# from django.shortcuts import render
# import requests
from django.http import HttpResponse
from fa_access_control.settings import CNPJ, METHOD, MASTER
from .models import Code
import base64
from .utils import data


def heartbeat(request):
    if request.method == 'GET':
        key = request.GET.get('Key')
        data = 'DATA={"Key":"' + key + '"}'
        return HttpResponse(data)


def qrcode(request):
    if request.method == 'GET':
        code_base64 = request.GET.get('Card')
        code_decode = base64.b64decode(code_base64).decode('utf-8')
        qrcode_full = code_decode[43:]
        qrcode_cnpj = code_decode[43:67]

        if code_decode == MASTER:
            res = data('open')
        elif qrcode_cnpj == CNPJ:
            if METHOD == 'unique':
                if Code.objects.filter(qrcode=qrcode_full).count() == 0:
                    Code(qrcode=qrcode_full).save()
                    res = data('open')
                else:
                    res = data('reject')
            else: 
                res = data('open')
        else:
            res = data('reject')

    return HttpResponse(res)

    # response = requests.get('http://192.168.0.180/cdor.cgi?open=1&door=1', headers={'Authorization': 'Basic YWRtaW46ODg4ODg4'})
    # return HttpResponse("Hello, world. You're at the polls index.")
