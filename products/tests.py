from rest_framework import status
from rest_framework.test import APITestCase

from .models import Product


class ProductListCreateAPITest(APITestCase):
	def test_get_returns_products(self):
		product = Product.objects.create(
			title='Наушники Sony WH-1000XM5',
			description='Беспроводные наушники с шумоподавлением',
			price='34990.00',
			quantity=5,
		)

		response = self.client.get('/api/v1/products/')

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data[0]['id'], product.id)
		self.assertEqual(response.data[0]['title'], product.title)
		self.assertEqual(response.data[0]['price'], '34990.00')
