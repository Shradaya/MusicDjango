from django.shortcuts import render
from playlist.models import videoUpload, Order
import xml.etree.ElementTree as ET
from django.shortcuts import redirect
from django.db import connection
import requests

# Create your views here.

def EsewaVerifyView(request):
    oid_vid=request.GET.get("oid")
    amt=request.GET.get("amt")
    refId=request.GET.get("refId")
    url ="https://uat.esewa.com.np/epay/transrec"
    pid = oid_vid.split('-')[1]
    oid = oid_vid.split('-')[0]
    d = {
    'amt': amt,
    'scd': 'EPAYTEST',
    'rid': refId,
    'pid':oid_vid,
    }

    resp = requests.post(url, d)
    root = ET.fromstring(resp.content)
    status = root[0].text.strip()
    if status == 'Success':
        p = Order(orderID=oid, userID= request.user.id, videoID= pid)
        p.save()
        return redirect("/")
    else:
        return redirect("/")
