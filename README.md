# Music Forum (MusMate)

It's django project for music lovers that want get in touch with each-other. Create playlists, find friends and just share your thoughts on music.


## Check it out!

[Music Forum deployed to Render](https://musmate.onrender.com/)
provided account(
login: user
password: user12345
)
## Installation

Python3 must be already installed

```shell
git clone https://github.com/pnasonov/mus-mate
cd mus-mate
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

## Features
* at home page not authorized visitor see amount of all songs, playlists, posts of forum, but authorized see own statistic
* every logged in user has own profile page, with his username, first-last names, about me info and email or instagram name; user can edit his profile page; username is used as page slug
* posts pages have 2 layouts, all posts and my posts. user can see paginated pages, with post info and open each to see detailed view; post pages have search by title form, button create post; for not logged in users all posts page allowed, but my posts is not
* post detailed view shows title, create date, full text of post, owner, comments; owner's name is link to owner's profile, page has buttons to edit or delete post only for his owner, also there is comment section where only logged in users can comment; page is available to visit also for unauthenticated users
* playlists pages have 2 layouts, all playlists and my playlists. user can see paginated pages, with playlist shorted view up to 5 songs; playlist pages have search by name form, button create playlist where user create playlist only with own songs; for not logged in users all playlists page allowed, but my playlists is not
* playlist detailed view shows name, create date, full numerated song list, owner, songs amount; owner's name is link to owner's profile, page has buttons to edit or delete playlist only for his owner; page is available to visit also for unauthenticated users.
* songs page is available only for logged in users, it shows only their songs and allow to create, update, delete them;there is a search form that allow to search by artist; it is useful for user to set up songs that will be added to playlist
