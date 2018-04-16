from unittest import TestCase, main


class TestRecordValidation(TestCase):
    def test_validateId(self):
        from app import RecordValidation as rv
        self.assertEqual( rv.validateId("19872983792"), "Id is not 8 digits or is not positive")
        self.assertEqual(rv.validateId("100000000"),"Id is not 8 digits or is not positive")


    def test_validateName(self):
        from app import RecordValidation as rv
        self.assertEqual(rv.validateName("John"), None)
        self.assertEqual(rv.validateName("JohnJacobJingleheimerSchmidt"),"name length invalid")
        self.assertNotEqual(rv.validateName(None), None)


    def test_validateMidName(self):
        from app import RecordValidation as rv
        self.assertEqual(rv.validateMidName("John"), None)
        self.assertEqual(rv.validateMidName("JohnJacobJingleheimerSchmidt"),"middle name too long")
        self.assertEqual(rv.validateMidName(None), None)

    def test_validatePhoneNumber(self):
        from app import RecordValidation as rv
        self.assertEqual(rv.validatePhoneNumber("907-256-0987"), None)
        self.assertNotEqual(rv.validatePhoneNumber("+1-904-256-0987"),None)
        self.assertEqual(rv.validatePhoneNumber("1-904-256-0987"), "phone number has too many groups")
        self.assertEquals(rv.validatePhoneNumber("000"), "phone number has too few groups")
        self.assertEquals(rv.validatePhoneNumber("9907-256-0987"),"Area code invalid")
        self.assertEquals(rv.validatePhoneNumber("9907-2s6-098a"), "some phone number values not digits")



if __name__ == '__main__':
    main()