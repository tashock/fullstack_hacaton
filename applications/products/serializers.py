from rest_framework import serializers
from applications.products.models import Category, Product, Rating, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate_title(self, title):
        if Category.objects.filter(title=title.lower()).exists():
            raise serializers.ValidationError('Такое название уже существует!')
        return title


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        product = Product.objects.create(**validated_data)

        files = request.FILES
        list_images = []
        for image in files.getlist('images'):
            list_images.append(Product(product=product, image=image))
        Product.objects.bulk_create(list_images)
        return product

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['likes'] = instance.likes.filter(like=True).count()
        return rep


class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Rating
        fields = ['rating']


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = '__all__'

