# test_Project.py

import unittest
from Project import calculate_mean, plot_fathers_education

class TestProjectFunctions(unittest.TestCase):
    def setUp(self):
        # Load your data for testing
        self.student_data = pd.read_csv("students.csv", sep=";")

    def test_calculate_mean(self):
        result = calculate_mean(self.student_data, 'Admission grade')
        self.assertAlmostEqual(result, self.student_data['Admission grade'].mean(), places=2)

    def test_plot_fathers_education(self):
        # Ensure the function does not raise any exceptions
        try:
            plot_fathers_education(self.student_data)
        except Exception as e:
            self.fail(f"plot_fathers_education raised an exception: {e}")

    # Add more test methods for other functions...

if __name__ == '__main__':
    unittest.main()
