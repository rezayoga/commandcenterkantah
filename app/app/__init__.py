# importing date class from datetime module
import datetime
import os
import time
from datetime import date
from functools import wraps
from hashlib import md5
from urllib.parse import unquote

import pymysql
from cryptography.fernet import Fernet
from flask import Flask, render_template, request, redirect, url_for, session, flash, Markup, jsonify, make_response
from flask_wtf.csrf import CSRFError
from flask_wtf.csrf import CSRFProtect
from jinja2 import Template
from werkzeug.debug import DebuggedApplication

now = datetime.datetime.now()
# print now.year, now.month, now.day, now.hour, now.minute, now.second
os.environ['TZ'] = 'Asia/Jakarta'
time.tzset()

# creating the date object of today's date
todays_date = date.today()

from form.login_form import LoginForm

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True, show_hidden_frames=True)
app.config['SECRET_KEY'] = "S3CRET_KeY!"
app.config['WTF_CSRF_TIME_LIMIT'] = 6000

# from app import routes
db_config = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "passwd": "pmnP_AkjWk26x2020",
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor,
    "database": "db_c2s_kantah"
}
web_config = {
    "SECURE_KEY": Fernet.generate_key(),
    "BASE_URL": "https://c2ssetup.pusakha.id/",
    "BASE_URL_ACTION_FORM": "https://c2ssetup.pusakha.id/action_form/",
    "MEDIA_IMAGES_DIR": "https://c2ssetup.pusakha.id/media/images/",
    "MEDIA_CSS_DIR": "https://c2ssetup.pusakha.id/media/css/",
    "MEDIA_JS_DIR": "https://c2ssetup.pusakha.id/media/js/",
    "MEDIA_DOCS_DIR": "https://c2ssetup.pusakha.id/media/docs/",
    "UPLOADS_DIR": "https://c2ssetup.pusakha.id/uploads/",
    "APP_NAME": "C2S Kantor Pertanahan Kab. Nganjuk",
    "APP_NAME_LONG": "Command Center System Kantor Pertanahan Kab. Nganjuk",
    "APP_SLOGAN": "Smart Work Pays Best",
    "APP_VERSION": "1.0.0",
    "APP_STAKEHOLDER": "Kantor Pertanahan Kab. Nganjuk",
    "DEVELOPER": "Reza Yogaswara",
    "DEVELOPER_ADDRESS": "Perum Green View Regency Blok B3 - Malang, Jawa Timur",
    "DEVELOPER_PHONE": "+6282228223500",
    "DEVELOPER_WEBSITE": "https://me.rezayogaswara.dev",
    "CURRENT_DATE": todays_date,
    "CURRENT_YEAR": todays_date.year
}

csrf = CSRFProtect()
csrf.init_app(app)
f = Fernet(web_config['SECURE_KEY'])
encrypted_string = f.encrypt(bytes(web_config['DEVELOPER'], encoding='utf8')).decode("utf-8")

web_menu = {
    "MENU_PEGAWAI": f.encrypt(bytes('PEGAWAI', encoding='utf8')).decode("utf-8"),
    "MENU_TIM_PTSL": f.encrypt(bytes('TIM_PTSL', encoding='utf8')).decode("utf-8"),
    "MENU_BERKAS_PNBP": f.encrypt(bytes('BERKAS_PNBP', encoding='utf8')).decode("utf-8"),
    "MENU_DAFTAR_TUNGGAKAN_BERKAS_PNBP_PER_JABATAN": f.encrypt(
        bytes('DAFTAR_TUNGGAKAN_BERKAS_PNBP_PER_JABATAN', encoding='utf8')).decode(
        "utf-8"),
    "MENU_DAFTAR_TUNGGAKAN_BERKAS_PNBP_PER_LAYANAN": f.encrypt(
        bytes('DAFTAR_TUNGGAKAN_BERKAS_PNBP_PER_LAYANAN', encoding='utf8')).decode(
        "utf-8"),
    "MENU_DAFTAR_TUNGGAKAN_PENERIMAAN_DIMUKA_PER_TAHUN": f.encrypt(
        bytes('DAFTAR_TUNGGAKAN_PENERIMAAN_DIMUKA_PER_TAHUN', encoding='utf8')).decode(
        "utf-8"),
    "MENU_DAFTAR_TUNGGAKAN_PENERIMAAN_DIMUKA_PER_BULAN": f.encrypt(
        bytes('DAFTAR_TUNGGAKAN_PENERIMAAN_DIMUKA_PER_BULAN', encoding='utf8')).decode(
        "utf-8"),
    "MENU_PROGRES_PTSL_KANTAH": f.encrypt(bytes('PROGRES_PTSL_KANTAH', encoding='utf8')).decode(
        "utf-8"),
    "MENU_BERKAS_TANPA_BIDANG_TANAH": f.encrypt(bytes('BERKAS_TANPA_BIDANG_TANAH', encoding='utf8')).decode(
        "utf-8"),
    "MENU_BERKAS_TANPA_DATA_YURIDIS": f.encrypt(bytes('BERKAS_TANPA_DATA_YURIDIS', encoding='utf8')).decode(
        "utf-8"),
    "MENU_BERKAS_TANPA_PEMOHON": f.encrypt(bytes('BERKAS_TANPA_PEMOHON', encoding='utf8')).decode(
        "utf-8"),
    "MENU_PENGUMUMAN_KADALUWARSA": f.encrypt(bytes('PENGUMUMAN_KADALUWARSA', encoding='utf8')).decode(
        "utf-8"),
    "MENU_PROGRES_ANGGARAN_PTSL": f.encrypt(bytes('PROGRES_ANGGARAN_PTSL', encoding='utf8')).decode(
        "utf-8"),
     "MENU_PNBP": f.encrypt(bytes('PNBP', encoding='utf8')).decode(
        "utf-8")
}

'''
Function, Tools, and Helper ============================================
'''


def encrypt_string(plain_text):
    f = Fernet(web_config['SECURE_KEY'])
    return f.encrypt(bytes(str(plain_text), encoding='utf8')).decode("utf-8")


