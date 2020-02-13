'''
Created on 21-Oct-2019

@author: hemasunder.g
'''
from Utilities import utilities as utils
from selenium.webdriver.support.select import Select

class Registration:
   
    def __init__(self, driver):
        self.driver = driver
        self.driver.mainframe_id = "topFrame"
        self.driver.borrower_linktext = "Borrower"
        self.driver.mainFrame_id = "mainFrame"
        self.driver.registration_linktext = "Registration"
        self.driver.bdyLoadframe_id = "bdyLoad"
        self.driver.ssn1_textbox_name = "ssn1"
        self.driver.ssn2_textbox_name = "ssn2"
        self.driver.ssn3_textbox_name = "ssn3"
        self.driver.ssn4_textbox_name = "ssn4"
        self.driver.ssn5_textbox_name = "ssn5"
        self.driver.ssn6_textbox_name = "ssn6"
        self.driver.lastname_textbox_name = "customerBean.lastNm"
        self.driver.firstname_textbox_name = "customerBean.firstNm"
        self.driver.address_textbox_name = "customerBean.addressLn"
        self.driver.city_textbox_name = "customerBean.city"
        self.driver.state_dropdown_name = "customerBean.stateCd"
        self.driver.zipcode_textbox_name = "customerBean.postalCd"
        self.monthsataddress_textbox_name = "customerBean.monthsAtAddress"
        self.phonenbr1_textbox_name = "phoneNbr1"
        self.phonenbr2_textbox_name = "phoneNbr2"
        self.phonenbr3_textbox_name = "phoneNbr3"
        self.phonetype_dropdown_name = "customerBean.phoneCd"
        self.donthaveemail_checkbox_name = "customerBean.isCustomerEmailQuest"
        self.photoidnbr_textbox_name = "customerBean.driversLicNbr"
        self.idstate_dropdown_name = "customerBean.driversLicSt"
        self.idexpiredate_textbox_name = "dlexpiry1"
        self.idexpiredatemonth_textbox_name = "dlexpiry2"
        self.idexpiredateyear_textbox_name = "dlexpiry3"
        self.photoidtype_dropdown_name = "customerBean.photoIdType"
        self.idzipcode_textbox_name = "customerBean.drivingZipcode"
        self.dobday_textbox_name = "dob1"
        self.dobmonth_textbox_name = "dob2"
        self.dobyear_textbox_name = "dob3"
        self.incometype_dropdown_name = "customerBean.incomeCdDisp"
        self.employer_textbox_name = "customerBean.empNmDisp"
        self.employeestatus_dropdown_name = "customerBean.roomEmpStatus"
        self.workphone1_textbox_name = "workPhoneNbrDisp1"
        self.workphone2_textbox_name = "workPhoneNbrDisp2"
        self.workphone3_textbox_name = "workPhoneNbrDisp3"
        self.workphoneext_textbox_name = "customerBean.extw"
        self.netincome_textbox_name = "customerBean.incomeAmtDisp"
        self.grossincome_textbox_name = "customerBean.grossAmtDisp"
        self.payfrequency_dropdown_name = "customerBean.payFreqCdDisp"
        self.whichday_dropdown_name = "customerBean.monthlyDate"
        self.friday_radiobtn_id = "rad_wk6"
        self.whichtwodays_radiobtn_id = "rad_semi2"
        self.paystubrevdate_textbox_name = "payStubReviewed1"
        self.paystubrevmonth_textbox_name = "payStubReviewed2"
        self.paystubrevyear_textbox_name = "payStubReviewed3"
        self.paystubdate_textbox_name = "payStubDate1"
        self.paystubmonth_textbox_name = "payStubDate2"
        self.paystubyear_textbox_name = "payStubDate3"
        self.hiredate_textbox_name = "hireDate1"
        self.hiremonth_textbox_name = "hireDate2"
        self.hireyear_textbox_name = "hireDate3"
        self.directdep_dropdown_name = "customerBean.directDeposit"
        self.accountverificationdate_textbox_name = "statementEndDtDisp1"
        self.accountverificationmonth_textbox_name = "statementEndDtDisp2"
        self.accountverificationyear_textbox_name = "statementEndDtDisp3"
        self.abanbr_textbox_name = "customerBean.abaNbrDisp"
        self.confirm_abanbr_textbox_name = "checkAbaNbrDisp"
        self.chngacntnbr_textbox_name = "customerBean.accountNbrDisp"
        self.confirm_chngacntnbr_textbox_name = "checkAccountNbrDisp"
        self.ref1_lastname_textbox_name = "customerBean.contName"
        self.ref1_firstname_textbox_name = "customerBean.contactFirstName"
        self.ref1_phone1_textbox_name = "cphoneNbrDisp1"
        self.ref1_phone2_textbox_name = "cphoneNbrDisp2"
        self.ref1_phone3_textbox_name = "cphoneNbrDisp3"
        self.ref1_relationship_dropdown_name = "customerBean.contactrelationDisp"
        self.ref2_lastname_textbox_name = "customerBean.nameDispSummary"
        self.ref2_firstname_textbox_name = "customerBean.referenceFirstNameSummary"
        self.ref2_relationship_dropdown_name = "customerBean.relationDispSummary"
        self.ref2_phone1_textbox_name = "refPhoneNbr1"
        self.ref2_phone2_textbox_name = "refPhoneNbr2"
        self.ref2_phone3_textbox_name = "refPhoneNbr3"
        self.addreference_btn_name = "bt_Reference"
        self.bankrupt_dropdown_name = "customerBean.bankrupty"
        self.oper_email_optout_radiobtn_id = "oprRadioEmailOptOut"
        self.oper_sms_optout_radiobtn_id = "oprRadioSmsOptOut"
        self.oper_autocalls_optout_radiobtn_id = "oprRadioAutoCallOptOut"
        self.mark_email_optout_radiobtn_id = "marRadioEmailOptOut"
        self.mark_sms_optout_radiobtn_id = "marRadioSmsOptOut"
        self.mark_autocalls_optout_radiobtn_id = "marRadioAutoCallOut"
        self.mark_mail_optout_radiobtn_id = "marRadioMailOptOut"
        self.savenext_btn_xpath = "//input[@value='Save & Next > ']"
        self.getbocode_xpath = "//td[@class='subHeading']//b"
        
    def registration(self):
        self.driver.switch_to.frame(self.driver.mainframe_id)
        self.driver.find_element_by_link_text(self.driver.borrower_linktext).click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.mainFrame_id)
        self.driver.find_element_by_link_text(self.driver.registration_linktext).click()
        self.driver.switch_to.frame(self.driver.bdyLoadframe_id)
        self.driver.find_element_by_name(self.driver.ssn1_textbox_name).send_keys(utils.ssn1)
        self.driver.find_element_by_name(self.driver.ssn2_textbox_name).send_keys(utils.ssn2)
        self.driver.find_element_by_name(self.driver.ssn3_textbox_name).send_keys(utils.ssn3)
        self.driver.find_element_by_name(self.driver.ssn4_textbox_name).send_keys(utils.ssn1)
        self.driver.find_element_by_name(self.driver.ssn5_textbox_name).send_keys(utils.ssn2)
        self.driver.find_element_by_name(self.driver.ssn6_textbox_name).send_keys(utils.ssn3)
        self.driver.find_element_by_name(self.driver.lastname_textbox_name).send_keys(utils.lastname)
        self.driver.find_element_by_name(self.driver.firstname_textbox_name).send_keys(utils.firstname)
        self.driver.find_element_by_name(self.driver.address_textbox_name).send_keys("109 avenue")
        self.driver.find_element_by_name(self.driver.city_textbox_name).send_keys("NewYorkCity")
        state_dd = self.driver.find_element_by_name(self.driver.state_dropdown_name)
        Select(state_dd).select_by_visible_text(utils.state_dd)
        zipcode = self.driver.find_element_by_name(self.driver.zipcode_textbox_name)
        if utils.state_dd == "Kansas":
            zipcode.send_keys("66210")
        elif utils.state_dd == "Missouri":
            zipcode.send_keys("63010")
        self.driver.find_element_by_name(self.monthsataddress_textbox_name).send_keys("12")
        self.driver.find_element_by_name(self.phonenbr1_textbox_name).send_keys("984")
        self.driver.find_element_by_name(self.phonenbr2_textbox_name).send_keys("154")
        self.driver.find_element_by_name(self.phonenbr3_textbox_name).send_keys("1000")
        phonetype_dd = self.driver.find_element_by_name(self.phonetype_dropdown_name)
        Select(phonetype_dd).select_by_visible_text("Home")
        self.driver.find_element_by_name(self.donthaveemail_checkbox_name).click()
        self.driver.find_element_by_name(self.photoidnbr_textbox_name).send_keys(utils.photoidNbr)
        idstate_dd = self.driver.find_element_by_name(self.idstate_dropdown_name)
        Select(idstate_dd).select_by_visible_text(utils.state_dd)
        self.driver.find_element_by_name(self.idexpiredate_textbox_name).send_keys(utils.day)
        self.driver.find_element_by_name(self.idexpiredatemonth_textbox_name).send_keys(utils.month)
        self.driver.find_element_by_name(self.idexpiredateyear_textbox_name).send_keys(utils.IDExpire_year)
        photoidtype_dd = self.driver.find_element_by_name(self.photoidtype_dropdown_name)
        Select(photoidtype_dd).select_by_visible_text("Driver License")
        idzipcode = self.driver.find_element_by_name(self.idzipcode_textbox_name)
        if utils.state_dd == "Kansas":
            idzipcode.send_keys("66210")
        elif utils.state_dd == "Missouri":
            idzipcode.send_keys("63010")
        self.driver.find_element_by_name(self.dobday_textbox_name).send_keys(utils.day)
        self.driver.find_element_by_name(self.dobmonth_textbox_name).send_keys(utils.month)
        self.driver.find_element_by_name(self.dobyear_textbox_name).send_keys(utils.DOBYear)
        incometype_dd = self.driver.find_element_by_name(self.incometype_dropdown_name)
        Select(incometype_dd).select_by_visible_text("Salary")
        self.driver.find_element_by_name(self.employer_textbox_name).send_keys("VTL")
        employee_dd = self.driver.find_element_by_name(self.employeestatus_dropdown_name)
        Select(employee_dd).select_by_visible_text("Active")
        self.driver.find_element_by_name(self.workphone1_textbox_name).send_keys("315")
        self.driver.find_element_by_name(self.workphone2_textbox_name).send_keys("312")
        self.driver.find_element_by_name(self.workphone3_textbox_name).send_keys("3122")
        self.driver.find_element_by_name(self.workphoneext_textbox_name).send_keys("3")
        self.driver.find_element_by_name(self.netincome_textbox_name).send_keys(utils.netincome)
        self.driver.find_element_by_name(self.grossincome_textbox_name).send_keys(utils.grossincome)
        payfrequency_dd = self.driver.find_element_by_name(self.payfrequency_dropdown_name)
        Select(payfrequency_dd).select_by_visible_text(utils.Pay_freq)
        if utils.Pay_freq == "Monthly":
            whichday_dd = self.driver.find_element_by_name(self.whichday_dropdown_name)
            Select(whichday_dd).select_by_visible_text("Last Day")
        elif utils.Pay_freq == "Bi-Weekly":
            fridayradio_btn = self.driver.find_element_by_name(self.friday_radiobtn_id)
            fridayradio_btn.click()
        elif utils.Pay_freq == "Semi-Monthly":
            whichtwodays_radio = self.driver.find_element_by_name(self.whichtwodays_radiobtn_id)
            whichtwodays_radio.click()
        elif utils.Pay_freq == "Weekly":    
            fridayradio_btn.click()
        self.driver.find_element_by_name(self.paystubrevdate_textbox_name).send_keys(utils.day)
        self.driver.find_element_by_name(self.paystubrevmonth_textbox_name).send_keys(utils.month)
        self.driver.find_element_by_name(self.paystubrevyear_textbox_name).send_keys(utils.year)
        self.driver.find_element_by_name(self.paystubdate_textbox_name).send_keys(utils.day)
        self.driver.find_element_by_name(self.paystubmonth_textbox_name).send_keys(utils.month)
        self.driver.find_element_by_name(self.paystubyear_textbox_name).send_keys(utils.year)
        self.driver.find_element_by_name(self.hiredate_textbox_name).send_keys(utils.day)
        self.driver.find_element_by_name(self.hiremonth_textbox_name).send_keys(utils.month)
        self.driver.find_element_by_name(self.hireyear_textbox_name).send_keys(utils.year)
        directdep_dd = self.driver.find_element_by_name(self.directdep_dropdown_name)    
        Select(directdep_dd).select_by_visible_text("No")
        self.driver.find_element_by_name(self.accountverificationdate_textbox_name).send_keys(utils.day)
        self.driver.find_element_by_name(self.accountverificationmonth_textbox_name).send_keys(utils.month)
        self.driver.find_element_by_name(self.accountverificationyear_textbox_name).send_keys(utils.year)
        self.driver.find_element_by_name(self.abanbr_textbox_name).send_keys("111111118")
        self.driver.find_element_by_name(self.confirm_abanbr_textbox_name).send_keys("111111118")
        self.driver.find_element_by_name(self.chngacntnbr_textbox_name).send_keys(utils.checking_acnt_nbr)
        self.driver.find_element_by_name(self.confirm_chngacntnbr_textbox_name).send_keys(utils.checking_acnt_nbr)
        self.driver.find_element_by_name(self.ref1_lastname_textbox_name).send_keys("Rajni")
        self.driver.find_element_by_name(self.ref1_firstname_textbox_name).send_keys("Kanth")
        ref1relation_dd = self.driver.find_element_by_name(self.ref1_relationship_dropdown_name)
        Select(ref1relation_dd).select_by_visible_text("Spouse")
        self.driver.find_element_by_name(self.ref1_phone1_textbox_name).send_keys("145")
        self.driver.find_element_by_name(self.ref1_phone2_textbox_name).send_keys("751")
        self.driver.find_element_by_name(self.ref1_phone3_textbox_name).send_keys("1450")
        self.driver.find_element_by_name(self.ref2_lastname_textbox_name).send_keys("Sonam")
        self.driver.find_element_by_name(self.ref2_firstname_textbox_name).send_keys("Kapoor")
        ref2relation_dd = self.driver.find_element_by_name(self.ref2_relationship_dropdown_name)
        Select(ref2relation_dd).select_by_visible_text("Child")
        self.driver.find_element_by_name(self.ref2_phone1_textbox_name).send_keys("345")
        self.driver.find_element_by_name(self.ref2_phone2_textbox_name).send_keys("551")
        self.driver.find_element_by_name(self.ref2_phone3_textbox_name).send_keys("1458")
        self.driver.find_element_by_name(self.addreference_btn_name).click()
        bankrupt_dd = self.driver.find_element_by_name(self.bankrupt_dropdown_name)
        Select(bankrupt_dd).select_by_visible_text("No")    
        self.driver.find_element_by_id(self.oper_email_optout_radiobtn_id).click()
        self.driver.find_element_by_id(self.oper_sms_optout_radiobtn_id).click()
        self.driver.find_element_by_id(self.oper_autocalls_optout_radiobtn_id).click()
        self.driver.find_element_by_id(self.mark_email_optout_radiobtn_id).click()
        self.driver.find_element_by_id(self.mark_sms_optout_radiobtn_id).click()
        self.driver.find_element_by_id(self.mark_autocalls_optout_radiobtn_id).click()
        self.driver.find_element_by_id(self.mark_mail_optout_radiobtn_id).click()
        self.driver.find_element_by_xpath(self.savenext_btn_xpath).click()
#         bo_code = self.driver.find_element_by_xpath(self.getbocode_xpath).getAttribute()
#         print("bo_code is ", bo_code)
        print("Borrower registration has been completed successfully")