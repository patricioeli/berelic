from flask import Flask, render_template, request, redirect, url_for, flash
class categoria:
    def __init__(self):
        self.__idCat=0
        self.__nomCat="A"
    @property
    def idCat(self):
        return self.__idCat
    @idCat.setter
    def idCat(self,idCat):
        self.__idCat=idCat
    @property
    def nomCat(self):
        return self.__nomCat
    @nomCat.setter
    def nomCat(self,nomCat):
        self.__nomCat=nomCat
