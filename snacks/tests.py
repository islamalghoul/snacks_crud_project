from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.
from django.test import SimpleTestCase
from django.urls import reverse
from .models import Snack


class SnacksTest(TestCase):
    def tests_home_page_status(self):
        url = reverse('snack')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_home_page_template(self):
        url = reverse('snack')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'Home.html')

    def setUp(self):
        self.user=get_user_model().objects.create_user(

            username='test',
            email='test@test.com',
            password='123'
        )
        self.Snack=Snack.objects.create(
            title='test',
            purchaser=self.user,
            discreption='test'

        )
    def test_str(self):
        self.assertEqual(str(self.Snack),'test')    
    def test_snack_detail(self):
        url= reverse('SnackList',kwargs={'pk':self.Snack.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_detail_template(self):
        url = reverse('SnackList',kwargs={'pk':self.Snack.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_detail.html')
    def test_create(self):
        url=reverse("Create")
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
    def test_create_template(self):
        url = reverse('Create')
        response = self.client.post(url)
        self.assertTemplateUsed(response, 'create.html')
    def test_Update(self):
        url=reverse('Update',kwargs={'pk':self.Snack.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
    def test_Update_template(self):
        url=reverse('Update',kwargs={'pk':self.Snack.pk})
        response = self.client.post(url)
        self.assertTemplateUsed(response, 'update.html')


    # def test_Delete(self):
    #     url=reverse('Delete',kwargs={'pk':self.Snack.pk})
    #     response = self.client.post(url)
    #     self.assertEqual(response.status_code, 200)
    # def test_delete_template(self):
    #     url=reverse('Delete',kwargs={'pk':self.Snack.pk})
    #     response = self.client.post(url)
    #     self.assertTemplateUsed(response, 'snack_detail.html')