def decrypt_string(encrypted_text):
    plaintext = ''
    try:
        plaintext = f.decrypt(bytes(unquote(encrypted_text), encoding='utf-8')).decode("utf-8")
    except Exception as error:
        plaintext = error
    return plaintext


def get_nama_pegawai(id):
    conn = pymysql.connect(**db_config)
    result = None
    try:
        with conn.cursor() as cur:
            sql = "SELECT * FROM `tb_user` WHERE id = %s"
            cur.execute(sql, id)
            result = cur.fetchone()
    finally:
        conn.close()
    return result


def formatrupiah(uang):
    y = str(uang)

    if len(y) <= 3:
        return 'Rp ' + y
    else:
        p = y[-3:]
        q = y[:-3]
        return formatrupiah(q) + '.' + p
        print
        'Rp ' + formatrupiah(q) + '.' + p

def extract_biaya(s):
    r = 0
    sc = s.split(' ')
    valid = False
    for i in range(len(sc)):
        if sc[i] == 'NTPN:':
            valid = True
            break

    if valid == True:
        for i in range(len(sc)):
            if sc[i] == 'Biaya:':
                new_string = sc[i + 1].replace('.', '')
                biaya = ""
                for m in new_string:
                    if m.isdigit():
                        biaya = biaya + m
                r = biaya
                break

    return int(r)

'''
Function, Tools, and Helper ============================================
'''


def get_current_date(withTime=False):
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
        return '%s-%s-%s %s:%s:%s' % (
            time.strftime('%Y'), time.strftime('%m'), time.strftime('%d'), time.strftime('%H'), time.strftime('%M'),
            time.strftime('%S'))
    return '%s-%s-%s' % (time.strftime('%d'), month[int(time.strftime('%m')) - 1], now.year)


app.add_template_global(encrypt_string, name='encrypt_string')
app.add_template_global(get_nama_pegawai, name='get_nama_pegawai')
app.add_template_global(formatrupiah, name='formatrupiah')
app.add_template_global(get_current_date, name='get_current_date')
app.add_template_global(extract_biaya, name='extract_biaya')


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'USER' in session:
            return f(*args, **kwargs)
        else:
            flash(Markup('<div class="ui error floating message">Anda belum login!</div>'))
            return redirect(url_for('/'))

    return wrap


@app.route('/search')
def search():
    search = request.args.get('s') or None

    t = Template("Hello, {{n}} {{ encrypt_string('{{n}}') }}")

    return t.render(n=search, encrypt_string=encrypt_string)


@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    # return render_template('csrf_error.html', reason=e.description), 400
    return render_template('csrf_error.html',
                           reason='Halaman ini telah kadaluwarsa, silakan muat ulang pada halaman ini/sebelumnya'), 400


'''
View Renderer =========================================================
'''


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    if 'USER' in session:
        return redirect(url_for('dashboard', random=encrypted_string))
    login_form = LoginForm()
    return render_template('index.html', web_config=web_config, form=login_form, random=encrypted_string)


@login_required
@app.route('/dashboard.<string:random>', methods=['GET'])
def dashboard(random):
    try:
        d = f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
        if d != web_config['DEVELOPER']:
            session.pop('USER', None)
            session.clear()
            flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
            return redirect(url_for('index', random=encrypted_string))
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))
    if 'USER' in session:

        conn = pymysql.connect(**db_config)
        tim_ptsl = None
        try:
            with conn.cursor() as cur:
                sql = "SELECT * FROM `tb_tim_ptsl` WHERE daftar_pegawai LIKE '%{}%' ORDER BY id DESC".format(
                    session['USER']['id'])
                # print(sql)
                cur.execute(sql)
                tim_ptsl = cur.fetchall()

        finally:
            conn.close()

        user_session = session['USER']
        return render_template('dashboard.html', web_config=web_config, user_session=user_session, web_menu=web_menu,
                               random=random, tim_ptsl=tim_ptsl)
    flash(Markup('<div class="ui error floating message">Anda belum login!</div>'))
    return redirect(url_for('index', random=encrypted_string))


