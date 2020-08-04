from flask import render_template, url_for, flash, redirect
from flaskblog import app,db,bcrypt
from flaskblog.forms import RegistrationForm, LoginForm ,UserProfileForm
from flaskblog.models import User,Usage,Performanceval
from flask_login import login_user,current_user,logout_user,login_required
import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import csv
from flaskblog.best_performance import Content
TOPIC_DICT=Content()
print(TOPIC_DICT)

k=[]
posts = [

    {

        'author': 'Corey Schafer',

        'title': 'Blog Post 1',

        'content': 'First post content',

        'date_posted': 'April 20, 2018'

    },

    {

        'author': 'Jane Doe',

        'title': 'Blog Post 2',

        'content': 'Second post content',

        'date_posted': 'April 21, 2018'

    }

]


    
    




@app.route("/")

@app.route("/home")

def home():

    return render_template('home.html', posts=posts)





@app.route("/about")

def about():

    return render_template('about.html', title='About')





@app.route("/register", methods=['GET', 'POST'])

def register():

    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_pasword = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hashed_pasword)
        usage = Usage(username=form.username.data,nosessions=0)
        db.session.add(user)
        db.session.add(usage)
        db.session.commit()
        flash(f'Your account was created Successfully', 'success')

        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)





@app.route("/login", methods=['GET', 'POST'])

