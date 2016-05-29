Stripe CTF: Level #5
####################
:date: 2012-10-27 23:31
:author: useless
:category: Write-up
:slug: stripe-ctf-level-5
:status: published

.. image:: /images/stripe-ctf-level-5/level05-logo.jpg
    :alt: level05-logo.jpg
    :align: center

You can find the code for this level
`here </docs/stripe-ctf-level-5/stripe-ctf-level05.tar.gz>`__.

(sha256:
:code:`82b066cca46fd24a16959ada973d6df0d7c693f7791a8b673add276f324a5885`)

This level wants to solve a real problem: identification. We have too
many online accounts and we have to remember usernames/passwords for
everyone of them. It would be way simpler to be able to log into a new
web service using your Google account, or your Facebook account (kind of
like `OpenID <https://en.wikipedia.org/wiki/OpenID>`__). That's what
this level is all about.

This service asks for a pingback address (it's the service you want
to use to identify, like using Google or Facebook with OpenID), and your
username/password to this pingback. The form will then send your
credentials to the pingback and see if you're successfully
authenticated.

.. code-block:: ruby

    # File srv.rb, line 20
    PASSWORD_HOSTS = /^level05-\d+\.stripe-ctf\.com$/ # To get the password, the pingback must follow this regex
    ALLOWED_HOSTS = /\.stripe-ctf\.com$/ # The pingback must follow this regex

Note that these regex were for the real CTF. For a local usage, here are
what they look like:

.. code-block:: ruby

    # File srv.rb, line 23
    PASSWORD_HOSTS = /^localhost$/ # To get the password, the pingback must follow this regex
    ALLOWED_HOSTS = // # No restriction on the allowed hosts

We can only use pingback URL ending in .stripe-ctf.com, but fortunately,
we still have access to the social network on level #2! We can upload a
PHP file, which will always say the authentication is successful.

Note: on the next screenshots, I'll use 127.0.0.1 as the address for
level #2, and localhost as the address for level #5!

So, how does the service know that we were successfully authenticated to
the pingback?

.. code-block:: ruby

    # File srv.rb, line 109
    def authenticated?(body)
        body =~ /[^\w]AUTHENTICATED[^\w]*$/
    end

So, all we have to do is upload the following file to level #2:

.. code-block:: php

    <?php
        echo " AUTHENTICATED \n";
    ?>

Let's fill the form to use :code:`level02-[numbers].stripe-ctf.com`
as a pingback:

.. image:: /images/stripe-ctf-level-5/level05-first-form.png
    :alt: level05-first-form.png
    :align: center

We submit, and here are the result of the authentication...

.. image:: /images/stripe-ctf-level-5/level05-first-login.png
    :alt: level05-first-login.png
    :align: center

...and the new login page:

.. image:: /images/stripe-ctf-level-5/level05-first-authentication.png
    :alt: level05-first-authentication.png
    :align: center

Okay, now we can authenticate using this script, but we can't recover
the password, cause the URL is
:code:`level02-[numbers].stripe-ctf.com`, and not
:code:`level05-[numbers].stripe-ctf.com`. The key is to see how the
server recovers the pingback URL we give him:

.. code-block:: ruby

    # File srv.rb, line 67
    pingback = params[:pingback]
    username = params[:username]
    password = params[:password]
    [...]
    # File srv.rb, line 80
    body = perform_authenticate(pingback, username, password)
    [...]
    # File srv.rb, line 99
    def perform_authenticate(url, username, password)
        $log.info("Sending request to #{url}")
        response = RestClient.post(url, {:password => password,
                                         :username => username})
        body = response.body

        $log.info("Server responded with: #{body}")
        body
    end

The server uses :code:`params` to recover the informations sent by
the form. Then it :code:`POST` s the username and the password to the
to the pingback URL. But :code:`params` is the Ruby equivalent of
:code:`$_REQUEST` in PHP, which recovers the informations sent by
:code:`POST`, but also by :code:`GET`. So let's say we put this as
a pingback URL:
:code:`http://leve05-[numbers].stripe-ctf.com?pingback=http://level02-[numbers].stripe-ctf.com`.

Okay, here is where it gets tricky: the server retrieves the previous
URL as a pingback. It then posts our username/password to it, i.e. to
itself, since the address is
:code:`level05-[numbers].stripe-ctf.com`. So the server finds itself
with a username/password by :code:`POST`, and a pingback (the level
#2 URL) by :code:`GET`. So it does its business: sends the
username/password to the pingback.

First we fill in the login:

.. image:: /images/stripe-ctf-level-5/level05-second-form.png
    :alt: level05-second-form.png
    :align: center

Then we submit:

.. image:: /images/stripe-ctf-level-5/level05-second-login.png
    :alt: level05-second-login.png
    :align: center

We clearly see here that the server was interrogated twice.

And we just have to go back to the login page:

.. image:: /images/stripe-ctf-level-5/level05-w00t.png
    :alt: level05-w00t.png
    :align: center

w00t!

