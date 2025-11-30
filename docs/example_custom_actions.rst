Example Custom Actions
######################

.. highlight:: python3

We have a new type of action that we've found ourselves writing over and over
again. Our project has a system that allows us to send emails to customers for
things like welcome messages, password resets, and notifications. Sometimes,
though, these messages need to be resent to a customer if they didn't receive
them the first time.

This is what our custom admin action class might look like. We've overridden the
:py:class:`~admin_actions.lib.AdminActionBaseClass.handle_item` method so that
it looks up an email template before calling the provided function to send the
email. We've also overridden the
:py:class:`~admin_actions.lib.AdminActionBaseClass.__init__` method to accept a
new parameter for the email template name.

::

    # actions/send_email.py
    from admin_actions import AdminActionBaseClass
    from some_email_module import get_email_template

    class SendEmailAction(AdminActionBaseClass):
        """An admin action that sends an email to selected users."""

        def __init__(
            self,
            function: Function,
            *,
            email_template: str,
            condition: Condition | None = None,
            name: str | None = None,
        ) -> None:
            super().__init__(function, condition=condition,
                name=name or f"Send Email: {email_template}")
            self.email_template = email_template

        def handle_item(self, user: Model) -> None:
            email_template = get_email_template(self.email_template)
            self.function(to=user.email, template=email_template)


Now we can use our ``SendEmailAction`` class to make actions for our admin
interface. Here's an example of how we might use it to create an action that
sends a welcome email to selected users.

::

    # admin.py
    from .actions.send_email import SendEmailAction
    from some_email_module import send_email
    from myapp.models import User

    class UserAdmin(AdminInterface):
        model = User
        actions = [
            SendEmailAction(
                function=send_email,
                email_template="welcome_email",
                name="Send Welcome Email",
            ),
        ]

With this setup, when an admin selects users in the admin interface and chooses
the "Send Welcome Email" action, the system will send the welcome email template
to each selected user's email address. This makes it easy to resend important
emails without having to write the email-sending logic from scratch each time.
Adding new emails to resend is as simple as creating a new instance of the
``SendEmailAction`` with the desired template name.

::

        actions = [
            SendEmailAction(
                function=send_email,
                email_template="welcome_email",
                name="Send Welcome Email",
            ),
            SendEmailAction(
                function=send_email,
                email_template="password_reset",
                name="Send Password Reset Email",
            ),
        ]

This approach keeps our code DRY (Don't Repeat Yourself) and makes it easy to
manage email-sending actions in our admin interface. It also allows us to easily
control which emails can be resent by simply adding or removing instances of the
``SendEmailAction`` class in any admin. This means we could quickly send a
"Password Reset Email" from our ``users`` admin and also an "Order Shipped"
email from our ``orders`` admin, all while reusing the same action class.