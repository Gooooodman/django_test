from django.views.generic import DetailView
from book.models import Publisher, Book
from django.shortcuts import get_object_or_404
from django.views.generic import ListView





class PublisherList(ListView):
    model = Publisher
    context_object_name = 'publisher_list'
    template_name = 'book/publisher_list.html'



# class PublisherDetail(DetailView):
#
#     model = Publisher
#     # template_name =  'book/books_by_publisher.html'
#     context_object_name = 'publisher'
#     queryset = Publisher.objects.all()
#
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super(PublisherDetail, self).get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context['book_list'] = Book.objects.all()
#         return context


#
# class PublisherDetail(DetailView):
#
#     context_object_name = 'publisher'
#     queryset = Publisher.objects.all()



# class BookList(ListView):
#     queryset = Book.objects.order_by('-publication_date')
#     context_object_name = 'book_list'

class PublisherBookList(ListView):
    model = Publisher
    context_object_name = 'publisher'
    template_name = 'book/books_by_publisher.html'

    def get_queryset(self):
        #self.publisher = get_object_or_404(Publisher, name=self.args[0])
        return Book.objects.filter(publisher=1)