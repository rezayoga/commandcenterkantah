#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#*Bot-Scraper-Anggaran-Command-Center-Kantor-Pertanahan" data-toc-modified-id="*Bot-Scraper-Anggaran-Command-Center-Kantor-Pertanahan-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>*Bot Scraper Anggaran Command Center Kantor Pertanahan</a></span></li><li><span><a href="#Bot-Init!" data-toc-modified-id="Bot-Init!-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Bot Init!</a></span></li><li><span><a href="#Variables" data-toc-modified-id="Variables-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Variables</a></span></li><li><span><a href="#Login-SSO" data-toc-modified-id="Login-SSO-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Login SSO</a></span></li><li><span><a href="#Rekapitulasi-Realisasi-Anggaran-PTSL-Kantah" data-toc-modified-id="Rekapitulasi-Realisasi-Anggaran-PTSL-Kantah-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Rekapitulasi Realisasi Anggaran PTSL Kantah</a></span><ul class="toc-item"><li><span><a href="#Kantor-Pertanahan" data-toc-modified-id="Kantor-Pertanahan-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Kantor Pertanahan</a></span></li><li><span><a href="#Daftar-Nominatif-Pencairan" data-toc-modified-id="Daftar-Nominatif-Pencairan-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Daftar Nominatif Pencairan</a></span><ul class="toc-item"><li><span><a href="#Puldadis" data-toc-modified-id="Puldadis-5.2.1"><span class="toc-item-num">5.2.1&nbsp;&nbsp;</span>Puldadis</a></span></li><li><span><a href="#Pemeriksaan-Tanah" data-toc-modified-id="Pemeriksaan-Tanah-5.2.2"><span class="toc-item-num">5.2.2&nbsp;&nbsp;</span>Pemeriksaan Tanah</a></span></li></ul></li></ul></li></ul></div>

# 
# # *Bot Scraper Anggaran Command Center Kantor Pertanahan
# ---
# * Crafted by: [**Reza Yogaswara**](http://me.rezayogaswara.com)
# * Output Report: SQL Data

# In[1]:


from datetime import datetime, timedelta, date
import datetime as dt
import time, os

os.environ['TZ'] = 'Asia/Jakarta'
time.tzset()

hari_ini = date.today()
start_time = time.time()


# In[ ]:





# In[2]:


print('\n=> Crafted by: Reza D Yogaswara | me@rezayogaswara.com')
print('\n=> Output Report: SQL / Progres Kegiatan APBN dan Rutin Kantor Pertanahan')


# # Bot Init!

# In[3]:


print('\n=> Bot Init!\n')
import time
start_time = time.time()


# In[4]:


get_ipython().system('python -V')


# In[5]:


import pandas as pd


# In[6]:


pd.show_versions(as_json=False)


# In[ ]:





# # Variables

# In[7]:


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





# In[8]:


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


# In[ ]:





# In[9]:


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


# In[10]:


#send_mail('reza.yoga@gmail.com', 'Bot Scrap Anggaran Init', '[%s] Hi!\n<i>Bot Scrap</i> anggaran init:' % (getCurrentDate(True)))


# In[ ]:





# # Login SSO

# In[11]:


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





# In[12]:


# Example format: "21/10/2021 - 21/10/2021"
def getCurrentDateFilterPenghasilanNegaraDI307():
    return '%s/%s/%s - %s/%s/%s' % (time.strftime('%d'), time.strftime('%m'), time.strftime('%Y'), time.strftime('%d'), time.strftime('%m'), time.strftime('%Y'))


# In[13]:


print(getCurrentDateFilterPenghasilanNegaraDI307())


# In[14]:


import pymysql
# Connect to the database


# In[15]:


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


# # Rekapitulasi Realisasi Anggaran PTSL Kantah

# In[16]:


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
    'Nama': satker_nama_kanwil,
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


# ## Kantor Pertanahan

# In[17]:


print(df.loc[satker_nama_kantah, :])


# In[18]:


print(df.loc[satker_nama_kantah, :]['Penyuluhan'])

data = df.loc[satker_nama_kantah, :]
print(data['Pendataan'])


# In[19]:


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


# ## Daftar Nominatif Pencairan

# ### Puldadis

# In[20]:


from IPython.display import display, HTML

