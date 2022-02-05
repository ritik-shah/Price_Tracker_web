import requests
from flask import Flask, render_template, request, session, jsonify
from DBConnection import Db
from bs4 import BeautifulSoup
from flask_cors import CORS
app = Flask(__name__)
app.secret_key="6767"

CORS(app)

@app.route('/')
def login():
    return render_template('login.html')
@app.route('/loginpost',methods=['post'])
def loginpost():
    c=Db()
    uname=request.form['textfield']
    password=request.form['textfield2']
    qry="SELECT * FROM login WHERE username='"+uname+"' AND PASSWORD='"+password+"'"
    res=c.selectOne(qry)
    if res is not None :
        session['lid']=res['lid']
        session['username']=res['username']
        type=res['type']
        if type=="admin":
            return home()
        else:
            return "Unauthorised Access"
    else:
        return ("invalid username or password")

@app.route('/home')
def home():
    uname=session['username']
    uname=uname.upper()
    print(uname)

    return render_template('/Admin/index.html')




@app.route('/changepassword')
def changepassword():
    uname = session['username']
    uname = uname.upper()
    return render_template('Admin/changepassword.html', name=uname)
@app.route('/changepassword_post',methods=['post'])
def changepassword_post():
    z=Db()
    x=session['lid']
    old_password=request.form['textfield']
    new_password=request.form['textfield2']
    confirm_password=request.form['textfield3']
    qry = "SELECT * FROM login WHERE lid='"+str(x)+"'"
    res=z.selectOne(qry)
    if res['password']==old_password:
        qry="update  login set password= '"+new_password+"' where lid = '"+str(x)+"'"
        z.update(qry)
        return "ok"
    else:
        return "no"

@app.route('/viewregstd_users')
def viewregstd_users():
    uname = session['username']
    uname = uname.upper()
    d=Db()
    qry="SELECT * FROM users"
    res=d.select(qry)
    return render_template('Admin/viewregstd_users.html',data=res, name=uname)
@app.route('/viewregstd_post',methods=['post'])
def viewregstd_post():
    search=request.form['textfield']



@app.route('/view_complaints')
def view_complaints():
    uname = session['username']
    uname = uname.upper()
    d=Db()
    qry="SELECT users.*,complaint.* FROM users,complaint WHERE users.ulid=complaint.cuid ORDER by status DESC"
    res=d.select(qry)
    return render_template('Admin/view_complaints.html',data=res, name=uname)






@app.route('/hh',methods=['post'])
def view_complaints_post():
    d=Db()
    print("------------------------------------------")
    btn=request.form['submit']
    print(btn)
    if btn=="GO":
        from_date=request.form['ff']
        to_date=request.form['tt']
        qry="SELECT users.*,complaint.* FROM users,complaint WHERE users.ulid=complaint.cuid AND complaint.cdate BETWEEN '"+from_date+"' AND '"+to_date+"' ORDER by status DESC"
        res=d.select(qry)
        print(res)
        return render_template('Admin/view_complaints.html',data=res)
    else:
        status=request.form['select3']
        if status=="ALL":
            qry = "SELECT users.*,complaint.* FROM users,complaint WHERE users.ulid=complaint.cuid ORDER by status DESC"
            res = d.select(qry)
        else:
            qry = "SELECT users.*,complaint.* FROM users,complaint WHERE users.ulid=complaint.cuid AND complaint.STATUS= '"+status+"'"
            res=d.select(qry)
        return render_template('Admin/view_complaints.html', data=res)
@app.route('/send_replies/<a>')
def send_replies(a):
    uname = session['username']
    uname = uname.upper()
    session["cid"]=a
    z=Db()
    qry="SELECT * FROM complaint WHERE `cid`='"+a+"'"
    res=z.selectOne(qry)
    return render_template('Admin/send_replies.html',res=res, name=uname)


@app.route('/send_replies_post',methods=['post'])
def send_replies_post():
    z=Db()
    reply=request.form['comp_reply']
    qry="UPDATE complaint SET STATUS='DONE', reply='"+reply+"',rdate=NOW() where cid='"+session["cid"]+"'"
    z.update(qry)
    return "<script>alert('Replied Sccessfully');window.location='/view_complaints'</script>"

