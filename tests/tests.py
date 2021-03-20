import random


def generate_email():
    prefix = 'ak' + str(''.join([random.choice(list('qwertyuio')) for x in range(5)]))
    return f"{prefix}@mail.ru"


def generate_name():
    prefix = 'Pug_' + str(''.join([random.choice(list('123456789')) for x in range(2)]))
    return prefix


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


def test_task_9_verify_sort_in_all_countries_list(app):
    """Проверяет сортировку всех стран"""

    admin_form = app.forms.open_admin_form()
    admin_form.login_as_admin()

    admin_form.open_countries_tab()
    admin_form.verify_sort_for_all_country()

    admin_form.verify_sort_zones_in_country()


def test_task_9_verify_sort_for_zone_list_in_country(app):
    """Проверяет сортировку зон в карточке страны"""

    admin_form = app.forms.open_admin_form()
    admin_form.login_as_admin()

    admin_form.open_countries_tab()

    admin_form.verify_sort_zones_in_country()


def test_task_9_verify_sort_zones_in_geo_zone(app):
    """Проверяет сортировку зон в карточке страны на вкладке Geo zone"""
    admin_form = app.forms.open_admin_form()
    admin_form.login_as_admin()

    admin_form.open_geo_zones_tab()
    admin_form.verify_sort_zones_in_geo_zone()


def test_task_10_verify_fields(app):
    """Проверки на главной странице и на странице товара совпадают текст названия товара, акционная и обычная цена"""

    store_form = app.forms.open_store_form()
    store_form.verify_product()


def test_task_10_verify_product_style_on_main_page(app):
    """Проверки стилей акционной и обычной цен продукта на главной странице"""

    store_form = app.forms.open_store_form()

    store_form.verify_regular_price_is_through()
    store_form.verify_regular_price_color_is_gray()
    store_form.verify_campaign_price_color_is_red()
    store_form.verify_campaign_price_color_is_bold()


def test_task_10_verify_product_style_in_product_card(app):
    """Проверки стилей акционной и обычной цен продукта в карточке продукта"""

    store_form = app.forms.open_store_form()

    store_form.open_duck_card()

    store_form.verify_regular_price_color_is_gray_in_card()
    store_form.verify_regular_price_is_through_in_card()
    store_form.verify_campaign_price_color_is_red_in_card()
    store_form.verify_campaign_price_color_is_bold_in_card()


def test_task_10_verify_text_size_on_main_page(app):
    """Проверка размера цен продукта на главной странице"""

    store_form = app.forms.open_store_form()
    store_form.verify_size_of_prices()


def test_task_10_verify_text_size_in_product_card(app):
    """Проверка размера цен продукта в карточке продукта"""

    store_form = app.forms.open_store_form()

    store_form.open_duck_card()

    store_form.verify_size_of_prices_in_card()


def test_task_11(app):
    email = generate_email()
    password = "Qwe12345"

    new_user_form = app.forms.open_new_user_form()
    new_user_form.create_user(email, password)
    app.forms.store_form.logout()

    app.forms.store_form.login(email, password)


def test_task_12(app):
    product_name = generate_name()

    admin_form = app.forms.open_admin_form()
    admin_form.login_as_admin()

    new_product_form = app.forms.open_new_product_form()
    new_product_form.fill_form(product_name)

    admin_form.verify_product_presents(product_name)


def test_task_13(app):

    store_form = app.forms.open_store_form()
    store_form.add_products_to_cart()

    store_form = app.forms.open_store_form()
    store_form.add_products_to_cart()

    store_form = app.forms.open_store_form()
    store_form.add_products_to_cart()

    store_form.open_cart()

    store_form.remove_all_products()
    # store_form.remove_product()
    # store_form.remove_product()
    # store_form.remove_product()


def test_task_14(app):
    admin_form = app.forms.open_admin_form()
    admin_form.login_as_admin()

    admin_form.open_countries_tab()
    admin_form.open_new_country_form()
    admin_form.open_all_external_links()


def test_task_17(app):
    admin_form = app.forms.open_admin_form()
    admin_form.login_as_admin()

    admin_form.open_catalog_tab()
    admin_form.get_browser_log()

