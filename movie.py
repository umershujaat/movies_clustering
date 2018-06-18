# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 12:03:49 2018

@author: urabbani
"""

import webbrowser
class Movies():
    """This is a class for storing movies and their attributes"""
    GENRES = ["Action", "Comedy", "Horror", "Romance","Fantasy"]
    def __init__(self, movie_title, movie_genre, movie_rating):
        self.title = movie_title
        self.genre = movie_genre
        self.rating = movie_rating


    