# Customization and Extension of Django-admin user interface.
This app was written in Django.

## Tasks
- Create a superuser with credentials: Username: root; Password: password
- Extend the Django admin dashboard page to show user metrics, example is the number of users created over the past 24hours, past week and past month. (You can add additional metrics to the admin dashboard at your discretion).
- Add a custom action button to the users list page that enables staff to set a user to active or inactive with the click of a button. (You can add additional useful functionalities to the admin users list page at your discretion).
- Add a functionality page that allows staff to send an email to all existing users. You can/should use Django's console.EmailBackend to send the emails.
- Please don't forget to add your db.sqlite3 file to your repo.
- Host your code on Heroku or any PAAS of your choice

## Notes
- The app is hosted on Heroku ==> https://savesttasks.herokuapp.com/
- All actions are carried out in the admin section of the app
- The admin url is https://savesttasks.herokuapp.com/admin/
- You'd be required to login with the superuser username and password
- You Can perform the following actions in the admin dashboard
  - View User Metrics
  - Add User
  - Update User
  - Filter Users & Search for user
  - Enable / Disable User by making them active/inactive
  - Make a user a staff and vice versa
  - Sending mails to all active users
