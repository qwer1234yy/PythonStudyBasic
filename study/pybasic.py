import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        name = 'test#'
        name2 = name.rstrip('#')
        print(name)
    def test_dictionary(self):

        saved_searches = {
            'APC Reimbursement Information-SO': 'Jon_test_PlsDoNotChange_APC',
            'Outpatient Flag Information-SO': 'JonTest_pls_do_not_delete_it',
            'Outpatient Flag Information by Facility-SO': 'JonTest_pls_do_not_delete_it',
            'Evaluation & Management Clinical Profile-SO': 'Jon_test_pls_do_do_change_Evaluation',
            'DRG Listing by Payer-SI': 'Jon_automation_test_pls_do_not_change_it',
            'Present on Admission(POA) Comparison-SI': 'JonTestPlsDoNotChangeItPOA',
            'DRG Contribution to Payer CMI-EI': 'JonTestPlsDoNotChangeItDRG',
            'Security Administration Information by Role-SI': 'JonTestPlsDoNotChangeIt_SAIBR',
            'Inpatient Flag Information-SI': 'JonTestPlsDoNotChangeIt_FlagInfor',
            'Inpatient Flag Information by Facility-SI': 'JonTestPlsDoNotChangeIt_FlagInfor',
        }
        for i in saved_searches.keys():
            print(i)
            print(saved_searches.get(i))


if __name__ == '__main__':
    unittest.main()
