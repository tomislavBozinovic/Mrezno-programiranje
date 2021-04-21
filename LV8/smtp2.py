import smtplib 

content = 'Bok profesore, kako ste? Molim vas da mi odgovorite na mail, ako ste dobili poruku. Tomislav' 

mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()
mail.starttls()
mail.login('email', 'password')

mail.sendmail('fromEmail', 'toEmail', content)

mail.close()