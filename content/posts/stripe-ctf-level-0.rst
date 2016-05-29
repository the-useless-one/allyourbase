Stripe CTF: Level #0
####################
:date: 2012-10-13 15:41
:author: useless
:category: Write-up
:slug: stripe-ctf-level-0
:status: published

.. image:: /images/stripe-ctf-level-0/level00-logo.png
    :alt: level00-logo.png
    :align: center


You can find the code of this level
`here </docs/stripe-ctf-level-0/level00-code.tar.gz>`__.

(sha256: :code:`da9712a1851597d6d4b5a90224a1d0fcaa4b558f55a10ca0c7a115d18fe9dcb7`)

So, this level is a safe that keeps your secrets for you. But it also
keeps secrets for other people. Let's find out how we can recover the
password for this level.

The page is a simple form with three fields: your key, your secret
and the name of your secret. When you post these values, they are
registered in a database in this format: (key.secret_name, secret).

The safe gives you the possibility to retrieve your secrets by entering
your key (otherwise, it'd be a stupid safe). Then, it'll do a SQL query
to get every entry which looks like this: (entered_key.anything,
anything). The SQL query is this one:

.. code-block:: sql

    SELECT * FROM secrets WHERE key LIKE ? || ".%"

It's a prepared query, used to prevent SQL injection (with quotes and
the like). The ? will be replaced by the value you send to the server.
The :code:`LIKE` keyword is used to match a string against a regexp.
The % means "any number of any characters" (kind of like the \*).

The problem with this is that the key you enter is not sanitized. Well,
it's sanitized by the prepared query so that you cannot perform SQL.
But it's not sanitized for the :code:`LIKE` syntax. So
let's say you enter % as a key, the query will look like this:

.. code-block:: sql

    SELECT * FROM secrets WHERE key LIKE %.%

It means "select every secret where the key has the form
'any_characters.any_characters'". And that's every secret! So the safe
will give you every secret stored, and thus, the password for this
level.

w00t!

