from django.conf.urls import url
from . import views

app_name = 'external'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^account/addPaymentRequestToDB/$', views.addPaymentRequestToDB, name='add_merchantPaymentRequest_toDB'),
    url(r'^account/credit/checking/$', views.credit_checking, name='credit_checking'),
    url(r'^account/credit/checking/validate/$', views.credit_checking_validate, name='credit_checking_validate'),
    url(r'^account/credit/savings/$', views.credit_savings, name='credit_savings'),
    url(r'^account/credit/savings/validate/$', views.credit_savings_validate, name='credit_savings_validate'),
    url(r'^account/debit/checking/$', views.debit_checking, name='debit_checking'),
    url(r'^account/debit/checking/validate/$', views.debit_checking_validate, name='debit_checking_validate'),
    url(r'^account/debit/savings/$', views.debit_savings, name='debit_savings'),
    url(r'^account/debit/savings/validate/$', views.debit_savings_validate, name='debit_savings_validate'),
    url(r'^account/email_payment/checking/$', views.payment_email_checking, name='payment_email_checking'),
    url(r'^account/email_payment/savings/$', views.payment_email_savings, name='payment_email_savings'),
    url(r'^account/email_payment_on_behalf/checking/$', views.payment_on_behalf_email_checking, name='payment_on_behalf_email_checking'),
    url(r'^account/email_payment_on_behalf/savings/$', views.payment_on_behalf_email_savings, name='payment_on_behalf_email_savings'),
    url(r'^account/email_transfer/checking/$', views.transfer_email_checking, name='transfer_email_checking'),
    url(r'^account/email_transfer/savings/$', views.transfer_email_savings, name='transfer_email_savings'),
    url(r'^account/payment/checking/$', views.payment_checking, name='payment_checking'),
    url(r'^account/payment/checking/validate/$', views.payment_checking_validate, name='payment_checking_validate'),
    url(r'^account/payment/savings/$', views.payment_savings, name='payment_savings'),
    url(r'^account/payment/savings/validate/$', views.payment_savings_validate, name='payment_savings_validate'),
    url(r'^account/payment_on_behalf/checking/$', views.payment_on_behalf_checking, name='payment_on_behalf_checking'),
    url(r'^account/payment_on_behalf/checking/validate/$', views.payment_on_behalf_checking_validate, name='payment_on_behalf_checking_validate'),
    url(r'^account/payment_on_behalf/savings/$', views.payment_on_behalf_savings, name='payment_on_behalf_savings'),
    url(r'^account/payment_on_behalf/savings/validate/$', views.payment_on_behalf_savings_validate, name='payment_on_behalf_savings_validate'),
    url(r'^account/reject_approvals/$', views.reject_approvals, name='reject_approvals'),
    url(r'^account/request_payment/$', views.request_payment, name='request_payment'),
    url(r'^account/showPaymentRequests/$', views.showPaymentRequests, name='showPaymentRequests'),
    url(r'^account/transfer/checking/$', views.transfer_checking, name='transfer_checking'),
    url(r'^account/transfer/checking/validate/$', views.transfer_checking_validate, name='transfer_checking_validate'),
    url(r'^account/transfer/savings/$', views.transfer_savings, name='transfer_savings'),
    url(r'^account/transfer/savings/validate/$', views.transfer_savings_validate, name='transfer_savings_validate'),
    url(r'^account/update_approvals/$', views.update_approvals, name='update_approvals'),
    url(r'^account/view/checking/$', views.checking_account, name='checking_account'),
    url(r'^account/view/savings/$', views.savings_account, name='savings_account'),
    url(r'^credit_card/$', views.credit_card, name='credit_card'),
    url(r'^error/$', views.error, name='error'),
    url(r'^profile/certificate/add/$', views.add_certificate, name='add_certificate'),
    url(r'^profile/certificate/encrypt/$', views.certificate_encrypt, name='certificate_encrypt'),
    url(r'^profile/certificate/view/$', views.certificate, name='certificate'),
    url(r'^profile/edit/$', views.profile_edit, name='profile_edit'),
    url(r'^profile/edit/validate/$', views.profile_edit_validate, name='profile_edit_validate'),
    url(r'^profile/view/$', views.profile, name='profile'),
]
