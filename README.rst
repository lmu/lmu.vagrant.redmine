===================
lmu.vagrant.redmine
===================

Vagrant and Ansible based test setup for a Redmine Multi-Instance setup as used at LMU Dez. VI.

Requirements
============

* git
* Vagrant (tested on Vagrant 1.8.1, https://www.vagrantup.com/)
* Ansible (1.9 or 2.0+, https://www.ansible.com/)

Your implicite requirements for this setup is:

* for Vagrant / used Vagrant base box:

  * A 64 bit Processor
  * A vPro enabled System / Processor (Intel I5/I7) so that you could use 64 bit guests
  * Virtualbox (https://www.virtualbox.org/)

* for Ansible:

  * An Unix complied Environment (Linux, Mac OS, *BSD)
  * Python2

Dependencies
============

This Git repository uses submodules for including ansible rolls and playbooks used at the LMU Dez. VI.
Please refere to the lmu.ansible.playbooks repository at https://github.com/loechel/lmu.ansible.playbooks for them.

Setup
=====

Please clone this git Repository with all submodules (lmu.ansible.playbooks).
go into the directory and start Vagrant

.. code:: bash

    git clone --recursive https://github.com/loechel/lmu.vagrant.redmine.git
    cd lmu.vagrant.redmine
    vagrant up

If you update or change the redmine playbook rerun the vagrant provision with:

.. code:: bash

    vagrant provision


Development
===========

If you want to contribute to this vagrant environment please contact me at Alexander.Loechel@lmu.de and tell me your github account, so that I could add you to the allowed contributers list.

State of Deployment
===================

This Vagrant Environment is used to update our current Redmine setup from Redmine 2.5.3 to a more current version (3.2.1+) and than continoue upgrades and deployment via the connected playbook and testing via Vagrant.

Current Production State
------------------------

Redmine Agile plugin (PRO version)Scrum and Agile project management plugin for redminehttp://redminecrm.com 	RedmineCRM 	01.03.2005
Redmine Auto Watch pluginThis plugin is a hook to add users in the issue watchers list automatically when they are involved in it. 	Teddy Lerat 	1.0.0
Redmine Checklists plugin (Light version)This is a issue checklist plugin for Redminehttp://redminecrm.com 	RedmineCRM 	3.0.1
Redmine CRM plugin (PRO version)This is a CRM plugin for Redmine that can be used to track contacts and deals informationhttp://redminecrm.com 	RedmineCRM 	03.04.2004
Redmine Helpdesk plugin (PRO version)This is a Helpdesk plugin for Redminehttp://redminecrm.com 	RedmineCRM 	02.03.2000
Did You Mean?A plugin to search for duplicate issues before opening them.http://www.github.com/abahgat/redmine_didyoumean 	Alessandro Bahgat and Mattia Tommasone 	01.02.2000
Redmine Favorite Projects pluginThis is a favorite projects plugin for Redminehttps://github.com/alexandermeindl/redmine_favorite_projects 	RedmineCRM, AlphaNodes GmbH 	1.0.3
Redmine Issue Templates pluginPlugin to generate and use issue templates for each project to assist issue creation.https://bitbucket.org/akiko_pusu/redmine_issue_templates 	Akiko Takano 	0.0.9
KnowledgebaseA plugin for Redmine that adds knowledgebase functionalityhttps://github.com/alexbevi/redmine_knowledgebase 	Alex Bevilacqua 	3.0.4
Redmine LMU modifications pluginCustomizing for LMU Redmine 	AlphaNodes GmbH 	0.0.1
Redmine Local Avatars pluginThis plugin lets users upload avatars directly into Redmine 	Andrew Chaika and Luca Pireddu 	0.1.1
Redmine Spent Time ColumnThis plugin adds a spent time column to issue lists. 	Jan Schulz-Hofen, Planio GmbH 	2.0.0-devel
Redmine TweaksWiki and content extensionshttp://github.com/alexandermeindl/redmine_tweaks 	AlphaNodes GmbH 	0.4.8
Redmine Wiki Extensions pluginThis is a Wiki Extensions plugin for Redminehttp://www.r-labs.org/projects/r-labs/wiki/Wiki_Extensions_en 	Haruyuki Iida 	0.6.4
Redmine Wiki Lists pluginwiki macros to display lists of contents.http://www.r-labs.org/projects/wiki_lists/wiki/Wiki_Lists 	Tomohisa Kusukawa 	0.0.3
Sidebar Hide PluginThis plugin provides ability to hide sidebarhttps://github.com/bdemirkir/sidebar_hide 	Berk Demirkır 	0.0.7

===== ===== ===== ===== ===== ===== ===== =====
Plugin name 	Plugin title 	Provider 	Version 	Prio 	Kommentar
===== ===== ===== ===== ===== ===== ===== =====
redmine_agile 	Redmine Agile plugin (PRO version)Scrum and Agile project management plugin for redminehttp://redminecrm.com 	RedmineCRM 	1.3.5 	1
redmine_auto_watch 	Redmine Auto Watch pluginThis plugin is a hook to add users in the issue watchers list automatically when they are involved in it. 	Teddy Lerat 	1.0.0 	1
redmine_checklists 	Redmine Checklists plugin (Light version)This is a issue checklist plugin for Redminehttp://redminecrm.com 	RedmineCRM 	3.0.1 	?? 	Kann Liz nichts zu sagen
redmine_contacts 	Redmine CRM plugin (PRO version)This is a CRM plugin for Redmine that can be used to track contacts and deals informationhttp://redminecrm.com 	RedmineCRM 	3.4.4 	1
redmine_contacts_helpdesk 	Redmine Helpdesk plugin (PRO version)This is a Helpdesk plugin for Redminehttp://redminecrm.com 	RedmineCRM 	2.3.0 	1
redmine_didyoumean 	Did You Mean?A plugin to search for duplicate issues before opening them.http://www.github.com/abahgat/redmine_didyoumean 	Alessandro Bahgat and Mattia Tommasone 	1.2.0 	?? 	wird bisher nicht eingesetzt
redmine_favorite_projects 	Redmine Favorite Projects pluginThis is a favorite projects plugin for Redminehttps://github.com/alexandermeindl/redmine_favorite_projects 	RedmineCRM, AlphaNodes GmbH 	1.0.3 	1 	wird für die Projektübersichtsseite verwendet zur hierarchischen Darstellung, für Auswertungen hilfreich (Überprojekte müssten von uns aus keine eigenen Projekte sein)
redmine_issue_templates 	Redmine Issue Templates pluginPlugin to generate and use issue templates for each project to assist issue creation.https://bitbucket.org/akiko_pusu/redmine_issue_templates 	Akiko Takano 	0.0.9 	?? 	Kann Liz nichts zu sagen
redmine_knowledgebase 	KnowledgebaseA plugin for Redmine that adds knowledgebase functionalityhttps://github.com/alexbevi/redmine_knowledgebase 	Alex Bevilacqua 	3.0.4 	1
redmine_lmu_modifications 	Redmine LMU modifications pluginCustomizing for LMU Redmine 	AlphaNodes GmbH 	0.0.1
redmine_local_avatars 	Redmine Local Avatars pluginThis plugin lets users upload avatars directly into Redmine 	Andrew Chaika and Luca Pireddu 	0.1.1 	2 	wär aber schön zu haben
redmine_spent_time_column 	Redmine Spent Time ColumnThis plugin adds a spent time column to issue lists. 	Jan Schulz-Hofen, Planio GmbH 	2.0.0-devel 	2 	wird aktuell nicht genutzt
redmine_tweaks 	Redmine TweaksWiki and content extensionshttp://github.com/alexandermeindl/redmine_tweaks 	AlphaNodes GmbH 	0.4.8 	1
redmine_wiki_extensions 	Redmine Wiki Extensions pluginThis is a Wiki Extensions plugin for Redminehttp://www.r-labs.org/projects/r-labs/wiki/Wiki_Extensions_en 	Haruyuki Iida 	0.6.4 	1
redmine_wiki_lists 	Redmine Wiki Lists pluginwiki macros to display lists of contents.http://www.r-labs.org/projects/wiki_lists/wiki/Wiki_Lists 	Tomohisa Kusukawa 	0.0.3 	1 	Wird verwendet für Macros im Taskboard
sidebar_hide 	Sidebar Hide PluginThis plugin provides ability to hide sidebarhttps://github.com/bdemirkir/sidebar_hide 	Berk Demirkır 	0.0.7 	1
===== ===== ===== ===== ===== ===== ===== =====



Current Development State
-------------------------

Test for Redmine Versions:

* 3.2.1
* 3.1.4

Test for Ubuntu Versions (64bit):

* Ubuntu 14.04 (Trusty64)
* Ubuntu 16.04 (Xenial64)

Development States
------------------

Based on dates

* 2016-04-06
* 2016-04-07
* 2016-04-08
* 2016-04-11


State of 2016-04-06
...................

* Vagrant box tests for Ubuntu 16.04 and Redmine 3.2.x

  * seen differences, newer package versions:

    * postgresql (9.3 --> 9.5)
    * ruby (1.9.1 --> 2.3.0)
    * switch from initd --> systemd

* Implementation of 'memcached' Server
* Configuration of Redmine Instance based cache:store via dalli


Todos für heute
+++++++++++++++

* Überblick über Plugins verschaffen
* Betriebskonzept formulieren
* Aktuelles Setup beschreiben
* redminetest2 bespielen

State of 2016-04-07
...................



TODOs
-----







Probleme
--------

* Grundproblem: Redmine 3.2 hat nicht funktioniert -> zurück auf 3.1 mit 5 Plugins --> läuft auf Entwicklungsrechner
* bei Bespielen von redminetest2:
* svn checkout geht nicht (Proxy-Problem, curl geht)
* ruby gems download geht nicht (proxy)
* plugins download geht nicht (proxy)
Workaround: gem-cache und plugins kopieren auf ansible-master
* offene Frage: auch redmine-basis-app über lokales Verzeichnis bereitstellen?

redminmetest2
(A) http/https müssen offen sein --> Alexander klärt das mit Subur/Andrej


Ausblick (Perspektive von Jan)
------------------------------

* Server redminetest2 sollte vor Alexanders langem Urlaub in einem definierten und funktionablen Zustand sein, bei dem grundsätzlich ein Weiterarbeiten ohne Ansible möglich ist:
Mindestanforderungen:
* Redmine 3.1 inklusive der notwendigen Plugins
* überführte Daten aus dem redminetest1 samt update der Applikation auf 3.1


Offene Fragen zum Betriebskonzept
---------------------------------

* Welche Infrastrukturkomponenten und Arbeitswerkzeuge sind für Entwicklung und Betrieb notwendig?
* Ist die Ansible-Infrastruktur für den allgemeinen Betrieb ausgelegt/verfügbar, so dass andere Kollegen im Dezernat damit arbeiten können?
* Gibt es alternative Möglichkeiten, im Notfall auch ohne Ansible modifikationen am Redmine-Server vorzunehmen? Kann man zur Not auch lokal auf dem redminetest2 arbeiten und die Abweichungen später wieder einfangen?
