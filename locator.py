class Locator:
    deepset_url = 'https://annotate.deepset.ai/login'

    email_id = 'email'
    password_id = 'password'

    login_button_path = '//div[@class="ant-spin-nested-loading"]//button[1]'

    projects_heading_path = "//div[@class='styles_title__3xSDk']//h1"

    create_project_button_path = "//div[@class='styles_title__3xSDk']//button[1]"

    project_name_placeholder_id = "name"
    final_create_project_button = "//div[@class='ant-modal-body']//button[1]"

    project_created_row_path = "//tbody[@class='ant-table-tbody']/tr"

    delete_project_icon = '//div[@class="styles_buttons__1DWZI"]//i[@class="icon-delete"]'

    icon_arrow_right = '//div[@class="styles_buttons__1DWZI"]//i[@class="icon-arrow-right"]'

    yes_span_to_delete_pjt = '//div[@class="ant-popover-buttons"]//span[text()="Yes"]'

    documents_heading = '//div[@class="styles_title__3MfC7"]//h1[@class = "h2"]'
    documents_tab = '//*[@id="root"]/div/header/div[2]/ul/li[4]/a'

    import_xpath = '//*[@id="item_3$Menu"]/li[1]/a'
    import_menu = '//*[@id="root"]/div/header/div[2]/ul/li[8]/div/span'

    upload_icon = '//p[@class="ant-upload-drag-icon"]//i'

    input_icon = "//input[@type='file']"

    projects_table = '//tbody[@class="ant-table-tbody"]'
