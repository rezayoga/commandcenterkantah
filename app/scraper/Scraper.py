#!/usr/bin/env python
# coding: utf-8

# 
# # *Bot Scraper Command Center Kantor Pertanahan
# ---
# * Crafted by: [**Reza Yogaswara**](http://me.rezayogaswara.com)
# * Output Report: SQL Data

# In[44]:


from datetime import datetime, timedelta, date
import datetime as dt
import time, os

os.environ['TZ'] = 'Asia/Jakarta'
time.tzset()

hari_ini = date.today()
start_time = time.time()


# In[45]:


#from IPython.core.interactiveshell import InteractiveShell
#InteractiveShell.ast_node_interactivity = "all"


# In[ ]:





# In[46]:


print('\n=> Crafted by: Reza D Yogaswara | me@rezayogaswara.com')
print('\n=> Output Report: SQL / Progres Kegiatan APBN dan Rutin Kantor Pertanahan')


# In[ ]:





# # Bot Init!

# In[47]:


print('\n=> Bot Init!\n')
import time
start_time = time.time()


# In[48]:


get_ipython().system('python -V')


# In[49]:


import pandas as pd


# In[50]:


pd.show_versions(as_json=False)


# In[ ]:





# # Variables

# In[51]:


username = ''
password = ''
satker_id_kanwil = 'A1DED793DAF0C64DE0400B0A9A144C4A'
satker_kanwil = 'Jatim'
satker_id_kantah = ''
satker_nama_kantah = ''
satker_nama_kantah_pendek = ''
mysql_host = 'localhost'
mysql_port = 3306
mysql_user = 'root'
mysql_password = 'pmnP_AkjWk26x2020'
mysql_database = 'db_c2s_kantah'


# In[52]:


import pymysql
# Connect to the database


# In[53]:


config_mysql = {
    "host": mysql_host,
    "port": mysql_port,
    "user": mysql_user,
    "passwd": mysql_password,
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor,
    "database": mysql_database
}


connection = pymysql.connect(**config_mysql)
results = None
try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `tb_config` WHERE `key` = 'BOT_USERNAME'"
        cursor.execute(sql)
        result = cursor.fetchone()
        username = result['value']
        
        sql = "SELECT * FROM `tb_config` WHERE `key` = 'BOT_PASSWORD'"
        cursor.execute(sql)
        result = cursor.fetchone()
        password = result['value']
        
        sql = "SELECT * FROM `tb_config` WHERE `key` = 'ID_SATKER'"
        cursor.execute(sql)
        result = cursor.fetchone()
        satker_id_kantah = result['value']
        
        sql = "SELECT * FROM `tb_config` WHERE `key` = 'SATKER'"
        cursor.execute(sql)
        result = cursor.fetchone()
        satker_nama_kantah = result['value']
        
        
        sql = "SELECT * FROM `tb_config` WHERE `key` = 'SATKER_PENDEK'"
        cursor.execute(sql)
        result = cursor.fetchone()
        satker_nama_kantah_pendek = result['value']
        
        print(f"{username}//{password}//{satker_id_kantah}//{satker_nama_kantah}//{satker_nama_kantah_pendek}")
finally:
    connection.close()
   
get_ipython().run_line_magic('time', '')


# In[ ]:





# In[54]:


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


# In[55]:


import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(to, subject, text):
    # me == my email address
    # you == recipient's email address
    me = "botsystem.kantahnganjuk@pusakha.id"
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
        <title>Command Center System Kantor Pertanahan</title>
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
                <span class="preheader">Command Center System Kantor Pertanahan</span>
                <table class="main">

                  <!-- START MAIN CONTENT AREA -->
                  <tr>
                    <td class="wrapper">
                      <table border="0" cellpadding="0" cellspacing="0">
                        <tr>
                          <td>
                            <p><img src="https://c2ssetup.pusakha.id/static/images/logo_fit_small.png" alt="Command Center System Kantor Pertanahan" height="70" border="0" style="border:0; outline:none; text-decoration:none; display:block;"></p>
                            <p>&nbsp;</p>
                            <p>""" + text + """</p>
                            <p>&nbsp;</p>
                            <p>Regards,<br />🤖 C2S Kantor Pertanahan</p>
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
                        <span class="apple-link">Command Center System Kantor Pertanahan</span>
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
    mail = smtplib.SMTP('mail.pusakha.id', 25)
    mail.ehlo()
    mail.starttls()
    mail.login(me, "@R0boT_")
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    mail.sendmail(me, to, msg.as_string())
    mail.quit()


# In[56]:


#send_mail('reza.yoga@gmail.com', 'Bot Scrap Init', '[%s] Hi!\n<i>Bot Scrap</i> init:' % (getCurrentDate(True)))


# In[ ]:





# # Login SSO

# In[57]:


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
      'IpPublic': '207.138.123.123',
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

