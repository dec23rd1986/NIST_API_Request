import requests
import json
import pprint

url = "https://services.nvd.nist.gov/rest/json/cves/1.0/?pubStartDate=2021-09-01T13:00:00:000 UTC-05:00&pubEndDate=2021-11-30T13:36:00:000 UTC-05:00"
params = {"q": "CVE"}
response = requests.get(url, params)

data = json.loads(response.content)
cvssV3Severity = (data['result']['CVE_Items'][0]['impact']['baseMetricV3']['cvssV3']['baseSeverity'])


pprint.pprint(len(cvssV3Severity))