May the Cipher be with you
##########################
:date: 2013-02-03 01:42
:author: useless
:category: Cryptography
:slug: may-the-cipher-be-with-you
:status: published

.. image:: /images/may-the-cipher-be-with-you/ciphersaber-logo.png
    :alt: ciphersaber-logo.png
    :align: center

NB: I know that implementing cryptographic algorithms yourself is
dangerous. There are many implementation problems people won't think
about, like memory management. I just wanted to talk about the
CipherSaber because I think it's an old, yet neat project. I think it's
important to sensitize people about cryptography and the regulations
around its usage. **If you want to use cryptography to protect your
privacy, I suggest you look at a more serious project like PGP.**

A few months ago, while checking my RSS feeds, I saw `this discussion
<http://www.reddit.com/r/netsec/comments/10d7zb/are_there_any_inprogress_opensource_cryptography/>`_
on Reddit. Since I love cryptography and FLOSS, I looked at the comment
section, to see what kind of answers were posted.

One comment caught my attention:

.. image:: /images/may-the-cipher-be-with-you/ciphersaber-comment.png
    :alt: ciphersaber-comment.png
    :align: center

What intrigued me was the idea of creating your own "something" (plus,
the "something" had a really cool name), and I also like the fact that I
could start right away.

So, I went to the `CipherSaber <http://ciphersaber.gurus.org/>`__ web
page, to see what's what. And, being the privacy advocate that I am, I
was not disappointed. The CipherSaber is a form of protest against US
ban on cryptography.

It was written after 9/11, when the US government wanted to limit the
use/publication of cryptography, in order to prevent the terrorists from
using it. It's, of course, a ridiculous idea, since the crypto is
*already* out there, and anybody can use it, even the terrorists: it's
a little too late to try to prevent cryptography export. Plus, as stated
in the CipherSaber web page, nothing would prevent terrorists to send
some of their members to US universities to learn cryptography, as they
do to learn chemistry, nuclear engineering etc.

As my good friend (okay, we've never met, but still, he has a point)
Philip Zimmermann said:

    If privacy is outlawed, only outlaws will have privacy.

The idea behind the CipherSaber, is to have everyone implementing a
strong crypto algorithm, so that people don't rely on products that can
be banned. The chosen algorithm is the stream cipher RC4, because it's
strong, and easy to implement (see CipherSaber-2 in the web page to
correct a known vulnerability in RC4). The name CipherSaber comes from
Star Wars, because every Jedi knight has to build its own light saber,
just like every CipherKnight should implement its own CipherSaber.

I know I'm not from the US, and I know this web page was written ten
years ago, but I like the idea of being a part of some community, and
Internet ban concern everyone. That's why I've decided to revamp the
CipherKnight's certificate (the old one, in addition to being hard to
find, is too directed towards Americans).

All you have to do to get your certificate is to enter your name, click
the button, and decipher it using your own CipherSaber (the encryption
key is *AlanTuring*).

.. raw:: html

   <form action="/cscertificate/index.php" method="post">
        <label for="name">Name</label>: <input name="name" type="text"> <input value="Get your certificate!" type="submit">
   </form>

If you're old school, you can get the former CipherKnight's certificate
`here <https://allyourbase.utouch.fr/wp-content/uploads/2014/08/cknight.cs1>`__
(the encryption key is *ThomasJefferson*).

So go ahead, forge your own CipherSaber, print out your certificate, and
spread the word.

May the Cipher be with you.