def login():

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            usage=Usage.query.filter_by(username=user.username).first()
            if usage.nosessions==0:
                usage.nosessions=1
                db.session.commit()
                return redirect(url_for('us_profile'))
            else:
                pv=Performanceval.query.filter_by(username=user.username).first()
                if pv.performance == 'MP':
                    return redirect(url_for('mp_home'))
                if pv.performance == 'LP':
                    return redirect(url_for('lp_home'))
                if pv.performance == 'BP':
                    return redirect(url_for('bp_home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/us_prof", methods=['GET', 'POST'])

def us_profile():

    form = UserProfileForm()
    if form.validate_on_submit():
        df=pd.read_csv("AMML_dataset.csv")
        avg_10=df.iloc[:,2]
        avg_12=df.iloc[:,3]
        avg_collper=df.iloc[:,7]
        avg_english1=df.iloc[:,9]
        avg_english2=df.iloc[:,10]
        avg_english3=df.iloc[:,11]
        avg_english4=df.iloc[:,12]
        avg_quantative1=df.iloc[:,13]
        avg_quantative2=df.iloc[:,14]
        avg_quantative3=df.iloc[:,15]
        avg_quantative4=df.iloc[:,16]
        avg_domain1=df.iloc[:,17]
        avg_domain2=df.iloc[:,18]
        avg_domain3=df.iloc[:,19]
        avg_domain4=df.iloc[:,20]
        avg_analyt1=df.iloc[:,21]
        avg_analyt2=df.iloc[:,22]
        avg_analyt3=df.iloc[:,23]
        #avg_10=df["10th percentage"].mean()
        #computing averages
        avg_10=avg_10.mean()
        avg_12=avg_12.mean()
        avg_collper=avg_collper.mean()
        avg_english1=avg_english1.mean()
        avg_english2=avg_english2.mean()
        avg_english3=avg_english3.mean()
        avg_english4=avg_english4.mean()
        avg_quantative1=avg_quantative1.mean()
        avg_quantative2=avg_quantative2.mean()
        avg_quantative3=avg_quantative3.mean()
        avg_quantative4=avg_quantative4.mean()

        avg_domain1=avg_domain1.mean()
        avg_domain2=avg_domain2.mean()
        avg_domain3=avg_domain3.mean()
        avg_domain4=avg_domain4.mean()
        avg_analyt1=avg_analyt1.mean()
        avg_analyt2=avg_analyt2.mean()
        avg_analyt3=avg_analyt3.mean()

        
        print(avg_10)
        print(avg_12)
        print(avg_collper)
        print(avg_english1)
        print(avg_english2)
        print(avg_english3)
        print(avg_english4)
        print(avg_quantative1)
        print(avg_quantative2)
        print(avg_quantative3)
        print(avg_quantative4)
        
      
        
      
        l=[]
        nans = df.index[(df['Performance'] != "MP") & (df['Performance'] != "LP") & (df['Performance'] != "BP")]
        df.drop(nans, inplace = True)
        df2 = pd.DataFrame({"Gender":[form.Gender.data],"State (Location)":[form.State.data]," 10th percentage":[form.Marks_10th.data]," 12th percentage":[form.Marks_12th.data],"Difference":[form.Year_12th.data-form.Year_10th.data],"Degree of study":[form.Degree.data],"Specialization in study":[form.Specialisation.data]," College percentage":[form.College_Percent.data],"Age":[form.Age.data-6]," English 1":[form.English_Test_1.data],"English 2":[form.English_Test_2.data],"English 3":[form.English_Test_3.data],"English 4":[form.English_Test_4.data],"Quantitative Ability 1":[form.Quants_1.data],"Quantitative Ability 2":[form.Quants_2.data],"Quantitative Ability 3":[form.Quants_3.data],"Quantitative Ability 4":[form.Quants_4.data],"Domain Skills 1":[form.Domain_1.data],"Domain Skills 2":[form.Domain_2.data],"Domain Test 3":[form.Domain_3.data],"Domain Test 4":[form.Domain_4.data],"Analytical Skills 1":[form.Analytics_1.data],"Analytical Skills 2":[form.Analytics_2.data],"Analytical Skills 3":[form.Analytics_3.data]})
        print(form.Marks_10th.data)
        if(form.Marks_10th.data<avg_10):
            l.append('You need to improve on your 10th subject')
        if(form.Marks_12th.data<avg_12):
            l.append('You need to work on your 12th syllabus')
        if(form.College_Percent.data<avg_collper):
            l.append('Just go to your college syallbus')
        if(form.English_Test_1.data<avg_english1):
            l.append('Work on your preliminary english')
        
            
        print(l)
        k.extend(l)
            

            
        y=df['Performance']
        df = df.drop(columns=['Performance'])
        df = df.append(df2)
        X=df.values
        imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
        imputer = imputer.fit(X[:, 7:])
        X[:, 7:] = imputer.transform(X[:, 7:])
        labelencoder_X = LabelEncoder()
        X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
        X[:, 1] = labelencoder_X.fit_transform(X[:, 1])
        X[:, 5] = labelencoder_X.fit_transform(X[:, 5])
        X[:, 6] = labelencoder_X.fit_transform(X[:, 6])
        onehotencoder = OneHotEncoder(categorical_features = [0, 1, 5, 6])
        X = onehotencoder.fit_transform(X).toarray()
        sc_X = StandardScaler()
        X = sc_X.fit_transform(X)
        print(X[0])
        print(X[642])
        A=X[642]
        X=X[0:642]
        print(A)
        B=[A]
        print(B)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 42)
        classifier = SVC(C=1.0,kernel = 'rbf',gamma=0.1,random_state = 0)
        classifier.fit(X_train, y_train)
        pvalue=classifier.predict(B)
        pvalue=pvalue[0]
        print(pvalue)   
        list_csv=[current_user.username,form.Gender.data,form.State.data,form.Marks_10th.data,form.Marks_12th.data,form.Year_12th.data-form.Year_10th.data,form.Degree.data,form.Specialisation.data,form.College_Percent.data,form.Age.data,form.English_Test_1.data,form.English_Test_2.data,form.English_Test_3.data,form.English_Test_4.data,form.Quants_1.data,form.Quants_2.data,form.Quants_3.data,form.Quants_4.data,form.Domain_1.data,form.Domain_2.data,form.Domain_3.data,form.Domain_4.data,form.Analytics_1.data,form.Analytics_2.data,form.Analytics_3.data]
        with open('user_values.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(list_csv)
        csvFile.close()        
        pv = Performanceval(username=current_user.username,performance=pvalue)
        db.session.add(pv)
        db.session.commit()
        list_csv=[current_user.username,form.Gender.data,form.State.data,form.Marks_10th.data,form.Marks_12th.data,form.Year_12th.data-form.Year_10th.data,form.Degree.data,form.Specialisation.data,form.College_Percent.data,form.Age.data,form.English_Test_1.data,form.English_Test_2.data,form.English_Test_3.data,form.English_Test_4.data,form.Quants_1.data,form.Quants_2.data,form.Quants_3.data,form.Quants_4.data,form.Domain_1.data,form.Domain_2.data,form.Domain_3.data,form.Domain_4.data,form.Analytics_1.data,form.Analytics_2.data,form.Analytics_3.data]
        with open('user_values.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(list_csv)
        csvFile.close()
        if pvalue=='MP':
            return redirect(url_for('mp_home'))
        if pvalue=='BP':
            return redirect(url_for('bp_home'))
        if pvalue=='LP':
            return redirect(url_for('lp_home'))
    return render_template('user_profile.html', title='User Profile', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

@app.route("/bp_home")
@login_required
def bp_home():
    return render_template('bp_home.html',title='User Homepage',TOPIC_DICT=TOPIC_DICT,k=k)

@app.route("/lp_home")
@login_required
def lp_home():
    return render_template('lp_home.html',title='User Homepage',TOPIC_DICT=TOPIC_DICT)
          
@app.route("/mp_home")
@login_required
def mp_home():
    return render_template('mp_home.html',title='User Homepage',TOPIC_DICT=TOPIC_DICT)
