SANS Christmas Challenge 2012
#############################
:date: 2013-01-07 12:20
:author: useless
:category: Write-up
:slug: sans-christmas-challenge-2012
:status: published

.. image:: /images/sans-christmas-challenge-2012/sans_christmas_challenge_2012_logo.jpg
    :alt: sans_christmas_challenge_2012_logo.jpg
    :align: center


During December, SANS posted a `Christmas
challenge <http://pen-testing.sans.org/holiday-challenge/2012>`__ based
on a Christmas story.

This year, Santa is sad because he feels that nobody believes in him
anymore, so he decides to cancel Christmas. Mrs. Claus wants to cheer
her husband up, in order not to let children down, but her reindeer gets
imprisoned in Southtown's dog pound. The mayor accepts to let Vixen, the
reindeer, go if Mrs. Claus can make it snow in Southtown, which is a
relatively hot region.

So Mrs. Claus goes to see Snow Miser, who is in charge of the cold
weather. Unfortunately, he refuses to make it snow in Southtown, because
it's in his brother's, Heat Miser, territory. But Heat Miser agrees to
make it snow in Southtown as long as he's allowed to melt the North
Pole. Unfortunately, the brothers are too stubborn, and refuse to let
each other have control over the other's territory. So Mrs. Claus takes
it to a higher authority: Mother Nature, who forces the brothers to
cooperate.

Since they have to collaborate, Snow Miser and Heat Miser decide to
have a little fun and make it a competition: they both have to hack
every level of the other brother's weather control. You can follow
`@sn0w_m1s3r <https://twitter.com/sn0w_m1s3r>`__ and
`@h34t_m1s3r <https://twitter.com/h34t_m1s3r>`__ on Twitter.

To make things interesting, SANS posted six questions, and will
reward the best answers:

#. Where did you find the remainder of Snow Miser's Zone 1 URL?
#. What is the key you used with steghide to extract Snow Miser's Zone 2
   URL? Where did you find the key?
#. On Snow Miser's Zone 3 page, why is using the same key multiple times
   a bad idea?
#. What was the coding error in Zone 4 of Heat Miser's site that allowed
   you to find the URL for Zone 5?
#. How did you manipulate the cookie to get to Zone 5 of Heat Miser's
   Control System?
#. Please briefly describe the process, steps, and tools you used to
   conquer each zone, including all of the flags hidden in the comments
   of each zone page.

I'll focus on the sixth question, while answering the first questions in
my write up.

`Snow Miser <http://snowmiser.counterhack.com/>`__
==================================================

Zone 0
------

flag: :code:`3b5a630fc67251aa5555f4979787c93f`

    Unlike my brother, my fridged minions (without freakish hair) didn't
    mess up and leak our URLs to search engines or have to block them
    from the search engines. There is no vulnerability to get to the
    next zone and you will not find a vulnerability here. Move along.

    Those of you with proper access, the URL you need starts with the
    following:
    
    zone-1-D2E31380-50E6-4869-8A85-XXXXXXXXXXXX

