import gmail
import imaplib


username = "xxxxx@gmail.com"
password  = "xxxxxx"


mail = imaplib.IMAP4_SSL('imap.gmail.com')#mail = imaplib.IMAP4_SSL('imap.google.com')e04打錯字了
mail.login(username,password)