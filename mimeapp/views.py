from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

data = """<table>
  <tr>
    <th>Company</th>
    <th>Contact</th>
    
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
   
  </tr>
  <tr>
    <td>Centro comercial Moctezuma</td>
    <td>Francisco Chang</td>
    
  </tr>
</table>
"""
class HtmlView(View):
    def get(self,request):
        return HttpResponse(data,content_type="text/html")

class XmlView(View):
    def get(self,request):
        return HttpResponse(data,content_type="application/xml")

class ExcelView(View):
    def get(self,request):
        return HttpResponse(data,content_type="application/vnd.ms-excel")