print('\n=> Daftar Nominatif Pencairan Pengumpulan Data\n')
'''=============================================Daftar Nominatif Pencairan Pengumpulan Data'''
'''
<script type="text/javascript">
    (function (a) { a.createModal = function (b) { defaults = { title: "", message: "Your Message Goes Here!", closeButton: true, scrollable: false }; var b = a.extend({}, defaults, b); var c = (b.scrollable === true) ? 'style="max-height: 420px;overflow-y: auto;"' : ""; html = '<div class="modal fade" id="myModal">'; html += '<div class="modal-dialog">'; html += '<div class="modal-content">'; html += '<div class="modal-header">'; html += '<button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>'; if (b.title.length > 0) { html += '<h4 class="modal-title">' + b.title + "</h4>" } html += "</div>"; html += '<div class="modal-body" ' + c + ">"; html += b.message; html += "</div>"; html += '<div class="modal-footer">'; if (b.closeButton === true) { html += '<button type="button" class="btn btn-primary" data-dismiss="modal" id="btn-ok">OK</button>' } html += "</div>"; html += "</div>"; html += "</div>"; html += "</div>"; a("body").prepend(html); a("#myModal").modal().on("hidden.bs.modal", function () { a(this).remove() }) } })(jQuery);
    function showmsg(judul, isi) { $.createModal({ title: judul, message: isi, closeButton: true, scrollable: false }); return false; };
    (function ($) {
        $(document).ready(function () {
            $('.select2_single').select2({ width: 'resolve' });
            $(window).scroll(function () { if ($(this).scrollTop() > 50) { $('#back-to-top').fadeIn(); } else { $('#back-to-top').fadeOut(); } });
            $('#back-to-top').click(function () { $('#back-to-top').tooltip('hide'); $('body,html').animate({ scrollTop: 0 }, 800); return false; }); $('#back-to-top').tooltip('show');
            $('#allcb').change(function () { $('tbody tr td input[type="checkbox"]').prop('checked', $(this).prop('checked')); });
        });
        $("#frmUsulanNominatif").submit(function (e) {
            if ($(this).valid()) {
                resetInfiniteScroll();
                $("#lstberkasnominatif").html('');
                formToPost = $('#frmUsulanNominatif');
                $.blockUI({ message: '<div style=\"padding:10px\"><b>Sedang proses... </b><p>harap tunggu</p></div>' });
                $.ajax({
                    type: "POST",
                    url: '/Yuridis/NominatifPencairan/UsulanPengumpulanData',
                    data: $(this).serialize(),
                    success: function (data, textStatus, XMLHttpRequest) {
                        if (data == 'noresults') {
                            $("#lstberkasnominatif").html('Data tidak ditemukan.');
                        }
                        else {
                            $('#allcb').prop('checked', false);
                            $("#daftarusulan").html(data);
                        }
                        $.unblockUI();
                    },
                    error: function (XMLHttpRequest, textStatus, errorThrown) { $.unblockUI(); }
                });
            }
            e.preventDefault();
            return false;
        });
        GetWilayah = function () {
            var id = $('#programselected').val();
            $.blockUI({ message: '<div style=\"padding:10px\"><b>Sedang proses... </b><p>harap tunggu</p></div>' });
            $.ajax({
                type: "POST",
                url: '/Yuridis/InputPTSL/DaftarWilayah',
                data: { programid: id },
                success: function (data) {
                    $('#Wilayah').html('');
                    $.each(data.wilayah, function (i, data) {
                        $('#Wilayah').append(
                            $('<option></option>').val(data.wilayahid).html(data.nama));
                    });

                    $.unblockUI();
                },
                error: function (XMLHttpRequest, textStatus, errorThrown) {
                    $.unblockUI();
                }
            });
        };
        $("#btnprosesusulan").click(function (e) {
            var jsonArr = [];
            $('#daftarusulan').find('tr').each(function () {
                var row = $(this);
                if (row.find('input[type="checkbox"]').is(':checked')) {
                    jsonArr.push(row.find('input[type="checkbox"]').val());
                }
            });

            if (jsonArr.length == 0) {
                showmsg('Peringatan', 'Tidak ada berkas yang dipilih.');
                e.preventDefault();
                return false;
            }
            $.blockUI({ message: '<div style=\"padding:10px\"><b>Sedang proses... </b><p>harap tunggu</p></div>' });
            var pdata = { n: $('#NomorBerkas').val(), t: $('#TahunBerkas').val(), w: $('#Wilayah').val(), p: $('#programselected').val(), v: JSON.stringify(jsonArr) };
            $.ajax({
                type: 'POST',
                url: '/Yuridis/NominatifPencairan/ProsesUsulanPengumpulanData',
                data: pdata,
                success: function (data, textStatus, XMLHttpRequest) {
                    if (data.Status) {
                        $('#daftarusulan').html(data.ListBerkas);
                    }
                    else {
                        showmsg('Status', data.Pesan);
                    }
                    $('#allcb').prop('checked', false);
                    $.unblockUI();
                },
                error: function (XMLHttpRequest, textStatus, errorThrown) { alert("Error"); $.unblockUI(); }
            });
        });
        moreRowsUrl = '/Yuridis/NominatifPencairan/UsulanPengumpulanData';
        $(window).scroll(scrollHandler);
    }(jQuery));
</script>
'''
    