# In[58]:


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


# In[59]:


df = get_data()
display(df)
#df.loc['Tim Panitia/Tim Peneliti Tanah', :]

get_ipython().run_line_magic('time', '')


# In[ ]:





# In[60]:


# for col_name, data in df.items():
#	print("col_name:", col_name, "- data:", data)  
#	print("----------------------------------------------------------------------")


# In[ ]:





# In[61]:


# Example format: "21/10/2021 - 21/10/2021"
def getCurrentDateFilterPenghasilanNegaraDI307():
    return '%s/%s/%s - %s/%s/%s' % (time.strftime('%d'), time.strftime('%m'), time.strftime('%Y'), time.strftime('%d'), time.strftime('%m'), time.strftime('%Y'))


# In[62]:


print(getCurrentDateFilterPenghasilanNegaraDI307())


# In[ ]:





# In[63]:


connection = pymysql.connect(**config_mysql)
now = getCurrentDate(True)

'''
with connection.cursor() as cursor:
    # Create a new record
    sql = "TRUNCATE `tb_daftar_tunggakan_berkas_pnbp_per_jabatan`"
    cursor.execute(sql)
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    print(cursor.rowcount, " current records.")
    connection.commit()
'''

for index, row in df.iterrows():
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `tb_daftar_tunggakan_berkas_pnbp_per_jabatan` (jabatan, jumlah_berkas, sesuai_durasi, hampir_jatuh_tempo, sudah_jatuh_tempo, created_at) VALUES (%s, %s, %s, %s, %s, %s)"
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





# In[64]:


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
    authentication_url = 'https://kkp2.atrbpn.go.id/bo/Monitoring/DaftarTunggakanBerkasProsedur'

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
                         "<td>layanan</td>"+
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


    df.set_index("layanan", inplace = True) 
    #df=df.sort_index()

    #print(df.columns.tolist())
    return df


# In[65]:


df = get_data()
display(df)
#df.loc['Tim Panitia/Tim Peneliti Tanah', :]

get_ipython().run_line_magic('time', '')


# In[ ]:





# In[66]:


connection = pymysql.connect(**config_mysql)
now = getCurrentDate(True)

'''
with connection.cursor() as cursor:
    # Create a new record
    sql = "TRUNCATE `tb_daftar_tunggakan_berkas_pnbp_per_layanan`"
    cursor.execute(sql)
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    print(cursor.rowcount, " current records.")
    connection.commit()
'''

for index, row in df.iterrows():
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"INSERT INTO `tb_daftar_tunggakan_berkas_pnbp_per_layanan` (layanan, jumlah_berkas, sesuai_durasi, hampir_jatuh_tempo, sudah_jatuh_tempo, created_at) VALUES ('{index}', '{str(row['jumlah_berkas'])}', '{str(row['sesuai_durasi'])}', '{str(row['hampir_jatuh_tempo'])}', '{str(row['sudah_jatuh_tempo'])}', '{now}')"
            cursor.execute(sql)
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





# # Tunggakan Penerimaan Dimuka

# ## Tahunan

# In[67]:


from urllib.error import URLError
@retry((Exception), tries=25, delay=10, backoff=0)
def get_data(th):
    """
     var showTunggakanKanwil = function (v, n) {
        $.blockUI({ message: '<div style=\"padding:10px\"><b>Sedang proses... </b><p>harap tunggu</p></div>' });
        $.ajax({
            type: 'POST',
            url: '/Keuangan/TunggakanTriwulanKanwil',
            data: ({ Kt: $('#Kategori').val(), Nm: $('#Kategori :selected').text(), Th: $('#TahunBerkas').val(), Id: v, NamaKantor: n }),
            success: function (data, textStatus, XMLHttpRequest) {
                $('#dataplaceholder').html(data);
                //$.unblockUI();
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                $.unblockUI();
            }
        });
    };
    """
    
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
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/70.0')]

    # Install our opener (note that this changes the global opener to the one
    # we just made, but you can also just call opener.open() if you want)
    urllib.request.install_opener(opener)

    # The action/ target from the form
    authentication_url = 'https://statistik.atrbpn.go.id/Keuangan/TunggakanTriwulanKanwil'

    # Input parameters we are going to send
    
    #print(f"{th}/{satker_id_kanwil}/{satker_kanwil}")
    
    payload = {
        "Kt": "",
        "Nm": "Pilih kategori",
        "Th": th,
        "Id": satker_id_kanwil,
        "NamaKantor": satker_kanwil
    }
    
    # Use urllib to encode the payload
    data = urllib.parse.urlencode(payload).encode("utf-8")

    #print(data)
    
    # Build our Request object (supplying 'data' makes it a POST)
    req = urllib.request.Request(url=authentication_url, data=data)
    #req = urllib.request.Request(authentication_url)

    # Make the request and read the response
    resp = urllib.request.urlopen(req, data=data)
    
    #print(resp.info())
    
    html = urllib.request.urlopen(req,data=data).read()
    
    #print(html)
    #bs = BeautifulSoup(html, "html5lib")
    bs = BeautifulSoup(resp, 'html.parser')
    
    #print(bs)

    for script in bs.find_all('script'):
        script.extract()

    for i in bs.find_all('i'):
        i.extract()

    for i in bs.find_all('style'):
        i.extract()
    soup = BeautifulSoup("<table class='table'><tr>"+
                         "<td>no</td>"+
                         "<td>kantah</td>"+
                         "<td>jumlah_tunggakan</td>"+
                         "<td>nilai_tunggakan</td>"+
                         "</tr></table>", "lxml")
    tag = soup.table
    tag.append(bs)    

    data = pd.read_html(str(tag), header=0, flavor = 'bs4', decimal=",", thousands='.')
    
    #print(data)
    
    df = data[1]

    del df['No.']


    df.set_index("Kantah", inplace = True) 
    #df=df.sort_index()

    #print(df.columns.tolist())
    return df


