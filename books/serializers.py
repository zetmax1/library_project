from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle','description', 'author','isbn', 'price')

    def validate(self, data):
        title = data.get('title')
        author = data.get('author')
        isbn = data.get('isbn')

        if not title.isalpha() or not author.isalpha():
            raise serializers.ValidationError({
                'status': False,
                'message': 'Title should be a string',
            })

        if Book.objects.filter(title=title, author=author, isbn=isbn).exists():
            raise serializers.ValidationError({
                'status': False,
                'message': 'you cannot add the same book twice',
            })
        return data

    # def validate_title(self, value):
    #     if not isinstance(value, str):
    #         raise serializers.ValidationError({
    #             'status': False,
    #             'message': 'Title must be a string'
    #         })
    #     return value
    #
    # def validate_author(self, value):
    #     if not isinstance(value, str):
    #         raise serializers.ValidationError({
    #             'status': False,
    #             'message': 'Author must be a string'
    #         })
    #     return value

    def validate_price(self, price):
        if price <= 0 or price is None or price > 9999999999:
            raise serializers.ValidationError({
                'status': False,
                'message': 'Please enter a valid price',
            })
        return price
