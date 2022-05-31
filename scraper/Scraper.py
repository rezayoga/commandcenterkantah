#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#*Bot-Scraper-Command-Center-Kantor-Pertanahan" data-toc-modified-id="*Bot-Scraper-Command-Center-Kantor-Pertanahan-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>*Bot Scraper Command Center Kantor Pertanahan</a></span></li><li><span><a href="#Bot-Init!" data-toc-modified-id="Bot-Init!-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Bot Init!</a></span></li><li><span><a href="#Variables" data-toc-modified-id="Variables-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Variables</a></span></li><li><span><a href="#Login-SSO" data-toc-modified-id="Login-SSO-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Login SSO</a></span></li><li><span><a href="#Daftar-Tunggakan-Berkas" data-toc-modified-id="Daftar-Tunggakan-Berkas-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Daftar Tunggakan Berkas</a></span></li><li><span><a href="#Informasi-Detail-Berkas" data-toc-modified-id="Informasi-Detail-Berkas-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Informasi Detail Berkas</a></span></li><li><span><a href="#Daftar-Penghasilan-Negara-DI.307" data-toc-modified-id="Daftar-Penghasilan-Negara-DI.307-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Daftar Penghasilan Negara DI.307</a></span></li><li><span><a href="#Realisasi-PTSL-Rupiah-Murni-Kantah" data-toc-modified-id="Realisasi-PTSL-Rupiah-Murni-Kantah-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Realisasi PTSL Rupiah Murni Kantah</a></span></li><li><span><a href="#Re-Login-SSO" data-toc-modified-id="Re-Login-SSO-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Re-Login SSO</a></span></li><li><span><a href="#Early-Warning" data-toc-modified-id="Early-Warning-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>Early Warning</a></span><ul class="toc-item"><li><span><a href="#Rekapitulasi-Bidang-Tanah-Tanpa-Data-Yuridis-Kantah" data-toc-modified-id="Rekapitulasi-Bidang-Tanah-Tanpa-Data-Yuridis-Kantah-10.1"><span class="toc-item-num">10.1&nbsp;&nbsp;</span>Rekapitulasi Bidang Tanah Tanpa Data Yuridis Kantah</a></span></li><li><span><a href="#Rekapitulasi-Pengumuman-Kedaluwarsa-Kantah" data-toc-modified-id="Rekapitulasi-Pengumuman-Kedaluwarsa-Kantah-10.2"><span class="toc-item-num">10.2&nbsp;&nbsp;</span>Rekapitulasi Pengumuman Kedaluwarsa Kantah</a></span></li><li><span><a href="#Rekapitulasi-Berkas-Tanpa-Bidang-Tanah-Kantah" data-toc-modified-id="Rekapitulasi-Berkas-Tanpa-Bidang-Tanah-Kantah-10.3"><span class="toc-item-num">10.3&nbsp;&nbsp;</span>Rekapitulasi Berkas Tanpa Bidang Tanah Kantah</a></span></li><li><span><a href="#Rekapitulasi-Berkas-Tanpa-Pemohon-Kantah" data-toc-modified-id="Rekapitulasi-Berkas-Tanpa-Pemohon-Kantah-10.4"><span class="toc-item-num">10.4&nbsp;&nbsp;</span>Rekapitulasi Berkas Tanpa Pemohon Kantah</a></span></li></ul></li></ul></div>

# 
# # *Bot Scraper Command Center Kantor Pertanahan
# ---
# * Crafted by: [**Reza Yogaswara**](http://me.rezayogaswara.com)
# * Output Report: SQL Data

# In[28]:


from datetime import datetime, timedelta, date
import datetime as dt
import time, os

os.environ['TZ'] = 'Asia/Jakarta'
time.tzset()

hari_ini = date.today()
start_time = time.time()


# In[29]:


#from IPython.core.interactiveshell import InteractiveShell
#InteractiveShell.ast_node_interactivity = "all"


# In[ ]:





# In[30]:


print('\n=> Crafted by: Reza D Yogaswara | me@rezayogaswara.com')
print('\n=> Output Report: SQL / Progres Kegiatan APBN dan Rutin Kantor Pertanahan')


# In[ ]:





# # Bot Init!

# In[31]:


print('\n=> Bot Init!\n')
import time
start_time = time.time()


# In[32]:


get_ipython().system('python -V')


# In[33]:


import pandas as pd


# In[34]:


pd.show_versions(as_json=False)


# In[ ]:





# # Variables

# In[35]:


username = '197003151994041007'
password = 'Ristanto1503'
satker_id_kanwil = 'A1DED793DAF0C64DE0400B0A9A144C4A'
satker_id_kantah = '9fe8d1abe5b74f36baff1f26ea9f26c3'
satker_nama_kanwil = 'JATIM'
satker_nama_kantah = 'Kota Batu'
mysql_host = 'localhost'
mysql_port = 3306
mysql_user = 'root'
mysql_password = 'JyiI7tDdkcDqaI7x'
mysql_database = 'db_command_center_kantah'
program_id_ptsl = 'D367ADB61BD9FFF5E0530C1D140A1FD0'


# In[ ]:





# In[36]:


import datetime
import calendar
import os, time
now = datetime.datetime.now()
#print now.year, now.month, now.day, now.hour, now.minute, now.second
os.environ['TZ'] = 'Asia/Jakarta'
time.tzset()

def getCurrentDate(withTime = False):
  month = ['Januari',
			'Februari',
			'Maret',
			'April',
			'Mei',
			'Juni',
			'Juli',
			'Agustus',
			'September',
			'Oktober',
			'November',
			'Desember'
  ];

  if (withTime):
    return '%s-%s-%s %s:%s:%s' % (time.strftime('%Y'), time.strftime('%m'), time.strftime('%d'), time.strftime('%H'), time.strftime('%M'), time.strftime('%S'))
  return '%s-%s-%s' % (time.strftime('%d'), month[int(time.strftime('%m')) - 1].upper(), now.year)


# In[37]:


