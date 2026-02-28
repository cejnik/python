import smtplib
import requests

response = requests.get("https://api.kanye.rest/")
response.raise_for_status()
data = response.json()



my_email = ""#email ze kterého posílám
password ="" #hesla aplikací
recieved_email = ["danekslama@gmail.com"] #doplnit email
message = f"Subject: Kaney West \n\n{data['quote']}"

with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=recieved_email,
                        msg=message.encode("utf-8")
                        )
    
