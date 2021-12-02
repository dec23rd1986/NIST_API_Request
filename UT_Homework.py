import requests
import json
import pprint

url = "https://services.nvd.nist.gov/rest/json/cve/1.0/CVE-2021-40463/"
params = {"q": "CVE"}
response = requests.get(url, params)

data = json.loads(response.content)
cveID = (data['result']['CVE_Items'][0]['cve']['CVE_data_meta']['ID'])
refURL = (data['result']['CVE_Items'][0]['cve']['references']['reference_data'][0]['url'])
desData = (data['result']['CVE_Items'][0]['cve']['description']['description_data'][0]['value'])
severity = (data['result']['CVE_Items'][0]['impact']['baseMetricV2']['severity'])


pprint.pprint(f'CVE ID: {cveID}')
pprint.pprint(f'Reference URL: {refURL}')
pprint.pprint(f'Description: {desData}')
pprint.pprint(f'Severity: {severity}')
