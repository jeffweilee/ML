#!/usr/bin/python
import json
import base64
import requests
import sqlite3
from datetime import datetime
from datetime import timedelta
import os

fileCfgPath ='cve.py.config'
defaultLastExecDate = '1980-01-01 00:00'

def addUpdateHandler():
    # 0:cve_id, 1:vendor, 2:product, 3:score, 4:severity, 5:published_date, 6:last_modified_date, 7:created_at, 8:updated_at, 9:cve_description
    sqlstatement = "select distinct cve_id, vendor, product, score, severity, strftime('%Y-%m-%d %H:%M', published_date), strftime('%Y-%m-%d %H:%M', last_modified_date), strftime('%Y-%m-%d %H:%M', created_at), strftime('%Y-%m-%d %H:%M', updated_at), cve_description from ( select js.id, js.cve_id, js.published_date, js.last_modified_date, js.created_at, js.updated_at, af.vendor, af.product, af.version, case when (c3.base_score is NULL) then c2.base_score else c3.base_score end score, case when (c3.base_severity is NULL) then c2.severity else c3.base_severity end severity, de.value as cve_description from nvd_jsons js left join cvss3 c3 on js.id = c3.nvd_json_id left join cvss2_extras c2 on js.id = c2.nvd_json_id left join affects af on js.id = af.nvd_json_id left join descriptions de on js.id = de.nvd_json_id where af.vendor in ('redhat','centos','linux') and (af.product LIKE '%linux%' or af.product LIKE '%centos%' or af.product LIKE '%redhat%') ) nvd_all where score >= 7.0 order by score desc, cve_id desc limit 6;"
    cves=query(sqlstatement)

    for cve in cves:
        isUpdated = datetime.strptime(cve['updatedAt'],'%Y-%m-%d %H:%M') > lastExecDate
        #print(isUpdated)
        if isUpdated:
            callService(cve,'add')



def deleteHandler():
    # 0:cve_id, 1:vendor, 2:product, 3:score, 4:severity, 5:published_date, 6:last_modified_date, 7:created_at, 8:updated_at, 9:cve_description
    sqlstatement = "select distinct cve_id, vendor, product, score, severity, strftime('%Y-%m-%d %H:%M', published_date), strftime('%Y-%m-%d %H:%M', last_modified_date), strftime('%Y-%m-%d %H:%M', created_at), strftime('%Y-%m-%d %H:%M', updated_at), cve_description from ( select js.id, js.cve_id, js.published_date, js.last_modified_date, js.created_at, js.updated_at, af.vendor, af.product, af.version, case when (c3.base_score is NULL) then c2.base_score else c3.base_score end score, case when (c3.base_severity is NULL) then c2.severity else c3.base_severity end severity, de.value as cve_description from nvd_jsons js left join cvss3 c3 on js.id = c3.nvd_json_id left join cvss2_extras c2 on js.id = c2.nvd_json_id left join affects af on js.id = af.nvd_json_id left join descriptions de on js.id = de.nvd_json_id where af.vendor in ('redhat','centos','linux') and (af.product LIKE '%linux%' or af.product LIKE '%centos%' or af.product LIKE '%redhat%') ) nvd_all where score < 7.0 order by score desc, cve_id desc limit 6;"
    cves=query(sqlstatement)

    for cve in cves:
        isUpdated = datetime.strptime(cve['updatedAt'],'%Y-%m-%d %H:%M') > lastExecDate
        #print(isUpdated)
        if isUpdated:
            callService(cve,'delete')



def query(sqlstatement):
    # 0:cve_id, 1:vendor, 2:product, 3:score, 4:severity, 5:published_date, 6:last_modified_date, 7:created_at, 8:updated_at, 9:cve_description
    conn = sqlite3.connect('cve.sqlite3')
    cursor = conn.cursor()
    cursor.execute(sqlstatement)
    rows = cursor.fetchall()
    cves = []
    vendors = []
    products = []
    updatedAts = []
    
    for i in range(len(rows)):                                                    
        if i>0 and rows[i][0] != rows[i-1][0]:
            vendors.append({'vendor':rows[i-1][1], 'products':products})
            cves.append({'cveID':rows[i-1][0], 'cvssScore':rows[i-1][3], 'vendors': vendors, 'publishDate':rows[i-1][5], 'lastModifiedDate':rows[i-1][6], 'createdAt':rows[i-1][7], 'updatedAt':rows[i-1][8], 'description':rows[i-1][9], 'threatCategory':'cve'})
            products = []
            vendors = []
        elif i>0 and rows[i][1] != rows[i-1][1]:
            vendors.append({'vendor':rows[i-1][1], 'products':products})
            products = []

        products.append(rows[i][2])
            
        if i == len(rows)-1:
            vendors.append({'vendor':rows[i][1], 'products':products})
            cves.append({'cveID':rows[i][0], 'cvssScore':rows[i][3], 'vendors': vendors, 'publishDate':rows[i][5], 'lastModifiedDate':rows[i][6], 'createdAt':rows[i][7], 'updatedAt':rows[i][8], 'description':rows[i][9], 'threatCategory':'cve'})
            products = []
            vendors = []
    
    conn.close()
    return cves



def callService(cve,action):
    print(json.dumps(cve))
    print(action)
    #serviceUrl = 'http://a12avipaas043:8580/CIKPI/GetSonarInfo/getSonarScore'
    #jsonResult = json.dumps({'sonarKey':'bap-redirect:bap-redirect','oldVersion':'N/A','newVersion':'1.0.2-SNAPSHOT','jenkinsUrl':'https://hviajenkins:4430/job/ERPPT_PRPO_Sonar/'})
    #hd= {'Content-Type': 'application/json'}
    #res = requests.post(serviceUrl,headers=hd,data=json.dumps(cve))
    #print(res.status_code, res.reason, res.content)



def writeCfg(val):
    fileCfg = open("cve.py.config", "w")
    fileCfg.write(val)
    fileCfg.close()
    print('[INFO]: Finished check: ' + val)



def main():
    # Retrieve lastExecDate
    try:
        global lastExecDate
        global isUseDefaultLastExecDate
        global isValid
        if os.path.isfile(fileCfgPath):
            fileCfg = open(fileCfgPath, "r")
            line = fileCfg.readline().splitlines()[0]
            linedt = datetime.strptime(line, '%Y-%m-%d %H:%M')
            lastExecDate = linedt
            isValid = True
        else:
            isValid = False
    except Exception as e1:
        print('[ERROR1]: ' + str(e1))
        isValid = False
    finally:
        if not isValid:
            isUseDefaultLastExecDate = raw_input('[INFO]: Use "' + defaultLastExecDate + '" as default lastExecDate? [y/n]: ')
            if isUseDefaultLastExecDate == 'y':
                lastExecDate = datetime.strptime(defaultLastExecDate, '%Y-%m-%d %H:%M')
                isValid = True
            else:
                exit()

    # Fetch CVE DB
    try:
        if isValid:
            addUpdateHandler()
            deleteHandler()
            writeCfg(datetime.now().strftime("%Y-%m-%d %H:%M")) 
    except Exception as e2:
        print('[ERROR2]: ' + str(e2))
 



if __name__ == "__main__":
    main()
