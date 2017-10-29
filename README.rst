cs101ab-team1
===============

Project goal: ML chatbot that can parse a conversation and suggest humorous GIF
responses

Installation
------------

#. Download the project::

     $ git clone git@github.com:mosbasik/cs101ab-team1.git
     $ cd cs101ab-team1/

#. Install Python 3.6 virtual environment and project dependencies::

     $ python3 -m venv .env      # create the virtual environment
     $ source .env/bin/activate  # activate the virtual environment
     $ pip install pip-tools     # install library to help with package managment
     $ pip-compile               # generate requirements.txt from requirements.in
     $ pip-sync                  # install everything in requirements.txt

   You activate the venv by running ``source .env/bin/activate`` and deactivate
   the venv by running ``deactivate``.

   **Note**: the virtual environment folder is platform-specific and should not
   be committed to the repo (``.env`` is in our ``.gitignore``).  You can put
   your venv anywhere your system you want, or use something like
   virtualenvwrapper_ to handle these decisions for you.

.. _virtualenvwrapper: https://virtualenvwrapper.readthedocs.io/en/latest/
