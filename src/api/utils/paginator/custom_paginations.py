from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    """
    Using this method requires calling the 'paginate_queryset' method before.
    Keep in mind that for the operation, you need to pass the request response
    already 'mounted', here will only be made the spread based on the data informed.
    """

    def get_paginated_response(self, data):
        return {
            **data,
            **{
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
                'count': self.page.paginator.count,
            }
        }