The URL is composed only of digits (0 through 9) and letters (A through
F), which gives us 281.474.976.710.656 possible combinations. We can't
bruteforce so many combinations (plus, it's explicitly stated in the
challenge's rules that bruteforce is disallowed).

Fortunately, Snow Miser tweets this message:

.. image:: /images/sans-christmas-challenge-2012/snow_miser_tweet_1.png
    :alt: snow_miser_tweet_1.png
    :align: center

Here's the posted image:

.. image:: /images/sans-christmas-challenge-2012/snow_miser_glass_reflection.jpg
    :alt: snow_miser_glass_reflection.jpg
    :align: center


We can see in the something interesting in the screen's reflection in
the glass: the end of the URL we're looking for. With a tool like GIMP,
we can manipulate the image to make it easier to read it:

.. image:: /images/sans-christmas-challenge-2012/snow_miser_glass_reflection_enhanced.jpg
    :alt: snow_miser_glass_reflection_enhanced.jpg
    :align: center


Which gives us this final URL:
zone-1-D2E31380-50E6-4869-8A85-F9CDB3AF6226

Zone 1
------

flag: :code:`38bef0b61ba8edda377b626fe6708bfa`

    One of my minions, who has been turned into a snowman, messed up and
    changed the URL for Zone 2. If you have access to this level you can
    analyze the images and access the next zone.

This message kind of points to some sort of steganography use. This is
where the second question helps us. We know the program steghide was
used on a image. While looking at the website's images, we can see that
they're all PNG, except for `this
one </images/sans-christmas-challenge-2012/off.jpg>`__,
which is JPG. Since steghide doesn't support PNG, we know that the URL
is hidden in the last image.

Now, we need to find the key, in order to extract the hidden file. If
you open the image in a hexadecimal editor, you'll find an ASCII string,
"IceIceBaby!". Let's use it as the key:

.. code-block:: shell

    $ steghide extract -sf off.jpg
    Enter passphrase: IceIceBaby!
    Extracted data written to tmpfile.txt
    $ cat tmpfile.txt
    zone-2-6D46A633-25D7-42C8-AF94-8E786142A3E3

Zone 2
------

flag: :code:`b8231c2bac801b54f732cfbdcd7e47b7`

    The same minion that messed up the Zone 2 link also messed up the
    Zone 3 link. Make sure you use the new link that starts with:

    zone-3-EAB6B031-4EFA-49F1-B542-XXXXXXXXXXXX

    Please do not tweet the links or parts of the links.

    All security issues that used to allow access to the next zone have
    been fixed. There is no vulnerability to get to the next zone and
    you will not find a vulnerability here. Move along.

Heat Miser kindly tweets:

.. image:: /images/sans-christmas-challenge-2012/heat_miser_tweet_2.png
    :alt: heat_miser_tweet_2.png
    :align: center

You can retrieve Snow Miser's data
`here </docs/sans-christmas-challenge-2012/android.data_.tar.gz>`__
(sha256:
:code:`286387c77b533aae4d605d85a5e74c819f3e0ca7ca42b991ddd29abf9ff5a6b4`).

After extracting it, we can use some shell mojo to find files mentioning
the zone 3 URL:

.. code-block:: shell

    $ tar -xzvf android.data.tgz
    $ cd data
    $ grep -Rn "zone-3" . 2> /dev/null
    Binary file ./data/com.android.browser/cache/browser_state.parcel
    concordant
    Binary file
    ./data/com.android.browser/cache/webviewCacheChromium/data_1 concordant
    Binary file
    ./data/com.android.browser/cache/webviewCacheChromium/data_2 concordant
    Binary file ./data/com.android.browser/databases/browser2.db
    concordant
    Binary file ./data/com.android.browser/databases/browser2.db-wal
    concordant

The first file looks is a browser cache file, which may contain the
wanted URL. By reading it, we'll find:
zone-3-EAB6B031-4EFA-49F1-B542-30EBE9EB3962

Zone 3
------

flag: :code:`08ba610172aade5d1c8ea738013a2e99`

    To reduce the impact of URL exposure or modification we have added a
    new mechanism to distribute changes to the URL (thanks to that
    minion that broke Zones 2+). Those of you with with access to Zone 4
    should have received an encryption key. This key can be used to
    decrypt the URL for Zone 4. This allows us to securely communicate
    it to you without risk of unauthorized access.

    To verify your key you can check the previous Zone 4 URL:

    zone-4-F7677DA8-3D77-11E2-BB65-E4BF6188709B

    20d916c6c29ee53c30ea1effc63b1c72147eb86b998a25c0cf1bf66939e8621b3132d83abb1683df619238

    The new Zone 4 encrypted string is:
    20d916c6c29ee54343e81ff1b14c1372650cbf19998f51b5c51bf66f49ec62184034a94fc9198fa9179849

We know the cipher texts both encrypt plain texts starting with zone-4-,
and by looking at them, we can see that they both start with the same
letters. It hints to a bytewise encryption scheme. It turns out that
it's a XOR encryption. The first "oops" here, is that since we're given
a plain text and its cipher text, we can recover the whole key. Indeed,
by the propriety of the XOR operator (here denoted by :math:`\oplus`):

* :math:`c = k \oplus p`
* :math:`c \oplus p = k \oplus p \oplus p = k`

The second "oops" is using the same key twice, because now that we have
the key, we can decrypt the second cipher text:

.. code-block:: python

    #!/usr/bin/python
    #-*- encoding: Utf-8 -*-

    import sys

    def main():
        if len(sys.argv) < 4:
            print 'usage: %s ' % sys.argv[0]
            return -1

        plain1, cipher1, cipher2, = sys.argv[1:]
        plain2 = ''

        for i in xrange(len(plain1)):
            plain2 += chr(ord(plain1[i]) ^ int(cipher1[2*i:2*i+2], 16) ^ int(cipher2[2*i:2*i+2], 16))

        print plain2

        return 0

    if __name__ == '__main__':
        main()

Now let's launch this program:

.. code-block:: shell

    $ ls
    xor_encrypt.py
    $ ./xor_enc.py zone-4-F7677DA8-3D77-11E2-BB65-E4BF6188709B
    20d916c6c29ee53c30ea1effc63b1c72147eb86b998a25c0cf1bf66939e8621b3132d83abb1683df619238
    20d916c6c29ee54343e81ff1b14c1372650cbf19998f51b5c51bf66f49ec62184034a94fc9198fa9179849
    zone-4-9D469367-B60E-4E08-BDF1-FED7CC74AF33

Zone 4
------

flag: :code:`de32b158f102a60aba7de3ee8d5d265a`

    Zone 5 requires top security. We are updating the code using svn 1.7
    and have implemented One-Time-Password (OTP) functionality to access
    Zone 5.

    The passwords are in a SHA1 format, so they are unguessable.

If we look at the source code, we can see that the One Time Password is
sent to the zone 5 URL, so we don't have to look very far to find it.
But if we try to access it directly, we're redirected to a page,
noaccess.php. With this tweet, Heat Miser gives us a big hint:

.. image:: /images/sans-christmas-challenge-2012/heat_miser_tweet_3.png
    :alt: heat_miser_tweet_3.png
    :align: center

By looking at `the tutorial he
gives <http://pen-testing.sans.org/blog/pen-testing/2012/12/06/all-your-svn-are-belong-to-us>`__
(see, this meme doesn't get old!) we can get the index page source code:

.. code-block:: php

    <?php
        function generate_otp($time) {
            $pass = sha1("$time 7998f77a7dc74f182a76219d7ee58db38be3841c");
            return($pass);
        }

        function verify_otp($inpass) {
            // passwords are valid for up to 3 minutes
            // don't forget to use the server time (see the noaccess.php page)
            $validstamps = array(
                date('Y-m-d H:i', strtotime('+1 minute')), // added just in case the time sync is off
                date('Y-m-d H:i'),
                date('Y-m-d H:i', strtotime('-1 minute')),
                date('Y-m-d H:i', strtotime('-2 minute')),
            );

            foreach ($validstamps as $stamp) {
                if (strtolower($inpass) == generate_otp($stamp))
                    return TRUE;
            }
            return FALSE;
        }

        if ((array_key_exists('otp', $_POST) &&
            verify_otp($_POST['otp'])) || (array_key_exists('otp', $_COOKIE)
            && verify_otp($_COOKIE['otp']))) {
                setcookie('otp', generate_otp(date('Y-m-d H:i')));
        } else {
            header( 'Location: noaccess.php' );
            die();
        }

        $accessallowed = TRUE;
        $zone=5;
        require_once('../include/template.inc.php');
    ?>

Now we know how the One Time Passwords are generated. We just have to
send the correct SHA1 sum, using the server's current time, which we can
find in the source code of the noaccess.php page.

Zone 5
------

flag: :code:`3ab1c5fa327343721bc798f116be8dc6`

Game over for the North Pole.

`Heat Miser <http://heatmiser.counterhack.com/>`__
==================================================

Zone 0
------

flag: :code:`1732bcff12e6550ff9ea44d594001418`

    We had a security concern where the Zone 1 URL ended up in search
    engine results. We added a file to prevent the search engines from
    caching these pages. The system is now secure an no unauthorized
    users have access to the URL.

    Don't even try to access the other zones, because you won't be able
    to. And if you are helping my brother, GO AWAY!

The important part here is the file to prevent indexing by search
engines. Heat Miser is talking about the robots.txt file, which tells
search engine crawlers what page they can crawl. By loading this file,
we find the wanted URL: zone-1-E919DBF1-E4FA-4141-97C4-3F38693D2161.

Zone 1
------

flag: :code:`d8c94233daef256c42bb95bd61382e02`

    We had an issue with Zone 2 and we had to temporarily remove the
    link. It is now back and in full operation. We appoligize to those
    living in Zone 2 as it may have gotten a tad chilly. Everything is
    fully operational now.

Looking at the comment will give you the URL to the next zone:
zone-2-761EBBCF-099F-4DB0-B63F-9ADC61825D49

Zone 2
------

flag: :code:`ef963731de7e886226fe4a6a6c2971f1`

    We are sorry, but due to the negligence of one of our fiery minions,
    we had to change the link for Zone 3. If you should have access then
    you should have received an email. The new zone 3 link starts with
    zone-3-83FEE8BE-B1C6-4395-A56A-XXXXXXXXXXXX.

There are 281,474,976,710,656 possibilities for the last set of numbers,
so don't bother brute forcing it. Once again, we have an incomplete URL.
But Heat Miser tweets this message:

.. image:: /images/sans-christmas-challenge-2012/heat_miser_tweet_1.png
    :alt: heat_miser_tweet_1.png
    :align: center


The tweeted image is:

.. image:: /images/sans-christmas-challenge-2012/heat_miser_transparent_terminal.png
    :alt: heat_miser_transparent_terminal.png
    :align: center


And, as Snow Miser says:

.. image:: /images/sans-christmas-challenge-2012/snow_miser_tweet_2.png
    :alt: snow_miser_tweet_2.png
    :align: center

This is looks just like the first level of Snow Miser. Using GIMP, we
can make the end of the URL appear:

.. image:: /images/sans-christmas-challenge-2012/heat_miser_transparent_terminal_enhanced.png
    :alt: heat_miser_transparent_terminal_enhanced.png
    :align: center

Which gives us the URL: zone-3-83FEE8BE-B1C6-4395-A56A-BF933FC85254

Zone 3
------

flag: :code:`0d524fb8d8f9f88eb9da5b286661a824`

    We added a new security mechanism to Zone 4 so it won't matter if
    SOMEONE LEAKS IT AGAIN!

    Zone 4 (zone-4-0F2EA639-19BF-40DD-A38D-635E1344C02B)

We can directly access zone 4, since Heat Miser posts a link to it. But
when we click it, we're redirected to another page, noaccess.php. The
hint comes from a tweet from Snow Miser:

.. image:: /images/sans-christmas-challenge-2012/snow_miser_tweet_3.png
    :alt: snow_miser_tweet_3.png
    :align: center


The tweeted image is from `the most interesting man in the
world <http://knowyourmeme.com/memes/the-most-interesting-man-in-the-world>`__:

.. image:: /images/sans-christmas-challenge-2012/snow_miser_most_interesting_man.jpg
    :alt: snow_miser_most_interesting_man.jpg
    :align: center


Heat Miser redirects us, using a :code:`header("location: new_url");`, but
forgets to use the :code:`exit` function. It
means that the rest of the page is executed, then sent to our browser,
with a Location header, which our browser follows. But if we use a
client which does not follow redirection, we can recover the first page.

.. code-block:: shell

    $ curl "http://heatmiser.counterhack.com/zone-4-0F2EA639-19BF-40DD-A38D-635E1344C02B/" | grep "zone-5"
    Link to <a href="/zone-5-15614E3A-CEA7-4A28-A85A-D688CC418287/">Zone 5</a>

Zone 4
------

flag: :code:`e3ae414e6d428c3b0c7cff03783e305f`

Okay, we have the URL to zone 5, but when we try to access it directly,
we're redirected again to noaccess.php. To give us a clue about where to
look, Snow Miser tweets:

.. image:: /images/sans-christmas-challenge-2012/snow_miser_tweet_4.png
    :alt: snow_miser_tweet_4.png
    :align: center


So, we know that we should look at the cookies. There's only one:
:code:`UID=b8c37e33defde51cf91e1e03e51657da`. A 32 byte hex string:
it looks like a MD5 hash. If we reverse it (using online tools, or
programs like John The Ripper), we find that it's the hash of the string
"1001", which explains Snow Miser's tweet.

A value like 1001, and a name like UID indicates that this hash
corresponds to a user ID, and an unprivileged one, since he can't access
zone 5. The first value I tried was a UID of 0 (which means a MD5 of
:code:`cfcd208495d565ef66e7dff9f98764da`) since it's root's UID on
Linux, but it turned out that the correct value was 1 (which means a MD5
:code:`c4ca4238a0b923820dcc509a6f75849b`). We modify the cookie's
value, and we reload the page to access zone 5.

Zone 5
------

flag: :code:`f478c549e37fa33467241d847f862e6f`

Game over for Southtown.

Conclusion
==========

I'll give it to you: this challenge wasn't really complicated. Mostly
because the first zones of both controllers where kinda easy, but also
because of all the hints in the tweets. Yet, I'm still glad I did it
because:

- I learned the SVN vulnerability
- I learned common mistakes, like forgetting :code:`exit` after a
  redirect
- I added new tricks to my "to-do" list when looking for
  vulnerability/information disclosure (like the use of steghide, or
  looking at files in docs leaks)

I hoped this wasn't too long, and that you learned something from it. I
wish you a merry Christmas, a happy new year, and lots of pentesting ;)

Cheers.