@app.route('/view_feedback')
def view_feedback():
    uname = session['username']
    uname = uname.upper()
    f=Db()
    qry="SELECT users.*,feedback.* FROM users,feedback WHERE users.ulid=feedback.fuid "
    res=f.select(qry)
    return render_template('Admin/view_feedback.html',data=res, name=uname)
@app.route('/view_feedbacks_post',methods=['post'])
def view_feedbacks_post():
    f=Db()
    from_date = request.form['textfield']
    to_date = request.form['textfield2']

    qry="SELECT users.*,feedback.* FROM users,feedback WHERE users.ulid=feedback.fuid AND feedback.fdate BETWEEN '"+from_date+"' AND '"+to_date+"'"
    res=f.select(qry)
    return render_template('Admin/view_feedback.html',data=res)



@app.route('/search')
def search():
    uname = session['username']
    uname = uname.upper()
    return render_template('Admin/search.html', name=uname)
@app.route('/search_post',methods=['post'])
def search_post():
    url=request.form['textfield']
    source=request.form['select']



@app.route('/forgot1')
def forgot1():
    return render_template('forgot1.html')
@app.route('/forgot1_post',methods=['post'])
def forgot1_post():
    email_id=request.form['textfield']



@app.route('/forgot2')
def forgot2():
    return render_template('forgot2.html')
@app.route('/forgot2_post',methods=['post'])
def forgot2_post():
    otp=request.form['textfield']



@app.route('/forgot3')
def forgot3():
    return render_template('forgot3.html')
@app.route('/forgot3_post',methods=['post'])
def forgot3_post():
    new_password=request.form['textfield']
    confirm_password=request.form['textfield2']




@app.route('/index')
def index():
    return render_template('Admin/index.html')

@app.route('/and_pr_scrap',methods=['post'])
def and_pr_scrap():
    URL=request.json["prurl"]
    if "flipkart" in URL:
        itemname,pricedata,imgdata=and_flipkart(URL)
        return  jsonify(status="ok",prname=itemname,prprice=pricedata,primg=imgdata)
    elif "amazon" in URL:

        itemname,pricedata,imgdata=and_amazon(URL)
        return jsonify(status="ok", prname=itemname, prprice=pricedata, primg=imgdata)
    else:
        return jsonify("Enter correct URL")

def and_flipkart(URL):



    r = requests.get(URL)
    soup = BeautifulSoup(r.content,'html.parser')

    bnamedata=soup.find('span',class_="G6XhRU")
    namedata=soup.find('span',class_="B_NuCI")
    # prname=bnamedata.text+namedata.text
    pricedata=soup.find('div',class_="_30jeq3 _16Jk6d")
    imgdata=soup.find('div',class_="_3kidJX")
    imgdata1=soup.find_all_next('div')
    # name = namedata[0].find('span', attrs={'class': 'B_NuCI'})
    n =soup.find_all('img', alt=True)
    if (bnamedata is not None):
        itemname=bnamedata+namedata
    else:
        itemname=namedata
    itemname=itemname.text
    pricedata=pricedata.text



    return itemname,pricedata,""


# @app.route("/aaaaa")
# def aaaa():
#     and_amazon()
#
#     print("firstchance")
#     and_amazon()
#     print("2chnace")
#     and_amazon()
#     print("3rd chance")
#     and_amazon()
#     print("4 th chance")
#
#     return "ok"

