Meet beautiful XSS in your area: a YouPorn bug bounty [SFW]
===========================================================
:date: 2017-03-28
:author: useless
:category: Bug bounty
:slug: meet-beautiful-xss-in-your-area-a-youporn-bug-bounty-sfw

.. role:: strike
    :class: strike

.. image:: /images/meet-beautiful-xss-in-your-area-a-youporn-bug-bounty-sfw/youporn_logo.png
    :alt: youporn_logo.png
    :align: center

I don't do bug bounties due to a lack of time. Although I have a `HackerOne
profile <https://hackerone.com/the-useless-one>`__, you can see that I'm not so
active. However, `a coworker of mine <https://hackerone.com/myst404>`__ spends
quite some time on different bug bounty programs.

On 2017-02-06 evening, when we were both connected to our work Jabber server,
he told me that YouPorn had launched their `bug bounty program on HackerOne
<https://hackerone.com/youporn>`__:

    him: youporn bug bounty launched today btw

    me: on hacker one?

    him: yes

    me: no time, i'm migrating my DNS servers

As I was reading documentation on bind, he wrote me back:

    him: oh shit, exploitable XSS in the search bar, can't believe it

Now, things were interesting! I had to hop in. I was also surprised that
nobody had ever found it before. XSS in the search form is the base case.
:strike:`I often go to` errr, some of my friends often go to YouPorn, and
they've never found such a vulnerability on it before.

Time was of the essence, because we wanted to have a working exploit and report
it before someone else did.

From lack of filtering to open redirect
---------------------------------------

I fired up my browser and Burp, and sent a request on the search form. I
searched for :code:`foobar"`. As you can see in the following screenshot,
the search term is output, without any filtering (except for the capitalization)
in a `meta tag <https://www.w3schools.com/tags/tag_meta.asp>`__:

.. image:: /images/meet-beautiful-xss-in-your-area-a-youporn-bug-bounty-sfw/first_payload.png
    :alt: first_payload.png
    :align: center

However, when we tried to close the meta tag, and open another one, to put
our Javascript payload, we couldn't get it to work:

.. image:: /images/meet-beautiful-xss-in-your-area-a-youporn-bug-bounty-sfw/first_fail.png
    :alt: first_fail.png
    :align: center

Disappointed, we still decided to exploit the meta HTML tag. It's a powerful
tag, because it has the :code:`http-equiv` directive. `This directive
<https://www.w3schools.com/tags/att_meta_http_equiv.asp>`__ allows
you to define the equivalent of an HTTP header in the HTML code.

The :code:`http-equiv` directive can take a value of :code:`refresh`, which
can be used to redirect a user to another page. This kind of `open redirect
<https://www.owasp.org/index.php/Unvalidated_Redirects_and_Forwards_Cheat_Sheet>`__
vulnerability can be very useful in case of a phishing attack:

1. You send someone a link to http://youporn.com, with your payload;
2. Your payload redirects them to a site you control, imitating YouPorn's CSS;
3. You ask them for their credentials, their credit card number, etc.

We put the following payload to test our vulnerability:

.. image:: /images/meet-beautiful-xss-in-your-area-a-youporn-bug-bounty-sfw/second_fail.png
    :alt: second_fail.png
    :align: center

As you can see, there is a slight problem: the dash in :code:`http-equiv`
is not inserted in the source code. I decided to use some XSS voodoo bypass,
and so, I decided to HTML encode, then URL encode the dash.

A dash, :code:`-`, HTML-encoded is :code:`&#45;`, which, URL-encoded, is
:code:`%26%2345%3b`:

.. image:: /images/meet-beautiful-xss-in-your-area-a-youporn-bug-bounty-sfw/first_success.png
    :alt: first_success.png
    :align: center

Boom, we now had a working payload, and were able to redirect users to a
URL of our choosing. Sweet!

Marked as duplicate
-------------------

Just as I had found the correct syntax, my coworker, who had already notified
YouPorn, got the following answer:

    In fact, this was reported already, **but the original reporter did not
    provide a working exploit**.  What I should do is to close it as duplicate,
    because the original  bug was already reported. However **I will leave it
    open so you have a  chance to provide a working payload**.  Note that the
    original ticket was triaged. If you find a working  payload, I will triage
    your ticket as well as you managed to go further  in the exploitation.

    Thanks and happy hacking

From open redirect to full reflective XSS
-----------------------------------------

So that was it, somebody had already reported the vulnerability. However,
YouPorn had kindly decided to let the report open, so that we could find a
working payload, and we already had one with the open redirect payload.

But then I thought "Wait a second, maybe I can use the same trick to put
:code:`>` and :code:`<` instead of a dash!"

And indeed, it worked. With the "HTML-encode-then-URL-encode" trick, we could
insert arbitrary Javascript:

.. image:: /images/meet-beautiful-xss-in-your-area-a-youporn-bug-bounty-sfw/second_success.png
    :alt: second_success.png
    :align: center

Obligatory pop-up:

.. image:: /images/meet-beautiful-xss-in-your-area-a-youporn-bug-bounty-sfw/w00t.png
    :alt: w00t.png
    :align: center

We continued to do some tests afterwards, and we found out something weird
about YouPorn's HTML rendering: no matter how many recursions of HTML-encoding
we did on our payloads, they were still fully decoded server-side. This means
that:

* :code:`&lt;` became :code:`<`
* :code:`&amp;lt;` also became :code:`<`
* :code:`&amp;amp;lt;` **also** became :code:`<`
* etc.

Weird behaviour, but very interesting to bypass some filters!

Anyway, I still have to migrate my DNS servers.

Timeline (YYYY-MM-DD)
---------------------

* **2017-02-06**: Report sent to YouPorn
* **2017-02-06**: Response from YouPorn saying that this bug was already
  reported, but that we could keep trying to find a working payload
* **2017-02-06**: Working payload sent to YouPorn
* **2017-02-06**: Report triaged
* **2017-02-10**: Bounty paid, $250
* **2017-02-03**: Bug fixed
* **2017-03-04**: Request to disclose publicly the report
* **2017-03-28**: Public disclosure of the `report <https://hackerone.com/reports/203974>`__
  granted

