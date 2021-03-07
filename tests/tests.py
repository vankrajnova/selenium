def test_login(app):
    admin_form = app.forms.open_admin_form()
    admin_form.login_as_admin()


def test_task_7(app):
    admin_form = app.forms.open_admin_form()
    admin_form.login_as_admin()

    admin_form.click_all_menu_buttons()


def test_task_8(app):
    store_form = app.forms.open_store_page()
    store_form.verify_products_has_one_sticker()