import json

@retry((Exception), tries=25, delay=10, backoff=0)
def getDataUsulan(wilayahid, headers, pageNum):
    if wilayahid != '':
        url = 'https://ptsl.atrbpn.go.id/Yuridis/NominatifPencairan/UsulanPengumpulanData'
        payload = {
          'programselected': program_id_ptsl,
          'Wilayah': wilayahid,
          'TahunBerkas': hari_ini.year,
          'NomorBerkas':'',
          'pageNum': pageNum  
        }

        data = urllib.parse.urlencode(payload).encode("utf-8")
        req = urllib.request.Request(url)
        req.data = data
        req.headers = headers
        f = urllib.request.urlopen(req)
        #print(f.read())


        #bs = BeautifulSoup(html, "html5lib")
        bs = BeautifulSoup(f.read(), 'html.parser')

        for script in bs.find_all('script'):
            script.extract()

        for i in bs.find_all('i'):
            i.extract()

        soup = BeautifulSoup("<table class='table'><tr>"+
                         "<td>-</td>"+
                         "<td>Nomor Berkas</td>"+
                         "<td>Nama Desa</td>"+
                         "<td>Kode Desa</td>"+
                         "<td>NIB</td>"+
                         "<td>Luas</td>"+
                         "</tr></table>", "lxml")
        tag = soup.table
        tag.append(bs)    

        data = pd.read_html(str(tag), header=0, flavor = 'bs4', decimal=",", thousands='.')
        df = data[0]

        del df['-']
        df.set_index("Nomor Berkas", inplace = True)

        #print(df)
        # Assuming that dataframes df1 and df2 are already defined:
        #display(df)
        #display(HTML(df.to_html()))
        return df

