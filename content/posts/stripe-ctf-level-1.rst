Stripe CTF: Level #1
####################
:date: 2012-10-13 15:52
:author: useless
:category: Write-up
:slug: stripe-ctf-level-1
:status: published

.. image:: /images/stripe-ctf-level-1/level01-logo.jpg
    :alt: level01-logo.jpg
    :align: center

You can find the code of this level
`here </docs/stripe-ctf-level-1/level01-code.tar.gz>`__.

(sha256: :code:`b67c313a1a3bebd8702159efae32f95f1b41885f6e00103ee53e896a53194f43`)

So, this level wants you to guess a password, stored in a file named
"secret-combination.txt" on the server. If you manage to do it, it'll
give you the password for this level. Let's take a look at the code and
see how to get the password without knowing the combination.

The server starts by defining a variable :code:`$filename` equal
to "secret-combination.txt". That's the file of the combination (I'm so
deductive). It then retrieves your attempt (which was passed by :code:`GET`),
and compares it to the content of the file. If they're the same, the
server will gives you the sweet, sweet password. Otherwise, tough.

.. image:: /images/stripe-ctf-level-1/level01-failed-attempt.png
    :alt: level01-failed-attempt.png
    :align: center

The thing is, the server doesn't retrieve your attempt using
:code:`$_GET['attempt']`. It uses the `extract PHP
function <http://php.net/manual/en/function.extract.php>`__ on the
:code:`$_GET` array. Basically, for every entry :code:`$_GET['key'] = value`,
it’ll create a variable :code:`$key` with the value
:code:`value`. It means that if we give a parameter filename in the
:code:`GET` request, we can override the variable :code:`$filename`, and open
any file. So let's open a non-existing file, and give an empty guess:
:code:`?attempt=&filename=dummy-filename.txt`

This request will set :code:`$filename` to "dummy-filename.txt", so
that when the server tries to retrieve its content, it'll yield an empty
string. Since our attempt is empty, it will match, and the server will
give us the password for this level.

.. image:: /images/stripe-ctf-level-1/level01-success-attempt.png
    :alt: level01-success-attempt.png
    :align: center

w00t!

