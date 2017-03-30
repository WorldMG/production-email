# Copyright 2016 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
from google.appengine.api import app_identity
from google.appengine.api import mail
from google.appengine.ext.webapp.mail_handlers import BounceNotification
from google.appengine.ext.webapp.mail_handlers import BounceNotificationHandler
import webapp2

#logging.info("==============================")
# [START bounce_handler]
#class LogBounceHandler(BounceNotificationHandler):
#   def receive(self, bounce_message):
#        logging.info('Received bounce post ... [%s]', self.request)
#        logging.info('Bounce original: %s', bounce_message.original)
#        logging.info('Bounce notification: %s', bounce_message.notification)
# [END bounce_handler]


#app = webapp2.WSGIApplication([(r'/_ah/bounce',LogBounceHandler.mapping())], debug=True)

#########################
# [START bounce_handler]
#class MailBounceHandler(BounceNotificationHandler,mail):
#    def receive(self, bounce_message,mail):
#    	logging.info('Received bounce post ... [%s]', self.request)
#        logging.info('Bounce original: %s', bounce_message.original)
#        logging.info('Bounce notification: %s', bounce_message.notification)
#        log1 = 'Received bounce post ... [%s]', self.request
#        log2 = 'Bounce original: %s', bounce_message.original
#        log3 = 'Bounce notification: %s', bounce_message.notification
#        bouncelog = log1+log2+log3
#        mail.send_mail(sender="Lawyer.com Referrals <yding@corp.lawyer.com>",
#		               to="Lawyer.com Support <yding@corp.lawyer.com>",
#		               subject="GAE Referral Email Bounce Notification",
#		               body=bouncelog)
        #return bouncelog
# [END bounce_handler]
#bapp = webapp2.WSGIApplication([MailBounceHandler.mapping()], debug=True)

######################################
#def send_approved_mail(mailcontent):
#    # [START send_mail]
#    mail.send_mail(sender="Lawyer.com Referrals <yding@corp.lawyer.com>",
#                   to="Lawyer.com Support <yding@corp.lawyer.com>",
#                   subject="GAE Referral Email Bounce Notification",
#                   body=mailcontent)
#    # [END send_mail]
#
#class MailBounceHandler(BounceNotificationHandler,webapp2.RequestHandler):
#    def receive(self, bounce_message):
#        logging.info('Received bounce post ... [%s]', self.request)
#        logging.info('Bounce original: %s', bounce_message.original)
#        logging.info('Bounce notification: %s', bounce_message.notification)
#        log1 = 'Received bounce post ... [%s]', self.request
#        log2 = 'Bounce original: %s', bounce_message.original
#        log3 = 'Bounce notification: %s', bounce_message.notification
#        bouncelog = log1+log2+log3
#
#        send_approved_mail(bouncelog)
#        self.response.content_type = 'text/plain'
#        self.response.write('Sent an email to Albert.')
#
#app = webapp2.WSGIApplication([
#    ('/_ah/bounce', MailBounceHandler),
#], debug=True)
######################################

######################################
class LogBounceHandler(BounceNotificationHandler):
    def receive(self, bounce_message):
        mail.send_mail(to='support@corp.lawyer.com', sender='referrals@corp.lawyer.com', subject='Referral Premium - GAE Bounced Email',
                       body=str(self.request))
        logging.info('Received bounce post ... [%s]', self.request)
        logging.info('Bounce original: %s', bounce_message.original)
        logging.info('Bounce notification: %s', bounce_message.notification)

class BounceHandler(webapp2.RequestHandler):
    def post(self):
        bounce = BounceNotification(self.request.POST)
        logging.info('Bounce original: %s', bounce.original)
        logging.info('Bounce notification: %s', bounce.notification)

app = webapp2.WSGIApplication([
    ('/_ah/bounce', LogBounceHandler),
], debug=True)