@retry((Exception), tries=25, delay=10, backoff=0)
def get_data():
    url = 'https://ptsl.atrbpn.go.id/Yuridis/InputPTSL/DaftarWilayah'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,id;q=0.8,ms;q=0.7,la;q=0.6',
        'Connection': 'keep-alive',
        #'Content-Length': '42',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        #'Cookie': '.atrbpn2409=A2F3699F41AC9B97183C34DB058CD4846AA1EE09797CF11C4A06ABDAF36502383AB11355E78E78E2E59E5031C8ECF2F83B23D72DF19B88B7DD4DE9A2AAB22022F610E2F373A4CDEA8E96CC3D297D75E6A12898DB41B14AC2A6C8586B22D9245CD45EEB22AFC0C9C1972AA71CC1CEB13D2EA7C75717DCEF2BBD34CE149521ADC15A0C49FC54129287C3169205ED5AA461AC1654D31EDA58A1FF2410F30BC8AD1157F74755D4AAB5302E2B9B3DA7AEC246E967AF11291CBEB059C77BAA76AF971D76A0E446A8D8E4B3F84C182FEAF065BA80D70C66B7EFE7E650C0E267785593BB6495B593662A83DFF2A51D27D4CC6091D5588BDE0BE5665486DEB929657020A2A005382F3D56B355F516EE22E9AE6BA9FF2D0D42E9C7D5B9D0C39584D060CE996FBDA22E9E584E480DFD8897E14D16A898E6C57784B161BC58D394611D7A7826B5FF80606FA30B7E2EFD0B23047D29C7A878BA4B88D63DAE938504C7A2A42300DDB55E60819BB7CB9E12EAC136C03B82760FC9D5436E5670CDF0EC79A5BB65ACF3C51A7CDAD69D0F49B18B590C4C5520B2702EFC16D805A3A766BA59EA2232B38D35C7F3AB9BA5D224660E62DF66F0CC01055F8F924173F80DAF78F5923B4D11B8F7448A0B1C3678B92AB9E2FD28427F53F75D24813E9AE5BE591B3ED174810F26357ACFF1038291FF259522A1BFACE8684719D1E3BB961A5EC00B5E86796321C7F667C4C9534436C319AB57EF47E2E1811D5C63BE9F062F3AACC24BAA4DC36448063220E9B525251B4D7324A127CE6D375AD294C32F9CECC762594E6A9273B4AA315B321D87F019DC68989351F46A1881102921AD1C221482B79439A7D24A4B3133F33538EA99776708CED9239FAC1AC831A3F2CCBA577EE47A31FBF66E37829E586B8A58B5628C839A42428A82072C326A9B0B16F523B308E918FF22DAF8ED5DC13321345F1B103680EAB880F25262C357458AA99DF70BD84C9A0D3599899F3B165F95818EA363DF4874662B1B7F265FFC252D9CC309A7F3FB3C8F7D9F9ABF01C773B1511B2104262E1C4EA316EE2E0C7F0E3987A8EABA64422233880B017EDF3ADA23924A2EDD751825A118D764F668E3B673638FA32012B8B2A2BDBBF0217DAE026B663D1F4392DEF484065C32A60E1F6C4FCC1410C9B86E2A850CD20929D78FDD9A3F4AF42D9DD1A4D27ADCFC0191B261A0BFBCE13C3E3404890EDD171E2B8579AAF39479E95B0E513F3B32A907BD9D2006F1145C4EC649D99FDF060B7BA44EA1E0',
        'Host': 'ptsl.atrbpn.go.id',
        'Origin': 'https://ptsl.atrbpn.go.id',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    payload = {
          'programid': program_id_ptsl
        }

    data = urllib.parse.urlencode(payload).encode("utf-8")
    req = urllib.request.Request(url)
    req.data = data
    req.headers = headers
    f = urllib.request.urlopen(req)

    data = json.load(f)   
    #print(f.read())

    # Desa Tlomar Error
    # getUsulanPengumpulanData('7B05D234392F4D85E0400A0A8376759E', headers)

    now = getCurrentDate(True)
    connection = pymysql.connect(**config_mysql)

    with connection.cursor() as cursor:
        # Create a new record
        sql = "TRUNCATE `tb_daftar_nominatif_pencairan_pengumpulan_data`"
        cursor.execute(sql)
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        print(cursor.rowcount, " current records.")
        connection.commit()

    x = 0
    for i in data.keys():
        #print(i)
        for j in data[i]:
            try:
                x = x + 1
                #print(j)
                #print('[',x,']')
                for y in range(1000):
                    df = getDataUsulan(str(j['wilayahid']), headers, y)
                    #print(type(df))
                    if df.empty:
                        del df
                        continue
                        print('DataFrame is empty!')
                    else:
                        print('(',x,') ', str(j['wilayahid']), ' - ', j['nama'], '| Halaman: ', y,', Jumlah data:', len(df.index))
                        #print(df)
                        for index, row in df.iterrows():
                            # print(index, row['Nama Desa'])
                            with connection.cursor() as cursor:
                                # Create a new record
                                sql = "INSERT INTO `tb_daftar_nominatif_pencairan_pengumpulan_data` (nomor_berkas, nama_desa, kode_desa, nib, luas, created_at) VALUES (%s, %s, %s, %s, %s, %s)"
                                cursor.execute(sql, (index, str(row['Nama Desa']), str(row['Kode Desa']), str(row['NIB']), str(row['Luas']), now))
                                # connection is not autocommit by default. So you must commit to save
                                # your changes.
                                #print(cursor.rowcount, "record inserted.")
                                connection.commit()
                #time.sleep(3)
                print ("======================================================================")
            except:
                pass

    connection.close()

get_data()
get_ipython().run_line_magic('time', '')


# In[21]:


time.sleep(30)


# ### Pemeriksaan Tanah

# In[22]:


