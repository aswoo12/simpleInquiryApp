# simpleInquiryApp
Django Based Student Inquiry App implemented to demonstrate the use of custom users and django tags. The project uses Sqlite3 as the database.

Here's a table of the application's endpoints:

| URL Path                                 | Endpoint Name               | View                        |
| --------------------------------------- | --------------------------- | ---------------------------- |
| /academicrequest/new/                   | academicrequests-create     | AcademicRequestsCreateView   |
| /academicrequest/&lt;int:pk&gt;/update/ | academicrequests-update     | AcademicRequestsUpdateView   |
| /academicrequest/&lt;int:pk&gt;/delete/ | academicrequests-delete     | AcademicRequestsDeleteView   |
| /academicrequests/                      | academicrequests-list       | AcademicRequestsListView     |
| /administrativerequest/new/             | administrativerequests-create | AdministrativeRequestsCreateView |
| /administrativerequest/&lt;int:pk&gt;/update/ | administrativerequests-update | AdministrativeRequestsUpdateView |
| /administrativerequest/&lt;int:pk&gt;/delete/ | administrativerequests-delete | AdministrativeRequestsDeleteView |
| /administrativerequests/                | administrativerequests-list   | AdministrativeRequestsListView |
| /registration/                          | registration                | views.registration           |
| /base/                                 | base                        | views.base                   |
| /home/                                 | home                        | views.home                   |
| /login/                                | login                       | auth_views.LoginView         |
| /logout/                               | logout                      | auth_views.LogoutView        |

This table provides a mapping of the URL paths to their corresponding endpoint names and views within your Django application.
