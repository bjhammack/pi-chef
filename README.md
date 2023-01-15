# Pi Chef


## Summary
Pi Chef is a simple flask webapp that takes recipes stored in a sqlite3 database and displays them in a simple, touchscreen friendly format to be used with a Raspberry Pi and its 7" touchscreen display as a "recipe kiosk" in the kitchen.

![website-example](/assets/images/recipes_example.png)


## Structure
All source code is stored in [src/pi_chef](/src/pi_chef/). Data is handled with [data_controller.py](/src/pi_chef/data_controller.py) and all data is stored in [recipes.db](/src/pi_chef/data/recipes.db). The webapp is launched from and maintained with [pi_chef_webapp.py](/src/pi_chef/pi_chef_webapp.py) and its assets are stored in [templates](/src/pi_chef/templates/) and [static](/src/pi_chef/static/) respectively.


## Workflow
Since this is meant to be a Raspberry Pi kiosk application, the application is meant to launch upon powering up of the Raspberry Pi. This can be achieved through configuring things on the Pi itself and then having this [bash script](/src/pi_chef/app.sh) get called as the final step. This script launches the webapp, then opens the pi's chromium web browser in "kiosk" mode, meaning no borders or menu bars are visible.

When the application is launched, data_controller.py is imported and is used to gather up all the recipes in recipes.db. These recipes are them passed the app and are rendered within the template using JavaScript.


## Future Iterations
This project is still a work in progress; several key features are still in the pipeline and need to be fully debugged and implemented.
- The ability to add new recipes via the application itself.
- The ability to edit and delete existing recipes.
- A more attractive recipe view. The current one is very barebones and tacky. <img src="/assets/images/recipe_example.png" width=200 height=200>