def and_amazon(URL):

    p=""
    from bs4 import BeautifulSoup
    import requests
    HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit / 537.36(KHTML, like Gecko)Chrome / 44.0.2403.157Safari / 537.36','Accept-Language': 'en-US, en;q=0.5'})
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, 'html.parser')

    pname= soup.find('span', id="productTitle")
    pname=pname.text
    print(pname)
    pricedata = soup.find('span', id="priceblock_ourprice")
    if(pricedata is not None):
        print(2,pricedata.text)
        p=pricedata.text
    else:
        pricedata=soup.find('span', id="priceblock_dealprice")
        if (pricedata is not None):
            print(3,pricedata.text)
            p=pricedata.text

        else:
            pricedata = soup.findAll('span', class_="a-price a-text-price a-size-medium apexPriceToPay")
            f=0
            for i in pricedata:
                a=i.findNext('span',class_="a-offscreen")

                f=f+1
                if a is not None:
                    print(a.text,"hi")
                    p = a.text
                    break
                else:
                    print("no")
                    continue


            # if(pricedata is not None):
            #     print(4,pricedata.text)
            else:
                pricedata = soup.find('input', id="twister-plus-price-data-price")
                if(pricedata is not None):
                    print(5,pricedata.text)
                    p = pricedata.text
                else:
                    pricedata=soup.find('span',class_="a-size-medium a-color-price priceBlockBuyingPriceString")
                    print(6,pricedata.text)
                    p = pricedata.text



    imgdata = soup.find('img', class_="a-dynamic-image a-stretch-horizontal")
    if(imgdata is not None):
        print(imgdata.attrs['data-old-hires'])
    else:
        imgdata=soup.find('img',id="landingImage")
        if(imgdata is not None):
            print(imgdata.attrs['data-a-dynamic-image'])

    print(pname,"h")
    # print(pricedata.text)
    # p=p.text
    # pricedata=pricedata.text

    return pname,p,"imgdata"

@app.route('/priceinsert/<pbid>')
def priceinsert(pbid):
    from bs4 import BeautifulSoup
    from DBConnection import Db

    c = Db()

    qry="SELECT pr_url FROM budget WHERE bid='"+pbid+"'"
    res=c.selectOne(qry)
    URL =res['pr_url']
    import requests
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "DNT": "1",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
    }
    r = requests.get(URL, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    f = soup.findAll("span", class_="a-offscreen")
    f = soup.findAll("span", class_="a-price a-text-price a-size-medium apexPriceToPay")
    price = ""
    for i in f:
        price = i.text

    if len(f) == 0:
        f = soup.findAll("span", class_="a-size-base a-color-price a-color-price")
        for i in f:
            price = i.text
    if len(f) == 0:
        f = soup.find("span", class_="a-price-whole")
        price = i.text
    print(price)
    qry = "INSERT INTO prevprice (pbid,pr_date,pr_amt,pr_time) values ('"+pbid+"',curdate(),'" + price + "',curtime())"
    res = c.insert(qry)
    return 'ok'






# -------------------------ANDROID---------------------------------------------------------------------------------





@app.route('/insertintobudget',methods=['post'])
def insertintobudget():
    prurl=request.json["prurl"]
    tarprice=request.json["tarprice"]
    prname=request.json["prname"]
    buid=request.json["buid"]
    c = Db()
    qry="INSERT INTO budget (`pr_url`,`tar_price`,`pr_name`,`buid`,`set_date`) VALUES ('"+prurl+"','"+tarprice+"','"+prname+"','"+buid+"',curdate())"
    res=c.insert(qry)
    return "ok"




@app.route('/viewmybudget',methods=['post'])
def viewmybudget():
    c=Db()
    buid=request.json["lid"]
    qry="SELECT * FROM budget where buid='"+buid+"'"
    res=c.select(qry)

    return jsonify(data=res)



@app.route('/deletemybudget',methods=['post'])
def deletemybudget():
    c=Db()
    bid=request.form["bid"]
    qry="DELETE * FROM budget where bid='"+bid+"'"
    c.delete(qry)
    return jsonify(status="ok")




@app.route('/regusers',methods=['post'])
def regusers():
    c=Db()
    fname = request.json["fname"]
    lname = request.json["lname"]
    phno = request.json["phno"]
    emailid = request.json["emailid"]
    dob = request.json["dob"]
    country = request.json["country"]
    prpic=request.json['img']

    import base64
    a = base64.b64decode(prpic)
    print(len(a))
    from datetime import datetime
    filename = str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day) + str(
        datetime.now().hour) + str(datetime.now().minute) + str(datetime.now().second) + str(
        datetime.now().microsecond) + ".jpg"
    with open("D:\\Price_Tracker\\static\\userimage\\" + filename, "wb") as fh:
        fh.write(a)
    cimg = "/static/userimage/" + filename

    pw=request.json["pw"]
    uname=fname+" "+lname
    qry1="INSERT INTO login(`username`,`password`,`type`) VALUES ('"+uname+"','"+pw+"','user')"
    id=c.insert(qry1)


    qry="INSERT INTO users (`fname`,`lname`,`phno`,`emailid`,`dob`,`country`,`pr_pic`,ulid,doj) VALUES ('"+fname+"','"+lname+"','"+phno+"','"+emailid+"','"+dob+"','"+country+"','"+cimg+"','"+str(id)+"',now())"
    c.insert(qry)
    return jsonify(status="ok")