# In[69]:


connection = pymysql.connect(**config_mysql)
now = getCurrentDate(True)

for i in range(2015, 2021, 1):
    df = get_data(i)
    #display(df)
    #print(i)
    print(f"Jumlah Tunggakan: {df.loc[satker_nama_kantah_pendek, 'Jumlah Tunggakan']}")
    print(f"Nilai Tunggakan: {df.loc[satker_nama_kantah_pendek, 'Nilai Tunggakan']}")
    print(f"Tahun Tunggakan: {i}")
    print("-----------------------------")
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `tb_tunggakan_penerimaan_dimuka_tahunan` (kantah, jumlah_tunggakan, nilai_tunggakan, tahun, created_at) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (satker_nama_kantah_pendek, str(df.loc[satker_nama_kantah_pendek, 'Jumlah Tunggakan']), str(df.loc[satker_nama_kantah_pendek, 'Nilai Tunggakan']), str(i), now))
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
print('"Daftar Tunggakan Penerimaan Dimuka Tahunan" done!')
get_ipython().run_line_magic('time', '')


# In[ ]:





# ## Bulanan

# In[85]:


#connection = pymysql.connect(**config_mysql)
now = getCurrentDate(True)
'''
with connection.cursor() as cursor:
    # Create a new record
    sql = "TRUNCATE `tb_tunggakan_penerimaan_dimuka_bulanan`"
    cursor.execute(sql)
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    print(cursor.rowcount, " current records.")
    connection.commit()
'''

@retry((Exception), tries=25, delay=10, backoff=0)
def get_data(kt, nm):
    scrap_link = ''
    connection = pymysql.connect(**config_mysql)
    """
     var showTunggakanKanwil = function (v, n) {
        $.blockUI({ message: '<div style=\"padding:10px\"><b>Sedang proses... </b><p>harap tunggu</p></div>' });
        $.ajax({
            type: 'POST',
            url: '/Keuangan/TunggakanTriwulanKanwil',
            data: ({ Kt: $('#Kategori').val(), Nm: $('#Kategori :selected').text(), Th: $('#TahunBerkas').val(), Id: v, NamaKantor: n }),
            success: function (data, textStatus, XMLHttpRequest) {
                $('#dataplaceholder').html(data);
                //$.unblockUI();
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                $.unblockUI();
            }
        });
    };
    """
    
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
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/70.0')]

    # Install our opener (note that this changes the global opener to the one
    # we just made, but you can also just call opener.open() if you want)
    urllib.request.install_opener(opener)

    # The action/ target from the form
    authentication_url = 'https://statistik.atrbpn.go.id/Keuangan/TunggakanTriwulanKanwil'

    # Input parameters we are going to send
    
    #print(f"{kt}/{nm}/{satker_id_kanwil}/{satker_kanwil}")
    
    #print(f"{nm.split()[0]}")
    #print(f"{nm.split()[1]}")
    
    payload = {
        "Kt": kt,
        "Nm": nm,
        "Th": "",
        "Id": satker_id_kanwil,
        "NamaKantor": satker_kanwil
    }
    
    # Use urllib to encode the payload
    data = urllib.parse.urlencode(payload).encode("utf-8")

    #print(data)
    
    # Build our Request object (supplying 'data' makes it a POST)
    req = urllib.request.Request(url=authentication_url, data=data)
    #req = urllib.request.Request(authentication_url)

    # Make the request and read the response
    resp = urllib.request.urlopen(req, data=data)
    
    #print(resp.info())
    
    html = urllib.request.urlopen(req,data=data).read()
    
    #print(html)
    #bs = BeautifulSoup(html, "html5lib")
    bs = BeautifulSoup(resp, 'html.parser')
    
    #print(bs)
    
    for a in bs.find_all("a", string=satker_nama_kantah_pendek):
        scrap_link = a['href']
        #print(f"LINK: {scrap_link}")
    
    for script in bs.find_all('script'):
        script.extract()

    for i in bs.find_all('i'):
        i.extract()
        
    for i in bs.find_all('style'):
        i.extract()

    soup = BeautifulSoup("<table class='table'><tr>"+
                         "<td>no</td>"+
                         "<td>kantah</td>"+
                         "<td>jumlah_tunggakan</td>"+
                         "<td>nilai_tunggakan</td>"+
                         "</tr></table>", "lxml")
    tag = soup.table
    tag.append(bs)   
    
    #print(tag)

    data = pd.read_html(str(tag), header=0, flavor = 'bs4', decimal=",", thousands='.')
    
    #print(data)
    
    df = data[1]
    del df['No.']


    df.set_index("Kantah", inplace = True) 
    #df=df.sort_index()

    #print(df.columns.tolist())

    print(f"Jumlah Tunggakan: {df.loc[satker_nama_kantah_pendek, 'Jumlah Tunggakan']}")
    print(f"Nilai Tunggakan: {df.loc[satker_nama_kantah_pendek, 'Nilai Tunggakan']}")
    print("-----------------------------")
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"INSERT INTO `tb_tunggakan_penerimaan_dimuka_bulanan` (kantah, jumlah_tunggakan, nilai_tunggakan, idx, bulan, tahun, created_at) VALUES ('{satker_nama_kantah_pendek}', '{str(df.loc[satker_nama_kantah_pendek, 'Jumlah Tunggakan'])}', '{str(df.loc[satker_nama_kantah_pendek, 'Nilai Tunggakan'])}', '{kt}', '{nm.split()[0]}', '{nm.split()[1]}', '{now}')"
            print(sql)
            cursor.execute(sql)
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
    
    return scrap_link


