from django.test import SimpleTestCase
from Ap.forms import CommentForm

class TestCommentForm(SimpleTestCase):
    
    def test_comment_form_valid_data(self):
        form = CommentForm(data={
            'nazwa' : 'gabriela',
            'tresc' : 'test',          
        })
        
        self.assertTrue(form.is_valid())