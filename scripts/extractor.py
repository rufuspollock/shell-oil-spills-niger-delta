#!/usr/bin/env python
# Script to extract data from the xml file to the CSV files

from datetime import date
from lxml import etree
from unicodecsv import DictWriter


def writetocsv(xmlfile=None, month=None, year=None, outfile='../data/data.csv'):
    if xmlfile is None:
        raise Exception, "No XML file passed"
    if month is None:
        raise Exception, "No month passed"
    if year is None:
        raise Exception, "No year passed"
    xmldata = etree.parse(xmlfile)
    csvwriter = None
    csvfile = open('../data/data.csv', 'a')
    for incident in xmldata.iter('DATA'):
        data = {'month': month, 'year': year}
        for field in incident.iterchildren():
            data[field.tag] = field.text
        if not csvwriter:
            csvwriter = DictWriter(csvfile, fieldnames=data.keys())
            csvwriter.writeheader()
        csvwriter.writerow(data)
    csvfile.close()


if __name__ == '__main__':
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    today = date.today()
    for month in months:
        url = 'http://www.shell.com.ng/home/page/nga/environment_society/environment_tpkg/oil_spills/data_2011/data_%s.xml' % month
        print url
        writetocsv(xmlfile=url, month=month, year=2011)
    for index, month in enumerate(months):
        if today.month - 1 > index:
            url = 'http://www.shell.com.ng/home/page/nga/environment_society/environment_tpkg/oil_spills/data_%s.xml' % month
            print url
            writetocsv(xmlfile=url, month=month, year=2012)
