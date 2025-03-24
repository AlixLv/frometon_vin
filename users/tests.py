from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

class UsersTests(TestCase):
    
    def setUp(self):
        # créer un utilisateur de test
        User = get_user_model()
        self.user = User.objects.create_user(
            username= "testuser", 
            email="normal@user.com", 
            password="foo"
            )
    
    def test_create_user(self):
        User = get_user_model()
       
        # vérifier que le user a été créé correctement
        self.assertEqual(self.user.email, "normal@user.com")
        self.assertEqual(self.user.username, "testuser")
       
       # tester la création avec des valeurs invalides
        with self.assertRaises(ValueError):
            User.objects.create_user(username="", email="test@example.com", password="foo")
        
        with self.assertRaises(ValueError):
            User.objects.create_user(username="test2", email="", password="foo")    

    def test_authenticate_user_using_login(self):
        # connexion du user
        login_successful = self.client.login(username= "testuser", email="normal@user.com", password="foo")
        self.assertTrue(login_successful)
        
        # vérifier si user connecté a bien accès à la homepage
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        
    def test_user_get_profile(self):
        login_successful = self.client.login(username= "testuser", email="normal@user.com", password="foo")
        self.assertTrue(login_successful)
        
        response = self.client.get('/users/profile/{}'.format(self.user.id), follow=True, HTTP_ACCEPT ='application/json')
        # print("🟣 ", response.status_code)
        # print(response.context)
        # print("🟡 ", response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['username'], 'testuser')
        self.assertEqual(response.context['email'], 'normal@user.com')