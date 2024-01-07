from django.test import TestCase
from django.urls import reverse

class TestUrls(TestCase):

    def test_index_url(self):
        url = reverse('homepage:index')
        self.assertEqual(url, '/')

    def test_about_url(self):
        url = reverse('homepage:about')
        self.assertEqual(url, '/about/')

    def test_volunteering_url(self):
        url = reverse('homepage:volunteering')
        self.assertEqual(url, '/volunteering/')

    def test_projects_url(self):
        url = reverse('homepage:projects')
        self.assertEqual(url, '/projects/')

    def test_tesda_url(self):
        url = reverse('homepage:tesda')
        self.assertEqual(url, '/tesda/')

    def test_donate_url(self):
        url = reverse('homepage:donate')
        self.assertEqual(url, '/donate/')


    # About links
    def test_orgchart_url(self):
        url = reverse('homepage:orgchart')
        self.assertEqual(url, '/about/orgchart')

    def test_visitkfi_url(self):
        url = reverse('homepage:visitkfi')
        self.assertEqual(url, '/about/visitkfi')

    def test_accreditations_url(self):
        url = reverse('homepage:accreditations')
        self.assertEqual(url, '/about/accreditations')

    def test_administration_url(self):
        url = reverse('homepage:administration')
        self.assertEqual(url, '/about/administration')

    def test_manualofoperations_url(self):
        url = reverse('homepage:manualofoperations')
        self.assertEqual(url, '/about/manualofoperations')


    # Volunteering links
    def test_volunteeringapply_url(self):
        url = reverse('homepage:volunteeringapply')
        self.assertEqual(url, '/volunteering/apply')


    # Projects links
    def test_projectsinformation_url(self):
        url = reverse('homepage:projectsinformation')
        self.assertEqual(url, '/projects/information')

    def test_projectspartners_url(self):
        url = reverse('homepage:projectspartners')
        self.assertEqual(url, '/projects/partners')\
        

    # Tesda links
    def test_tesdacoursesoffered_url(self):
        url = reverse('homepage:tesdacoursesoffered')
        self.assertEqual(url, '/tesda/coursesoffered')

    def test_tesdahistory_url(self):
        url = reverse('homepage:tesdahistory')
        self.assertEqual(url, '/tesda/history')

    # DB links
    def test_file_upload_url(self):
        url = reverse('homepage:file_upload')
        self.assertEqual(url, '/db/upload')

    def test_file_list_url(self):
        url = reverse('homepage:file_list')
        self.assertEqual(url, '/db/files')
    
    
    