@login_required
@app.route('/total_berkas_pnbp.<string:random>.json', methods=['GET'])
def total_berkas_pnbp(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            cur.execute("SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")
            sql = "SELECT nama_kegiatan, COUNT(*) AS jumlah FROM tb_berkas_pnbp AS total GROUP BY nama_kegiatan ORDER BY nama_kegiatan ASC"
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()

    r = make_response(jsonify(results))
    r.mimetype = 'application/json'
    return r


@login_required
@app.route('/tunggakan_berkas_pnbp_per_jabatan.<string:random>.json', methods=['GET'])
def tunggakan_berkas_pnbp_per_jabatan(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    q = request.args.get('q') or None

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            # cur.execute("SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")
            sql = "SELECT * FROM tb_daftar_tunggakan_berkas_pnbp_per_jabatan WHERE jabatan = '{}' ORDER BY created_at ASC;".format(
                q)
            # print(sql_tunggakan_berkas_pnbp)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()

    r = make_response(jsonify(results))
    r.mimetype = 'application/json'
    return r


@login_required
@app.route('/tunggakan_berkas_pnbp_per_layanan.<string:random>.json', methods=['GET'])
def tunggakan_berkas_pnbp_per_layanan(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    q = request.args.get('q') or None

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            # cur.execute("SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")
            sql = "SELECT * FROM tb_daftar_tunggakan_berkas_pnbp_per_layanan WHERE layanan = '{}' ORDER BY created_at ASC;".format(
                q)
            # print(sql_tunggakan_berkas_pnbp)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()

    r = make_response(jsonify(results))
    r.mimetype = 'application/json'
    return r


@login_required
@app.route('/tunggakan_penerimaan_dimuka_per_tahun.<string:random>.json', methods=['GET'])
def tunggakan_penerimaan_dimuka_per_tahun(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            # cur.execute("SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")
            sql = """SELECT * FROM `tb_tunggakan_penerimaan_dimuka_tahunan` WHERE created_at LIKE '%{}%' AND created_at = (
                SELECT MAX(created_at)
                FROM `tb_tunggakan_penerimaan_dimuka_tahunan` AS b
                WHERE 1
            )""".format(datetime.date.today())
            # print(sql_tunggakan_berkas_pnbp)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()

    r = make_response(jsonify(results))
    r.mimetype = 'application/json'
    return r


@login_required
@app.route('/tunggakan_penerimaan_dimuka_per_bulan.<string:random>.json', methods=['GET'])
def tunggakan_penerimaan_dimuka_per_bulan(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            # cur.execute("SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")
            sql = """SELECT * FROM `tb_tunggakan_penerimaan_dimuka_bulanan` WHERE created_at LIKE '%{}%' AND created_at = (
    SELECT MAX(created_at)
    FROM `tb_tunggakan_penerimaan_dimuka_bulanan` AS b
    WHERE 1
) GROUP BY jumlah_tunggakan, nilai_tunggakan""".format(
                datetime.date.today())
            # print(sql_tunggakan_berkas_pnbp)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()

    r = make_response(jsonify(results))
    r.mimetype = 'application/json'
    return r


@login_required
@app.route('/view_daftar_tunggakan_berkas_pnbp_per_jabatan.<string:random>', methods=['GET'])
def view_daftar_tunggakan_berkas_pnbp_per_jabatan(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    template = '/renderer/view_daftar_tunggakan_berkas_pnbp_per_jabatan.html'

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            sql = """SELECT * FROM `tb_daftar_tunggakan_berkas_pnbp_per_jabatan` WHERE created_at LIKE '%{}%' AND created_at = (
    SELECT MAX(created_at)
    FROM `tb_daftar_tunggakan_berkas_pnbp_per_jabatan` AS b
    WHERE 1
)""".format(datetime.date.today())
            print(sql)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()
    return render_template(template, random=random, results=results)


@login_required
@app.route('/view_daftar_tunggakan_berkas_pnbp_per_layanan.<string:random>', methods=['GET'])
def view_daftar_tunggakan_berkas_pnbp_per_layanan(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    template = '/renderer/view_daftar_tunggakan_berkas_pnbp_per_layanan.html'

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            sql = """SELECT * FROM `tb_daftar_tunggakan_berkas_pnbp_per_layanan` WHERE created_at LIKE '%{}%' AND created_at = (
    SELECT MAX(created_at)
    FROM `tb_daftar_tunggakan_berkas_pnbp_per_layanan` AS b
    WHERE 1
)""".format(datetime.date.today())
            # print(sql)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()
    return render_template(template, random=random, results=results)


@login_required
@app.route('/view_daftar_tunggakan_penerimaan_dimuka_per_tahun.<string:random>', methods=['GET'])
def view_daftar_tunggakan_penerimaan_dimuka_per_tahun(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    template = '/renderer/view_daftar_tunggakan_penerimaan_dimuka_per_tahun.html'

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            sql = """SELECT * FROM `tb_tunggakan_penerimaan_dimuka_tahunan` WHERE created_at LIKE '%{}%' AND created_at = (
    SELECT MAX(created_at)
    FROM `tb_tunggakan_penerimaan_dimuka_tahunan` AS b
    WHERE 1
)""".format(datetime.date.today())
            # print(sql)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()
    return render_template(template, random=random, results=results)


@login_required
@app.route('/view_daftar_tunggakan_penerimaan_dimuka_per_bulan.<string:random>', methods=['GET'])
def view_daftar_tunggakan_penerimaan_dimuka_per_bulan(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    template = '/renderer/view_daftar_tunggakan_penerimaan_dimuka_per_bulan.html'

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            sql = """SELECT * FROM `tb_tunggakan_penerimaan_dimuka_bulanan` WHERE created_at LIKE '%{}%' AND created_at = (
    SELECT MAX(created_at)
    FROM `tb_tunggakan_penerimaan_dimuka_bulanan` AS b
    WHERE 1
) GROUP BY jumlah_tunggakan, nilai_tunggakan""".format(
                datetime.date.today())
            print(sql)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()
    return render_template(template, random=random, results=results)


@login_required
@app.route('/early_warning_berkas_tanpa_bidang_tanah.<string:random>.json', methods=['GET'])
def early_warning_berkas_tanpa_bidang_tanah(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    q = request.args.get('q') or None

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            # cur.execute("SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")
            sql = "SELECT * FROM tb_early_warning_berkas_tanpa_bidang_tanah WHERE desa = '{}' GROUP BY created_at ORDER BY created_at ASC;".format(
                q)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()

    r = make_response(jsonify(results))
    r.mimetype = 'application/json'
    return r


@login_required
@app.route('/early_warning_bidang_tanah_tanpa_data_yuridis_kantah.<string:random>.json', methods=['GET'])
def early_warning_bidang_tanah_tanpa_data_yuridis_kantah(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    q = request.args.get('q') or None

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            # cur.execute("SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")
            sql = "SELECT * FROM tb_early_warning_bidang_tanah_tanpa_data_yuridis_kantah WHERE desa = '{}' GROUP BY created_at ORDER BY created_at ASC;".format(
                q)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()

    r = make_response(jsonify(results))
    r.mimetype = 'application/json'
    return r


@login_required
@app.route('/early_warning_pengumuman_kadaluwarsa_kantor_pertanahan.<string:random>.json', methods=['GET'])
def early_warning_pengumuman_kadaluwarsa_kantor_pertanahan(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    q = request.args.get('q') or None

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            # cur.execute("SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")
            sql = "SELECT * FROM tb_early_warning_pengumuman_kadaluwarsa_kantor_pertanahan WHERE desa = '{}' GROUP BY created_at ORDER BY created_at ASC;".format(
                q)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()

    r = make_response(jsonify(results))
    r.mimetype = 'application/json'
    return r


@login_required
@app.route('/early_warning_berkas_tanpa_pemohon.<string:random>.json', methods=['GET'])
def early_warning_berkas_tanpa_pemohon(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    q = request.args.get('q') or None

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            cur.execute("SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")
            sql = "SELECT * FROM tb_early_warning_berkas_tanpa_pemohon WHERE desa = '{}' GROUP BY created_at ORDER BY created_at ASC;".format(
                q)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()

    r = make_response(jsonify(results))
    r.mimetype = 'application/json'
    return r


@login_required
@app.route('/view_dashboard.<string:random>', methods=['GET'])
def view_dashboard(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))
    template = '/renderer/view_dashboard.html'

    conn = pymysql.connect(**db_config)
    results_distinct_jabatan = None
    try:
        with conn.cursor() as cur:
            cur.execute("SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")

            sql_tunggakan_berkas_pnbp = "SELECT DISTINCT (jabatan) AS jabatan FROM tb_daftar_tunggakan_berkas_pnbp_per_jabatan ORDER BY jabatan ASC;"
            cur.execute(sql_tunggakan_berkas_pnbp)
            results_distinct_jabatan = cur.fetchall()

            sql_tunggakan_berkas_pnbp = "SELECT DISTINCT (layanan) AS layanan FROM tb_daftar_tunggakan_berkas_pnbp_per_layanan ORDER BY layanan ASC;"
            cur.execute(sql_tunggakan_berkas_pnbp)
            results_distinct_layanan = cur.fetchall()

            sql = "select count(*) as total from tb_residu_ptsl_tahun_berjalan WHERE lokasi_desa != 'Total'"
            # print(sql)
            cur.execute(sql)
            results_total_desa = cur.fetchone()

            sql = "SELECT target_pbt, target_shat, survei, pemetaan, puldadis, pemberkasan FROM `tb_residu_ptsl_tahun_berjalan` WHERE `lokasi_desa` = 'Total'"
            # print(sql)
            cur.execute(sql)
            results_target_realisai_pbt_shat = cur.fetchone()
            
    finally:
        conn.close()
    return render_template(template, random=random,  results_total_desa=results_total_desa['total'],
                           results_target_realisai_pbt_shat=results_target_realisai_pbt_shat, results_distinct_jabatan=results_distinct_jabatan,
                           results_distinct_layanan=results_distinct_layanan
                           )
    # return str(results_total_berkas_pnbp)


@login_required
@app.route('/view_pegawai.<string:random>', methods=['GET'])
def view_pegawai(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    template = '/renderer/view_pegawai.html'

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            sql = "SELECT * FROM `tb_user`"
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()
    return render_template(template, random=random, results=results)


@login_required
@app.route('/view_pegawai_search.<string:random>', methods=['GET'])
def view_pegawai_search(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    template = '/renderer/view_pegawai.html'

    search = request.args.get('q') or None

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            sql = "SELECT * FROM `tb_user` WHERE nama LIKE '%{}%' OR nip LIKE '%{}%' OR jabatan LIKE '%{}%' OR email LIKE '%{}%' ORDER BY id DESC".format(
                search, search, search, search)
            # print(sql)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()
    return render_template(template, random=random, results=results)


@login_required
@app.route('/view_tim_ptsl.<string:random>', methods=['GET'])
def view_tim_ptsl(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    template = '/renderer/view_tim_ptsl.html'

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            sql = "SELECT * FROM `tb_tim_ptsl`"
            cur.execute(sql)
            results = cur.fetchall()

            sql = "SELECT DISTINCT (lokasi_desa) as desa_kelurahan FROM `tb_residu_ptsl_tahun_berjalan` WHERE lokasi_desa != 'Total'"
            cur.execute(sql)
            results_tim_ptsl = cur.fetchall()

            sql = "SELECT * FROM `tb_user`"
            cur.execute(sql)
            results_user = cur.fetchall()
    finally:
        conn.close()
    return render_template(template, random=random, results=results, results_tim_ptsl=results_tim_ptsl,
                           results_user=results_user)


@login_required
@app.route('/view_berkas_pnbp.<string:random>', methods=['GET'])
def view_berkas_pnbp(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    template = '/renderer/view_berkas_pnbp.html'

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            sql = "SELECT * FROM `tb_berkas_pnbp` ORDER BY tahun_berkas DESC LIMIT 500 "
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()
    return render_template(template, random=random, results=results)


@login_required
@app.route('/view_berkas_pnbp_search.<string:random>', methods=['GET'])
def view_berkas_pnbp_search(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    template = '/renderer/view_berkas_pnbp.html'

    search = request.args.get('q') or None

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            sql = "SELECT * FROM `tb_berkas_pnbp` WHERE nomor_berkas LIKE '%{}%' OR tahun_berkas LIKE '%{}%' OR tanggal_terdaftar LIKE '%{}%' OR jatuh_tempo LIKE '%{}%' OR tanggal_selesai LIKE '%{}%' OR tanggal_diserahkan LIKE '%{}%' OR nama_kegiatan LIKE '%{}%' OR nama_pemohon LIKE '%{}%' OR posisi_terakhir LIKE '%{}%' ORDER BY id DESC LIMIT 500 ".format(
                search, search, search, search, search, search, search, search, search, search)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()
    return render_template(template, random=random, results=results)


@login_required
@app.route('/view_daftar_tunggakan_berkas_pnbp.<string:random>', methods=['GET'])
def view_daftar_tunggakan_berkas_pnbp(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    template = '/renderer/view_daftar_tunggakan_berkas_pnbp.html'

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            sql = """SELECT * FROM `tb_daftar_tunggakan_berkas_pnbp` WHERE created_at LIKE '%{}%' AND created_at = (
    SELECT MAX(created_at)
    FROM `tb_daftar_tunggakan_berkas_pnbp` AS b
    WHERE 1
)""".format(datetime.date.today())
            # print(sql)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()
    return render_template(template, random=random, results=results)


@login_required
@app.route('/view_daftar_tunggakan_berkas_pnbp_search.<string:random>', methods=['GET'])
def view_daftar_tunggakan_berkas_pnbp_search(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    template = '/renderer/view_daftar_tunggakan_berkas_pnbp.html'

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            '''
            sql = """SELECT * FROM `tb_daftar_tunggakan_berkas_pnbp` WHERE created_at LIKE '%{}%' AND created_at = (
    SELECT MAX(created_at)
    FROM `tb_daftar_tunggakan_berkas_pnbp` AS b
    WHERE 1
)""".format(datetime.date.today())
'''
            search = request.args.get('q') or None
            sql = "SELECT * FROM `tb_daftar_tunggakan_berkas_pnbp` WHERE jabatan LIKE '%{}%' OR created_at LIKE '%{}%' ORDER BY id DESC".format(
                search, search)
            # print(sql)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()
    return render_template(template, random=random, results=results)


@login_required
@app.route('/view_progres_ptsl_kantah.<string:random>', methods=['GET'])
def view_progres_ptsl_kantah(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    template = '/renderer/view_progres_ptsl_kantah.html'

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            sql = """SELECT * FROM `tb_residu_ptsl_tahun_berjalan` WHERE lokasi_desa != 'Total' AND created_at LIKE '%{}%' AND created_at = (
    SELECT MAX(created_at)
    FROM `tb_residu_ptsl_tahun_berjalan` AS b
    WHERE 1
) """.format(
                datetime.date.today())
            # print(sql)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()
    return render_template(template, random=random, results=results)


@login_required
@app.route('/view_progres_ptsl_kantah_search.<string:random>', methods=['GET'])
def view_progres_ptsl_kantah_search(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    template = '/renderer/view_progres_ptsl_kantah.html'

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            '''
            sql = """SELECT * FROM `tb_residu_ptsl_tahun_berjalan` WHERE lokasi_desa != 'Total' AND created_at LIKE '%{}%' AND created_at = (
    SELECT MAX(created_at)
    FROM `tb_residu_ptsl_tahun_berjalan` AS b
    WHERE 1
) """.format(
                datetime.date.today())
                '''
            search = request.args.get('q') or None
            sql = "SELECT * FROM `tb_residu_ptsl_tahun_berjalan` WHERE lokasi_desa != 'Total'AND ( created_at LIKE '%{}%' OR lokasi_desa LIKE '%{}%') ORDER BY id DESC".format(
                search, search)

            # print(sql)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()
    return render_template(template, random=random, results=results)


@login_required
@app.route('/view_berkas_tanpa_bidang_tanah.<string:random>', methods=['GET'])
def view_berkas_tanpa_bidang_tanah(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    template = '/renderer/view_berkas_tanpa_bidang_tanah.html'

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            sql = """SELECT * FROM `tb_early_warning_berkas_tanpa_bidang_tanah` WHERE created_at LIKE '%{}%' AND desa != 'Total' AND created_at = (
    SELECT MAX(created_at)
    FROM `tb_early_warning_berkas_tanpa_bidang_tanah` AS b
    WHERE 1) ORDER BY id DESC""".format(
                datetime.date.today())
            # print(sql)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()
    return render_template(template, random=random, results=results)


@login_required
@app.route('/view_berkas_tanpa_bidang_tanah_search.<string:random>', methods=['GET'])
def view_berkas_tanpa_bidang_tanah_search(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    template = '/renderer/view_berkas_tanpa_bidang_tanah.html'

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            '''
            sql = """SELECT * FROM `tb_early_warning_berkas_tanpa_bidang_tanah` WHERE created_at LIKE '%{}%' AND desa != 'Total' AND created_at = (
    SELECT MAX(created_at)
    FROM `tb_early_warning_berkas_tanpa_bidang_tanah` AS b
    WHERE 1)""".format(
                datetime.date.today())
                '''
            search = request.args.get('q') or None
            sql = "SELECT * FROM `tb_early_warning_berkas_tanpa_bidang_tanah` WHERE desa != 'Total' AND (desa LIKE '%{}%' OR kecamatan LIKE '%{}%' OR created_at LIKE '%{}%') ORDER BY id DESC".format(
                search, search, search)
            # print(sql)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()
    return render_template(template, random=random, results=results)


@login_required
@app.route('/view_berkas_tanpa_data_yuridis.<string:random>', methods=['GET'])
def view_berkas_tanpa_data_yuridis(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    template = '/renderer/view_berkas_tanpa_data_yuridis.html'

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            sql = """SELECT * FROM `tb_early_warning_bidang_tanah_tanpa_data_yuridis_kantah` WHERE created_at LIKE '%{}%' AND desa != 'Total' AND created_at = (
    SELECT MAX(created_at)
    FROM `tb_early_warning_bidang_tanah_tanpa_data_yuridis_kantah` AS b
    WHERE 1) ORDER BY id DESC""".format(
                datetime.date.today())
            # print(sql)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()
    return render_template(template, random=random, results=results)


@login_required
@app.route('/view_berkas_tanpa_data_yuridis_search.<string:random>', methods=['GET'])
def view_berkas_tanpa_data_yuridis_search(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    template = '/renderer/view_berkas_tanpa_data_yuridis.html'

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            '''
            sql = """SELECT * FROM `tb_early_warning_bidang_tanah_tanpa_data_yuridis_kantah` WHERE created_at LIKE '%{}%' AND desa != 'Total' AND created_at = (
    SELECT MAX(created_at)
    FROM `tb_early_warning_bidang_tanah_tanpa_data_yuridis_kantah` AS b
    WHERE 1)""".format(
                datetime.date.today())
                '''
            search = request.args.get('q') or None
            sql = "SELECT * FROM `tb_early_warning_bidang_tanah_tanpa_data_yuridis_kantah` WHERE desa != 'Total' AND (desa LIKE '%{}%' OR kecamatan LIKE '%{}%' OR created_at LIKE '%{}%') ORDER BY id DESC".format(
                search, search, search)
            # print(sql)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()
    return render_template(template, random=random, results=results)


@login_required
@app.route('/view_pengumuman_kadaluwarsa.<string:random>', methods=['GET'])
def view_pengumuman_kadaluwarsa(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    template = '/renderer/view_pengumuman_kadaluwarsa.html'

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            sql = """SELECT * FROM `tb_early_warning_pengumuman_kadaluwarsa_kantor_pertanahan` WHERE created_at LIKE '%{}%' AND desa != 'Total' AND created_at = (
    SELECT MAX(created_at)
    FROM `tb_early_warning_pengumuman_kadaluwarsa_kantor_pertanahan` AS b
    WHERE 1) ORDER BY id DESC""".format(
                datetime.date.today())
            # print(sql)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()
    return render_template(template, random=random, results=results)


@login_required
@app.route('/view_pengumuman_kadaluwarsa_search.<string:random>', methods=['GET'])
def view_pengumuman_kadaluwarsa_search(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    template = '/renderer/view_pengumuman_kadaluwarsa.html'

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            '''
            sql = """SELECT * FROM `tb_early_warning_pengumuman_kadaluwarsa_kantor_pertanahan` WHERE created_at LIKE '%{}%' AND desa != 'Total' AND created_at = (
    SELECT MAX(created_at)
    FROM `tb_early_warning_pengumuman_kadaluwarsa_kantor_pertanahan` AS b
    WHERE 1)""".format(
                datetime.date.today())
            print(sql)
            '''

            search = request.args.get('q') or None
            sql = "SELECT * FROM `tb_early_warning_pengumuman_kadaluwarsa_kantor_pertanahan` WHERE desa != 'Total' AND (desa LIKE '%{}%' OR kecamatan LIKE '%{}%' OR created_at LIKE '%{}%') ORDER BY id DESC".format(
                search, search, search)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()
    return render_template(template, random=random, results=results)


@login_required
@app.route('/view_berkas_tanpa_pemohon.<string:random>', methods=['GET'])
def view_berkas_tanpa_pemohon(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    template = '/renderer/view_berkas_tanpa_pemohon.html'

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            sql = """SELECT * FROM `tb_early_warning_berkas_tanpa_pemohon` WHERE created_at LIKE '%{}%' AND desa != 'Total' AND created_at = (
    SELECT MAX(created_at)
    FROM `tb_early_warning_berkas_tanpa_pemohon` AS b
    WHERE 1) ORDER BY id DESC""".format(
                datetime.date.today())
            # print(sql)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()
    return render_template(template, random=random, results=results)


@login_required
@app.route('/view_berkas_tanpa_pemohon_search.<string:random>', methods=['GET'])
def view_berkas_tanpa_pemohon_search(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    template = '/renderer/view_berkas_tanpa_pemohon.html'

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            '''
            sql = """SELECT * FROM `tb_early_warning_berkas_tanpa_pemohon` WHERE created_at LIKE '%{}%' AND desa != 'Total' AND created_at = (
    SELECT MAX(created_at)
    FROM `tb_early_warning_berkas_tanpa_pemohon` AS b
    WHERE 1)""".format(
                datetime.date.today())
'''
            search = request.args.get('q') or None
            sql = "SELECT * FROM `tb_early_warning_berkas_tanpa_pemohon` WHERE desa != 'Total' AND (desa LIKE '%{}%' OR kecamatan LIKE '%{}%' OR created_at LIKE '%{}%') ORDER BY id DESC".format(
                search, search, search)
            # print(sql)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()
    return render_template(template, random=random, results=results)


@login_required
@app.route('/view_progres_anggaran_ptsl.<string:random>', methods=['GET'])
def view_progres_anggaran_ptsl(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    template = '/renderer/view_progres_anggaran_ptsl.html'

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            sql = """SELECT * FROM `tb_progres_ptsl_kantah_anggaran` WHERE created_at LIKE '%{}%' AND created_at = (
    SELECT MAX(created_at)
    FROM `tb_progres_ptsl_kantah_anggaran` AS b
    WHERE 1
) ORDER BY id DESC""".format(
                datetime.date.today())
            # print(sql)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()
    return render_template(template, random=random, results=results)


@login_required
@app.route('/view_progres_anggaran_ptsl_search.<string:random>', methods=['GET'])
def view_progres_anggaran_ptsl_search(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    template = '/renderer/view_progres_anggaran_ptsl.html'

    conn = pymysql.connect(**db_config)
    results = None
    try:
        with conn.cursor() as cur:
            '''
            sql = """SELECT * FROM `tb_progres_ptsl_kantah_anggaran` WHERE created_at LIKE '%{}%' AND created_at = (
    SELECT MAX(created_at)
    FROM `tb_progres_ptsl_kantah_anggaran` AS b
    WHERE 1
) """.format(
                datetime.date.today())
                '''
            search = request.args.get('q') or None
            sql = "SELECT * FROM `tb_progres_ptsl_kantah_anggaran` WHERE created_at LIKE '%{}%' ORDER BY id DESC".format(
                search)
            # print(sql)
            cur.execute(sql)
            results = cur.fetchall()
    finally:
        conn.close()
    return render_template(template, random=random, results=results)

@login_required
@app.route('/view_pnbp.<string:random>', methods=['GET'])
def view_pnbp(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))
    template = '/renderer/view_pnbp.html'

    conn = pymysql.connect(**db_config)
    results_total_potensi_pencairan = None
    try:
        with conn.cursor() as cur:
            cur.execute("SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")

            sql = "select * from tb_tunggakan_penerimaan_dimuka_detail_permohonan ORDER BY id ASC"
            cur.execute(sql)
            results = cur.fetchall()

            sql = "SELECT nama_prosedur, SUM(besarnya) AS total FROM `tb_tunggakan_penerimaan_dimuka_detail_permohonan` GROUP BY nama_prosedur ORDER BY nama_prosedur ASC"
            cur.execute(sql)
            results_permohonan_per_layanan = cur.fetchall()

            sql = "select sum(besarnya) as total from tb_tunggakan_penerimaan_dimuka_detail_permohonan"
            cur.execute(sql)
            results_total_potensi_pencairan = cur.fetchone()

            sql = "select count(*) as total from tb_tunggakan_penerimaan_dimuka_detail_permohonan"
            cur.execute(sql)
            results_total_berkas = cur.fetchone()

    finally:
        conn.close()
    return render_template(template, random=random, results=results,
                           results_permohonan_per_layanan=results_permohonan_per_layanan,
                           results_total_potensi_pencairan=results_total_potensi_pencairan,
                           results_total_berkas=results_total_berkas
                           )
    # return str(results_total_berkas_pnbp)
    
    
@login_required
@app.route('/view_get_tim_detail_by_desa.<string:random>.<string:desa>', methods=['GET'])
def view_get_tim_detail_by_desa(random, desa):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    results = None
    anggota = None
    result = {}
    response = '<div class="ui inverted segment"><div class="ui inverted celled ordered list">'
    conn = pymysql.connect(**db_config)
    try:
        with conn.cursor() as cur:
            sql = "SELECT * FROM `tb_tim_ptsl` WHERE daftar_desa LIKE '%{}%'".format(desa)
            cur.execute(sql)
            results = cur.fetchall()

            if cur.rowcount > 0:
                for data in results:
                    anggota = data['daftar_pegawai']
                    anggota_ids = anggota.split(',')

                    for anggota_id in anggota_ids:
                        sql = "SELECT * FROM `tb_user` WHERE id LIKE '%{}%'".format(anggota_id)
                        cur.execute(sql)
                        if cur.rowcount > 0:
                            results = cur.fetchone()

                            for key, value in results.items():
                                if value not in result.values():
                                    result[key] = value
                                    # print('{} ============'.format(str(result)))

                            response += str(
                                "<div class='item'>{} / {} / {}</div>".format((result['nama']), str(result['jabatan']),
                                                                              str(data['tim_nama'])))
            else:
                response += str(
                    "<div class='item'>Tidak ada data</div>")

    finally:
        conn.close()

    response += '</div></div>'

    return response


@app.route('/mysqlversion')
def mysqlversion():
    conn = pymysql.connect(**db_config)
    cur = conn.cursor()
    cur.execute("select @@version")
    output = cur.fetchall()
    conn.close()
    return str(output)


'''
Action Form and Redirect =========================================================
'''

'''
{
  "csrf_token": "IjdlMjA0N2E1MjlmMjlhYjA4YTRjMzY5MzAyMWEzZGY5NjBjZTljZGMi.YYU_8Q.YtXwLwOlxpS_LxInFhsoilzjKBM", 
  "email": "me@rezayogaswara.com", 
  "id": "gAAAAABhhT_xemlz0v0dFXOrJL6ERxV8m3ku3nc295xBJak9qQdg8ciKIF7EhZ15D0WQH2pYkFJTISe5GTkMH5U8U3N0KZ_y5Q==", 
  "nama": "Reza Yogaswara", 
  "nip": "198510182011011006", 
  "password_baru": "", 
  "password_baru_konfirmasi": "", 
  "password_lama": ""
}
'''


@app.route('/action_form_ubah_akun.<string:random>', methods=['POST'])
def action_form_ubah_akun(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    conn = pymysql.connect(**db_config)
    if md5(request.form['password_lama'].strip().encode("utf-8")).hexdigest() == session['USER']['password'] and \
            request.form['password_baru_konfirmasi'] != '' and request.form['password_baru'] == request.form[
        'password_baru_konfirmasi']:
        try:
            with conn.cursor() as cur:
                sql = "UPDATE `tb_user` SET `password` = %s WHERE id = %s"

                # Execute the query
                cur.execute(sql, (
                    md5(request.form['password_baru_konfirmasi'].strip().encode("utf-8")).hexdigest(),
                    decrypt_string(request.form['id'])
                ))

                flash(Markup('<div class="ui success floating message">Data anda berhasil diperbarui!</div>'))
                # the connection is not autocommited by default. So we must commit to save our changes.
                conn.commit()

        finally:
            # close the database connection using close() method.
            conn.close()
    else:
        flash(Markup(
            '<div class="ui error floating message">Akun anda gagal diperbarui, pastikan password lama anda sesuai dan password konfirmasi sama dengan password baru!</div>'))
    return redirect(url_for('dashboard', random=random))


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('USER', None)
    session.clear()
    return redirect(url_for('index', random=encrypted_string))


@app.route('/action_form_login.<string:random>', methods=['POST'])
def action_form_login(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    login_form = LoginForm()
    if login_form.validate_on_submit():
        # print("{} is not from {}. It is from {}.".format(self.name, to_compare, self.origin))
        email = request.form['email'].strip()
        password = md5(request.form['password'].strip().encode("utf-8")).hexdigest()
        conn = pymysql.connect(**db_config)
        results = None
        try:
            with conn.cursor() as cur:
                sql = "SELECT * FROM `tb_user` WHERE role = 'ADMIN' AND email = '{}' AND password = '{}'".format(email,
                                                                                                                 str(password))
                # print(sql)
                # exit()
                cur.execute(sql)
                results = cur.fetchall()

                if len(results) == 1:
                    # print(results[0])
                    # print(type(results[0]))
                    session['USER'] = results[0]
                    return redirect(url_for('dashboard', random=random))
                else:
                    return render_template('index.html', web_config=web_config, form=login_form,
                                           error_login='invalid account!', random=encrypted_string)
        finally:
            conn.close()

    return render_template('index.html', web_config=web_config, form=login_form, random=encrypted_string)


'''
Pegawai CRUD =========================================================
'''


@app.route('/action_form_hapus_pegawai.<string:random>', methods=['GET'])
def action_form_hapus_pegawai(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    id = request.args.get('id') or None

    # print(id)

    result = 'Error'
    if id != None:
        conn = pymysql.connect(**db_config)
        try:
            with conn.cursor() as cur:
                sql = "DELETE FROM `tb_user` WHERE id = %s"
                cur.execute(sql, id)
                conn.commit()
                # print("{} record deleted".format(cur.rowcount))
                result = "{} record deleted".format(cur.rowcount)
                flash(Markup('<div class="ui error floating message">{}</div>'.format(result)))
        except Exception as error:
            flash(Markup('<div class="ui error floating message">Gagal menghapus data!</div>'))
            print("Failed to delete record from table: {}".format(error))
        finally:
            conn.close()
    return redirect(url_for('dashboard', random=random, m=web_menu['MENU_PEGAWAI']))


@app.route('/action_form_tambah_pegawai.<string:random>', methods=['POST'])
def action_form_tambah_pegawai(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    conn = pymysql.connect(**db_config)
    try:
        with conn.cursor() as cur:
            sql = "INSERT INTO `tb_user` (`nama`, `email`, `jabatan`, `nip`, `password`, `mailed`, `role`, `created_at` ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

            # Execute the query
            cur.execute(sql, (
                request.form['nama'],
                request.form['email'],
                request.form['jabatan'],
                request.form['nip'],
                md5(request.form['password'].strip().encode("utf-8")).hexdigest(),
                request.form['status_mailed'],
                request.form['status_role'],
                get_current_date(True)))

            flash(Markup('<div class="ui success floating message">Data pegawai berhasil ditambahkan!</div>'))
            # the connection is not autocommited by default. So we must commit to save our changes.
            conn.commit()

    finally:
        # close the database connection using close() method.
        conn.close()
    return redirect(url_for('dashboard', random=random, m=web_menu['MENU_PEGAWAI']))


@app.route('/action_form_ubah_pegawai.<string:random>', methods=['POST'])
def action_form_ubah_pegawai(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    conn = pymysql.connect(**db_config)
    try:
        with conn.cursor() as cur:
            sql = "UPDATE `tb_user` SET `nama` = %s, `email` = %s, `jabatan` = %s, `nip` = %s, `mailed` = %s, `role` = %s WHERE id = %s"

            # Execute the query
            cur.execute(sql, (
                request.form['nama'],
                request.form['email'],
                request.form['jabatan'],
                request.form['nip'],
                request.form['status_mailed'],
                request.form['status_role'],
                decrypt_string(request.form['id'])
            ))

            flash(Markup('<div class="ui success floating message">Data pegawai berhasil diperbarui!</div>'))
            # the connection is not autocommited by default. So we must commit to save our changes.
            conn.commit()

    finally:
        # close the database connection using close() method.
        conn.close()
    return redirect(url_for('dashboard', random=random, m=web_menu['MENU_PEGAWAI']))


'''
Tim PTSL CRUD =========================================================
'''


@app.route('/action_form_hapus_tim_ptsl.<string:random>', methods=['GET'])
def action_form_hapus_tim_ptsl(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    id = request.args.get('id') or None

    # print(id)

    result = 'Error'
    if id != None:
        conn = pymysql.connect(**db_config)
        try:
            with conn.cursor() as cur:
                sql = "DELETE FROM `tb_tim_ptsl` WHERE id = %s"
                cur.execute(sql, id)
                conn.commit()
                # print("{} record deleted".format(cur.rowcount))
                result = "{} record deleted".format(cur.rowcount)
                flash(Markup('<div class="ui error floating message">{}</div>'.format(result)))
        except Exception as error:
            flash(Markup('<div class="ui error floating message">Gagal menghapus data!</div>'))
            print("Failed to delete record from table: {}".format(error))
        finally:
            conn.close()
    return redirect(url_for('dashboard', random=random, m=web_menu['MENU_TIM_PTSL']))


@app.route('/action_form_tambah_tim_ptsl.<string:random>', methods=['POST'])
def action_form_tambah_tim_ptsl(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    conn = pymysql.connect(**db_config)
    try:
        with conn.cursor() as cur:
            sql = "INSERT INTO `tb_tim_ptsl` (`tim_nama`, `daftar_pegawai`, `daftar_desa`, `created_at` ) VALUES (%s,%s, %s, %s)"

            # Execute the query
            cur.execute(sql, (
                request.form['tim_nama'],
                request.form['daftar_anggota'],
                request.form['daftar_desa'],
                get_current_date(True)))

            flash(Markup('<div class="ui success floating message">Data tim PTSL berhasil ditambahkan!</div>'))
            # the connection is not autocommited by default. So we must commit to save our changes.
            conn.commit()

    finally:
        # close the database connection using close() method.
        conn.close()
    return redirect(url_for('dashboard', random=random, m=web_menu['MENU_TIM_PTSL']))


@app.route('/action_form_ubah_tim_ptsl.<string:random>', methods=['POST'])
def action_form_ubah_tim_ptsl(random):
    try:
        f.decrypt(bytes(unquote(random), encoding='utf-8')).decode("utf-8")
    except:
        session.pop('USER', None)
        session.clear()
        flash(Markup('<div class="ui error floating message">Invalid URL!</div>'))
        return redirect(url_for('index', random=encrypted_string))

    conn = pymysql.connect(**db_config)
    try:
        with conn.cursor() as cur:
            sql = "UPDATE `tb_tim_ptsl` SET `tim_nama` = %s, `daftar_pegawai` = %s, `daftar_desa` = %s WHERE id = %s"

            # Execute the query
            cur.execute(sql, (
                request.form['tim_nama'],
                request.form['daftar_anggota'],
                request.form['daftar_desa'],
                decrypt_string(request.form['id'])
            ))

            flash(Markup('<div class="ui success floating message">Data tim PTSL berhasil diperbarui!</div>'))
            # the connection is not autocommited by default. So we must commit to save our changes.
            conn.commit()

    finally:
        # close the database connection using close() method.
        conn.close()
    return redirect(url_for('dashboard', random=random, m=web_menu['MENU_TIM_PTSL']))


@app.route('/foo', methods=('GET', 'POST'))
@csrf.exempt
def foo():
    # ...
    return 'foo'


@app.route('/bar', methods=('GET', 'POST'))
def bar():
    # ...
    return 'bar'
