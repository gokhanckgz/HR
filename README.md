Feelincs HR
-----------
Kurulum için

1)Pip kurulumu

2)Virtualenv kurulumu

3)Django kurulumu

Kullanım için (hata almamak için adım adım uygulamak gerekebilir)

1)Postgresql veritabanı oluşturma

2)Veritabanını senkronize etmek

#KURULUM
-------

#Pip kurulumu

<code>sudo apt-get install python</code>

<code>sudo apt-get install python-pip</code>

#Virtualenv kurulumu

<code>pip install virtualenv</code>

<code>cd /path/to/virtualenv</code>

<code>virtualenv virtual_env_name</code>

#Virtualenv Ortamına Geçiş

<code>cd /path/to/virtualenv/virtual_env_name</code>

<code>source bin/activate</code>

#Django kurulumu

<code>pip install django</code>

#Postgresql kurulumu

<code>sudo apt-get install postgresql postgresql-contrib</code> Postgresql temel paketleri.

<code>sudo apt-get install python-psycopg2 libpq-dev</code> Psycopg2 modülünü kullanmak için gerekli paketler.

#Gerekli modüllerin kurulumu

LDAP modülü
----------
<code>pip install python-ldap</code>

PSYCOPG2 modülü
---------
<code>pip install django-auth-ldap</code> 

<code>pip install psycopg2</code>

Crispy-Forms modülü
---------
<code>pip install django-crispy-forms</code>

Pillow Modülü
---------
<code>pip install pillow</code> Image dosyalarının görüntülenmesi için gerekli.

#KULLANIM
-------

#POSTGRESQL DATABASE 
----------
<code>sudo -u postgres psql</code>

<code>alter user postgres password 'kullanici_sifresi';</code>  Bu şifre settings.py dosyasında belirtilen şifre olmalı.

<code>\q</code> çıkış yapmak için.

<code>sudo nano /etc/postgresql/9.1/main/pg_hba.conf</code>


    <code>local     all     all     peer</code> 
    
    bu satırı
    
    <code>local     all     all     md5</code>
    
    olarak değiştirip.
    
<code>sudo service postgresql restart</code> komutunu gir.

<code>CREATE DATABASE database_ismi</code> Settings.py dosyasında belirtilen database ismi ile aynı olmalı.

#POSTGRESQL SENKRONİZE ETMEK
----------

<code>cd /path/to/project_folder</code>

<code>python2 manage.py makemigrations</code>

<code>python2 manage.py migrate</code>

#SUPERUSER OLUŞTURMA
----------

<code>cd /path/to/project_folder</code>

<code>python2 manage.py createsuperuser</code>

#ÇALIŞTIRMA
----------

<code>cd /path/to/project_folder</code>

<code>python2 manage.py runserver</code>
