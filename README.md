# What to do next:  
### Jé's Assistant:
  -- The way as Artist and Album Views are working using render is not the better Django way, let's analyze if we rewrite all the views or if redirect can help us
  
## Read - diary(On Pause):  
###   Login  
   -- create modal or error message to fields  
   -- create validation to secure same password  
   -- create db and tables to record users data  
   -- create user session  
   -- create redirect view properly to login  

## To curious people around here
This is a very new portfolio, right now I'm trying to work on it adding more exercises projects, but it's happening in a slow pace for some reasons like, I'm studying a lot about many IT subjects and sometimes I question my own sanity that make me chose this as profession area...

Well hope your sanity is alright too, although i doubt it a little since you're reading this...
regards, Ana  

```
my_portfolio
├─ ana_portfolio
│  ├─ ana_portfolio
│  │  ├─ asgi.py
│  │  ├─ README.md
│  │  ├─ settings.py
│  │  ├─ urls.py
│  │  ├─ wsgi.py
│  │  └─ __init__.py
│  ├─ blog
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ static
│  │  │  └─ blog
│  │  │     └─ style_base.css
│  │  ├─ templates
│  │  │  └─ blog
│  │  │     ├─ 404.html
│  │  │     ├─ base.html
│  │  │     ├─ index.html
│  │  │     ├─ list_posts.html
│  │  │     ├─ post.html
│  │  │     └─ upload.html
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  └─ __init__.py
│  ├─ build.sh
│  ├─ je_assistant
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ forms.py
│  │  ├─ migrations
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ services
│  │  │  └─ spotify.py
│  │  ├─ static
│  │  │  └─ je_assistant
│  │  │     ├─ css
│  │  │     │  └─ base.css
│  │  │     ├─ dog_pc.png
│  │  │     ├─ images
│  │  │     ├─ js
│  │  │     └─ logo_with_dog.png
│  │  ├─ templates
│  │  │  └─ je_assistant
│  │  │     ├─ album_info.html
│  │  │     ├─ artists_list_albums.html
│  │  │     ├─ base_je_assistant.html
│  │  │     └─ index.html
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  └─ __init__.py
│  ├─ manage.py
│  ├─ morse_translator
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ forms
│  │  │  └─ translate_form.py
│  │  ├─ migrations
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ static
│  │  │  └─ morse_translator
│  │  │     ├─ css
│  │  │     │  └─ style.css
│  │  │     └─ js
│  │  │        └─ index.js
│  │  ├─ templates
│  │  │  └─ morse_translator
│  │  │     └─ index.html
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  └─ __init__.py
│  ├─ portfolio
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ forms
│  │  │  └─ contact_form.py
│  │  ├─ migrations
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ static
│  │  │  └─ portfolio
│  │  │     ├─ css
│  │  │     │  ├─ style.css
│  │  │     │  └─ style_2.css
│  │  │     ├─ cvs
│  │  │     │  ├─ cv- Ana Lemos - dev-en.pdf
│  │  │     │  ├─ cv- Ana Lemos - en_v1.pdf
│  │  │     │  ├─ cv- Ana Lemos - pt-br.pdf
│  │  │     │  ├─ cv_analemos-en.pdf
│  │  │     │  └─ QA_DEV
│  │  │     │     └─ Ana Lemos_pt.pdf
│  │  │     ├─ img
│  │  │     │  ├─ blog_thumb.jpg
│  │  │     │  ├─ char_base_ajustada.gif
│  │  │     │  ├─ char_sem_ruido.gif
│  │  │     │  ├─ char_working.gif
│  │  │     │  ├─ favicon_io.zip
│  │  │     │  ├─ github-logo.png
│  │  │     │  ├─ img_autoral_ana_lemos.jpf
│  │  │     │  ├─ img_autoral_ana_lemos.jpg
│  │  │     │  ├─ img_autoral_ana_lemos_progressive.jpg
│  │  │     │  ├─ linkedIn.svg
│  │  │     │  ├─ message.svg
│  │  │     │  ├─ morse_thumb.jpg
│  │  │     │  ├─ new_blush.gif
│  │  │     │  ├─ thumb_je.jpg
│  │  │     │  └─ thumb_page.jpg
│  │  │     └─ js
│  │  │        ├─ cv.js
│  │  │        ├─ language.js
│  │  │        ├─ navBar.js
│  │  │        └─ printThis
│  │  │           ├─ assets
│  │  │           │  ├─ css
│  │  │           │  │  ├─ normalize.css
│  │  │           │  │  └─ skeleton.css
│  │  │           │  └─ images
│  │  │           │     ├─ cat1.jpg
│  │  │           │     ├─ cat2.jpg
│  │  │           │     ├─ cat3.jpg
│  │  │           │     └─ print.png
│  │  │           ├─ bower.json
│  │  │           ├─ changelog.txt
│  │  │           ├─ CODE_OF_CONDUCT.md
│  │  │           ├─ composer.json
│  │  │           ├─ index.html
│  │  │           ├─ LICENSE
│  │  │           ├─ package-lock.json
│  │  │           ├─ package.json
│  │  │           ├─ printThis.d.ts
│  │  │           ├─ printThis.jquery.json
│  │  │           ├─ printThis.js
│  │  │           └─ README.md
│  │  ├─ templates
│  │  │  └─ portfolio
│  │  │     ├─ 404.html
│  │  │     ├─ base_portfolio.html
│  │  │     ├─ contact.html
│  │  │     ├─ contact_mail.html
│  │  │     ├─ includes
│  │  │     │  └─ nav_buttons.html
│  │  │     ├─ index.html
│  │  │     ├─ projects.html
│  │  │     ├─ resume.html
│  │  │     ├─ skills.html
│  │  │     └─ thanks_msg.html
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  └─ __init__.py
│  ├─ reading_diary
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ forms
│  │  │  ├─ login.py
│  │  │  └─ search_books.py
│  │  ├─ google_books.py
│  │  ├─ migrations
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ static
│  │  │  └─ reading_diary
│  │  │     ├─ css
│  │  │     │  ├─ buttons.css
│  │  │     │  ├─ form.css
│  │  │     │  └─ style.css
│  │  │     ├─ img
│  │  │     │  ├─ amarelo_frufru.png
│  │  │     │  ├─ areia.png
│  │  │     │  ├─ avocado.png
│  │  │     │  ├─ bkg_sereneAqua.jpg
│  │  │     │  ├─ border2.png
│  │  │     │  ├─ border_books.png
│  │  │     │  ├─ frufru.png
│  │  │     │  ├─ frufru_flip.png
│  │  │     │  ├─ logo.png
│  │  │     │  ├─ logo.psd
│  │  │     │  ├─ logo_rasberry_smoothy.png
│  │  │     │  ├─ organic_frufru.psd
│  │  │     │  ├─ rasberry.png
│  │  │     │  ├─ rasberry_frufru.png
│  │  │     │  └─ sereneAqua_frufru.png
│  │  │     └─ js
│  │  │        └─ login.js
│  │  ├─ templates
│  │  │  └─ reading_diary
│  │  │     ├─ base_template.html
│  │  │     └─ index.html
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  └─ __init__.py
│  └─ requirements.txt
└─ README.md

```