print('\n=> Daftar Nominatif Pencairan Pemeriksaan Tanah\n')
'''=============================================Daftar Nominatif Pencairan Pemeriksaan Tanah'''
'''
<script type="text/javascript">
    (function (a) { a.createModal = function (b) { defaults = { title: "", message: "Your Message Goes Here!", closeButton: true, scrollable: false }; var b = a.extend({}, defaults, b); var c = (b.scrollable === true) ? 'style="max-height: 420px;overflow-y: auto;"' : ""; html = '<div class="modal fade" id="myModal">'; html += '<div class="modal-dialog">'; html += '<div class="modal-content">'; html += '<div class="modal-header">'; html += '<button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>'; if (b.title.length > 0) { html += '<h4 class="modal-title">' + b.title + "</h4>" } html += "</div>"; html += '<div class="modal-body" ' + c + ">"; html += b.message; html += "</div>"; html += '<div class="modal-footer">'; if (b.closeButton === true) { html += '<button type="button" class="btn btn-primary" data-dismiss="modal" id="btn-ok">OK</button>' } html += "</div>"; html += "</div>"; html += "</div>"; html += "</div>"; a("body").prepend(html); a("#myModal").modal().on("hidden.bs.modal", function () { a(this).remove() }) } })(jQuery);
    function showmsg(judul, isi) { $.createModal({ title: judul, message: isi, closeButton: true, scrollable: false }); return false; };
    (function ($) {
        $(document).ready(function () {
            $('.select2_single').select2({ width: 'resolve' });
            $(window).scroll(function () { if ($(this).scrollTop() > 50) { $('#back-to-top').fadeIn(); } else { $('#back-to-top').fadeOut(); } });
            $('#back-to-top').click(function () { $('#back-to-top').tooltip('hide'); $('body,html').animate({ scrollTop: 0 }, 800); return false; }); $('#back-to-top').tooltip('show');
            $('#allcb').change(function () { $('tbody tr td input[type="checkbox"]').prop('checked', $(this).prop('checked')); });            
        });        
        $("#frmUsulanNominatif").submit(function (e) {
            if ($(this).valid()) {
                resetInfiniteScroll();
                $("#lstberkasnominatif").html('');
                formToPost = $('#frmUsulanNominatif');
                $.blockUI({ message: '<div style=\"padding:10px\"><b>Sedang proses... </b><p>harap tunggu</p></div>' });
                $.ajax({
                    type: "POST",
                    url: '/Yuridis/NominatifPencairan/UsulanPemeriksaanTanah',
                    data: $(this).serialize(),
                    success: function (data, textStatus, XMLHttpRequest) {
                        if (data == 'noresults') {
                            $("#lstberkasnominatif").html('Data tidak ditemukan.');
                        }
                        else {
                            $('#allcb').prop('checked', false);
                            $("#daftarusulan").html(data);
                        }
                        $.unblockUI();
                    },
                    error: function (XMLHttpRequest, textStatus, errorThrown) { $.unblockUI(); }
                });
            }
            e.preventDefault();
            return false;
        });
        GetWilayah = function () {
            var id = $('#programselected').val();
            $.blockUI({ message: '<div style=\"padding:10px\"><b>Sedang proses... </b><p>harap tunggu</p></div>' });
            $.ajax({
                type: "POST",
                url: '/Yuridis/InputPTSL/DaftarWilayah',
                data: { programid: id },
                success: function (data) {
                    $('#Wilayah').html('');
                    $.each(data.wilayah, function (i, data) {
                        $('#Wilayah').append(
                            $('<option></option>').val(data.wilayahid).html(data.nama));
                    });

                    $.unblockUI();
                },
                error: function (XMLHttpRequest, textStatus, errorThrown) {
                    $.unblockUI();
                }
            });
        };
        $("#btnprosesusulan").click(function (e) {
            var jsonArr = [];
            $('#daftarusulan').find('tr').each(function () {
                var row = $(this);
                if (row.find('input[type="checkbox"]').is(':checked')) {
                    jsonArr.push(row.find('input[type="checkbox"]').val());
                }
            });

            if (jsonArr.length == 0) {
                showmsg('Peringatan', 'Tidak ada berkas yang dipilih.');
                e.preventDefault();
                return false;
            }
            $.blockUI({ message: '<div style=\"padding:10px\"><b>Sedang proses... </b><p>harap tunggu</p></div>' });
            var pdata = { n: $('#NomorBerkas').val(), t: $('#TahunBerkas').val(), w: $('#Wilayah').val(), p: $('#programselected').val(), v: JSON.stringify(jsonArr) };
            $.ajax({
                type: 'POST',
                url: '/Yuridis/NominatifPencairan/ProsesUsulanPemeriksaanTanah',
                data: pdata,
                success: function (data, textStatus, XMLHttpRequest) {
                    if (data.Status) {
                        $('#daftarusulan').html(data.ListBerkas);
                    }
                    else {
                        showmsg('Status', data.Pesan);
                    }
                    $('#allcb').prop('checked', false);
                    $.unblockUI();
                },
                error: function (XMLHttpRequest, textStatus, errorThrown) { alert("Error"); $.unblockUI(); }
            });
        });
        moreRowsUrl = '/Yuridis/NominatifPencairan/UsulanPemeriksaanTanah';
        $(window).scroll(scrollHandler);
    }(jQuery));
</script>
'''

