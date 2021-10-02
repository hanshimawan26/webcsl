import time
import ssl
from flask import Flask, render_template, url_for, request, redirect, session, flash
from datetime import datetime
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import os
import random
import string

app = Flask(__name__)
app.secret_key = 'xcvbnm,cvbnm,dcvfbgnhmj,kcvbnm,dcvfbghnmj'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pendaf.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
context = ssl.SSLContext()
context.load_cert_chain('/root/webcsl/fullchain.pem', '/root/webcsl/privkey.pem')

db = SQLAlchemy(app)
global pwd_input
global code_input
datapeserta = None
numberid = None
nomorpeserta_input = None
code_input = None
pwd_input = None
password = "dajelek"

def sisakuota(filled, max) :
    sisa = max - filled
    return(sisa)

def inisialcabang(cabang_data):
    if cabang_data=="chess":
        output = "CL"
        return(output)
    elif cabang_data=="film":
        output = "FP"
        return(output)
    elif cabang_data=="basketputra":
        output = "BS-M"
        return(output)
    elif cabang_data=="basketputri":
        output = "BS-F"
        return(output)
    elif cabang_data=="band":
        output = "BA"
        return(output)
    elif cabang_data=="dance":
        output = "MD"
        return(output)
    elif cabang_data=="foto":
        output = "FG"
        return(output)
    elif cabang_data=="debat":
        output = "ED"
        return(output)
    elif cabang_data=="pidato":
        output = "PI"
        return(output)
    elif cabang_data=="kosong":
        output = "PS-K"
        return(output)
    elif cabang_data=="senjata":
        output = "PS-B"
        return(output)
    elif cabang_data=="ganda":
        output = "PS-G"
        return(output)
    elif cabang_data=="padus":
        output = "PD"
        return(output)
    elif cabang_data=="design":
        output = "SD"
        return(output)

def biaya(cabang_data):
    if cabang_data=="chess":
        output = "75"
        return(output)
    elif cabang_data=="film":
        output = "75"
        return(output)
    elif cabang_data=="basketputra":
        output = "75"
        return(output)
    elif cabang_data=="basketputri":
        output = "75"
        return(output)
    elif cabang_data=="band":
        output = "75"
        return(output)
    elif cabang_data=="dance":
        output = "75"
        return(output)
    elif cabang_data=="foto":
        output = "75"
        return(output)
    elif cabang_data=="debat":
        output = "75"
        return(output)
    elif cabang_data=="pidato":
        output = "75"
        return(output)
    elif cabang_data=="kosong":
        output = "75"
        return(output)
    elif cabang_data=="senjata":
        output = "75"
        return(output)
    elif cabang_data=="ganda":
        output = "75"
        return(output)
    elif cabang_data=="padus":
        output = "75"
        return(output)
    elif cabang_data=="design":
        output = "75"
        return(output)

