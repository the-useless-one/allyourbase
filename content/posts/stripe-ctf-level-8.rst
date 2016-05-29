Stripe CTF: Level #8
####################
:date: 2012-12-15 20:06
:author: useless
:category: Write-up
:slug: stripe-ctf-level-8
:status: published

.. image:: /images/stripe-ctf-level-8/level08-logo.jpg
    :alt: level08-logo.jpg
    :align: center

You can find the code for this level
`here </docs/stripe-ctf-level-8/stripe-ctf-level08.tar.gz>`__.

(sha256:
:code:`d211aa240a0a59eb1f56d3c42a55080d0e27eea2c04bc4410bf608824c847c96`)

This is it. The final level to the Stripe CTF. The goal here is to
retrieve a 12-digit password, which is too long to brute force. Let's
see how we can use the protocol to our advantage.
 
The infrastructure looks like this:

-  a central server, used to verify the password
-  four "chunk" servers, which each knows only a part of the password

When you send a password to the central server, it cuts it in four
pieces, and procedes like this:

-  it asks the first chunk server if the first piece is correct
-  if not, it sends a failure message to the client (and doesn't contact
   any other chunk server)
-  if it is, it asks the second chunk server if the second piece is
   correct
-  etc.

Furthermore, we can give the server a list of webhooks, to which it'll
send the result.

Seeing the password verification protocol, I know what you're thinking:
timing attack. Seeing how much time the server takes to respond, we can
find how many chunk servers it contacted, thus how many chunk we
:math:`10^12` possibilities, we're down to
:math:`4 \times 10^3` possibilities, which is feasible.

The problem is that the server has a way to prevent timing attack:

.. code-block:: python

    # File primary_server, line 58
    def nextServerCallback(self, data):
        parsed_data = json.loads(data)
        # Chunk was wrong!
        if not parsed_data['success']:
            # Defend against timing attacks
            remaining_time = self.expectedRemainingTime()
            self.log_info('Going to wait %s seconds before responding' %
            remaining_time)
            reactor.callLater(remaining_time, self.sendResult, False)
            return

        self.checkNext()

If a chunk is wrong, the server waits before telling the client he made
a mistake. So we can't use a timing attack.

But there is another way to know how many chunk servers the primary
contacted, and thus go from :math:`10^12` to :math:`4 \times 10^3`
the webhooks. Here is the idea:

-  when the primary server communicates with an external resource
   (whether it's a chunk server or a webhook), it opens a socket
-  every time the primary server opens a socket, its client port is
   incremented by one
-  the webhook knows the client port of the primary server

So, by looking at how much was the client port incremented between two
responses, the webhook knows how many chunk servers were contacted.
Indeed, let's say the first chunk is wrong: the primary server connects
to the first chunk server, then to the webhook. The port is therefore
incremented by two. If the first chunk is correct, but not the second is
wrong, the primary servers contacts the first chunk server, the second
chunk server, then the webhook. The port is incremented by three, etc.

So, knowing this we can't find the correct chunks, but we can eliminate
the bad chunks, which is faster than bruteforcing the whole password,
but still takes a lot of time. What's more, the primary server can only
contact webhooks with URL ending with .stripe-ctf.com (in the production
environment). Fortunately, we still have access to the level 2 server
(remember, the one with the upload vulnerability?) We can upload an SSH
key, connect, and then launch our webhook.

Unfortunately, I lost the source code of my custom webhook (sorry about
that!). It was based on a webhook coded by a friend of Lopi. Basically,
it tried every possible combination, chunk by chunk, and eliminated the
bad ones as it did so.

The attack took something like two days, because I kept being
disconnected of the server, and because there were so many people on it
running their own webhook. I think it was kind of stubborn from Stripe
to force the webhook to be on one of their server.

.. image:: /images/stripe-ctf-level-8/level08-scumbag-stripe.png
    :alt: level08-scumbag-stripe.png
    :align: center

Anyway, after some time, you find the correct password, which you submit
to the Stripe web site.

.. image:: /images/stripe-ctf-level-8/level08-w00t.png
    :alt: level08-w00t.png
    :align: center

w00t!

That's it for the Stripe CTF! I know I took a lot of time writing these
write ups, but I learned a lot from this competition, especially the
SHA1 padding attack, how to find where to put my Javascript so it's
executed, and how to obfuscate it. Plus I won a super cool t-shirt!

See you for another CTF!

.. image:: /images/stripe-ctf-level-8/stripe-ctf-prize.jpg
    :alt: stripe-ctf-prize.jpg
    :align: center