@retry((Exception), tries=25, delay=10, backoff=0)
def getDataUsulan(wilayahid, headers, pageNum):
    if wilayahid != '':
        url = 'https://ptsl.atrbpn.go.id/Yuridis/NominatifPencairan/UsulanPemeriksaanTanah'
        payload = {
            'programselected': program_id_ptsl,
            'Wilayah': wilayahid,
            'TahunBerkas': hari_ini.year,
            'NomorBerkas': '',
            'pageNum': pageNum
        }

        data = urllib.parse.urlencode(payload).encode("utf-8")
        req = urllib.request.Request(url)
        req.data = data
        req.headers = headers
        f = urllib.request.urlopen(req)
        #print(f.read())

        #bs = BeautifulSoup(html, "html5lib")
        bs = BeautifulSoup(f.read(), 'html.parser')

        for script in bs.find_all('script'):
            script.extract()

        for i in bs.find_all('i'):
            i.extract()

        soup = BeautifulSoup(
            "<table class='table'><tr>" + "<td>-</td>" +
            "<td>Nomor Berkas</td>" + "<td>Nama Desa</td>" +
            "<td>Kode Desa</td>" + "<td>NIB</td>" + "<td>Luas</td>" +
            "</tr></table>", "lxml")
        tag = soup.table
        tag.append(bs)

        data = pd.read_html(str(tag),
                            header=0,
                            flavor='bs4',
                            decimal=",",
                            thousands='.')
        df = data[0]

        del df['-']
        df.set_index("Nomor Berkas", inplace=True)

        #print(df)
        # Assuming that dataframes df1 and df2 are already defined:
        #display(df)
        #display(HTML(df.to_html()))
        return df

