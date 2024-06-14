from django.test import TestCase

# Create your tests here.
from restaurant.models import Menu

#Create a menu item called
#menu_item = Greek salad
#price = 6
#inventory = 18
class MenuItemTest(TestCase):
    def test_create_item(self):
        item = Menu.objects.create(menu_item="Greek salad", price=6, inventory=18)
        self.assertEqual(str(item), "Greek salad: 6")
        self.assertEqual(item.menu_item, "Greek salad")
        self.assertEqual(item.price, 6)
        self.assertEqual(item.inventory, 18)

#Setup a menu item called
#menu_item = Pasta
#price = 11.25
#inventory = 25
class MenuViewTest(TestCase):
    def setUp(self):
        self.pasta_item = Menu.objects.create(menu_item = "Pasta", price = 11.25, inventory = 25)

    def test_get_item(self):
        item = Menu.objects.get(id = self.pasta_item.id)
        self.assertEqual(item.menu_item, "Pasta")
        self.assertEqual(item.price, 11.25)
        self.assertEqual(item.inventory, 25)

    def test_getall(self):
        self.assertEqual(Menu.objects.count(),1)