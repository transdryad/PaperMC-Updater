Usage
=====
.. note::

    **These docs are under construction.**

.. _install:

Installation
------------

To use PaperMC-Updater, simply install via pip:

.. code-block:: console

   $ pip install papermc-updater

Creating the Server
-------------------

To create a server for the first time, navigate to the desired location and run:

.. code-block:: console

   $ pmcu create

You will be asked to pick a minecraft version:

.. code-block:: console

    Creating the server...
    Querying version list from PaperMC...
    Current Version list for PaperMC:
    ['1.8.8', '1.9.4', '1.10.2', '1.11.2', '1.12', '1.12.1', '1.12.2', '1.13-pre7', '1.13', '1.13.1', '1.13.2', '1.14', '1.14.1', '1.14.2', '1.14.3', '1.14.4', '1.15', '1.15.1', '1.15.2', '1.16.1', '1.16.2', '1.16.3', '1.16.4', '1.16.5', '1.17', '1.17.1', '1.18', '1.18.1', '1.18.2', '1.19', '1.19.1', '1.19.2', '1.19.3', '1.19.4', '1.20', '1.20.1', '1.20.2', '1.20.4', '1.20.5', '1.20.6', '1.21', '1.21.1', '1.21.3', '1.21.4']
    Choose a version:

Simply type the version you wish to install, typically the latest one, and hit enter.
You will next be asked for how much RAM/memory the server should consume.

.. code-block:: console

    Enter the amount of memory the server should have, in GB:

Type the numer of gigabytes. Your new minecraft server has now been created. To run it, execute the start.sh script.

Updating the Server
-------------------
To update the server, run:

.. code-block:: console

    pmcu update

You will be notifed of your current minecraft server version.
When you are asked to enter your desired version, pick one from the list or stick with the one you had.

Plugins
-------
To install a plugin, run:

.. code-block:: console

    pmcu install

To update all plugins, run:

.. code-block:: console

    pmcu update-plugins

For more information on plugins, see :doc:`plugins`
