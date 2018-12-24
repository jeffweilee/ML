#   -*- coding: utf-8 -*-
#!/usr/bin/python

import base64, json, getopt, os, requests, sqlite3, sys, configparser
from datetime import datetime


fileCfgPath ='cve.py.config'
defaultLastExecDate = '1980-01-01 00:00'
serviceUrl = 'http://a08avideb23.tsmc.com.tw:8580/CIRCPlatform/NewThreatCveRest'
sqlstatement = "select distinct cve_id, vendor, product, score, severity, strftime('%%Y-%%m-%%d %%H:%%M', published_date) as published_date, strftime('%%Y-%%m-%%d %%H:%%M', last_modified_date) as last_modified_date, strftime('%%Y-%%m-%%d %%H:%%M', created_at) as created_at, strftime('%%Y-%%m-%%d %%H:%%M', updated_at) as updated_at, cve_description from ( select js.id, js.cve_id, js.published_date, js.last_modified_date, js.created_at, js.updated_at, af.vendor, af.product, af.version, case when (c3.base_score is NULL) then c2.base_score else c3.base_score end score, case when (c3.base_severity is NULL) then c2.severity else c3.base_severity end severity, de.value as cve_description from nvd_jsons js left join cvss3 c3 on js.id = c3.nvd_json_id left join cvss2_extras c2 on js.id = c2.nvd_json_id left join affects af on js.id = af.nvd_json_id left join descriptions de on js.id = de.nvd_json_id where af.vendor in (%(vendor)s)) nvd_all where score >= ? and score < ? order by cve_id desc, vendor desc limit ?;"
sqlstatementbyCveid = "select distinct cve_id, vendor, product, score, severity, strftime('%%Y-%%m-%%d %%H:%%M', published_date) as published_date, strftime('%%Y-%%m-%%d %%H:%%M', last_modified_date) as last_modified_date, strftime('%%Y-%%m-%%d %%H:%%M', created_at) as created_at, strftime('%%Y-%%m-%%d %%H:%%M', updated_at) as updated_at, cve_description from ( select js.id, js.cve_id, js.published_date, js.last_modified_date, js.created_at, js.updated_at, af.vendor, af.product, af.version, case when (c3.base_score is NULL) then c2.base_score else c3.base_score end score, case when (c3.base_severity is NULL) then c2.severity else c3.base_severity end severity, de.value as cve_description from nvd_jsons js left join cvss3 c3 on js.id = c3.nvd_json_id left join cvss2_extras c2 on js.id = c2.nvd_json_id left join affects af on js.id = af.nvd_json_id left join descriptions de on js.id = de.nvd_json_id where af.vendor in (%(vendor)s)) nvd_all where score >= ? and score < ? and cve_id in (%(cveid)s) order by cve_id desc, vendor desc;"



def addUpdateHandler():
    preparedTuple = vendorKeywordsTuple + (int(scoreCriteria), 11)
    rows=query(preparedTuple)
    cves=toJson(rows)
    for cve in cves:
        isUpdated = datetime.strptime(cve['updatedAt'],'%Y-%m-%d %H:%M') > lastExecDate
        if isUpdated:
            callService(cve,'add')


def deleteHandler():
    preparedTuple = vendorKeywordsTuple + (0, int(scoreCriteria))
    rows=query(preparedTuple)
    cves=toJson(rows)
    for cve in cves:
        isUpdated = datetime.strptime(cve['updatedAt'],'%Y-%m-%d %H:%M') > lastExecDate
        if isUpdated:
            callService(cve,'delete')


def query(preparedTuple):
    conn = sqlite3.connect('cve.sqlite3')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    if len(cveidsTuple[0]) > 0:
        preparedTuple = preparedTuple + cveidsTuple
        cursor.execute(sqlstatementbyCveid % {'vendor':','.join('?'*len(vendorKeywordsTuple)), 'cveid':','.join('?'*len(cveidsTuple))}, preparedTuple)
    else:
        preparedTuple = preparedTuple + limitQueryTuple
        cursor.execute(sqlstatement % {'vendor':','.join('?'*len(vendorKeywordsTuple))}, preparedTuple)
    rows = cursor.fetchall()
    conn.close()
    return rows
    

def toJson(rowsTmp):
    # 0:cve_id, 1:vendor, 2:product, 3:score, 4:severity, 5:published_date, 6:last_modified_date, 7:created_at, 8:updated_at, 9:cve_description
    cves, vendors, products, updatedAts, rows = [], [], [], [], []

    for row in rowsTmp:
        if any(k in row['product'] for k in productKeywordsTuple):
            rows.append(row)


    for i in range(len(rows)):
        if i>0 and rows[i]['cve_id'] != rows[i-1]['cve_id']:
            vendors.append({'vendor':rows[i-1]['vendor'], 'products':products})
            cves.append({'cveID':rows[i-1]['cve_id'], 
                'cvssScore':rows[i-1]['score'], 
                'vendors': vendors, 
                'publishDate':rows[i-1]['published_date'], 
                'lastModifiedDate':rows[i-1]['last_modified_date'], 
                'createdAt':rows[i-1]['created_at'], 
                'updatedAt':rows[i-1]['updated_at'], 
                'description':rows[i-1]['cve_description'], 
                'threatCategory':'cve'})
            products = []
            vendors = []
        elif i>0 and rows[i]['vendor'] != rows[i-1]['vendor']:
            vendors.append({'vendor':rows[i-1]['vendor'], 
                'products':products})
            products = []

        products.append(rows[i]['product'])
            
        if i == len(rows)-1:
            vendors.append({'vendor':rows[i]['vendor'], 
                'products':products})
            cves.append({'cveID':rows[i]['cve_id'], 
                'cvssScore':rows[i]['score'], 
                'vendors': vendors, 
                'publishDate':rows[i]['published_date'], 
                'lastModifiedDate':rows[i]['last_modified_date'], 
                'createdAt':rows[i]['created_at'], 
                'updatedAt':rows[i]['updated_at'], 
                'description':rows[i]['cve_description'], 
                'threatCategory':'cve'})
            products = []
            vendors = []
    return cves


