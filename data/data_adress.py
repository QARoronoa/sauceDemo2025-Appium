from faker import Faker
faker = Faker(locale="fr_Fr")

class Adress:

    @staticmethod
    def adress_form():
        return{
            "fullName" : faker.name(),
            "adressLine1": faker.address(),
            "city": faker.city(),
            "zipCode": faker.postcode(),
            "country": faker.country()
        }

    @staticmethod
    def payment_form():
        return {
            "fullName": faker.name(),
            "cardNumber": faker.credit_card_number(),
            "expirationDate": faker.credit_card_expire(),
            "securityCode": faker.credit_card_security_code()
        }