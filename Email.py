import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from textwrap import dedent

__author__ = 'YU Yang, JAIST'

class Email():
    def __init__(self, my_address, my_password):
        # Set sender address and password.
        self.my_address = my_address
        self.my_password = my_password
    
    def send(self, donor_address):

        HOST_ADDRESS = 'smtp.gmail.com'   # Gmail Outgoing Mail (SMTP) Server
        HOST_PORT = 587   # Port for TLS/STARTTLS: 587

        # Connection with the server
        server = smtplib.SMTP(host = HOST_ADDRESS, port = HOST_PORT)
        server.starttls()
        server.login(self.my_address, self.my_password)

        # Creation of the MIMEMultipart Object
        message = MIMEMultipart()

        # Setup of MIMEMultipart Object Header
        message['From'] = self.my_address
        message['To'] = donor_address
        message['Subject'] = "Automated THANK-YOU email by YU Yang(ver. Dec 21st)"

        # Creation of a MIMEText Part
        
        ThanksMessage = '''\
        Dear Mr. and Ms. 

        Thank you for your generous contribution to Let's Support Sagorika (LSS) campaign. Your donation and goodwill enable us to collect a sufficient fund to support Sagorika who has been suffering from Acute Lymphoblastic Leukemia. You have truly made a positive difference in Sagorika, her family, and JAIST community, and we are extremely grateful.

        Your donation will be sent to Sagorika and her family to help them cover the medical costs. Should you have any questions about how your money will be used or about Let's Support Sagorika campaign, please do not hesitate to contact a founder of this campaign, Prof. Shungo Kawanishi (s-kawani@jaist.ac.jp) or Dr. Kotona Motoyama (kotona@jaist.ac.jp).

        We really appreciate your invaluable contribution and cooperation.

        Sincerely yours,
        LSS Collaborators


        サゴリカさんを支援する会の募金活動にご協力いただいた方々へ

        この度は、サゴリカさんを支援する会 (LSS)にご協力いただき誠にありがとうございます。暖かいお心遣いとご支援を承り、心より感謝申し上げます。皆様のご寄付のおかげで、白血病のため闘病生活をされているサゴリカさんへの支援がかないます。皆様のご支援が、サゴリカさん、ご家族、そしてJAISTにおける積極的な変化に繋がっていると思っております。本当にありがとうございました。

        募金活動で集めた寄付金は、サゴリカさんやそのご家族に送られ、治療費として使用されます。寄付金の使い道に関してや、LSSに関して、何かご質問がありましたら、LSSの発起人のメンバーである川西俊吾特任教授（s-kawani@jaist.ac.jp）か元山琴菜講師（kotona@jaist.ac.jp）にご連絡ください。

        この度は、本当にありがとうございました。

        LSSメンバー
        ''' 
        
        textPart = MIMEText(dedent(ThanksMessage), 'plain')

        # Part attachment
        message.attach(textPart)

        # Send Email and close connection
        server.send_message(message)
        server.quit()
        
        print("[{}] Mail Status: Sent!".format(donor_address))
        
    
    # def __str__(self):
    #     for i in range(len(self.email)):
    #         return self.email[i]
    

def main():
    
    Sender_ADDRESS = "helping.sagorika.jaist@gmail.com" # Address
    Sender_PASSWORD = "" # Password
    
    My_JAIST = Email(Sender_ADDRESS, Sender_PASSWORD)
    
    My_JAIST.send("sXXXXXXX@jaist.ac.jp") # Testing
        
    
if __name__ == "__main__":
    main()