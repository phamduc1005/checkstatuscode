from httpcore import request
from flask import Flask, json, request
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)
@app.route('/check-website-status', methods=['POST', 'GET']) 
def testUrlsFromSitemaps():
    def getUrlsFromSitemap(xmlUrl):
        r = requests.get(xmlUrl)
        xml = r.text
        soup = BeautifulSoup(xml)

        links = []
        for link in soup.findAll('loc'):
            linkStr = link.getText('', True)
            links.append(linkStr)
        return links
    
    if request.method == 'POST':
        inputXmlUrls = request.form.get('site')
    else:
        inputXmlUrls = request.args.get('site')
    
    
    if inputXmlUrls == 'pmp':
        xmlUrls = ['https://pmp-testprep.com/post-sitemap.xml', 'https://pmp-testprep.com/page-sitemap.xml']
    elif inputXmlUrls == 'cna':
        xmlUrls = ['https://cna-prep.com/post-sitemap.xml', 'https://cna-prep.com/page-sitemap.xml']
    elif inputXmlUrls == 'aws':
        xmlUrls = ['https://aws-prep.com/post-sitemap.xml', 'https://aws-prep.com/page-sitemap.xml']
    elif inputXmlUrls == 'drivingtheory':
        xmlUrls = ['https://drivingtheory-tests.com/post-sitemap.xml', 'https://drivingtheory-tests.com/page-sitemap.xml']
    elif inputXmlUrls == 'ged':
        xmlUrls = ['https://ged-testprep.com/post-sitemap.xml', 'https://ged-testprep.com/page-sitemap.xml']
    elif inputXmlUrls == 'ptce':
        xmlUrls = ['https://ptceprep.com/post-sitemap.xml', 'https://ptceprep.com/page-sitemap.xml']
    elif inputXmlUrls == 'realestate':
        xmlUrls = ['https://realestate-prep.com/post-sitemap.xml', 'https://realestate-prep.com/page-sitemap.xml']
    elif inputXmlUrls == 'teas':
        xmlUrls = ['https://teas-prep.com/post-sitemap.xml', 'https://teas-prep.com/page-sitemap.xml']
    elif inputXmlUrls == 'servsafe':
        xmlUrls = ['https://servsafe-prep.com/post-sitemap.xml', 'https://servsafe-prep.com/page-sitemap.xml']
    else:
        xmlUrls = ['https://servsafe-prep.com/post-sitemap.xml', 'https://servsafe-prep.com/page-sitemap.xml']
    # xmlUrls.append(inputXmlUrls)
    listError = []
    print(xmlUrls)
    
    for xmlUrl in xmlUrls:
        links = getUrlsFromSitemap(xmlUrl)
        print(links)
        for link in links:
            response = requests.get(link)
            statusCode = response.status_code
            print(statusCode)
            if statusCode not in range(200, 300):
                listError.append(link)
    if len(listError) > 0:        
        return json.dumps(listError)
    else:
        return 'All is good'

if __name__ == '__main__':
    app.run()