@retry((Exception), tries=30, delay=10, backoff=0)
def get_data():
    url = 'https://ptsl.atrbpn.go.id/Yuridis/InputPTSL/DaftarWilayah'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,id;q=0.8,ms;q=0.7,la;q=0.6',
        'Connection': 'keep-alive',
        #'Content-Length': '42',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        #'Cookie': '.atrbpn2409=A2F3699F41AC9B97183C34DB058CD4846AA1EE09797CF11C4A06ABDAF36502383AB11355E78E78E2E59E5031C8ECF2F83B23D72DF19B88B7DD4DE9A2AAB22022F610E2F373A4CDEA8E96CC3D297D75E6A12898DB41B14AC2A6C8586B22D9245CD45EEB22AFC0C9C1972AA71CC1CEB13D2EA7C75717DCEF2BBD34CE149521ADC15A0C49FC54129287C3169205ED5AA461AC1654D31EDA58A1FF2410F30BC8AD1157F74755D4AAB5302E2B9B3DA7AEC246E967AF11291CBEB059C77BAA76AF971D76A0E446A8D8E4B3F84C182FEAF065BA80D70C66B7EFE7E650C0E267785593BB6495B593662A83DFF2A51D27D4CC6091D5588BDE0BE5665486DEB929657020A2A005382F3D56B355F516EE22E9AE6BA9FF2D0D42E9C7D5B9D0C39584D060CE996FBDA22E9E584E480DFD8897E14D16A898E6C57784B161BC58D394611D7A7826B5FF80606FA30B7E2EFD0B23047D29C7A878BA4B88D63DAE938504C7A2A42300DDB55E60819BB7CB9E12EAC136C03B82760FC9D5436E5670CDF0EC79A5BB65ACF3C51A7CDAD69D0F49B18B590C4C5520B2702EFC16D805A3A766BA59EA2232B38D35C7F3AB9BA5D224660E62DF66F0CC01055F8F924173F80DAF78F5923B4D11B8F7448A0B1C3678B92AB9E2FD28427F53F75D24813E9AE5BE591B3ED174810F26357ACFF1038291FF259522A1BFACE8684719D1E3BB961A5EC00B5E86796321C7F667C4C9534436C319AB57EF47E2E1811D5C63BE9F062F3AACC24BAA4DC36448063220E9B525251B4D7324A127CE6D375AD294C32F9CECC762594E6A9273B4AA315B321D87F019DC68989351F46A1881102921AD1C221482B79439A7D24A4B3133F33538EA99776708CED9239FAC1AC831A3F2CCBA577EE47A31FBF66E37829E586B8A58B5628C839A42428A82072C326A9B0B16F523B308E918FF22DAF8ED5DC13321345F1B103680EAB880F25262C357458AA99DF70BD84C9A0D3599899F3B165F95818EA363DF4874662B1B7F265FFC252D9CC309A7F3FB3C8F7D9F9ABF01C773B1511B2104262E1C4EA316EE2E0C7F0E3987A8EABA64422233880B017EDF3ADA23924A2EDD751825A118D764F668E3B673638FA32012B8B2A2BDBBF0217DAE026B663D1F4392DEF484065C32A60E1F6C4FCC1410C9B86E2A850CD20929D78FDD9A3F4AF42D9DD1A4D27ADCFC0191B261A0BFBCE13C3E3404890EDD171E2B8579AAF39479E95B0E513F3B32A907BD9D2006F1145C4EC649D99FDF060B7BA44EA1E0',
        'Host': 'ptsl.atrbpn.go.id',
        'Origin': 'https://ptsl.atrbpn.go.id',
        'sec-ch-ua':
        '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    payload = {'programid': program_id_ptsl}

    data = urllib.parse.urlencode(payload).encode("utf-8")
    req = urllib.request.Request(url)
    req.data = data
    req.headers = headers
    f = urllib.request.urlopen(req)

    data = json.load(f)

    #print(f.read())

    # Desa Tlomar Error
    # getUsulanPengumpulanData('7B05D234392F4D85E0400A0A8376759E', headers)

    now = getCurrentDate(True)
    connection = pymysql.connect(**config_mysql)

    with connection.cursor() as cursor:
        # Create a new record
        sql = "TRUNCATE `tb_daftar_nominatif_pencairan_pemeriksaan_tanah`"
        cursor.execute(sql)
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        print(cursor.rowcount, " current records.")
        connection.commit()

    x = 0
    for i in data.keys():
        #print(i)
        for j in data[i]:
            try:
                x = x + 1
                #print(j)
                #print('[',x,']')
                for y in range(1000):
                    df = getDataUsulan(str(j['wilayahid']), headers, y)
                    #print(type(df))
                    if df.empty:
                        del df
                        continue
                        print('DataFrame is empty!')
                    else:
                        print('(',x,') ', str(j['wilayahid']), ' - ', j['nama'], '| Halaman: ', y,', Jumlah data:', len(df.index))
                        #print(df)
                        for index, row in df.iterrows():
                            #print(index, row['Nama Desa'])
                            with connection.cursor() as cursor:
                                # Create a new record
                                sql = "INSERT INTO `tb_daftar_nominatif_pencairan_pemeriksaan_tanah` (nomor_berkas, nama_desa, kode_desa, nib, luas, created_at) VALUES (%s, %s, %s, %s, %s, %s)"
                                cursor.execute(sql, (index, str(row['Nama Desa']), str(row['Kode Desa']), str(row['NIB']), str(row['Luas']), now))
                                # connection is not autocommit by default. So you must commit to save
                                # your changes.
                                #print(cursor.rowcount, "record inserted.")
                                connection.commit()
                #time.sleep(3)
                print ("======================================================================")
            except:
                pass

    connection.close()
    
get_data()
get_ipython().run_line_magic('time', '')


# 

# In[23]:


print('\n=> Finished')
print(getCurrentDate(True))
elapsed_time = time.time() - start_time
print('%f minutes:' % (float(elapsed_time/60)))
print('\n')


# In[ ]:





# In[24]:


#send_mail("dimasardi1349@gmail.com", "Bot Scrap Anggaran Done", '[%s] Hi!\n<i>Bot Scrap</i> anggaran task done in %f minutes:' % (getCurrentDate(True), float(elapsed_time/60)))


# In[ ]:




