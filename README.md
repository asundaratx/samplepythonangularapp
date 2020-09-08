The project has a Python Flask Backend exposing an api to store your favourite repo's.
The frontend shows your current favorite repo's and allows you to add and remove repo's
To do:
Store the favorites to a Mongo Datastore
To setup required installs:
  conda create --name <your env>
  conda activate <your env>
  conda install -c conda-forge marshmallow
  conda install -c conda-forge pymongo
  conda install -c conda-forge flask
  conda install -c conda-forge flask-cors

To run the backend:
  cd to <projectfolder>
  set FLASK_APP=<projectfolder/app/http/api/endpoints.py>
  python -m flask run --port 4433

  when done:
  conda deactivate <your env>

To run the frontend:
  ng serve --open --port 8080
# WebApp

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 10.1.0.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/master/README.md).
