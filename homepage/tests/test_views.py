from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from homepage.models import Stories

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.superuser = User.objects.create_superuser(username='admin', email='admin@example.com', password='adminpassword')
        """
        self.test_story = Stories.objects.create(
            title='Test Story',
            content='This is a test story.',
            category='test_category',
            slug='test-slug'
            # Add any other fields you need
        )
        """
        self.index_url = reverse('homepage:index')
        self.about_url = reverse('homepage:about')
        self.volunteering_url = reverse('homepage:volunteering')
        self.projects_url = reverse('homepage:projects')
        self.tesda_url = reverse('homepage:tesda')
        self.donate_url = reverse('homepage:donate')

        self.orgchart_url = reverse('homepage:orgchart')
        self.visitkfi_url = reverse('homepage:visitkfi')
        self.accreditations_url = reverse('homepage:accreditations')
        self.administration_url = reverse('homepage:administration')
        self.manualofoperations_url = reverse('homepage:manualofoperations')

        self.projectsinformation_url = reverse('homepage:projectsinformation')
        self.projectspartners_url = reverse('homepage:projectspartners')

        self.tesdahistory_url = reverse('homepage:tesdahistory')
        self.tesdacoursesoffered_url = reverse('homepage:tesdacoursesoffered')

        self.volunteeringapply_url = reverse('homepage:volunteeringapply')

        self.file_upload_url = reverse('homepage:file_upload')
        self.file_list_url = reverse('homepage:file_list')


        """
        self.stories_create_url = reverse('homepage:stories_create')
        self.stories_list_url = reverse('homepage:stories_list')
        self.stories_detail_url = reverse('homepage:stories_detail')
        self.stories_update_url = reverse('homepage:stories_update')
        self.stories_delete_url = reverse('homepage:stories_delete')
        

    def tearDown(self):
        # Cleanup: Delete the temporary story object
        self.test_story.delete()
        """
        
    # Main navigations
    def test_index_GET(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage.html')  

    def test_about_GET(self):
        response = self.client.get(self.about_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')  

    def test_volunteering_GET(self):
        response = self.client.get(self.volunteering_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'volunteering.html')  

    def test_projects_GET(self):
        response = self.client.get(self.projects_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects.html')  

    def test_tesda_GET(self):
        response = self.client.get(self.tesda_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tesda.html')  

    def test_donate_GET(self):
        response = self.client.get(self.donate_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'donate.html')  

    
    # About links
    def test_orgchart_GET(self):
        response = self.client.get(self.orgchart_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/orgchart.html')  
    
    def test_visitkfi_GET(self):
        response = self.client.get(self.visitkfi_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/visitkfi.html')  
    
    def test_accreditations_GET(self):
        response = self.client.get(self.accreditations_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/accreditations.html')  
    
    def test_manualofoperations_GET(self):
        self.client.force_login(self.superuser)
        response = self.client.get(self.manualofoperations_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/manualofoperations.html')  

    def test_administration_GET(self):
        response = self.client.get(self.administration_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/administration.html')  
    
        
    # Projects links
    def test_projectsinformation_GET(self):
        response = self.client.get(self.projectsinformation_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/information.html')  

    def test_projectspartners_GET(self):
        response = self.client.get(self.projectspartners_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/partners.html')


    # TESDA links
    def test_tesdacoursesoffered_GET(self):
        response = self.client.get(self.tesdacoursesoffered_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tesda/coursesoffered.html')  

    def test_tesdahistory_GET(self):
        response = self.client.get(self.tesdahistory_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tesda/history.html')  


    # Volunteering links
    def test_volunteeringapply_GET(self):
        response = self.client.get(self.volunteeringapply_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'volunteering/apply.html')  


    # DB links
    def test_file_upload_GET(self):
        self.client.force_login(self.superuser)
        response = self.client.get(self.file_upload_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'db/file_upload.html')  
    
    def test_file_list_GET(self):
        self.client.force_login(self.superuser)
        response = self.client.get(self.file_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'db/file_list.html')
        
"""
      # Stories links
      def test_stories_create_GET(self):
          self.client.force_login(self.superuser)
          response = self.client.get(self.stories_create_url)
          self.assertEqual(response.status_code, 200)
          self.assertTemplateUsed(response, 'stories/stories_create.html')

      def test_stories_list_GET(self):
          response = self.client.get(self.stories_list_url)
          self.assertEqual(response.status_code, 200)
          self.assertTemplateUsed(response, 'stories/stories_list.html')

      def test_stories_detail_GET(self):
          url = reverse('stories_detail', args=[self.test_story.category, self.test_story.slug])
          response = self.client.get(url)
          self.assertEqual(response.status_code, 200)
          self.assertTemplateUsed(response, 'stories/stories_detail.html')

      def test_stories_delete_GET(self):
          self.client.force_login(self.superuser)
          response = self.client.get(self.stories_delete_url)
          self.assertEqual(response.status_code, 200)
          self.assertTemplateUsed(response, 'stories/stories_delete.html')

      def test_stories_update_GET(self):
          self.client.force_login(self.superuser)
          response = self.client.get(self.stories_update_url)
          self.assertEqual(response.status_code, 200)
          self.assertTemplateUsed(response, 'stories/stories_.html')
"""