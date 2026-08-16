from cinema.models import Actor, Genre, CinemaHall, Movie, MovieSession
from rest_framework import serializers

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = '__all__'

class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")

class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(slug_field = 'name', many=True, read_only=True)
    actors = serializers.SlugRelatedField(slug_field = 'name', read_only=True)

    class Meta:
        fields = ("id", "title", "description", "duration", "genres", "actors")

class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")

class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.ReadOnlyField(source='movie.title')
    cinema_hall_name = serializers.ReadOnlyField(source='cinema.hall.name')
    cinema_hall_capacity = serializers.ReadOnlyField(source='cinema.hall.capacity')

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity"
        )

class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieDetailSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")
