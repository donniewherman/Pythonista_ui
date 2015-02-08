# click the button to put a snapshot of a webpage onto the clipboard

import clipboard, ui

html = '''<html>
  <head>
    <title>my html</title>
  </head>
  <body>
    <h1>h1</h1>
    <h2>h2</h2>
    <h3>h3</h3>
    This is <b>bold</b> text.
  </body>
</html>'''
    
class ScreenshotView(ui.View):
    def __init__(self):
        self.present()
        self.add_subview(self.make_button())
        self.add_subview(self.make_webview(html))

    def get_shapshot(self):
        with ui.ImageContext(self.width, self.height) as context:
            self.draw_snapshot()
            return context.get_image()

    def screenshot_action(self, sender):
        print('Saving a screenshot to the clipboard.')
        clipboard.set_image(self.get_shapshot())

    def make_button(self):
        button = ui.Button(name='button', title='Save a screenshot to the clipboard')
        button.action = self.screenshot_action
        button.width  = self.width
        return button

    #def make_webview(self, url='http://apple.com'):
    #    wv = ui.WebView(name='webview', title=url, frame=self.bounds)
    #    wv.load_url(url)
    def make_webview(self, html=html):
        wv = ui.WebView(name='webview', title='ScreenshotWebView', frame=self.bounds)
        wv.load_html(html)
        offset = self['button'].height
        wv.y      += offset
        wv.height -= offset
        wv.border_color = (0, 0, 1)
        wv.border_width = 2
        return wv

view = ScreenshotView()
