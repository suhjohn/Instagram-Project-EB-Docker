import filecmp
import io
from random import randint

from PIL import Image
from django.contrib.auth import get_user_model
from django.core.files import File
from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APILiveServerTestCase, force_authenticate

from config.settings import STATICFILES_DIRS, STATIC_DIR
from post.apis import PostList
from post.models import Post

User = get_user_model()


class PostListViewTest(APILiveServerTestCase):
    URL_API_POST_LIST_NAME = 'api-post'
    URL_API_POST_LIST = '/api/post/'
    VIEW = PostList

    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    @staticmethod
    def create_user(username='dummy'):
        return User.objects.create_user(username=username)

    @staticmethod
    def create_post(author=None):
        Post.objects.create(author=author, photo=File(io.BytesIO()))

    def test_post_list_url_name_reverse(self):
        url = reverse(self.URL_API_POST_LIST_NAME)
        self.assertEqual(url, self.URL_API_POST_LIST)

    def test_post_list_url_resolve_view_class(self):
        """

        """
        resolver_match = resolve(self.URL_API_POST_LIST)
        self.assertEqual(
            resolver_match.url_name,
            self.URL_API_POST_LIST_NAME)
        self.assertEqual(
            resolver_match.func.view_class,
            self.VIEW.as_view().view_class)

    def test_get_post_list(self):
        """
        임의의 개수만큼 Post 생성, 해당 개수만큼 Response가 돌아오는지 확인
        """
        user = self.create_user()
        num = randint(0, 20)
        for i in range(num):
            self.create_post(author=user)

        url = reverse(self.URL_API_POST_LIST_NAME)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # response로 돌아온 json 길이가 입력한 개수와 동일한지 확인
        self.assertEqual(len(response.data), num)

        # object에 필드가 다 존재하는지 확인
        for i in range(num):
            current_post = response.data[i]
            self.assertIn('pk', current_post)

    def test_get_post_list_exclude_author(self):
        """
        author가 None인 Post가 postlist get 요청에서 제외되는지 확인
        :return:
        """
        user = self.create_user()
        num_author_none_posts = randint(0, 10)
        num_posts = randint(0, 10)
        for i in range(num_author_none_posts):
            self.create_post()
        for i in range(num_posts):
            self.create_post(author=user)

        response = self.client.get(self.URL_API_POST_LIST)
        self.assertEqual(len(response.data), num_posts)

    def test_create_post(self):
        """
        Post Create가 되는지 확인
        :return:
        """
        user= self.create_user()
        self.client.force_authenticate(user=user)
        photo = self.generate_photo_file()
        data = {
            "photo": photo,
        }
        response = self.client.post(self.URL_API_POST_LIST, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        print(response.data)
        post = Post.objects.get(pk=response.data['pk'])
        # 업로드 시도한 파일 == 파일

#
# """
# simple test to create a request and print the postlist
# # """
#
# factory = APIRequestFactory()
# request = factory.get('/api/post')
#
# view = PostList.as_view()
# response = view(request)
#
# pprint(response.data)

# """
# A real test case with creation of new db
# """
# class PostListViewTest(APILiveServerTestCase):
