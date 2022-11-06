# SQL - More queries
# SQL - Introduction

## Description

[MySQL](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04) is an open-source database management system, commonly installed as part of the popular LAMP (Linux, Apache, MySQL, PHP/Python/Perl) stack. It implements the relational model and uses Structured Query Language (better known as SQL) to manage its data.
---

### Requirements

- Allowed editors: vi, vim, emacs
- All files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25).
- All SQL queries have a comment just before (i.e. syntax above).
- All files start with a comment describing the task.
---

### File Description

- **0-privileges.sql** - file contains script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on server (in `localhost`).
- **1-create_user.sql** - file contains script that creates MySQL server user `user_0d_1`` with all privileges.
- **2-create_read_user.sql** - file contains script that creates the database `hbtn_0d_2` and the user `user_0d_2` (only `SELECT` privileges).
- **3-force_name.sql** - file contains script that creates the table `force_name` on MySQL server with specifics.
- **4-never_empty.sql** - file contains script that creates the table `id_not_null` on MySQL server with specifics.
- **5-unique_id.sql** - file contains script that creates the table `unique_id` on MySQL server.
- **6-states.sql** - file contains script creates database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on MySQL server.
- **7-cities.sql** - file contains script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.
- **8-cities_of_california_subquery.sql** - contains script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.
- **9-cities_by_state_join.sql** - contains a script that lists all cities contained in the database `hbtn_0d_usa`.
- **10-genre_id_by_show.sql** - contains script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked.
- **11-genre_id_all_shows.sql** - contains script that lists all shows contained in the database `hbtn_0d_tvshows` with specifics..
- **12-no_genre.sql** - file contains script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked.
- **13-count_shows_by_genre.sql** - file contains script that lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each.
- **14-my_genres.sql** - contains script that uses the `hbtn_0d_tvshows` database to lists all genres of the show Dexter.
- **15-comedy_only.sql** - file contains script that lists all Comedy shows in the database `hbtn_0d_tvshows` with specifics.
- **16-shows_by_genre.sql** - contains script that lists all shows, and all genres linked to that show, from the database ``hbtn_0d_tvshows``.



---

## Author

Written by [Denisse Landau](https://www.linkedin.com/in/denisselandau/ "Denisse Landau").