@app.route('/editprofile',methods=['post'])
def editprofile():
    c = Db()
    fname = request.json["fname"]
    lname = request.json["lname"]
    phno = request.json["phno"]
    emailid = request.json["emailid"]
    dob = request.json["dob"]
    country = request.json["country"]
    prpic =request.json['img']
    uid=request.json["lid"]

    import base64
    a = base64.b64decode(prpic)
    print(len(a))
    from datetime import datetime
    filename = str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day) + str(
        datetime.now().hour) + str(datetime.now().minute) + str(datetime.now().second) + str(
        datetime.now().microsecond) + ".jpg"
    with open("D:\\Price_Tracker\\static\\userimage\\" + filename, "wb") as fh:
        fh.write(a)
    cimg = "/static/userimage/" + filename

    qry="UPDATE users set fname='"+fname+"',lname='"+lname+"',phno='"+phno+"',emailid='"+emailid+"',dob='"+dob+"',country='"+country+"',pr_pic='"+cimg+"' where ulid='"+uid+"'"
    print(qry)

    c.update(qry)
    return jsonify(status="ok")




@app.route('/viewmyprofile',methods=['post'])
def viewmyprofile():
    c=Db()
    ulid=request.json["lid"]
    qry="SELECT * FROM users WHERE ulid='"+ulid+"'"
    s=c.selectOne(qry)
    return jsonify(status="ok",fname=s['fname'],lname=s['lname'],phno=s['phno'],emailid=s['emailid'],dob=s['dob'],country=s['country'],prpic=s['pr_pic'],doj=s['doj'])




@app.route('/changepw',methods=['post'])
def changepw():
    c=Db()
    oldpw=request.json["oldpw"]
    newpw=request.json["newpw"]
    lid=request.json["lid"]
    qry="SELECT * FROM login WHERE lid='"+lid+"' AND password='"+oldpw+"'"
    res=c.selectOne(qry)
    if res is not None:
        qry="UPDATE login SET password='"+newpw+"' where lid='"+lid+"'"
        c.update(qry)
        return jsonify(status="ok")
    else:
        return jsonify(status="no")





@app.route('/forgotpw',methods=['post'])
def forgotpw():
    c=Db()
    emailid=request.json["emailid"]
    return jsonify(status="ok")




@app.route('/resetpw',methods=['post'])
def resetpw():
    c=Db()
    lid=request.json["lid"]
    newpw=request.json["newpw"]
    qry = "UPDATE login SET password='" + newpw + " where lid='" + lid + ""
    return jsonify(status="ok")




@app.route('/androidlogin',methods=['post'])
def androidlogin():
    c=Db()
    username=request.json["username"]
    password=request.json["password"]
    qry="SELECT * FROM login WHERE username='"+username+"' AND password='"+password+"' AND type='user'"
    print(qry)
    res=c.selectOne(qry)
    if res is not None:
        return jsonify(status="ok",lid= res['lid'])
    else:
        return jsonify(status="no")




