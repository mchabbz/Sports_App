# Sports Top Players App

A Flask web application for managing and displaying top player records from three major sports leagues: MLB, NBA, and NFL.

The application uses CSV files as the original data source, loads that data into a SQLite database, and displays the records through dynamic Flask pages using Flask-SQLAlchemy ORM queries.

---

## 1. Project Overview

The Sports Top Players App models a real-world sports statistics dashboard. It allows users to view, search, filter, sort, create, update, and delete player records from MLB, NBA, and NFL.

The application was built in five phases:

1. Proposal and Database
2. Displaying Data with ORM
3. Advanced Querying and Relationships
4. Altering Data: Create, Update, Delete
5. User Authentication, Authorization, and Application Refinement

The app is organized using an MVC-style structure:

| Layer | Project Files |
|---|---|
| Models | `mlb.py`, `nba.py`, `nfl.py`, `sport.py`, `user.py` |
| Views | HTML templates inside the `templates` folders |
| Controllers | `*_controller.py` files |
| Managers | `*_manager.py` files |
| Routes | `*_routes.py` files |

---

## 2. CSV Data Source

The project uses three CSV files:

```text
mlb.csv
nba.csv
nfl.csv
```

Each file uses the same universal column structure so that the application can process all three sports consistently.

The CSV columns are:

```text
Game_ID
League
Teams
Players
Metric_1
Metric_2
Metric_3
Metric_4
```

Although the columns are universal, the meaning of each metric changes depending on the sport.

---

## 3. Universal CSV Column Meaning

| Universal Column | What it represents in MLB | What it represents in NBA | What it represents in NFL |
|---|---|---|---|
| `Game_ID` | `MLB-2024-001` | `NBA-2024-001` | `NFL-2024-001` |
| `League` | MLB | NBA | NFL |
| `Teams` | Baseball team name | Basketball team name | Football team name |
| `Players` | MLB player name | NBA player name | NFL player name |
| `Metric_1` Scoring | Home Runs | 3-Pointers Made | Touchdowns |
| `Metric_2` Possession | At Bats | Field Goal Attempts | Offensive Snaps |
| `Metric_3` Accuracy | Batting Average | Field Goal % | Completion % |
| `Metric_4` Defense | Strikeouts, Pitcher | Blocks | Sacks |

---

## 4. What Each CSV Column Does in the App

### `Game_ID`

The `Game_ID` column identifies the data batch or game record.

Examples:

```text
MLB-2024-001
NBA-2024-001
NFL-2024-001
```

It helps separate records by league and dataset.

---

### `League`

The `League` column identifies which league the record belongs to.

Possible values:

```text
MLB
NBA
NFL
```

This is used by the app to separate baseball, basketball, and football records.

---

### `Teams`

The `Teams` column stores the name of the team.

Examples:

```text
New York Yankees
Los Angeles Lakers
Kansas City Chiefs
```

The app uses this field for:

```text
Team display
Team filtering
Team search
Sorting by team
```

---

### `Players`

The `Players` column stores the player name.

Examples:

```text
Alex Yankee NY1
Jordan Laker LA2
Taylor Chief KC3
```

The app uses this field for:

```text
Player display
Player search
Sorting by player name
Player detail pages
```

---

### `Metric_1`

`Metric_1` represents a scoring-related statistic.

| League | Meaning |
|---|---|
| MLB | Home Runs |
| NBA | 3-Pointers Made |
| NFL | Touchdowns |

---

### `Metric_2`

`Metric_2` represents a possession or attempt-related statistic.

| League | Meaning |
|---|---|
| MLB | At Bats |
| NBA | Field Goal Attempts |
| NFL | Offensive Snaps |

---

### `Metric_3`

`Metric_3` represents an accuracy-related statistic.

| League | Meaning |
|---|---|
| MLB | Batting Average |
| NBA | Field Goal Percentage |
| NFL | Completion Percentage |

---

### `Metric_4`

`Metric_4` represents a defensive statistic.

| League | Meaning |
|---|---|
| MLB | Strikeouts, Pitcher |
| NBA | Blocks |
| NFL | Sacks |

---

## 5. Database Design

The application uses SQLite as the database.

The database file is created here:

```text
instance/sports_app.db
```

The main database tables are:

```text
sports
mlb_players
nba_players
nfl_players
users
```

---

## 6. Main Entities

### Sport

The `Sport` model represents the general sports category.

Examples:

```text
Baseball
Basketball
Football
```

Each sport has a league value:

```text
MLB
NBA
NFL
```

The `Sport` table connects to the player tables through relationships.

---

### MLBPlayer

Represents one MLB player record.

Important fields:

```text
id
game_id
league
team
player
metric_1
metric_2
metric_3
metric_4
sport_id
created_by_user_id
```

---

### NBAPlayer

Represents one NBA player record.

Important fields:

```text
id
game_id
league
team
player
metric_1
metric_2
metric_3
metric_4
sport_id
created_by_user_id
```

---

### NFLPlayer

Represents one NFL player record.

Important fields:

```text
id
game_id
league
team
player
metric_1
metric_2
metric_3
metric_4
sport_id
created_by_user_id
```

---

### User

Represents a registered user account.

Important fields:

```text
id
username
email
password_hash
is_admin
```

Users can register, log in, and create player records.

---

## 7. Important Note About the ID Column

The `ID` column shown on the website is not a sports ranking.

It is the database primary key.

For example:

```text
/mlb/12
/mlb/12/edit
/mlb/12/delete
```

The number `12` means the database record with ID 12.

It is used by Flask and SQLite to find, view, edit, and delete a specific row.

It does not mean the player is ranked number 12.

---

## 8. Project Features

The application includes the following major features:

```text
View MLB player records
View NBA player records
View NFL player records
Search within MLB only
Search within NBA only
Search within NFL only
Search globally across all leagues
Filter by team
Sort by player, team, and metrics
View player detail pages
Create new records
Edit existing records
Delete records
Register a user account
Log in and log out
View user profile
Track records created by users
Protect create/edit/delete routes
Support admin and regular user authorization
Switch between light and dark mode
Display custom error pages
```

---

## 9. Search Features

The app has two types of search.

### League-Specific Search

These pages search only one sport section:

```text
/mlb/search
/nba/search
/nfl/search
```

For example:

```text
/mlb/search
```

only searches MLB records.

Users can search by:

```text
All properties
Game ID
League
Team
Player
```

---

### Global Search

The home page has a global search feature.

The global search route is:

```text
/search
```

It searches across:

```text
MLB
NBA
NFL
```

This is useful when the user wants to find a player, team, league, or game ID without choosing a specific sport first.

---

## 10. Filtering and Sorting

Each league list page supports filtering and sorting.

Example league pages:

```text
/mlb/
/nba/
/nfl/
```

Users can filter by team.

Users can sort by:

```text
Player name
Team name
Metric 1
Metric 2
Metric 3
Metric 4
```

The sorting and filtering are done using Flask-SQLAlchemy ORM queries.

---

## 11. Create, Update, and Delete Features

Logged-in users can create new player records.

Protected routes include:

```text
/mlb/create
/mlb/<id>/edit
/mlb/<id>/delete

/nba/create
/nba/<id>/edit
/nba/<id>/delete

/nfl/create
/nfl/<id>/edit
/nfl/<id>/delete
```

The app validates form data before saving it.

Validation checks include:

```text
Required fields cannot be empty
Metric 1 must be a whole number
Metric 2 must be a whole number
Metric 3 must be a decimal number
Metric 4 must be a whole number
```

---

## 12. Authentication

The application includes user registration and login.

Authentication routes:

```text
/auth/register
/auth/login
/auth/logout
```

A registered user can:

```text
Log in
Log out
Create player records
View profile information
View records they created
```

Passwords are not stored directly. The application stores password hashes.

---

## 13. Authorization Rules

The app uses authorization rules to protect sensitive features.

### Public Visitors

Public visitors can:

```text
View records
Search records
Filter records
Sort records
View player details
```

Public visitors cannot:

```text
Create records
Edit records
Delete records
```

---

### Regular Users

Regular users can:

```text
Create records
Edit records they created
Delete records they created
View their profile
```

Regular users cannot edit or delete CSV-loaded records unless they are admin.

---

### Admin User

The first registered user becomes the admin.

The admin can:

```text
Create records
Edit any record
Delete any record
Manage CSV-loaded records
Manage records created by other users
```

This is important because the original CSV records do not belong to any registered user.

---

## 14. User Profile

The profile page is available at:

```text
/user/profile
```

The profile page shows:

```text
Username
Email
User role
Number of MLB records created
Number of NBA records created
Number of NFL records created
Total records created
Tables of records created by the user
```

---

## 15. Light and Dark Mode

The app includes a light and dark theme switcher.

The button is located in the header.

The selected theme is saved in the browser using `localStorage`, so the theme remains selected after refreshing the page.

Files involved:

```text
app/static/css/main.css
app/static/js/main.js
app/templates/base.html
```

---

## 16. Error Handling

The application includes custom error pages:

```text
401 Unauthorized
404 Page Not Found
500 Server Error
```

Files:

```text
app/templates/errors/401.html
app/templates/errors/404.html
app/templates/errors/500.html
```

These pages improve the user experience when something goes wrong.

---

## 17. Folder Structure

Main project structure:

```text
PROJECT ROOT/
database.py
extensions.py
helper.py
main.py
load_csv_data.py
requirements.txt

app/
    __init__.py

    auth/
        auth_controller.py
        auth_manager.py
        auth_routes.py
        templates/auth/
            login.html
            register.html

    user/
        user.py
        user_controller.py
        user_manager.py
        user_routes.py
        templates/user/
            index.html
            profile.html

    sport/
        sport.py
        mlb.csv
        nba.csv
        nfl.csv

    mlb/
        mlb.py
        mlb_controller.py
        mlb_manager.py
        mlb_routes.py
        templates/mlb/
            index.html
            search.html
            detail.html
            create.html
            edit.html
            delete.html

    nba/
        nba.py
        nba_controller.py
        nba_manager.py
        nba_routes.py
        templates/nba/
            index.html
            search.html
            detail.html
            create.html
            edit.html
            delete.html

    nfl/
        nfl.py
        nfl_controller.py
        nfl_manager.py
        nfl_routes.py
        templates/nfl/
            index.html
            search.html
            detail.html
            create.html
            edit.html
            delete.html

    templates/
        base.html
        index.html
        search.html
        errors/
            401.html
            404.html
            500.html

    static/
        css/main.css
        js/main.js
```

---

## 18. How to Run the Project

### Step 1: Create and activate virtual environment

PyCharm usually creates the virtual environment automatically.

If using terminal:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

---

### Step 2: Install dependencies

```bash
pip install flask flask-sqlalchemy flask-login python-dotenv
```

Or install from requirements:

```bash
pip install -r requirements.txt
```

---

### Step 3: Load the CSV data

Make sure the CSV files are inside:

```text
app/sport/
```

Then run:

```bash
python load_csv_data.py
```

This creates the database and loads the CSV records.

---

### Step 4: Run the Flask app

```bash
python main.py
```

Open the browser at:

```text
http://127.0.0.1:5000/
```

---

## 19. Important Reset Instructions

If the database structure changes, reset the database.

To reset:

```text
1. Stop the Flask server.
2. Delete instance/sports_app.db.
3. Run python load_csv_data.py.
4. Run python main.py.
5. Register a new user.
```

The first registered user becomes admin.

---

## 20. Main Routes

| Route | Purpose |
|---|---|
| `/` | Home page |
| `/search` | Global search |
| `/mlb/` | MLB list page |
| `/mlb/search` | MLB-only search |
| `/mlb/create` | Create MLB player |
| `/mlb/<id>` | MLB detail page |
| `/mlb/<id>/edit` | Edit MLB player |
| `/mlb/<id>/delete` | Delete MLB player |
| `/nba/` | NBA list page |
| `/nba/search` | NBA-only search |
| `/nba/create` | Create NBA player |
| `/nba/<id>` | NBA detail page |
| `/nba/<id>/edit` | Edit NBA player |
| `/nba/<id>/delete` | Delete NBA player |
| `/nfl/` | NFL list page |
| `/nfl/search` | NFL-only search |
| `/nfl/create` | Create NFL player |
| `/nfl/<id>` | NFL detail page |
| `/nfl/<id>/edit` | Edit NFL player |
| `/nfl/<id>/delete` | Delete NFL player |
| `/auth/register` | Register user |
| `/auth/login` | Login user |
| `/auth/logout` | Logout user |
| `/user/profile` | User profile |

---

## 21. Technologies Used

```text
Python
Flask
Flask-SQLAlchemy
Flask-Login
SQLite
HTML
CSS
JavaScript
Jinja Templates
CSV
PyCharm
```

---

## 22. Phase Completion Summary

### Phase 1: Proposal and Database

Completed.

The app identifies the real-world system, defines the purpose, identifies entities, designs the database schema, creates SQLAlchemy models, and loads CSV data.

---

### Phase 2: Displaying Data with ORM

Completed.

The app uses MVC organization, connects to the database, performs ORM queries, and displays dynamic list pages.

---

### Phase 3: Advanced Querying and Relationships

Completed.

The app includes filtering, sorting, league-specific search, global search, pattern-based queries, and related sport data through relationships.

---

### Phase 4: Altering Data

Completed.

The app includes create, update, delete, detail pages, forms, validation, flash messages, and error handling.

---

### Phase 5: Authentication, Authorization, and Refinement

Completed.

The app includes registration, login, logout, protected routes, authorization rules, user profile, user-record association, custom error pages, improved interface, and light/dark mode.

---

## 23. Project Purpose Statement

The purpose of this project is to demonstrate how a Flask application can manage real-world sports data using a relational database, ORM queries, dynamic templates, user authentication, and protected data modification features.

The app begins with CSV data, transforms it into database records, and provides users with an interactive web interface for exploring and managing sports player statistics.

---

## 24. Notes for Future Improvements

Possible future improvements include:

```text
Pagination for large datasets
Better metric labels on each league page
Charts and visual summaries
Admin dashboard
User account editing
CSV upload through the website
Export search results
More detailed team pages
More detailed sport pages
```

---

## 25. Author

Created as a Flask course project for managing and displaying sports player records from MLB, NBA, and NFL datasets.