# In[86]:


#df = get_data('0', 'Desember 2021')
'''
'0', 'Desember 2021'
'1', 'Januari 2022'
'2', 'Februari 2022'
'3', 'Maret 2022'
'4', 'April 2022'
'5', 'Mei 2022'
'6', 'Juni 2022'
'7', 'Juli 2022'
'8', 'Agustus 2022'
'9', 'September 2022'
'10', 'Oktober 2022'
'12', 'November 2022'
'13', 'Desember 2022'
'''

scrap_link = get_data('0', 'Desember 2021')


print(scrap_link)

scrap_link = get_data('1', 'Januari 2022')
scrap_link = get_data('2', 'Februari 2022')
scrap_link = get_data('3', 'Maret 2022')
scrap_link = get_data('4', 'April 2022')
scrap_link = get_data('5', 'Mei 2022')
scrap_link = get_data('6', 'Juni 2022')
scrap_link = get_data('7', 'Juli 2022')
scrap_link = get_data('8', 'Agustus 2022')
scrap_link = get_data('9', 'September 2022')
scrap_link = get_data('10', 'Oktober 2022')
scrap_link = get_data('11', 'November 2022')
scrap_link = get_data('12', 'Desember 2022')

#display(df)

print(scrap_link)

get_ipython().run_line_magic('time', '')


# In[ ]:





# ## Detail Tunggakan

# In[87]:


@retry((Exception), tries=1, delay=10, backoff=0)
def get_data(page_num, scrap_link):
    """
     var showTunggakanKanwil = function (v, n) {
        $.blockUI({ message: '<div style=\"padding:10px\"><b>Sedang proses... </b><p>harap tunggu</p></div>' });
        $.ajax({
            type: 'POST',
            url: '/Keuangan/TunggakanTriwulanKanwil',
            data: ({ Kt: $('#Kategori').val(), Nm: $('#Kategori :selected').text(), Th: $('#TahunBerkas').val(), Id: v, NamaKantor: n }),
            success: function (data, textStatus, XMLHttpRequest) {
                $('#dataplaceholder').html(data);
                //$.unblockUI();
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                $.unblockUI();
            }
        });
    };
    """
    
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
    authentication_url = f'https://statistik.atrbpn.go.id/{scrap_link}'
    # Input parameters we are going to send
    
    #print(f"{page_num}")
    
    payload = {
        "pageNum": page_num
    }
    
    # Use urllib to encode the payload
    data = urllib.parse.urlencode(payload).encode("utf-8")

    #print(data)
    
    # Build our Request object (supplying 'data' makes it a POST)
    req = urllib.request.Request(url=authentication_url, data=data)
    #req = urllib.request.Request(authentication_url)

    # Make the request and read the response
    resp = urllib.request.urlopen(req, data=data)
    
    #print(resp.info())
    
    html = urllib.request.urlopen(req,data=data).read()
    
    #print(html)
    #bs = BeautifulSoup(html, "html5lib")
    bs = BeautifulSoup(resp, 'html.parser')
    
    #print(bs)

    for script in bs.find_all('script'):
        script.extract()

    for i in bs.find_all('i'):
        i.extract()
    
    soup = BeautifulSoup("<table class='table'><tr>"+
                         "<td>no</td>"+
                         "<td>nomor_305</td>"+
                         "<td>tanggal_305</td>"+
                         "<td>besarnya</td>"+
                         "<td>nama_pemohon</td>"+
                         "<td>nomor_berkas</td>"+
                         "<td>nama_prosedur</td>"+
                         "<td>kode_billing</td>"+
                         "<td>ntpn</td>"+
                         "<td>alas_hak</td>"+
                         "<td>nomor_sk</td>"+
                         "<td>nomor_hak</td>"+
                         "<td>di_penyelesaian</td>"+
                         "<td>tgl_selesai</td>"+
                         "<td>nama_profile</td>"+
                         "</tr></table>", "lxml")
    tag = soup.table
    tag.append(bs)    

    data = pd.read_html(str(tag).replace('\'', ''), header=0, flavor = 'bs4', decimal=",", thousands='.')
    
    #print(data)
    
    df = data[0]

    #del df['no']

    df.set_index("nomor_305", inplace = True) 
    #df=df.sort_index()

    #print(df.columns.tolist())
    return df


