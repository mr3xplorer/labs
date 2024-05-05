class WelcomeController < ApplicationController
    def index
    end
  
    def greet
      @username = params[:username]
    end
  end