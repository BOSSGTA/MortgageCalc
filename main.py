from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.tab import MDTabsBase
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.font_definitions import fonts
from kivymd.icon_definitions import md_icons

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
import requests
from bs4 import BeautifulSoup

test = '123'

KV = '''
# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/logo/kivy-icon-256.png"

    MDLabel:
        text: "KivyMD library"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: "kivydevelopment@gmail.com"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:

        DrawerList:
            id: md_list



Screen:

    MDNavigationLayout:

        ScreenManager:

            Screen:
                MDLabel:
                    text: '123'

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Mortgage"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                    
                                        
                    MDTabs:
                        id: tabs

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer
            
            
'''

class Tab(MDFloatLayout, MDTabsBase):
    pass

class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

bitcoin = 'https://www.google.com/finance/quote/BTC-RUB?sa=X&ved=2ahUKEwjHyN3hqqX0AhVjtIsKHX6ABroQ' \
              '-fUHegQIShAS '
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/89.0.4389.114 Safari/537.36'}

full_page = requests.get(bitcoin, headers=headers)

soup = BeautifulSoup(full_page.content, 'html.parser')

convert = soup.find("div", class_="YMlKec fxKbKc").text

class MortgageApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        icons_item = {
            "folder": "My files",
            "account-multiple": "Shared with me",
            "star": convert,
            "history": "Recent",
            "checkbox-marked": "Shared with me",
            "upload": "Upload",
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )
        # for name_tab in list(md_icons.keys())[15:30]:
        #     self.root.ids.tabs.add_widget(Tab(icon=name_tab, title=name_tab))

        for icon_name, name_tab in icons_item.items():
            self.root.ids.tabs.add_widget(
                Tab(text=f"[ref={name_tab}][font={fonts[-1]['fn_regular']}]{md_icons[icon_name]}[/font][/ref] {name_tab}")
            )


MortgageApp().run()