@app.route('/viewprevprice',methods=['post'])
def viewprevprice():
    c=Db()
    lid=request.json['lid']
    qry="SELECT * FROM prevprice where pbid='"+lid+"'"
    res=c.select(qry)
    print(res)
    return jsonify(status="ok",data=res)




@app.route('/and_complaint',methods=['post'])
def and_complaint():
    c=Db()
    lid=request.json["lid"]
    complaint=request.json['complaint']
    img=request.json['img']
    # print(img)
    # print(len(img))
    import base64
    a=base64.b64decode(img)
    print(len(a))
    from datetime import  datetime
    filename= str(datetime.now().year)+ str(datetime.now().month)+str(datetime.now().day)+str(datetime.now().hour)+str(datetime.now().minute)+str(datetime.now().second)+str(datetime.now().microsecond)+".jpg"
    with open("D:\\Price_Tracker\\static\\complaintimage\\"+filename, "wb") as fh:
        fh.write(a)
    cimg="/static/complaintimage/"+filename

    qry="INSERT into complaint (u_complaint,c_img,cuid,cdate) VALUES ('"+complaint+"','"+cimg+"','"+lid+"',now())"
    c.insert(qry)
    return jsonify(status="ok")

@app.route('/and_viewcomplaint',methods=['post'])
def and_viewcomplaint():
    c=Db();
    lid=request.json['lid']
    qry="SELECT `cid`,`u_complaint`,`c_img`,`reply`,`status`, DATE_FORMAT(`cdate`, '%m-%d-%Y') AS 'cdate',DATE_FORMAT(`rdate`, '%m-%d-%Y') AS 'rdate'  FROM complaint WHERE cuid='"+lid+"' ORDER BY cdate DESC"
    print(qry)
    comp=c.select(qry)
    return jsonify(status="ok",data=comp)


@app.route('/and_feedback',methods=['post'])
def and_feedback():
    c=Db()
    lid=request.json['lid']
    feedback=request.json['feedback']

    print(lid)
    print(feedback)
    qry="INSERT into feedback (feedback,fuid) VALUES ('"+feedback+"','"+lid+"')"
    c.insert(qry)
    return jsonify(status="ok")

@app.route('/and_viewfeedback',methods=['post'])
def and_viewfeedback():
    c=Db()
    lid=request.json['lid']
    qry="SELECT feedback,DATE_FORMAT(`fdate`, '%m-%d-%Y') AS 'fdate' from feedback where fuid='"+lid+"'"
    feed=c.select(qry)
    return jsonify(status="ok",data=feed)


@app.route('/ml',methods=['get'])
def ml():
    c=Db()

    qry="SELECT pr_date,pr_amt,pr_time from prevprice where pbid='2'"
    res=c.select(qry)
    ldate=[]
    lprice=[]
    for i in res:
        ldate.append(i['pr_date'])
        lprice.append(i['pr_amt'])
    print(lprice,"*******")
    # com_lis=[]
    # los_list=[]
    lol_list=[]
    for i in range(len(lprice)):
        if len(lol_list)==0:
            a=int(lprice[i])
            b=int(lprice[i])
            # com_lis.append([a,b])
            # los_list.append(0)
            lol_list.append([a,b,0])
        else:
            a = int(lprice[i-1])
            b = int(lprice[i])
            loss=b-a
            # los_list.append(loss)
            # com_lis.append([a,b])
            lol_list.append([a, b, loss])
    print(lol_list, "***************************")
    # print(los_list,"--------------------------------------")
    # print(com_lis,"***************************")
    return "ok"


@app.route('/prediction',methods=['post'])
def prediction():
    c=Db()
    uid=request.json["uid"]
    qry="SELECT * FROM budget where buid='"+uid+"'"
    res=c.select(qry)
    for i in res:
        k = []
        f=i['bid']
        qry="SELECT pr_amt from prevprice where pbid='"+f+"' ORDER BY pr_date ASC"
        res=c.select(qry)
        for i in res :
            k.append(i['pr_amt'])
    return jsonify(data=res)



if __name__ == '__main__':
    app.run(port=8000,debug=True,host='0.0.0.0')