import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(to, subject, text):
    # me == my email address
    # you == recipient's email address
    me = "robot@commandcenterbangkalan.id"
    #you = "me@rezayogaswara.com"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = to

    # Create the body of the message (a plain-text and an HTML version).
    # text = '[%s] Hi!\n<i>Bot Scrap</i> task done in %f minutes:' % (getCurrentDate(True), float(elapsed_time/60))

    html = """<!doctype html>
    <html>
      <head>
        <meta name="viewport" content="width=device-width" />
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <title>Command Center Bangkalan</title>
        <link href="https://fonts.googleapis.com/css?family=Quicksand&display=swap" rel="stylesheet">
        <style>

            body {
                font-family: \'Quicksand\', sans-serif;
            }
        </style>
        <style>
          /* -------------------------------------
              GLOBAL RESETS
          ------------------------------------- */
          img {
            border: none;
            -ms-interpolation-mode: bicubic;
            max-width: 100%; }

          body {
            background-color: #f6f6f6;
            font-family: sans-serif;
            -webkit-font-smoothing: antialiased;
            font-size: 14px;
            line-height: 1.4;
            margin: 0;
            padding: 0;
            -ms-text-size-adjust: 100%;
            -webkit-text-size-adjust: 100%; }

          table {
            border-collapse: separate;
            mso-table-lspace: 0pt;
            mso-table-rspace: 0pt;
            width: 100%; }
            table td {
              font-family: sans-serif;
              font-size: 14px;
              vertical-align: top; }

          /* -------------------------------------
              BODY & CONTAINER
          ------------------------------------- */

          .body {
            background-color: #f6f6f6;
            width: 100%; }

          /* Set a max-width, and make it display as block so it will automatically stretch to that width, but will also shrink down on a phone or something */
          .container {
            display: block;
            margin: 0 auto !important;
            /* makes it centered */
            max-width: 580px;
            padding: 10px;
            width: 580px; }

          /* This should also be a block element, so that it will fill 100% of the .container */
          .content {
            box-sizing: border-box;
            display: block;
            margin: 0 auto;
            max-width: 580px;
            padding: 10px; }

          /* -------------------------------------
              HEADER, FOOTER, MAIN
          ------------------------------------- */
          .main {
            background: #ffffff;
            border-radius: 3px;
            width: 100%; }

          .wrapper {
            box-sizing: border-box;
            padding: 20px; }

          .content-block {
            padding-bottom: 10px;
            padding-top: 10px;
          }

          .footer {
            clear: both;
            margin-top: 10px;
            text-align: center;
            width: 100%; }
            .footer td,
            .footer p,
            .footer span,
            .footer a {
              color: #999999;
              font-size: 12px;
              text-align: center; }

          /* -------------------------------------
              TYPOGRAPHY
          ------------------------------------- */
          h1,
          h2,
          h3,
          h4 {
            color: #000000;
            font-family: sans-serif;
            font-weight: 400;
            line-height: 1.4;
            margin: 0;
            margin-bottom: 30px; }

          h1 {
            font-size: 35px;
            font-weight: 300;
            text-align: center;
            text-transform: capitalize; }

          p,
          ul,
          ol {
            font-family: sans-serif;
            font-size: 14px;
            font-weight: normal;
            margin: 0;
            margin-bottom: 15px; }
            p li,
            ul li,
            ol li {
              list-style-position: inside;
              margin-left: 5px; }

          a {
            color: #3498db;
            text-decoration: underline; }

          /* -------------------------------------
              BUTTONS
          ------------------------------------- */
          .btn {
            box-sizing: border-box;
            width: 100%; }
            .btn > tbody > tr > td {
              padding-bottom: 15px; }
            .btn table {
              width: auto; }
            .btn table td {
              background-color: #ffffff;
              border-radius: 5px;
              text-align: center; }
            .btn a {
              background-color: #ffffff;
              border: solid 1px #3498db;
              border-radius: 5px;
              box-sizing: border-box;
              color: #3498db;
              cursor: pointer;
              display: inline-block;
              font-size: 14px;
              font-weight: bold;
              margin: 0;
              padding: 12px 25px;
              text-decoration: none;
              text-transform: capitalize; }

          .btn-primary table td {
            background-color: #3498db; }

          .btn-primary a {
            background-color: #3498db;
            border-color: #3498db;
            color: #ffffff; }

          /* -------------------------------------
              OTHER STYLES THAT MIGHT BE USEFUL
          ------------------------------------- */
          .last {
            margin-bottom: 0; }

          .first {
            margin-top: 0; }

          .align-center {
            text-align: center; }

          .align-right {
            text-align: right; }

          .align-left {
            text-align: left; }

          .clear {
            clear: both; }

          .mt0 {
            margin-top: 0; }

          .mb0 {
            margin-bottom: 0; }

          .preheader {
            color: transparent;
            display: none;
            height: 0;
            max-height: 0;
            max-width: 0;
            opacity: 0;
            overflow: hidden;
            mso-hide: all;
            visibility: hidden;
            width: 0; }

          .powered-by a {
            text-decoration: none; }

          hr {
            border: 0;
            border-bottom: 1px solid #f6f6f6;
            Margin: 20px 0; }

          /* -------------------------------------
              RESPONSIVE AND MOBILE FRIENDLY STYLES
          ------------------------------------- */
          @media only screen and (max-width: 620px) {
            table[class=body] h1 {
              font-size: 28px !important;
              margin-bottom: 10px !important; }
            table[class=body] p,
            table[class=body] ul,
            table[class=body] ol,
            table[class=body] td,
            table[class=body] span,
            table[class=body] a {
              font-size: 16px !important; }
            table[class=body] .wrapper,
            table[class=body] .article {
              padding: 10px !important; }
            table[class=body] .content {
              padding: 0 !important; }
            table[class=body] .container {
              padding: 0 !important;
              width: 100% !important; }
            table[class=body] .main {
              border-left-width: 0 !important;
              border-radius: 0 !important;
              border-right-width: 0 !important; }
            table[class=body] .btn table {
              width: 100% !important; }
            table[class=body] .btn a {
              width: 100% !important; }
            table[class=body] .img-responsive {
              height: auto !important;
              max-width: 100% !important;
              width: auto !important; }}

          /* -------------------------------------
              PRESERVE THESE STYLES IN THE HEAD
          ------------------------------------- */
          @media all {
            .ExternalClass {
              width: 100%; }
            .ExternalClass,
            .ExternalClass p,
            .ExternalClass span,
            .ExternalClass font,
            .ExternalClass td,
            .ExternalClass div {
              line-height: 100%; }
            .apple-link a {
              color: inherit !important;
              font-family: inherit !important;
              font-size: inherit !important;
              font-weight: inherit !important;
              line-height: inherit !important;
              text-decoration: none !important; }
            .btn-primary table td:hover {
              background-color: #34495e !important; }
            .btn-primary a:hover {
              background-color: #34495e !important;
              border-color: #34495e !important; } }

        </style>
      </head>
      <body class="">
        <table border="0" cellpadding="0" cellspacing="0" class="body">
          <tr>
            <td>&nbsp;</td>
            <td class="container">
              <div class="content">

                <!-- START CENTERED WHITE CONTAINER -->
                <span class="preheader">Command Center Bangkalan</span>
                <table class="main">

                  <!-- START MAIN CONTENT AREA -->
                  <tr>
                    <td class="wrapper">
                      <table border="0" cellpadding="0" cellspacing="0">
                        <tr>
                          <td>
                            <p><img src="http://static.commandcenterbangkalan.id/logo_fit.png" alt="Command Center Bangkalan" height="70" border="0" style="border:0; outline:none; text-decoration:none; display:block;"></p>
                            <p>&nbsp;</p>
                            <p>""" + text + """</p>
                            <p>&nbsp;</p>
                            <p>Regards,<br />🤖 Robot</p>
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>

                <!-- END MAIN CONTENT AREA -->
                </table>

                <!-- START FOOTER -->
                <div class="footer">
                  <table border="0" cellpadding="0" cellspacing="0">
                    <tr>
                      <td class="content-block">
                        <span class="apple-link">Command Center Bangkalan</span>
                        <br> <i>Smart Work Pays Best</i>.
                      </td>
                    </tr>
                  </table>
                </div>
                <!-- END FOOTER -->

              <!-- END CENTERED WHITE CONTAINER -->
              </div>
            </td>
            <td>&nbsp;</td>
          </tr>
        </table>

      </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    mail = smtplib.SMTP('mail.commandcenterbangkalan.id', 25)
    mail.ehlo()
    mail.starttls()
    mail.login(me, "@R0boT_")
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    mail.sendmail(me, to, msg.as_string())
    mail.quit()


# In[38]:


#send_mail('reza.yoga@gmail.com', 'Bot Scrap Init', '[%s] Hi!\n<i>Bot Scrap</i> init:' % (getCurrentDate(True)))


# In[ ]:





# # Login SSO

# In[39]:


import http.cookiejar
import urllib.request
from bs4 import BeautifulSoup
from IPython.core.display import display, HTML
import pandas as pd
import datetime
import ssl
from retry import retry

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):ssl._create_default_https_context = ssl._create_unverified_context

now = datetime.datetime.now()
print ("Scraped at : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

'''====================================================================================================Login''' 
# Store the cookies and create an opener that will hold them
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

# Add our headers
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/70.0')]

@retry((Exception), tries=25, delay=30, backoff=0)
def login():
    time.sleep(2)  
    
    # Install our opener (note that this changes the global opener to the one
    # we just made, but you can also just call opener.open() if you want)
    urllib.request.install_opener(opener)

    # The action/ target from the form
    authentication_url = 'https://kkp2.atrbpn.go.id/Account/Index?returnUrl=%2F'

    # Input parameters we are going to send
    payload = {
      'UserName': username,
      'Password': password,
      'IpPublic': '201.132.123.123',
      'IpLocal': '2.2.2.2',
      'MacAddress' :'00:1B:44:11:3A:B7',
      'DeviceName' : ''
    }

    # Use urllib to encode the payload
    data = urllib.parse.urlencode(payload).encode("utf-8")

    # Build our Request object (supplying 'data' makes it a POST)
    #req = urllib.request.Request(authentication_url, data)
    req = urllib.request.Request(authentication_url)

    # Make the request and read the response
    resp = urllib.request.urlopen(req, data=data)

    with urllib.request.urlopen(req,data=data) as f:
        resp = f.read()
        #display(resp)
        #bs = BeautifulSoup(html)
        #display(HTML(bs))
    '''=========================================================================================Assigning Kantor Pertanahan'''

    # The action/ target from the form
    authentication_url = 'https://kkp2.atrbpn.go.id/Account/SetKantor'

    # Input parameters we are going to send
    payload = {
      'UserName': username,
      'ReturnUrl': '/',
      'Persistent': 'False',
      'SelectedOffice': satker_id_kantah
      }

    # Use urllib to encode the payload
    data = urllib.parse.urlencode(payload).encode("utf-8")

    # Build our Request object (supplying 'data' makes Fit a POST)
    #req = urllib.request.Request(authentication_url, data)
    req = urllib.request.Request(authentication_url)

    # Make the request and read the response
    resp = urllib.request.urlopen(req, data=data)

    with urllib.request.urlopen(req,data=data) as f:
        resp = f.read()
        soup = BeautifulSoup(resp, 'html.parser')
        #print(soup.prettify())
        #display(HTML(soup.prettify()))

login()
get_ipython().run_line_magic('time', '')


# In[ ]:





# # Daftar Tunggakan Berkas

# In[40]:


@retry((Exception), tries=25, delay=10, backoff=0)
def get_data():
    #time.sleep(2)
    #
    #
    # INI BIKIN RESET COOKIE< HARUS  DI COMMENT!
    #
    #
    # Store the cookies and create an opener that will hold them
    #cj = http.cookiejar.CookieJar()
    #opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

    # Add our headers
    opener.addheaders = [("X-Requested-With", "XMLHttpRequest",),('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/70.0')]

    # Install our opener (note that this changes the global opener to the one
    # we just made, but you can also just call opener.open() if you want)
    urllib.request.install_opener(opener)

    # The action/ target from the form
    authentication_url = 'https://kkp2.atrbpn.go.id/bo/Monitoring/DaftarTunggakanBerkas'

    # Input parameters we are going to send
    payload = {
      }

    # Use urllib to encode the payload
    data = urllib.parse.urlencode(payload).encode("utf-8")

    # Build our Request object (supplying 'data' makes it a POST)
    req = urllib.request.Request(authentication_url, data)
    #req = urllib.request.Request(authentication_url)

    # Make the request and read the response
    resp = urllib.request.urlopen(req, data=data)

    html = urllib.request.urlopen(req,data=data).read()

    #soup = BeautifulSoup(resp, 'html.parser')
    #display(HTML(soup.prettify()))

    #print(html)
    #bs = BeautifulSoup(html, "html5lib")
    bs = BeautifulSoup(resp, 'html.parser')

    for script in bs.find_all('script'):
        script.extract()

    for i in bs.find_all('i'):
        i.extract()

    soup = BeautifulSoup("<table class='table'><tr>"+
                         "<td>no</td>"+
                         "<td>jabatan</td>"+
                         "<td>jumlah_berkas</td>"+
                         "<td>sesuai_durasi</td>"+
                         "<td>hampir_jatuh_tempo</td>"+
                         "<td>sudah_jatuh_tempo</td>"+
                         "</tr></table>", "lxml")
    tag = soup.table
    tag.append(bs)    

    data = pd.read_html(str(tag), header=0, flavor = 'bs4', decimal=",", thousands='.')
    df = data[0]

    del df['no']


    df.set_index("jabatan", inplace = True) 
    #df=df.sort_index()

    #print(df.columns.tolist())
    return df


# In[41]:


df = get_data()
display(df)
#df.loc['Tim Panitia/Tim Peneliti Tanah', :]

get_ipython().run_line_magic('time', '')


# In[ ]:





# In[ ]:





# In[42]:


for col_name, data in df.items():
	print("col_name:", col_name, "- data:", data)  
	print("----------------------------------------------------------------------")


# In[ ]:





# In[43]:


# Example format: "21/10/2021 - 21/10/2021"
def getCurrentDateFilterPenghasilanNegaraDI307():
    return '%s/%s/%s - %s/%s/%s' % (time.strftime('%d'), time.strftime('%m'), time.strftime('%Y'), time.strftime('%d'), time.strftime('%m'), time.strftime('%Y'))


# In[44]:


print(getCurrentDateFilterPenghasilanNegaraDI307())


# In[ ]:





# In[45]:


get_ipython().run_line_magic('lsmagic', '')


# In[ ]:





# In[46]:


import pymysql
# Connect to the database


# In[47]:


config_mysql = {
    "host": mysql_host,
    "port": mysql_port,
    "user": mysql_user,
    "passwd": mysql_password,
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor,
    "database": mysql_database
}

"""
connection = pymysql.connect(**config_mysql)
results = None
try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `tb_berkas_pnbp`"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
finally:
    connection.close()
