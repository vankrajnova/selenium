import random


def generate_email():
    prefix = 'ak' + str(''.join([random.choice(list('qwertyuio')) for x in range(5)]))
    return f"{prefix}@mail.ru"


def test_login(app):
    admin_form = app.forms.open_admin_form()
    admin_form.login_as_admin()


def test_task_7(app):
    admin_form = app.forms.open_admin_form()
    admin_form.login_as_admin()

    admin_form.click_all_menu_buttons()


def test_task_8(app):
    store_form = app.forms.open_store_form()
    store_form.verify_products_has_one_sticker()


def test_task_11(app):
    email = generate_email()
    password = "Qwe12345"

    new_user_form = app.forms.open_new_user_form()
    new_user_form.create_user(email, password)
    app.forms.store_form.logout()

    app.forms.store_form.login(email, password)


def test_task_12(app):
    """"""



