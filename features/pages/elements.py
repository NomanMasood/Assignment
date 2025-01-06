############################################################################
"""
    Description:
        | Classes to manage the page/functionalities wise element controls and few variables

"""
############################################################################

class LandingPage:
    items_cmbx_xpath = "//mat-select[@id='mat-select-0']"
    items_cmbx_lstbx_xpath = "//div//mat-option//span[@class='mat-option-text']"
    prod_grids_xpath = "//div//mat-grid-tile"
    prod_disply_range_label_xpath = "//div//div[@class='mat-paginator-range-label']"
    all_prods_xpath = "//img[@role='button']"
    prod_popup_xpath = "//mat-dialog-container"
    rev_sec_xpath = "//mat-expansion-panel-header[contains(., 'Reviews')]"
    exp_rev_sec_xpath = "//div[@role='region']"
    prod_pop_close_btn_xpath = "//span[normalize-space()='Close']"
    lst_sec_ques = ["Your eldest siblings middle name?", "Mother's maiden name?", "Mother's birth date? (MM/DD/YY)",
                    "Father's birth date? (MM/DD/YY)", "Maternal grandmother's first name?",
                    "Paternal grandmother's first name?", "Name of your favorite pet?",
                    "Last name of dentist when you were a teenager? (Do not include 'Dr.')",
                    "Your ZIP/postal code when you were a teenager?", "Company you first work for as an adult?",
                    "Your favorite book?", "Your favorite movie?", "Number of one of your customer or ID cards?",
                    "What's your favorite place to go hiking?"]

class Registration:
    usr_reg_lbl_xpath = "//h1[normalize-space()='User Registration']"
    email_id = "emailControl"
    password_id = "passwordControl"
    rep_password_id = "repeatPasswordControl"
    sec_quest_drop_xpath = "//mat-select[@id='mat-select-0']"
    answer_id = "securityAnswerControl"
    val_err_xpath = "//mat-error"
    pass_adv_css = "input[type='checkbox']"
    pass_adv_tog_xpath = "//span[@class='mat-slide-toggle-thumb-container']"
    pass_adv_expd_sec_xpath = "//mat-card-content//div//span"
    register_btn_xpath = "//button[@id='registerButton']"
    lst_msgs = ['Please provide an email address.', 'Please provide a password.', 'Please repeat your password.',
                'Please select a security question.', 'Please provide an answer to your security question.']
    err_info = ['contains at least one lower character', 'contains at least one upper character',
                'contains at least one digit', 'contains at least one special character',
                'contains at least 8 characters']


class Login:
    email_xpath = "//input[@id='email']"
    pwd_xpath = "//input[@id='password']"
    login_btn_xpath = "//button[@id='loginButton']"

class WelcomePopup:
    welcome_popup_css_sel = "app-welcome-banner[class='ng-star-inserted'] div[class='mat-typography']"
    dismis_btn_xpath = "//span[normalize-space()='Dismiss']"

class Basket:
    add_qty_btn_xpath = "//mat-row[1]//mat-cell[3]//button[2]//span[1]//*[name()='svg']"
    add_sub_qty_btn_xpath = "//mat-row[1]//mat-cell[3]//span[1]"
    qty_btns_xpath = '//mat-row[1]//mat-cell[3]//span[1]'
    your_basket_mm_xpath = "//span[normalize-space()='Your Basket']"
    total_prc_xpath = "//div[@id='price']"
    del_btn_xpath = ("//mat-row[1]//mat-cell[5]//button[1]//span[1]//*[name()='svg']")
    prev_prc_xpath = "//div[@id='price']"
    cart_suc_msg_xpath = "//span[@class='mat-simple-snack-bar-content']"

class Products:
    cart_suc_msg_xpath = "//span[@class='mat-simple-snack-bar-content']"
    add_to_bkt_btn_xpath = "//button[@aria-label='Add to Basket']"
    all_prods_lbl_xpath = "//div[contains(text(),'All Products')]"

class Checkout:
    chk_out_btn_xpath = "//button[@id='checkoutButton']"
    sel_add_rdbox_xpath = "//span[@class='mat-radio-container']"
    add_new_addr_btn_xpath = "//span[normalize-space()='Add New Address']"
    addrs_exp_xpath = "//button[@aria-label='Add a new address']"
    countryf_inp_xpath = "//input[@placeholder='Please provide a country.']"
    namef_inp_xpath = "//input[@placeholder='Please provide a name.']"
    mobf_inp_xpath="//input[@placeholder='Please provide a mobile number.']"
    zipcodef_inp_xpath = "//input[@placeholder='Please provide a ZIP code.']"
    cityf_inp_xpath = "//input[@placeholder='Please provide a city.']"
    statef_inp_xpath = "//input[@placeholder='Please provide a state.']"
    country_inp_xpath = "//input[@id='mat-input-1']"
    name_inp_xpath = "//input[@id='mat-input-2']"
    mob_inp_xpath = "//input[@id='mat-input-3']"
    zipcode_inp_xpath = "//input[@id='mat-input-4']"
    address_inp_xpath = "//textarea[@id='address']"   #Please provide an address.
    city_inp_xpath = "//input[@id='mat-input-6']"
    state_inp_xpath = "//input[@id='mat-input-7']"
    sub_btn_xpath = "//button[@id='submitButton']"
    add_addrs_rdbtn_xpath = "//input[@id='mat-radio-42-input']"
    continue_btn_xpath = "//span[normalize-space()='Continue']"
    delvr_speed_rdbtn_xpath = "//input[@id='mat-radio-43-input']"
    wallet_blnc_xpath = "//span[@class='confirmation card-title']"
    new_card_exp_xpath = "//span[@class='mat-content ng-tns-c41-28']"  #
    add_new_card_xpath = "//mat-expansion-panel-header[@id='mat-expansion-panel-header-0']//span[2]"
    card_name_inp_xpath = "//input[@type='text']"
    card_num_inp_xpath = "//input[@type='number']"
    card_exp_mnt_inp_xpath = "//select"
    card_exp_yr_inp_xpath = "//select"
    sel_added_crd_rdbox_xpath = "//mat-radio-button[@id='mat-radio-46']"
    purc_succ_note_xpath = "//h1[normalize-space()='Thank you for your purchase!']"
    del_speed_rdboxs_xpath = "//span[@class='mat-radio-container']"
    added_card_sel_rdbox_id= "mat-radio-56"
    cart_suc_msg_xpath = "//span[@class='mat-simple-snack-bar-content']"