"""    
get_ipython().run_line_magic('time', '')


# In[ ]:





# In[48]:


connection = pymysql.connect(**config_mysql)
now = getCurrentDate(True)

"""
with connection.cursor() as cursor:
    # Create a new record
    sql = "TRUNCATE `tb_daftar_tunggakan_berkas_pnbp`"
    cursor.execute(sql)
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    print(cursor.rowcount, " current records.")
    connection.commit()
"""

for index, row in df.iterrows():
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `tb_daftar_tunggakan_berkas_pnbp` (jabatan, jumlah_berkas, sesuai_durasi, hampir_jatuh_tempo, sudah_jatuh_tempo, created_at) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (index, str(row['jumlah_berkas']), str(row['sesuai_durasi']), str(row['hampir_jatuh_tempo']), str(row['sudah_jatuh_tempo']), now))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        #with connection.cursor() as cursor:
            # Read a single record
            #sql = "SELECT * FROM `tb_daftar_tunggakan_berkas_pnbp` ORDER BY id DESC"
            #cursor.execute(sql, ())
            #result = cursor.fetchone()
            #print(result)
    finally:
        #connection.close()
        pass
connection.close()
print('"Daftar Tunggakan Berkas" done!')


# In[ ]:





# # Informasi Detail Berkas

# In[49]:


import re
import json

connection = pymysql.connect(**config_mysql)
now = getCurrentDate(True)

with connection.cursor() as cursor:
    # Create a new record
    sql = "TRUNCATE `tb_berkas_pnbp`"
    cursor.execute(sql)
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    print(cursor.rowcount, " current records.")
    connection.commit()
    
def getDetailBerkas(b):
    """
    Contoh HTML Format ============================================================================================
    <div class="col-md-4 col-sm-4 col-xs-12">
        <div class="x_content">
            <div class="project_detail">
                <input id="BerkasId" name="BerkasId" type="hidden" value="B81F433788A9D8B7E0530B1D140A6DA4" />
                <p class="title">Nomor Berkas</p>
                <p>27/2021, Kantor Pertanahan Kabupaten Bangkalan</p>
                <p class="title">Kegiatan</p>
                <p>Pengukuran Dan Pemetaan Kadastral</p>
                <p class="title">Tanggal Mulai</p>
                <p>Rabu  , 06/01/2021 10:20:28</p>
                            <p class="title">Status</p>
                <p>Dalam Proses</p>
                <p class="title">Pemohon</p>
                <p>ROMI MUJIONO</p>
                    <p class="title">Pemberi Kuasa</p>
                    <p>IMAM</p>
                <p class="title">Petugas Terakhir</p>
                <p>CHOLIFAH</p>
                <p class="title">Posisi Terakhir</p>
                <p>Pelaksana Subseksi Pengukuran dan Pemetaan Kadastral</p>
            </div>
        </div>
    </div>
    <div class="col-md-4 col-sm-4 col-xs-12">
        <div class="x_content">
            <div class="project_detail">
                <p class="title">Biaya</p>
                <p>Pelayanan Pengukuran dan Pemetaan Bidang Tanah, Unit: 1, Jumlah: 250.000<br /><strong class="myLabelContent">Total Biaya: 250.000</strong></p>
                <p class="title">Kode Billing</p>
                <p>820210105585402, Biaya: 250.000, Tanggal Kadaluarsa: Jumat , 08/01/2021 10:00:40, NTPN: 111A82G4UTAOI3NQ, Tanggal Bayar: Rabu  , 06/01/2021 09:56:21</p>
                                    </div>
        </div>
    </div>
    <div class="col-md-4 col-sm-4 col-xs-12">
        <div class="x_content">
            <div class="project_detail">
                <p class="title">Buku Tanah Yang Diinput</p>
                <p>-</p>
                    <p class="title">Permohonan Pengukuran</p>
                    <p>Permohonan Pengukuran sejumlah 1 bidang, dengan jumlah luas 1.500 M2, dan jumlah Biaya Pengukuran Rp. 250.000,-</p>
                                <p class="title">Gambar Ukur</p>
                    <p>Nomor 76/2021 Tanggal 02/02/2021</p>
                            <p class="title">Catatan Berkas</p>
                <p>Tanggal: 12/03/2021, Aditiya Purindana (Pelaksana Subseksi Pengukuran dan Pemetaan Kadastral) - 12-3-2021 ADIT : Naik ke Nur Kholis
    18-3-2021 Nur kholis : Naik ke pak Nur Syaiful
    (24-05-2021) Adit : Naik ke pak nur syaiful</p>
            </div>
        </div>
    </div>
    """
    #
    #
    # INI BIKIN RESET COOKIE< HARUS  DI COMMENT!
    #
    #
    # Store the cookies and create an opener that will hold them
    #cj = http.cookiejar.CookieJar()
    #opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

    # Add our headers
    opener.addheaders = [("X-Requested-With", "XMLHttpRequest",),('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/70.0')]

    # Install our opener (note that this changes the global opener to the one
    # we just made, but you can also just call opener.open() if you want)
    urllib.request.install_opener(opener)

    # The action/ target from the form
    authentication_url = 'https://kkp2.atrbpn.go.id/bo/Monitoring/InformasiBerkasContentFromList'

    # Input parameters we are going to send
    payload = {
        'berkasid': b
    }

    # Use urllib to encode the payload
    data = urllib.parse.urlencode(payload).encode("utf-8")

    # Build our Request object (supplying 'data' makes it a POST)
    req = urllib.request.Request(authentication_url, data)
    #req = urllib.request.Request(authentication_url)

    # Make the request and read the response
    resp = urllib.request.urlopen(req, data=data)

    html = urllib.request.urlopen(req,data=data).read()

    soup = BeautifulSoup(resp, 'html.parser')
    #display(HTML(soup.prettify()))
    
    table = soup.find_all('div', attrs={"class":"project_detail"})
    
    #print(table)
    
    """
    for x in table:
        p = x.find_all('p')
        for y in p:
            print(y)
            
    """
    return table

def getDaftarBerkasFlow(b):
    #
    #
    # INI BIKIN RESET COOKIE< HARUS  DI COMMENT!
    #
    #
    # Store the cookies and create an opener that will hold them
    #cj = http.cookiejar.CookieJar()
    #opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

    # Add our headers
    opener.addheaders = [("X-Requested-With", "XMLHttpRequest",),('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/70.0')]

    # Install our opener (note that this changes the global opener to the one
    # we just made, but you can also just call opener.open() if you want)
    urllib.request.install_opener(opener)

    # The action/ target from the form
    authentication_url = 'https://kkp2.atrbpn.go.id/bo/Berkas/DaftarBerkasFlow'

    # Input parameters we are going to send
    payload = {
        'berkasid': b
    }

    # Use urllib to encode the payload
    data = urllib.parse.urlencode(payload).encode("utf-8")

    # Build our Request object (supplying 'data' makes it a POST)
    req = urllib.request.Request(authentication_url, data)
    #req = urllib.request.Request(authentication_url)

    # Make the request and read the response
    resp = urllib.request.urlopen(req, data=data)

    html = urllib.request.urlopen(req,data=data).read()

    #soup = BeautifulSoup(resp, 'html.parser')
    #display(HTML(soup.prettify()))
    
    json_daftar_berkas_flow = json.loads(html)
    #print(json_daftar_berkas_flow)
    
    return_data = '''
    <div class="ui tablet fluid vertical stackable mini steps">
    '''
    
    for d in json_daftar_berkas_flow['data']:
        return_data +=  '''<div class="step">
                    <i class="user tie icon"></i>
                    <div class="content">
                      <div class="title">{}</div>
                      <div class="description">{}</div>
                    </div>
                  </div>'''.format(d.get('NamaProfileTujuan'), d.get('TanggalFull'))
    
    
    
    # print([d.get('DariPegawai') for d in json_daftar_berkas_flow['data']])
    
    return_data += '</div>'
    
    #print(return_data)
    
    #return str(json_daftar_berkas_flow)
    return return_data

@retry((Exception), tries=25, delay=10, backoff=0)
def getBTN(pageNum, idStatusBerkas = 1):
    #time.sleep(3)
    #
    #
    # INI BIKIN RESET COOKIE< HARUS  DI COMMENT!
    #
    #
    # Store the cookies and create an opener that will hold them
    #cj = http.cookiejar.CookieJar()
    #opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

    # Add our headers
    opener.addheaders = [("X-Requested-With", "XMLHttpRequest",),('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/70.0')]

    # Install our opener (note that this changes the global opener to the one
    # we just made, but you can also just call opener.open() if you want)
    urllib.request.install_opener(opener)

    # The action/ target from the form
    authentication_url = 'https://kkp2.atrbpn.go.id/bo/Monitoring/DaftarBerkasPNBP'

    # Input parameters we are going to send
    payload = {
      'NomorDari': '',
      'NomorSampai': '',
      'Tahun': '',
      'NamaProsedur': '',
      'NamaPemohon': '',
      'PosisiTerakhir': '',
      'TanggalDari': '',
      'TanggalSampai': '',
      'IdStatusBerkas': idStatusBerkas,
      'status': 1,
      'pageNum': pageNum 
    }

    # Use urllib to encode the payload
    data = urllib.parse.urlencode(payload).encode("utf-8")

    # Build our Request object (supplying 'data' makes it a POST)
    req = urllib.request.Request(authentication_url, data)
    #req = urllib.request.Request(authentication_url)

    # Make the request and read the response
    resp = urllib.request.urlopen(req, data=data)

    html = urllib.request.urlopen(req,data=data).read()

    #soup = BeautifulSoup(resp, 'html.parser')
    #display(HTML(soup.prettify()))

    #print(html)
    #bs = BeautifulSoup(html, "html5lib")
    bs = BeautifulSoup(resp, 'html.parser')

    for script in bs.find_all('script'):
        script.extract()    

    for i in bs.find_all('i'):
        i.extract()
    
    soup = BeautifulSoup("<table class='table'><tr>"+
                         "<td>no.</td>"+
                         "<td>nomor_berkas</td>"+
                         "<td>tahun_berkas</td>"+
                         "<td>tanggal_terdaftar</td>"+
                         "<td>jatuh_tempo</td>"+
                         "<td>tanggal_selesai</td>"+
                         "<td>tanggal_diserahkan</td>"+
                         "<td>nama_kegiatan</td>"+
                         "<td>nama_pemohon</td>"+
                         "<td>posisi_terakhir</td>"+
                         "<td>info</td>"+
                         "</tr></table>", "lxml")
    tag = soup.table
    tag.append(bs)  
    
    #print(str(tag))
    data = pd.read_html(str(tag), header=0, flavor = 'bs4', decimal=",", thousands='.')
    df = data[0]

    #del df['no.']
    
    #print(df['nomor_berkas'])
    #df.set_index("nomor", inplace = True) 
    #df=df.sort_index()
    #print(df.columns.tolist())
    
    df = df.where(pd.notnull(df), 'NULL')
    #print(df)
    
    detail_berkas = None
    
    i = 0
    for x in tag.find_all('td'): # will give you all a tag
        #print(x)
        try:
            if re.match('infoBerkas', x['onclick']): # if onclick attribute exist, it will match for searchDB, if success will print
                search_results = re.finditer(r'\(.*?\)', x['onclick']) 
                for item in search_results: 
                    #print(df.loc[:, 'nomor_berkas'][i])
                    #print(item.group(0)) 
                    s = item.group(0)
                    b = s[s.find("(")+1:s.find(")")].replace('\'', "").split(',')[0]
                    t = s[s.find("(")+1:s.find(")")].replace('\'', "").split(',')[1]
                    n = s[s.find("(")+1:s.find(")")].replace('\'', "").split(',')[2]           
                    #print (b)
                    
                    try:
                        with connection.cursor() as cursor:
                            # Create a new record
                            #print(df.where(pd.notnull(df), None))
                            
                            getDetailBerkas(b)
                            
                            sql = "INSERT INTO tb_berkas_pnbp (nomor_berkas, tahun_berkas, tanggal_terdaftar, jatuh_tempo, tanggal_selesai, tanggal_diserahkan, nama_kegiatan, nama_pemohon, posisi_terakhir, json_perjalanan_berkas, html_informasi_berkas_content_from_list, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            cursor.execute(sql, (str(df.loc[:, 'nomor_berkas'][i]), 
                                                 str(df.loc[:, 'tahun_berkas'][i]), 
                                                 str(df.loc[:, 'tanggal_terdaftar'][i]), 
                                                 str(df.loc[:, 'jatuh_tempo'][i]), 
                                                 str(df.loc[:, 'tanggal_selesai'][i]), 
                                                 str(df.loc[:, 'tanggal_diserahkan'][i]), 
                                                 str(df.loc[:, 'nama_kegiatan'][i]), 
                                                 str(df.loc[:, 'nama_pemohon'][i]), 
                                                 str(df.loc[:, 'posisi_terakhir'][i]),
                                                 getDaftarBerkasFlow(b), 
                                                 getDetailBerkas(b),
                                                 now))
                            # connection is not autocommit by default. So you must commit to save
                            # your changes.
                            # print(cursor.rowcount, "record inserted.")
                            connection.commit()
                        #with connection.cursor() as cursor:
                            # Read a single record
                            #sql = "SELECT * FROM tb_berkas_pnbp ORDER BY id DESC"
                            #cursor.execute(sql, ())
                            #result = cursor.fetchone()
                            #print(result)
                    except pymysql.err.InternalError as e:
                        print(str(e))
                        raise MySQLConnectionError        
                            
                    finally:
                        pass
                    
                    i = i + 1
        except:pass
        
    #print(detail_berkas)
    
#getBTN(1)
#getBTN(2)

#getDetailBerkas('B848658C7A04F5B9E0530C1D140AE461')
#getDaftarBerkasFlow('B848658C7A04F5B9E0530C1D140AE461')

for x in range(0, 250):
    #print(str(x) + ' ' + '(' + getCurrentDate(True) + ')')
    getBTN(x)
    
connection.close()

print('"Informasi Detail Berkas" done!')
get_ipython().run_line_magic('time', '')


# In[ ]:





# # Daftar Penghasilan Negara DI.307

# In[50]:

'''
import json

connection = pymysql.connect(**config_mysql)
now = getCurrentDate(True)

with connection.cursor() as cursor:
    # Create a new record
    sql = "TRUNCATE `tb_daftar_penghasilan_negara`"
    cursor.execute(sql)
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    print(cursor.rowcount, " current records.")
    connection.commit()
    
@retry((Exception), tries=25, delay=10, backoff=0)
def get_data():
    time.sleep(3)
    url = 'https://kkp2.atrbpn.go.id/laporan/DaftarIsian/GetDI307'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,id;q=0.8,ms;q=0.7,la;q=0.6',
        'Connection': 'keep-alive',
        #'Content-Length': '219',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        #'Cookie': 'ASP.NET_SessionId=401pawk5iigwkrxm5gmx5yys; .atrbpn2409=4A0911E812B135D862924D2E3840BD1179746F97DDB8DFF5E159D7A50BB8580A3107A3BF3C99FBA1B171C881B724BF08634CC02260A98F68DDEEABA43B9856D560D7217803EECB3FE08A85C3BFDE549FBBB386EDCD1A24D3DDC2FB89B12C9E75F6E7B1B7FFEB55D9537EC09477A45630FE13C004050342D12170AB3DFDD25200E7F698934BA4AC7BF245EE87A375D28DF7AD595D36D1450390E61C87F5979BC248CB3F4C6745BDFA39A0891CCB1A99889F9A3D67F58B802CAF0D791B5C137603A261405065A3D6D6495DDD80D70D26A8294C96461F55E719D54182479CBBCED4CA67B82B70D3408EE12F566B116705690075619AC2AD2CCB39A1AD1BED442B04A67F6AD46456A2E2A233DFEE9CBE66AFD3CF99169E9B2FA076F2E258E51C7AE16E3E3135CEED81826D30F32C2E4D48885E2ED5756955DF2F2ECD6D33CC1C5E32A670CAE56E80E093AD4332620ACAB31B8E755AFFD9EC89BE06BEB82031427032867221B3BF9760B54B0F7EC6FC74C3675788A5225110202063EB90097B79186E892C531BD455BED209D451B06E9DDA9F7CE64D7CA149DD8E684E4F527F9A16164F491A98F576650FD0767F1B379DE807560792ED97179BAD7353D242BAB1CC130AD91DECCB4FD0DE2EBBAB4830983781B794623A959D8688C85E2626968C32CFCD7607A8FC6DCB3648B13EC2C8B1A0F0F9DEEB8D2705E4712E85845AE33B1332FF0E6BB596005886D3B9FC72A537FCF7C5146588863B636AF52A573F7ACB13804BFBA202750CB8ABD571DF6A9B47EF8DE271118ABEBC45AF0809BA89A8A2C21065839C1082FD1FDC503A4B7E16382A8D576CDA60A42E38330511EE30D458A690D4326EC1E4D6724CE91D4644B504163483B4EC0CFB051B5D758FDA898D16903F97B711D6F514440AA91247B74FCE5337BBB2B8877FDFE13477CA8568FE52A34041AC98D0600E6090C0F8F6BAF07A0139EFCB5529BDBA5940C88729EC8B8EE93B99D6C85E671808C597C6C03D3BCECE9FAAE50DD1D4BF2ACF1541F941BF869F3B948BE530E0A86DFD12509DDE29B11A0F573EB08DA3DE5AA74170084F9B937F8D975A6FA8E3025C2791A58FE5AB3CC59683B17F057E193BAA47A227CE9F3F307C49B5BAD9DDC69CECFB9503CF07914B03C87B616E2D1792413E4A5DBA2A0DC6EF1C90EF0978D4C2A6C8DD8FF6ED16A0C4E05CE8349EF0B9DBA69C3275375F6FB72FD95625BB27501FF7718158520C82E7BEC9536BB071FEB45A353AC93DCCBD2E0C294128; TS01cf2c65=012302fab966159f39a8f2e700ca6718171052ddd44b8d74fe7d5fe666cee13cac88de2f97130eb69154ba7c1d1c954f6e99283a1bcb3cb5c518f1ece145aae4ab51ec36cf4997d256d739708e7e28b4a15175f3edf4fc78a9c46ce9c156b0c3237c9541f1',
        'Host': 'kkp2.atrbpn.go.id',
        'Origin': 'https://kkp2.atrbpn.go.id',
        'Referer': 'https://kkp2.atrbpn.go.id/laporan/DaftarIsian/DI307',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    data = (
       ("tpfilter", "Experienced"),
       ("kriteria", ""), 
       ("jenispelayanan", ""), 
       ("tahunnomor", ""), 
       ("dari", ""), 
       ("sampai", ""), 
       ("tahunberkas", ""), 
       ("tanggalperiode", getCurrentDateFilterPenghasilanNegaraDI307()), 
       #("tanggalperiode", '21/10/2021 - 21/10/2021'), 
       ("bulanperiode", ""), 
       ("tahunberkasperiode", ""), 
       ("qtype", "Experienced"), 
       ("draw", 5), 
       ("start", 0), 
       ("length", 1000)
    )

    data = urllib.parse.urlencode(data).encode()
    #data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url)
    req.data = data
    req.headers = headers

    f = urllib.request.urlopen(req)

    #print(f.read())

    data = json.load(f)
    #print(json.dumps(data, indent=4, sort_keys=True))

    x = 0
    for i in data.keys():
        #print(i)
        if i == 'data':
            for j in data[i]:
                x = x + 1
                #print(j)
                #print('[x: ',x,']')
                #print(str(j['BERKASID']))
                try:
                    with connection.cursor() as cursor:
                        sql = "INSERT INTO tb_daftar_penghasilan_negara (alamat_pemohon, berkasid, catatan, di307id, jumlahbiaya, kantorid, kodespopp, namapemohon, namaprosedur, nib, nomor, nomordi305, nomorhak, rnumber, suratlelang, suratpendaftaran,tahun, tanggal, total, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        cursor.execute(sql, (
                            j['ALAMATPEMOHON'], 
                            j['BERKASID'], 
                            j['CATATAN'], 
                            j['DI307ID'], 
                            j['JUMLAHBIAYA'], 
                            j['KANTORID'], 
                            j['KODESPOPP'], 
                            j['NAMAPEMOHON'], 
                            j['NAMAPROSEDUR'], 
                            j['NIB'], 
                            j['NOMOR'], 
                            j['NOMORDI305'], 
                            j['NOMORHAK'], 
                            j['RNUMBER'], 
                            j['SURATLELANG'], 
                            j['SURATPENDAFTARAN'], 
                            j['TAHUN'], 
                            j['TANGGAL'], 
                            j['Total'], 
                            now))
                        # connection is not autocommit by default. So you must commit to save
                        # your changes.
                        # print(cursor.rowcount, "record inserted.")
                        # connection.commit()
                        print ("======================================================================")
                finally:
                    pass

    connection.close()
    
get_data()
get_ipython().run_line_magic('time', '')
'''

# In[ ]:





# # Realisasi PTSL Rupiah Murni Kantah

# In[51]:


@retry((Exception), tries=25, delay=10, backoff=0)
def get_data():

    '''======================================================================================Move to Jawa Timur'''

    # The action/ target from the form
    authentication_url = 'https://ptsl.atrbpn.go.id/Progress'

    # Input parameters we are going to send
    #payload = {
    #  'Id': 'A1DED793DAF0C64DE0400B0A9A144C4A',
    #  'Nama': 'Jatim'  
    #  }

    payload = {
        'tipe': 'RM'
    }

    # Use urllib to encode the payload
    data = urllib.parse.urlencode(payload).encode("utf-8")

    # Build our Request object (supplying 'data' makes it a POST)
    #req = urllib.request.Request(authentication_url, data)
    req = urllib.request.Request(authentication_url)

    # Make the request and read the response
    resp = urllib.request.urlopen(req, data=data)

    html = urllib.request.urlopen(req,data=data).read()

    #bs = BeautifulSoup(html, "html5lib")
    bs = BeautifulSoup(resp, 'html.parser')

    #display(HTML(str(bs.find('table', class_="table")).replace('.', '').replace('K3', 'K3.')))
    data = pd.read_html(str(bs.find('table', class_="table")).replace('.', '').replace('K3', 'K3.').replace('Kab ', 'Kab. '), encoding = 'utf-8', decimal=",", thousands='.')
    df = data[0]

    df.set_index("Wilayah", inplace = True) 
    df=df.sort_index()

    display(df)
    return df
    


# In[52]:


df = get_data()

#print(df)

print('% Capaian PBT: ' + str(df.loc['Jatim', '% Capaian PBT']))
print('% Capaian SHAT: ' + str(df.loc['Jatim', '% Capaian SHAT']))
print('% Capaian K4: ' + str(df.loc['Jatim', '% Capaian K4']))

persen_capaian_pbt = df.loc['Jatim', '% Capaian PBT']
persen_capaian_shat = df.loc['Jatim', '% Capaian SHAT']
persen_capaian_k4 = df.loc['Jatim', '% Capaian K4']


# In[53]:


@retry((Exception), tries=25, delay=10, backoff=0)
def get_data():
    '''======================================================================================Move to Jawa Timur'''

    '''
    <script type="text/javascript">
        $(document).ready(function () {
            $.unblockUI();
            $('#subtitle').html('PTSL Rupiah Murni<br /><br />Tanggal perhitungan 29/09/2020 04:37:21 WIB');
        });
        var showProgressKanwil = function (v, n, p, s, k) {
            $.blockUI({ message: '<div style=\"padding:10px\"><b>Sedang proses... </b><p>harap tunggu</p></div>' });
            $.pjax({
                container: "#htplaceholder",
                type: 'POST',
                url: '/Progress/RekapKantah',
                data: ({ Id: v, Nama: n, RPBT: p, PSHAT: s, PK4: k, Tipe: 'RM' }),
                success: function (data, textStatus, XMLHttpRequest) {
                    $('#htplaceholder').html(data);
                    $('html,body').scrollTop(0);
                },
                error: function (XMLHttpRequest, textStatus, errorThrown) {
                    $.unblockUI();
                }
            });
        }
    </script>
    '''

    #
    # INI BIKIN RESET COOKIE< HARUS  DI COMMENT!
    #
    #
    # Store the cookies and create an opener that will hold them
    #cj = http.cookiejar.CookieJar()
    #opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

    # Add our headers
    opener.addheaders = [("X-Requested-With", "XMLHttpRequest",),('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/70.0')]

    # Install our opener (note that this changes the global opener to the one
    # we just made, but you can also just call opener.open() if you want)
    urllib.request.install_opener(opener)

    # The action/ target from the form
    authentication_url = 'https://ptsl.atrbpn.go.id/Progress/RekapKantah'

    # Input parameters we are going to send
    payload = {
      'Id': satker_id_kanwil,
      'Nama': satker_nama_kanwil,
      'RPBT': persen_capaian_pbt, 
      'PSHAT': persen_capaian_shat, 
      'PK4': persen_capaian_k4, 
      'Tipe': 'RM',
      '_pjax': '#htplaceholder'
      }

    # Use urllib to encode the payload
    data = urllib.parse.urlencode(payload).encode("utf-8")

    # Build our Request object (supplying 'data' makes it a POST)
    req = urllib.request.Request(authentication_url, data)
    #req = urllib.request.Request(authentication_url)

    # Make the request and read the response
    resp = urllib.request.urlopen(req, data=data)

    html = urllib.request.urlopen(req,data=data).read()


    #print(html)
    #bs = BeautifulSoup(html, "html5lib")
    bs = BeautifulSoup(resp, 'html.parser')

    for script in bs.find_all('script'):
        script.extract()

    for i in bs.find_all('i'):
        i.extract()

    soup = BeautifulSoup("<table class='table'><tr>"+
                         "<td>No.</td>"+
                         "<td>Wilayah</td>"+
                         "<td>Target PBT</td>"+
                         "<td>Target SHAT</td>"+
                         "<td>Target K4</td>"+
                         "<td>Survei</td>"+
                         "<td>Pemetaan</td>"+
                         "<td>Puldadis</td>"+
                         "<td>Pemberkasan *</td>"+
                         "<td>Potensi K1</td>"+
                         "<td>K1</td>"+
                         "<td>K2</td>"+
                         "<td>K3.1 *</td>"+
                         "<td>K3.2 *</td>"+
                         "<td>K3.3 *</td>"+
                         "<td>K4</td>"+
                         "<td>KW4,5,6</td>"+
                         # "<td>Unggah BT</td>"+
                         "<td>Siap Diserahkan</td>"+
                         "<td>Diserahkan</td>"+
                         "<td>K1 PBT Sebelumnya</td>"+
                         "<td>% Capaian PBT</td>"+
                         "<td>% Capaian SHAT</td>"+
                         "<td>% Capaian K4</td>"+
                         "</tr></table>", "lxml")
    tag = soup.table
    tag.append(bs)    

    #data = pd.read_html(str(tag).replace('Kab. ','Kabupaten '), header=0, flavor = 'bs4', encoding = 'utf-8', decimal=",", thousands='.')
    #df = data[0]

    #del df['No.']

    #df.set_index("Wilayah", inplace = True) 
    #df=df.sort_index()

    #print(df.columns.tolist())
    #df = df.drop(index='Kota Madiun')
    #df
    
get_data()
get_ipython().run_line_magic('time', '')


# In[ ]:





# In[54]:


@retry((Exception), tries=25, delay=10, backoff=0)
def get_data():
    print('\n=> Progres Kantah\n')
    '''=============================================Progres Kantah'''
    '''
    <script type="text/javascript">
        $(document).ready(function () {
            $.unblockUI();
            $('#subtitle').html('PTSL Rupiah Murni Provinsi Jatim<br /><br />Tanggal perhitungan 20/10/2021 04:36:52 WIB');
        });
        var showProgressKantah = function (v, n) {
            $.blockUI({ message: '<div style=\"padding:10px\"><b>Sedang proses... </b><p>harap tunggu</p></div>' });
            $.pjax({
                container: "#panelplaceholder",
                type: 'POST',
                url: '/Progress/HeaderKantah',
                data: ({ Id: v, Nama: n, Tipe: 'RM' }),
                success: function (data, textStatus, XMLHttpRequest) {
                    $('#panelplaceholder').html(data);
                    $('html,body').scrollTop(0);
                },
                error: function (XMLHttpRequest, textStatus, errorThrown) {
                    $.unblockUI();
                }
            });
        }
    </script>
    '''

    # The action/ target from the form
    authentication_url = 'https://ptsl.atrbpn.go.id/Progress/HeaderKantah'

    # Input parameters we are going to send
    payload = {
        'Id': satker_id_kantah,
        'Nama': satker_nama_kantah,
        'Tipe': 'RM'
    }

    # Use urllib to encode the payload
    data = urllib.parse.urlencode(payload).encode("utf-8")

    # Build our Request object (supplying 'data' makes it a POST)
    #req = urllib.request.Request(authentication_url, data)
    req = urllib.request.Request(authentication_url)

    # Make the request and read the response
    resp = urllib.request.urlopen(req, data=data)

    #with urllib.request.urlopen(req,data=data) as f:
    #    resp = f.read()
    #display(resp)

    html = urllib.request.urlopen(req, data=data).read()
    bs = BeautifulSoup(html, "html5lib")

    #display(HTML(str(bs.find('table', class_="table")).replace('.', '')))
    data = pd.read_html(str(bs.find('table', class_="table")).replace('.', ''))

    df = data[0]

    del df['No']
    df.set_index("Desa/Kelurahan", inplace=True)

    print(getCurrentDate(True))
    return df


# In[ ]:





# In[55]:


df = get_data()

print(df)
#for col_name, data in df.items():
#	print("col_name:", col_name, "- data:", data)

now = getCurrentDate(True)
connection = pymysql.connect(**config_mysql)

with connection.cursor() as cursor:
    # Create a new record
    sql = "TRUNCATE `tb_progres_ptsl_kantah`"
    cursor.execute(sql)
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    print(cursor.rowcount, " current records.")
    connection.commit()

for index, row in df.iterrows():
    print(index, row['Puldadis'])
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `tb_progres_ptsl_kantah` (desa_kelurahan, target_pbt, target_shat, target_k4, survei, pemetaan, puldadis, pemberkasan, potensi_k1, k1, k2, k31, k32, k33, k4, unggah_bt, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s)"
            cursor.execute(sql, (index, str(row['Target PBT']), str(row['Target SHAT']), str(row['Target K4']), str(row['Survei']), str(row['Pemetaan']), str(row['Puldadis']), str(row['Pemberkasan *']), str(row['Potensi K1']), str(row['K1']), str(row['K2']), str(row['K31 *']), str(row['K32 *']), str(row['K33 *']), str(row['K4']), str(0), now))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            #print(cursor.rowcount, "record inserted.")
            connection.commit()
        #with connection.cursor() as cursor:
            # Read a single record
            #sql = "SELECT * FROM `tb_progres_ptsl_kantah` ORDER BY id DESC"
            #cursor.execute(sql, ())
            #result = cursor.fetchone()
            #print(result)
    finally:
        #connection.close()
        pass
connection.close()
    


# In[ ]:





# # Re-Login SSO

# In[56]:


login()
get_ipython().run_line_magic('time', '')


# # Early Warning

# ## Rekapitulasi Bidang Tanah Tanpa Data Yuridis Kantah

# In[57]:


@retry((Exception), tries=25, delay=10, backoff=0)
def get_data():
    print('\n=> Rekapitulasi Bidang Tanah Tanpa Data Yuridis Kantah\n')
    '''=============================================Rekapitulasi Bidang Tanah Tanpa Data Yuridis Kantah'''

    '''
    <script type="text/javascript">
        $(document).ready(function () {
            $.unblockUI();
        });

        var showTanpaYuridisKantah = function (v, n) {
            $.blockUI({ message: '<div style=\"padding:10px\"><b>Sedang proses... </b><p>harap tunggu</p></div>' });
            $.pjax({
                container: "#right_col",
                type: 'POST',
                url: '/EarlyWarning/TanpaYuridisKantah',
                data: ({ Id: v, Nama: n }),
                success: function (data, textStatus, XMLHttpRequest) {
                    $('#right_col').html(data);
                },
                error: function (XMLHttpRequest, textStatus, errorThrown) {
                    $.unblockUI();
                }
            });
        }
    </script>

    '''

    # The action/ target from the form
    authentication_url = 'https://ptsl.atrbpn.go.id/EarlyWarning/TanpaYuridisKantah'

    # Input parameters we are going to send
    payload = {
      'Id': satker_id_kantah,
      'Nama': satker_nama_kantah
      }

    # Use urllib to encode the payload
    data = urllib.parse.urlencode(payload).encode("utf-8")

    # Build our Request object (supplying 'data' makes it a POST)
    #req = urllib.request.Request(authentication_url, data)
    req = urllib.request.Request(authentication_url)

    # Make the request and read the response
    resp = urllib.request.urlopen(req, data=data)

    #with urllib.request.urlopen(req,data=data) as f:
    #    resp = f.read()
        #display(resp)

    html = urllib.request.urlopen(req,data=data).read()
    bs = BeautifulSoup(html, "html5lib")

    #display(HTML(str(bs.find('table', class_="table")).replace('.', '')))
    data = pd.read_html(str(bs.find('table', class_="table")).replace('.', ''))

    df = data[0]
    df.set_index("Desa", inplace = True)
    print(getCurrentDate(True))

    return df


# In[58]:


df = get_data()
now = getCurrentDate(True)
connection = pymysql.connect(**config_mysql)
for index, row in df.iterrows():
    if index != '#':
        #print(index, row['Nama Desa'])
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `tb_early_warning_bidang_tanah_tanpa_data_yuridis_kantah` (desa, kecamatan, jumlah, created_at) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (index, str(row['Kecamatan']), str(row['Jumlah']), now))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            #print(cursor.rowcount, "record inserted.")
            connection.commit()
        
connection.close()
get_ipython().run_line_magic('time', '')


# ## Rekapitulasi Pengumuman Kedaluwarsa Kantah

# In[59]:


@retry((Exception), tries=25, delay=10, backoff=0)
def get_data():
    print('\n=> Rekapitulasi Pengumuman Kedaluwarsa Kantah\n')
    '''=============================================Rekapitulasi Pengumuman Kedaluwarsa Kantah'''

    '''
    <script type="text/javascript">
        $(document).ready(function () {
            $.unblockUI();
        });

        var showPengumumanKantah = function (v, n) {
            $.blockUI({ message: '<div style=\"padding:10px\"><b>Sedang proses... </b><p>harap tunggu</p></div>' });
            $.pjax({
                container: "#right_col",
                type: 'POST',
                url: '/EarlyWarning/PengumumanKantah',
                data: ({ Id: v, Nama: n }),
                success: function (data, textStatus, XMLHttpRequest) {
                    $('#right_col').html(data);
                },
                error: function (XMLHttpRequest, textStatus, errorThrown) {
                    $.unblockUI();
                }
            });
        }
    </script>

    '''

    # The action/ target from the form
    authentication_url = 'https://ptsl.atrbpn.go.id/EarlyWarning/PengumumanKantah'

    # Input parameters we are going to send
    payload = {
      'Id': satker_id_kantah,
      'Nama': satker_nama_kantah
      }

    # Use urllib to encode the payload
    data = urllib.parse.urlencode(payload).encode("utf-8")

    # Build our Request object (supplying 'data' makes it a POST)
    #req = urllib.request.Request(authentication_url, data)
    req = urllib.request.Request(authentication_url)

    # Make the request and read the response
    resp = urllib.request.urlopen(req, data=data)

    #with urllib.request.urlopen(req,data=data) as f:
    #    resp = f.read()
        #display(resp)

    html = urllib.request.urlopen(req,data=data).read()
    bs = BeautifulSoup(html, "html5lib")

    #display(HTML(str(bs.find('table', class_="table")).replace('.', '')))
    data = pd.read_html(str(bs.find('table', class_="table")).replace('.', ''))

    df = data[0]
    df.set_index("Desa", inplace = True)
    print(getCurrentDate(True))

    return df


# In[60]:


df = get_data()
now = getCurrentDate(True)
connection = pymysql.connect(**config_mysql)
for index, row in df.iterrows():
    if index != '#':
        #print(index, row['Nama Desa'])
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `tb_early_warning_pengumuman_kadaluwarsa_kantor_pertanahan` (desa, kecamatan, jumlah, created_at) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (index, str(row['Kecamatan']), str(row['Jumlah']), now))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            #print(cursor.rowcount, "record inserted.")
            connection.commit()
        
connection.close()
get_ipython().run_line_magic('time', '')


# ## Rekapitulasi Berkas Tanpa Bidang Tanah Kantah

# In[61]:


@retry((Exception), tries=25, delay=10, backoff=0)
def get_data():
    print('\n=> Rekapitulasi Berkas Tanpa Bidang Tanah Kantah\n')
    '''=============================================Rekapitulasi Berkas Tanpa Bidang Tanah Kantah'''

    '''
    <script type="text/javascript">
        $(document).ready(function () {
            $.unblockUI();
        });

        var showTanpaFisikKantah = function (v, n) {
            $.blockUI({ message: '<div style=\"padding:10px\"><b>Sedang proses... </b><p>harap tunggu</p></div>' });
            $.pjax({
                container: "#right_col",
                type: 'POST',
                url: '/EarlyWarning/TanpaFisikKantah',
                data: ({ Id: v, Nama: n }),
                success: function (data, textStatus, XMLHttpRequest) {
                    $('#right_col').html(data);
                },
                error: function (XMLHttpRequest, textStatus, errorThrown) {
                    $.unblockUI();
                }
            });
        }
    </script>

    '''

    # The action/ target from the form
    authentication_url = 'https://ptsl.atrbpn.go.id/EarlyWarning/TanpaFisikKantah'

    # Input parameters we are going to send
    payload = {
      'Id': satker_id_kantah,
      'Nama': satker_nama_kantah
      }

    # Use urllib to encode the payload
    data = urllib.parse.urlencode(payload).encode("utf-8")

    # Build our Request object (supplying 'data' makes it a POST)
    #req = urllib.request.Request(authentication_url, data)
    req = urllib.request.Request(authentication_url)

    # Make the request and read the response
    resp = urllib.request.urlopen(req, data=data)

    #with urllib.request.urlopen(req,data=data) as f:
    #    resp = f.read()
        #display(resp)

    html = urllib.request.urlopen(req,data=data).read()
    bs = BeautifulSoup(html, "html5lib")

    #display(HTML(str(bs.find('table', class_="table")).replace('.', '')))
    data = pd.read_html(str(bs.find('table', class_="table")).replace('.', ''))

    df = data[0]
    df.set_index("Desa", inplace = True)
    print(getCurrentDate(True))

    return df


# In[62]:


df = get_data()
now = getCurrentDate(True)
connection = pymysql.connect(**config_mysql)
for index, row in df.iterrows():
    if index != '#':
        #print(index, row['Nama Desa'])
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `tb_early_warning_berkas_tanpa_bidang_tanah` (desa, kecamatan, jumlah, created_at) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (index, str(row['Kecamatan']), str(row['Jumlah']), now))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            #print(cursor.rowcount, "record inserted.")
            connection.commit()
        
connection.close()
get_ipython().run_line_magic('time', '')


# ## Rekapitulasi Berkas Tanpa Pemohon Kantah

# In[63]:


@retry((Exception), tries=25, delay=10, backoff=0)
def get_data():
    print('\n=> Rekapitulasi Berkas Tanpa Pemohon Kantah\n')
    '''=============================================Rekapitulasi Berkas Tanpa Pemohon Kantah'''

    '''
    <script type="text/javascript">
        $(document).ready(function () {
            $.unblockUI();
        });
        var showKantah = function (v, n) {
            $.blockUI({ message: '<div style=\"padding:10px\"><b>Sedang proses... </b><p>harap tunggu</p></div>' });
            $.pjax({
                container: "#right_col",
                type: 'POST',
                url: '/EarlyWarning/BerkasTanpaPemohonKantah',
                data: ({ Id: v, Nama: n }),
                success: function (data, textStatus, XMLHttpRequest) {
                    $('#right_col').html(data);
                },
                error: function (XMLHttpRequest, textStatus, errorThrown) {
                    $.unblockUI();
                }
            });
        }
    </script>

    '''

    # The action/ target from the form
    authentication_url = 'https://ptsl.atrbpn.go.id/EarlyWarning/BerkasTanpaPemohonKantah'

    # Input parameters we are going to send
    payload = {
      'Id': satker_id_kantah,
      'Nama': satker_nama_kantah
      }

    # Use urllib to encode the payload
    data = urllib.parse.urlencode(payload).encode("utf-8")

    # Build our Request object (supplying 'data' makes it a POST)
    #req = urllib.request.Request(authentication_url, data)
    req = urllib.request.Request(authentication_url)

    # Make the request and read the response
    resp = urllib.request.urlopen(req, data=data)

    #with urllib.request.urlopen(req,data=data) as f:
    #    resp = f.read()
        #display(resp)

    html = urllib.request.urlopen(req,data=data).read()
    bs = BeautifulSoup(html, "html5lib")

    #display(HTML(str(bs.find('table', class_="table")).replace('.', '')))
    data = pd.read_html(str(bs.find('table', class_="table")).replace('.', ''))

    df = data[0]
    df.set_index("Desa", inplace = True)
    print(getCurrentDate(True))

    return df


# In[64]:


df = get_data()
now = getCurrentDate(True)
connection = pymysql.connect(**config_mysql)
for index, row in df.iterrows():
    if index != '#':
        #print(index, row['Nama Desa'])
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `tb_early_warning_berkas_tanpa_pemohon` (desa, kecamatan, jumlah, created_at) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (index, str(row['Kecamatan']), str(row['Jumlah']), now))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            #print(cursor.rowcount, "record inserted.")
            connection.commit()
        
connection.close()
get_ipython().run_line_magic('time', '')


# In[ ]:





# In[65]:


print('\n=> Finished')
print(getCurrentDate(True))
elapsed_time = time.time() - start_time
print('%f minutes:' % (float(elapsed_time/60)))
print('\n')


# In[66]:


#send_mail("dimasardi1349@gmail.com", "Bot Scrap Done", '[%s] Hi!\n<i>Bot Scrap</i> task done in %f minutes:' % (getCurrentDate(True), float(elapsed_time/60)))


# In[ ]:




