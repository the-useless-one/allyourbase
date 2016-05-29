Stripe CTF: Level #2
####################
:date: 2012-10-13 16:11
:author: useless
:category: Write-up
:slug: stripe-ctf-level-2
:status: published

.. image:: /images/stripe-ctf-level-2/level02-logo.png
    :alt: level02-logo.png
    :align: center


You can find the code for this level
`here </docs/stripe-ctf-level-2/level02-code.tar.gz>`__.

(sha256: :code:`d175b624ed888badd795c5474ae855f711e856cc41c0757059594babe8f23413`)

This level is a whole social network!

Okay, it's not, it's just a page with a profile picture. But on the
bottom of the page, you can see something interesting: "Password for
Level 3 (accessible only to members of the club)". Of course, if you
click on it it doesn't work. Let's see how we can access this file.

The key here is that you can upload your picture so that it's displayed
on your profile page.

.. image:: /images/stripe-ctf-level-2/level02-uploaded-picture.png
    :alt: level02-uploaded-picture.png
    :align: center

But if you look at the code, you can see that no check is performed on
the file you upload. Which means you can upload **any** file, not just a
picture.

You also know where your "picture" is stored: uploads/your_file. So we
can upload a PHP script that'll open the password file, and visit the
URL where it's located to execute it:

.. code-block:: php

    <?php
        $content = file_get_contents("../password.txt"):
        echo $content;
    ?>

Let's name this file exploit.php. We upload it:

.. image:: /images/stripe-ctf-level-2/level02-uploaded-script.png
    :alt: level02-uploaded-script.png
    :align: center

We can see that no image is displayed (because your browser can't
display the script as an image), yet the server says it was successfully
uploaded. Now, we just have to go to upoads/exploit.php, and **bam!**
you have the password for this level.

.. image:: /images/stripe-ctf-level-2/level02-executing-script.png
    :alt: level02-executing-script.png
    :align: center

w00t!