# In[89]:


#df = get_data(0)
#display(df)
import json
connection = pymysql.connect(**config_mysql)
now = getCurrentDate(True)

'''
with connection.cursor() as cursor:
    # Create a new record
    sql = "TRUNCATE `tb_tunggakan_penerimaan_dimuka_detail_permohonan`"
    cursor.execute(sql)
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    print(cursor.rowcount, " current records.")
    connection.commit()
'''

for i in range(200):
    df = get_data(i, scrap_link)
    #display(df)
    
    for index, row in df.iterrows():
        #print(str(row['no']))
    
        try:
            with connection.cursor() as cursor:
                # Create a new record
                
                sql = f"""SELECT * FROM `tb_tunggakan_penerimaan_dimuka_detail_permohonan` 
                        WHERE nomor_305 = '{str(index)}' AND 
                        tanggal_305 = '{str(row['tanggal_305'])}' AND 
                        nomor_berkas = '{str(row['nomor_berkas'])}' AND 
                        nama_prosedur = '{str(row['nama_prosedur'])}' AND 
                        kode_billing = '{str(row['kode_billing'])}' AND 
                        ntpn = '{str(row['ntpn'])}'
                        ORDER BY id DESC"""
                
                cursor.execute(sql)
                #print(cursor.rowcount)
                #print(json.dumps(cursor.fetchall(), indent=2))
                
                if cursor.rowcount == 0:
                    sql = f"INSERT INTO `tb_tunggakan_penerimaan_dimuka_detail_permohonan` (nomor_305, tanggal_305, besarnya, nama_pemohon, nomor_berkas, nama_prosedur, kode_billing, ntpn, alas_hak, nomor_sk, nomor_hak, di_penyelesaian, tgl_selesai, nama_profile, created_at) VALUES ('{str(index)}', '{str(row['tanggal_305'])}', '{str(row['besarnya'])}', '{str(row['nama_pemohon'])}', '{str(row['nomor_berkas'])}', '{str(row['nama_prosedur'])}', '{str(row['kode_billing'])}', '{str(row['ntpn'])}', '{str(row['alas_hak'])}', '{str(row['nomor_sk'])}', '{str(row['nomor_hak'])}', '{str(row['di_penyelesaian'])}', '{str(row['tgl_selesai'])}', '{str(row['nama_profile'])}', '{now}')"
                    cursor.execute(sql)
                
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
print('"Daftar Tunggakan Penerimaan Dimuka Detail Permohonan" done!')
get_ipython().run_line_magic('time', '')


# In[ ]:





# # Informasi Detail Berkas

# In[ ]:


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

for x in range(0, 750):
    print(str(x) + ' ' + '(' + getCurrentDate(True) + ')')
    getBTN(x)

    
connection.close()

print('"Informasi Detail Berkas" done!')
get_ipython().run_line_magic('time', '')


# In[ ]:





# # Daftar Penghasilan Negara DI.307

# In[ ]:


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
def get_data(page):
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
       ("tpfilter", "Fresher"),
       ("kriteria", ""), 
       ("jenispelayanan", ""), 
       ("tahunnomor", ""), 
       ("dari", ""), 
       ("sampai", ""), 
       ("tahunberkas", "2022"), 
       ("tanggalperiode", getCurrentDateFilterPenghasilanNegaraDI307()), 
       #("tanggalperiode", '21/10/2021 - 21/10/2021'), 
       ("bulanperiode", ""), 
       ("tahunberkasperiode", ""), 
       ("qtype", "Fresher"), 
       ("draw", 5), 
       ("start", page), 
       ("length", 10)
    )

    data = urllib.parse.urlencode(data).encode()
    #data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url)
    req.data = data
    req.headers = headers

    f = urllib.request.urlopen(req)

    #print(f.read())

    data = json.load(f)
    print(json.dumps(data, indent=4, sort_keys=True))

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
                        connection.commit()
                        #print ("======================================================================")
                        time.sleep(2)
                finally:
                    pass

    