def callService(cve,action):
    print(cve)
    print()
    hd= {'Content-Type': 'application/json'}
    if action == 'add':
        req = requests.post(serviceUrl, headers=hd, data=json.dumps(cve), verify=False)
        print('{} {} {} {}\n'.format('[INFO]: ', req.status_code, req.reason, req.url) + req.text)
    elif action == 'delete':
        req = requests.delete(serviceUrl, headers=hd, data=json.dumps(cve), verify=False)
        print('{} {} {} {}\n'.format('[INFO]: ', req.status_code, req.reason, req.url) + req.text)


def writeCfg(section, key,val):
    config = configparser.ConfigParser()
    config.read(fileCfgPath)
    config.set(section, key, val)
    with open(fileCfgPath, 'w') as configfile:
        config.write(configfile)
    print('[INFO]: Finished check. [' + section + '] ' + key + ':' + val)


def parser(argv):
    global scoreCriteria 
    global vendorKeywordsTuple  # query condition in sql
    global productKeywordsTuple # filter condition in query() b' product column value is fuzzy
    global cveidsTuple
    global lastExecDate
    global isUseDefaultLastExecDate
    global limitQueryTuple
    vendorKeywords, productKeywords, scoreCriteria, cveids, lastExecDate, limitQuery  = '', '', '', '', '', ''

    if not os.path.isfile(fileCfgPath):
        print('[ERROR]: Config file [' + fileCfgPath + '] not found. ' + str(e1))
        exit()

    ### Fetch [SERVICE] serviceURL from cve.py.config
    try:
        config = configparser.ConfigParser()
        config.read(fileCfgPath)
        serviceurl = config['SERVICE']['serviceurl']
        #print(serviceurl)
    except Exception as e1:
        print('[ERROR]: serviceurl attribute not found in config file [' + fileCfgPath + ']. ' + str(e1))
        exit()

    ### Fetch [EXEC] lastExecDateTime from cve.py.config
    try:
        config = configparser.ConfigParser()
        config.read(fileCfgPath)
        lastExecDate = datetime.strptime(config['EXEC']['lastexecdatetime'], '%Y-%m-%d %H:%M')
        #print(lastExecDate)
    except Exception as e1:
        print('[ERROR]: lastexecdatetime attribute not found or format mismatch [Y-m-d H:M]. ' + str(e1))
        isUseDefaultLastExecDate = input('[INFO]: Import all data? (Use "' + defaultLastExecDate + '" as default lastExecDate) [y/n]: ')
        if isUseDefaultLastExecDate == 'y':
            lastExecDate = datetime.strptime(defaultLastExecDate, '%Y-%m-%d %H:%M')
        else:
            exit()

    ### Fetch [PARA] from cve.py.config
    try:
        config = configparser.ConfigParser()
        config.read(fileCfgPath)
        vendorKeywords = config['PARA']['vendors']
        productKeywords = config['PARA']['products']
        scoreCriteria = config['PARA']['scoreCriteria']
        cveids = config['PARA']['cveids']
        limitQuery = config['PARA']['limitquery'] if len(config['PARA']['limitquery']) > 0 else -1
    except Exception as e1:
        print('[WARNING]: ' + str(e1))


    ### Parse input parameter
    try:
        opts, args = getopt.getopt(argv,"hv:p:s:c:f",["vendors=","products=","scoreCriteria=","cveids=","force"])
    except getopt.GetoptError:
        print('[Usage] -v <vendors,> -p <products,> -c <cveids,> -s <scoreCriteria> -f force[optional]')
        exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('[Usage] -v <vendors,> -p <products,> -c <cveids,> -s <scoreCriteria> -f force[optional]')
            exit()
        elif opt in ("-v", "--vendors"):
            vendorKeywords = arg
        elif opt in ("-p", "--products"):
            productKeywords = arg
        elif opt in ("-s", "--scoreCriteria"):
            scoreCriteria = arg
        elif opt in ("-c", "--cveids"):
            cveids = arg
        elif opt in ("-f", "--force"):
            print(lastExecDate)
            lastExecDate = datetime.strptime(defaultLastExecDate, '%Y-%m-%d %H:%M')
            print(lastExecDate)

    vendorKeywordsTuple = tuple(vendorKeywords.split(','))
    productKeywordsTuple = tuple(productKeywords.split(','))
    cveidsTuple = tuple(cveids.split(','))
    limitQueryTuple = tuple(limitQuery.split(','))
    print('[INFO]: vendorKeywords: ' + vendorKeywords)
    print('[INFO]: productKeywords: ' + productKeywords)
    print('[INFO]: cveids: ' + cveids)
    print('[INFO]: scoreCriteria: ' + scoreCriteria)
    print('[INFO]: limitQuery: '+ limitQuery)

def main(argv):
    try:
        parser(argv)
        addUpdateHandler()
        #deleteHandler()
        writeCfg('EXEC', 'lastexecdatetime', datetime.utcnow().strftime("%Y-%m-%d %H:%M"))
    except Exception as e2:
        print('[ERROR]: ' + str(e2))



if __name__ == "__main__":
    main(sys.argv[1:])
