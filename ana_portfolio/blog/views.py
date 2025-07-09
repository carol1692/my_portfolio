from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.


dict_blog = {
            "1":{
                "author":"Ana",
                "title": "Lorem Ipsum post 1",
                "subtitle": "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",
                "text":""" Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus at ante volutpat, aliquam risus quis, elementum mi. Mauris vulputate mauris id pharetra malesuada. Pellentesque finibus ultrices malesuada. Etiam vehicula, ligula lacinia semper euismod, turpis metus sodales erat, eu porttitor est justo vitae tellus. In nec lacinia odio. Ut neque dolor, scelerisque ac semper semper, blandit et mauris. Pellentesque sed suscipit mauris. Integer pharetra velit eget quam bibendum tincidunt. Morbi vehicula nulla ut lacus venenatis sollicitudin ac a justo. Fusce quis nulla urna. Vivamus velit mauris, rhoncus ut tristique a, tristique tincidunt tortor. Quisque rutrum pharetra quam id ornare. Aliquam a justo eu lorem facilisis convallis vitae in nisl. Sed erat lectus, imperdiet et dictum in, laoreet sit amet nunc. Phasellus tellus mi, imperdiet vitae arcu ut, hendrerit tempus orci. Integer at blandit purus.

                    Etiam eget tempor ipsum, dignissim dignissim mi. Curabitur ac libero et ligula blandit commodo vel ac ex. Interdum et malesuada fames ac ante ipsum primis in faucibus. Cras mollis mattis purus nec cursus. Morbi mollis tortor leo, a faucibus sapien ultricies non. Aenean vulputate auctor magna, ac fermentum dui gravida a. Donec non placerat metus. Etiam vitae elit massa. Mauris laoreet quam neque, sed hendrerit enim pharetra non. Proin auctor ornare vestibulum. Suspendisse id nisi vitae arcu finibus efficitur. Fusce pretium ante a nulla aliquet bibendum. Cras luctus varius nibh, ac accumsan turpis. Nulla eu neque ultrices, tempor velit nec, pharetra metus. Aliquam volutpat pellentesque finibus.

                    Morbi vitae urna sit amet ex posuere interdum. Nulla bibendum porttitor bibendum. Vestibulum pellentesque vel magna vel fringilla. Praesent sagittis condimentum neque, a semper ante dapibus nec. Vivamus volutpat nisi eu elementum congue. Donec nec aliquam lacus. Sed felis ipsum, aliquam ut efficitur in, aliquet ut nisl.

                    Maecenas nulla massa, volutpat placerat est a, convallis malesuada elit. Suspendisse blandit ut sapien nec volutpat. Donec in metus et mi fermentum tempor id ut purus. Mauris varius placerat felis, sed mollis erat sodales at. Fusce imperdiet rhoncus metus, vel porta est facilisis ac. Curabitur lacinia mauris tempus lectus vestibulum placerat. Mauris ac ante finibus, tempus sapien a, rutrum felis. Aenean efficitur mauris quis lectus fermentum scelerisque. Vivamus id blandit magna. In hac habitasse platea dictumst. Donec hendrerit neque arcu, sit amet faucibus quam vulputate a. Etiam et risus nec augue tincidunt aliquam. Proin ac turpis in sapien venenatis accumsan efficitur vel urna. Donec convallis, augue id scelerisque consequat, sem mi imperdiet neque, quis tincidunt diam justo vitae eros. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Pellentesque in pretium ex, eu placerat lorem.
                """
            },
            "2":{
                "author":"Ana",
                "title": "Lorem Ipsum post 2",
                "subtitle": "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",
                "text":""" Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus at ante volutpat, aliquam risus quis, elementum mi. Mauris vulputate mauris id pharetra malesuada. Pellentesque finibus ultrices malesuada. Etiam vehicula, ligula lacinia semper euismod, turpis metus sodales erat, eu porttitor est justo vitae tellus. In nec lacinia odio. Ut neque dolor, scelerisque ac semper semper, blandit et mauris. Pellentesque sed suscipit mauris. Integer pharetra velit eget quam bibendum tincidunt. Morbi vehicula nulla ut lacus venenatis sollicitudin ac a justo. Fusce quis nulla urna. Vivamus velit mauris, rhoncus ut tristique a, tristique tincidunt tortor. Quisque rutrum pharetra quam id ornare. Aliquam a justo eu lorem facilisis convallis vitae in nisl. Sed erat lectus, imperdiet et dictum in, laoreet sit amet nunc. Phasellus tellus mi, imperdiet vitae arcu ut, hendrerit tempus orci. Integer at blandit purus.

                    Etiam eget tempor ipsum, dignissim dignissim mi. Curabitur ac libero et ligula blandit commodo vel ac ex. Interdum et malesuada fames ac ante ipsum primis in faucibus. Cras mollis mattis purus nec cursus. Morbi mollis tortor leo, a faucibus sapien ultricies non. Aenean vulputate auctor magna, ac fermentum dui gravida a. Donec non placerat metus. Etiam vitae elit massa. Mauris laoreet quam neque, sed hendrerit enim pharetra non. Proin auctor ornare vestibulum. Suspendisse id nisi vitae arcu finibus efficitur. Fusce pretium ante a nulla aliquet bibendum. Cras luctus varius nibh, ac accumsan turpis. Nulla eu neque ultrices, tempor velit nec, pharetra metus. Aliquam volutpat pellentesque finibus.

                    Morbi vitae urna sit amet ex posuere interdum. Nulla bibendum porttitor bibendum. Vestibulum pellentesque vel magna vel fringilla. Praesent sagittis condimentum neque, a semper ante dapibus nec. Vivamus volutpat nisi eu elementum congue. Donec nec aliquam lacus. Sed felis ipsum, aliquam ut efficitur in, aliquet ut nisl.

                    Maecenas nulla massa, volutpat placerat est a, convallis malesuada elit. Suspendisse blandit ut sapien nec volutpat. Donec in metus et mi fermentum tempor id ut purus. Mauris varius placerat felis, sed mollis erat sodales at. Fusce imperdiet rhoncus metus, vel porta est facilisis ac. Curabitur lacinia mauris tempus lectus vestibulum placerat. Mauris ac ante finibus, tempus sapien a, rutrum felis. Aenean efficitur mauris quis lectus fermentum scelerisque. Vivamus id blandit magna. In hac habitasse platea dictumst. Donec hendrerit neque arcu, sit amet faucibus quam vulputate a. Etiam et risus nec augue tincidunt aliquam. Proin ac turpis in sapien venenatis accumsan efficitur vel urna. Donec convallis, augue id scelerisque consequat, sem mi imperdiet neque, quis tincidunt diam justo vitae eros. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Pellentesque in pretium ex, eu placerat lorem.
                """
                
            },
            "3":{
                "author":"Ana",
                "title": "Lorem Ipsum post 3",
                "subtitle": "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",
                "text":""" Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus at ante volutpat, aliquam risus quis, elementum mi. Mauris vulputate mauris id pharetra malesuada. Pellentesque finibus ultrices malesuada. Etiam vehicula, ligula lacinia semper euismod, turpis metus sodales erat, eu porttitor est justo vitae tellus. In nec lacinia odio. Ut neque dolor, scelerisque ac semper semper, blandit et mauris. Pellentesque sed suscipit mauris. Integer pharetra velit eget quam bibendum tincidunt. Morbi vehicula nulla ut lacus venenatis sollicitudin ac a justo. Fusce quis nulla urna. Vivamus velit mauris, rhoncus ut tristique a, tristique tincidunt tortor. Quisque rutrum pharetra quam id ornare. Aliquam a justo eu lorem facilisis convallis vitae in nisl. Sed erat lectus, imperdiet et dictum in, laoreet sit amet nunc. Phasellus tellus mi, imperdiet vitae arcu ut, hendrerit tempus orci. Integer at blandit purus.

                    Etiam eget tempor ipsum, dignissim dignissim mi. Curabitur ac libero et ligula blandit commodo vel ac ex. Interdum et malesuada fames ac ante ipsum primis in faucibus. Cras mollis mattis purus nec cursus. Morbi mollis tortor leo, a faucibus sapien ultricies non. Aenean vulputate auctor magna, ac fermentum dui gravida a. Donec non placerat metus. Etiam vitae elit massa. Mauris laoreet quam neque, sed hendrerit enim pharetra non. Proin auctor ornare vestibulum. Suspendisse id nisi vitae arcu finibus efficitur. Fusce pretium ante a nulla aliquet bibendum. Cras luctus varius nibh, ac accumsan turpis. Nulla eu neque ultrices, tempor velit nec, pharetra metus. Aliquam volutpat pellentesque finibus.

                    Morbi vitae urna sit amet ex posuere interdum. Nulla bibendum porttitor bibendum. Vestibulum pellentesque vel magna vel fringilla. Praesent sagittis condimentum neque, a semper ante dapibus nec. Vivamus volutpat nisi eu elementum congue. Donec nec aliquam lacus. Sed felis ipsum, aliquam ut efficitur in, aliquet ut nisl.

                    Maecenas nulla massa, volutpat placerat est a, convallis malesuada elit. Suspendisse blandit ut sapien nec volutpat. Donec in metus et mi fermentum tempor id ut purus. Mauris varius placerat felis, sed mollis erat sodales at. Fusce imperdiet rhoncus metus, vel porta est facilisis ac. Curabitur lacinia mauris tempus lectus vestibulum placerat. Mauris ac ante finibus, tempus sapien a, rutrum felis. Aenean efficitur mauris quis lectus fermentum scelerisque. Vivamus id blandit magna. In hac habitasse platea dictumst. Donec hendrerit neque arcu, sit amet faucibus quam vulputate a. Etiam et risus nec augue tincidunt aliquam. Proin ac turpis in sapien venenatis accumsan efficitur vel urna. Donec convallis, augue id scelerisque consequat, sem mi imperdiet neque, quis tincidunt diam justo vitae eros. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Pellentesque in pretium ex, eu placerat lorem.
                """
                
            },
            "4":{
                "author":"Ana",
                "title": "Lorem Ipsum post 4",
                "subtitle": "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...",
                "text":""" Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus at ante volutpat, aliquam risus quis, elementum mi. Mauris vulputate mauris id pharetra malesuada. Pellentesque finibus ultrices malesuada. Etiam vehicula, ligula lacinia semper euismod, turpis metus sodales erat, eu porttitor est justo vitae tellus. In nec lacinia odio. Ut neque dolor, scelerisque ac semper semper, blandit et mauris. Pellentesque sed suscipit mauris. Integer pharetra velit eget quam bibendum tincidunt. Morbi vehicula nulla ut lacus venenatis sollicitudin ac a justo. Fusce quis nulla urna. Vivamus velit mauris, rhoncus ut tristique a, tristique tincidunt tortor. Quisque rutrum pharetra quam id ornare. Aliquam a justo eu lorem facilisis convallis vitae in nisl. Sed erat lectus, imperdiet et dictum in, laoreet sit amet nunc. Phasellus tellus mi, imperdiet vitae arcu ut, hendrerit tempus orci. Integer at blandit purus.

                    Etiam eget tempor ipsum, dignissim dignissim mi. Curabitur ac libero et ligula blandit commodo vel ac ex. Interdum et malesuada fames ac ante ipsum primis in faucibus. Cras mollis mattis purus nec cursus. Morbi mollis tortor leo, a faucibus sapien ultricies non. Aenean vulputate auctor magna, ac fermentum dui gravida a. Donec non placerat metus. Etiam vitae elit massa. Mauris laoreet quam neque, sed hendrerit enim pharetra non. Proin auctor ornare vestibulum. Suspendisse id nisi vitae arcu finibus efficitur. Fusce pretium ante a nulla aliquet bibendum. Cras luctus varius nibh, ac accumsan turpis. Nulla eu neque ultrices, tempor velit nec, pharetra metus. Aliquam volutpat pellentesque finibus.

                    Morbi vitae urna sit amet ex posuere interdum. Nulla bibendum porttitor bibendum. Vestibulum pellentesque vel magna vel fringilla. Praesent sagittis condimentum neque, a semper ante dapibus nec. Vivamus volutpat nisi eu elementum congue. Donec nec aliquam lacus. Sed felis ipsum, aliquam ut efficitur in, aliquet ut nisl.

                    Maecenas nulla massa, volutpat placerat est a, convallis malesuada elit. Suspendisse blandit ut sapien nec volutpat. Donec in metus et mi fermentum tempor id ut purus. Mauris varius placerat felis, sed mollis erat sodales at. Fusce imperdiet rhoncus metus, vel porta est facilisis ac. Curabitur lacinia mauris tempus lectus vestibulum placerat. Mauris ac ante finibus, tempus sapien a, rutrum felis. Aenean efficitur mauris quis lectus fermentum scelerisque. Vivamus id blandit magna. In hac habitasse platea dictumst. Donec hendrerit neque arcu, sit amet faucibus quam vulputate a. Etiam et risus nec augue tincidunt aliquam. Proin ac turpis in sapien venenatis accumsan efficitur vel urna. Donec convallis, augue id scelerisque consequat, sem mi imperdiet neque, quis tincidunt diam justo vitae eros. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Pellentesque in pretium ex, eu placerat lorem.
                """
               },
            
        }



#index blog - latest posts and welcome message
def index_blog(request):
    index_posts = dict(sorted(dict_blog.items(), key=lambda x: x[0], reverse=True)[:3])
    return HttpResponse(render(request, "blog/index.html", {'posts':index_posts}))

#this page will load list of all post blog
def posts_blog(request):
    return HttpResponse(render(request, "blog/list_posts.html", {'posts':dict_blog}))

#this page will load the post choosen
def post(request, id):
    return HttpResponse(render(request, "blog/post.html",{'post':dict_blog[f"{id}"]}))

class CreateProfileView(View):
    def get(self, request):
        return render(request, "blog/upload.html")

    def post(self, request):
        print(request.FILES["upload_input"])
        return render(request, "blog/upload.html")