for x in range(0, 10):
    get_data(x)
    
connection.close()
get_ipython().run_line_magic('time', '')


# In[ ]:





# # Realisasi PTSL Rupiah Murni Kantah

# In[21]:


import re
from re import search

@retry((Exception), tries=25, delay=10, backoff=0)
def get_data():

    '''======================================================================================Move to Jawa Timur'''

    # The action/ target from the form
    authentication_url = 'https://ptsl.atrbpn.go.id/Progress/HeaderKantah'

    # Input parameters we are going to send
    #payload = {
    #  'Id': 'A1DED793DAF0C64DE0400B0A9A144C4A',
    #  'Nama': 'Jatim'  
    #  }

    payload = {
        'Id': satker_id_kantah,
        'Nama': satker_nama_kantah_pendek,
        '_pjax': '#panelplaceholder',
        'Tipe': 'RM'
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
    
    #display(bs)
    l = []
    for y in bs.find_all('tr'):
        for x in y.find_all("td"):
            #i = i+1
            a = x.parent.find_all('td')[1]  # last cell in the row
            b = x.parent.find_all('td')[9]
            
            try:
                z = re.match('showBerkas', b['onclick'])  
                if z:
                    if search('Potensi', b['onclick']):
                        s = (b['onclick'])
                        z = s[s.find("(")+1:s.find(")")]
                        id = z.split(',')[0].replace("'", "")
                        l.append(id)
                        #print(f"{a.get_text()} - {id}")
                        break
                
            except:
                l.append('')
                #print(f"{a.get_text()} - *")
                break
    
    #print(l)
    
    #display(HTML(str(bs.find('table', class_="table")).replace('.', '').replace('K3', 'K3.')))
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    data = pd.read_html(str(bs.find('table', class_="table")).replace('.', ''), encoding = 'utf-8', decimal=",", thousands='.')
    df = data[0]
    
    # Gabung kolom
    df['id_desa'] = pd.Series(l)
    
    df.set_index("Desa/Kelurahan", inplace = True) 
    # df=df.sort_index()
    
    return df
    


# In[22]:


df = get_data()

#display(df)

@retry((Exception), tries=25, delay=10, backoff=0)
def getDetailBerkas(id_desa, page_num):
    if id_desa == '':
        return
    
    # The action/ target from the form
    authentication_url = 'https://ptsl.atrbpn.go.id/Progress/DetailBerkas/' + id_desa + '?nama=Potensi&amp;tipe=RM&amp;kantor=' + satker_id_kantah

    # Input parameters we are going to send
    #payload = {
    #  'Id': 'A1DED793DAF0C64DE0400B0A9A144C4A',
    #  'Nama': 'Jatim'  
    #  }

    payload = {
        'id': id_desa,
        'nama': 'Potensi',
        'pageNum': page_num,
        'tipe': 'RM',
        'kantor': satker_id_kantah
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
    for script in bs.find_all('script'):
        script.extract()

    for i in bs.find_all('i'):
        i.extract()

    for i in bs.find_all('style'):
        i.extract()
        
    #print('_____')
    
    soup = BeautifulSoup("<table class='table'><tr>"+
                         "<td>no</td>"+
                         "<td>nomor_berkas</td>"+
                         "<td>tahun_berkas</td>"+
                         "<td>kegiatan</td>"+
                         "</tr></table>", "lxml")
    tag = soup.table
    tag.append(bs)
    
    data = pd.read_html(str(tag), header=0, flavor = 'bs4', decimal=",", thousands='.')
    df = data[0]
    
    if not df.empty:
        if id_desa != None:
            #print(f"ID Desa: {id_desa}")
            del df['no']
            df.set_index("nomor_berkas", inplace = True) 
            return df
    
    return

def range_switcher(val):
    ret = 0
    for i in range(0, 2000, 100):
        if val <= i:
            break
        else:
            ret += 1
            
    return ret
    
# print(range_switcher(700))

connection = pymysql.connect(**config_mysql)
now = getCurrentDate(True)

with connection.cursor() as cursor:
    # Create a new record
    sql = "TRUNCATE `tb_residu_ptsl_tahun_berjalan` "
    cursor.execute(sql)
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    print(cursor.rowcount, " current records.")
    connection.commit()

try:
    with connection.cursor() as cursor:

        sql = f"SELECT lokasi_desa FROM tb_residu_ptsl_tahun_berjalan ORDER BY lokasi_desa ASC"
        cursor.execute(sql)
        results = cursor.fetchall()

        #print(type(df.index.values.tolist()))
        #print(type(results))
        
        list_df = df.index.values.tolist()
        list_db = []
        
        for x in results:
            #print(f"{x['lokasi_desa']}\n")
            list_db.append(x['lokasi_desa'])
        
        print(f"list_df: {list_df} \n-> len: {len(list_df)} \n")
        print(f"list_db: {list_db} \n-> len: {len(list_db)} \n")
        
        list_diff = set(list_df).difference(set(list_db))
        print(f"Check -> {list_diff}")
            

finally:
    #connection.close()
    pass


for index, row in df.iterrows():
    #print(index, row['K1'])
    try:
        with connection.cursor() as cursor:
            
            sql = f"SELECT * FROM tb_residu_ptsl_tahun_berjalan WHERE lokasi_desa = '{str(index)}' AND id_desa = '{str(row['id_desa'])}'"
            cursor.execute(sql)
            result = cursor.fetchone()
            
            if cursor.rownumber == 0:
                # Create a new record
                sql = f"INSERT INTO `tb_residu_ptsl_tahun_berjalan` (lokasi_desa, id_desa, target_pbt, target_shat, target_k4, survei, pemetaan, puldadis, pemberkasan, potensi_k1, k1, k2, k31, k32, k33, k4, siap_diserahkan, diserahkan, k1_pbt_sebelumnya, tahun_ptsl, created_at) VALUES ('{index}', '{str(row['id_desa'])}','{str(row['Target PBT'])}', '{str(row['Target SHAT'])}', '{str(row['Target K4'])}', '{str(row['Survei'])}', '{str(row['Pemetaan'])}', '{str(row['Puldadis'])}', '{str(row['Pemberkasan *'])}', '{str(row['Potensi K1'])}', '{str(row['K1'])}', '{str(row['K2'])}', '{str(row['K31 *'])}', '{str(row['K32 *'])}', '{str(row['K33 *'])}', '{str(row['K4'])}', '{str(row['Siap Diserahkan'])}', '{str(row['Diserahkan'])}', '{str(row['K1 PBT Sebelumnya'])}', '2022', '{now}')"
                # print(f"{index}")   
                cursor.execute(sql)
                connection.commit()
            else:
                # Update existing record
                sql = f"UPDATE `tb_residu_ptsl_tahun_berjalan` SET updated_at = '{now}', target_pbt = '{str(row['Target PBT'])}', target_shat = '{str(row['Target SHAT'])}', target_k4 = '{str(row['Target K4'])}', survei = '{str(row['Survei'])}', pemetaan = '{str(row['Pemetaan'])}', puldadis = '{str(row['Puldadis'])}', pemberkasan = '{str(row['Pemberkasan *'])}', potensi_k1 = '{str(row['Potensi K1'])}', k1 = '{str(row['K1'])}', k2 = '{str(row['K2'])}', k31 = '{str(row['K31 *'])}', k32 = '{str(row['K32 *'])}', k33 = '{str(row['K33 *'])}', k4 = '{str(row['K4'])}', siap_diserahkan = '{str(row['Siap Diserahkan'])}', diserahkan = '{str(row['Diserahkan'])}', k1_pbt_sebelumnya = '{str(row['K1 PBT Sebelumnya'])}' WHERE id = {str(result['id'])}" 
                # print(sql)    
                cursor.execute(sql)
                connection.commit()
            
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            #print(cursor.rowcount, "record inserted.")
        #with connection.cursor() as cursor:
            # Read a single record
            #sql = "SELECT * FROM `tb_progres_ptsl_kantah` ORDER BY id DESC"
            #cursor.execute(sql, ())
            #result = cursor.fetchone()
            #print(result)
            
            #print(str(row['id_desa']))
            
            
            '''
            if str(row['id_desa']) != '':
                #print(str(row['id_desa']))
                #print(str(row['K1']))
                for i in range(0, range_switcher(int(row['Potensi K1'])), 1):
                    df_berkas = getDetailBerkas(str(row['id_desa']), i)
                    #display(df_berkas)
                    
                    if df_berkas is not None:
                        for index_berkas, row_berkas in df_berkas.iterrows():
                            try:
                                with connection.cursor() as cursor:
                                    # Create a new record       
                                    
                                    sql = f"INSERT INTO `tb_berkas_sebelumnya` (nomor_berkas, tahun_berkas, id_desa, desa, kegiatan, tipe_produk, created_at) VALUES ('{index_berkas}', '{str(row_berkas['tahun_berkas'])}','{str(row['id_desa'])}', '{index}', '{str(row_berkas['kegiatan'])}', 'Potensi K1', '{now}')"
                                    #print(str(result['lokasi_desa']))    
                                    cursor.execute(sql)
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
            '''
    finally:
        #connection.close()
        pass
    
connection.close()


# In[ ]:





# # Rekapitulasi Realisasi Anggaran PTSL Kantah

# In[23]:


'''======================================================================================Move to Jawa Timur'''
'''
<script type="text/javascript">
    var showPencairanKanwil = function (v, n) {
        $.blockUI({ message: '<div style=\"padding:10px\"><b>Sedang proses... </b><p>harap tunggu</p></div>' });
        $.pjax({
            container: "#right_col",
            type: 'POST',
            url: '/Keuangan/PtslKanwil',
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

#
#
# INI BIKIN RESET COOKIE< HARUS  DI COMMENT!
#
#
# Store the cookies and create an opener that will hold them
#cj = http.cookiejar.CookieJar()
#opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

# Add our headers
opener.addheaders = [
    (
        "X-Requested-With",
        "XMLHttpRequest",
    ),
    ('User-agent',
     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/70.0'
     )
]

# Install our opener (note that this changes the global opener to the one
# we just made, but you can also just call opener.open() if you want)
urllib.request.install_opener(opener)

# The action/ target from the form
authentication_url = 'https://ptsl.atrbpn.go.id/Keuangan/PtslKanwil'

# Input parameters we are going to send
payload = {
    'Id': satker_id_kanwil,
    'Nama': satker_kanwil,
    '_pjax': '#right_col'
}

# Use urllib to encode the payload
data = urllib.parse.urlencode(payload).encode("utf-8")

# Build our Request object (supplying 'data' makes it a POST)
req = urllib.request.Request(authentication_url, data)
#req = urllib.request.Request(authentication_url)

# Make the request and read the response
resp = urllib.request.urlopen(req, data=data)

html = urllib.request.urlopen(req, data=data).read()

#print(html)
#bs = BeautifulSoup(html, "html5lib")
bs = BeautifulSoup(resp, 'html.parser')

#print(bs)

table = bs.find('table', attrs={'class': 'table'})
#table_body = table.find('tbody')

#print(table)

data = pd.read_html(str(table),
                    header=0,
                    flavor='bs4',
                    encoding='utf-8',
                    decimal=",",
                    thousands='.')
df = data[0]

#del df['No.']

df.set_index("Kanwil", inplace=True)
df = df.sort_index()

#print(df.columns.tolist())
#df = df.drop(index='Kota Madiun')
df


# In[24]:


print(df.loc[satker_nama_kantah_pendek, :])


# In[25]:


print(df.loc[satker_nama_kantah_pendek, :]['Penyuluhan'])

data = df.loc[satker_nama_kantah_pendek, :]
print(data['Pendataan'])


# In[26]:


now = getCurrentDate(True)
connection = pymysql.connect(**config_mysql)
try:
    with connection.cursor() as cursor:
        sql = "INSERT INTO `tb_progres_ptsl_kantah_anggaran` (penyuluhan, penyuluhan_persen, pendataan, pendataan_persen, pengukuran, pengukuran_persen, k4_asn, k4_asn_persen, skb, skb_persen, k4_skb, k4_skb_persen, pemeriksaan, pemeriksaan_persen, pengesahan, pengesahan_persen, penerbitan, penerbitan_persen, pelaporan, pelaporan_persen, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (data['Penyuluhan'], data['%'], data['Pendataan'], data['%.1'], data['Pengukuran'], data['%.2'], data['K4 ASN'], data['%.3'], data['SKB'], data['%.4'], data['K4 SKB'], data['%.5'], data['Pemeriksaan'], data['%.6'], data['Pengesahan'], data['%.7'], data['Penerbitan'], data['%.8'], data['Pelaporan'], data['%.9'], now))
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        print(cursor.rowcount, "record inserted.")
        connection.commit()
finally:
    connection.close()


# In[ ]:





# # Re-Login SSO

# In[27]:


login()
get_ipython().run_line_magic('time', '')


# # Early Warning

# ## Rekapitulasi Bidang Tanah Tanpa Data Yuridis Kantah

# In[28]:


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
      'Nama': satker_nama_kantah_pendek
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


# In[29]:


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

# In[30]:


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
      'Nama': satker_nama_kantah_pendek
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


# In[31]:


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

# In[32]:


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
      'Nama': satker_nama_kantah_pendek
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


# In[33]:


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

# In[34]:


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
      'Nama': satker_nama_kantah_pendek
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


# In[35]:


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





# In[36]:


print('\n=> Finished')
print(getCurrentDate(True))
elapsed_time = time.time() - start_time
print('%f minutes:' % (float(elapsed_time/60)))
print('\n')


# In[43]:


send_mail("me@rezayogaswara.com", "Bot Scrap Done", '[%s] Hi!\n<i>Bot Scrap</i> task done in %f minutes:' % (getCurrentDate(True), float(elapsed_time/60)))


# In[ ]:




