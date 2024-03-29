# kojitechsapiserver
This Project create Fast maintainable API's for kojitechs

## Test Locally 

```sh
- Create a Virtual Environment python -m venv venv
- Activate Virtual Environment source venv/bin/activate
- Install Requirements Package pip install -r requirements.txt
- Migrate Database python manage.py migrate
- Create Super User python manage.py createsuperuser
- Finally Run The Project python manage.py runserver
```

# Kojitechs API

<h3>🔗 Final Project Links (Arranged According To Usage)</h3>
<br>

<b>1. Admin Access</b>
<ul>
    <li>Admin Section: http://127.0.0.1:8000/dashboard/</li>
</ul>
<br>

<b>2. Accounts</b>
<ul>
    <li>Registration: http://127.0.0.1:8000/api/account/register/</li>
    <li>Login: http://127.0.0.1:8000/api/account/login/</li>
    <li>Logout: http://127.0.0.1:8000/api/account/logout/</li>
</ul>
<br>

<b>3. See all courses kojitechs offers</b>
<ul>
    <li>Create Element & Access List: http://127.0.0.1:8000/api/courses/</li>
    <li>Access, Update & Destroy Individual Element: http://127.0.0.1:8000/api/cources/&lt;int:&gt;/</li>

</ul>
<br>

<b>4. Students List</b>
<ul>
    <li>Create & Access List: http://127.0.0.1:8000/api/students/</li>
    <li>Access, Update & Destroy Individual Element: http://127.0.0.1:8000/api/student/&lt;int:students&gt;/</li>
</ul>
<br>

<b>5. Reviews</b>
<ul>
    <li>Create Review For Specific Movie: http://127.0.0.1:8000/api/watch/&lt;int:movie_id&gt;/reviews/create/</li>
    <li>List Of All Reviews For Specific Movie: http://127.0.0.1:8000/api/watch/&lt;int:movie_id&gt;/reviews/</li>
    <li>Access, Update & Destroy Individual Review: http://127.0.0.1:8000/api/watch/reviews/&lt;int:review_id&gt;/</li>
</ul>
<br>

<b>6. User Review</b>
<ul>
    <li>Access All Reviews For Specific User: http://127.0.0.1:8000/api/watch/user-reviews/?username=example</li>
</ul>
<br>