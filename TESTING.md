# TasteBuds - Testing

![TasteBuds Banner](documentation/readme/banner.png)

[Visit TasteBuds Here](https://tastebuds-project3-ab3740a15628.herokuapp.com/recipes/)

---

Testing was an ongoing process throughout the development of this project. From the early stages of building functionality to the final design refinements, a range of tools and techniques were used to ensure the application performs as expected.

Google Chrome Developer Tools were used extensively to test layout responsiveness, debug issues, and inspect elements across different screen sizes. Manual testing was also carried out on various devices to ensure the site functions smoothly on desktop, tablet, and mobile.

Automated tools such as Lighthouse and WAVE were used to assess accessibility, performance, and best practices, helping to improve the overall user experience.

---
## Validation Testing

### HTML

### HTML Validation

HTML was validated using the [W3C Markup Validation Service](https://validator.w3.org/). As the project is built using Django, which uses a templating language within HTML files, I validated the HTML by inspecting the fully rendered page in the browser (using "View Page Source") and copying that output into the validator. This ensured that the actual output served to users was compliant with HTML standards.

| Page | Result | Evidence |
| :--- | :--- | :---: |
| Home Page | Pass| [Home Page Validation](documentation/testing/validation/html/Home%20-%20w3Vali.png) |
| Recipe Details Page | Pass | [Recipe Details Page Validation](documentation/testing/validation/html/Recipe-details-w3Vali.png) |
| Add Recipe Page | Pass | [Add Recipe Page Page Validation](documentation/testing/validation/html/Add-Recipe-w3Vali.png) |
| Recipe Filter Page | Pass | [Recipe Filter Page Validation](documentation/testing/validation/html/Recipe-Filter-w3Vali.png) |
| Profile Page | Pass | [Profile Page Validation](documentation/testing/validation/html/Profile-page-w3Vali.png)|
| Login Page| Pass | [Login Page Validation](documentation/testing/validation/html/Login-w3Vali.png) |

### CSS

[W3C](https://validator.w3.org/) was used to validate the CSS.

| File | Result | Evidence |
| :--- | :--- | :---: |
| static/style.css | Pass | [static/style.css validation](documentation/testing/validation/css/stylecss-w3Vali.png) |

### JavaScript

[JS Hint](https://jshint.com/) was used to validate the JavaScript.

| File | Result | Evidence |
| :--- | :--- | :---: |
| recipes/base | Pass | [stripe-elements.js](documentation/testing/validation/js/jshint-base.png) |
| recipes/add-recipes | Pass | [stripe-elements.js](documentation/testing/validation/js/jshint-addrecipe.png) |
| recipes/edit-recipes | Pass | [stripe-elements.js](documentation/testing/validation/js/jshint-%20editrecipe.png) |
| users/profile | Pass | [stripe-elements.js](documentation/testing/validation/js/jshint-profile.png) |

### Python

[Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python.

| File | Result | Evidence |
| :--- | :--- | :---: |
| my_project/settings.py | Pass | [settings.py validation](documentation/testing/validation/python/project%20-%20Settings.png) |
| my_project/urls.py | Pass | [urls.py validation](documentation/testing/validation/python/project%20-%20urls.png) |
| **RECIPES** |
| recipes/apps.py | Pass | [apps.py validation](documentation/testing/validation/python/recipes%20-%20apps.png) |
| recipes/context-processor.py | Pass | [context-processor.py validation](documentation/testing/validation/python/recipes%20-%20context%20processor.png) |
| recipes/db.py | Pass | [db.py validation](documentation/testing/validation/python/recipes%20-%20db.png) |
| recipes/forms.py | Pass | [forms.py validation](documentation/testing/validation/python/recipes-forms.png) |
| recipes/models.py | Pass | [models.py validation](documentation/testing/validation/python/recipes-models.png) |
| recipes/urls.py | Pass | [urls.py validation](documentation/testing/validation/python/recipes%20-%20urls.png) |
| recipes/views.py | Pass | [views.py validation](documentation/testing/validation/python/recipes%20-%20views.png) |
| **REVIEWS** |
| reviews/apps.py | Pass | [apps.py validation](documentation/testing/validation/python/reviews%20-%20apps.png) |
| reviews/forms.py | Pass | [forms.py validation](documentation/testing/validation/python/reviews%20-%20forms.png) |
| reviews/models.py | Pass | [models.py validation](documentation/testing/validation/python/reviews%20-%20models.png) |
| reviews/urls.py | Pass | [urls.py validation](documentation/testing/validation/python/reviews%20-%20url.png) |
| reviews/views.py | Pass | [views.py validation](documentation/testing/validation/python/reviews%20-%20views.png) |
| **USERS** |
| users/admin.py | Pass | [admin.py validation](documentation/testing/validation/python/users%20-%20admin.png) |
| users/apps.py | Pass | [apps.py validation](documentation/testing/validation/python/users%20-%20apps.png) |
| users/forms.py | Pass | [forms.py validation](documentation/testing/validation/python/users%20-%20forms.png) |
| users/models.py | Pass | [models.py validation](documentation/testing/validation/python/users%20-%20models.png) |
| users/urls.py | Pass | [urls.py validation](documentation/testing/validation/python/users%20-%20urls.png) |
| users/views.py | Pass | [views.py validation](documentation/testing/validation/python/users%20-%20views.png) |

### Lighthouse

I used Google's Lighthouse tool to evaluate the site's performance, accessibility, best practices, and SEO.

#### Desktop Results

| Page | Result |
| :--- | :--- |
| Home Page | [Home Desktop Lighthouse Testing](documentation/testing/lighthouse/home-desktop-lh.png) |
| Recipe Detail Page | [Recipe Detail Desktop Lighthouse Testing](documentation/testing/lighthouse/recipedetail-desktop-lh.png) |
| Add Recipe Page | [Add Recipe Desktop Lighthouse Testing](documentation/testing/lighthouse/addrecipe-desktop-lh.png) |
| Edit Recipe Page | [Edit Recipe Desktop Lighthouse Testing](documentation/testing/lighthouse/editrecipe-desktop-lh.png) |
| Filter Recipe Page | [Filter Recipe Desktop Lighthouse Testing](documentation/testing/lighthouse/filterrecipe-desktop-lh.png) |
| Profile Page | [Profile Desktop Lighthouse Testing](documentation/testing/lighthouse/profile-desktop-lh.png) |
| Login Page | [Login Desktop Lighthouse Testing](documentation/testing/lighthouse/login-desktop-lh.png) |
| Register Page | [Register Desktop Lighthouse Testing](documentation/testing/lighthouse/register-desktop-lh.png) |

#### Mobile Results

| Page | Result |
| :--- | :--- |
| Home Page | [Home Mobile Lighthouse Testing](documentation/testing/lighthouse/home-mobile-lh.png) |
| Recipe Detail Page | [Recipe Detail Mobile Lighthouse Testing](documentation/testing/lighthouse/recipedetail-mobile-lh.png) |
| Add Recipe Page | [Add Recipe Mobile Lighthouse Testing](documentation/testing/lighthouse/addrecipe-mobile-lh.png) |
| Edit Recipe Page | [Edit Recipe Mobile Lighthouse Testing](documentation/testing/lighthouse/editrecipe-mobile-lh.png) |
| Filter Recipe Page | [Filter Recipe Mobile Lighthouse Testing](documentation/testing/lighthouse/filterrecipe-mobile-lh.png) |
| Profile Page | [Profile Mobile Lighthouse Testing](documentation/testing/lighthouse/profile-mobile-lh.png) |
| Login Page | [Login Mobile Lighthouse Testing](documentation/testing/lighthouse/login-mobile-lh.png) |
| Register Page | [Register Mobile Lighthouse Testing](documentation/testing/lighthouse/register-mobile-lh.png) |

## Manual Testing

### Testing User Stories

### Testing User Stories

| User Story ID | As a/an | I want to be able to ... | So that I can... | How is this achieved? | Evidence |
| :--- | :--- | :--- | :--- | :--- | :---: |
| 1 | Guest | Browse a list of all recipes | Explore what’s available without signing up | The homepage lists all recipes using Django views and templates to render entries from the database. | [List of Recipes](documentation/testing/user-stories/all-recipes-us.png) |
| 2 | Guest | View full details of a recipe | Decide if I want to try making it | Each recipe links to a detail view with full information including ingredients, instructions, and images. | [Full Recipe](documentation/testing/user-stories/detials-of-recipe-us.png) |
| 3 | Guest | Search for and filter recipes by keyword or category | Find exactly what I’m in the mood to cook | A category filter use Django querysets to return filtered results. | [Filtered Recipes](documentation/testing/user-stories/filterby-us.png) |
| 4 | Guest | Sign up for an account | Save and contribute my own recipes | A registration page using Django’s `UserCreationForm` allows users to create an account. | [Reigster Page](documentation/testing/user-stories/register-us.png) |
| 5 | User | Log in and log out | Access my personal content securely | Django’s authentication system manages login/logout and sessions securely. | [Log In/Out Buttons](documentation/testing/user-stories/login-out-us.png) |
| 6 | User | Create and submit a new recipe | Share my cooking ideas with the community | A recipe form linked to the user model allows recipe creation and saves data to the database. | [Add Recipe Page](documentation/testing/user-stories/add-recipe-us.png) |
| 7 | User | Edit or delete my own recipes | Keep my content up to date or remove it | Recipes created by the logged-in user include edit/delete buttons, handled via update/delete views. | [Edit and Delete Button](documentation/testing/user-stories/edit-delete-us.png) |
| 8 | User | Like a recipe | Show appreciation and bookmark favorites | A like button toggles a like model linked to the user and recipe using JavaScript and Django views. | [Like a Recipe Button](documentation/testing/user-stories/like-recipe-us.png) |
| 9 | User | View a dashboard of my own recipes | Manage my contributions in one place | A user dashboard filters and displays only the recipes created by the logged-in user. | [My Recipes](documentation/testing/user-stories//myrecipes-us.png) |
| 10 | User | Upload images to my recipes | Make my recipe posts visually appealing | Recipe forms include an image upload field. | [Add Image to Recipe](documentation/testing/user-stories/upload-image-us.png) |
| 11 | User | Manage my personal bio and profile info | Customize my profile for others to see | Profile edit view allows users to update their bio and information using a `UserProfile` model. | [Profile Page](documentation/testing/user-stories/mybio-us.png) |
| 12 | User | Comment on recipes | Share feedback or ask questions about recipes | Comment form below each recipe saves user comments. | [Comment Section](documentation/testing/user-stories/comments-us.png) |
| 13 | Admin | Access the Django admin panel | Manage backend tasks and oversee site activity | Django’s admin interface is enabled and accessible only to superusers. | [Admin Page](documentation/testing/user-stories/Adminsite-us.png) |
| 14 | Admin | Delete inappropriate or flagged content | Keep the platform safe and welcoming | Admin panel allows moderators to delete any content as needed. | [Edit and Delete Button](documentation/testing/user-stories/admin-edit-delete-us.png) |
| 15 | All | View the site on mobile/tablet devices | Use the app seamlessly on any screen | The site is responsive using CSS media queries. | [Mobile Friendly View](documentation/testing/user-stories/mobileview-us.png) |

### Full Testing

Full testing was performed on the following devices:

* Desktop
  * 34 inch ultrawide Monitor
* Laptop:
  * Macbook Pro 2024 14 inch Screen
* Tablet:
  * iPad Air Pro
* Mobile:
  * iPhone 16 
  * iPhone 14 Pro Max

Testing was also performed using the following browsers:

* Chrome
* FireFox
* Safari

Additional testing was carried out by friends and family on a variety of devices and screens.

### Features Testing Table

| **NAVBAR** |
| Feature | Expected Functionality | Test Action | Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| Logo Button | Directs to the home page | Clicked logo | Taken to home page | Pass |
| Home Button | Directs to the home page | Clicked Home | Taken to home page | Pass |
| Recipes Dropdown | Displays category and cuisine filters | Hovered over/Clicked Recipes | Dropdown displayed with filter options | Pass |
| Category/Cuisine Buttons | Filters recipes by chosen category or cuisine | Clicked a filter option | Recipes filtered by selected category/cuisine | Pass |
| Add Recipe Button (Navbar) | Directs to Add Recipe page | Clicked Add Recipe | Taken to Add Recipe form | Pass |
| Profile Button | Directs to profile page | Clicked Profile | Taken to user profile page | Pass |
| Log in Button | Directs to login page | Clicked Log in | Taken to login form | Pass |

---

| **RECIPES LIST PAGE** |
| Feature | Expected Functionality | Test Action | Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| Add Recipe Button | Directs to Add Recipe page | Clicked Add Recipe | Taken to recipe submission form | Pass |
| Recipe Card | Directs to selected recipe detail page | Clicked a recipe card | Taken to detailed recipe page | Pass |

---

| **RECIPE DETAILS PAGE** |
| Feature | Expected Functionality | Test Action | Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| Like Button | Adds a like to the recipe | Clicked like | Like count increased | Pass |
| Post Comment | Submits a comment on the recipe | Entered text and clicked Post | Comment displayed below recipe | Pass |
| Edit Recipe Button | Directs to edit page for that recipe | Clicked Edit | Taken to edit form | Pass |
| Delete Button | Deletes the recipe completely | Clicked Delete and confirmed | Recipe removed from site | Pass |
| Back to Recipes Button | Returns to recipe list page | Clicked Back | Taken to home/recipes list | Pass |

---

| **ADD RECIPE PAGE** |
| Feature | Expected Functionality | Test Action | Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| Add Ingredient Button | Adds new ingredient input field | Clicked Add Ingredient | New input field appears | Pass |
| Add Recipe Button | Posts the new recipe to the site | Filled form and clicked Post | Recipe added to site | Pass |
| Back to Recipes Button | Returns to home page | Clicked Back | Taken to home page | Pass |

---

| **PROFILE PAGE** |
| Feature | Expected Functionality | Test Action | Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| Edit Bio Button | Allows editing of user bio or image | Clicked Edit | Text field/image upload available | Pass |

---

| **LOG IN PAGE** |
| Feature | Expected Functionality | Test Action | Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| Log In Button | Authenticates and logs user in | Entered credentials and clicked Log In | User logged in and redirected | Pass |
| Register Here Button | Directs to registration page | Clicked Register Here | Taken to registration form | Pass |

---

| **REGISTER PAGE** |
| Feature | Expected Functionality | Test Action | Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| Register Button | Creates a new user account | Filled form and clicked Register | Account created and user logged in | Pass |
| Log In Button | Directs to login page | Clicked Log In | Taken to login form | Pass |

## Bugs

### Solved Bugs

| No | Bug | How I solved the issue |
|:--:|:-----|:------------------------|
| 1 | TemplateDoesNotExist error when trying to render a page | Checked the template path in the view and ensured the template file was correctly named and placed in the appropriate app's `templates` folder. |
| 2 | Static files not loading in development | Added `django.contrib.staticfiles` to `INSTALLED_APPS`, ensured `{% load static %}` was used in templates, and that `STATICFILES_DIRS` was correctly configured. |
| 3 | Form not submitting or saving data | Verified that the form was using the POST method, included `{% csrf_token %}` in the template, and checked that `form.is_valid()` was being called in the view. |
| 4 | Image upload not working | Configured Cloudinary by installing `django-cloudinary-storage`, adding it to `INSTALLED_APPS`, setting up the Cloudinary API keys in environment variables, and updating `DEFAULT_FILE_STORAGE` in settings. Also ensured the form used `enctype="multipart/form-data"`. |
| 5 | Page redirects not working after form submission | Used `redirect()` properly in views after `form.save()` to avoid resubmitting the form on page refresh. |
| 6 | User cannot edit or delete someone else's recipe | Added logic in the view to ensure only the owner of the recipe can access edit/delete functions (`if request.user == recipe.author`). |
| 7 | Login form not authenticating user | Confirmed `authenticate()` and `login()` functions were used properly in the view, and that the username and password matched an existing user. |
| 8 | Comments not appearing after posting | Ensured the comment was being saved to the database and that the template loop for displaying comments was correctly written. |
| 9 | Like button not updating count dynamically | Added JavaScript to send an asynchronous request and update the count without reloading the page. |
| 10 | CSRF token missing or incorrect error | Made sure `{% csrf_token %}` was included in all forms and that requests included the token in headers. |
| 11 | URLs for recipe detail pages not working | Double-checked the URL pattern with the correct slug or ID and confirmed the view used the correct lookup (e.g., `get_object_or_404(Recipe`). |

### Known Bugs

| No | Bug | Evidence |
|:--- | :--- | :---: |