def id_generator(size=3, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

def kodepeserta(id, inisial):
    if id<100:
        if id<10:
            kodenomor="CSL"+"-"+inisial+"-"+"00"+str(id)+"-"+id_generator()
            return(kodenomor)
        else:
            kodenomor="CSL"+"-"+inisial+"-"+"0"+str(id)+"-"+id_generator()
            return(kodenomor)
    else:
        kodenomor="CSL"+"-"+inisial+"-"+str(id)+"-"+id_generator()
        return(kodenomor)

def kodeunik(id):
    if id>800:
        id=id-800

    if id<100:
        if id<10:
            unik="00"+str(id)
            return(unik)
        else:
            unik="0"+str(id)
            return(unik)
    else:
        unik=str(id)
        return(unik)

def biayapeserta(biaya, kodeunik):
    biayaakhir= "Rp "+ biaya+"."+kodeunik
    return(biayaakhir)

class peserta (db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    #waktuisi = db.Column (db.DateTime, nullable=False)
    sekolah_data = db.Column (db.String(100), nullable=False)
    user_data = db.Column (db.String(100), nullable=False)
    cabang_data = db.Column (db.String(60), nullable=False)
    catur_kuota = db.Column (db.Integer)
    film_kuota = db.Column (db.Integer)
    basketputra_kuota = db.Column (db.Integer)
    basketputri_kuota = db.Column (db.Integer)
    band_kuota = db.Column (db.Integer)
    dance_kuota = db.Column (db.Integer)
    foto_kuota = db.Column (db.Integer)
    debat_kuota = db.Column (db.Integer)
    pidato_kuota = db.Column (db.Integer)
    kosong_kuota = db.Column (db.Integer)
    senjata_kuota = db.Column (db.Integer)
    ganda_kuota = db.Column (db.Integer)
    padus_kuota = db.Column (db.Integer)
    design_kuota = db.Column (db.Integer)
    suratketerangan_data = db.Column (db.String(100), nullable=False)
    inisialcabang_data = db.Column (db.String(100), nullable=False)
    biaya_data = db.Column (db.String(100), nullable=False)
    kodepeserta_data = db.Column (db.String(100))
    kodeunik_data = db.Column (db.String(100))
    biayapeserta_data = db.Column (db.String(100))
    nama_1_data = db.Column (db.String(500), nullable=False)
    telpon_1_data = db.Column (db.String(500), nullable=False)
    email_1_data = db.Column (db.String(500), nullable=False)
    lahir_1_data = db.Column (db.String(500), nullable=False)
    nama_2_data = db.Column (db.String(500))
    telpon_2_data = db.Column (db.String(500))
    email_2_data = db.Column (db.String(500))
    lahir_2_data = db.Column (db.String(500))
    nama_3_data = db.Column (db.String(500))
    telpon_3_data = db.Column (db.String(500))
    email_3_data = db.Column (db.String(500))
    lahir_3_data = db.Column (db.String(500))
    nama_4_data = db.Column (db.String(500))
    telpon_4_data = db.Column (db.String(500))
    email_4_data = db.Column (db.String(500))
    lahir_4_data = db.Column (db.String(500))
    nama_5_data = db.Column (db.String(500))
    telpon_5_data = db.Column (db.String(500))
    email_5_data = db.Column (db.String(500))
    lahir_5_data = db.Column (db.String(500))
    nama_6_data = db.Column (db.String(500))
    telpon_6_data = db.Column (db.String(500))
    email_6_data = db.Column (db.String(500))
    lahir_6_data = db.Column (db.String(500))
    nama_7_data = db.Column (db.String(500))
    telpon_7_data = db.Column (db.String(500))
    email_7_data = db.Column (db.String(500))
    lahir_7_data = db.Column (db.String(500))
    nama_8_data = db.Column (db.String(500))
    telpon_8_data = db.Column (db.String(500))
    email_8_data = db.Column (db.String(500))
    lahir_8_data = db.Column (db.String(500))
    nama_9_data = db.Column (db.String(500))
    telpon_9_data = db.Column (db.String(500))
    email_9_data = db.Column (db.String(500))
    lahir_9_data = db.Column (db.String(500))
    nama_10_data = db.Column (db.String(500))
    telpon_10_data = db.Column (db.String(500))
    email_10_data = db.Column (db.String(500))
    lahir_10_data = db.Column (db.String(500))
    nama_11_data = db.Column (db.String(500))
    telpon_11_data = db.Column (db.String(500))
    email_11_data = db.Column (db.String(500))
    lahir_11_data = db.Column (db.String(500))
    nama_12_data = db.Column (db.String(500))
    telpon_12_data = db.Column (db.String(500))
    email_12_data = db.Column (db.String(500))
    lahir_12_data = db.Column (db.String(500))
    nama_13_data = db.Column (db.String(500))
    telpon_13_data = db.Column (db.String(500))
    email_13_data = db.Column (db.String(500))
    lahir_13_data = db.Column (db.String(500))
    nama_14_data = db.Column (db.String(500))
    telpon_14_data = db.Column (db.String(500))
    email_14_data = db.Column (db.String(500))
    lahir_14_data = db.Column (db.String(500))
    nama_15_data = db.Column (db.String(500))
    telpon_15_data = db.Column (db.String(500))
    email_15_data = db.Column (db.String(500))
    lahir_15_data = db.Column (db.String(500))
    nama_16_data = db.Column (db.String(500))
    telpon_16_data = db.Column (db.String(500))
    email_16_data = db.Column (db.String(500))
    lahir_16_data = db.Column (db.String(500))
    nama_17_data = db.Column (db.String(500))
    telpon_17_data = db.Column (db.String(500))
    email_17_data = db.Column (db.String(500))
    lahir_17_data = db.Column (db.String(500))
    nama_18_data = db.Column (db.String(500))
    telpon_18_data = db.Column (db.String(500))
    email_18_data = db.Column (db.String(500))
    lahir_18_data = db.Column (db.String(500))
    nama_19_data = db.Column (db.String(500))
    telpon_19_data = db.Column (db.String(500))
    email_19_data = db.Column (db.String(500))
    lahir_19_data = db.Column (db.String(500))
    nama_20_data = db.Column (db.String(500))
    telpon_20_data = db.Column (db.String(500))
    email_20_data = db.Column (db.String(500))
    lahir_20_data = db.Column (db.String(500))
    verifikasi_data = db.Column (db.String(500))


    def __init__(self, sekolah_data, user_data, cabang_data, catur_kuota, film_kuota, basketputra_kuota, basketputri_kuota, band_kuota, dance_kuota, foto_kuota, debat_kuota, pidato_kuota, kosong_kuota, senjata_kuota, ganda_kuota, padus_kuota, design_kuota, suratketerangan_data, inisialcabang_data, biaya_data, kodepeserta_data, kodeunik_data, biayapeserta_data, nama_1_data, telpon_1_data, email_1_data, lahir_1_data, nama_2_data, telpon_2_data, email_2_data, lahir_2_data, nama_3_data, telpon_3_data, email_3_data, lahir_3_data, nama_4_data, telpon_4_data, email_4_data, lahir_4_data, nama_5_data, telpon_5_data, email_5_data, lahir_5_data, nama_6_data, telpon_6_data, email_6_data, lahir_6_data, nama_7_data, telpon_7_data, email_7_data, lahir_7_data, nama_8_data, telpon_8_data, email_8_data, lahir_8_data, nama_9_data, telpon_9_data, email_9_data, lahir_9_data, nama_10_data, telpon_10_data, email_10_data, lahir_10_data, nama_11_data, telpon_11_data, email_11_data, lahir_11_data, nama_12_data, telpon_12_data, email_12_data, lahir_12_data, nama_13_data, telpon_13_data, email_13_data, lahir_13_data, nama_14_data, telpon_14_data, email_14_data, lahir_14_data, nama_15_data, telpon_15_data, email_15_data, lahir_15_data, nama_16_data, telpon_16_data, email_16_data, lahir_16_data, nama_17_data, telpon_17_data, email_17_data, lahir_17_data, nama_18_data, telpon_18_data, email_18_data, lahir_18_data, nama_19_data, telpon_19_data, email_19_data, lahir_19_data, nama_20_data, telpon_20_data, email_20_data, lahir_20_data, verifikasi_data):
        #self.waktuisi = waktuisi
        self.sekolah_data = sekolah_data
        self.user_data = user_data
        self.cabang_data = cabang_data
        self.catur_kuota = catur_kuota
        self.film_kuota = film_kuota
        self.basketputra_kuota = basketputra_kuota
        self.basketputri_kuota = basketputri_kuota
        self.band_kuota = band_kuota
        self.dance_kuota = dance_kuota
        self.foto_kuota = foto_kuota
        self.debat_kuota = debat_kuota
        self.pidato_kuota = pidato_kuota
        self.kosong_kuota = kosong_kuota
        self.senjata_kuota = senjata_kuota
        self.ganda_kuota = ganda_kuota
        self.padus_kuota = padus_kuota
        self.design_kuota = design_kuota
        self.suratketerangan_data = suratketerangan_data
        self.inisialcabang_data = inisialcabang_data
        self.biaya_data = biaya_data
        self.kodepeserta_data = kodepeserta_data
        self.kodeunik_data = kodeunik_data
        self.biayapeserta_data = biayapeserta_data
        self.nama_1_data = nama_1_data
        self.telpon_1_data = telpon_1_data
        self.email_1_data = email_1_data
        self.lahir_1_data = lahir_1_data
        self.nama_2_data = nama_2_data
        self.telpon_2_data = telpon_2_data
        self.email_2_data = email_2_data
        self.lahir_2_data = lahir_2_data
        self.nama_3_data = nama_3_data
        self.telpon_3_data = telpon_3_data
        self.email_3_data = email_3_data
        self.lahir_3_data = lahir_3_data
        self.nama_4_data = nama_4_data
        self.telpon_4_data = telpon_4_data
        self.email_4_data = email_4_data
        self.lahir_4_data = lahir_4_data
        self.nama_5_data = nama_5_data
        self.telpon_5_data = telpon_5_data
        self.email_5_data = email_5_data
        self.lahir_5_data = lahir_5_data
        self.nama_6_data = nama_6_data
        self.telpon_6_data = telpon_6_data
        self.email_6_data = email_6_data
        self.lahir_6_data = lahir_6_data
        self.nama_7_data = nama_7_data
        self.telpon_7_data = telpon_7_data
        self.email_7_data = email_7_data
        self.lahir_7_data = lahir_7_data
        self.nama_8_data = nama_8_data
        self.telpon_8_data = telpon_8_data
        self.email_8_data = email_8_data
        self.lahir_8_data = lahir_8_data
        self.nama_9_data = nama_9_data
        self.telpon_9_data = telpon_9_data
        self.email_9_data = email_9_data
        self.lahir_9_data = lahir_9_data
        self.nama_10_data = nama_10_data
        self.telpon_10_data = telpon_10_data
        self.email_10_data = email_10_data
        self.lahir_10_data = lahir_10_data
        self.nama_11_data = nama_11_data
        self.telpon_11_data = telpon_11_data
        self.email_11_data = email_11_data
        self.lahir_11_data = lahir_11_data
        self.nama_12_data = nama_12_data
        self.telpon_12_data = telpon_12_data
        self.email_12_data = email_12_data
        self.lahir_12_data = lahir_12_data
        self.nama_13_data = nama_13_data
        self.telpon_13_data = telpon_13_data
        self.email_13_data = email_13_data
        self.lahir_13_data = lahir_13_data
        self.nama_14_data = nama_14_data
        self.telpon_14_data = telpon_14_data
        self.email_14_data = email_14_data
        self.lahir_14_data = lahir_14_data
        self.nama_15_data = nama_15_data
        self.telpon_15_data = telpon_15_data
        self.email_15_data = email_15_data
        self.lahir_15_data = lahir_15_data
        self.nama_16_data = nama_16_data
        self.telpon_16_data = telpon_16_data
        self.email_16_data = email_16_data
        self.lahir_16_data = lahir_16_data
        self.nama_17_data = nama_17_data
        self.telpon_17_data = telpon_17_data
        self.email_17_data = email_17_data
        self.lahir_17_data = lahir_17_data
        self.nama_18_data = nama_18_data
        self.telpon_18_data = telpon_18_data
        self.email_18_data = email_18_data
        self.lahir_18_data = lahir_18_data
        self.nama_19_data = nama_19_data
        self.telpon_19_data = telpon_19_data
        self.email_19_data = email_19_data
        self.lahir_19_data = lahir_19_data
        self.nama_20_data = nama_20_data
        self.telpon_20_data = telpon_20_data
        self.email_20_data = email_20_data
        self.lahir_20_data = lahir_20_data
        self.verifikasi_data = verifikasi_data

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/pendaf', methods=['POST','GET'])
def index():
    if request.method == "POST":
        print("loaded index")
        sekolah_data = None
        user_data = None
        cabang_data = None
        suratketerangan_data = None
        session.permanent = True

        catur_kuota = 0
        film_kuota = 0
        basketputra_kuota = 0
        basketputri_kuota = 0
        band_kuota = 0
        dance_kuota = 0
        foto_kuota = 0
        debat_kuota = 0
        pidato_kuota = 0
        kosong_kuota = 0
        senjata_kuota = 0
        ganda_kuota = 0
        padus_kuota = 0
        design_kuota = 0

        nama_1_data = None
        telpon_1_data = None
        email_1_data = None
        lahir_1_data = None

        nama_2_data = None
        telpon_2_data = None
        email_2_data = None
        lahir_2_data = None

        nama_3_data = None
        telpon_3_data = None
        email_3_data = None
        lahir_3_data = None

        nama_4_data = None
        telpon_4_data = None
        email_4_data = None
        lahir_4_data = None

        nama_5_data = None
        telpon_5_data = None
        email_5_data = None
        lahir_5_data = None

        nama_6_data = None
        telpon_6_data = None
        email_6_data = None
        lahir_6_data = None

        nama_7_data = None
        telpon_7_data = None
        email_7_data = None
        lahir_7_data = None

        nama_8_data = None
        telpon_8_data = None
        email_8_data = None
        lahir_8_data = None

        nama_9_data = None
        telpon_9_data = None
        email_9_data = None
        lahir_9_data = None

        nama_10_data = None
        telpon_10_data = None
        email_10_data = None
        lahir_10_data = None

        nama_11_data = None
        telpon_11_data = None
        email_11_data = None
        lahir_11_data = None

        nama_12_data = None
        telpon_12_data = None
        email_12_data = None
        lahir_12_data = None

        nama_13_data = None
        telpon_13_data = None
        email_13_data = None
        lahir_13_data = None

        nama_14_data = None
        telpon_14_data = None
        email_14_data = None
        lahir_14_data = None

        nama_15_data = None
        telpon_15_data = None
        email_15_data = None
        lahir_15_data = None

        nama_16_data = None
        telpon_16_data = None
        email_16_data = None
        lahir_16_data = None

        nama_17_data = None
        telpon_17_data = None
        email_17_data = None
        lahir_17_data = None

        nama_18_data = None
        telpon_18_data = None
        email_18_data = None
        lahir_18_data = None

        nama_19_data = None
        telpon_19_data = None
        email_19_data = None
        lahir_19_data = None

        nama_20_data = None
        telpon_20_data = None
        email_20_data = None
        lahir_20_data = None

        #app.permanent_session_lifetime = timedelta(minutes=1)
        print("post")
        #waktuisi = datetime.utcnow
        sekolah_data = request.form["sekolah"]
        user_data = request.form["user"]
        cabang_data = request.form["cabang"]
        suratketerangan_data = request.form["surat"]
        session["cabang_session"] = cabang_data
        session["sekolah_session"] = sekolah_data
        session["user_session"] = user_data

        nama_1_data = request.form["nama_1"]
        telpon_1_data = request.form["telpon_1"]
        email_1_data = request.form["email_1"]
        lahir_1_data = request.form["lahir_1"]
        session["nama_1_data"] = nama_1_data
        session["telpon_1_data"] = telpon_1_data
        session["email_1_data"] = email_1_data
        session["lahir_1_data"] = lahir_1_data

        nama_2_data = request.form["nama_2"]
        telpon_2_data = request.form["telpon_2"]
        email_2_data = request.form["email_2"]
        lahir_2_data = request.form["lahir_2"]
        session["nama_2_data"] = nama_2_data
        session["telpon_2_data"] = telpon_2_data
        session["email_2_data"] = email_2_data
        session["lahir_2_data"] = lahir_2_data

        nama_3_data = request.form["nama_3"]
        telpon_3_data = request.form["telpon_3"]
        email_3_data = request.form["email_3"]
        lahir_3_data = request.form["lahir_3"]
        session["nama_3_data"] = nama_3_data
        session["telpon_3_data"] = telpon_3_data
        session["email_3_data"] = email_3_data
        session["lahir_3_data"] = lahir_3_data

        nama_4_data = request.form["nama_4"]
        telpon_4_data = request.form["telpon_4"]
        email_4_data = request.form["email_4"]
        lahir_4_data = request.form["lahir_4"]
        session["nama_4_data"] = nama_4_data
        session["telpon_4_data"] = telpon_4_data
        session["email_4_data"] = email_4_data
        session["lahir_4_data"] = lahir_4_data

        nama_5_data = request.form["nama_5"]
        telpon_5_data = request.form["telpon_5"]
        email_5_data = request.form["email_5"]
        lahir_5_data = request.form["lahir_5"]
        session["nama_5_data"] = nama_5_data
        session["telpon_5_data"] = telpon_5_data
        session["email_5_data"] = email_5_data
        session["lahir_5_data"] = lahir_5_data

        nama_6_data = request.form["nama_6"]
        telpon_6_data = request.form["telpon_6"]
        email_6_data = request.form["email_6"]
        lahir_6_data = request.form["lahir_6"]
        session["nama_6_data"] = nama_6_data
        session["telpon_6_data"] = telpon_6_data
        session["email_6_data"] = email_6_data
        session["lahir_6_data"] = lahir_6_data

        nama_7_data = request.form["nama_7"]
        telpon_7_data = request.form["telpon_7"]
        email_7_data = request.form["email_7"]
        lahir_7_data = request.form["lahir_7"]
        session["nama_7_data"] = nama_7_data
        session["telpon_7_data"] = telpon_7_data
        session["email_7_data"] = email_7_data
        session["lahir_7_data"] = lahir_7_data

        nama_8_data = request.form["nama_8"]
        telpon_8_data = request.form["telpon_8"]
        email_8_data = request.form["email_8"]
        lahir_8_data = request.form["lahir_8"]
        session["nama_8_data"] = nama_8_data
        session["telpon_8_data"] = telpon_8_data
        session["email_8_data"] = email_8_data
        session["lahir_8_data"] = lahir_8_data

        nama_9_data = request.form["nama_9"]
        telpon_9_data = request.form["telpon_9"]
        email_9_data = request.form["email_9"]
        lahir_9_data = request.form["lahir_9"]
        session["nama_9_data"] = nama_9_data
        session["telpon_9_data"] = telpon_9_data
        session["email_9_data"] = email_9_data
        session["lahir_9_data"] = lahir_9_data

        nama_10_data = request.form["nama_10"]
        telpon_10_data = request.form["telpon_10"]
        email_10_data = request.form["email_10"]
        lahir_10_data = request.form["lahir_10"]
        session["nama_10_data"] = nama_10_data
        session["telpon_10_data"] = telpon_10_data
        session["email_10_data"] = email_10_data
        session["lahir_10_data"] = lahir_10_data

        nama_11_data = request.form["nama_11"]
        telpon_11_data = request.form["telpon_11"]
        email_11_data = request.form["email_11"]
        lahir_11_data = request.form["lahir_11"]
        session["nama_11_data"] = nama_11_data
        session["telpon_11_data"] = telpon_11_data
        session["email_11_data"] = email_11_data
        session["lahir_11_data"] = lahir_11_data

        nama_12_data = request.form["nama_12"]
        telpon_12_data = request.form["telpon_12"]
        email_12_data = request.form["email_12"]
        lahir_12_data = request.form["lahir_12"]
        session["nama_12_data"] = nama_12_data
        session["telpon_12_data"] = telpon_12_data
        session["email_12_data"] = email_12_data
        session["lahir_12_data"] = lahir_12_data

        nama_13_data = request.form["nama_13"]
        telpon_13_data = request.form["telpon_13"]
        email_13_data = request.form["email_13"]
        lahir_13_data = request.form["lahir_13"]
        session["nama_13_data"] = nama_13_data
        session["telpon_13_data"] = telpon_13_data
        session["email_13_data"] = email_13_data
        session["lahir_13_data"] = lahir_13_data

        nama_14_data = request.form["nama_14"]
        telpon_14_data = request.form["telpon_14"]
        email_14_data = request.form["email_14"]
        lahir_14_data = request.form["lahir_14"]
        session["nama_14_data"] = nama_14_data
        session["telpon_14_data"] = telpon_14_data
        session["email_14_data"] = email_14_data
        session["lahir_14_data"] = lahir_14_data

        nama_15_data = request.form["nama_15"]
        telpon_15_data = request.form["telpon_15"]
        email_15_data = request.form["email_15"]
        lahir_15_data = request.form["lahir_15"]
        session["nama_15_data"] = nama_15_data
        session["telpon_15_data"] = telpon_15_data
        session["email_15_data"] = email_15_data
        session["lahir_15_data"] = lahir_15_data

        nama_16_data = request.form["nama_16"]
        telpon_16_data = request.form["telpon_16"]
        email_16_data = request.form["email_16"]
        lahir_16_data = request.form["lahir_16"]
        session["nama_16_data"] = nama_16_data
        session["telpon_16_data"] = telpon_16_data
        session["email_16_data"] = email_16_data
        session["lahir_16_data"] = lahir_16_data

        nama_17_data = request.form["nama_17"]
        telpon_17_data = request.form["telpon_17"]
        email_17_data = request.form["email_17"]
        lahir_17_data = request.form["lahir_17"]
        session["nama_17_data"] = nama_17_data
        session["telpon_17_data"] = telpon_17_data
        session["email_17_data"] = email_17_data
        session["lahir_17_data"] = lahir_17_data

        nama_18_data = request.form["nama_18"]
        telpon_18_data = request.form["telpon_18"]
        email_18_data = request.form["email_18"]
        lahir_18_data = request.form["lahir_18"]
        session["nama_18_data"] = nama_18_data
        session["telpon_18_data"] = telpon_18_data
        session["email_18_data"] = email_18_data
        session["lahir_18_data"] = lahir_18_data

        nama_19_data = request.form["nama_19"]
        telpon_19_data = request.form["telpon_19"]
        email_19_data = request.form["email_19"]
        lahir_19_data = request.form["lahir_19"]
        session["nama_19_data"] = nama_19_data
        session["telpon_19_data"] = telpon_19_data
        session["email_19_data"] = email_19_data
        session["lahir_19_data"] = lahir_19_data

        nama_20_data = request.form["nama_20"]
        telpon_20_data = request.form["telpon_20"]
        email_20_data = request.form["email_20"]
        lahir_20_data = request.form["lahir_20"]
        session["nama_20_data"] = nama_20_data
        session["telpon_20_data"] = telpon_20_data
        session["email_20_data"] = email_20_data
        session["lahir_20_data"] = lahir_20_data

        inisialcabang_data = inisialcabang(cabang_data)
        biaya_data = biaya(cabang_data)
        kodepeserta_data = ""
        kodeunik_data = ""
        biayapeserta_data = ""
        verifikasi_data = "BELUM"

        print('berhasil')
        print(sekolah_data, user_data, cabang_data, suratketerangan_data, nama_1_data, telpon_1_data, email_1_data, lahir_1_data)
        global datapeserta
        datapeserta = peserta(sekolah_data, user_data, cabang_data, catur_kuota, film_kuota, basketputra_kuota, basketputri_kuota, band_kuota, dance_kuota, foto_kuota, debat_kuota, pidato_kuota, kosong_kuota, senjata_kuota, ganda_kuota, padus_kuota, design_kuota, suratketerangan_data, inisialcabang_data, biaya_data, kodepeserta_data, kodeunik_data, biayapeserta_data, nama_1_data, telpon_1_data, email_1_data, lahir_1_data, nama_2_data, telpon_2_data, email_2_data, lahir_2_data, nama_3_data, telpon_3_data, email_3_data, lahir_3_data, nama_4_data, telpon_4_data, email_4_data, lahir_4_data, nama_5_data, telpon_5_data, email_5_data, lahir_5_data,  nama_6_data, telpon_6_data, email_6_data, lahir_6_data, nama_7_data, telpon_7_data, email_7_data, lahir_7_data, nama_8_data, telpon_8_data, email_8_data, lahir_8_data, nama_9_data, telpon_9_data, email_9_data, lahir_9_data, nama_10_data, telpon_10_data, email_10_data, lahir_10_data, nama_11_data, telpon_11_data, email_11_data, lahir_11_data, nama_12_data, telpon_12_data, email_12_data, lahir_12_data, nama_13_data, telpon_13_data, email_13_data, lahir_13_data, nama_14_data, telpon_14_data, email_14_data, lahir_14_data, nama_15_data, telpon_15_data, email_15_data, lahir_15_data, nama_16_data, telpon_16_data, email_16_data, lahir_16_data, nama_17_data, telpon_17_data, email_17_data, lahir_17_data, nama_18_data, telpon_18_data, email_18_data, lahir_18_data, nama_19_data, telpon_19_data, email_19_data, lahir_19_data, nama_20_data, telpon_20_data, email_20_data, lahir_20_data, verifikasi_data)
        db.session.add(datapeserta)
        db.session.commit()

        print(datapeserta._id)
        tableid = datapeserta._id
        inisial = datapeserta.inisialcabang_data
        datapeserta.kodepeserta_data = kodepeserta(tableid, inisial)
        datapeserta.kodeunik_data = kodeunik(tableid)
        db.session.commit()
        datapeserta.biayapeserta_data = biayapeserta(datapeserta.biaya_data, datapeserta.kodeunik_data)

        db.session.commit()

        global numberid
        numberid = datapeserta._id

        return redirect (url_for('submit'))

    elif request.method == "GET":
        print ("get")
        catur_list = []
        film_list = []
        basketputra_list = []
        basketputri_list = []
        band_list = []
        dance_list = []
        foto_list = []
        debat_list = []
        pidato_list = []
        kosong_list = []
        senjata_list = []
        ganda_list = []
        padus_list = []
        design_list = []

        table = peserta.query.all()
        data = peserta.query.all()
        for data in table:
            catur_list.append(data.catur_kuota)
        for data in table:
            film_list.append(data.film_kuota)
        for data in table:
            basketputra_list.append(data.basketputra_kuota)
        for data in table:
            basketputri_list.append(data.basketputri_kuota)
        for data in table:
            band_list.append(data.band_kuota)
        for data in table:
            dance_list.append(data.dance_kuota)
        for data in table:
            foto_list.append(data.foto_kuota)
        for data in table:
            debat_list.append(data.debat_kuota)
        for data in table:
            pidato_list.append(data.pidato_kuota)
        for data in table:
            kosong_list.append(data.kosong_kuota)
        for data in table:
            senjata_list.append(data.senjata_kuota)
        for data in table:
            ganda_list.append(data.ganda_kuota)
        for data in table:
            padus_list.append(data.padus_kuota)
        for data in table:
            design_list.append(data.design_kuota)

        print("catur")
        print(sum(catur_list))

        catur_sisa = sisakuota(sum(catur_list), 40)
        film_sisa = sisakuota(sum(film_list), 30)
        basketputra_sisa = sisakuota(sum(basketputra_list), 40)
        basketputri_sisa = sisakuota(sum(basketputri_list), 40)
        band_sisa = sisakuota(sum(band_list), 30)
        dance_sisa = sisakuota(sum(dance_list), 30)
        foto_sisa = sisakuota(sum(foto_list), 30)
        debat_sisa = sisakuota(sum(debat_list), 16)
        pidato_sisa = sisakuota(sum(pidato_list), 40)
        kosong_sisa = sisakuota(sum(kosong_list), 40)
        senjata_sisa = sisakuota(sum(senjata_list), 40)
        ganda_sisa = sisakuota(sum(ganda_list), 40)
        padus_sisa = sisakuota(sum(padus_list), 40)
        design_sisa = sisakuota(sum(design_list), 40)

        print(catur_sisa)

        totalsisa = catur_sisa+film_sisa+basketputra_sisa+basketputri_sisa+band_sisa+dance_sisa+foto_sisa+debat_sisa+pidato_sisa+kosong_sisa+senjata_sisa+ganda_sisa+padus_sisa+design_sisa
        if request.args.get('password') == 'darrenalexandergantengsekali':
            return render_template('index.html', title='Pendaftaran', sisacatur = catur_sisa, sisafilm = film_sisa, sisabasketputra = basketputra_sisa, sisabasketputri = basketputri_sisa, sisaband = band_sisa, sisadance = dance_sisa, sisafoto = foto_sisa, sisadebat= debat_sisa, sisapidato = pidato_sisa, sisakosong = kosong_sisa, sisasenjata = senjata_sisa, sisaganda = ganda_sisa, sisapadus = padus_sisa, sisadesign = design_sisa)
        if time.time() < 1633167000:
            return render_template('closed.html')
        if time.time() >= 1633744800:
            return render_template('due.html')
        if totalsisa != 0 :
            return render_template('index.html', title='Pendaftaran', sisacatur = catur_sisa, sisafilm = film_sisa, sisabasketputra = basketputra_sisa, sisabasketputri = basketputri_sisa, sisaband = band_sisa, sisadance = dance_sisa, sisafoto = foto_sisa, sisadebat= debat_sisa, sisapidato = pidato_sisa, sisakosong = kosong_sisa, sisasenjata = senjata_sisa, sisaganda = ganda_sisa, sisapadus = padus_sisa, sisadesign = design_sisa)
        else :
            return render_template('full.html')

@app.route('/submitted', methods=['GET', 'POST'])
def submit():
    output = peserta.query.filter_by(_id=numberid).first()
    if output == None:
        return redirect(url_for('index'))
    else:
        biayaoutput = output.biayapeserta_data
        kodepesertaoutput = output.kodepeserta_data
        print(biayaoutput)
        return render_template('submission.html', biaya=biayaoutput, kodepeserta =kodepesertaoutput)

@app.route('/cekdata', methods = ["GET","POST"])
def cekdata():
    if request.method == "POST":
        print("start post")

        input = None
        input = request.form["input"]

        global nomorpeserta_input
        nomorpeserta_input = input

        print("datainput")

        return redirect(url_for('view'))

    elif request.method == "GET":
        print("get")
        return render_template('cekdata.html', title='Cek Data')
    
@app.route('/view', methods=['GET', 'POST'])
def view():
    if request.method == 'GET':
        print('loadedview')
        user = peserta.query.filter_by(kodepeserta_data = nomorpeserta_input).first()
        if user == None:
            return redirect (url_for('cekdata'))
        else:
            print(user.sekolah_data)
            return render_template('view.html', item=user)
    elif request.method == 'POST':
        return redirect(url_for('cekdata'))

@app.route('/admin', methods = ["GET","POST"])
def admin():
    if request.method == "POST":
        print("start post")

        pwd = None
        code = None
        pwd = request.form["pwd"]
        code = request.form["input"]
        verify = request.form["verifikasi"]

        user = peserta.query.filter_by(kodepeserta_data = code).first()

        print("passwordinput")

        print("password validation")
        if pwd != password:
            print("incorrect pwd")
            return redirect (url_for('admin'))
        elif user == None:
            return redirect (url_for('admin'))
        else:
            user.verifikasi_data = verify
            if verify == "SUDAH":
                if user.cabang_data == "chess" :
                    user.catur_kuota = 1
                elif user.cabang_data == "film" :
                    user.film_kuota = 1
                elif user.cabang_data == "basketputra" :
                    user.basketputra_kuota = 1
                elif user.cabang_data == "basketputri" :
                    user.basketputri_kuota = 1
                elif user.cabang_data == "band" :
                    user.band_kuota = 1
                elif user.cabang_data == "dance" :
                    user.dance_kuota = 1
                elif user.cabang_data == "foto" :
                    user.foto_kuota = 1
                elif user.cabang_data == "debat" :
                    user.debat_kuota = 1
                elif user.cabang_data == "pidato" :
                    user.pidato_kuota = 1
                elif user.cabang_data == "kosong" :
                    user.kosong_kuota = 1
                elif user.cabang_data == "senjata" :
                    user.senjata_kuota = 1
                elif user.cabang_data == "ganda" :
                    user.ganda_kuota = 1
                elif user.cabang_data == "padus" :
                    user.padus_kuota = 1
                elif user.cabang_data == "design" :
                    user.design_kuota = 1

            elif verify == "BELUM":
                if user.cabang_data == "chess" :
                    user.catur_kuota = 0
                elif user.cabang_data == "film" :
                    user.film_kuota = 0
                elif user.cabang_data == "basketputra" :
                    user.basketputra_kuota = 0
                elif user.cabang_data == "basketputri" :
                    user.basketputri_kuota = 0
                elif user.cabang_data == "band" :
                    user.band_kuota = 0
                elif user.cabang_data == "dance" :
                    user.dance_kuota = 0
                elif user.cabang_data == "foto" :
                    user.foto_kuota = 0
                elif user.cabang_data == "debat" :
                    user.debat_kuota = 0
                elif user.cabang_data == "pidato" :
                    user.pidato_kuota = 0
                elif user.cabang_data == "kosong" :
                    user.kosong_kuota = 0
                elif user.cabang_data == "senjata" :
                    user.senjata_kuota = 0
                elif user.cabang_data == "ganda" :
                    user.ganda_kuota = 0
                elif user.cabang_data == "padus" :
                    user.padus_kuota = 0
                elif user.cabang_data == "design" :
                    user.design_kuota = 0

            db.session.commit()
            return redirect (url_for('edited'))

    elif request.method == "GET":
        print("get")
        return render_template('admin.html', title='Admin')

@app.route('/edited', methods=['GET', 'POST'])
def edited():
    return render_template('edited.html')

@app.route('/team', methods=['GET'])
def team():
    return render_template('team.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/syarat', methods=['GET'])
def syarat():
    return render_template('sop.html')

@app.route('/pendaftaran', methods=['GET'])
def pendaftaran():
    return render_template('pendaftaran.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000, ssl_context=context)
    #
