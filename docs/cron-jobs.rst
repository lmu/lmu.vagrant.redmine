Cron-Jobs
=========

User: root

hosts file should link www.scm.verwaltung.uni-muenchen.de to localhost / 127.0.0.1

.. code:: cron

    # Backup Scripts
    * 21 * * * backup.sh
    * 20 * * * cleanup-backups.sh

    # E-Mail
    * * * * * wget

    # Redmine Helper Scripts
    * * * * * spam.py
    * * * * * warteschlange.py
