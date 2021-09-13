from flask import render_template
from .import main


@main.app_errorhandler(404)
def app_errorhandler(error):
  '''
  Function to return error page
  '''

  return render_template('404.html')
