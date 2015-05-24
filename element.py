__author__ = 'thker'
class Topnav:

    def __init__(self,name,cls,vau,url):
        self.cls =cls
        self.id=name
        self.vau=vau
        self.url=url

    def getstr(self):
        innerhtml='<div class="' + self.cls +'" '\
                  + 'id="' +self.id +'">' \
                  '<ul>' \
                  '<li>' \
                  '<a href="'+self.url+'">'+self.vau+'</a>' \
                  '</li>' \
                  '</ul>' \
                  '</div>'
        return innerhtml


#
# class left-nav():
#     pass
#
# class right-mini-nva():
#     pass
#
# class right-nav():
#     pass
#
# class right-content():
#     pass
#


