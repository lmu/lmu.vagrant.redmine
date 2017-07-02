=======================
Migrations-Plan Redmine
=======================

Geplante Migration des Servers Redmine1 --> Redmine3 / Redminetest3.

Zu migrierende Instanzen
========================

* ref_vi.4 --> dez_vi
* ref_vi.5 --> webprojekte
* dez_vii

Nicht zu migrierende Instanzen
==============================

* ref_vi.3

Termin
======

* 13.07.2017
* 27.07.2017 (Alternativ Termin)

Schritte
========

Redmine1
--------

#. Apache ausschalten
#. Cron-Jobs dauerhaft ausschalten (Mailabruf, SPAM, Warteschlange)
#. Backup erstellen
#. Backup kopieren

Redmine3
--------

Vorbereitung
............

#. Löschen aller Instanzen (dbs, files, app)
#. Neusetup Redmine via Ansible-Playbook

Migration
.........

#. Restore Backup (wichtig, files-Storage kontrolieren)
#. Migrations-Lauf des Ansible-Playbooks
#. Reboot
#. DNS-Eintrag umziehen
#. Redmine-Konfiguration in allen Instanzen anpassen

Nachbereitung
.............

#. Standard Backup erstellen und auf Redminetest3 übertragen
#. Load-Tests
#. Tests der Migration
#. Info das Migration beendet

Redminetest3
------------

Vorbereitung
............

#. Löschen aller Instanzen (dbs, files, app)
#. Neu-Setup Redmine via Ansible-Playbook

Auto-Migration / Daily Restore testen
.....................................

#. Backup-Import
#. Jenkins-Run Migration (Redmine Ansible Playbook)
#. Reboot
