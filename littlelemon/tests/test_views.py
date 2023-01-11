from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        item1 = Menu.objects.create(title="Chocolate Cake", price=500, inventory = 3)
        item1.save()
        item2 = Menu.objects.create(title="Bacon and Eggs", price=300, inventory = 4)
        item2.save()
    def test_getall(self):
        items = Menu.objects.all()
        self.assertEqual(items.count(), 2)

        item_dict = [
            {
                'title' : 'Chocolate Cake',
                'price' : 500.00,
                'inventory' : 3
            },
            {
                'title' : 'Bacon and Eggs',
                'price' : 300.00,
                'inventory' : 4
            },
        ]
        for count, item in enumerate(items):
            serialized_item = MenuItemSerializer(item)
            self.assertEqual(serialized_item.data['title'], item_dict[count]['title'])
            self.assertEqual(float(serialized_item.data['price']), item_dict[count]['price'])
            self.assertEqual(float(serialized_item.data['inventory']), item_dict[count]['inventory'])

